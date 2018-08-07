import sys
import numpy as np
from params import get_params
import scipy.io as spio
from scipy.io import loadmat
import os
import matplotlib.pyplot as plots
import matplotlib
from scipy import stats
from misc import make_path

params = get_params(sys.argv)
conds_to_plot = params['conds_to_plot']
plot_colors_scatter = params['plot_colors_scatter']
subject = params['subject_number']
sample_rate = params['sample_rate']


def plot_scatter(pupil_data, desired_indecies, ecog_matrix, merged,
                    channel_name, out_dir, base_name,pupil_data_smooth_matrix):
    labels = []
    n = len(ecog_matrix[1, :])

    fig, ax = plots.subplots()
    for count, i in enumerate(conds_to_plot):
        #use this if you want to plot not-smoothed data
        #x = pupil_data[count, 0:len(desired_indecies)]
        to_plot = pupil_data_smooth_matrix[count]
        x = to_plot[0:len(desired_indecies)]
        y = ecog_matrix[count+1, :]
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        r_value = np.round(r_value, 3)
        p_value = np.round(p_value, 4)
        ax.plot(x, y, marker= 'o', color = plot_colors_scatter[count], linestyle='None',
                    label=merged.names[i], ms=1)
        labels = np.append(labels, merged.names[i] + ', r-value = ' + str(r_value))
                            #+', p-value= ' + str(p_value))

    ax.legend(labels = labels, loc='upper left', fontsize=7)

    for count, i in enumerate(conds_to_plot):
        #x = pupil_data[count, 0:len(desired_indecies)]
        to_plot = pupil_data_smooth_matrix[count]
        x = to_plot[0:len(desired_indecies)]
        y = ecog_matrix[count+1, :]
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        ax.plot(x, intercept + slope*x, 'r', color=plot_colors_scatter[count], lw=-0.8)

    ax.annotate('n= ' + str(n), xy=(1, 0), xycoords='axes fraction', fontsize=10,
                horizontalalignment='right', verticalalignment='bottom')
    ax.set_xlabel('Baseline Corrected Pupil Diameter (mm)')
    ax.set_ylabel('HFB Power')
    plots.title('Pupil/ECoG Correlation: ' + 'Subject ' + str(subject) +
                ', Channel ' + str(channel_name), fontsize = 12)
    plots.savefig(make_path('pupil_ecog_correlation_scatter', '.png', out_dir=out_dir,
                    base_name=str(channel_name)), dpi=600)
    plots.close()

    return fig

def plot_scatter_der (pupil_data, desired_indecies, ecog_matrix, merged,
                        channel_name, out_dir, base_name, pupil_data_smooth_matrix):
    labels = []
    n = len(ecog_matrix[1, :])

    fig, ax = plots.subplots()
    for count, i in enumerate(conds_to_plot):
        to_plot = pupil_data_smooth_matrix[count]
        x = (to_plot[1:len(desired_indecies)]-to_plot[0:len(desired_indecies)-1])/(1/sample_rate)
        a = ecog_matrix[count+1, 1:len(desired_indecies)]
        b = ecog_matrix[count+1, 0:len(desired_indecies)-1]
        y = (a[:]-b[:])/(1/sample_rate)
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        r_value = np.round(r_value, 3)
        p_value = np.round(p_value, 4)
        ax.plot(x, y, marker= 'o', color = plot_colors_scatter[count], linestyle='None',
                    label=merged.names[i], ms=1)
        labels = np.append(labels, merged.names[i] + ', r-value = ' + str(r_value)
                            +', p-value= ' + str(p_value))

    ax.legend(labels = labels, loc='upper left', fontsize=7)

    for count, i in enumerate(conds_to_plot):
        to_plot = pupil_data_smooth_matrix[count]
        x = (to_plot[1:len(desired_indecies)]-to_plot[0:len(desired_indecies)-1])/(1/sample_rate)
        a = ecog_matrix[count+1, 1:len(desired_indecies)]
        b = ecog_matrix[count+1, 0:len(desired_indecies)-1]
        y = (a[:]-b[:])/(1/sample_rate)
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        ax.plot(x, intercept + slope*x, 'r', color=plot_colors_scatter[count], lw=-0.8)

    ax.annotate('n= ' + str(n), xy=(1, 0), xycoords='axes fraction', fontsize=10,
                horizontalalignment='right', verticalalignment='bottom')
    ax.set_xlabel('Derivative of Baseline Corrected Pupil Diameter (△mm/△t)')
    ax.set_ylabel('Derivative HFB Power (△HFB/△t)')
    plots.title('Pupil/ECoG Correlation: ' + 'Subject ' + str(subject) +
                ', Channel ' + str(channel_name), fontsize = 12)
    plots.savefig(make_path('pupil_ecog_correlation_scatter'+str(subject), '.png', out_dir=out_dir,
                    base_name=str(channel_name)), dpi=600)
    plots.close()

    return fig
