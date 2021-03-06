import tkinter as tk
from tkinter import filedialog
import os
import datetime
import pickle

def get_files(choose_files=True, **params):
    if choose_files:
        #eye_paths = select_files('Select Pupil Data')
        #events_paths = select_files('Select Events Data')
        ecog_path_raw = select_files('Select ECoG Data')
        ecog_path = ecog_path_raw[0]
        pupil_path_raw = select_files('Select Pupil Data')
        pupil_path = pupil_path_raw[0]
    else:
        eye_paths = params['eye_paths']
        events_paths = params['events_paths']
        ecog_path = params['ecog_path']
    return ecog_path, pupil_path


def select_files(prompt='Select your files'):
    '''Asks user to select files and return a tuple of paths'''
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilenames(title=prompt)

def select_folder(prompt='Select your folder'):
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory(title=prompt)

def make_output_folder(path, base):
    '''Creates a folder for the pipeline output'''
    folder_name = 'pipeline_output_'+ base
    folder_name = folder_name.replace(' ','_')
    out = os.path.join(path, folder_name)
    os.makedirs(out)
    return out


def folder_setup(eye_path, params):
    '''
    Sets up the folder for the pipeline output and updates params to include
    output folder path, as well as the base name for a particular run of the
    pipeline
    '''
    print('\nSetting up the folder...\n')
    params['base_name'] = os.path.splitext(os.path.basename(eye_path))[0]
    out_dir = make_output_folder(
        os.path.dirname(eye_path), params['base_name'])
    params['out_dir'] = out_dir


def make_path(name, ext, out_dir='', base_name='', **kwargs):
    '''
    Creates a path to a file in out_dir with filename of this format:
    name_base_nameext.
    '''
    return os.path.join(out_dir, name + '_' + base_name + ext)


def save_pkl(path, obj):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)


def load_pkl(path):
    with open(path, 'rb') as f:
        return pickle.load(f)
