# Journal

Today I started the Linux part of the Devops course.
I knew a little bit of Linux before but it is nice to recap some basic commands that will help me in the future.
Some things to remember from this lesson:
- /etc is the configuration direcotry
- files from /tmp are deleted after vm shutdown
- VIM editor has 3 modes: command mode, insert mode, extended commnad mode.
- there are several types of files in linux: Directories (d) Links (l) Special files (c) Sockets (s) Pipes (p) Regular files (-)
- there are 3 types of users in Linux: root user, system user (created by softwares or applications), normal users.
- /etc/passwd file is where you find users and /etc/group is where you find groups
- child process = process that was opened by other process (parent)
- orphan process = process that remains running even after the parent process has been terminated or completed
- zombie process = process that completed its task but it is still showing in the process table.

Some commands that I did not knew as well:
ln -s [option] [shortcut name] - creates shortcuts
cut -d -f filename (d=delimiter, f=field) returns the column of file
sed 's/searchfor/replacewith/g' filename - search a word in the file and replace it with the word required to be in the output
find - used to find the files or directory's path.
chown - change file ownership
chmod - change access modes
systemctl start/stop/enable/disable - change service status.
tar -czvf - create a tar file
top - display and update cpu processes

Linux is a great OS to learn especially for SysAdmins, Cloud engineers or, of course, for Devops engineers.
