# Snippets

[<img align="left" alt="Website" width="135px" src="https://www.python.org/static/community_logos/python-logo-inkscape.svg" />][python]
[<img align="left" alt="Website" width="120px" src="https://i.imgur.com/BOgY9ai.png" />][pyrogram]

<br />

<br />

## INFO
``` python

secret = b'\x5b\x22\x53\x6f\x6d\x65\x22\x2c\x22\x55\x73\x65\x66\x75\x6c\x6c\x22\x2c\x22\x61\x6e\x64\x22\x2c\x22\x46\x75\x6e\x22\x2c\x22\x50\x79\x74\x68\x6f\x6e\x2d\x50\x79\x72\x6f\x22\x2c\x22\x53\x6e\x69\x70\x70\x65\x74\x73\x22\x2c\x22\x62\x79\x22\x2c\x22\x61\x22\x2c\x22\x4e\x6f\x6f\x62\x22\x2c\x22\xf0\x9f\xa5\xb2\x22\x5d'
hack = secret.decode("utf-8")
oops = hack.strip('][').split(', ')
text = " ".join(oops).replace('"','')
final_text = text.replace(',',' ')

print(final_text) #😁

```

[python]: www.python.org
[pyrogram]: https://github.com/pyrogram/pyrogram
