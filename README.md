# darkwebmysterybot

**Dark Web Mystery Bot v5.2 stable (20211218)**

Dark Web Mystery Bot, created by redneonglow, is a Fediverse phrase bot inspired by YouTube videos and urban legends about the Deep Web. The bot generates silly phrases such as these:

* dark net mystery programming
* marianas web mystery republican
* hoax mystery box
* troll.clos
* marianas net salvadorian
* dark web mystery chemist
* 3 AM moroccan potion
* deep web taekwondo box
* overnight algebra challenge 
* dark net netball
* deep web sausage
* 24 hour basketball challenge

Phrases are derived from the following lists:

* christmas (christmas, winter holidays)^%
* conspiracy (conspiracy theories, pseudoscience, aliens, the occult)^
* italian (italian food, italian-american foods, pizza toppings)
* medieval (stuff from fairy tales)^
* nationalities (nationalities, ethnicities, races)^
* occupations (originally based on the studies list below)
* politics (related to us politics)^
* sports (professional sports, extreme sports, martial arts)
* studies (academic studies)

^ excluded from safe-space mode

% only active during month of December

Dark Web Mystery Bot can post directly to Mastodon and Pleroma instances and is great for use in an hourly cronjob.

WARNING: Dark Web Mystery Bot may produce phrases which are only suitable for "free speech" instances. For "safe space" instances, an option is provided to exclude such possibilities, but there are still no guarantees.

**REQUIREMENTS:**

* Python 3.6 or higher
* Mastodon.py and its dependencies
* curl

**SET UP THE TOKEN FILE:**

1. Create a Fediverse account for Dark Web Mystery Bot.
2. Set up a token here: https://tinysubversions.com/notes/mastodon-bot/
3. Create a token file by running this command:
   `curl <command you are given> > tokenfile.json`

Note that if you change the password on the account, you will need to create a new token file.

**VISIBILITY:**

The visibility option may be any of the following:

* `direct` (only visible to the bot account)
* `private` (only visible to the bot account's followers)
* `public` (visible to everyone)
* `unlisted` (visible to everyone, but hidden from the public timeline)

In most cases you would want to use either `public` or `unlisted` for the visibility option.

**EXAMPLE COMMANDS:**

Show help: `./dwmbot.py -h`

Show license (Simplified BSD): `./dwmbot.py -l`

Show version: `./dwmbot.py -v`

Print 1 phrase to stdout: `./dwmbot.py -p 1`

Print 4 phrases to stdout: `./dwmbot.py -p 4`

Post to an account on Pleroma instance Neckbeard using token file tokenfile.json and public visibility:

`./dwmbot.py -o https://neckbeard.xyz tokenfile.json public`

Post to an account on Mastodon instance mastodon.social, using token file wokenfile.json and unlisted visibility, while avoiding phrases which would not be suitable for safe-space instances:

`./dwmbot.py -c https://mastodon.social wokenfile.json unlisted`

Post version info to an account on Pleroma instance Neckbeard using token file tokenfile.json (visibility always unlisted):

`./dwmbot.py -w https://neckbeard.xyz tokenfile.json`

Enjoy!

-redblade7 aka redneonglow

**SPECIAL THANKS**

* Your New SJW Waifu (`@sjw@neckbeard.xyz`) for allowing me to host the bot on Neckbeard
* Dielan (`@dielan@shitposter.club`) for showing me how to create Fediverse bots with Python
* chincostud (`@asylore@neckbeard.xyz`) who suggested adding shadow web/shadow net support

**FEDIVERSE CONTACT INFO:**

* `@redneonglow@neckbeard.xyz` / https://neckbeard.xyz/redneonglow (main)
* `@redneonglow@anime.website` / https://anime.website/redneonglow (backup)
* `@redneonglow@weeaboo.space` / https://weeaboo.space/redneonglow (backup)

The author runs an instance of Dark Web Mystery Bot here, generating phrases every half hour:

* `@darkweb@neckbeard.xyz` / https://neckbeard.xyz/darkweb
