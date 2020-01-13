# Move torrents

Have you just renamed a directory or moved your storage to a new hard-drive and now all of your torrents need to be updated? By change fastresume file we can skip the reckeck. For more information about fastresume file, see https://www.libtorrent.org/manual-ref.html#fast-resume .

This script only works on qBittorrent 3.3+ because in that version the location for torrent metadata was moved. Tested with qBittorrent 4.2.1 and Python 3.8 .

### example usage

```
# Backup the BT_BACKUP directory, in case something goes wrong.
$ cp -r "C:\\Users\\Jimi\\AppData\\Local\\qBittorrent\\BT_BACKUP" "C:\\Users\\Jimi\\AppData\\Local\\qBittorrent\\BT_BACKUP_2"

# Install the script's dependencies.
$ pip install requirements.txt

or

$ pip install bencode.py

# Run the script with the three required arguments.
$ python move_torrents.py --find-path "F:\\Anime\\" --replace-path "F:\\" --bt-backup-path "C:\\Users\\Jimi\\AppData\\Local\\qBittorrent\\BT_BACKUP"
```
