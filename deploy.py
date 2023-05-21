import os
import sys
import json
import uuid
import sqlite3
data = json.loads(
    sys.argv[1]
)

app_dir = str(uuid.uuid4()).replace("-", "")  # this will be unique
image_name = app_dir
database = "huddu.sqlite"


# 1 get new code
clone_command = f"sudo git clone --single-branch --branch {data['git_branch']} {data['git_repository']} {app_dir}"
os.system(clone_command)


# 2 build with nixpacks
nixpacks_command = f"cd {app_dir}; sudo nixpacks build "
if data.get("build_command"):
    nixpacks_command += f" --build {data['build_command']}"
if data.get("start_command"):
    nixpacks_command += f" --start {data['start_command']}"
if data.get("install_command"):
    nixpacks_command += f" --install {data['install_command']}"
if data.get("environment"):
    nixpacks_command += " --env".join(data["environment"])


nixpacks_command += " ."
print(nixpacks_command)
os.system(nixpacks_command)

# 3 deploy on docker


# cleanup
cleanup_command = f"sudo rm -r {app_dir}"
os.system(cleanup_command)

print(data)

# 3 build the image
