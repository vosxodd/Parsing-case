# Case-study #4
# Developers:   Aksenov A. (%),
#               Soloveychik D. (%),
#               Labuzov A. (%)
import urllib.request
with open("input.txt") as f:
  with open("output.txt","w") as f_out:
    for line in f:
      url = line
      f = urllib.request.urlopen(url)
      s = f.read()
      text = str(s)
      part_name = text.find("nfl-c-player-header__title")
      name = text[text.find('>',part_name)+1:text.find('</h1',part_name)]
      print(name,file=f_out)









