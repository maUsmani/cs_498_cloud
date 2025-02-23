#!/bin/bash
export HOME=/home/ec2-user
sudo yum update
sudo yum install stress-ng -y
sudo yum install htop -y
sudo yum install python3-pip -y
pip3 install flask
sudo yum install git -y
cd /home/ec2-user
git clone YOUR_CODECOMMIT_REPO_LINK (https://<github-personal-access-token>@github.com/username/repository_name)
cd /home/ec2-user/YOUR_CODECOMMIT_REPO_NAME
python3 serve.py
