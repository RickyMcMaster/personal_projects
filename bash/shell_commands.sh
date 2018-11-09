# LIST OF USEFUL SHELL COMMANDS

### FIND ###

# find every directory and file, in current directory
find .

# Find files by name with wildcards
find . -type f -name "*ython*"

# Find directories by name with wildcards
find . -type d -name "*ython*"

# Case insensitive
find . -type f -iname "*ython*"

# Find files by extension (with wildcards)
find . -type f -name "*.*py*"

# Find files modified in less than 10 minutes ago
find ~ -type f -mmin -10

# Find files modified more than 20 days ago
find ~ -type f -mtime +20

# find empty files
find . -empty

# permission-based find
find . -perm 777

# results of find to command
find /Users/richard.mcmaster/Documents/PDFs/Datorama -type f -name "*.pdf" -exec chown richard.mcmaster:datorama {} + 

# Just search current directory
find . -type f -name "*.pdf" -maxdepth 1


# ls

# list files - long, all, human-readable, sort by filesize. r for reverse order
ls -lahS
# r for reverse order
ls -lahSr