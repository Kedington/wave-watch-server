import uuid

ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}


# Generate a unique file name with uuid.uuid1() and the extension of the file
def generate_filename(filename):
    return filename.replace(filename.rsplit('.', 1)[0], str(uuid.uuid1()))


# Verify that the filename has a valid extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
