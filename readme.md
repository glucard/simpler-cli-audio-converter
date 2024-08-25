# SIMPLER CLI AUDIO CONVERTER

Simplifier audio convertion on folders struct

## Requirements

- ffmpeg
- Python
- Git

## Installation

### Linux/WSL

1. Install ffmpeg:
    ```bash
    sudo apt update && sudo apt upgrade
    sudo apt install ffmpeg
    ```
2. Install __SCAC__ repository:
    ```bash
    git clone https://github.com/glucard/simpler-cli-audio-converter
    cd simpler-cli-audio-converter
    pip install .
    ```

## Usage

### Linux/WSL

```bash
scac "path/to/source_audios_folder" "path/to/converted_audios_dest" --sf "mp3" --tf "wav"
```
