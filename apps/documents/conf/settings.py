import datetime
import hashlib
import uuid

from django.conf import settings
from django.contrib.auth.models import User


default_available_functions = {
    'current_date':datetime.datetime.now().date,
}

default_available_models = {
    'User':User
}

# Definition
AVAILABLE_FUNCTIONS = getattr(settings, 'DOCUMENTS_METADATA_AVAILABLE_FUNCTIONS', default_available_functions)
AVAILABLE_MODELS = getattr(settings, 'DOCUMENTS_METADATA_AVAILABLE_MODELS', default_available_models)
# Upload
USE_STAGING_DIRECTORY = getattr(settings, 'DOCUMENTS_USE_STAGING_DIRECTORY', False)
STAGING_DIRECTORY = getattr(settings, 'DOCUMENTS_STAGING_DIRECTORY', u'/tmp/mayan/staging')
DELETE_STAGING_FILE_AFTER_UPLOAD = getattr(settings, 'DOCUMENTS_DELETE_STAGING_FILE_AFTER_UPLOAD', False)
DELETE_LOCAL_ORIGINAL = getattr(settings, 'DOCUMENTS_DELETE_LOCAL_ORIGINAL', False)
# Saving
CHECKSUM_FUNCTION = getattr(settings, 'DOCUMENTS_CHECKSUM_FUNCTION', lambda x: hashlib.sha256(x).hexdigest())
UUID_FUNCTION = getattr(settings, 'DOCUMENTS_UUID_FUNTION', lambda:unicode(uuid.uuid4()))
# Storage
STORAGE_DIRECTORY_NAME = getattr(settings, 'DOCUMENTS_STORAGE_DIRECTORY_NAME', 'documents')
# Serving
FILESERVING_PATH = getattr(settings, 'DOCUMENTS_FILESERVING_PATH', u'/tmp/mayan/documents')
SLUGIFY_PATH = getattr(settings, 'DOCUMENTS_SLUGIFY_PATH', False)
