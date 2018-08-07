import sys
import numpy as np
import pickle
from params import get_params
import scipy.io as spio
from scipy.io import loadmat

params = get_params(sys.argv)
conds_to_plot = params['conds_to_plot']

def load_ecog(ecog_path):

    ecog_path = ''.join(ecog_path)

    ecog_file = spio.loadmat(ecog_path, struct_as_record=False, appendmat=False)
    time_ecog_raw = ecog_file['plot_time']
    time_ecog = time_ecog_raw[0]
    ecog_data = ecog_file['temp_mean']
    ecog_dataT = ecog_data.transpose()


    if len(conds_to_plot) > 1:
#for three conditions
        time_with_ecog = np.row_stack((time_ecog, ecog_dataT[0,:],
                                        ecog_dataT[1,:], ecog_dataT[2,:]))
    else:
#for one condition
        if conds_to_plot in np.arange(4,7):
            index = int(conds_to_plot[0])-4
            time_with_ecog = np.row_stack((time_ecog, ecog_dataT[index,:]))
        else:
            index = int(conds_to_plot[0])-1
            time_with_ecog = np.row_stack((time_ecog, ecog_dataT[index,:]))

    return time_with_ecog, time_ecog
