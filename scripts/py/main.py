
# UNDERLINE / HIGHLIGHT
# s = "Every other character in this sentence is underlined with the <u> tag and every other word is highlighted with the <mark> tag for no good reason whatsoever."
# outputS = ""

# for idx,char in enumerate(s):
# 	if idx % 2 == 0:
# 		outputS += "<u>" + char + "</u>"
# 	else:
# 		outputS += char

# print (' '.join(["<mark>" + word + "</mark>" if idx % 2 == 0 else word for idx, word in enumerate(outputS.split(' '))]))


# GENERATIVE LOREM IPSUM
# import random

# def decision(probability):
#     return random.random() < probability

# def getCharStyle(char):
# 	face = ""
# 	size = ""
# 	color = ""
# 	underline = False
# 	emphasis = False
# 	superscript = False
# 	subscript = False
# 	highlight = False
# 	font_styles = ['Georgia', 'Arial', 'Times New Roman', 
# 	'Palatino', 'Garamond', 'Bookman', 'Avant Garde', 
# 	'Verdana', 'Comic Sans MS', 'Trebuchet MS', 
# 	'Arial Black', 'Impact', 'Courier New', 'Helvetica']
# 	# get color
# 	if decision(1.0):
# 		r = lambda: random.randint(0,255)
# 		color = str('#%02X%02X%02X' % (r(),r(),r()))
# 	if decision(1.0):
# 		size = str(random.randint(1, 7))
# 	if decision(1.0):
# 		face = str(random.choice(font_styles))
# 	s = "<font face=\"" + face + "\" size=\"" + size + 
# 	"\" color=\"" + color + "\">" + char + "</font>"
# 	return s


# s = # omitted lorem ipsum string to save space
# outputS = ""
# for idx, char in enumerate(s):
# 	outputS += getCharStyle(char)

# print (outputS)



# HTML TABLE ART
# see also http://www.decalage.info/en/python/html for more details

# table_data = [
#         ['Last name',   'First name',   'Age'],
#         ['Smith',       'John',         30],
#         ['Carpenter',   'Jack',         47],
#         ['Johnson',     'Paul',         62],
#     ]

# table_data = [
#     [' ','' ,'' ,' ',   '','', ' ',' ',' ',' ',' '  , '','',       '',' ', '',' ', '','', '','',  ' ','', '','',     '','', ' ','', ''],
#     [' ','' ,'' ,' ',   '','',   '','',' ','',''    , '','',       ' ','', ' ','', ' ','', '','',  ' ','', '','',    '','', ' ','', ''],
#     [' ','' ,'' ,' ',   '','',   '','',' ','',''    , '','',       ' ','', ' ','', ' ','', '','', ' ','', '','',     '','', ' ','', ''],
#     [' ','' ,'' ,' ',   '','',   '','',' ','',''    , '','',       ' ','', ' ','', ' ','', '','', ' ','', '','',     '','', ' ','', ''],
#     [' ','' ,'' ,' ',   '','',   '','',' ','',''    , '','',       ' ','', ' ','', ' ','', '','', ' ','', '','',     '','', ' ','', ''],
#     [' ',' ',' ',' ',   '','',   '','',' ','',''    , '','',       ' ','', ' ','', ' ','', '','', ' ','', '','',     '','', ' ','', ''],
#     [' ','' ,'' ,' ',   '','',   '','',' ','',''    , '','',       ' ','', ' ','', ' ','', '','', ' ','', '','',     '','', ' ','', ''],
#     [' ','' ,'' ,' ',   '','',   '','',' ','',''    , '','',       ' ','', ' ','', ' ','', '','', ' ','', '','',     '','', ' ','', ''],
#     [' ','' ,'' ,' ',   '','',   '','',' ','',''    , '','',       ' ','', ' ','', ' ','', '','', ' ','', '','',     '','', ' ','', ''],
#     [' ','' ,'' ,' ',   '','',   '','',' ','',''    , '','',       ' ','', ' ','', ' ','', '','', ' ','', '','',     '','', '','', ''],
#     [' ','' ,'' ,' ',   '','',   '','',' ','',''    , '','',       ' ','', ' ','', ' ','', '','', ' ',' ', ' ',' ',  '','', ' ','', ''],

# ]
# import random

# new_table_data = []
# for idx, row in enumerate(table_data):
#     new_table_data.append([])
#     for idy, column in enumerate(row):
#         if column == " ":
#             r = lambda: random.randint(0,255)
#             # print '#%02X%02X%02X' % (r(),r(),r())
#             color = str('#%02X%02X%02X' % (r(),r(),r()))
#             new_table_data[idx].append(color) # random color
#         else:
#             new_table_data[idx].append("ffffff") # white
# t = HTML.Table()
# for row in new_table_data:
#     colored_cells = []
#     for cell in row:
#         colored_cells.append( HTML.TableCell(' ', bgcolor=cell) )
#     t.rows.append(colored_cells)
# htmlcode = str(t)
# print htmlcode
