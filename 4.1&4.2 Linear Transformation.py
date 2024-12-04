import numpy as np
import pandas as pd
import soundfile as sf
import librosa
from scipy.signal import stft

synth_file = '/Users/lucas/Desktop/24fall/2595MACHINE LEARNING/hw2/INFSCI_2595_F24_HW2-1/hw2materials/audio/Synth.wav'
piano_file = '/Users/lucas/Desktop/24fall/2595MACHINE LEARNING/hw2/INFSCI_2595_F24_HW2-1/hw2materials/audio/Piano.wav'
blinding_lights_file = '/Users/lucas/Desktop/24fall/2595MACHINE LEARNING/hw2/INFSCI_2595_F24_HW2-1/hw2materials/audio/BlindingLights.wav'

audio_A, sr = sf.read(synth_file)
audio_B, _ = sf.read(piano_file)
audio_C, _ = sf.read(blinding_lights_file)

# Compute the magnitude spectrograms with a window length of 1024
f_A, t_A, Zxx_A = stft(audio_A, sr, nperseg=1024, noverlap=256)
M_A = np.abs(Zxx_A)

f_B, t_B, Zxx_B = stft(audio_B, sr, nperseg=1024, noverlap=256)
M_B = np.abs(Zxx_B)

f_C, t_C, Zxx_C = stft(audio_C, sr, nperseg=1024, noverlap=256)
M_C = np.abs(Zxx_C)
phase_C = Zxx_C / (M_C + 1e-16)

# Step 1: Compute the transformation matrix T
M_A_pseudo_inverse = np.linalg.pinv(M_A)
T = np.dot(M_B, M_A_pseudo_inverse)

# Step 2: Compute the Frobenius norm of the error ||T M_A - M_B||_F^2
error = np.sum((np.dot(T, M_A) - M_B) ** 2)
print(f"Frobenius norm ||T M_A - M_B||_F^2: {error}")

# Ensure labels match the dimensions of the matrices
freq_labels = [f'Freq_{i}' for i in range(T.shape[0])]
time_labels_T = [f'Time_{j}' for j in range(T.shape[1])]
time_labels_D = [f'Time_{j}' for j in range(M_C.shape[1])]

df_T = pd.DataFrame(T, index=freq_labels, columns=time_labels_T)
df_T.to_csv("/Users/lucas/Desktop/24fall/2595MACHINE LEARNING/hw2/INFSCI_2595_F24_HW2-1/problem3t.csv", float_format="%.8f")

# Step 3: Apply T to M_C to estimate M_D
M_D = np.dot(T, M_C)

# Ensure the time labels for M_D match its shape
df_M_D = pd.DataFrame(M_D, index=freq_labels, columns=time_labels_D)
df_M_D.to_csv("/Users/lucas/Desktop/24fall/2595MACHINE LEARNING/hw2/INFSCI_2595_F24_HW2-1/problem3md.csv", float_format="%.8f")

# Step 4: Recompose the time-domain signal using the phase from M_C
M_D_with_phase = M_D * phase_C
signal_hat = librosa.istft(M_D_with_phase, hop_length=256, center=False, win_length=1024)

sf.write("/Users/lucas/Desktop/24fall/2595MACHINE LEARNING/hw2/INFSCI_2595_F24_HW2-1/problem3.wav", signal_hat, sr)
