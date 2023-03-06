# Video splitter tool for facebook

This Python script lets you split long videos into shorter segments for posting to Facebook or other social media platforms. Use this tool to prepare your video stories for Facebook. The tool will automatically split the video into segments and save them to a new output folder.

## Requirements
- MoviePy library (pip install moviepy)

## How to Use
- Clone the repository to your local machine `git clone https://github.com/jPrudence/Video-splitter-tool-for-Facebook.git`
- Navigate to the project directory `cd Video-splitter-tool-for-Facebook`
- Install the required package by running `pip install moviepy`
- Place your video file(s) in the /videos directory.
- Run the script using `python splitter.py`
- Choose the video you want to split from the list of found videos.
- Enter the number of minutes to ignore at the beginning of the video (if needed, this is useful for skipping the opening sequence of a video).
- Enter the desired duration of each segment in minutes.
- The tool will automatically split the video into segments and save them to a new output folder in /videos/output ( ex : /videos/output/1638320603_video_name/ )

## Example
- Suppose you have a video that is 5 minutes long and you want to post it as a story on Facebook. Using this tool, you can split the video into 30-second segments, which is the maximum length for a Facebook story. You can also choose to ignore the first minute of the video if there is an introduction or opening sequence that you want to skip. The tool will automatically create a new folder in /videos/output/ with the segmented video files ready to be uploaded to Facebook.