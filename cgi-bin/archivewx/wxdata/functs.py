#!/usr/local/bin/python
# This is funct file for Archived Weather Data Searching
# Daryl Herzmann 2/25/99

from cgi import *
import os, style, re


def get_content(field):
        form = FormContent()
        if form.has_key(field):
                return form[field][0]
        else:
                style.SendError("No "+field+" specified")

def convert_month(month):
        file = '/home/httpd/html/src/months.con'
        f = open(file,'r').read()

        lines = re.split('\n',f)
        for i in range(len(lines)):
                line = lines[i]
                if month == line[-2:]:
                        name = line[:-3]
        return name

