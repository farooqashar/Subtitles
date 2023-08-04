#generating srt file.
#Code Sample to convert CSV file to a subtitle file in srt format:

'''
To remove speaker for the English text:
1. uncomment the section `# Removing Speaker for English Text`


To remove speaker for the Non-English text:
1. uncomment the section `# Removing Speaker for Non-English Text`

'''

import csv
import os


def generate_srt_file(csv_file_path, srt_file_path):
    with open(csv_file_path, 'r') as csv_file, open(srt_file_path, 'w') as srt_file:
        reader = csv.reader(csv_file)
        reader_list = list(reader)

        subtitle_count = 1

        for row_index, row in enumerate(reader_list, start=1):
            if row_index == len(reader_list):
                continue
            start_time = row[0] + ",000"
            start_time = start_time.replace(" ", "")
            next_row = reader_list[row_index]
            #if time is an empty string
            if next_row[0] == "":
                next_row_2 = reader_list[row_index + 1]
                end_time = next_row_2[0] + ",000"
                end_time = end_time.replace(" ", "")
                subtitle_text_1 = row[1] + next_row[1]
                subtitle_text_2 = row[2] + next_row[2]

                # #removing the first word of English 
                # split_subtitle_text_1 = subtitle_text_1.split(' ', 1)
                # if len(split_subtitle_text_1) > 1:
                #     subtitle_text_1 = split_subtitle_text_1[1]
                # else:
                #     subtitle_text_1 = ""


                #removing first word from non-english subtitles

                # split_subtitle_text_2 = subtitle_text_2.split(' ', 1)
                # if len(split_subtitle_text_2) > 1:
                #     subtitle_text_2 = split_subtitle_text_2[1]
                # else:
                #     subtitle_text_2 = ""

                #add column after non english speaker:
                subtitle_text_2_ls = subtitle_text_2.split()
                if len(subtitle_text_2_ls) > 0:
                    subtitle_text_2_ls[0] += ":"
                subtitle_text_2 = ' '.join(subtitle_text_2_ls)


            else:
                end_time = next_row[0] + ",000"
            
                end_time = end_time.replace(" ", "")
                subtitle_text_1 = row[1] 
                subtitle_text_2 = row[2]

                # #removing the first word of English 
                # split_subtitle_text_1 = subtitle_text_1.split(' ', 1)
                # if len(split_subtitle_text_1) > 1:
                #     subtitle_text_1 = split_subtitle_text_1[1]
                # else:
                #     subtitle_text_1 = ""


                #removing first word from non-english subtitles

                # split_subtitle_text_2 = subtitle_text_2.split(' ', 1)
                # if len(split_subtitle_text_2) > 1:
                #     subtitle_text_2 = split_subtitle_text_2[1]
                # else:
                #     subtitle_text_2 = ""

                # #add column after non english speaker:
                # subtitle_text_2_ls = subtitle_text_2.split()
                # if len(subtitle_text_2_ls) > 0:
                #     subtitle_text_2_ls[0] += ":"
                # subtitle_text_2 = ' '.join(subtitle_text_2_ls)

            # Handling language encoding for Afrikaans tags
            if "<afr>" in subtitle_text_2 and "</afr>" in subtitle_text_2:
                subtitle_text_2=subtitle_text_2.replace("<afr>","$")
                subtitle_text_2=subtitle_text_2.replace("</afr>","$")
        
            # Handling language encoding for Nama tags
            if "<nam>" in subtitle_text_2 and "</nam>" in subtitle_text_2:
                subtitle_text_2=subtitle_text_2.replace("<nam>","+")
                subtitle_text_2=subtitle_text_2.replace("</nam>","+")

            # Handling language encoding for N|uu tags
            if "<nuu>" in subtitle_text_2 and "</nuu>" in subtitle_text_2:
                subtitle_text_2=subtitle_text_2.replace("<nuu>",">")
                subtitle_text_2=subtitle_text_2.replace("</nuu>",">")

            # # Removing Speaker for English Text
            # split_subtitle_text_1 = subtitle_text_1.split(':', 1)
            # if len(split_subtitle_text_1) > 1:
            #     subtitle_text_1 = split_subtitle_text_1[1]
            # else:
            #     subtitle_text_1 = ""
                
            # # Removing Speaker for Non-English Text
            # subtitle_text_2 = subtitle_text_2.split(':', 1)
            # if len(subtitle_text_2) > 1:
            #     subtitle_text_2 = subtitle_text_2[1]
            # else:
            #     subtitle_text_2 = ""      

            subtitle_text_1.lstrip()
            subtitle_text_2.lstrip()

            srt_file.write(str(subtitle_count) + '\n')
            srt_file.write(start_time + ' --> ' + end_time + '\n')
            srt_file.write(subtitle_text_1 + '\n')
            srt_file.write('--' + '\n')
            srt_file.write(subtitle_text_2 + '\n\n')

            subtitle_count += 1


# Usage Example
#You can generate the csv files from pdf_to_csv.py and then use the csv files inside outputcsv folder.

## SETUP ##

# FOR DOING DIRECTORY
# Define the input and output folder paths
csv_input_folder = '/Users/asharfarooq/Downloads/Uliza/Subtitles/inputsrt'
srt_output_folder = '/Users/asharfarooq/Downloads/Uliza/Subtitles/outputsrt'

# Create the output folder if it doesn't exist
if not os.path.exists(srt_output_folder):
    os.makedirs(srt_output_folder)

# Iterate over each file in the input folder
for file_name in os.listdir(csv_input_folder):
    # Construct the full file paths
    csv_file_path = os.path.join(csv_input_folder, file_name)
    srt_file_path = os.path.join(srt_output_folder, f'{os.path.splitext(file_name)[0]}.srt')

    generate_srt_file(csv_file_path, srt_file_path)

# FOR DOING ONE FILE
# Define the input and output folder paths
# csv_input_file_path = '/Users/asharfarooq/Downloads/Uliza/Subtitles/inputsrt/1997_01-01transcript.csv'
# srt_output_file_path = "/Users/asharfarooq/Downloads/Uliza/Subtitles/outputsrt/1997_01-01transcript.srt"
# generate_srt_file(csv_input_file_path, srt_output_file_path)







