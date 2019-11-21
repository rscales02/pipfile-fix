#!/usr/bin/env python3

# app to change pipfile from specific dependencies to any dependency after conversion from pip to pipenv

import sys

def file_fixer(file):
  f = open(file, "r")
  fileArray = f.readlines()
  f.close()

  packageStart = fileArray.index('[packages]\n')
  packageStop = fileArray.index('[requires]\n') - 2

  for i in range(packageStart, packageStop):
    i += 1
    line = fileArray[i]
    end = line.index('=') + 1
    line = line[0:end]
    line = line + ' "*"\n'
    fileArray[i] = line

  pipfile = open('Pipfile', 'r+')
  pipfile.truncate(0)
  for line in fileArray:
    pipfile.write(line)
  pipfile.close()

file_fixer(sys.argv[1])