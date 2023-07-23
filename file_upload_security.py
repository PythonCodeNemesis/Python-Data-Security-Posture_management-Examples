import magic
# Validate uploaded file against a whitelist of allowed file types
def validate_uploaded_file(file_path):
    allowed_file_types = ["image/jpeg", "image/png"]
    file_type = magic.from_file(file_path, mime=True)
    return file_type in allowed_file_types
# Usage example
uploaded_file = "/path/to/uploaded/file.jpg"
is_valid = validate_uploaded_file(uploaded_file)
print("Is the uploaded file valid?", is_valid)
