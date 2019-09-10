from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
for ii in range(1):
    markdown =''' <tr>
                                    <td>1</td>
                                    <td>Duke (58)</td>
                                    <td>29-5</td>
                                    <td>1,592</td>
                                    <td>5</td>
                                </tr>
                            <tr>
                                    <td>2</td>
                                    <td>Virginia (5)</td>
                                    <td>29-3</td>
                                    <td>1,497</td>
                                    <td>2</td>
                                </tr>
                            <tr>
                                    <td>3</td>
                                    <td>North Carolina</td>
                                    <td>27-6</td>
                                    <td>1,453</td>
                                    <td>3</td>
                                </tr>
                            <tr>
                                    <td>4</td>
                                    <td>Gonzaga (1)</td>
                                    <td>30-3</td>
                                    <td>1,398</td>
                                    <td>1</td>
                                </tr>
                            <tr>
                                    <td>5</td>
                                    <td>Michigan State</td>
                                    <td>28-6</td>
                                    <td>1,382</td>
                                    <td>6</td>
                                </tr>
                            <tr>
                                    <td>6</td>
                                    <td>Tennessee</td>
                                    <td>29-5</td>
                                    <td>1,270</td>
                                    <td>8</td>
                                </tr>
                            <tr>
                                    <td>7</td>
                                    <td>Kentucky</td>
                                    <td>27-6</td>
                                    <td>1,232</td>
                                    <td>4</td>
                                </tr>
                            <tr>
                                    <td>8</td>
                                    <td>Michigan</td>
                                    <td>28-6</td>
                                    <td>1,146</td>
                                    <td>10</td>
                                </tr>
                            <tr>
                                    <td>9</td>
                                    <td>Texas Tech</td>
                                    <td>26-6</td>
                                    <td>1,033</td>
                                    <td>7</td>
                                </tr>
                            <tr>
                                    <td>10</td>
                                    <td>Florida State</td>
                                    <td>27-7</td>
                                    <td>1,017</td>
                                    <td>12</td>
                                </tr>
                            <tr>
                                    <td>11</td>
                                    <td>Houston</td>
                                    <td>31-3</td>
                                    <td>933</td>
                                    <td>11</td>
                                </tr>
                            <tr>
                                    <td>12</td>
                                    <td>LSU</td>
                                    <td>26-6</td>
                                    <td>886</td>
                                    <td>9</td>
                                </tr>
                            <tr>
                                    <td>13</td>
                                    <td>Purdue</td>
                                    <td>23-9</td>
                                    <td>727</td>
                                    <td>13</td>
                                </tr>
                            <tr>
                                    <td>14</td>
                                    <td>Auburn</td>
                                    <td>26-9</td>
                                    <td>665</td>
                                    <td>22</td>
                                </tr>
                            <tr>
                                    <td>15</td>
                                    <td>Buffalo</td>
                                    <td>31-3</td>
                                    <td>608</td>
                                    <td>18</td>
                                </tr>
                            <tr>
                                    <td>16</td>
                                    <td>Virginia Tech</td>
                                    <td>24-8</td>
                                    <td>595</td>
                                    <td>16</td>
                                </tr>
                            <tr>
                                    <td>17</td>
                                    <td>Kansas</td>
                                    <td>25-9</td>
                                    <td>590</td>
                                    <td>17</td>
                                </tr>
                            <tr>
                                    <td>18</td>
                                    <td>Kansas State</td>
                                    <td>25-8</td>
                                    <td>529</td>
                                    <td>3</td>
                                </tr>
                            <tr>
                                    <td>19</td>
                                    <td>Wofford</td>
                                    <td>29-4</td>
                                    <td>385</td>
                                    <td>20</td>
                                </tr>
                            <tr>
                                    <td>20</td>
                                    <td>Nevada</td>
                                    <td>29-4</td>
                                    <td>361</td>
                                    <td>14</td>
                                </tr>
                            <tr>
                                    <td>21</td>
                                    <td>Wisconsin</td>
                                    <td>23-10</td>
                                    <td>339</td>
                                    <td>19</td>
                                </tr>
                            <tr>
                                    <td>22</td>
                                    <td>Cincinnati</td>
                                    <td>28-6</td>
                                    <td>335</td>
                                    <td>24</td>
                                </tr>
                            <tr>
                                    <td>23</td>
                                    <td>Villanova</td>
                                    <td>25-9</td>
                                    <td>306</td>
                                    <td>25</td>
                                </tr>
                            <tr>
                                    <td>24</td>
                                    <td>Iowa State</td>
                                    <td>23-11</td>
                                    <td>245</td>
                                    <td>NR</td>
                                </tr>
                            <tr>
                                    <td>25</td>
                                    <td>Utah State</td>
                                    <td>28-6</td>
                                    <td>73</td>
                                    <td>NR</td>
                                </tr> '''

tempword = ''
stats = []
for kk in range(len(markdown)):
    if markdown[kk] == '<' and markdown[kk+1] == 't' and markdown[kk+2] == 'r' and markdown[kk+3] == '>' :
        with open('APfullstats.csv', 'a') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            filewriter.writerow(stats)
            stats = []
    if markdown[kk] == '<' and markdown[kk+1] == 't' and markdown[kk+2] == 'd' and markdown[kk+3] == '>' :
        i = 4
        while True:
            if markdown[kk+i] == '<':
                break
            tempword += str(markdown[kk+i])
            i += 1
        stats.append(tempword)
        print(tempword)
        tempword = ''
