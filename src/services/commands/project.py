import os
from datetime import datetime

def createDir(projectName):
    time = datetime.now()
    name = f"{projectName}-{time.timestamp()}"
    dir_now = os.path.dirname(os.path.realpath(__file__))
    dir_projct = dir_now.replace("/cli_liinaliiis/src/services/commands", "")
    os.chdir(dir_now)
    os.system("chmod u+x project.py")
    os.chdir(dir_projct)
    os.mkdir(name)
    os.mkdir(name+"/src")
    os.mkdir(name+"/src/controllers")
    os.mkdir(name+"/src/services")
    os.mkdir(name+"/src/database")
    os.mkdir(name+"/src/models")
    return dir_projct+"/"+name

def projectPython(name):
    dir = createDir(name)
    try:
        file = open(f"{dir}/main.py", 'r+')
        file = open(f"{dir}/src/controllers/app_controller.py", 'r+')
        file = open(f"{dir}/src/controllers/users_controller.py", 'r+')
        file = open(f"{dir}/src/services/app_service.py", 'r+')
        file = open(f"{dir}/src/services/users_service.py", 'r+')
        file = open(f"{dir}/src/database/connection.py", 'r+')
        file = open(f"{dir}/src/models/User.py", 'r+')
        file = open(f"{dir}/.gitignore", 'r+')
        file = open(f"{dir}/.env", 'r+')
    except FileNotFoundError:
        file = open(f"{dir}/main.py", 'w+')
        file = open(f"{dir}/src/controllers/app_controller.py", 'w+')
        file = open(f"{dir}/src/controllers/users_controller.py", 'w+')
        file = open(f"{dir}/src/services/app_service.py", 'w+')
        file = open(f"{dir}/src/services/users_service.py", 'w+')
        file = open(f"{dir}/src/database/connection.py", 'w+')
        file = open(f"{dir}/src/models/User.py", 'w+')
        file = open(f"{dir}/.gitignore", 'w+')
        file = open(f"{dir}/.env", 'w+')
    file.close()

def projectNodeJS(name):
    dir = createDir(name)
    os.chdir(dir)
    os.system("npm init -y")
    try:
        file = open(f"{dir}/index.js", 'r+')
        file = open(f"{dir}/src/controllers/app_controller.js", 'r+')
        file = open(f"{dir}/src/controllers/users_controller.js", 'r+')
        file = open(f"{dir}/src/services/app_service.js", 'r+')
        file = open(f"{dir}/src/services/users_service.js", 'r+')
        file = open(f"{dir}/src/database/connection.js", 'r+')
        file = open(f"{dir}/src/models/User.js", 'r+')
        file = open(f"{dir}/.gitignore", 'r+')
        file = open(f"{dir}/.env", 'r+')
    except FileNotFoundError:
        file = open(f"{dir}/index.js", 'w+')
        file = open(f"{dir}/src/controllers/app_controller.js", 'w+')
        file = open(f"{dir}/src/controllers/users_controller.js", 'w+')
        file = open(f"{dir}/src/services/app_service.js", 'w+')
        file = open(f"{dir}/src/services/users_service.js", 'w+')
        file = open(f"{dir}/src/database/connection.js", 'w+')
        file = open(f"{dir}/src/models/User.js", 'w+')
        file = open(f"{dir}/.gitignore", 'w+')
        file = open(f"{dir}/.env", 'w+')
    file.close()

def project():
    name = input("NOME: ")
    tipe = input("TIPO: ")
    
    if tipe == "python" or tipe == "py" or tipe == "p":
        projectPython(name)
        print("Projeto Python criado!")
    elif tipe == "nodejs" or tipe == "node" or tipe == "n":
        projectNodeJS(name)
        print("Projeto NodeJS criado!")
