# SIMPLER CLI AUDIO CONVERTER

Simplifier audio convertion on folders struct

## Requirements

- ffmpeg
- Python
- Git

## Installation


### 1. Install ffmpeg:

#### Linux/WSL
-   ```bash
    sudo apt update && sudo apt upgrade
    sudo apt install ffmpeg

    ```

#### Windows
- <a href="https://phoenixnap.com/kb/ffmpeg-windows">Install ffmpeg on Windows</a>

### 2. Install __SCAC__ repository:
```bash
git clone https://github.com/glucard/simpler-cli-audio-converter
cd simpler-cli-audio-converter
pip install .

```

## Usage

```bash
scac "path/to/source_audios_folder" "path/to/converted_audios_dest" --sf "mp3" --tf "wav"
```
