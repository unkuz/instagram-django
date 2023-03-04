import os
from ..constants.file import MAX_FILE_SIZE_VIDEO, MAX_FILE_SIZE_IMAGE


def is_video(file):
    if file.size > MAX_FILE_SIZE_VIDEO:
        return False
    if os.path.splitext(file.name)[1] not in ['.mp4', '.avi', '.mov']:
        return False
    return True
        


def is_image(file):
    if file.size > MAX_FILE_SIZE_IMAGE:
        return False
    if os.path.splitext(file.name)[1] not in ['.jpg', '.jpeg', '.png']:
        return False
    return True