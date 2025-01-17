import numpy as np

def waveform_to_frames(waveform, frame_length, step):
    num_frames = int((len(waveform) - frame_length) / step) + 1
    frames = np.zeros((frame_length, num_frames))
    
    for t in range(num_frames):
        start_idx = t * step
        frames[:, t] = waveform[start_idx:start_idx + frame_length]
    
    return frames

def frames_to_stft(frames):
    return np.fft.fft(frames, axis=0)

def stft_to_spectrogram(stft):
    magnitude = np.abs(stft)
    spectrogram = 20 * np.log10(magnitude + 1e-10)
    spectrogram -= np.amax(spectrogram)
    spectrogram = np.clip(spectrogram, -60, 0)
    return spectrogram