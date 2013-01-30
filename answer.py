# answer.py
# 11-411 NLP Spring 2013, Group 6
# (Stub) Authored by Ryhan Hassan | rhassan@andrew.cmu.edu

import os, sys, errno
import re
import itertools

# Returns string containing content at file path.
def read_file(path):
  content = ""
  inputfile = open(path)
  for line in inputfile: content += str(line)
  inputfile.close()
  return content

def answer(question):
  print("The answer to '" + str(question) + "'' is 42.")


# Main
path_to_article = sys.argv[1]
path_to_questions = sys.argv[2]

# Pre-process article content.
article_content = read_file(path_to_article)

# Open the question file and start answering questions.
question_file = open(path_to_questions)
for question in question_file:
  answer(question.strip())