from JaanxMusic.core.bot import Aviax
from JaanxMusic.core.dir import dirr
from JaanxMusic.core.git import git
from JaanxMusic.core.userbot import Userbot
from JaanxMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Aviax()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
