import boto3



def assume_full_access_role(accountid, user):
 """
 start assume session role with full access profile for the provided account ID with user
 """
 print("Creating custom Assumerole Session")
 boto_session_original = boto3.Session(
 profile_name="identity", region_name="<default region name>"
 )
 mfa_1 = input("Enter MFA Code: ")
 sts_connection = boto_session_original.client("sts")
 aws_account_from_id = accountid
 assumedRoleObject1 = sts_connection.assume_role(
 DurationSeconds=3600,
 RoleArn="arn:aws:iam::"
 + str(aws_account_from_id)
 + ":role/LandingZone/FullAccess",
 RoleSessionName="AssumeRoleSessionFrom",
 SerialNumber="arn:aws:iam::<AWS_MFA_ACCOUNT_NUMBER>:mfa/" + user,
 TokenCode=mfa_1,
 )
 credentialsfrom = assumedRoleObject1["Credentials"]
 session = boto3.session.Session(
 aws_access_key_id=credentialsfrom["AccessKeyId"],
 aws_secret_access_key=credentialsfrom["SecretAccessKey"],
 aws_session_token=credentialsfrom["SessionToken"],
 )
 return session