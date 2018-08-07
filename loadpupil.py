import sys
import numpy as np
import pickle
from params import get_params

params = get_params(sys.argv)
sample_rate = params['sample_rate']
conds_to_plot = params['conds_to_plot']
conds_to_plot_array = np.asarray(conds_to_plot)


def load_pupil(pupil_path):
    with open(pupil_path, 'rb') as f:
        merged = pickle.load(f)

    averaged = np.nanmean(merged.matrix, axis=2)

    start_sample = merged.n_backsamples
    end_sample = merged.n_forwardsamples

    start_time = start_sample/sample_rate
    end_time = end_sample/sample_rate

    samples_to_time = np.arange(start_time, end_time, 1/sample_rate)
    samples_to_time0 = samples_to_time - start_time

    pupil_data = averaged[:, np.arange(start_sample, end_sample+1)]
    pupil_data = pupil_data[conds_to_plot_array, :]

    time_list_raw = samples_to_time0.tolist()
    time_list = np.round(time_list_raw, 3)

#smooths data using average of 11 points
    pupil_data_smooth_matrix = []
    for cond in np.arange(0, len(pupil_data)):
        pupil_data_smooth = []
        pupil_array = pupil_data[cond, :]
        for count, i in enumerate(pupil_array):
            if count == 0:
                nums = [i, pupil_array[1]]
            elif count < 6:
                nums = []
                for x in np.arange(1,count+1):
                    num_pos = pupil_array[count-x]
                    num_neg = pupil_array[count+x]
                    nums = np.append(nums, num_pos)
                    nums = np.append(nums, num_neg)
                nums = np.append(nums, pupil_array[count])
            elif count == len(pupil_array)-1:
                nums = [i, pupil_array[count-2]]
            elif count > len(pupil_array)-6:
                count_rev = len(pupil_array)-count-1
                nums = []
                for x in np.arange(1, count_rev+1):
                    num_pos = pupil_array[count-x]
                    num_neg = pupil_array[count+x]
                    nums=np.append(nums, num_pos)
                    nums = np.append(nums, num_neg)
                nums = np.append(nums, pupil_array[count])
            else:
                nums = []
                for x in np.arange(1,6):
                    num_pos = pupil_array[count-x]
                    num_neg = pupil_array[count+x]
                    nums = np.append(nums, num_pos)
                    nums = np.append(nums, num_neg)
                nums = np.append(nums, pupil_array[count])

            new_data = np.mean(nums)
            pupil_data_smooth = np.append(pupil_data_smooth, new_data)
        pupil_data_smooth_matrix.append(pupil_data_smooth)

    return pupil_data, time_list, merged, pupil_data_smooth_matrix
