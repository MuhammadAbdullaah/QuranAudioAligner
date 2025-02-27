# Forced Alignment Tool

A repository that aligns audio with its corresponding text using deep learning. This tool processes audio files and their matching text files to generate precise word-level timestamps, which are useful in speech recognition, transcription, and linguistic research. Additionally, the repository includes a utility script to convert audio files to a standardized WAV format (16kHz, mono) using ffmpeg.

#useage 
- To run this, you need to provide the path to a directory containing all your audio files (e.g., audio1.wav) and the path to a directory containing all your text files (e.g., 1.txt)

## Features

- **Forced Alignment:** Automatically align audio with text and generate word-level timestamps.
- **Audio Conversion:** Convert audio files to WAV format with 16kHz sample rate and mono channel.
- **Deep Learning:** Leverage deep learning models for high accuracy in alignment tasks.

## Dependencies

### Python Dependencies

- Python 3.7+
- [PyTorch]
- [ctc-forced-aligner](https://github.com/MahmoudAshraf97/ctc-forced-aligner) 

Install the required Python packages using pip:
```bash
pip install torch numpy ctc-forced-aligner
