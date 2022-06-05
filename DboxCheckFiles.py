import dropbox
import config
import os
import sys  
import argparse
import unidecode

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
        print('Yeah! The local folder', local_folder, ' does exists!')
    else:
        print('Bad news! Local folder', local_folder, ' does not exists!')
        exit(2)

    folder_counting = 0
    dropbox_root = config.photo_root_folder
    print('Validating folders against: ', dropbox_root)
    try:
        dropbox_list_result = dbx.files_list_folder(dropbox_root)
        while len(dropbox_list_result.entries) > 0:
            for dropbox_entry in dropbox_list_result.entries:
                folder_counting += 1
                xpto = dbx.files_list_folder(dropbox_entry.path_lower)
                dropbox_folder = dropbox_root + '/' + dropbox_entry.name
                # print('Dropbox folder:', dropboxfolder)
                local_entry_folder = local_folder + '/' + dropbox_entry.name
                # print('Backup  folder:', localfolder)
                if not (os.path.exists(local_entry_folder)):
                    print('Local folder not found: ', dropbox_folder)
                else:
                    file_count = check_folder_contents(dbx, dropbox_entry, local_folder)
            dropbox_list_result = dbx.files_list_folder_continue(dropbox_list_result.cursor)
    except dropbox.exceptions.ApiError as err:
        print('Folder listing failed for', dropbox_root , '-- assumed empty:', err)
        exit(2)
    else:
        print('Has more? ', dropbox_list_result.has_more)
    dbx.close()

def check_folder_contents(dbx, dropbox_folder, local_folder):
    try:
        local_folder = local_folder + '/' if local_folder[-1] != '/' else local_folder
        localdir = local_folder + dropbox_folder.name
        file_counting = 0
        dropbox_list_file_result = dbx.files_list_folder(dropbox_folder.path_lower)
        xpto = os.listdir(localdir)
        lcf = [unidecode.unidecode(ff) for ff in xpto]
        a = 0
        dropbox_file_couting = len(dropbox_list_file_result.entries)
        while len(dropbox_list_file_result.entries) > 0:
            for dropbox_file in dropbox_list_file_result.entries:
                file_counting +=1
                dpb = unidecode.unidecode(dropbox_file.name)
                xpta = lcf.index(dpb)
                # index above will issue an Exception if not found
            dropbox_list_file_result = dbx.files_list_folder_continue(dropbox_list_file_result.cursor)
    except dropbox.exceptions.HttpError as err:
        print('*** Http error:', err)
        exit(2)
        return None
    except ValueError as err:
        print('Folder: ', dropbox_folder.name, '*** Value error:', err)
        return None
    except OSError as err:
        print('*** OS Error:', err)
        exit(2)
        return None
    print('Folder: ', dropbox_folder.name, dropbox_file_couting, ':', file_counting)
    return file_counting

if __name__ == '__main__':
    main()
