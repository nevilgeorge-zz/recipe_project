# requester.py
import requests, re
from bs4 import BeautifulSoup
import csv

class Tools:

  # constructor takes in a link of a recipe from allRecipes.com
  def __init__(self, link):
    # GET the markup of the URL and store it as a member
    r = requests.get(link)
    self.markup = BeautifulSoup(r.text)
    # web URL of the allRecipes link we are using in this instance of the Recipe
    self.link = link
    #list of tools
    self.tools = self.find_tools()


  # find all tools used in directions, and return a list of all the tools (in order)
  def find_tools(self):
    elements = self.markup.select('.directions')
    arr = []
    for el in elements:
        arr.append(el.text)
    self.tools=arr

    all_tools = []

    #build a list of all tools
    with open('tools.csv') as inputfile:
      results = list(csv.reader(inputfile))
      for tool in results:
        tooltext = ''.join(tool)
        if tooltext in ''.join(self.tools):
          if tooltext:
            all_tools.append(tooltext)
        #if tool in ''.join(self.tools):
        # all_tools.append(tooltext)
        # print 'success2'


    return all_tools

  # print tools

  def print_tools(self):
    for x in self.tools:
      if x != '':
        print "%s" % x
