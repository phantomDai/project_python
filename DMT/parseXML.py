from xml.dom.minidom import parse
import os

def parsexml():
    doc = parse("MOS.xml")
    # get root
    root = doc.documentElement
    groups = root.getElementsByTagName("pairsfromdiffgroups")
    countNo = 0

    for group in groups:
        pair = group.getElementsByTagName("pair")[0]
        hasmr = pair.getElementsByTagName("hasmr")[0]
        if hasmr.childNodes[0].data is "No":
            countNo = countNo + 1
            continue
        else:




