"""
extra settings for flask api configurations
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
from os.path import isdir, join as joinpath

BASE_DIR = Path(__file__).resolve().parent

UPLOADS_DIR = joinpath(BASE_DIR, "uploads")
ASSETS_DIR = joinpath(BASE_DIR, "assets")
FILTERS_DIR = joinpath(BASE_DIR, "filters")

def create_directory(folder_name):
    """ Create new directory """
    if not isdir(folder_name):
        os.mkdir(folder_name)


def recreate_uploads_dir():
    """ Recreate the entire uploads directory """
    try:
        shutil.rmtree(joinpath(UPLOADS_DIR)),
    except Exception as error:
        print(error)
    create_directory("uploads")
    try:
        shutil.copy(
            joinpath(ASSETS_DIR, "sample.jpeg"), joinpath(UPLOADS_DIR, "sample.jpeg")
        )
    except Exception as error:
        print(error)

# creaing uploads directry
create_directory('uploads')

""" Json data """
title = "Corrosion Detection"
api_version = "0.0.1-alpha"
base_url = "localhost:8000"
documentation_url = "/docs"
current_time = datetime.utcnow()
num_of_image_on_server = len(os.listdir(UPLOADS_DIR))

MAX_CONTENT_LENGTH = 2097152
