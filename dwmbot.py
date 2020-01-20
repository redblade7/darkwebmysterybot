#!/usr/bin/env python3
#
# Dark Web Mystery Bot
# 
# A Fediverse phrase bot inspired by YouTube videos and urban legends about
# the Deep Web.
#
# Copyright (c) 2019-20, redneonglow
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from mastodon import Mastodon,MastodonError
import argparse,json,secrets,sys

#program version
progver = "4-dev (20200121)"

#prefix
prefix = ["dark net","dark web","deep web","marianas net","marianas web","shadow net","shadow web"]

#faketld (onion, i2p, and fake TLDs associated with urban legends)
faketld = ["clos","dafy","end","i2p","loky","nept","onion","taur"]

#conspiracy (conspiracy theories, pseudoscience, aliens, the occult, etc.)
conspiracy = ["agenda","alchemy","alien","antichrist","assassination","astrology","aura","autism","birther","bodycount","brainwashing","cabal","camp","chemtrails","clairvoyance","classified","conspiracy","control","creationism","creepypasta","cryptozoology","deathpanel","deepstate","delusion","demolition","demon","denial","detention","ectoplasm","epidemic","extermination","extraterrestrial","fakenews","fallacy","falseflag","fluoride","foreknowledge","freemasonry","gaybomb","gayfrog","genocide","ghost","ghosthunting","glyphosate","guidestones","hallucination","homeopathy","horoscope","illuminati","infowar","infowarrior","interrogation","intelligence","intuition","jesuit","magick","masonry","massacre","medication","mercury","missing","mkultra","mindcontrol","mindreading","monarch","nibiru","nostradamus","occultism","orb","order","paranoia","paranormal","pizzagate","plot","poison","population","possession","power","precognition","projection","prophecy","prophet","pseudohistory","pseudolaw","pseudoscience","psychic","psycho","psychosis","psychotic","radiation","reincarnation","remote","reptilian","ritual","revisionism","roswell","satan","satanism","sandyhook","seance","secret","shaman","silverstein","soros","sovereign","specter","spirit","spiritualism","supernatural","superstition","surveillance","telekinesis","telepathy","thimerosal","tinfoil","torture","truther","vaccination","vaccine","vampire","viewing","zionist"]

#italian (italian food, italian-american foods, pizza toppings)
italian = ["alfredo","anchovy","artichoke","arugula","asiago","bacon","basil","bologna","bread","broccoli","calamari","cannoli","capicola","cheese","chicken","egg","eggplant","fettucine","garlic","gelato","gorgonzola","jalapeno","ham","lasagna","linguine","macaroni","meatball","meatlovers","mozzarella","mushroom","olive","onion","oregano","parmesan","pasta","peperoncini","pepper","pepperoni","pineapple","pizza","prosciutto","provolone","ravioli","ricotta","risotto","romano","salami","sausage","seafood","shellfish","spaghetti","spinach","supreme","tomato","tortellini","ziti"]

#medieval (stuff from fairy tales)
medieval = ["amulet","apprentice","banishment","banshee","beanstalk","bear","beast","bridge","carpet","castle","cauldron","chalice","changeling","crossbow","crown","crusader","crusades","crystal","curse","damsel","dragon","drawbridge","dungeonmaster","dwarf","elf","fairy","fantasy","folktale","frog","genie","giant","gnome","goblin","godmother","gown","grail","guillotine","hag","hangman","harem","hero","heroine","imp","inquisitor","jester","joust","howl","kettle","king","kingdom","knight","lady","land","legend","leprechaun","lord","lore","magic","magician","mace","maiden","mask","mirror","monk","monster","moon","myth","necromancer","newt","nun","ogre","orc","paladin","pegasus","pixie","prince","princess","protector","quail","queen","quest","rack","realm","reign","robe","roundtable","sage","sandman","scepter","scroll","shapeshifter","slippers","soothsayer","sorcerer","spear","spell","spider","sprite","staff","stepmother","sultan","sword","swordfight","talisman","toad","torch","tower","troll","unicorn","valiant","valor","vanquish","vizier","wail","wand","warlock","warrior","werewolf","witch","wizard","wolf"]

#nationalities (nationalities, ethnicities, races)
nationalities = ["afghan","african","albanian","algerian","american","andorran","angolan","argentine","argentinian","armenian","asian","australian","austrian","azerbaijani","bahamian","bangladeshi","barbadian","belarusian","belgian","beninese","bhutanese","black","bolivian","bosnian","brazilian","brit","briton","bruneian","bulgarian","burmese","burundian","cambodian","cameroonian","canadian","caucasian","chadian","chilean","chinese","colombian","congolese","croat","croatian","cuban","cypriot","czech","dane","dominican","dutchman","dutchwoman","ecuadorian","egyptian","emirati","englishman","englishwoman","eritrean","estonian","ethiopian","european","fijian","filipino","finn","frenchman","frenchwoman","gabonese","gambian","georgian","german","ghanaian","greek","grenadian","guatemalan","guinean","guyanese","haitian","hawaiian","hispanic","honduran","hungarian","icelander","indian","indonesian","iranian","iraqi","irishman","irishwoman","islander","israeli","italian","ivorian","jamaican","japanese","jew","jewish","jordanian","kazakh","kazakhistani","kenyan","korean","kuwaiti","laotian","latvian","lebanese","liberian","libyan","liechtensteiner","lithuanian","luxembourger","macedonian","madagascan","malagasy","malawian","malaysian","maldivian","malian","maltese","mauritanian","mauritian","mexican","moldovan","monacan","mongolian","montenegrin","moroccan","mozambican","namibian","native","nepalese","nicaraguan","nigerian","nigerien","norwegian","omani","pakistani","palestinian","panamanian","paraguayan","persian","peruvian","pole","portuguese","qatari","romanian","russian","rwandan","salvadoran","salvadorean","salvadorian","saudi","scot","senegalese","serb","serbian","singaporean","slovak","slovenian","somali","somalian","spaniard","sudanese","surinamese","swazi","swede","swiss","syrian","taiwanese","tadzhik","tajik","tanzanian","thai","togolese","trinidadian","tunisian","turk","turkmen","ugandan","ukrainian","uruguayan","uzbek","venezuelan","vietnamese","welshman","welshwoman","white","yemeni","yugoslav","zambian","zimbabwean"]

#occupations (originally based on the studies list)
occupations = ["accountant","administrator","agent","analyzer","anatomist","anesthesiologist","anthropologist","archeologist","artist","astronaut","astronomer","astrophysicist","biologist","biochemist","botanist","cardiologist","chemist","climatologist","cosmologist","criminologist","cybernetician","dancer","dentist","dermatologist","designer","developer","director","doctor","ecologist","economist","endocrinologist","engineer","ethicist","evolutionist","gastroenterologist","geneticist","geographer","gynecologist","hematologist","hepatologist","historian","linguist","logician","manager","marketer","mathematician","metaphysicist","mechanist","musician","nanotechnologist","nephrologist","neurologist","neurosurgeon","nurse","nutritionist","oncologist","operator","ophthalmologist","optometrist","paleontologist","pathologist","pediatrician","pharmacist","pharmacologist","philosopher","physician","podiatrist","priest","producer","programmer","psychiatrist","psychologist","psychoanalyst","pulmonologist","rheumatologist","robot","scientist","sociologist","spy","statistician","surgeon","sysadmin","technician","theologian","theorist","therapist","toxicologist","writer","zoologist"]

#politics (related to us politics)
politics = ["abortion","abuse","agency","agreement","amendment","alt-left","alt-right","antifa","antitrust","arbitration","argument","arms","assault","backdoor","barack","based","bathroom","bernie","bias","biden","bigotry","bill","bisexuality","bluestate","breakup","bush","capital","capitalism","capitol","cartel","case","catholic","catholicism","censorship","centrist","cheney","choice","christian","christianity","church","climate","clinton","college","collusion","communism","confederate","confederacy","congress","congressman","congresswoman","consent","conservative","conservatism","correctness","corruption","constitution","court","coverage","crime","criminal","debate","democracy","democrat","discrimination","druglord","drugs","drugwar","election","elector","execution","executive","extremist","fascism","fearmonger","feminism","fentanyl","fracking","freedom","gay","gender","gore","guncontrol","guns","hamas","harassment","hate","hatemonger","hatred","heteronormative","heterosexual","hillary","hoax","holocaust","homophobia","homosexuality","house","hydrofracture","illegal","illegals","immigrant","immigration","impeachment","incel","inclusion","indecency","insurance","intersex","isis","islam","israel","judiciary","justice","law","left","leftist","legislature","lesbian","liberal","liberalism","libertarian","libertarianism","liberty","marijuana","marriage","masculinity","media","medicare","microaggression","military","minority","moderate","muslim","narcotics","neocon","neoconservative","neoconservatism","news","obama","obscenity","opinion","opioid","palestine","partisan","party","patriarchy","peace","pedophilia","penalty","pence","pepe","piracy","police","policy","politician","politics","pornography","presidency","president","privacy","progressive","progressivism","property","polyamory","queer","race","racism","racist","rape","rapist","redpill","redpilled","redstate","religion","reparations","representative","republican","resources","right","rocketman","sanders","scandal","senate","senator","sex","sexuality","sexist","sexism","slave","slavery","socialist","socialism","socialsecurity","speech","state","strawman","tariff","terror","terrorism","terrorist","theft","trade","transgender","toxic","transphobia","treaty","trump","truth","undocumented","unlawful","vote","voter","voting","wall","war","warming","washington","woke","xenophobia"]

#sports (professional sports, extreme sports, martial arts)
sports = ["aikido","archery","athletics","badminton","baseball","basketball","biking","billiards","bouldering","bowling","boxing","canoeing","climbing","cricket","curling","cycling","darts","diving","equestrian","fencing","fishing","football","gliding","golf","gymnastics","handball","hockey","hunting","jai-alai","judo","jiu-jitsu","jumping","karate","kickboxing","motocross","motorsport","mountaineering","netball","ninjutsu","olympics","paragliding","parasailing","pentathlon","pool","racing","riding","rollerblading","rollerskating","rowing","running","rugby","sailing","sandboarding","shooting","skateboarding","skating","skiing","skydiving","snooker","snowboarding","soccer","softball","squash","sumo","surfing","swimming","taekwondo","tennis","volleyball","weightlifting","wrestling","yoga"]

#studies (academic studies)
studies = ["accounting","administration","aerobics","aerodynamics","aerospace","algebra","analysis","anatomy","anesthesiology","anthropology","archeology","art","arts","astronomy","astrophysics","biology","biochemistry","botany","business","calculus","cardiology","chemistry","climatology","computing","cosmology","criminology","cybernetics","dance","dentistry","dermatology","design","development","ecology","economics","electronics","endocrinology","energy","engineering","ethics","evolution","film","finance","fitness","forensics","gastroenterology","genetics","geography","geometry","geriatrics","gynecology","hematology","hepatology","history","humanities","language","languages","linguistics","literature","logic","management","marketing","mathematics","medicine","metaphysics","macroeconomics","mechanics","microeconomics","music","nanotechnology","nephrology","neurology","neurosurgery","nursing","nutrition","obstetrics","oncology","operations","ophthalmology","optometry","paleontology","pathology","pediatrics","pharmacology","pharmaceuticals","philosophy","physics","podiatry","probability","programming","psychiatry","psychology","psychoanalysis","pulmonology","radiology","rehabilitation","rheumatology","robotics","science","security","sociology","statistics","surgery","systems","technology","television","theater","theology","theory","therapy","thermodynamics","toxicology","trigonometry","writing","zoology"]

#returns a random word from a random list
#off: allow offensive content (bool)
def pickword(off):

    if off:
        listname = secrets.randbelow(8)
    else:
        listname = secrets.randbelow(4)

    if listname == 0:
        listword = secrets.choice(italian)
    elif listname == 1:
        listword = secrets.choice(studies)
    elif listname == 2:
        listword = secrets.choice(occupations)
    elif listname == 3:
        listword = secrets.choice(sports)
    elif listname == 4 and off:
        listword = secrets.choice(conspiracy)
    elif listname == 5 and off:
        listword = secrets.choice(politics)
    elif listname == 6 and off:
        listword = secrets.choice(medieval)
    elif listname == 7 and off:
        listword = secrets.choice(nationalities)
    else:
        print("ERROR: Invalid set!")
        sys.exit(1)

    return str(listword)

#returns the phrase as a string
#off: allow offensive content (bool)
def genphrase(off):
    
    outtype = secrets.randbelow(6)

    if outtype == 0:
        phrase = secrets.choice(prefix) + ' ' + pickword(off)
    elif outtype == 1:
        phrase = secrets.choice(prefix) + " dybbuk " + pickword(off)
    elif outtype == 2:
        phrase = secrets.choice(prefix) + " mystery " + pickword(off)
    elif outtype == 3:
        phrase = pickword(off) + '.' + secrets.choice(faketld)
    elif outtype == 4:
        #keep chance of 3 AM the same as the other potions
        potiontype = secrets.randbelow(len(prefix) + 1)

        if potiontype == len(prefix):
            phrase = "3 AM " + pickword(off) + " potion"
        else:
            phrase = prefix[potiontype] + ' ' + pickword(off) + " potion"
    elif outtype == 5:
        #keep chance of all box types the same
        boxtype = secrets.randbelow(len(prefix) + 2)

        if boxtype == len(prefix) + 1:
            phrase = pickword(off) + " mystery box"
        elif boxtype == len(prefix):
            phrase = pickword(off) + " dybbuk box"
        else:
            phrase = secrets.choice(prefix) + ' ' + pickword(off) + " box"
    else:
        print("ERROR: Invalid phrase type!");
        sys.exit(1)

    return str(phrase)

#open json access token
def readtoken(token):
    try:
        with open(str(token)) as replyfile:
            json_obj = json.load(replyfile)
    except OSError as err:
            print("ERROR:",err,'\n')
            sys.exit(1)
    
    return json_obj["access_token"]

#returns the main version line as a string
#used in version and license commands
def verline():
    return str("Dark Web Mystery Bot v" + progver)

#return part two of version info as string
def verpart2():
    return str("A Fediverse phrase bot by redneonglow.\nMore info: https://github.com/redblade7/darkwebmysterybot")

#shows version info
def optversion():
    print(verline())
    print(verpart2())

#shows license info
def optlicense():
    print(verline())
    print("\nCopyright (c) 2019-20, redneonglow\nAll rights reserved.\n")
    print("Redistribution and use in source and binary forms, with or without\nmodification, are permitted provided that the following conditions are met:\n")
    print("1. Redistributions of source code must retain the above copyright notice, this\n   list of conditions and the following disclaimer.")
    print("2. Redistributions in binary form must reproduce the above copyright notice,\n   this list of conditions and the following disclaimer in the documentation\n   and/or other materials provided with the distribution.\n")
    print("THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS \"AS IS\"\nAND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE\nIMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE\nDISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE\nFOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL\nDAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR\nSERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER\nCAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,\nOR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE\nOF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.")

#print phrase to stdout (incl. offensive)
def optprint():
    print(genphrase(True))

#post phrase to fediverse (public)
#viz: Mastodon.py visibility setting (string)
#off: allow offensive content (bool)
def optpostphrase(baseurl,token,vis,off):

    try:
        mastodon = Mastodon(api_base_url=str(baseurl),access_token=readtoken(str(token)))
        mastodon.status_post(genphrase(bool(off)),visibility=str(vis))
    except ValueError as err:
        print("ERROR:",err,'\n')
        sys.exit(2)
    except MastodonError as err:
        print("ERROR:",err,'\n')
        sys.exit(1)

    print("Successfully posted phrase to " + str(baseurl) + '!')

#post version info to fediverse (unlisted)
def optpostver(baseurl,token):

    try:
        mastodon = Mastodon(api_base_url=str(baseurl),access_token=readtoken(str(token)))
        mastodon.status_post(verline()+'\n'+verpart2(),visibility="unlisted")
    except MastodonError as err:
        print("ERROR:",err,'\n')
        sys.exit(1)

    print("Successfully posted version info to " + str(baseurl) + '!')

#main
def main():
   
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-l","--license",help="Show license info",action="store_true")
    group.add_argument("-v","--version",action="store_true",help="Show version info")
    group.add_argument("-w","--postversion",help="Post version info once, unlisted, to Fediverse site SERVER using token file TOKEN.",type=str,nargs=2,metavar=("SERVER","TOKEN"))
    group.add_argument("-p","--printphrase",help="Print phrase to stdout NUM times",type=str,metavar="NUM")
    group.add_argument("-o","--postphrase",help="Post phrase once to Fediverse site SERVER using token file TOKEN and visibility value VISIBILITY.",type=str,nargs=3,metavar=("SERVER","TOKEN","VISIBILITY"))
    group.add_argument("-c","--postpcphrase",help="Same as -o, but avoids phrases not suitable for safe-space instances.",type=str,nargs=3,metavar=("SERVER","TOKEN","VISIBILITY"))

    args = parser.parse_args()

    if args.license:
        optlicense()
    elif args.version:
        optversion()
    elif args.postversion:
        optpostver(args.postversion[0],args.postversion[1])
    elif args.postphrase:
        optpostphrase(args.postphrase[0],args.postphrase[1],args.postphrase[2],True)
    elif args.postpcphrase:
        optpostphrase(args.postpcphrase[0],args.postpcphrase[1],args.postpcphrase[2],False)
    elif args.printphrase:

        try:
            times = int(args.printphrase)
        except ValueError: 
            print("ERROR: argument -p/--printphrase NUM must be whole number!\n")
            parser.print_help()
            sys.exit(2)

        if times < 1:
            print("ERROR: argument -p/--printphrase NUM must be 1 or greater!\n")
            parser.print_help()
            sys.exit(2)
        else:
            for count in range(0,times):
                optprint()

    else:
        print("ERROR: Invalid command!\n")
        parser.print_help()
        sys.exit(2)
        
if __name__ == "__main__":
    main()
    sys.exit(0)
