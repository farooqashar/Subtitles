#generating srt file.
#Code Sample to convert CSV file to a subtitle file in srt format:

'''
To show both speakers you will need to uncomment the following:
1.removing the first word of English 
2.add column after non english speaker:


To show no speakers you will need to uncomment the following:
1.removing everything before ":"
2.removing first word from non-english subtitles

'''

import csv


def generate_srt_file(csv_file_path, srt_file_path):
    with open(csv_file_path, 'r') as csv_file, open(srt_file_path, 'w') as srt_file:
        reader = csv.reader(csv_file)
        reader_list = list(reader)

        subtitle_count = 1

        for row_index, row in enumerate(reader_list, start=1):
            if row_index <= 9 or row_index == len(reader_list):
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

                #removing the first word of English 
                split_subtitle_text_1 = subtitle_text_1.split(' ', 1)
                if len(split_subtitle_text_1) > 1:
                    subtitle_text_1 = split_subtitle_text_1[1]
                else:
                    subtitle_text_1 = ""

                # #removing everything before ":"

                # split_subtitle_text_1 = subtitle_text_1.split(':', 1)
                # print(split_subtitle_text_1)
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

                #removing the first word of English 
                split_subtitle_text_1 = subtitle_text_1.split(' ', 1)
                if len(split_subtitle_text_1) > 1:
                    subtitle_text_1 = split_subtitle_text_1[1]
                else:
                    subtitle_text_1 = ""

                # #removing everything before ":"

                # split_subtitle_text_1 = subtitle_text_1.split(':', 1)
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


            srt_file.write(str(subtitle_count) + '\n')
            srt_file.write(start_time + ' --> ' + end_time + '\n')
            srt_file.write(subtitle_text_1 + '\n')
            srt_file.write('--' + '\n')
            srt_file.write(subtitle_text_2 + '\n\n')

            subtitle_count += 1


# Usage example
#use sample 5 for no speakers and sample 4 for borth speakers
#You can generate the csv files from pdf_to_csv.py and then use the csv files inside outputcsv folder.
csv_file_path = '/Users/asharfarooq/Downloads/Uliza/Subtitles/outputcsv/1997_01-01 transcript.csv'
srt_file_path = 'example_srt_file.srt'
generate_srt_file(csv_file_path, srt_file_path)








