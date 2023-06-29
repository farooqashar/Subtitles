# CSV to SRT Converter

This code is a Python script that converts a CSV file containing subtitle information into a SubRip Subtitle (SRT) file. The script processes the CSV file and generates an SRT file with timed subtitles.

## Usage

1. Ensure you have Python installed on your system.
2. Prepare the CSV file that contains the subtitle information. You can generate the CSV file using the `finalcsv.py` script. Your csv files will be saved inside the `outputcsv` folder.
3. Modify the `csv_file_path` variable to specify the path of your input CSV file. For example:
   ```
   csv_file_path = 'outputcsv/sample4.csv'
   ```
5. Modify the `srt_file_path` variable to specify the desired path for the output SRT file. For example:
   ```
   srt_file_path = 'bothspeakers.srt'
   ```
6. Uncomment the desired section based on your requirements. The script provides two options:
   - To show both speakers, uncomment the following code block:
     ```
     # removing the first word of English 
     # add column after non-english speaker
     ```
   - To show no speakers, uncomment the following code block:
     ```
     # removing everything before ":"
     # removing first word from non-english subtitles
     ```
7. Save the changes to the script.
8. Run the script. It will read the CSV file, process the subtitle data, and generate the corresponding SRT file.

**Note:** Make sure you have the necessary permissions to read the CSV file and write the SRT file in the specified locations.

## Important Notes

- The script assumes that the CSV file follows a specific format where each row represents a subtitle entry. Modify the script accordingly if your CSV file structure is different.
- The generated SRT file will contain the subtitle text along with the corresponding start and end timestamps.

Feel free to customize and use this script to convert your CSV files to SRT format for subtitle processing or integration into video players.