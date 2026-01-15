import os
import configparser
import shutil
import platform

def get_protected_paths():
    system = platform.system().lower()
    if system == 'windows':
        return {
            'windows', 'system32', 'syswow64',
            'program files', 'program files (x86)', 'programdata',
            'downloads', 'documents', 'desktop', 'pictures', 'videos', 'music'
        }
    elif system == 'linux':
        return {
            '/', '/bin', '/sbin', '/etc', '/lib', '/lib64', '/dev', 
            '/proc', '/sys', '/run', '/home', '/usr', '/opt', '/srv',
            '/tmp', '/media', '/mnt', '/var'
        }
    elif system == 'darwin':
        return {
            '/','/system', '/library', '/applications', '/usr', '/bin', '/sbin',
            '/users', '/system/library/extensions', '/library/extensions',
            '/library/preferences', 'downloads', 'documents', 'desktop'
        }

def is_protected_path(full_path):
    protected = get_protected_paths()
    return any(p in os.path.normpath(full_path).lower() for p in protected)

def delete_files():
    file = configparser.ConfigParser()
    file.read('config.conf')
    directory_path = file.get('path','file_path')
    files = os.listdir(directory_path)
    exceptions = file.get('exceptions','exceptions').split(',')
    for f in files:
        full_path = os.path.join(directory_path,f)
        if is_protected_path(full_path):
            print(f"{f} is protected! The program skipped it")
            continue

        f_extension = f.rsplit(".",1)[-1] if '.' in f else ''
        if f_extension in exceptions :
            print(f"file {f} skipped, found in exceptions list!")
        else:
            try:
                if os.path.isfile(full_path):
                    os.remove(full_path)
                    print(f"file {f} deleted")
                elif os.path.isdir(full_path):
                    shutil.rmtree(full_path)
                
            except PermissionError:
                print(f"File {f} not deleted, permission denied")
            except Exception as e:
                print(f"Other problem occurred: {e}")