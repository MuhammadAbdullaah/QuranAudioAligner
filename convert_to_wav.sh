#!/bin/bash

# Set input and output directories
INPUT_DIR="/home/infiniti/Tarteel/Task2/lafzize/script/script/dataset/audio"
OUTPUT_DIR="/home/infiniti/Tarteel/Task2/lafzize/script/script/dataset"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Loop through all audio files in the input directory
for file in "$INPUT_DIR"/*; do
    if [[ -f "$file" ]]; then
        filename=$(basename -- "$file")
        output_file="$OUTPUT_DIR/${filename%.*}.wav"

         # Skip conversion if output file already exists
        if [[ -f "$output_file" ]]; then
            echo "✅ Skipping: $output_file (Already exists)"
            continue
        fi

        # Convert to WAV with 16kHz sample rate
        ffmpeg -i "$file" -ac 1 -ar 16000 "$output_file"

        echo "Converted: $filename -> $output_file"
    fi
done

echo "All files converted successfully!"

#to run this file 
# run command bash convert_to_wav.sh
