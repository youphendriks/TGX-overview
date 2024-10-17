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
    # Extracting each tag in the taglist from the readme.md files
    for project in projectlist:
        tagdict, name = extractData(project, taglist)
        # 4. Create Json
        formatJson = createJSon(tagdict, name)
        # 5. Save Json
        saveJson(formatJson, name)
    # 6. Create HTML
    createHTML(projectlist)
    # 7. Save HTML

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

# 4. Create Json
def createJson(tagdict, name):
    saveJson(tagdict, name)
    formatJson= {}
    for tag in tagdict:
        html = markdown.markdown(tagdict[tag])
        html = html.replace("\n"," ")
        html = html.replace("\t"," ")
        formatJson[tag] = html
    print("formatJson:")
    print(formatJson)
    return formatJson

# 5. Save Json
def saveJson(formatJson, name):
    with open(('db/' + name + '/' + name+'.json'), 'w') as f:
        json.dump(formatJson, f)

# 6. Create HTML
def createHTML(projectlist):
    template = open(("scripts/template-software.html"), 'r').read()
    accordion = ""
    for project in projectlist:
        name = project["name"]
        projectJson= open(("db/" + name + "/" + name + ".json"), 'r').read()
        projectJson= json.loads(projectJson)
        accordion.append('''
            <div class="col">
                <button class="accordion">
                    <h2>
                        ''' + projectJson["Title"] + '''
                    </h2>
                    <p id="statement">
                        ''' + projectJson["Statement"] + '''
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
                            ''' + projectJson["Description"] + '''
                        </p>
                    </p>
                    <p id="license">
                        <h4>
                            <b>
                                License:
                            </b>
                        </h4>
                        <p id="licenseJson">
                            ''' + projectJson["License"] + '''
                        </p>
                    </p>
                    <p id="dependencies">
                        <h4>
                            <b>
                                Dependencies:
                            </b>
                        </h4>
                        <p id="dependenciesJson">
                            ''' + projectJson["Dependencies"] + '''
                        </p>
                    </p>
                    <p id="code-language">
                        <h4>
                            <b>
                                Code language(s):
                            </b>
                        </h4>
                        <p id="code-languageJson">
                            ''' + projectJson["Code language"] + '''
                        </p>
                    </p>
                    <p id="available-platform">
                        <h4>
                            <b>
                                Available platform(s):
                            </b>
                        </h4>
                        <p id="available-platformJson">
                            ''' + projectJson["Available platform"] + '''
                        </p>
                    </p>
                    <p id="interface-cli">
                        <h4>
                            <b>
                                Interface CLI:
                            </b>
                        </h4>
                        <p id="interface-cliJson">
                            ''' + projectJson["Interface CLI"] + '''
                        </p>
                    </p>
                    <p id="interface-gui">
                        <h4>
                            <b>
                                Interface GUI:
                            </b>
                        </h4>
                        <p id="interface-guiJson">
                            ''' + projectJson["Interface GUI"] + '''
                        </p>
                    </p>
                    <p id="interface-web-platform">
                        <h4>
                            <b>
                                Interface web platform:
                            </b>
                        </h4>
                        <p id="interface-web-platformJson">
                            ''' + projectJson["Interface web platform"] + '''
                        </p>
                    </p>
                    <p id="input-format">
                        <h4>
                            <b>
                                Input format:
                            </b>
                        </h4>
                        <p id="input-formatJson">
                            ''' + projectJson["Input format"] + '''
                        </p>
                    </p>
                    <p id="output-format">
                        <h4>
                            <b>
                                Output format:
                            </b>
                        </h4>
                        <p id="output-formatJson">
                            ''' + projectJson["Output format"] + '''
                        </p>
                    </p>
                    <p id="source-code">
                        <h4>
                            <b>
                                Source code:
                            </b>
                        </h4>
                        <p id="source-codeJson">
                            ''' + projectJson["Source code"] + '''
                        </p>
                    </p>
                    <p id="documentation-link">
                        <h4>
                            <b>
                                Documentation link:
                            </b>
                        </h4>
                        <p id="documentation-linkJson">
                            ''' + projectJson["Documentation link"] + '''
                        </p>
                    </p>
                    <p id="installation-instructions">
                        <h4>
                            <b>
                                Installation instructions:
                            </b>
                        </h4>
                        <p id="installation-instructionsJson">
                            ''' + projectJson["Installation instructions"] + '''
                        </p>
                    </p>
                    <p id="zenodo-link">
                        <h4>
                            <b>
                                Zenodo link:
                            </b>
                        </h4>
                        <p id="zenodo-linkJson">
                            ''' + projectJson["Zenodo link"] + '''
                        </p>
                    </p>
                    <p id="citation-instructions">
                        <h4>
                            <b>
                                Citation instructions:
                            </b>
                        </h4>
                        <p id="citation-instructionsJson">
                            ''' + projectJson["Citation instructions"] + '''
                        </p>
                    </p>
                </div>
            </div>''')
    split = template.split('id="bodyContainer">')
    html = split[0] + 'id="bodyContainer">'+ accordion + split[1]
    with open(('pages/software.html'), 'w') as f:
        f.write(html)
    print("fin.")

# 7. Save HTML


main()
