# Copyright 2015 Jimmy Zelinskie. All rights reserved.
# Use of this source code is governed by the BSD 2-Clause license,
# which can be found in the LICENSE file.

import argparse
from pathlib import Path

import bencode

QBT_KEY = 'qBt-savePath'
LT_KEY = 'save_path'
FASTRESUME_EXT = 'fastresume'


def update_fastresume(file_path, find_str, replace_str):
    """
    qBittorrent stores metadata in "fastresume" files. The files are encoded in
    a format called bencode, which is used elsewhere in the BitTorrent protocol.
    There are two paths to your files in each fastresume file. One is for
    qBittorrent; the other is for libtorrent. This function runs a find and
    replace on those paths.
    """
    # Decode the bencoded file.
    fastresume = bencode.decode(file_path.read_bytes())

    # Update the two paths inside the file.
    fastresume[QBT_KEY] = fastresume[QBT_KEY].replace(find_str, replace_str)
    fastresume[LT_KEY] = fastresume[LT_KEY].replace(find_str, replace_str)

    # Overwrite the file with our updated structure.
    file_path.write_bytes(bencode.encode(fastresume))


def update_bt_backup(bt_backup_path, find_str, replace_str):
    """
    qBittorrent stores torrent metadata in a BT_BACKUP directory. This function
    walks that directory and runs a find and replace on the "fastresume" files
    for each torrent.
    """
    bt_backup_path = Path(bt_backup_path)
    for file_path in bt_backup_path.glob(f'*.{FASTRESUME_EXT}'):
        try:
            update_fastresume(file_path, find_str, replace_str)
        except:
            print(f'failed to update {file_path}')
            continue


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Find and replace filepaths in qBittorrent v3.3+'
    )
    parser.add_argument('--find-str',
                        help='string to find',
                        type=str,
                        required=True)
    parser.add_argument('--replace-str',
                        help='string that replaces find_path',
                        type=str,
                        required=True)
    parser.add_argument('--bt-backup-path',
                        help='path to qBittorrent BT_BACKUP directory',
                        type=str,
                        required=True)
    args = parser.parse_args()

    update_bt_backup(args.bt_backup_path, args.find_str, args.replace_str)
