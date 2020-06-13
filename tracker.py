import json, urllib.request, os, time

while(1):
    os.system('cls')
    page = urllib.request.urlopen('http://api.ttr-invasions.com/json/invasionlist/')
    data = sorted(json.load(page), key = lambda i: (i['invasion_cog']))

    for line in data:
        cog = line.get("invasion_cog")
        cogtype = line.get("invasion_cogType")
        shard = line.get("invasion_district")
        progress = line.get("invasion_progress")
        remainder = line.get("invasion_remaining")
        if cog == "Mover &amp; Shaker":
            cog = "Mover & Shaker"

        print(f'{cog:<17} {cogtype:<9} {shard:<14} {progress:<10} {remainder:}', flush = True)

    time.sleep(9.99)