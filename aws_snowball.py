import boto3


def create_job(access, secret):
    jobtype = input("Enter Job type -> Import / Export:\t")
    manifest = input("Enter manifest data:\t")
    validate = input("Validate only-> True / False:\t")
    client = boto3.client('importexport', aws_access_key_id=access,
                          aws_secret_access_key=secret)
    details = client.creat_job(JobType=jobtype, Manifest=manifest, ValidateOnly=validate, APIVersion="2012-10-17")
    print(details["JobId"])
    print(details["WarningMessage"])


def cancle_job(access, secret):
    client = boto3.client('importexport', aws_access_key_id=access,
                          aws_secret_access_key=secret)
    jobid = input("Enter Job ID:\t")
    print(client.cancel_job(JobId=jobid, APIVersion="2012-10-17"))


def get_job_list(access, secret):
    client = boto3.client('importexport', aws_access_key_id=access,
                          aws_secret_access_key=secret)
    job = client.list_jobs(MaxJobs=1,
                           APIVersion="2012-10-17")["Jobs"]
    if len(job) == 0:
        print("no job available!\n\n")
    else:
        print(job)
        print("\n\n")


def job_status(access, secret):
    client = boto3.client('importexport', aws_access_key_id=access,
                          aws_secret_access_key=secret)
    jobid = input("Enter Job ID:\t")
    print(client.get_status(JobId=jobid, APIVersion="2012-10-17"))


def credentials():
    access = input("Enter your access key:\t")
    secret = input("Enter your secret key:\t")
    return access, secret

def main():
    access, secret = credentials()
    while True:
        print("1.Create Job\n2.Get Job list\n3.Get Job Status\n4.Cancel a Job\n5.Exit")
        i = int(input("Enter the operation no:\t"))
        if i == 1:
            create_job(access, secret)
        elif i == 2:
            get_job_list(access, secret)
        elif i == 3:
            get_job_list(access, secret)
        elif i == 4:
            cancle_job(access, secret)
        elif i == 5:
            exit()
        else:
            continue


if __name__ == '__main__':
    main()
