#!/bin/bash
export HOME=/home/ec2-user
GITHUB_TOKEN=""
sudo yum update
sudo yum install stress-ng -y
sudo yum install htop -y
sudo yum install python3-pip -y
pip3 install flask
sudo yum install git -y
cd /home/ec2-user
git clone https://$GITHUB_TOKEN@github.com/mausmani/cs_498_cloud cs_498_cloud

cd /home/ec2-user/cs_498_cloud

python3 serve.py
