#!/usr/bin/env bash
# LIST OF USEFUL SHELL COMMANDS

### FIND ###

# find every directory and file, in current directory
find .

# Find files by name with wildcards
find . -type f -name "*ython*"

# Find directories by name with wildcards
find . -type d -name "*ython*"

# Case insensitive
find . -type f -iname "*iab*"

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


# history
history

# ls

# list files - long, all, human-readable, sort by filesize. r for reverse order
ls -lahS
# r for reverse order
ls -lahSr

# GREP

# search file for whole term
grep -w "John Williams" names.txt

# case insensitive
grep -wi "John Williams" names.txt

# case insensitive, partial match
grep -i "Joh" names.txt

# with line number
grep -wn "John Williams" names.txt


# lines before (5)
grep -wn -B 5 "John Williams" names.txt

# lines after (5)
grep -wn -A 5 "John Williams" names.txt

# context (lines before and after) (5)
grep -wn -C 5 "John Williams" names.txt

# all files in directory, colorise match, with context
grep --color=always -in -C 5 "row" ./*

# all files in current directory, recursive, with context
grep -inr -C 5 "row" .

# all files in current directory, recursive - list file names only
grep -irl  "row" .

# all files in current directory, recursive - count of matches
grep -irc  "row" .

# piping output
history | grep "git commit"| grep "IAB"

