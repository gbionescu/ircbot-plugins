import praw
import random
from cloudbot import hook

USER_AGENT = "Image fetcher for Snoonet:#Romania by /u/programatorulupeste"
domains = ['imgur.com', 'gfycat.com', 'redditmedia.com']

def get_links_from_subs(sub):
    data = []
    r = praw.Reddit("irc_bot", user_agent=USER_AGENT)

    for el in sub:
        subreddit = r.subreddit(el)

        for submission in subreddit.top("month"):
            if not submission.is_self:
                for domain in domains:
                    if domain in submission.url:
                        data.append(submission)
                        break
    return data

@hook.command()
def roscate(message, text, nick):
    data = get_links_from_subs(['ginger', 'redheads', 'RedheadGifs'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def nsfwfunny(message, text, nick):
    data = get_links_from_subs(['nsfwfunny'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def craci(message, text, nick):
    data = get_links_from_subs(['thighhighs', 'stockings'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def buci(message, text, nick):
    data = get_links_from_subs(['ass', 'asstastic', 'assinthong', 'pawg'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def tzatze(message, text, nick):
    data = get_links_from_subs(['boobs', 'boobies', 'BiggerThanYouThought'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def fetish(message, text, nick):
    data = get_links_from_subs(['kinky', 'bdsm', 'bondage', 'collared', 'lesdom'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def teen(message, text, nick):
    data = get_links_from_subs(['LegalTeens', 'Just18', 'youngporn', 'barelylegal'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def sloboz(message, text, nick):
    data = get_links_from_subs(['cumsluts', 'GirlsFinishingTheJob'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def anal(message, text, nick):
    data = get_links_from_subs(['anal', 'painal'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def milf(message, text, nick):
    data = get_links_from_subs(['milf'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def amateur(message, text, nick):
    data = get_links_from_subs(['RealGirls', 'Amateur', 'GoneWild'])

    return random.choice(data).url + " NSFW!"

@hook.command()
def traps(message, text, nick):
    data = get_links_from_subs(['Tgirls', 'traps', 'gonewildtrans', 'tgifs'])

    return random.choice(data).url + " NSFW!"
