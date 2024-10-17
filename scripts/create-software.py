#!/usr/bin/env python3
import os
import json
import markdown
from bs4 import BeautifulSoup

# 0. Call functions
def main():
    # Preparing str
    accordion = ""
    # 1. Import projectlist
    projectlist = importProjectlist("scripts/project_list.json")
    # 2. Import taglist
    taglist = importTaglist("scripts/tag_list.json")
    # 3. Extract data
    # Extracting each tag in the taglist from the readme.md files
    for project in projectlist:
        tagdict, name = extractData(project, taglist)
        # 5. Create Accordion
        accordion = createAccordion(tagdict, name, accordion)
        # 6. Create Json
        formatJson = createJson(tagdict, name)
        # 7. Save Json
        saveJson(formatJson, name)
    # 8. Save HTML
    saveHTML(accordion)

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
    return tagdict, name

# 4. Create Accordion
def createAccordion(tagdict, name, accordion):
    accordion = accordion + '''
        <div class="col">
            <button class="accordion">
                <h2>
                    ''' + tagdict["Title"] + '''
                </h2>
                <p id="statement">
                    ''' + tagdict["Statement"] + '''
                </p>
            </button>
            <div class="panel">
                <p id="description">
                    <h4>
                        <b>
                            Description:
                        </b>
                    </h4>
                    <p id="descriptionJson">
                        ''' + tagdict["Description"] + '''
                    </p>
                </p>
                <p id="license">
                    <h4>
                        <b>
                            License:
                        </b>
                    </h4>
                    <p id="licenseJson">
                        ''' + tagdict["License"] + '''
                    </p>
                </p>
                <p id="dependencies">
                    <h4>
                        <b>
                            Dependencies:
                        </b>
                    </h4>
                    <p id="dependenciesJson">
                        ''' + tagdict["Dependencies"] + '''
                    </p>
                </p>
                <p id="code-language">
                    <h4>
                        <b>
                            Code language(s):
                        </b>
                    </h4>
                    <p id="code-languageJson">
                        ''' + tagdict["Code language"] + '''
                    </p>
                </p>
                <p id="available-platform">
                    <h4>
                        <b>
                            Available platform(s):
                        </b>
                    </h4>
                    <p id="available-platformJson">
                        ''' + tagdict["Available platform"] + '''
                    </p>
                </p>
                <p id="interface-cli">
                    <h4>
                        <b>
                            Interface CLI:
                        </b>
                    </h4>
                    <p id="interface-cliJson">
                        ''' + tagdict["Interface CLI"] + '''
                    </p>
                </p>
                <p id="interface-gui">
                    <h4>
                        <b>
                            Interface GUI:
                        </b>
                    </h4>
                    <p id="interface-guiJson">
                        ''' + tagdict["Interface GUI"] + '''
                    </p>
                </p>
                <p id="interface-web-platform">
                    <h4>
                        <b>
                            Interface web platform:
                        </b>
                    </h4>
                    <p id="interface-web-platformJson">
                        ''' + tagdict["Interface web platform"] + '''
                    </p>
                </p>
                <p id="input-format">
                    <h4>
                        <b>
                            Input format:
                        </b>
                    </h4>
                    <p id="input-formatJson">
                        ''' + tagdict["Input format"] + '''
                    </p>
                </p>
                <p id="output-format">
                    <h4>
                        <b>
                            Output format:
                        </b>
                    </h4>
                    <p id="output-formatJson">
                        ''' + tagdict["Output format"] + '''
                    </p>
                </p>
                <p id="source-code">
                    <h4>
                        <b>
                            Source code:
                        </b>
                    </h4>
                    <p id="source-codeJson">
                        ''' + tagdict["Source code"] + '''
                    </p>
                </p>
                <p id="documentation-link">
                    <h4>
                        <b>
                            Documentation link:
                        </b>
                    </h4>
                    <p id="documentation-linkJson">
                        ''' + tagdict["Documentation link"] + '''
                    </p>
                </p>
                <p id="installation-instructions">
                    <h4>
                        <b>
                            Installation instructions:
                        </b>
                    </h4>
                    <p id="installation-instructionsJson">
                        ''' + tagdict["Installation instructions"] + '''
                    </p>
                </p>
                <p id="zenodo-link">
                    <h4>
                        <b>
                            Zenodo link:
                        </b>
                    </h4>
                    <p id="zenodo-linkJson">
                        ''' + tagdict["Zenodo link"] + '''
                    </p>
                </p>
                <p id="citation-instructions">
                    <h4>
                        <b>
                            Citation instructions:
                        </b>
                    </h4>
                    <p id="citation-instructionsJson">
                        ''' + tagdict["Citation instructions"] + '''
                    </p>
                </p>
            </div>
        </div>'''
    return accordion

# 6. Create Json
def createJson(tagdict, name):
    formatJson= {}
    for tag in tagdict:
        html = markdown.markdown(tagdict[tag])
        html = html.replace("\n"," ")
        html = html.replace("\t"," ")
        html = html.replace("<p>"," ")
        html = html.replace("</p>"," ")
        formatJson[tag] = html
    print("formatJson:")
    print(formatJson)
    return formatJson

# 7. Save Json
def saveJson(formatJson, name):
    with open(('db/' + name + '/' + name+'.json'), 'w') as f:
        json.dump(formatJson, f)

# 8. Save HTML
def saveHTML(accordion):
    template = open(("scripts/template-software.html"), 'r').read()
    split = template.split('id="bodyContainer">')
    html = split[0] + 'id="bodyContainer">'+ accordion + split[1]
    with open(('pages/software.html'), 'w') as f:
        f.write(html)

main()
