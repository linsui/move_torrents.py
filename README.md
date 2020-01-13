# Move torrents

Have you just renamed a directory or moved your storage to a new hard-drive and now all of your torrents need to be updated? By change fastresume file we can skip the reckeck. For more information about fastresume file, see https://www.libtorrent.org/manual-ref.html#fast-resume .

*This script does not move any data. Please move them manully first. Please close qBittorrent before running this script.*

This script only works on qBittorrent 3.3+ because in that version the location for torrent metadata was moved. Tested with qBittorrent 4.2.1 and Python 3.8 .

## Usage

1. Close your qBittorrent
2. Move your data files
3. Backup your torrents directory (e.g. $env:localappdata/qBittorrent/BT_backup)
4. Run this script with strings you want to replace in data file path
5. Reopen qBittorrent

## Example

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

## License

```
Copyright (c) 2015, Jimmy Zelinskie
Copyright (c) 2020, linsui
      
      
        

All rights reserved.
      
      
        


      
      
        
Redistribution and use in source and binary forms, with or without
      
      
        
modification, are permitted provided that the following conditions are met:
      
      
        


      
      
        
* Redistributions of source code must retain the above copyright notice, this
      
      
        
  list of conditions and the following disclaimer.
      
      
        


      
      
        
* Redistributions in binary form must reproduce the above copyright notice,
      
      
        
  this list of conditions and the following disclaimer in the documentation
      
      
        
  and/or other materials provided with the distribution.
      
      
        


      
      
        
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
      
      
        
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
      
      
        
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
      
      
        
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
      
      
        
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
      
      
        
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
      
      
        
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
      
      
        
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
      
      
        
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
      
      
        
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
