# darkwebmysterybot

Dark Web Mystery Bot v1-dev (20191113)

Dark Web Mystery Bot, created by redneonglow, is a Fediverse phrase bot inspired by YouTube videos and urban legends about the Deep Web. The bot generates silly phrases such as these:

* marianas web mystery polyamory
* dark net mystery programming
* dark net mystery trigonometry
* deep web dybbuk chicken
* deep web capitalism
* marianas net trade
* dark web mystery aerobics
* dark web pepperoni
* dark web hate
* deep web sausage

Phrases are derived from the following lists:

* conspiracy (conspiracy theories, pseudoscience, aliens, the occult, etc.)
* italian (italian food, italian-american foods, pizza toppings)
* medieval (stuff from fairy tales)
* politics (related to us politics)
* studies (academic studies)

Dark Web Mystery Bot can post directly to Mastodon and Pleroma instances and is great for use in an hourly cronjob.

WARNING: Dark Web Mystery Bot is currently only suitable for "free speech" instances. A special output mode for "safe space" instances will be available in a future version.

REQUIREMENTS:

* Python 3
* Mastodon.py and its dependencies
* curl

SET UP THE TOKEN FILE:

1. Create a Fediverse account for Dark Web Mystery Bot.
2. Set up a token here: https://tinysubversions.com/notes/mastodon-bot/
3. Create a token file by running this command:
   curl <command you are given> > tokenfile.json

EXAMPLE COMMANDS:

Show help: ./dwmbot.py -h

Show license (Simplified BSD): ./dwmbot.py -l

Show version: ./dwmbot.py -v

Print 1 phrase to stdout: ./dwmbot.py -p 1

Print 4 phrases to stdout: ./dwmbot.py -p 4

Post to an account on Pleroma instance Neckbeard.xyz using token file tokenfile.json:

./dwmbot.py -o https://neckbeard.xyz tokenfile.json

ENJOY!

-redblade7 aka redneonglow

Fediverse contact info:

* @redneonglow@neckbeard.xyz (main)
  https://neckbeard.xyz/redneonglow
* @redneonglow@anime.website (backup)
  https://anime.website/redneonglow
* @redneonglow@weeaboo.space (backup)
  https://weeaboo.space/redneonglow

The author runs an instance of Dark Web Mystery Bot here:

* @darkweb@neckbeard.xyz (phrases are generated every hour)
  https://neckbeard.xyz/darkweb
