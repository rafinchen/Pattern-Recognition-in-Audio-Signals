import numpy as np            # For numerical operations and signal generation
import pyaudio                # For audio playback

# Function to play generated audio samples
def play_sound(samples, volume=0.7, fs=44100):
    p = pyaudio.PyAudio()
    # Open a PyAudio stream with float32 format and given sample rate
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
    # Convert samples to bytes and write to stream
    stream.write((volume * samples).astype(np.float32).tobytes())
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()  # Terminate the PyAudio session

# Variant 1: Two sine waves combined with amplitude modulation
def variant_1_basic_dual_tone():
    fs = 44100                # Sampling rate in Hz
    duration = 5.0            # Duration in seconds
    t = np.arange(int(fs * duration)) / fs  # Time array

    freq1 = 440.0             # Frequency of tone 1 (A4)
    freq2 = 660.0             # Frequency of tone 2 (E5)

    # Amplitude modulation to create a pulsing effect
    mod = 0.5 * np.sin(2 * np.pi * 2 * t) + 0.5

    # Combined signal of two tones, modulated
    samples = (
        np.sin(2 * np.pi * freq1 * t) +
        0.6 * np.sin(2 * np.pi * freq2 * t)
    ) * mod

    return samples  # Return the generated audio samples

# Variant 2: Pitch sweep with gradually added harmonics
def variant_2_pitch_sweep():
    fs = 44100                # Sampling rate
    duration = 6.0            # Duration in seconds
    t = np.arange(int(fs * duration)) / fs  # Time array

    # Sweep frequency from 220 Hz to 880 Hz (low to high)
    sweep = np.linspace(220.0, 880.0, len(t))

    # Base tone plus 2 harmonics (2x and 3x frequency)
    base = np.sin(2 * np.pi * sweep * t)
    harmonic1 = 0.4 * np.sin(2 * np.pi * 2 * sweep * t)
    harmonic2 = 0.3 * np.sin(2 * np.pi * 3 * sweep * t)

    # Envelopes to gradually fade in the harmonics
    env1 = np.linspace(0, 1, len(t))
    env2 = np.linspace(0, 1, len(t))**2

    # Final sound with slight background noise for texture
    samples = base + env1 * harmonic1 + env2 * harmonic2 + 0.02 * np.random.randn(len(t))

    return samples

# Variant 3: Experimental sound using noise and square wave modulation
def variant_3_noise_experiment():
    fs = 44100                # Sampling rate
    duration = 5.0            # Duration in seconds
    t = np.arange(int(fs * duration)) / fs  # Time array

    # Base tone at 300 Hz
    base = np.sin(2 * np.pi * 300 * t)

    # Random noise modulated with a slow sine wave (7 Hz)
    noise = np.random.uniform(-1, 1, len(t)) * np.sin(2 * np.pi * 7 * t)

    # Square wave modulation (creates a pulsing, glitchy effect)
    pulse = np.sign(np.sin(2 * np.pi * 2 * t))

    # Final mix of base tone and modulated noise
    samples = 0.6 * base + 0.3 * noise * pulse

    return samples

# === Interactive selection menu ===
print("\n🎛 Sound Generator – Choose your variant:\n")
print("1. Dual Tone with Modulation")
print("2. Pitch Sweep with Harmonics (Extra Feature)")
print("3. Experimental Noise-Based Sound\n")

# Get user input
choice = input("Enter number (1, 2 or 3): ")

# Run the corresponding sound variant
if choice == "1":
    print("▶ Playing Variant 1: Dual Tone...")
    play_sound(variant_1_basic_dual_tone())

elif choice == "2":
    print("▶ Playing Variant 2: Pitch Sweep...")
    play_sound(variant_2_pitch_sweep())

elif choice == "3":
    print("▶ Playing Variant 3: Noise Experiment...")
    play_sound(variant_3_noise_experiment())

else:
    print("Invalid choice. Please run again and select 1, 2, or 3.")
