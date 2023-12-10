from JaanxMusic.core.bot import Jaanx
from JaanxMusic.core.dir import dirr
from JaanxMusic.core.git import git
from JaanxMusic.core.userbot import Userbot
from JaanxMusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Jaanx()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
