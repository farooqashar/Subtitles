import pysrt
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

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
        other_language, english = subtitle.text.split("\n")

        # Size of the subtitle picture/box in pixels (height is auto-determined/None)
        size=(video_width * 3/4, None) 

        # Run the code below to see all options for color and font
        # print(TextClip.list('color')) or print(TextClip.list('font'))

        # Creating subtitle TextClips with some attributes(duration, start time, styling)
        other_language_text_clip = TextClip(other_language, fontsize=24, font="Arial", color="red", bg_color = 'black',size=size, method='caption').set_start(start_time).set_duration(subtitle_duration)
        english_clip = TextClip(english, fontsize=18, font="STIXGeneral-Italic", color="white", bg_color = 'black',size=size, method='caption').set_start(start_time).set_duration(subtitle_duration)

        subtitle_x_position = 'center'
        # Positioning and handling the subtitle for the non-English language
        subtitle_y_position_non_eng = video_height * 8/10
        text_position_non_eng = (subtitle_x_position, subtitle_y_position_non_eng)   
        subtitle_clips.append(other_language_text_clip.set_position(text_position_non_eng))

        # Positioning and handling the subtitle for the English language (right below the non-English TextClip)
        subtitle_y_position_eng = (video_height * 8/10) + other_language_text_clip.size[1]
        text_position_eng = (subtitle_x_position, subtitle_y_position_eng)   
        subtitle_clips.append(english_clip.set_position(text_position_eng))

    return subtitle_clips

# Loading input video and opening subtitles file
video = VideoFileClip("input.mp4")
subtitles = pysrt.open("subtitles.srt")

subtitle_clips = create_subtitle_text_clips(subtitles,video.size)

# Burning subtitles and outputting video
final_video = CompositeVideoClip([video] + subtitle_clips)
final_video.write_videofile("output.mp4")
