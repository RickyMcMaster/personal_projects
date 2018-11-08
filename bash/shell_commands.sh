# LIST OF USEFUL SHELL COMMANDS



# find

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

# ls

# list files - long, all, human-readable, sort by filesize. r for reverse order
ls -lahS
# r for reverse order
ls -lahSr