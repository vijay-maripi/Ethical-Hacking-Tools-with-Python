# Jun 30 2020 Linux Privilege Escalation

## Linux User Enumeration: <cmd>:<Description>

1. uname -a : Kernel information and architecture information of machine (we can use this info for kernel exploit)
2. cat /proc/version
3. cat /etc/issue
4. lscpu : for architecture info
5. ps aux : To view the running services
6. whoami
7. id
8. sudo -l : see what privileges you have to run the programs
9. cat /etc/passswd : you can see user name, encrypted password,  user id, group id, user description, user's home directory, user's login shell.
10. cat /etc/passwd | cur -d : -f 1 : using this you can delimit with : and select by field either 1 or 2.. so on, this command gives the output as list of users!
11. cat /etc/shadow : file stores actual password in encrypted format (more like the hash of the password) for user's account with additional properties related to user password.
12. cat /etc/group : to check whether we can access group files or not.
13. sudo su - : siwth user
14. sudo -i : go to root (where $ changes to # )
15. env

## Linux Network Enumeration: <cmd> : <Description>

1. ifconfig
2. ip a
3. route
4. ip route
5. arp -a : tells about with whom we're communicating with
6. ip neigh : tells about with whom we're communicating with
7. netstat -ano : You can identify open ports, what communication exists

 

## Linux Privilege Escalation Password Hunting or Searching a word in Linux:

1. grep --color=auto -rnw '/' -ie "PASSWORD" --color=always 2> /dev/null
2. find . -type f -exec grep -i -I "PASSWORD" {} /dev/null \;
3. find / -name id_rsa 2> /dev/null
4. locate password

## Tools:

1. LinPEAS

[carlospolop/privilege-escalation-awesome-scripts-suite](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS)

 2.  LinEnum

[rebootuser/LinEnum](https://github.com/rebootuser/LinEnum)

 3.  linux-exploit-suggester

[mzet-/linux-exploit-suggester](https://github.com/mzet-/linux-exploit-suggester)

 4.  Linux Priv Checker

[sleventyeleven/linuxprivchecker](https://github.com/sleventyeleven/linuxprivchecker)

## Resources:

1. Linux Privilege Escalation

[swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md)

  2.  Hash Examples:

[example_hashes [hashcat wiki]](https://hashcat.net/wiki/doku.php?id=example_hashes)