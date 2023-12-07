#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives using the function do_clean
"""
from fabric.api import *
from os import listdir
from datetime import datetime

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'  # Replace with your username
env.key_filename = ['/path/to/your/private/key.pem']  # Replace with the path to your SSH private key

def do_clean(number=0):
    """
    Delete out-of-date archives.
    """
    number = int(number)
    if number < 1:
        number = 1
    else:
        number += 1

    # Delete old archives in versions folder
    with cd('versions'):
        local_archives = sorted(listdir('.'))
        to_delete = local_archives[:-number]
        for archive in to_delete:
            local('rm -f {}'.format(archive))

    # Delete old archives in web_static/releases folder on servers
    with cd('/data/web_static/releases'):
        remote_archives = run('ls -1t').split()
        to_delete = remote_archives[:-number]
        for archive in to_delete:
            run('rm -rf {}'.format(archive))

