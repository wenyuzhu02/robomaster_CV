import cv2
import importlib
import os
import stat
import youtube_dl
import sys

videos = [
    # {
    #     "link": "https://www.youtube.com/watch?v=CI7Dxbt_ayk",
    #     "filename": "sentry_bright"
    # },
    {
        "link": "https://github.com/uw-advanced-robotics/aruw-vision-platform-2019/raw/master/.github/sentinel_practice-opt.gif",
        "filename": "sentry_practice"
    },
    {
        "link": "https://github.com/uw-advanced-robotics/aruw-vision-platform-2019/raw/master/.github/ohio23-opt.gif",
        "filename": "competition_gif1"
    },
    {
        "link": "https://github.com/uw-advanced-robotics/aruw-vision-platform-2019/raw/master/.github/ohio48-opt.gif",
        "filename": "competition_gif2"
    },
    # {
    #     "link": "link to video",
    #     "filename": "file name to save video to"
    # }
]
folder = "CVideos"

# go from video to video
    # look through CVideos folder
    # pass filename through 
# scrubbing/video features
    # play feature
# include and exclude
# image side by side

def download(video):
    print("Downloading "+video.get("filename")+" from "+video.get("link")+" ... ", end="")
    save_stdout = sys.stdout
    sys.stdout = open(os.devnull, "w")  # supressing print
    ydl_opts = {
        "outtmpl": folder+"/"+video.get("filename")+".%(ext)s"
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video.get("link")])
    sys.stdout = save_stdout # enabling print
    print("finished")

def downloadAll(refreshAll=False):
    def file_exists(filename):
        for file in os.listdir(folder):
            if os.path.splitext(file)[0] == filename:
                return True
        return False
    if not os.path.isdir(folder):
        os.makedirs(folder)
    for video in videos:
        print(1)
        if not file_exists(video.get("filename")):
            download(video)

def imagefeed(cvfunction):
    print("here for now")

def videofeed(cvfunction):
    # for 
    video = cv2.VideoCapture(folder+"/tets.gif")
    
    while True:
        success,frame = video.read()
        image = cvfunction(frame)
        cv2.imshow("Image", image)
        cv2.waitKey(0)

downloadAll()