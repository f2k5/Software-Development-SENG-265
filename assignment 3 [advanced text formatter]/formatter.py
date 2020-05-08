#!/opt/local/bin/python

import re
import sys
import fileinput
import calendar

class Formatter:


	def __init__(self, filename=None, inputlines=None):
		self.filename = filename
		self.inputlines = inputlines

		#file_info = Formatter(sys.argv[1], None)

	def get_lines(self):
		margin = 0
		maxwidth = 0
		line_len = 0
		word = 0
		blank_line = 0
		words_lenghts = 0
		line1 = []
		line2 = []
		copy = []
		line_list = []
		word_to_replace = []
		replaced_word = []
		date_format = 0
		replace_list = []

		#The function that takes in a list 
		#does the what maxwidth is supposed to do:
		#>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<

		#This function only needs the list 
		#and words_length to work:
		def make_tidy():
			#print("function")
			copy2 = copy[:]
			#print(copy2)
			#print(line_len)
			#print(words_lenghts)
			padding_num = maxwidth - words_lenghts - margin
			padding_positions = len(copy2) - 1
			between_spaces = 0

			#Case 1: if no padding is required, that is all words in the list
			#        require just 1 regular space between 'em:
			if padding_positions == padding_num:
				no_padding_needed = " ".join(copy2)
				if len(no_padding_needed) == maxwidth - margin:
					#print("From no padding needed:")
					margin_spaces = " "*margin
					no_padding_needed = margin_spaces + no_padding_needed
					print(no_padding_needed)
				#print(len(no_padding_needed))
				#print("\n")

			#Case 2: if the list has only 2 words:
			if padding_positions == 1: 
				#print(padding_num)
				two_word_sentence = "{}{}{}".format(copy2[0], " "*padding_num, copy2[1])
				if len(two_word_sentence) == maxwidth - margin:
					#print("List has 2 words:")
					margin_spaces = " "*margin
					two_word_sentence = margin_spaces + two_word_sentence
					print(two_word_sentence)
				#print(len(two_word_sentence))
				#print("\n")

			#Case 3: if the list has only 1 word:
			if padding_positions == 0:
				one_word_sentence = "{}{}".format(copy2[0], " "*padding_num)
				if len(one_word_sentence) == maxwidth - margin:
					#print("List has only one word:")
					margin_spaces = " "*margin
					one_word_sentence = margin_spaces + one_word_sentence
					print(one_word_sentence)
				#print(len(one_word_sentence))

			#Case 4: if the list has more than 2 words
			if padding_positions > 1:

				#Case 4a: if equal num of padding is needed between each space:
				if padding_num % padding_positions == 0 and padding_positions != padding_num:
					between_spaces = padding_num / padding_positions
					b = int(between_spaces)
					equal_spaces_between_words = (" "*b).join(copy2)	
					if len(equal_spaces_between_words) == maxwidth - margin:
						#print("Multiple spaces evenly distributed:")
						margin_spaces = " "*margin
						equal_spaces_between_words = margin_spaces + equal_spaces_between_words
						print(equal_spaces_between_words)
					#print(len(equal_spaces_between_words))

				#Case 4b: in case of uneven padding:
				elif padding_num % padding_positions != 0:
					#pass
					space_added = 0
					space_inc = 2
					while space_added != padding_num:

						#print("BUG")
						index = 1
						#print("yeah")
					
						#space_inc = 2
						v = padding_positions
						temp = padding_positions
						#print(padding_positions)
						#print(temp)
						while temp != 0 and space_added != padding_num and len(copy2)+1 !=  maxwidth:
							
							copy2.insert(index, " ")
							index += space_inc
							temp -= 1
							space_added += 1

						space_inc += 1	

					uneven_padding_sentence = "".join(copy2)
					if len(uneven_padding_sentence) == maxwidth - margin:
					#print("uneven:")
						margin_spaces = " "*margin
						uneven_padding_sentence = margin_spaces + uneven_padding_sentence
						print(uneven_padding_sentence)

					# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

		#READING a file line by line:
		for line in fileinput.input():
			#def executing_each_line(self):
			#searching for the command "?mrgn":
			if line.startswith("?mrgn"):
				listed = line.split() 

				#checker now has the margin number:
				checker = listed[1]

				#checks the margin number type, whether of form: Y/+Y/-Y:

				#if the number is SIMPLY a whole number like 20:
				if checker[0] != "+" and checker[0] != "-":
					margin = int(checker)

				#if the number is positive like +20:
				if checker[0] == "+":
					add_margin = int(checker)
					margin += add_margin

				#if the number is negative like -20:
				if checker[0] == "-":
					sub_margin = int(checker)
					margin += sub_margin

				#if the value of margin ever becomes -ve, reset it to zero:
				if margin < 0:
					margin = 0

			#searching for the command ?maxwidth:
			elif line.startswith("?maxwidth"):
				listed = line.split()
				maxwidth = int(listed[1])

			#searching for the command ?replace:
			elif line.startswith("?replace"):
				replace_list = line.split()
				word_to_replace.append(replace_list[1])
				replaced_word.append(replace_list[2])

			#searching for the command ?monthabbr:
			elif line.startswith("?monthabbr"):
				date_format += 1

			#if line is an empty/ blank line:
			elif line.startswith("\n"):
				#print("\n", end = "")
				blank_line = 1
				if len(line_list) != 0:
					#print(line_list)
					copy = line1[:]
					make_tidy()
					words_lenghts = 0
					word = 0
					line_len = 0
					line1 = []
					print("\n", end = "")
					blank_line = 0
				else:
					print("\n", end = "")



			else:
				if maxwidth == 0:
					spaces = " " * margin
					output = spaces + line
					print(output, end = "")

				else:
					#>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<

					#if ?replace command is found, then replace the 
					#pattern to be replaced
					if len(replace_list) != 0:
						if bool(re.search(word_to_replace[0], line)) == True:
							line = re.sub(word_to_replace[0], replaced_word[0], line)

					#if ?monthabbr command is found, change dates of the 
					#format mm-dd-yyyy, mm/dd/yyyy and mm.dd.yyyy to "MMM. dd, yyyy" (OCT. 25, 1996)
					if date_format != 0:
						#if date is of the form: mm/dd/yyyy:
						if bool(re.search(r'\d\d/\d\d/\d\d\d\d', line)) == True:
							d = re.search(r'\d\d/\d\d/\d\d\d\d', line)
							d = d.span()
							x = d[0]

							#Getting the month value and converting it
							#int, to use it with calendar.month_abbr[]:
							month_num = int(line[x] + line[x+1])
							month_string = calendar.month_abbr[month_num]
							date_num = line[x+3] + line[x+4] #type char
							year_num = line[x+6] + line[x+7] + line[x+8] + line[x+9] #type char
							new_date_format = month_string + "." + " " + date_num + "," + " " + year_num

							line = re.sub(r'\d\d/\d\d/\d\d\d\d', new_date_format, line)
							
							

						elif bool(re.search(r'\d\d-\d\d-\d\d\d\d', line)) == True:
							d = re.search(r'\d\d-\d\d-\d\d\d\d', line)
							d = d.span()
							x = d[0]

							#Getting the month value and converting it
							#int, to use it with calendar.month_abbr[]:
							month_num = int(line[x] + line[x+1])
							month_string = calendar.month_abbr[month_num]
							date_num = line[x+3] + line[x+4] #type char
							year_num = line[x+6] + line[x+7] + line[x+8] + line[x+9] #type char
							new_date_format = month_string + "." + " " + date_num + "," + " " + year_num

							line = re.sub(r'\d\d-\d\d-\d\d\d\d', new_date_format, line)

						elif bool(re.search(r'\d\d\.\d\d\.\d\d\d\d', line)) == True:
							d = re.search(r'\d\d\.\d\d\.\d\d\d\d', line)
							d = d.span()
							x = d[0]

							#Getting the month value and converting it
							#int, to use it with calendar.month_abbr[]:
							month_num = int(line[x] + line[x+1])
							month_string = calendar.month_abbr[month_num]
							date_num = line[x+3] + line[x+4] #type char
							year_num = line[x+6] + line[x+7] + line[x+8] + line[x+9] #type char
							new_date_format = month_string + "." + " " + date_num + "," + " " + year_num

							line = re.sub(r'\d\d\.\d\d\.\d\d\d\d', new_date_format, line)







					line_list = line.split()
					#print(line_list)
					i = 0
					for w in line_list:

						word = len(line_list[i])
						line_len += word
						words_lenghts += word

						#State: 1:
						if line_len < maxwidth - margin:

							line_len += 1
							line1.append(line_list[i])
							#print(line1)


						#State: 2:
						elif line_len == maxwidth - margin:
							#print("line_len ==")
							#print(line_len)

							line1.append(line_list[i])
							copy = line1[:]
							#print(copy)
							make_tidy()

							#RESET VALUES:
							words_lenghts = 0
							line_len = 0
							word = 0
							line1 = []
							#copy = []

						#State: 3:
						elif line_len > maxwidth - margin:
							#print("line_len >")
							#print(line_len)

							words_lenghts -= word

							#No need to append here, append was already done
							#in Case 1:
							copy = line1[:]
							#print(copy)
							make_tidy()

							#RESET VALUES:
							words_lenghts = word
							line_len = word + 1
							#copy = []
							line1 = []
							line1.append(line_list[i])

						i += 1

		if len(line_list) != 0:
			#print(line_list)
			copy = line1[:]
			make_tidy()
			words_lenghts = 0
			word = 0
			line_len = 0
			line1 = []					