# Case-study #4
# Developers:   Aksenov A. (%),
#               Soloveychik D. (%),
#               Labuzov A. (%)
import urllib.request
k=19
y=6
with open("input.txt") as f:
  with open("output.txt","w") as f_out:
    for line in f:
      url = line
      f = urllib.request.urlopen(url)
      s = f.read()
      text = str(s)
      part_name = text.find("nfl-c-player-header__title")
      part_ATT = text.find('passingAttempts')
      part_COMP = text.find('passingCompletions')
      part_YDS = text.find('passingYards')
      part_TD = text.find('passingTouchdowns')
      part_INT = text.find('passingInterceptions')
      name = text[text.find('>',part_name)+1:text.find('</h1',part_name)]
      ATT = text[text.find('>',part_ATT)+1:text.find('</th',part_ATT)]
      ATT = ATT.replace('n','').replace('\\','').strip()
      COMP = text[text.find('>',part_COMP)+1:text.find('</th',part_COMP)]
      COMP = COMP.replace('n','').replace('\\','').strip()
      YDS= text[text.find('>',part_YDS)+1:text.find('</th',part_YDS)]
      YDS = YDS.replace('n','').replace('\\','').strip()
      TD= text[text.find('>',part_TD)+1:text.find('</th',part_TD)]
      TD = TD.replace('n','').replace('\\','').strip()
      INT= text[text.find('>',part_INT)+1:text.find('</th',part_INT)]
      INT = INT.replace('n','').replace('\\','').strip()
      part_PR = text.find('passingPasserRating')
      PR = text[text.find('>',part_PR)+1:text.find('</th',part_PR)]
      PR = PR.replace('n','').replace('\\','').strip()
      PR = format(float(PR),'.2f')
      print(name+" "*(k-len(name)),COMP+" "*(y-len(COMP)),ATT+" "*(y-len(ATT)),YDS+" "*(y-len(YDS)),TD+" "*(y-len(TD)),INT+" "*(y-len(INT)),PR+" "*(y-len(PR)))
      
