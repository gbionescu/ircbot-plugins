import praw
import random
from cloudbot import hook
from datetime import datetime

USER_AGENT = "Image fetcher for Snoonet:#Romania by /u/programatorulupeste"
domains = ['imgur.com', 'gfycat.com', 'redditmedia.com']

class cache_elem:
    last_fetch = None
    links = None
    def __init__(self):
        self.last_fetch = 0
        self.links = []

caches = {}

def refresh_cache(r, el):
    print("Refreshing cache for " + el)
    subreddit = r.subreddit(el)
    caches[el].links.clear()
    for submission in subreddit.top("month"):
        if not submission.is_self:
            for domain in domains:
                if domain in submission.url:
                    caches[el].links.append(submission)
                    break
    caches[el].last_fetch = datetime.utcnow()

def get_links_from_subs(sub):
    data = []
    r = praw.Reddit("irc_bot", user_agent=USER_AGENT)

    now = datetime.utcnow()
    
    for el in sub:
        if el in caches:
            print("Found cache for " + el)
            el_cache = caches[el]
            # Cache older than 2 hours?
            if (now - el_cache.last_fetch).total_seconds() > 7200:
                refresh_cache(r, el)
        
            data.extend(el_cache.links)
        else:
            print("Cold cache for " + el)
            caches[el] = cache_elem()
            refresh_cache(r, el)
            data.extend(caches[el].links)
    print(len(data)) 
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
