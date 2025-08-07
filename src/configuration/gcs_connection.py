from google.cloud import storage


def write_gcs_file(bucket_name, file_path, content):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_path)
    blob.upload_from_string(content)
    print(f"File written to gs://{bucket_name}/{file_path}")

# Usage
# write_gcs_file("my-bucket-name", "output/test.txt", "This isa test content.")

def read_gcs_file(bucket_name, file_path):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_path)
    content = blob.download_as_text()
    return content

# Usage
# content = read_gcs_file("my-bucket-name", "path/to/file.txt")
# print(content)
