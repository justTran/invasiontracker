import json, urllib, urllib2, os, time, string

'''
This function runs in an infinite loop. It uses the 
try / except clause as a error handling measure. It makes a 
request to the API to return some json data. The data is 
then sorted by the Cog name key and printed to the terminal. 
The process repeats after 9.5 seconds due to API limitations.
'''

while True:
  try:
    page = urllib2.urlopen('http://api.ttr-invasions.com/json/invasionlist/')
    data = sorted(json.load(page), key = lambda i: (i['invasion_cog']))
    os.system('cls')

    for line in data:
      cog = line.get("invasion_cog")
      cogtype = line.get("invasion_cogType")
      shard = line.get("invasion_district")
      progress = line.get("invasion_progress")
      remainder = line.get("invasion_remaining")
      print ('{:<17} {:<9} {:<14} {:<10} {:}'.format(cog, cogtype, shard, progress, remainder))

    time.sleep(9.5)

  except:
    pass


