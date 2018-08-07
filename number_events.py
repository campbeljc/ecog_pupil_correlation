'''
File that reads in the pupil diameter data
'''
import pandas as pd
import numpy as np
from misc import make_path


def read_pupil(path):
    """
    Given a path to the pupil diameter data, returns a Dataframe with the
    given info. Inputs may be of .txt, .xlsx, or .csv.
    """
    print('\nLoading in the data...\n')
    tail = path[-4:]
    raw = None
    if tail == '.txt':
        raw = pd.read_csv(path, delimiter='\t')
    elif tail == 'xlsx':
        raw = pd.read_excel(path)
    elif tail == '.csv':
        raw = pd.read_csv(path)
    else:
        raise ValueError('Please select a .txt, .xlsx or .csv file. ')

    raw.columns = ['Time', 'Pupil', 'Content']

    # If the Pupil is not already a numeric type, make it so.
    if not np.issubdtype(raw['Pupil'].dtype, np.number):
        raw.Pupil.replace({'-': np.nan}, inplace=True)
        raw.Pupil = pd.to_numeric(raw.Pupil)
    return raw

eye_path = '/Users/Parvizi/Desktop/JENNA/Python/Pupil/EmotionalFaces/Pipeline Inputs and Outputs/119/Block2/pupil_EF_119_Block2.txt'
pupil_data = read_pupil(eye_path)
out_dir = '/Users/Parvizi/Desktop/JENNA/Python/Pupil'
#pupil_data.to_csv(make_path('preprocessed', '.csv', out_dir=out_dir,
                            #base_name='event_test'), index=False)

pupil_events = pupil_data[pupil_data['Content'] != '-']
num_events = len(pupil_events)
print('There are {} events in the pupil data, does '
        'this look correct? If not, the first two events '
        'of pupil may not have been recorded...'.format(num_events))
