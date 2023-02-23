#!/usr/bin/python3
"""
<<<<<<< HEAD
Fabric script that distributes an archive to your web servers
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ["35.196.96.41", "3.234.218.189"]
env.user = "ubuntu"
=======
2-do_deploy_web_static.py
Task 2:
Fabric script based off the previous task (file 1-pack_web_static.py)
In order to distribute an archive to my web servers
(Contains do_pack() func from file 1-pack_web_static.py)
"""
import os
from fabric.api import *
from datetime import datetime

env.hosts = ['35.196.120.179', '35.229.21.132']
>>>>>>> 4629bf5c8ed62b1152a2a506fa1aeac09ba0b16a


def do_pack():
    """
<<<<<<< HEAD
        return the archive path if archive has generated correctly.
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))

    if t_gzip_archive.succeeded:
        return archived_f_path
    else:
        return None
=======
    A function that returns None or the archive path
    """

    now = datetime.now()
    time_now = now.strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_" + time_now + ".tgz"
    local('mkdir -p versions')
    archive_command = local("tar -zcvf " + archive_name + " web_static")

    if archive_command.succeeded:
        return archive_name

    return None
>>>>>>> 4629bf5c8ed62b1152a2a506fa1aeac09ba0b16a


def do_deploy(archive_path):
    """
<<<<<<< HEAD
        Distribute archive.
    """
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file,
                                             newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False
=======
    A function that returns either True or False
    True:  if all operations have been done correctly
    False: if the file at archive_path doesn’t exist or if true statement fails
    """

    if os.path.exists(archive_path) is False:
        return False

    file_name_exe = archive_path.split('/')[1]
    file_name = file_name_exe[:-4]
    new_folder = "/data/web_static/releases/" + file_name

    try:
        put(archive_path, "/tmp/{}".format(file_name_exe))
        run("mkdir -p {}".format(new_folder))
        run("tar -xzf /tmp/{} -C {}/".format(file_name_exe, new_folder))
        run("rm /tmp/{}".format(file_name_exe))
        run("mv {}/web_static/* {}/".format(new_folder, new_folder))
        run("rm -rf {}/web_static".format(new_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(new_folder))
        return True
    except:
        return False
>>>>>>> 4629bf5c8ed62b1152a2a506fa1aeac09ba0b16a
