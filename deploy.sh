#!/bin/bash

#sudo apt-get install python3 -y
#sudo apt-get install git -y

#sudo curl -fsSL get.docker.com -o get-docker.sh && sudo sh get-docker.sh
#sudo curl -sSL https://nixpacks.com/install.sh | sudo bash

python3 deploy.py '{"git_user": "oauth2", "git_password": "ghu_GYROsriQtRcE66tHOvB7GHJ9kYD1760NN6dk", "git_repository": "https://oauth2:ghu_GYROsriQtRcE66tHOvB7GHJ9kYD1760NN6dk@github.com/Joshua3212/huddu-example.git", "git_branch": "main", "port": 80}'