params = {}

#'yes' if you want to run all channels stored in a directory. 'no' if you want to run a single channel
params['all_channels'] = True

# True if you want to select the files with a GUI
params['choose_files'] = True

# List of paths for pupil_data relative to the main folder
# Note: only effective if choose_files is False
params['eye_paths'] = ['/Users/Parvizi/Desktop/JENNA/Python/Pupil_ECoG_correlation/Appraisal Audio/114/Block1/pupil_Appraisal_114_Block1.txt']

# Same as eye_paths for the events files
params['events_paths'] = ['/Users/Parvizi/Desktop/JENNA/Python/Pupil_ECoG_correlation/Appraisal Audio/114/Block1/eventsSODATA_DCchans_E17-526_0023.mat']

#Same as eye_paths for the ecog get_files
params['ecog_path']= ['/Users/Parvizi/Desktop/JENNA/Python/Pupil_ECoG_correlation/Appraisal Audio/114/Block1/Epoched_HFB_signal_window.mat']

# In hertz
params['sample_rate'] = 250

# Number of milliseconds to epoch after trial onset (ms)
params['epoch_time'] = 1000

# Number of milliseconds prior to epoch to show
# Multiple of 4 please :)
params['back_time'] = 60

# List of conditions (indices (e.g. [1, 2, 3]) to be plotted, or 'all' for all conditions. Based on pupil data
params['conds_to_plot'] = [1, 2, 3]

# List of colors (in hex) to plot. Google 'color picker to help find hex values'
# NOTE you need to add to this if you're plotting more than 10 conditions.

#Use these for colored lines on graph
params['plot_colors_scatter'] = ['#ff0000', '#0000ff', '#009933', '#ff9999', '#0099ff', '#85e085', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

#Use these for dashed/solid black lines on graph
params['plot_colors_line'] = ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
params['line_style'] = '--'

# File name of the plot
params['plot_fname'] = 'pupil_diameter_plot'

#Channel name for ECoG Correlation
params['subject_number'] = '119'

#Creates a scatter plot that plots pupil diameter vs HFB signal. Set scatter_plot to 'normal'
#to compare values of diameter and HFB directly or 'derivative' to compare the derivatives.
#Set to 'none' to not create a scatter plotself.
params['scatter_plot'] = 'none'

#show plots as you graph them
params['show']= False
