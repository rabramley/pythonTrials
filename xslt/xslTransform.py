#!/usr/bin/env python

import csv, sys, argparse, lxml.etree as ET

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('inputfile', nargs=1)
  parser.add_argument("-t", "--transformfilename", nargs='?', help="Transform filename", default="transform.xslt")
  parser.add_argument('--textoutput', dest='asText', action='store_true')
  parser.add_argument('--xmloutput', dest='asText', action='store_false')
  parser.set_defaults(asText=True)

  args = parser.parse_args()

  transformXmlToCsv(args.inputfile[0], args.transformfilename, args.asText)

def transformXmlToCsv(inputfile, transfromFile, asText):
  xslt = ET.parse(transfromFile)
  dom = ET.parse(inputfile)
  transform = ET.XSLT(xslt)
  if (asText):
    print(str(transform(dom)))
  else:
    print(ET.tostring(transform(dom), pretty_print=True))

if __name__ == "__main__":
   main()