#!/usr/bin/python3.7
# written by: atholcomb
# imgur_parser.py

def imgurUrlParser(link):
    if ".png" in link:
        p = link.index(".png")
        link = link[:p]
    if "/a/" in link:
        a = link.index('a/')
        return f'(id: "{link[a+2:]}", type: "album")' + ' -> ' + link
    elif "gallery" in link:
        g = link.index('ry')
        return f'(id: "{link[g+3:]}", type: "gallery")' + ' -> ' + link
    else:
        i = link.index('m/')
        return f'(id: "{link[i+2:]}", type: "image")' + ' -> ' + link


print(imgurUrlParser("http://imgur.com/a/cjh4E"))
print(imgurUrlParser("http://imgur.com/gallery/59npG"))
print(imgurUrlParser("http://imgur.com/OzZUNMM"))
print(imgurUrlParser("http://i.imgur.com/altd8Ld.png"))
