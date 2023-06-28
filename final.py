import pysrt
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os

# Convert a time object from the SRT file(i.e. 00:00:40,822) into total seconds
def time_to_seconds(time):

    hours, mins, seconds, milliseconds =  time
    # Convert each metric to seconds 
    return (hours * 3600) + (mins * 60) + seconds + (milliseconds / 1000)

# Creating TextClip objects for each subtitle in the SRT file with some styling
def create_subtitle_text_clips(subtitles, video_size):

    video_width, video_height = video_size

    subtitle_clips = []
    for subtitle in subtitles:
        # Getting time information
        start_time = time_to_seconds(subtitle.start)
        end_time = time_to_seconds(subtitle.end)
        subtitle_duration = end_time - start_time

        # splitting the subtitle text by a new line to get english text and the other language text of subtitle
        english, other_language = subtitle.text.split("--")

        # Size of the subtitle picture/box in pixels (height is auto-determined/None)
        size=(video_width, None) 

        # Run the code below to see all options for color and font
        # print(TextClip.list('color')) or print(TextClip.list('font'))

        # Creating subtitle TextClips with some attributes(duration, start time, styling)
        other_language_text_clip = TextClip(other_language, fontsize=22, font="Arial", color="red", bg_color = 'black',size=size, method='caption').set_start(start_time).set_duration(subtitle_duration)
        english_clip = TextClip(english, fontsize=22, font="STIXGeneral-Italic", color="white", bg_color = 'black',size=size, method='caption').set_start(start_time).set_duration(subtitle_duration)

        subtitle_x_position = 'center'
        # Positioning and handling the subtitle for the non-English language
        subtitle_y_position_non_eng = video_height * 0
        text_position_non_eng = (subtitle_x_position, subtitle_y_position_non_eng)   
        subtitle_clips.append(other_language_text_clip.set_position(text_position_non_eng))

        # Positioning and handling the subtitle for the English language (right below the non-English TextClip)
        subtitle_y_position_eng = video_height * 9/10
        text_position_eng = (subtitle_x_position, subtitle_y_position_eng)   
        subtitle_clips.append(english_clip.set_position(text_position_eng))

    return subtitle_clips


# Define the input folder path
adan_input = "/Users/adana/Downloads/Subtitles/Subtitles/input"
ashar_input = "/Users/asharfarooq/Downloads/Uliza/Subtitles/input"
input_folder_path = ashar_input  # Update with your input folder path

# Define the output folder path
adan_output = "/Users/adana/Downloads/Subtitles/Subtitles/output"
ashar_output = "/Users/asharfarooq/Downloads/Uliza/Subtitles/output"
output_folder_path = ashar_output  # Update with your output folder path

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Iterate over each file in the input folder
for file_name in os.listdir(input_folder_path):
    # Check if the file is a video file
    if file_name.endswith('.mp4'):

        file_name_root = os.path.splitext(file_name)[0]

        if f'{file_name_root}.srt' not in list(os.listdir(input_folder_path)):
            raise Exception(f'Please ensure that an .srt file with the same name({file_name_root}) as the video file is in this input folder.')

        # Construct the full file paths
        video_file_input_path = os.path.join(input_folder_path, file_name)
        subtitles_file_path = os.path.join(input_folder_path, f'{file_name_root}.srt')

        # Loading input video and opening subtitles file
        video = VideoFileClip(video_file_input_path)
        subtitles = pysrt.open(subtitles_file_path)

        subtitle_clips = create_subtitle_text_clips(subtitles,video.size)

        # Burning subtitles and outputting video
        final_video = CompositeVideoClip([video] + subtitle_clips)

        # Preview Video Without Writing(frame at 7.5 seconds)
        # final_video.show(7.5, interactive = True)

        os.chdir(output_folder_path)
        final_video.write_videofile(f'{file_name_root}_output.mp4', remove_temp=True, audio=True, audio_codec='libmp3lame', temp_audiofile=f'{file_name_root}_outputTEMP_MPY_wvf_snd.mp3')