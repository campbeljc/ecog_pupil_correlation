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
plot_colors_line = params['plot_colors_line']
subject = params['subject_number']
line_style = params['line_style']
show = params['show']
all_channels = params['all_channels']

def plot_line(pupil_data, time_list, time_with_ecog, start_index, channel_name,
                merged, out_dir, base_name, pupil_data_smooth_matrix):

    for count, i in enumerate(conds_to_plot):
        to_plot = pupil_data_smooth_matrix[count]
        fig1, ax1 = plots.subplots()
        ax1.set_xlabel('Time (ms)')
        x = time_list
        y = to_plot[0:len(time_list)]
        ax1.plot(x, y, color = plot_colors_line[count], lw = 0.8, ls=line_style)
        ax1.plot(np.nan, color=plot_colors_line[count+3], lw=0.8, ls= '-')
        ax1.set_ylabel('Baseline Corrected Pupil Diameter')
        ax1.set_xlim([0,0.8])
        a = time_with_ecog[0, start_index:]
        b = time_with_ecog[count+1, start_index:]
        ax2 = ax1.twinx()
        ax2.plot(a, b, color = plot_colors_line[count+3], lw= 0.8, ls='-')
        ax2.set_ylabel('HFB Power')
        plots.title('Subject ' + str(subject) + ', Channel ' + str(channel_name) +
                            ', Condition '+ str(merged.names[i]), fontsize = 10)
        ax1.legend(labels = ['Pupil', 'ECoG'], loc='upper right', fontsize=7)
        plots.gcf().subplots_adjust(left=0.15)
        plots.savefig(make_path('pupil_ecog_correlation_'+str(merged.names[i])+str(subject), '.png',
                        out_dir=out_dir, base_name=str(channel_name)),dpi=600,bbox_inches='tight')

        if all_channels:
            if show:
                plots.show()
        else:
            plots.close()

    return fig1
