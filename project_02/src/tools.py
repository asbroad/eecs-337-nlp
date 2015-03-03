import re
from nltk import *
from nltk.tag import pos_tag
from collections import defaultdict


class tool:
	def __init__ (self, name, description, use):
		self.name = name
		self.description = description
		self.use = use

def getTools():
	list_of_tools = []

	f = open("../data/tools-list.html")
	page = f.read()


	regex = re.compile("<section class=\"alphabetized\">(.*?)</section>", re.DOTALL)
	tools_list = re.findall(regex, page)[0]

	#print tools_list

	regex = re.compile("<li>(.*?)</li>", re.DOTALL)
	#regex = re.compile("<p>(.*?)</p>")
	tools = re.findall(regex, tools_list)
	#tool = re.findall(regex, tools_list)[1]
	
	for item in tools:
		regex = re.compile("<p>(.+?)</p>")
		res = re.findall(regex, item)
	
		#print(res)
	
		regex = re.compile("<strong>(.*?)</strong>")
		name = re.findall(regex, res[0])[0]
		regex = re.compile("(.*?)<.*?>(.*?)</.*?>")
		data = re.findall(regex, res[1])
		if not data:
			use = res[1]
		else:
			use =  "".join(re.findall(regex, res[1])[0])
		
	
		#print(name)
		#print(use)

		t = tool(name, use, 0)
		understandTool(t)
		list_of_tools.append(t)


	return list_of_tools


def understandTool(tool):
	#print("Building understanding of: {}".format(tool.name))

	regex = re.compile("to ([a-zA-Z]+)")
	res = re.findall(regex, tool.description)

	regex = re.compile("([a-zA-Z]+ing)")
	res = res + re.findall(regex, tool.description)

	regex = re.compile("([a-zA-Z]+ly)")
	res = res + re.findall(regex, tool.description)

	res = res + tool.name.lower().split()

	
	

	#tagged_description = pos_tag(tool.description.split())
	#print(tagged_description)
	#keyword_list = [vb.lower() for vb,pos in tagged_description if pos in ["VB", "NNP"]]
	#res = res + keyword_list

	tool.use = res