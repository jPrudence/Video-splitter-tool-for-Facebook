import os
import datetime
from moviepy.video.io.VideoFileClip import VideoFileClip


def get_videos_dir():
    # Get the absolute path of the /videos directory
    return os.path.abspath("videos")


def find_video_files(videos_dir):
    # Find all video files "*.mp4" in the /videos directory and ignore folders
    return [file_name for file_name in os.listdir(videos_dir) if file_name.endswith(".mp4") and os.path.isfile(os.path.join(videos_dir, file_name))]


def display_videos(video_files):
    # Display the list of found videos
    print("Found videos:")
    for i, video_file in enumerate(video_files):
        print(f"{i+1}. {video_file}")


def choose_video(video_files):
    # If there is only one video, return it
    if len(video_files) == 1:
        print(f"'{video_files[0]}' has been automatically chosen.")
        return video_files[0]

    # Ask the user to choose a video
    while True:
        try:
            video_choice = int(
                input(f"Choose a video (1 - {len(video_files)}) : "))

            if 1 <= video_choice <= len(video_files):
                video_choice = video_files[video_choice - 1]
                print(f"You have chosen the video '{video_choice}'")
                return video_choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid choice. Please try again.")


def get_ignore_minutes():
    # Ask the user how many minutes to ignore at the beginning of the video
    while True:
        try:
            ignore_minutes = int(input(
                "How many minutes do you want to ignore at the beginning of the video? ( Default: 0 minutes) : ") or "0")
            return ignore_minutes
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_segment_duration():
    # Set the duration of each segment in minutes"
    while True:
        try:
            default_segment_duration = 5
            segment_duration = int(input(
                f"What duration (in minutes) do you want for each segment? (Default: {default_segment_duration} minutes) : ") or default_segment_duration)
            if segment_duration > 0:
                return segment_duration * 60
            else:
                print("Invalid input. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def create_output_folder(videos_dir, video_name):
    # Create the output folder name
    today = datetime.datetime.now().strftime("%H%M%S%d%m")
    output_folder = os.path.join(videos_dir, "output", f"{today}_{video_name}")

    # Create the output folder if it doesn't already exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    return output_folder


def cut_video(video, ignore_minutes, segment_duration, output_folder):
    # Ignore the first n minutes of the video
    if ignore_minutes > 0:
        ignore_seconds = ignore_minutes * 60
        video = video.subclip(ignore_seconds)

    # Calculate the number of segments needed
    num_segments = int(video.duration // segment_duration) + 1

    # Cut the video into segments and save them to the output folder
    for i in range(num_segments):
        start_time = i * segment_duration
        end_time = min((i + 1) * segment_duration, video.duration)
        segment = video.subclip(start_time, end_time)
        segment_name = os.path.join(output_folder, f"segment_{i+1}.mp4")
        segment.write_videofile(segment_name)

    # Display a confirmation message
    print(
        f"The video has been cut into {num_segments} segments of {segment_duration} seconds and saved in the folder '{output_folder}'.")


#  Main program
videos_dir = get_videos_dir()
video_files = find_video_files(videos_dir)
display_videos(video_files)
video_name = choose_video(video_files)
ignore_minutes = get_ignore_minutes()
segment_duration = get_segment_duration()
output_folder = create_output_folder(videos_dir, video_name)
video = VideoFileClip(os.path.join(videos_dir, video_name))
cut_video(video, ignore_minutes, segment_duration, output_folder)
