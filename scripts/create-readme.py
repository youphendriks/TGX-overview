#!/usr/bin/env python3
import json
import os

import markdown


def main():
    """0. Call functions"""
    # 1. Import projectlist
    projectlist = import_projectlist("scripts/project_list.json")
    # 2. Import taglist
    taglist = import_taglist("scripts/tag_list.json")
    # 3. Extract data
    for project in projectlist:
        extract_data(project, taglist)
        # 4. Format Json
        # 5. Create Json
    # 6. Create HTML
    create_html(projectlist)


def import_projectlist(path):
    """1. Import projectlist"""
    with open(path, encoding="utf-8") as f:
        projectlist = json.load(f)
    for project in projectlist:
        name = project["name"]
        rawlink = project["rawlink"]
        os.system("rm -vr db/" + name)
        os.system("mkdir -p db/" + name)
        os.system("wget -O db/" + name + "/README.md " + rawlink)
    return projectlist


def import_taglist(path):
    """2. Import taglist"""
    with open(path, encoding="utf-8") as f:
        taglist = json.load(f)
    print("Taglist:")
    print(taglist)
    return taglist


def extract_data(project, taglist):
    """3. Extract data"""
    name = project["name"]
    path = "db/" + name + "/README.md"
    project_readme = open(path, "r", encoding="utf-8").read()
    tagdict = {}
    for tag in taglist:
        try:
            split1 = project_readme.split("<!--" + tag + "-->")
            split2 = split1[1].split("<!--/" + tag + "-->")
            tagdict[tag] = split2[0]
        except:
            tagdict[tag] = "404 data not found"
    # print(tagdict)
    format_json(tagdict, name)


def format_json(tagdict, name):
    """4. Format Json"""
    format_tagdict = {}
    for tag in tagdict:
        html = markdown.markdown(tagdict[tag])
        html = html.replace("\n", " ")
        html = html.replace("\t", " ")
        format_tagdict[tag] = html
    print("format_tagdict:")
    print(format_tagdict)
    create_json(format_tagdict, name)


def create_json(format_tagdict, name):
    """# 5. Create Json"""
    path = "db/" + name + "/" + name + ".json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(format_tagdict, f)


def create_html(projectlist):
    """# 6. Create HTML"""
    path = "scripts/template-software.html"
    template = open(path, "r", encoding="utf-8").read()
    accordion = ""
    for project in projectlist:
        name = project["name"]
        path = "db/" + name + "/" + name + ".json"
        projet_html = open(path, "r", encoding="utf-8").read()
        projet_html = json.loads(projet_html)
        accordion += (
            '<div class="col"><button class="accordion"><h2>'
            + projet_html["Title"]
            + '</h2><p id="statement">'
            + projet_html["Statement"]
            + '</p></button><div class="panel"><p id="description"><h4><b>Description:</b></h4>'
            + projet_html["Description"]
            + "</div></div>"
        )
    split = template.split('id="bodyContainer">')
    html = split[0] + 'id="bodyContainer">' + accordion + split[1]
    with open(("pages/software.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("fin.")


main()
