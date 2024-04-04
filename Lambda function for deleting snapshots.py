import boto3

def lambda_handler(event, context):
  # Configure boto3 session
  ec2_client = boto3.client('ec2')
  snapshot_client = boto3.client('ec2')

  # Get all snapshots
  snapshots = snapshot_client.describe_snapshots(OwnerIds=['self'])['Snapshots']

  # Iterate through snapshots
  for snapshot in snapshots:
    # Get snapshot ID
    snapshot_id = snapshot['SnapshotId']
    
    # Get all EC2 instances
    instances = ec2_client.describe_instances()["Reservations"]
    
    # Flag to track snapshot usage
    used_snapshot = False

    # Check if snapshot is attached to any running instance
    for reservation in instances:
      for instance in reservation.get('Instances', []):
        # Check for snapshot in block device mappings (handle missing key)
        block_devices = instance.get('BlockDevices', [])
        for block_device in block_devices:
          if block_device.get('SnapshotId', None) == snapshot_id:
            used_snapshot = True
            break
        # Break if snapshot found
        if used_snapshot:
          break
    
    # Delete unused snapshot
    if not used_snapshot:
      print(f"Deleting unused snapshot: {snapshot_id}")
      snapshot_client.delete_snapshot(SnapshotId=snapshot_id)

  return {'message': 'Snapshot cleanup completed'}
