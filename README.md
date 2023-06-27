# Subtitles Transformation

## Goal

Programmatically add subtitles to video (MP4) from CSV transcripts and timestamps

## Prerequisites
- Python 3.x
- Required Python packages: `os`, `pysrt`, `csv`, `moviepy.editor`

## Cloning
To clone the repository on local machine, run:
```
git clone https://github.com/farooqashar/Subtitles.git
```

## Running Locally 

1. change input and output folder path 
2. add an MP4 file to add subtitles to and a subtitles .srt file with the same name to the input folder 
2. cd into the Subtitles folder and run:

```
python3 final.py
```

## Code

The project is structured as follows:

- `final.py` contains the main project code to take in the input, create subtitle clips, perform formatting changes, and burns the subtiltes before writing out the outout video.
- `/input` contains video input .mp4 files and their respective subtitles .srt files with same name
- `/output` contains output video .mp4 files with subtitles added
- `SRT.py` contains the main project code to generate a subtitles .srt file from the relevant CSV file
