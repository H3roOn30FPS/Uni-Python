import numpy as np
from scipy.io import wavfile

class MusicGenerator:

    def __init__(self, sampling_rate):
        self.sampling_rate = sampling_rate

    def generate_sine_wave(self, frequency, duration, amplitude):
        """
        Generates a simple audio signal with a sine wave form.

        Arguments:
            frequency: The frequency of the signal in Hz.
            duration: The duration of the signal in seconds.
            amplitude: The amplitude of the signal.

        Returns:
            A simple audio signal with a sine wave form.
        """

        # Calculate number of samples

        # Generate a time scale.

        # Form the audio signal.
        audio_signal = 

        return audio_signal

    def generate_music(self, notes):
        """
        Generates a simple musical composition.

        Arguments:
            notes: A list of notes to play.

        Returns:
            composed music.
        """

        # Generate the audio signals for each note.
        composed_music = np.array([])
        for note in notes:
            note_length = note[2]
            audio_signal = self.generate_sine_wave(note[1], note_length, 0.2)
            composed_music = np.append(composed_music, audio_signal)

        return composed_music

    def save_signal_to_wav(self, filename, signal):
        """
        Save a signal to a WAV file.

        Arguments:
            filename (str): The name of the output WAV file.
            signal (numpy.ndarray): The signal data as a NumPy array.

        Returns:
            None
        """
        
        # Calculate the maximum amplitude of the signal
        
        
        # Normalize the signal to the range [-1, 1]
        
        
        # Write the signal to a WAV file
        

def main():

    sampling_rate = 44100
    
    # Create a music generator with the given sampling rate
    music_generator = 

    # Define musical notes with frequency and duration for "Für Elise" in a higher octave
    notes = [
        ('E5', 659.26, 0.5),   # E in the 5th octave
        ('D#5', 622.25, 0.5),  # D# in the 5th octave
        ('E5', 659.26, 0.5),   # E in the 5th octave
        ('D#5', 622.25, 0.5),  # D# in the 5th octave
        ('E5', 659.26, 0.5),   # E in the 5th octave
        ('B4', 493.88, 0.5),   # B in the 4th octave
        ('D5', 587.33, 0.5),   # D in the 5th octave
        ('C5', 523.25, 0.5),   # C in the 5th octave
        ('A4', 440.00, 1),   # A in the 4th octave
    ]

    # Generate the music.
    composed_music = music_generator.

    # Save the music.
    music_generator.save_signal_to_wav("composed_music.wav", composed_music)

if __name__ == "__main__":
    main()