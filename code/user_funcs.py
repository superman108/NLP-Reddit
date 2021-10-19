# This function recieves a string as an input, and it applies the following transformations:
# 1. It replaces emoji charectars with corresponding word
# 2. It removes hyperlinks from the the text
# 3. It removes any punctuatins from the text
# 4. It tokenizes the document and it shortens the words using lemmatizing and stemming

# Inputs: string, tokenizer,  stemmer, lemmatizer
# output: clean version of document as a string

import emoji
import re
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from wordcloud import WordCloud, STOPWORDS


def CleanText(document, tokenizer=None, p_stemmer = None, lemmatizer=None):
    
    document = document.lower() 
    document=document.replace('\n',' ')
    document=re.sub(r'\b\n\b', ' ', document)
    document= document.replace('u/',' ')
    document=re.sub(r'\bu/\b', ' ', document)
    document= document.replace('__________________________________________________'  ,' ')
    document=re.sub(r'\b__________________________________________________\b', ' ', document)
    document=re.sub(r'\byr\b', 'year', document)
    document=re.sub(r'\byryr\b', 'year', document)
    document=re.sub(r'\bcontributing\b', 'contribution', document)
    document=re.sub(r'\bcontribute\b', 'contribution', document)
    document=re.sub(r'\brefinancing\b', 'refinance', document)
    document=re.sub(r'\brefinanced\b', 'refinance', document)
    document=re.sub(r'\brefinanced\b', 'refinance', document)
    document=re.sub(r'\bfinancial\b', 'finance', document)
    document=re.sub(r'\bfinancially\b', 'finance', document)
    document=re.sub(r'\bscammed\b', 'scam', document)
    document=re.sub(r'\bscamed\b', 'scam', document)
    document=re.sub(r'\bautistic\b', 'autist', document)
    document=re.sub(r'\bautists\b', 'autist', document)
    document=re.sub(r'\bautism\b', 'autist', document)
    document=re.sub(r'\bpaid\b', 'pay', document)
    document=re.sub(r'\bbudgeting\b', 'budget', document)
    document=re.sub(r'\binvesting\b', 'invest', document)
    document=re.sub(r'\binvested\b', 'invest', document)
    document=re.sub(r'\bconsidered\b', 'consider', document)
    document=re.sub(r'\bconsidering\b', 'consider', document)
    document=re.sub(r'\bhouse\b', 'home', document)
    document=re.sub(r'\bsaved\b', 'saving', document)
    document=re.sub(r'\bsave\b', 'saving', document)
    document=re.sub(r'\boffered\b', 'offer', document)
    document=re.sub(r'\bplanning\b', 'plan', document)
    document=re.sub(r'\bplanned\b', 'plan', document)
    document=re.sub(r'\bvest\b', 'vested', document)
    document=re.sub(r'\blost\b', 'lose', document)
    document=re.sub(r'\bloss\b', 'lose', document)
    document=re.sub(r'\bretarded\b', 'retard', document)
    document=re.sub(r'\bability\b', 'able', document)
    document=re.sub(r'\bu\b', 'you', document)
    document=re.sub(r'\bdd\b', 'duediligence', document)
    document=re.sub(r'\byoure\b', ' ', document)
    document=re.sub(r'\bim\b', ' ', document)
    document=re.sub(r'\bthi\b', ' ', document)
    document=re.sub(r'\btha\b', ' ', document)
    document=re.sub(r'\bha\b', ' ', document)
    document=re.sub(r'\bive\b', ' ', document)
    document=re.sub(r'\bthanks\b', ' ', document)
    document=re.sub(r'\bthank\b', ' ', document)
    document=re.sub(r'\bguy\b', ' ', document)
    document=re.sub(r'\bsure\b', ' ', document)
    document=re.sub(r'\bnew\b', ' ', document)
    document=re.sub(r'\blike\b', ' ', document)
    document=re.sub(r'\bwant\b', ' ', document)
    document=re.sub(r'\bknow\b', ' ', document)
    document=re.sub(r'\bmake\b', ' ', document)
    document=re.sub(r'\bneed\b', ' ', document)
    document=re.sub(r'\bcurretnly\b', ' ', document)
    document=re.sub(r'\bget\b', ' ', document)
    document=re.sub(r'\bgot\b', ' ', document)
    document=re.sub(r'\blooking\b', ' ', document)
    document=re.sub(r'\blook\b', ' ', document)
    document=re.sub(r'\bconsider\b', ' ', document)
    document=re.sub(r'\bthrow\b', ' ', document)
    document=re.sub(r'\bthats\b', ' ', document)
    document=re.sub(r'\bquestion\b', ' ', document)
    document=re.sub(r'\bbag\b', ' ', document)
    document=re.sub(r'\bliterally\b', ' ', document)
    document=re.sub(r'\bsubreddit\b', ' ', document)
    document=re.sub(r'\brwallstreetbets\b', ' ', document)
    document=re.sub(r'\brpersonalfinance\b', ' ', document)
    document=re.sub(r'\bwallstreetbets\b', ' ', document)
    document=re.sub(r'\bpersonalfinance\b', ' ', document)

  
    document = emoji.demojize(document, delimiters=(" ", " ")) # replacing emoji with word
    document = re.sub(r"http\S+", "", document) # removing links
    document = re.sub(r'[^\w\s]','',document) # removing punctuations

    document = list(filter(None, '|'.join(re.split('(\d+)',document)).replace(' ','|').split('|')))
    document = ' '.join(map(str, document))
    

    document = tokenizer.tokenize(document.lower())
    if p_stemmer != None:
        document = [p_stemmer.stem(i) for i in document]  
        
    if lemmatizer != None:
        document = [lemmatizer.lemmatize(i) for i in document]          
              
    
    document = ['digit_replaced' if (item.isdigit()) else item for item in document] 
    document = ' '.join(map(str, document))
  
    return document



def hist_plot(figsize, params, row, col, df):

    fig= plt.subplots(figsize=figsize, facecolor='w', edgecolor='k')
    plt.subplots_adjust(hspace = .3, wspace=.3)
    count = 1
    sns.set(rc={'axes.facecolor':'lavender', 'figure.facecolor':'k'})

    for i in range(len(params)):
        ax = plt.subplot(row, col, count)
        sns.histplot(df[ (df[params[i]]>0) & (df[params[i]]<1000) ][params[i]], ax=ax)
        ax.set_xlabel(params[i],fontsize=18)
        ax.set_ylabel('Frequency',fontsize=18)
        plt.xticks(fontsize=16)
        plt.yticks(fontsize=16)
        for pos in ['top', 'bottom', 'right', 'left']:
            ax.spines[pos].set_edgecolor('k')
        count+=1
    return None


def hist_plot_combo(figsize, params, subred, row, col, df):

    fig= plt.subplots(figsize=figsize, facecolor='w', edgecolor='k')
    plt.subplots_adjust(hspace = .3, wspace=.3)
    count = 1
    sns.set(rc={'axes.facecolor':'lavender', 'figure.facecolor':'k'})
    
    for i in range(len(params)):
        ax = plt.subplot(row, col, count)
        df_1 =  df[ (df[params[i]]>0) & (df[params[i]]<1000) ]
        sns.histplot(df_1[(df_1['subreddit']==subred[0])][params[i]], ax=ax)
        sns.histplot(df_1[(df_1['subreddit']==subred[1])][params[i]], ax=ax, color='r')
        ax.set_xlabel(params[i], fontsize=18)
        ax.set_ylabel('Frequency',fontsize=18)
        plt.xticks(fontsize=16)
        plt.yticks(fontsize=16)
        ax.legend(labels=[subred[0],subred[1]], fontsize=16)
        for pos in ['top', 'bottom', 'right', 'left']:
            ax.spines[pos].set_edgecolor('k')
        count+=1
    return None


def hist_plot_sentiment(figsize, params, subred, row, col, df):
    fig= plt.subplots(figsize=figsize, facecolor='w', edgecolor='k')
    plt.subplots_adjust(hspace = .3, wspace=.3)
    count = 1
    sns.set(rc={'axes.facecolor':'lavender', 'figure.facecolor':'k'})
    
    for i in range(len(params)):
        ax = plt.subplot(row, col, count)
        df_1 =  df[ (df[params[i]]>-1.1) & (df[params[i]]<1.1) ]
        sns.histplot(df_1[(df_1['subreddit']==subred[0])][params[i]], ax=ax)
        sns.histplot(df_1[(df_1['subreddit']==subred[1])][params[i]], ax=ax, color='r')
        ax.set_xlabel(params[i], fontsize=18)
        ax.set_ylabel('Frequency',fontsize=18)
        plt.xticks(fontsize=16)
        plt.yticks(fontsize=16)
        ax.legend(labels=['wallstreetbets', 'personalfinance'], fontsize=16)
        for pos in ['top', 'bottom', 'right', 'left']:
            ax.spines[pos].set_edgecolor('k')
        count+=1
    return None




def word_cloud(figsize, subred, row, col, df):

 
    
    
    stopwords = set(STOPWORDS)
    fig= plt.subplots(figsize=figsize, facecolor='w', edgecolor='k')
    plt.subplots_adjust(hspace = .3, wspace=.1)
    count = 1
     
    for i in range(len(subred)):
        key = list(subred.keys())[i]
        val = list(subred.values())[i]
        
        ax = plt.subplot(row, col, count)
        wordcloud = WordCloud(background_color="white", collocations=False, colormap='plasma', max_words=200, stopwords=stopwords, max_font_size=50, min_font_size = 10).generate(' '.join(df[df['subreddit']==val]['combined'].tolist()))

        ax.imshow(wordcloud)
        ax.axis('off')
        ax.set_title('subreddit: %s' %key,  fontdict=dict(size=46))
        for pos in ['top', 'bottom', 'right', 'left']:
            ax.spines[pos].set_edgecolor('k')
        count+=1