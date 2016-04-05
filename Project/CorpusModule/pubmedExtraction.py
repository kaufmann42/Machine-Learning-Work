from __future__ import print_function
from __future__ import division
from Bio import Entrez, Medline
import csv
import sys
from textblob import TextBlob

def update_progress(prog_bar):
    prog_bar = int(prog_bar*100)
    sys.stdout.write('\r[{0}{1}] {2}%'.format('|'*int(prog_bar), ' '*int(100-prog_bar), (prog_bar+1)))
    sys.stdout.flush()

def getAbstracts(input_filename):
    print("getting terms from: ",input_filename,"...")
    terms = []
    with open(input_filename, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            terms.append(row[0])
            print("Adding term: " + str(row[0]))

    return terms

def printAbstracts(terms, output_filename):
    print("collecting abstracts and printing to ",output_filename,"...")
    num_terms = len(terms)
    with open(output_filename, 'w') as f:
        for term in terms:
            # print("Getting term: ",str(term)) # debugging
            update_progress(terms.index(term)/num_terms)
            Entrez.email = "kaufmann42@ufl.edu"     # Always tell NCBI who you are

            handle = Entrez.esearch(db="pubmed", term=term, retmax=463)
            record = Entrez.read(handle)
            idlist = record["IdList"]

            handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline",
                                       retmode="text")
            records = Medline.parse(handle)

            for record in records:
                f.write(record.get("AB", "?"))
                f.write("\n")

def getSentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def printSentiments(terms, output_filename):
    print("collecting abstracts and printing sentiments to ",output_filename,"...")
    num_terms = int(len(terms))
    with open(output_filename, 'w') as f:
        for term in terms:
            # print("Getting term: ",str(term)) # debugging
            update_progress(float(int(terms.index(term))/num_terms))
            Entrez.email = "kaufmann42@ufl.edu"     # Always tell NCBI who you are

            handle = Entrez.esearch(db="pubmed", term=term, retmax=463)
            record = Entrez.read(handle)
            idlist = record["IdList"]

            handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline",
                                       retmode="text")
            records = Medline.parse(handle)
            f.write(term)
            for record in records:
                f.write(", ")
                f.write(str(getSentiment(record.get("AB", "?"))))
            f.write("\n")

def printAverageSentiments(terms, output_filename):
    print("collecting abstracts and printing sentiments to ",output_filename,"...")
    num_terms = int(len(terms))
    with open(output_filename, 'w') as f:
        for term in terms:
            # print("Getting term: ",str(term)) # debugging
            update_progress(float(int(terms.index(term))/num_terms))
            Entrez.email = "kaufmann42@ufl.edu"     # Always tell NCBI who you are

            handle = Entrez.esearch(db="pubmed", term=term, retmax=463)
            record = Entrez.read(handle)
            idlist = record["IdList"]

            handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline",
                                       retmode="text")
            records = Medline.parse(handle)

            total = 0
            sum_sentiments = 0.0
            f.write(term + ", ")
            for record in records:
                total += 1
                sum_sentiments += float(getSentiment(record.get("AB", "?")))

            sentiment = float(sum_sentiments/total)
            # print("The sentiment is: ", sentiment)
            f.write(str(sentiment))
            f.write("\n")

print("running","program")
terms = getAbstracts('data.csv')
printAbstracts(terms, 'word2vecdata.txt')
