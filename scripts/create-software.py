#!/usr/bin/env python3
import os
import json
import markdown
from bs4 import BeautifulSoup

# 0. Call functions
def main():
    # 1. Import projectlist
    projectlist = importProjectlist("scripts/project_list.json")
    # 2. Import taglist
    taglist = importTaglist("scripts/tag_list.json")
    # 3. Extract data
    for project in projectlist:
        extractData(project, taglist)
        # 4. Format Json
        # 5. Create Json
    # 6. Create HTML
    createHTML(projectlist)

# 1. Import projectlist
def importProjectlist(path):
    with open(path) as f:
        projectlist = json.load(f)
    for project in projectlist:
        name = project["name"]
        rawlink = project["rawlink"]
        os.system("rm -vr db/" + name)
        os.system("mkdir -p db/" + name)
        os.system("wget -O db/" + name + "/README.md " + rawlink)
    return projectlist

# 2. Import taglist
def importTaglist(path):
    with open(path) as f:
        taglist = json.load(f)
    print("Taglist:")
    print(taglist)
    return taglist

# 3.Extract data
def extractData(project, taglist):
    name = project["name"]
    projectlib = open(("db/" + name + "/README.md"), 'r').read()
    tagdict = {}
    for tag in taglist:
        try:
            split1 = projectlib.split("<!--"+tag+"-->")
            split2 = split1[1].split("<!--/"+tag+"-->")
            tagdict[tag]=split2[0]
        except:
            tagdict[tag]="404 data not found"
    # print(tagdict)
    formatJson(tagdict, name)

# 4. Format Json
def formatJson(tagdict, name):
    createJson(tagdict, name)
    formatTagdict = {}
    for tag in tagdict:
        html = markdown.markdown(tagdict[tag])
        html = html.replace("\n"," ")
        html = html.replace("\t"," ")
        html = html.replace("\t"," ")
        formatTagdict[tag] = html
    print("formatTagdict:")
    print(formatTagdict)

# 5. Create Json
def createJson(formatTagdict, name):
    with open(('db/' + name + '/' + name+'.json'), 'w') as f:
        json.dump(formatTagdict, f)

# 6. Create HTML
def createHTML(projectlist):
    template = open(("scripts/template-software.html"), 'r').read()
    accordion = ""
    for project in projectlist:
        name = project["name"]
        projectHTML= open(("db/" + name + "/" + name + ".json"), 'r').read()
        projectHTML = json.loads(projectHTML)
        accordion = '<div class="col"><button class="accordion"><h2>' + projectHTML["Title"] + '</h2><br><p id="statement">' + projectHTML["Statement"] + '<br></p></button><div class="panel"><p id="description"><h4><b>Description:</b></h4><br>' + projectHTML["Description"] + '</div></div>'
    split = template.split('id="bodyContainer">')
    html = split[0] + 'id="bodyContainer">'+ accordion + split[1]
    with open(('pages/software.html'), 'w') as f:
        f.write(html)
    print("fin.")

main()
