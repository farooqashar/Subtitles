#generating srt file.
#Code Sample to convert CSV file to a subtitle file in srt format:

import csv


def generate_srt_file(csv_file_path, srt_file_path):
    with open(csv_file_path, 'r') as csv_file, open(srt_file_path, 'w') as srt_file:
        reader = csv.reader(csv_file)
        #next(reader)  # Skip the header row if present
        reader_list = list(reader)

        subtitle_count = 1
        #print("reached1")

        for row_index, row in enumerate(reader_list, start=1):
            if row_index <= 9 or row_index == len(reader_list):
                continue
            start_time = row[0] + ",000"
            start_time = start_time.replace(" ", "")
            next_row = reader_list[row_index]
            end_time = next_row[0] + ",000"
            end_time = end_time.replace(" ", "")
            subtitle_text_1 = row[1]
            subtitle_text_2 = row[2]

            #removing the first word of both English and Non-English Subtitles:
            split_subtitle_text_1 = subtitle_text_1.split(' ', 1)
            if len(split_subtitle_text_1) > 1:
                subtitle_text_1 = split_subtitle_text_1[1]
            else:
                subtitle_text_1 = ""

            split_subtitle_text_2 = subtitle_text_2.split(' ', 1)
            if len(split_subtitle_text_2) > 1:
                subtitle_text_2 = split_subtitle_text_2[1]
            else:
                subtitle_text_2 = ""


            srt_file.write(str(subtitle_count) + '\n')
            srt_file.write(start_time + ' --> ' + end_time + '\n')
            srt_file.write(subtitle_text_1 + '\n')
            srt_file.write('--' + '\n')
            srt_file.write(subtitle_text_2 + '\n\n')

            subtitle_count += 1


# Usage example
csv_file_path = 'Parsing2/output/sample3.csv'
srt_file_path = 'subtitlessss.srt'
generate_srt_file(csv_file_path, srt_file_path)








