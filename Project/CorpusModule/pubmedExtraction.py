from __future__ import print_function
from Bio import Entrez, Medline
import csv
import time

def update_progress(progress):
    int(progress=progress*100)
    print('\r[{0}] {1}%'.format('#'*(progress/10), progress))

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

            x = 0
            for record in records:
                b = "Writing" + "." * (x%3)
                x += 1
                print(b, end="\r")
                f.write(record.get("AB", "?"))

print("running","program")
