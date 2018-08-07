import sys
from params import save_params, get_params
from misc import folder_setup, select_files, make_path, select_folder
from loadpupil import load_pupil
from loadecog import load_ecog
from plotscatter import plot_scatter, plot_scatter_der
from plotline import plot_line

import time
import numpy as np
import pickle
import scipy.io as spio
from scipy.io import loadmat
import os

import matplotlib.pyplot as plots

if __name__ == '__main__':
    t0 = time.time()
    params = get_params(sys.argv)
    all_channels = params['all_channels']

#select files
    pupil_path_raw = select_files('Select Pupil Data')
    pupil_path = pupil_path_raw[0]

    if all_channels:
        ecog_path = select_files('Select ECoG Data')
        print (ecog_path)
    else:
        folder = select_folder(prompt='Select your folder')
        file_names = [f for f in os.listdir(folder) if ('mat' in f) and 'pupil' in f]
        ecog_path = list()
        for f in file_names:
            out_dir = os.path.dirname(folder)
            new_path = os.path.join(folder, f)
            ecog_path.append(new_path)
        print(ecog_path)

#load pupil data
    pupil_data, time_list, merged, pupil_data_smooth_matrix = load_pupil(pupil_path)

#load ecog data
    for count, path in enumerate(ecog_path):
        ecog = ecog_path[count]
        pos_pupil = path.find('pupil_')
        pos_ext = path.find('.')
        channel_name = ecog[pos_pupil+6:pos_ext]
        time_with_ecog, time_ecog = load_ecog(ecog)
        folder_setup(path, params)
        out_dir = params['out_dir']
        base_name = params['base_name']

#combine data (used to make scatter plot)
        desired_indecies_raw = []
        for i in np.arange(0, len(time_ecog)):
            if np.round(time_ecog[i], 3) in time_list:
                desired_indecies_raw = np.append(desired_indecies_raw, i)

        desired_indecies = [int(x) for x in desired_indecies_raw]
        ecog_matrix = time_with_ecog[:, desired_indecies]

        start_index = time_ecog.tolist().index(0)

#plots scatter plot of the pupil data vs HFB signal
        scatter_plot = params['scatter_plot']
        if scatter_plot == 'normal':
            fig = plot_scatter(pupil_data, desired_indecies, ecog_matrix, merged,
                                channel_name, out_dir, base_name, pupil_data_smooth_matrix)
        if scatter_plot == 'derivative':
            fig = plot_scatter_der(pupil_data, desired_indecies, ecog_matrix, merged,
                                channel_name, out_dir, base_name, pupil_data_smooth_matrix)

#plots line plot plot of pupil data and ecog data on same axis vs time
        fig1 = plot_line(pupil_data, time_list, time_with_ecog, start_index,
                                channel_name, merged, out_dir, base_name, pupil_data_smooth_matrix)


    print('\nDone!\n')
    print('\n\nIn total, that took {} seconds!'.format(time.time() - t0))
