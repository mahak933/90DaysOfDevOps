#!/bin/bash

# Master maintenance script
# Runs log rotation and backup

LOGFILE="/var/log/maintenance.log"

log_rotate_script="/home/ubuntu/scripts/day19/log_rotation.sh"
backup_script="/home/ubuntu/scripts/day19/backup.sh"

log_dir="/var/log/nginx"
source_dir="/home/ubuntu/functions"
backup_dir="/home/ubuntu/backup"

# Ensure log file exists
touch "$LOGFILE"

# Helper: timestamp logging
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S')  $*" >> "$LOGFILE"
}

log "===== Maintenance Started ====="

### Run log rotation
log "Running Log Rotation..."
bash "$log_rotate_script" "$log_dir" >> "$LOGFILE" 2>&1

### Run backup
log "Running Backup..."
bash "$backup_script" "$source_dir" "$backup_dir" >> "$LOGFILE" 2>&1

log "===== Maintenance Finished ====="
