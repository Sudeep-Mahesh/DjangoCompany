1.  ssh-keygen -t rsa -b 4096 -C "your_email@example.com"  //Create a ssh key
2.  cat ~/.ssh/id_rsa.pub                                  //Display git ssh key
3.  Paste the key to github profile (starting ssh-rsa)
4. Then clone ssh url

git pull origin main