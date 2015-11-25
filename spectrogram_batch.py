#Batch spectrogram analysis script by Robert Blaauboer
#Create a spectrograms directory relative to wav files in a file structure
#and fills it with a low- and high-frequency spectrogram per file

import subprocess, os
import configparser

#Directory to start from
rootDir = '.'
#folder to save spectrograms in
#will be created relative to the wav file
folder = "spectrograms";
soxPath = 'C:\Program Files (x86)\sox-14-4-2\sox';

config = configparser.ConfigParser()
config.optionxform = str
config.read('settings.ini')

s_low = []
for key in config['spectro-proc-low']:
    s_low.append(key)
    s_low.append(config['spectro-proc-low'][key])

s_high = []
for key in config['spectro-proc-high']:
    s_high.append(key)
    s_high.append(config['spectro-proc-high'][key])

s_spectro_settings = []
for key in config['spectro-settings']:
    s_spectro_settings.append(key)
    if config['spectro-settings'][key]:
        s_spectro_settings.append(config['spectro-settings'][key])

s_suffix_low = config['spectro-suffix']['low']
print(s_suffix_low)
s_suffix_high = config['spectro-suffix']['high']

overwrite_files = config['spectro-general']['overwrite']


for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for filename in fileList:
        if filename.endswith('.wav'):
            absolute_folder = dirName + '/' + folder
            if not os.path.exists(absolute_folder):
                os.makedirs(absolute_folder)

            s_prefix = [soxPath, dirName + '/' + filename, '-n'];

            s_spectro_low = s_prefix + s_low + ['spectrogram'] + s_spectro_settings;
            s_spectro_high = s_prefix + s_high + ['spectrogram'] + s_spectro_settings;

            if not os.path.exists(absolute_folder + '/' + filename[:-4] + s_suffix_low) or overwrite_files == 'true':
                print( dirName + '/' + folder + '/' + filename[:-4] + s_suffix_low)
                subprocess.call(s_spectro_low + ['-o', dirName + '/' + folder + '/' + filename[:-4] + s_suffix_low])
            if not os.path.exists(absolute_folder + '/' + filename[:-4] + s_suffix_high) or overwrite_files == 'true':
                print( dirName + '/' + folder + '/' + filename[:-4] + s_suffix_high)
                subprocess.call(s_spectro_high + ['-o',dirName + '/' + folder + '/' + filename[:-4] + s_suffix_high])