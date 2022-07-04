### import package 
### without consider efficiency 

from pyhive import hive
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
####################Package#################################
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
########################################################
from requests_kerberos import HTTPKerberosAuth, OPTIONAL
from pyhive import presto


### cosine distance with consider tfidf vector
def cosine_distance_tfidfvectorizer_method(s1, s2):
    
    # sentences to list
    allsentences = [s1 , s2]
    
    # packages
    from sklearn.feature_extraction.text import TfidfVectorizer
    from scipy.spatial import distance
    
    # text to vector
    # add stop words - do not consider stop words in english
    vectorizer = TfidfVectorizer(use_idf=True)
    all_sentences_to_vector = vectorizer.fit_transform(allsentences)
    text_to_vector_v1 = all_sentences_to_vector.toarray()[0].tolist()
    text_to_vector_v2 = all_sentences_to_vector.toarray()[1].tolist()
    
    # distance of similarity
    cosine = distance.cosine(text_to_vector_v1, text_to_vector_v2)
    #print('Similarity of two sentences are equal to ', round((1-cosine),4))
    cosine_list = round((1-cosine),4)
    return cosine_list

### match score with max score 

def get_score():
    l_max = []
    for j in range(0,len(api_name)):
        score = []
        for i in range(0,len(mrch_name)):
            score.append(cosine_distance_countvectorizer_method(api_name[j],mrch_name[i]))
        ## pre-request: gmr data with name in it
        df_dist[f'{j}'] = score
        ## select max score index to list
        y = df_dist[f'{j}'].idxmax(axis = 0)
        ## get the name of gmr
        x = df_dist['name'][y]
        ## get the max score 
        z = df_dist.loc[y,f'{j}']
        value = [x,y,z]
        l_max.append(value)
        del score
    return l_max

### create final table 

def final_table(max_data):
    ### output 1 -- DF1 - CLEANED NAME
    df_max = pd.DataFrame(l_max, columns =['name', 'index','score']) 
    df_max = pd.concat([df_max,merchant_df[['merchant_nm','latitude','longitude','zip_code']]], axis=1)
    df_max.to_csv('{}.csv'.format(max_data))
    ### output 2 --- DF2 - FUNCTION RESULT
    merged_df = pd.merge(left=df_max, 
                     right=df, how='left', 
                     right_on='name_clean',left_on='name')
    ### CODE MATCHING
    merged_df['zip_match'] = np.where(merged_df['zip_code']== merged_df['mrch_pstl_cd'], True, False)
    return df_max,merged_df
    

### DISTANCE CALCULATION
def haversine_np(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)

    All args must be of equal length.    

    """
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2

    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km

### FINAL 

if name == __main__:
    l_max = get_score()
    df_max,merged_df = final_table('xxx')
    
