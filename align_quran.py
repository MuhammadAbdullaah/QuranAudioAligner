import torch
import glob
import os
import json

from ctc_forced_aligner import (
    load_audio,
    load_alignment_model,
    generate_emissions,
    preprocess_text,
    get_alignments,
    get_spans,
    postprocess_results,
)

text_dir = "dataset/text/"
audio_dir = "dataset/audio/"
segments_dir = "timestamps/alnafes"

os.makedirs(segments_dir, exist_ok=True)

language = "ara"  # ISO-639-3 Language code
device = "cuda" if torch.cuda.is_available() else "cpu"
batch_size = 16


# Load model
alignment_model, alignment_tokenizer = load_alignment_model(
    device, dtype=torch.float16 if device == "cuda" else torch.float32
)

# Process all text files
text_files = glob.glob(os.path.join(text_dir, "*.txt"))

for text_path in text_files:
    filename = os.path.basename(text_path).replace(".txt", "")
    audio_path = os.path.join(audio_dir, f"{filename}.wav")
    segment_file_path = os.path.join(segments_dir, f"{filename}.json")

    if not os.path.exists(audio_path):
        print(f"Skipping {filename}: Audio file not found")
        continue

    print(f"Processing {text_path}")

    audio_waveform = load_audio(audio_path, alignment_model.dtype, alignment_model.device)


    with open(text_path, "r") as f:
        lines = f.readlines()
    text = "".join(line for line in lines).replace("\n", " ").strip()
    print(text)

    emissions, stride = generate_emissions(
      alignment_model, audio_waveform, batch_size=batch_size
    )

    tokens_starred, text_starred = preprocess_text(
      text,
      romanize=True,
      language=language,
    )

    segments, scores, blank_token = get_alignments(
      emissions,
      tokens_starred,
      alignment_tokenizer,
    )


    spans = get_spans(tokens_starred, segments, blank_token)

    word_timestamps = postprocess_results(text_starred, spans, stride, scores)
    print(word_timestamps)
    with open(segment_file_path, "w", encoding="utf-8") as f:
        json.dump(word_timestamps, f, ensure_ascii=False, indent=2)