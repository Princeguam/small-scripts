from pytube import YouTube
import request

def Download(link):
    youtubeObject  = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print('An Error has occured! check your link and try again!')
    print('Download complete!')

link = request.form.get('desired_link')
Download(link)

