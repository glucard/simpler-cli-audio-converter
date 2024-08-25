# scac (simpler cli audio converter)

import argparse
import os
from pydub import AudioSegment

def convert_audio(input_path:str, output_path:str, source_format:str, target_format:str):
    audio = AudioSegment.from_file(input_path, codec=source_format)
    audio.export(f"{output_path}.{target_format}", format=target_format)

def recursive_convert_dir(input_path: str, output_path: str, source_format:str, target_format:str):
    if os.path.isdir(input_path):
        if not os.path.isdir(output_path):
            os.mkdir(output_path)

        for p in os.listdir(input_path):
            recursive_convert_dir(os.path.join(input_path, p), os.path.join(output_path, p), source_format, target_format)

    if output_path.split('.')[-1] == source_format:
        convert_audio(input_path, output_path, source_format, target_format)
        print(f"{input_path} to {output_path}.{target_format}")

    return

def main():
    parser = argparse.ArgumentParser(description="A simple audio converter CLI tool.")
    parser.add_argument("source_path", help="Path to the source audios dir.")
    parser.add_argument("target_path", help="Path to the output audios dir.")
    parser.add_argument("--sf", default="opus", help="Source audio format (default: opus)")
    parser.add_argument("--tf", default="wav", help="Output audio format (default: wav)")

    args = parser.parse_args()

    if not os.path.isdir(args.source_path):
        raise ValueError(f"{args.source_path} is not a dir.")
    
    if not os.path.isdir(args.target_path):
        os.mkdir(args.target_path)
        # raise ValueError(f"{args.target_path} is not a dir.")
    
    recursive_convert_dir(args.source_path, args.target_path, args.sf, args.tf)

if __name__ == "__main__":
    main()
