#generating srt file.
#Code Sample to convert CSV file to a subtitle file in srt format:

import csv

#build a function that returns the end time because functions can't have more than one loop 
        #row_num = 0
        #printing how many rows we have 
        # for i in reader:
        # 	row_num += 1
        # #print(row_num)# will print how many rows we have in the file without skipping \
        # print("reached1")

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






# #generating srt file.
# #Code Sample to convert CSV file to a subtitle file in srt format:

# import csv

# #build a function that returns the end time because functions can't have more than one loop 
#         #row_num = 0
#         #printing how many rows we have 
#         # for i in reader:
#         # 	row_num += 1
#         # #print(row_num)# will print how many rows we have in the file without skipping \
#         # print("reached1")

# def generate_srt_file(csv_file_path, srt_file_path):
#     with open(csv_file_path, 'r') as csv_file, open(srt_file_path, 'w') as srt_file:
#         reader = csv.reader(csv_file)
#         #next(reader)  # Skip the header row if present
#         reader_list = list(reader)

#         subtitle_count = 1
#         print("reached1")

#         for row_index , row in enumerate(reader):
#             print("reached")
#             #print(row)
#             #print(row_index)
#             #skipping the first 8 rows and last row (55 should be changed accordingly)
#             if row_index <= 8 or row_index == 55:
#                 continue
#             # starting time
#             start_time = row[0] 

#             #end time is start time of next row 
#             #print(reader[row_index])
#             next_row_index = row_index + 1
#             next_row = reader_list[next_row_index]
#             end_time = next_row[0]


#             #get english translation as subtitles for now
#             subtitle_text = row[1] 
            
#             srt_file.write(str(subtitle_count) + '\n')
#             srt_file.write(start_time + ' --> ' + end_time + '\n')
#             srt_file.write(subtitle_text + '\n\n')
            
#             subtitle_count += 1

# # Usage example
# csv_file_path = 'Parsing2/output/sample2.csv'
# srt_file_path = 'subtitlessss.srt'
# generate_srt_file(csv_file_path, srt_file_path)



