import dropbox
import config
import os
import sys  
import argparse

"""for entry in dbx.files_list_folder(config.photo_root_file).entries:
    print(entry.name)
"""
parser = argparse.ArgumentParser(description='Check if backup is up to date with Dropbox')
parser.add_argument('local_folder', 
                    help='Local folder where the folders and files are stored.')

def main():
    """
        Main program
    """
    args = parser.parse_args()

    dbx = dropbox.Dropbox(config.dbox_dev_token)

    local_folder = args.local_folder
    if os.path.exists(local_folder):
        print('Yeah! The local folder does exists!')
    else:
        print("Bad news! Local folder doesn't exists!")
        exit(2)

    folder_counting = 0
    dropbox_root = config.photo_root_folder
    print('Validating folders against: ', dropbox_root)
    try:
        dropbox_list_result = dbx.files_list_folder(dropbox_root)
        while len(dropbox_list_result.entries) > 0:
            for dropbox_entry in dropbox_list_result.entries:
                folder_counting += 1
                dropbox_folder = dropbox_root + '/' + dropbox_entry.name
                # print('Dropbox folder:', dropboxfolder)
                local_entry_folder = local_folder + '/' + dropbox_entry.name
                # print('Backup  folder:', localfolder)
                if not (os.path.exists(local_entry_folder)):
                    print('Precisa download: ', dropbox_folder)
                    download_folder_contents(dbx, dropbox_entry)
            dropbox_list_result = dbx.files_list_folder_continue(dropbox_list_result.cursor)
    except dropbox.exceptions.ApiError as err:
        print('Folder listing failed for', dropbox_root , '-- assumed empty:', err)
        exit(2)
    else:
        print('Has more? ', dropbox_list_result.has_more)
    dbx.close()

def download_folder_contents(dbx, folder):
    try:
        basedir = '/Users/wcsantosfilho/Downloads/'
        newdir = basedir + folder.name
        os.mkdir(newdir)
        file_counting = 0
        dropbox_list_file_result = dbx.files_list_folder(folder.path_lower)
        while len(dropbox_list_file_result.entries) > 0:
            for dropbox_file in dropbox_list_file_result.entries:
                file_counting +=1
                # xxzz = dbx.files_download(dropbox_file.path_display)
                kpo = dropbox_file.path_lower
                zpo = newdir + '/' + dropbox_file.name
                zzxx = dbx.files_download_to_file(zpo, kpo)
            dropbox_list_file_result = dbx.files_list_folder_continue(dropbox_list_file_result.cursor)
    except dropbox.exceptions.HttpError as err:
        print('*** Http error:', err)
        return None
    except OSError as err:
        print('*** OS Error:', err)
        return None
    return file_counting

if __name__ == '__main__':
    main()