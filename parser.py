from bs4 import BeautifulSoup
from collections import OrderedDict
import csv
import os


fileNumber = 0  # starting from file 0
while os.path.exists("Movies\\movie" + str(fileNumber) + ".html"):  # Iterating for each file

    # Parsing the html file:
    with open("Movies\\movie" + str(fileNumber) + ".html", 'rb') as html:
        soup = BeautifulSoup(html)

    # initialysing variables as NA, so if the sections are missing the variable remains NA
    title = "NA"
    intro = "NA"
    plot = "NA"
    link = "NA"
    infobox = OrderedDict()  # we must put as key of the dict the keyword that we will find in the infobox of wikipedia:
    infobox["name"] = "NA"
    infobox["Directed by"] = "NA"
    infobox["Produced by"] = "NA"
    infobox["Written by"] = "NA"
    infobox["Starring"] = "NA"
    infobox["Music by"] = "NA"
    infobox["Release date"] = "NA"
    infobox["Running time"] = "NA"
    infobox["Country"] = "NA"
    infobox["Language"] = "NA"
    infobox["Budget"] = "NA"

    # we do fetch the infos only if the page is not a disambiguation page
    if not soup.body.find('a', title="Help:Disambiguation"):
        # -------------------------- Title, Intro and Plot code ----------------------------------------
        title = soup.title.string.strip(" - Wikipedia")  # taking the title, without the " - Wikipedia" last part.

        body = soup.body  # put the soup body in a variable.
        paragraphNumber = 1  # a counter for know whitch paragraf are we working on
        for paragraph in body.find_all('p'):  # iterating on the paragrafs
            if (paragraphNumber == 1):  # putting the first paragraf in the intro variable
                intro = paragraph.text.strip()  # using strip to delete space characters
                paragraphNumber += 1
            elif (paragraphNumber == 2):  # putting the second paragraf in the plot variable
                plot = paragraph.text.strip()  # using strip to delete space characters
                break  # we don't need the other paragrafs

        link = link = soup.find('link', rel='canonical')["href"]
        # -------------------------- Title, Intro and Plot code ----------------------------------------

        # -------------------------- Infobox code ----------------------------------------
        table = soup.find('table', class_='infobox vevent')

        try:
            infobox["name"] = table.find('tr').text  # let's search the infobox
            for tr in table.find_all('tr'):  # for each content in the infobox
                for section in infobox.keys():  # check for each content that we need...
                    try:
                        if section == tr.find('th').text:  # check if the current tr is the section that we wont
                            infobox[section] = tr.find('td').text.strip()  # if it is, save it in the infobox[section]
                    except:
                        pass  # if it is an empty tag
        except:
            pass  # if the infobox is not in the page
        # -------------------------- Infobox code ----------------------------------------

    # -------------------------- Writing on the file ----------------------------------------
    # this lines create a new directory, Movies, in your project folder
    if not os.path.exists("MoviesTSV\\"):
        os.makedirs("MoviesTSV\\")

    # writing the results in the tsv file
    with open('MoviesTSV\\article_' + str(fileNumber) + '.tsv', 'wt',
              encoding='utf-8') as out_file:  # creating one file for each different movie
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow([title, intro, plot, link] + list(infobox.values()))  # input to the tsv file.
    # -------------------------- Writing on the file ----------------------------------------

    fileNumber += 1  # let's move to the next file!