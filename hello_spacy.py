##
## python -m spacy download en_core_web_lg
##
## Create venv: python -m venv venv { or any other way you like to make virtual Env }
## ps don't get used to brackets 
##
## activate venv (windows: venv\Scripts\activete; bash/Mac  source venv/bin/activate)
##
## Install: pip install spacy
##
## download the model https://spacy.io/models/en
##
## I have always used _sm I should try this larger maodel using _lg here
## python -m spacy download en_core_web_lg 
##

## from the docs https://spacy.io/usage/rule-based-matching

import spacy
nlp = spacy.load('en_core_web_lg')

text = '''
Kayleigh McEnany
@PressSec
·
7h
FACT CHECK: President 
@realDonaldTrump
 DID NOT dismantle the pandemic response office.

The NSC’s Counter-proliferation and Biodefense Directorate exists today!
'''

doc = nlp(text)

## python list comprehension
## if not used to python is equivalent to 
## for ent in doc.ents:
##     print (ent.text, print ent.label_)

print([(ent.text, ent.label_) for ent in doc.ents])




