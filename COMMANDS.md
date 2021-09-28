# Print the number of items in the /etc/ folder
ls /etc | wc -l

# Print the number of unique (non-duplicate) lines in d/etc/ssh/ssh_config which contain the word "IdentityFile"
find /etc/ssh/ssh_config -type f -name'IdentityFile' | wc -l

# Print the total space on disk consumed by your home directory in gigabytes
cd ~; du -hs



############################################################
# Sources:

# https://devconnected.com/how-to-count-files-in-directory-on-linux/
# https://unix.stackexchange.com/questions/521464/count-number-of-files-in-directory-with-a-certain-name
# https://www.cs.washington.edu/lab/faq/home-directory-size
############################################################
