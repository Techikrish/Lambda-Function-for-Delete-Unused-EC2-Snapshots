## The function identifies snapshots that are no longer needed and removes them, helping you manage your AWS resources efficiently.
 
### Prerequisites - 
**Lambda Function Timeout**: Set the function timeout to **10 seconds** to ensure efficient execution

**IAM Policy Permissions** Create an IAM policy with the following permissions for your Lambda function’s execution role:

    -     `ec2:DescribeInstances`
    - -   `ec2:DescribeSnapshots`
    - -   `ec2:DescribeVolumes`
    - -   `ec2:DeleteSnapshot`

