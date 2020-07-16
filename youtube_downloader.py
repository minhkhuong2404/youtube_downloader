import json
import re
import urllib.request

from numpy.core import long
from pytube import YouTube
import pytube


class Helper:
    def __init__(self):
        pass

    def title_to_underscore_title(self, title: str):
        title = re.sub('[\W_]+', "_", title)
        return title.lower()

    def id_from_url(self, url: str):
        return pytube.extract.video_id(url)


class YouTubeStats:
    def __init__(self, url: str):
        self.json_url = urllib.request.urlopen(url)
        self.data = json.loads(self.json_url.read())

    def print_data(self):
        return self.data

    def get_video_title(self):
        return self.data["items"][0]["snippet"]["title"]

    def get_video_desciption(self):
        return self.data["items"][0]["snippet"]["description"]

    def get_video_upload_day(self):
        return self.data["items"][0]["snippet"]["publishedAt"]

    def get_channel_name(self):
        return self.data["items"][0]["snippet"]["channelTitle"]

    def get_view(self):
        return self.data["items"][0]["statistics"]["viewCount"]

    def get_like(self):
        return self.data["items"][0]["statistics"]["likeCount"]

    def get_comment(self):
        return self.data["items"][0]["statistics"]["commentCount"]

    def get_length(self):
        return self.data["items"][0]["contentDetails"]["duration"]

    def download_video(self, youtube_str: str, title_video: str):
        print("Downloading %s" % f"{title}_description.txt" + '\n')
        YouTube(youtube_str).streams.get_highest_resolution().download(filename=title_video)
        print("==================================================== " + '\n')


api_key = "AIzaSyCPaakCku8IgW4jJR8ivOEiMb2rWHp3Kos"

link_file = "link.csv"
with open(link_file, 'r') as f:
    content = f.readlines()

content = list(map(lambda s: s.strip(), content))
content = list(map(lambda s: s.strip(','), content))

helper = Helper()
for youtube_url in content:
    video_id = helper.id_from_url(youtube_url)
    url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part=snippet,contentDetails,statistics,status"
    yt_stats = YouTubeStats(url)

    title = yt_stats.get_video_title()

    description = yt_stats.get_video_desciption()

    uploaded_day = yt_stats.get_video_upload_day()

    channel_name = yt_stats.get_channel_name()

    view_count = yt_stats.get_view()

    view_like = yt_stats.get_like()

    view_comment = yt_stats.get_comment()

    view_duration = yt_stats.get_length()
    view_duration = view_duration[2:]

    print(title + '\n')
    print("Length: " + view_duration + '\n')
    print("Uploaded at: " + uploaded_day + '\n')
    print("Uploaded by: " + channel_name + '\n')
    print("View: " + "{:,}".format(long(view_count)) + '\n')
    print("Like: " + "{:,}".format(long(view_like)) + " Comment: " + "{:,}".format(long(view_comment)) + '\n')

    with open(f"{title}_description.txt", "w") as f:
        f.write(description)

    yt_stats.download_video(youtube_url, title)
