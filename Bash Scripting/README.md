# Journal

Today I have learned more about Bash scripting.
This was also a good way to learn more VIM commands.

Some interesting facts I have learned today:
-  every bash script starts with a #!/bin/bash
-  remember alwas to make the file executable (chmod +x) after you created it.
-  /dev/null is a directory in Linux that cleares all the outputs you direct towards it.
-  variables are called using $ sign.
-  some system variables:
  -  $0 - will return the name of the script
  -  $1-9 - the first 9 arguments of the bash script
  -  $? - the exit status of the most recently run process
-  command substitution is a method of storing OUTPUT of a command into variable ( VarName = `Command` or VarName= $(Command)
-  export variables is used to set enviroment variable in OS. (for user is ~/.bashrc file for all users is /etc/profile file)
-  crontab -e is the file to set the period of time the script you place in there will run automatically (Minute  Hour  DayOfMonth Month DayOfWeek (* - every time))
-  ssh-keygen generates public and privates keys
-  you can then place the public key to other vm's in order to connect to them using ssh and not password of user (ssh-copy-id)

Finally I have made a script to connect to 3 vm's and install prerequisites on each vm to build a static website using just bash scripting.
