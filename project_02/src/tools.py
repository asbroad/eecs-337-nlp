import re
from nltk import *
from nltk.tag import pos_tag
from collections import defaultdict
from nltk.stem.porter import *


class tool:
	def __init__ (self, name="", use=[]):
		self.name = name
		self.use = use

	def isUse(self, word):
		return word in self.use


def hc_make_tool_list():
	tools_list = []
	tools_list.append(tool("knife", ["slice", "cut", "chop"]))
	tools_list.append(tool("wooden spoon", ["stir", "mix"]))
	tools_list.append(tool("bowl", ["mix", "stir"]))
	tools_list.append(tool("baking sheet", ["bake", "broil", "chop"]))
	tools_list.append(tool("frying pan", ["fry", "saute", "sear"]))
	tools_list.append(tool("deep frier", ["deep-fry", "deep fry"]))
	tools_list.append(tool("wok", ["stir-fry", "stir fry"]))
	tools_list.append(tool("grill", ["grill", "roast"]))
	tools_list.append(tool("saucepan", ["boil", "simmer", "steam", "blanche"]))

	tools_list.append(tool("baking pan", ["bake", "broil", "chop"]))
	tools_list.append(tool("baking dish", ["bake", "broil", "chop"]))
	tools_list.append(tool("microwave safe bowl", ["microwave"]))
	tools_list.append(tool("microwave", ["microwave"]))
	tools_list.append(tool("saucepan", ["boil", "simmer", "steam", "blanche"]))
	tools_list.append(tool("baster", ["baste", "sauce"]))
	tools_list.append(tool("skillet", ["fry", "melting"]))
	return tools_list





























































#
#def getTools():
#	list_of_tools = []
#
#	f = open("../data/tools-list.html")
#	page = f.read()
#
#	regex = re.compile("<section class=\"alphabetized\">(.*?)</section>", re.DOTALL)
#	tools_list = re.findall(regex, page)[0]
#
#	#print tools_list
#
#	regex = re.compile("<li>(.*?)</li>", re.DOTALL)
#	#regex = re.compile("<p>(.*?)</p>")
#	tools = re.findall(regex, tools_list)
#	#tool = re.findall(regex, tools_list)[1]
#
#	for item in tools:
#		regex = re.compile("<p>(.+?)</p>")
#		res = re.findall(regex, item)
#
#		#print(res)
#
#		regex = re.compile("<strong>(.*?)</strong>")
#		name = re.findall(regex, res[0])[0]
#		regex = re.compile("(.*?)<.*?>(.*?)</.*?>")
#		data = re.findall(regex, res[1])
#		if not data:
#			use = res[1]
#		else:
#			use =  "".join(re.findall(regex, res[1])[0])
#
#
#		#print(name)
#		#print(use)
#
#		t = tool(name, use, 0)
#		understandTool(t)
#		list_of_tools.append(t)
#
#
#	return list_of_tools
#
#
#def understandTool(tool):
#	print("Building understanding of: {}".format(tool.name))
#	stemmer = PorterStemmer()
#
#	regex = re.compile("to ([a-zA-Z]+)")
#	res = re.findall(regex, tool.description)
#
#	regex = re.compile("([a-zA-Z]+ing)")
#	res = res + re.findall(regex, tool.description)
#
#	res = res + tool.name.lower().split()
#
#	tagged_description = pos_tag(tool.description.split())
#	#print(tagged_description)
#	keyword_list = [vb.lower() for vb,pos in tagged_description if pos in ["VB", "RB", "VBG"]]
#	res = res + keyword_list
#	res_stemmed = []
#	for word in res:
#		res_stemmed.append(stemmer.stem(word).encode("utf8"))
#
#	res_stemmed = list(set(res_stemmed))
#	tool.use = res_stemmed
#
