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
    exceptions = file.get('exceptions','exceptions')
    for f in files:
        f_extension = f.rsplit(".",1)[-1]
        if f_extension in exceptions :
            print(f"file {f} skipped, found in exceptions list!")
        else:
            try:
                if os.path.isfile(f"{directory_path}/{f}"):
                    os.remove(f"{directory_path}/{f}")
                    print(f"file {f} deleted")
                elif os.path.isdir(f"{directory_path}/{f}"):
                    shutil.rmtree(f"{directory_path}/{f}")
                
            except PermissionError:
                print(f"File {f} not deleted, permission denied")
            except Exception:
                print("Other problem occurred")