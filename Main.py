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
      part_ATT=text.find("js-iconhelper--down nfl-o-icon nfl-o-icon--small")
      part_COMP=text.find("")
      part_YDS=text.find("")
      part_TD=text.find("")
      part_INT=text.find("")
      name = text[text.find('>',part_name)+1:text.find('</h1',part_name)]
      ATT= text[text.find('>',part_ATT)+1:text.find('</h1',part_ATT)]
      COMP= text[text.find('>',part_COMP)+1:text.find('</h1',part_COMP)]
      YDS= text[text.find('>',part_YDS)+1:text.find('</h1',part_YDS)]
      TD= text[text.find('>',part_TD)+1:text.find('</h1',part_TD)]
      INT= text[text.find('>',part_name)+1:text.find('</h1',part_name)]
      print(name,file=f_out)
      print(ATT,file=f_out)
      print(COMP,file=f_out)
      print(name,file=f_out)
      print(name,file=f_out)
      
part_ATT = text.find('passingAttempts')
ATT = text[text.find('>',part_ATT)+1:text.find('</th',part_ATT)]
ATT = ATT.replace('n','').replace('\\','').strip()
print(ATT)

part_COMP = text.find('passingCompletions')
COMP = text[text.find('>',part_COMP)+1:text.find('</th',part_COMP)]
COMP = COMP.replace('n','').replace('\\','').strip()
print(COMP)

part_YDS = text.find('passingYards')
YDS = text[text.find('>',part_YDS)+1:text.find('</th',part_YDS)]
YDS = YDS.replace('n','').replace('\\','').strip()
print(YDS)

part_TD = text.find('passingTouchdowns')
TD = text[text.find('>',part_TD)+1:text.find('</th',part_TD)]
TD = TD.replace('n','').replace('\\','').strip()
print(TD)

part_INT = text.find('passingInterceptions')
INT = text[text.find('>',part_INT)+1:text.find('</th',part_INT)]
INT = INT.replace('n','').replace('\\','').strip()
print(INT)











