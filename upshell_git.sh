#-------------------------auto push

#ssh-keygen -t rsa -b 4096 -C "thai.itplus@gmail.com"
#default: /home/kids/.ssh/id_rsa

#ssh-add /home/kids/.ssh/id_rsa
#cat .ssh/id_rsa.pub
#copy key to https://github.com/settings/keys
#--------------------------------

path="https://github.com/TCU1/ChatClientServer_Python/"
username="balau123"
email="thai.itplus@gmail.com"
work_path="/home/kids/Desktop/ChatClientServer_Python"

git config --global user.name $username
git config --global user.email $email
git config --global color.ui auto

clear

echo "username: " $username
echo "Email: " $email
echo "Path: "$path

echo
echo "LIST FILE"
echo
#ls -la $work_path
echo

git config --global core.editor "$work_path"
git init

cd $work_path
ls -la

echo "commit content: "
read commit
echo
echo "Coomit content: $commit"
echo "PATH: $path"
echo
echo "*** working"
echo


git add *
git commit -m "$commit"
git remote remove origin

git reset --mixed

git remote add origin "$path"
git remote set-url origin git@github.com:$username
git branch NguyenDinhThai
git checkout NguyenDinhThai
#git pull origin master
git push -f origin NguyenDinhThai

echo
echo "DONE!!!"	
