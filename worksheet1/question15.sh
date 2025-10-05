#!/bin/bash
# (15) A script that finds files older than 7 days and compresses them into a .tar.gz file with
# the date of compression in the name in the format YYYYMMDD


date=$(date +%Y%m%d)

archive_name="old_files_$date.tar.gz"

files=$(find "." -type f -mtime +7)

if [ -z "$files" ]; then
    echo "No such file older than 7 days found."
    exit 0
fi
tar -czf "$archive_name" $files

echo "Compressed file contaning files older than 7 days $archive_name"
