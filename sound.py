import vlc
import time

class Radio:
    def __init__(self,url):
        self.name = url
        #define VLC instance
        instance = vlc.Instance()

        #Define VLC player
        player=instance.media_player_new()

        #Define VLC media
        media=instance.media_new(url)

        #Set player media
        player.set_media(media)

        #Play the media
        player.play()





        #Sleep for 5 sec for VLC to complete retries.
        time.sleep(5)

Radio('https://icecast.omroep.nl/radio2-bb-mp3')
time.sleep(1000000)
