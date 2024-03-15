import h5py
import numpy as np
import pandas as pd
import glob
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def init_df():
    columns = {
        'danceability': [],
        'song_hotttnesss': [],
        'energy': [],
        'duration': [],
        'key': [],
        'loudness': [],
        'tempo': [],
        'time_signature': [],
        'year': []
    }
    df = pd.DataFrame(columns)
    return df

def add_song(df, filename):
    # Open the HDF5 file in read mode
    with h5py.File(filename, 'r') as file:
        new_song = pd.DataFrame([{
            'danceability': file['analysis']['songs'][0][2],
            'song_hotttnesss': file['metadata']['songs'][0][16],
            'energy': file['analysis']['songs'][0][5],
            'duration': file['analysis']['songs'][0][3],
            'key': file['analysis']['songs'][0][21],
            'loudness': file['analysis']['songs'][0][23],
            'tempo': file['analysis']['songs'][0][27],
            'time_signature': file['analysis']['songs'][0][28],
            'year': file['musicbrainz']['songs'][0][1]
        }])
        df = pd.concat([df, new_song], ignore_index=True)
    return df

if __name__ == '__main__':
    df = init_df()
    song_paths = glob.glob('./MillionSongSubset/*/*/*/*.h5')
    for i in range(10000): # Max 10000
        if i % 100 == 0:
            print(i)
        df = add_song(df, song_paths[i])
    df.to_csv('MillionSongSubset.csv', index=False)