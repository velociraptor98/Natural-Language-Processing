import nltk
#only for bigrams
sentence='Before we plunge headfirst into a pile of patterns, I thought it might help to give you some context about how I think about software architecture and how it applies to games. It may help you understand the rest of this book better. If nothing else, when you get dragged into an argument about how terrible (or awesome) design patterns and software architecture are, it will give you some ammo to use.'
sentence=sentence.lower()
tokens=nltk.word_tokenize(sentence)
bi=list(nltk.bigrams(tokens))
for i in bi:
    countprev=sentence.count(i[0])
    countnext=0
    for j in range(len(tokens)):
        if(tokens[j]==i[1] and tokens[j-1]== i[0]):
            countnext+=1
    prob=countnext/countprev
    print('p(',i[1],'|',i[0],"): ",prob)