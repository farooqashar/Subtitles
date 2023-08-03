# Parsing PDF To XML and CSV Files

## Background and Goal

The transcripts and language tags for the Digital Preservation of N|uu Language project are not in an easy, machine readable format. They’re in Word docs and PDF, designed for reading by humans. This project designs a script that can parse the information needed from these files and save it in XML and CSV formats with CSV file providing readability. 

## Prerequisites

- Python 3.x
- Required Python packages: `os`, `docx`, `csv`, `xml.etree.ElementTree`, `pdf2docx`

## Cloning
To clone the repository on local machine, run:
```
git clone https://github.com/uliza/ParseText.git
```
## Running Locally 

1.change input and output folder path 
2.cd into the Parsing folder and run:

```
python3 pdf_to_csv.py
```

## Code

The project is structured as follows:

- `pdf_to_csv.py` contains the main project code to take in the input, perform parsing, extracting relevant information, and composing XML and CSV files
- `/input` contains files that need to be translated into XML and CSV files
  - `INPUT.docx` contains the input table in the form of a conversation that includes timeframe, English translation, different text colors for different languages, and any notes. 
- `/output` contains files related to user concept
  - `INPUT.csv` contains the input transformed into a CSV file with columns representing time, English translation with speaker tags, language tags along with speaker tags, and notes
  - `INPUT.xml` contains the input transformed into a hierarchical  XML file containing `<time>`, `<speaker>`, `<eng>`, language tags (`<afr>`,`<nam>`,`<nuu>`), and `<notes>` tags


## Customization

- You can customize the color-to-language mapping by updating the `color_to_language` dictionary in the script.
