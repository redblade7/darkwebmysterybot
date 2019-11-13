#!/usr/bin/env python3
#
# Dark Web Mystery Bot
# 
# A Fediverse phrase bot inspired by YouTube videos and urban legends about
# the Deep Web.
#
# Copyright (c) 2019, redneonglow
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

progver = "2-dev (20191114)"

#prefix
prefix = ["dark net","dark net dybbuk","dark net mystery","dark web","dark web dybbuk","dark web mystery","deep web","deep web mystery","deep web dybbuk","marianas net","marianas net dybbuk","marianas net mystery","marianas web","marianas web dybbuk","marianas web mystery"]

#italian (italian food, italian-american foods, pizza toppings)
italian = ["alfredo","anchovy","artichoke","arugula","asiago","bacon","basil","bologna","bread","broccoli","calamari","cannoli","capicola","cheese","chicken","egg","eggplant","fettucine","garlic","gelato","gorgonzola","jalapeno","ham","lasagna","linguine","macaroni","meatball","mozzarella","mushroom","olive","onion","oregano","parmesan","pasta","peperoncini","pepper","pepperoni","pineapple","pizza","prosciutto","provolone","ravioli","ricotta","risotto","romano","salami","sausage","seafood","shellfish","spaghetti","spinach","tomato","tortellini","ziti"]

#conspiracy (conspiracy theories, pseudoscience, aliens, the occult, etc.)
conspiracy = ["agenda","alchemy","alien","antichrist","assassination","astrology","aura","bodycount","cabal","camp","clairvoyance","classified","conspiracy","control","creationism","creepypasta","cryptozoology","deathpanel","deepstate","demolition","demon","denial","detention","ectoplasm","extermination","extraterrestrial","falseflag","fluoride","foreknowledge","freemasonry","gaybomb","genocide","ghost","ghosthunting","glyphosate","guidestones","hallucination","homeopathy","horoscope","illuminati","infowar","interrogation","intelligence","intuition","jesuit","magick","masonry","massacre","mkultra","mindreading","monarch","nostradamus","occultism","orb","order","paranoia","paranormal","plot","poison","population","possession","power","precognition","projection","prophecy","pseudohistory","pseudoscience","psychic","reincarnation","remote","ritual","revisionism","satanism","sandyhook","seance","secret","silverstein","soros","spirit","spiritualism","supernatural","surveillance","telekinesis","telepathy","tinfoil","torture","vaccination","vaccine","viewing","zionist"]

#studies (academic studies)
studies = ["accounting","aerobics","aerodynamics","aerospace","algebra","analysis","anatomy","anesthesiology","anthropology","archeology","art","arts","astronomy","astrophysics","biology","biochemistry","botany","business","calculus","cardiology","chemistry","climatology","computing","cosmology","criminology","cybernetics","dance","dentistry","dermatology","design","ecology","economics","electronics","endocrinology","energy","ethics","evolution","film","finance","fitness","forensics","gastroenterology","genetics","geography","geometry","geriatrics","gynecology","hematology","hepatology","history","language","languages","linguistics","literature","logic","management","marketing","mathematics","medicine","metaphysics","macroeconomics","mechanics","microeconomics","music","nanotechnology","nephrology","neurology","neurosurgery","nursing","nutrition","obstetrics","oncology","operations","ophthamology","optometry","paleontology","pathology","pediatrics","pharmacology","pharmaceuticals","philosophy","physics","podiatry","probability","programming","psychiatry","psychology","psychoanalysis","pulmonology","radiology","rehabilitation","rheumatology","robotics","science","security","sociology","statistics","surgery","surveillance","systems","technology","television","theater","theology","theory","therapy","thermodynamics","toxicology","trigonometry","writing","zoology"]

#politics (related to us politics)
politics = ["abortion","abuse","agreement","amendment","antifa","arbitration","argument","arms","assault","backdoor","barack","bathroom","bernie","bias","biden","bigotry","bill","bisexuality","bush","capitalism","case","catholic","catholicism","censorship","cheney","christian","christianity","church","climate","clinton","collusion","communism","congress","congressman","congresswoman","correctness","corruption","constitution","court","crime","criminal","debate","democracy","democrat","discrimination","drugs","execution","executive","fascism","fearmonger","feminism","fracking","freedom","gay","gender","gore","guns","harassment","hate","hatemonger","hatred","heteronormative","heterosexual","hillary","hoax","homophobia","homosexuality","house","hydrofracture","immigrant","immigration","impeachment","incel","intersex","judiciary","justice","law","legislature","lesbian","marijuana","marriage","masculinity","media","military","minority","obama","obscenity","partisan","party","patriarchy","pedophilia","pence","piracy","police","politics","pornography","presidency","president","privacy","property","polyamory","queer","racism","religion","representative","republican","rights","sanders","scandal","senate","senator","sexuality","sexism","socialism","speech","state","strawman","tariff","terror","terrorism","theft","trade","transgender","toxic","transphobia","treaty","trump","undocumented","unlawful","wall","war","warming","xenophobia"]

#medieval (stuff from fairy tales)
medieval = ["castle","crossbow","crown","crusader","crusades","curse","damsel","dwarf","fairy","fantasy","genie","gnome","godmother","guillotine","harem","jester","joust","king","kingdom","knight","lady","lord","magic","mace","mirror","monk","nun","paladin","prince","princess","protector","queen","rack","roundtable","scepter","sorcerer","spear","spell","staff","stepmother","sultan","sword","troll","vizier","wand","warrior","witch","wizard"]

#returns the phrase as a string
def genphrase():
    outtype = secrets.randbelow(5)

    if outtype == 0:
        phrase = secrets.choice(prefix) + ' ' + secrets.choice(italian)
    elif outtype == 1:
        phrase = secrets.choice(prefix) + ' ' + secrets.choice(conspiracy)
    elif outtype == 2:
        phrase = secrets.choice(prefix) + ' ' + secrets.choice(studies)
    elif outtype == 3:
        phrase = secrets.choice(prefix) + ' ' + secrets.choice(politics)
    elif outtype == 4:
        phrase = secrets.choice(prefix) + ' ' + secrets.choice(medieval)
    else:
        print("ERROR: Invalid set!")
        sys.exit(1)
    
    return str(phrase)

#open json access token
def readtoken(token):
    try:
        with open(str(token)) as replyfile:
            json_obj = json.load(replyfile)
    except OSError as err:
            print("ERROR:",err,"\n")
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
    print("\nCopyright (c) 2019, redneonglow\nAll rights reserved.\n")
    print("Redistribution and use in source and binary forms, with or without\nmodification, are permitted provided that the following conditions are met:\n")
    print("1. Redistributions of source code must retain the above copyright notice, this\n   list of conditions and the following disclaimer.")
    print("2. Redistributions in binary form must reproduce the above copyright notice,\n   this list of conditions and the following disclaimer in the documentation\n   and/or other materials provided with the distribution.\n")
    print("THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS \"AS IS\"\nAND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE\nIMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE\nDISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE\nFOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL\nDAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR\nSERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER\nCAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,\nOR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE\nOF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.")

#print phrase to stdout
def optprint():
    print(genphrase())

#post to fediverse
def optpost(baseurl,token):

    try:
        mastodon = Mastodon(api_base_url=str(baseurl),access_token=readtoken(str(token)))
        mastodon.status_post(genphrase(),visibility="public")
    except MastodonError as err:
        print("ERROR:",err,"\n")
        sys.exit(1)

    print("Successfully posted to " + str(baseurl) + '!')

#main
def main():
   
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-l","--license",help="Show license info",action="store_true")
    group.add_argument("-v","--version",action="store_true",help="Show version info")
    group.add_argument("-p","--printphrase",help="Print phrase to stdout NUM times",type=str,metavar="NUM")
    group.add_argument("-o","--postphrase",help="Post phrase once to Fediverse site SERVER using token file TOKEN.",type=str,nargs=2,metavar=("SERVER","TOKEN"))

    args = parser.parse_args()

    if args.license:
        optlicense()
    elif args.version:
        optversion()
    elif args.postphrase:
        optpost(args.postphrase[0],args.postphrase[1])
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
