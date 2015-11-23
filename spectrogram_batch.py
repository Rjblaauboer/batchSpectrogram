#Batch spectrogram analysis script by Robert Blaauboer
#Create a spectrograms directory relative to wav files in a file structure
#and fills it with a low- and high-frequency spectrogram per file

import subprocess, glob, os

#Directory to start from
rootDir = '.'
#folder to save spectrograms in
#will be created relative to the wav file
folder = "spectrograms";
soxPath = 'C:\Program Files (x86)\sox-14-4-2\sox';


for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        if fname.endswith('.wav'):
            absolute_folder = dirName + '/' + folder
            if not os.path.exists(absolute_folder):
                os.makedirs(absolute_folder)

            s_prefix = [soxPath, dirName + '/' + fname, '-n'];

            s_low = ['rate', '6k'];
            s_high = ['highpass', '16k'];

            s_spectro = ['spectrogram'];
            s_spectro_low = s_prefix + s_low + s_spectro;
            s_spectro_high = s_prefix + s_high + s_spectro;

            if not os.path.exists(absolute_folder + '/' + fname[:-4] + '-spectro_low.png'):
                subprocess.call(s_spectro_low + ['-o', dirName + '/' + folder + '/' + fname[:-4] + '-spectro_low.png'])
            if not os.path.exists(absolute_folder + '/' + fname[:-4] + '-spectro_high.png'):
                subprocess.call(s_spectro_high + ['-o',dirName + '/' + folder + '/' + fname[:-4] + '-spectro_high.png'])