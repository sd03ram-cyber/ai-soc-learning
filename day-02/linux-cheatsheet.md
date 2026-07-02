# Linux Command Cheat Sheet

1. `ls` – list files in a directory. `ls -la`
2. `cd` – change directory. `cd /var/log`
3. `pwd` – print current directory. `pwd`
4. `cat` – print file contents. `cat /etc/passwd`
5. `less` – view file page by page. `less /var/log/syslog`
6. `grep` – search text in files. `grep "error" app.log`
7. `find` – search for files. `find / -name "*.conf"`
8. `ps` – list running processes. `ps aux`
9. `top` – live process/resource monitor. `top`
10. `kill` – stop a process by PID. `kill -9 1234`
11. `chmod` – change file permissions. `chmod 644 file.txt`
12. `chown` – change file owner. `chown user:group file.txt`
13. `whoami` – show current user. `whoami`
14. `su` – switch user. `su root`
15. `sudo` – run command as another user (root). `sudo apt update`
16. `tail -f` – follow live log output. `tail -f /var/log/auth.log`
17. `head` – show first lines of a file. `head -n 20 file.txt`
18. `journalctl` – view systemd logs. `journalctl -u ssh`
19. `netstat` / `ss` – show network connections. `ss -tulpn`
20. `man` – show manual for a command. `man chmod`
