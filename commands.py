# -*- coding: utf-8 -*-
import os
import fourchan_json
import random
import string

class tcol:
        NORMAL = u"\u000f"
        BOLD = u"\u0002"
        UNDERLINE = u"\u001f"
        REVERSE = u"\u0016"
        WHITE = u"\u00030"
        BLACK = u"\u00031"
        DARK_BLUE = u"\u00032"
        DARK_GREEN = u"\u00033"
        RED = u"\u00034"
        BROWN = u"\u00035"
        GREEN = u"\u00039"

def get_random_line(file_name):
    total_bytes = os.stat(file_name).st_size
    random_point = random.randint(0, total_bytes)
    xfile = open(file_name)
    xfile.seek(random_point)
    c = xfile.read(1)
    s = ""
    while c != ".":
        c = xfile.read(1)

    xfile.read(1)
    c = xfile.read(1)
    while c == ".":
        xfile.read(1)
    while c != ".":
        if c != "\n":
            if c != "\r":
                s += c
            else:
                s += " "
        c = xfile.read(1)
    s += c
    c = xfile.read(1)
    s += c
    while c == ".":
        s += c
        c = xfile.read(1)
    s.replace("- ", " ")
    return s


def shitpost():  # almost entirely automated shitposting
    post = fourchan_json.get_random_post()
    return post


def halp(user):
    string = user + ", sending you a private message of my commands.\n"
    string1 = "ur a faget"
    return string, string1


def interjection():  # I'd just like to interject for a moment
    str = ("I'd just like to interject for moment. What you're referring to as "
              "Linux, is in fact, GNU/Linux, or as I've recently taken to calling it,"
              " GNU plus Linux. pastebin.com/2YxSM4St\n")
    return str


def git():
    str = "https://github.com/lovelaced/cybot What are we going to do on the repo? waaaah fork =3\n"
    return str


def memearrows():  # >implying you can triforce
    str = ("Meme arrows are often used to preface implications or feels. See "
              "also: implying, feel.\n")
    return str


def intensifies(args):  # [python intensifies]
    if len(args.split(" ")) > 1:
        args = args.split(" ")[1:]
        return "[" + " ".join(args).strip("\r\n") + " intensifies]\n"
    else:
        return "[no argument intensifies]\n"


def hello(user):  # This function responds to a user that inputs "Hello cybits"
    # random.randint(0, 5)
    str = ("are you even cyb, " + user + "?\n")
    return str


def feel():  # >tfw
    str = ('"tfw no gf" is an abbreviated expression for "that feeling [I get] '
              'when [I have] no girlfriend" often used in online discussions and '
              'comments.\n')

    str1 = ("░░░░░░░▄▀▀▀▀▀▀▀▀▀▀▄▄░░░░░░░░░\n"
                "░░░░▄▀▀░░░░░░░░░░░░░▀▄░░░░░░░\n"
                "░░▄▀░░░░░░░░░░░░░░░░░░▀▄░░░░░\n"
                "░░█░░░░░░░░░░░░░░░░░░░░░▀▄░░░\n"
                "░▐▌░░░░░░░░▄▄▄▄▄▄▄░░░░░░░▐▌░░\n"
                "░█░░░░░░░░░░░▄▄▄▄░░▀▀▀▀▀░░█░░\n"
                "▐▌░░░░░░░▀▀▀▀░░░░░▀▀▀▀▀░░░▐▌░\n"
                "█░░░░░░░░░▄▄▀▀▀▀▀░░░░▀▀▀▀▄░█░\n"
                "█░░░░░░░░░░░░░░░░▀░░░▐░░░░░▐▌\n"
                "▐▌░░░░░░░░░▐▀▀██▄░░░░░░▄▄▄░▐▌\n"
                "░█░░░░░░░░░░░▀▀▀░░░░░░▀▀██░▀▄\n"
                "░▐▌░░░░▄░░░░░░░░░░░░░▌░░░░░░█\n"
                "░░▐▌░░▐░░░░░░░░░░░░░░▀▄░░░░░█\n"
                "░░░█░░░▌░░░░░░░░▐▀░░░░▄▀░░░▐▌\n"
                "░░░▐▌░░▀▄░░░░░░░░▀░▀░▀▀░░░▄▀░\n"
                "░░░▐▌░░▐▀▄░░░░░░░░░░░░░░░░█░░\n"
                "░░░▐▌░░░▌░▀▄░░░░▀▀▀▀▀▀░░░█░░░\n"
                "░░░█░░░▀░░░░▀▄░░░░░░░░░░▄▀░░░\n"
                "░░▐▌░░░░░░░░░░▀▄░░░░░░▄▀░░░░░\n"
                "░▄▀░░░▄▀░░░░░░░░▀▀▀▀█▀░░░░░░░\n"
                "▀░░░▄▀░░░░░░░░░░▀░░░▀▀▀▀▄▄▄▄▄\n")


    return str, str1


def autointerject():  # making sure users don't forget the GNU
    str1 = ("I'd just like to interject for moment. What you're referring to as Linux, is in fact, "
            "GNU/Linux - further messages sent privately.\n")

    str2 = ("I'd just like to interject for moment. What you're referring to as Linux, is "
            "in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux. Linux "
            "is not an operating system unto itself, but rather another free component of a fully"
            " functioning GNU system made useful by the GNU corelibs, shell utilities and vital "
            "system components comprising a full OS as defined by POSIX.\n"
            "Many computer users run a modified version of the GNU system every day, "
            "without realizing it. Through a peculiar turn of events, the version of GNU "
            "which is widely used today is often called Linux, and many of its users are not"
            " aware that it is basically the GNU system, developed by the GNU Project.\n"
            "There really is a Linux, and these people are using it, but it is just a "
            "part of the system they use. Linux is the kernel: the program in the system "
            "that allocates the machine's resources to the other programs that you run. "
            "The kernel is an essential part of an operating system, but useless by "
            "itself; it can only function in the context of a complete operating "
            "system.\n"
            "Linux is normally used in combination with the GNU operating system: the "
            "whole system is basically GNU with Linux added, or GNU/Linux. All the "
            "so-called Linux distributions are really distributions of GNU/Linux!\n")

    return str1, str2


def implying():  # >implying this needs a comment
    return ('>implying is used in a mocking manner to challenge an "implication" '
            'that has been made, or sometimes it can be simply used as a joke in '
            'itself.\n')


def sentence():  # This function grabs a random sentence from a txt file and posts it to the channel
    return get_random_line(random.choice(os.listdir("/home/pi/PycharmProjects/cybot/texts/"))) + "\n"
    # return get_random_line(random.choice(os.listdir("/home/polaris/PycharmProjects/cybot/texts/"))) + "\n"


def coolt():
    spaces1 = random.randint(1,5)
    spaces2 = random.randint(1,3)
    string1 = (" "*spaces1 + (u"▲").encode('utf-8'))
    string2 = (" "*spaces2 + (u"▲ ▲").encode('utf-8'))
    return string1, string2


def shrug():
    return u"¯\_(ツ)_/¯".encode('utf-8')

def cute(user, args):
    if len(args.split(" ")) <= 1:
        cutelist = [u"✿◕ ‿ ◕✿".encode('utf-8'), u"❀◕ ‿ ◕❀".encode('utf-8'), u"(✿◠‿◠)".encode('utf-8'),
                    u"(◕‿◕✿) ".encode('utf-8'), u"( ｡◕‿◕｡)".encode('utf-8'), u"(◡‿◡✿)".encode('utf-8'),
                    u"⊂◉‿◉つ ❤".encode('utf-8'), u"{ ◕ ◡ ◕}".encode('utf-8'), u"( ´・‿-) ~ ♥".encode('utf-8'),
                    u"(っ⌒‿⌒)っ~ ♥".encode('utf-8'), u"ʕ´•ᴥ•`ʔσ”".encode('utf-8'), u"(･Θ･) caw".encode('utf-8'),
                    u"(=^･ω･^)y＝".encode('utf-8'), u"ヽ(=^･ω･^=)丿".encode('utf-8'), u"~(=^･ω･^)ヾ(^^ )".encode('utf-8'),
                    u"| (•□•) | (❍ᴥ❍ʋ)".encode('utf-8'), u"ϞϞ(๑⚈ ․̫ ⚈๑)∩".encode('utf-8'), u"ヾ(･ω･*)ﾉ".encode('utf-8'),
                    u"▽・ω・▽ woof~".encode('utf-8'), u"(◎｀・ω・´)人(´・ω・｀*)".encode('utf-8'), u"(*´・ω・)ノ(-ω-｀*)".encode('utf-8'),
                    u"(❁´ω`❁)".encode('utf-8'), u"(＊◕ᴗ◕＊)".encode('utf-8'), u"{´◕ ◡ ◕｀}".encode('utf-8'), u"₍•͈ᴗ•͈₎".encode('utf-8'),
                    u"(˘･ᴗ･˘)".encode('utf-8'), u"(ɔ ˘⌣˘)˘⌣˘ c)".encode('utf-8'), u"(⊃｡•́‿•̀｡)⊃".encode('utf-8'), u"(´ε｀ )♡".encode('utf-8'),
                    u"(◦˘ З(◦’ںˉ◦)♡".encode('utf-8'), u"( ＾◡＾)っ~ ❤ Leper".encode('utf-8'),
                    u"╰(　´◔　ω　◔ `)╯".encode('utf-8'), u"(*･ω･)".encode('utf-8'), u"(∗•ω•∗)".encode('utf-8'), u"( ◐ω◐ )".encode('utf-8')]
        return random.choice(cutelist)
    else:
        args = args.split(" ")[1:]
        args = " ".join(args).strip("\r\n")
        print args
        cutelist = [u"(✿◠‿◠)っ~ ♥ ".encode('utf-8') + args, u"⊂◉‿◉つ ❤ ".encode('utf-8') + args, u"( ´・‿-) ~ ♥ ".encode('utf-8') + args,
                    u"(っ⌒‿⌒)っ~ ♥ ".encode('utf-8') + args, u"ʕ´•ᴥ•`ʔσ” BEARHUG ".encode('utf-8') + args,
                    user + u" ~(=^･ω･^)ヾ(^^ ) ".encode('utf-8') + args, user + u" (◎｀・ω・´)人(´・ω・｀*) ".encode('utf-8') + args,
                    user + u" (*´・ω・)ノ(-ω-｀*) ".encode('utf-8') + args,
                    user + u" (ɔ ˘⌣˘)˘⌣˘ c) ".encode('utf-8') + args,
                    u"(⊃｡•́‿•̀｡)⊃ U GONNA GET HUGGED ".encode('utf-8') + args, args + u" (´ε｀ )♡".encode('utf-8'),
                    user + u" (◦˘ З(◦’ںˉ◦)♡ ".encode('utf-8') + args, u"( ＾◡＾)っ~ ❤ ".encode('utf-8') + args]
        return random.choice(cutelist)

def breaklines(str):  # This function breaks lines at \n and sends the split lines to where they need to go
    strarray = string.split(str, "\n")
    for lines in range(0, len(strarray)):
        print strarray[lines]
    return strarray