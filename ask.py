# ask.py
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

# Given a content string and integer n, generates n questions.
def generateQuestions(content, n):
  for i in range(int(n)):
    print("generated question #" + str(i))

# Main
path_to_article = sys.argv[1]
num_questions = sys.argv[2]

# Pre-process article content.
article_content = read_file(path_to_article)

generateQuestions(article_content, num_questions)