# darkwebmysterybot

**Dark Web Mystery Bot v2-dev (20191119)**

Dark Web Mystery Bot, created by redneonglow, is a Fediverse phrase bot inspired by YouTube videos and urban legends about the Deep Web. The bot generates silly phrases such as these:

* marianas web mystery polyamory
* dark net mystery programming
* marianas web mystery republican
* deep web mystery german
* marianas net salvadorian
* dark web mystery chemist
* dark web mystery singaporean
* dark web pepperoni
* dark web hate
* deep web sausage

Phrases are derived from the following lists:

* conspiracy (conspiracy theories, pseudoscience, aliens, the occult, etc.)^
* italian (italian food, italian-american foods, pizza toppings)
* medieval (stuff from fairy tales)^
* nationalities (nationalities, ethnicities, races)^
* occupations (based on the studies list below)
* politics (related to us politics)^
* studies (academic studies)

^ excluded from safe-space mode

Dark Web Mystery Bot can post directly to Mastodon and Pleroma instances and is great for use in an hourly cronjob.

WARNING: Dark Web Mystery Bot may produce phrases which are only suitable for "free speech" instances. For "safe space" instances, an option is provided to exclude such possibilities, but there are still no guarantees.

**REQUIREMENTS:**

* Python 3
* Mastodon.py and its dependencies
* curl

**SET UP THE TOKEN FILE:**

1. Create a Fediverse account for Dark Web Mystery Bot.
2. Set up a token here: https://tinysubversions.com/notes/mastodon-bot/
3. Create a token file by running this command:
   `curl <command you are given> > tokenfile.json`

**EXAMPLE COMMANDS:**

Show help: `./dwmbot.py -h`

Show license (Simplified BSD): `./dwmbot.py -l`

Show version: `./dwmbot.py -v`

Print 1 phrase to stdout: `./dwmbot.py -p 1`

Print 4 phrases to stdout: `./dwmbot.py -p 4`

Post to an account on Pleroma instance Neckbeard using token file tokenfile.json:

`./dwmbot.py -o https://neckbeard.xyz tokenfile.json`

Post to an account on Mastodon instance mastodon.social, using token file wokenfile.json, while avoiding phrases which would not be suitable for safe-space instances:

`./dwmbot.py -c https://mastodon.social wokenfile.json`

Post version info to an account on Pleroma instance Neckbeard using token file tokenfile.json:

`./dwmbot.py -w https://neckbeard.xyz tokenfile.json`

Enjoy!

-redblade7 aka redneonglow

**SPECIAL THANKS**

* Your New SJW Waifu (`@sjw@neckbeard.xyz`) for allowing me to host the bot on Neckbeard
* Dielan (`@dielan@shitposter.club`) for showing me how to create Fediverse bots with Python

**FEDIVERSE CONTACT INFO:**

* `@redneonglow@neckbeard.xyz` / https://neckbeard.xyz/redneonglow (main)
* `@redneonglow@anime.website` / https://anime.website/redneonglow (backup)
* `@redneonglow@weeaboo.space` / https://weeaboo.space/redneonglow (backup)

The author runs an instance of Dark Web Mystery Bot here, generating phrases hourly:

* `@darkweb@neckbeard.xyz` / https://neckbeard.xyz/darkweb
