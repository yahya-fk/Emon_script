import os
import shutil

prefix = 'SE39040'
target_folder = './' 
downloads_folder = os.path.expanduser('~') + '\\Downloads\\'
matching_files = [filename for filename in os.listdir(downloads_folder) if filename.startswith(prefix)]

matching_files.sort(key=lambda x: os.path.getmtime(os.path.join(downloads_folder, x)), reverse=True)

if matching_files:
    new_filename = 'PQGAPP.xsl' 
    old_path = os.path.join(downloads_folder, matching_files[0])
    new_path = os.path.join(downloads_folder, new_filename)
    
    if os.path.exists(target_folder + new_filename):
        os.remove(target_folder + new_filename)
    shutil.move(old_path, new_path)

    shutil.move(new_path, target_folder + new_filename)

