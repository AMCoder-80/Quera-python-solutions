import os

def combet(typ1, typ2, path):
	
	files = list()
	sajjad_ext = list()
	salib_ext = list()

	for m in os.walk(path):
		files += [x for x in m[2]]

	sajjad_ext = list(filter(lambda x: x.endswith(typ2), files))
	salib_ext = list(filter(lambda x: x.endswith(typ1), files)) 
	# print(len(sajjad_ext))
	# print(len(salib_ext))
  
	if len(sajjad_ext) > len(salib_ext):
		return 'Win! Normally!'

	# print(files)
 
	names = list(map(lambda a: a[:a.index('.')], files))
	# print(files)
	# print(names)
	for i in names:
		if names.count(i) + 1 >= (len(salib_ext) - len(sajjad_ext)):
			return f"Win! you can win if you cheat on '{i}'!"   
	return "Lose! you can't win this game!"


# print(combet('py', 'txt', '/home/am80/Codes/Quera/TiredFolders/test/1'))
# print(combet('py', 'txt', '/home/am80/Codes/Quera/TiredFolders/test/2'))
# print(combet('py', 'txt', '/home/am80/Codes/Quera/TiredFolders/test/3'))
# print(combet('py', 'txt', '/home/am80/Codes/Quera/TiredFolders/test/4'))
