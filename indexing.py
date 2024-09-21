#-------------------------------------------------------------------------
# AUTHOR: Alison Fung
# FILENAME: indexing.py
# SPECIFICATION: Calculate the document-term matrix for 3 specific documents
# FOR: CS 4250- Assignment #1
# TIME SPENT: 2 hours
#-----------------------------------------------------------*/

#Importing some Python libraries
import csv
import math

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])

#Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = set(["i", "and", "she", "her", "they", "their"])
for i in range(0, len(documents)):
    # make the string lowercase and split it by words
    split_string = documents[i].lower().split()
    for word in split_string:
        if word in stopWords:
            split_string.remove(word)
    documents[i] = split_string


#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
for i in range(0, len(documents)):
    # replace any word variations with the stem word for each document
    documents[i] = list(map(lambda term: term.replace("cats", "cat").replace("dogs", "dog").replace("loves", "love"), documents[i]))

#Identifying the index terms.
#--> add your Python code here
terms = set()
for document in documents:
    for word in document:
        # add terms if they do not exist already
        if word not in terms:
            terms.add(word)

#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
docTermMatrix = []
# convert terms to list so it can be subscripted
terms = list(terms)
for i in range(0, len(terms)):
    # calculate how many documents have the term, where true = 1
    num_docs_with_term = sum(map(lambda doc: terms[i] in doc, documents))
    # calculate idf
    idf = math.log(len(documents)/num_docs_with_term, 10)
    term_row = []
    for j in range(0, len(document)):
        # calculate tf-idf for the term in a document
        tf = documents[j].count(terms[i])/len(documents[j])
        tf_idf = tf * idf
        term_row.append(tf_idf)
    # add this term's tf-idf to the matrix
    docTermMatrix.append(term_row)


#Printing the document-term matrix.
#--> add your Python code here
for i in range(0, len(docTermMatrix)):
    print("Term:", terms[i])
    for j in range(0, len(docTermMatrix[0])):
        print("Document", j+1, ":", round(docTermMatrix[i][j], 2))
    print("\n")
