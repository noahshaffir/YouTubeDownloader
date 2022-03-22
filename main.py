from pytube import YouTube
import os
video=YouTube(input("Enter a YouTube link."))
print(video.title,"is the title.")
print(video.length,"seconds is the length.")
proceed = input("Proceed with download? Say 'No' to abort.")
if proceed!="No":
    extension_type=input("Hit 1 to download an MP4 or anything else to download MP3.")
    if extension_type=="1":
        print("Let's do this!")
        video.streams.get_highest_resolution().download()
    else:
        print("Okie dokie!")
        title=video.title
        video=video.streams.get_highest_resolution()
        downloaded_vid = video.download(output_path='.')
        file_name, extension = os.path.splitext(downloaded_vid)
        new_file = file_name + '.mp3'
        os.rename(downloaded_vid, new_file)
print("Done!")