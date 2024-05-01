#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generate a tgz archieve"""
    try:
        date = datetime.now.strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -czvf {} web_static".format(file_name))
        return filen_name
    finally:
        return None