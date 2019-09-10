from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv


def teamCsvCreator(teamName,markdown):
    b1 = False
    b2 = False
    b3 = False
    b4 = False
    tempstr = ''
    dates = []
    opponents = []
    scores = []
    score = 0
    for kk in range(len(markdown)):
        if markdown[kk] == '<' and markdown[kk+1] == 't' and markdown[kk+2] == 'r' and markdown[kk+3] == ' ' and markdown[kk+4] == '>':
            #Create new row in csv
            b1 = False
            b2 = False
            b3 = False
            b4 = False
        if b1 == False and markdown[kk] == 's' and markdown[kk+1] == 'm' and markdown[kk+2] == 't' :
            b1 = True
            for ii in range(8,18):
                tempstr += markdown[kk+ii]
            dates.append(tempstr)
            tempstr = ''
        if b1 == True and b2 == False and markdown[kk] == 'a' and markdown[kk+1] == ' ' and markdown[kk+2] == 'h' and markdown[kk+3] == 'r' and markdown[kk+4] == 'e':
            b2 = True
        if b1 == True and b2 == True and b3 == False and markdown[kk] == '>':
            b3 = True
            i = 1
            while True:
                if markdown[kk+i] == '<':
                    break
                tempstr += markdown[kk+i]
                i += 1
            opponents.append(tempstr)
            tempstr = ''
        if b1 == True and b2 == True and b3 == True and b4 == False and markdown[kk] == 'a' and markdown[kk+1] == ' ' and markdown[kk+2] == 'h' and markdown[kk+3] == 'r' and markdown[kk+4] == 'e':
            i = 1
            while True:
                if markdown[kk+i] == '>':
                    i += 1
                    break
                i += 1
            while True:
                if markdown[kk+i] == '<':
                    break
                tempstr += markdown[kk+i]
                i += 1
            scores.append(tempstr)
            tempstr = ''

    teamcsv = str(teamName)+'.csv'
    with open(teamcsv, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')

        for date in range(len(dates)):
            filewriter.writerow([dates[date],opponents[date],scores[date]])
    print(teamName)
    return





























markdown = '''<tr >
           <td class="smtext">11/06/2018</td>
           <td class="smtext">

                     <a href="/team/817/14300"> Youngstown St. </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4654200?org_id=545" class="skipMask" target="TEAM_WIN">W 69 - 53 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">11/09/2018</td>
           <td class="smtext">

                     <a href="/team/741/14300"> VMI </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4655978?org_id=545" class="skipMask" target="TEAM_WIN">W 94 - 55 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">11/12/2018</td>
           <td class="smtext">

                     <a href="/team/716/14300"> Troy </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4659012?org_id=545" class="skipMask" target="TEAM_WIN">W 84 - 75 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">11/15/2018</td>
           <td class="smtext">

                     <a href="/team/1004/14300"> Central Ark. </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4660411?org_id=545" class="skipMask" target="TEAM_WIN">W 97 - 71 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">11/17/2018</td>
           <td class="smtext">

                     <a href="/team/487/14300"> North Ala. </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4661805?org_id=545" class="skipMask" target="TEAM_WIN">W 71 - 66 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">11/21/2018</td>
           <td class="smtext">

                     <a href="/team/609/14300"> Saint Louis <br/>@ Brooklyn, N.Y. - Barclays Center</a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4664938?org_id=545" class="skipMask" target="TEAM_WIN">W 75 - 73 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">11/27/2018</td>
           <td class="smtext">

                     <a href="/team/312/14300">@ Iowa </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4667848?org_id=545" class="skipMask" target="TEAM_WIN">L 68 - 69 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">11/30/2018</td>
           <td class="smtext">

                     <a href="/team/194/14300"> Duquesne <br/>@ PPG Paints Arena (Pittsburgh, Pa.)</a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4669200?org_id=545" class="skipMask" target="TEAM_WIN">W 74 - 53 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">12/03/2018</td>
           <td class="smtext">

                     <a href="/team/482/14300"> Niagara </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4670947?org_id=545" class="skipMask" target="TEAM_WIN">L 70 - 71 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">12/08/2018</td>
           <td class="smtext">

                     <a href="/team/768/14300">@ West Virginia </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4672806?org_id=545" class="skipMask" target="TEAM_WIN">L 59 - 69 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">12/15/2018</td>
           <td class="smtext">

                     <a href="/team/393/14300"> UMES </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4675052?org_id=545" class="skipMask" target="TEAM_WIN">W 78 - 43 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">12/20/2018</td>
           <td class="smtext">

                     <a href="/team/474/14300"> New Orleans </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4677183?org_id=545" class="skipMask" target="TEAM_WIN">W 99 - 57 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">12/29/2018</td>
           <td class="smtext">

                     <a href="/team/153/14300"> Colgate </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4678735?org_id=545" class="skipMask" target="TEAM_WIN">W 68 - 54 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">01/05/2019</td>
           <td class="smtext">

                     <a href="/team/457/14300"> North Carolina </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4681088?org_id=545" class="skipMask" target="TEAM_WIN">L 60 - 85 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">01/09/2019</td>
           <td class="smtext">

                     <a href="/team/367/14300"> Louisville </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4683410?org_id=545" class="skipMask" target="TEAM_WIN">W 89 - 86 (1OT)</a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">01/12/2019</td>
           <td class="smtext">

                     <a href="/team/490/14300">@ NC State </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4684383?org_id=545" class="skipMask" target="TEAM_WIN">L 80 - 86 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">01/14/2019</td>
           <td class="smtext">

                     <a href="/team/234/14300"> Florida St. </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4685902?org_id=545" class="skipMask" target="TEAM_WIN">W 75 - 62 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">01/19/2019</td>
           <td class="smtext">

                     <a href="/team/688/14300">@ Syracuse </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4687990?org_id=545" class="skipMask" target="TEAM_WIN">L 63 - 74 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">01/22/2019</td>
           <td class="smtext">

                     <a href="/team/193/14300"> Duke </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4689499?org_id=545" class="skipMask" target="TEAM_WIN">L 64 - 79 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">01/26/2019</td>
           <td class="smtext">

                     <a href="/team/367/14300">@ Louisville </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4691766?org_id=545" class="skipMask" target="TEAM_WIN">L 51 - 66 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">01/29/2019</td>
           <td class="smtext">

                     <a href="/team/147/14300">@ Clemson </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4692638?org_id=545" class="skipMask" target="TEAM_WIN">L 69 - 82 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">02/02/2019</td>
           <td class="smtext">

                     <a href="/team/688/14300"> Syracuse </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4695294?org_id=545" class="skipMask" target="TEAM_WIN">L 56 - 65 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">02/05/2019</td>
           <td class="smtext">

                     <a href="/team/749/14300">@ Wake Forest </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4696987?org_id=545" class="skipMask" target="TEAM_WIN">L 76 - 78 (1OT)</a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">02/09/2019</td>
           <td class="smtext">

                     <a href="/team/490/14300"> NC State </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4699852?org_id=545" class="skipMask" target="TEAM_WIN">L 76 - 79 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">02/12/2019</td>
           <td class="smtext">

                     <a href="/team/67/14300">@ Boston College </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4702874?org_id=545" class="skipMask" target="TEAM_WIN">L 57 - 66 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">02/16/2019</td>
           <td class="smtext">

                     <a href="/team/742/14300"> Virginia Tech </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4706987?org_id=545" class="skipMask" target="TEAM_WIN">L 64 - 70 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">02/20/2019</td>
           <td class="smtext">

                     <a href="/team/255/14300">@ Georgia Tech </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4711184?org_id=545" class="skipMask" target="TEAM_WIN">L 65 - 73 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">02/27/2019</td>
           <td class="smtext">

                     <a href="/team/147/14300"> Clemson </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4717382?org_id=545" class="skipMask" target="TEAM_WIN">L 48 - 62 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">03/02/2019</td>
           <td class="smtext">

                     <a href="/team/746/14300">@ Virginia </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4720269?org_id=545" class="skipMask" target="TEAM_WIN">L 49 - 73 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">03/05/2019</td>
           <td class="smtext">

                     <a href="/team/415/14300">@ Miami (FL) </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4724114?org_id=545" class="skipMask" target="TEAM_WIN">L 63 - 76 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">03/09/2019</td>
           <td class="smtext">

                     <a href="/team/513/14300"> Notre Dame </a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4727543?org_id=545" class="skipMask" target="TEAM_WIN">W 56 - 53 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">03/12/2019</td>
           <td class="smtext">

                     <a href="/team/67/14300"> Boston College <br/>@ Charlotte, NC</a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4732581?org_id=545" class="skipMask" target="TEAM_WIN">W 80 - 70 </a>
           </td>


	     </tr>

          <tr >
           <td class="smtext">03/13/2019</td>
           <td class="smtext">

                     <a href="/team/688/14300"> Syracuse <br/>@ Charlotte, NC</a>
           </td>
           <td class="smtext" nowrap>
                <a href="/game/index/4733958?org_id=545" class="skipMask" target="TEAM_WIN">L 59 - 73 </a>
           </td>
'''

teamCsvCreator('Pittsburgh',markdown)
