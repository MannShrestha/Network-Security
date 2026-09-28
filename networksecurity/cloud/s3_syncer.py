
# import os


# class S3Sync:
#     def sync_folder_to_s3(self,folder,aws_bucket_url):
#         command = f"aws s3 sync {folder} {aws_bucket_url} "
#         os.system(command)

#     def sync_folder_from_s3(self,folder,aws_bucket_url):
#         command = f"aws s3 sync  {aws_bucket_url} {folder} "
#         os.system(command)


import os


class S3Sync:

    @staticmethod
    def _endpoint_flag():
        """
        Returns an --endpoint-url flag pointing at Floci if AWS_ENDPOINT_URL
        is set in the environment, otherwise returns an empty string so the
        command falls back to real AWS.
        """
        endpoint = os.getenv("AWS_ENDPOINT_URL")
        return f"--endpoint-url {endpoint} " if endpoint else ""

    def sync_folder_to_s3(self, folder, aws_bucket_url):
        command = f"aws s3 sync {self._endpoint_flag()}{folder} {aws_bucket_url} "
        os.system(command)

    def sync_folder_from_s3(self, folder, aws_bucket_url):
        command = f"aws s3 sync {self._endpoint_flag()}{aws_bucket_url} {folder} "
        os.system(command)