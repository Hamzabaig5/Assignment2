import newspaper


dawn_paper = newspaper.build('https://www.dawn.com/')
bbc_paper = newspaper.build('https://www.bbc.com/')

for article in dawn_paper.articles:
   with open('article.txt', 'a') as file:
         file.write(article.url + '\n')

for article in bbc_paper.articles:
   with open('article.txt', 'a') as file:
         file.write(article.url + '\n')         
         

print ('----------------------------------------------Done----------------------------------------------')