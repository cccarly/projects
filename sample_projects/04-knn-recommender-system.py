### import packages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler,RobustScaler,OrdinalEncoder,OneHotEncoder
from sklearn.pipeline import Pipeline
#from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from scipy.stats import chi2_contingency
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import TruncatedSVD


### purpose of project 
#### using collaborative filtering method to identify similar users that would 
#### like to use one new service the fintech company provided 
#### variables - adjust to JSON later 

drop_list = ['1','2','3']
column = 'sample_column'
num_list = ['c','d']
catg_list = ['a','b']
nn = 3
number = nn-1
### Import Data & Stratified Sampling
df = 'import data'
df.groupby('Grade', group_keys=False).apply(lambda x: x.sample(frac=0.6))

### data clean 

def data_clean():
    ## fillna w 0 when datatype is number
    for i,col in enumerate(df):
        if df.dtypes[i] != object:
            df[col].fillna(0,inplace=True)
    ##drop unwanted columns:
    df2 = df.drop([f'{column}'],axis = 1)
    ##replace inf to 0 
    df3 = df2.replace([np.inf, -np.inf], 0).reset_index(drop=True) 
    df4 = df3.drop(drop_list,axis = 1)
    ######## drop more variables that are correlated ########
    return df4

### correlation test / EDA

fig, ax = plt.subplots(figsize=(16,10))
sns.heatmap(df.corr(), ax=ax)

############# chi-square test on categorical variables ###############
def chi_test(column):
    contigency= pd.crosstab(df[f'{column}'], df['crypto_user_flag']) 
    c, p, dof, expected = chi2_contingency(contigency) 
    print(column,p)
    return contigency
### model pipeline

def pipeline_input(data):
    catg_pipeline = Pipeline([
           ('categorical',OrdinalEncoder()),
           ('std_scaler',StandardScaler())
            ])
    data_pipeline = ColumnTransformer([
                ('numerical',StandardScaler(),num_list),
                ('catg',catg_pipeline,catg_list)
                 ])
    df_processed = data_pipeline.fit_transform(data)
    return df_processed
### feature engineering
def weight_assign(df_model):
    X = df_model.iloc[:,1:].values
    ### error shows NAN,inf, or value larger than float64.
    ### checked no NAN, no inf, transfer value as type float
    X = np.nan_to_num(X.astype(np.float64))
    scaler = preprocessing.RobustScaler()
    robust_df = scaler.fit_transform(X)
    ##for PCA purpoase - standardize the data to have a mean of 0 and a variance of 1
    robust_df_std = StandardScaler().fit_transform(X)
    ###creat weighted cluster ###
    ### weighted is created on row level #### - find out outstanding cluster
    ### weighted variables - method weight a, 1-a
    X2 = robust_df_std
    X2[:,12:18] = X2[:,12:18]*0.65
    X2[:,0:12] = X2[:,0:12]*0.35
    robust_df_std_weighted = X2
    ### sample weight 
    print(np.any(np.isnan(X)))
    print(np.all(np.isfinite(X)))
    return robust_df, robust_df_std_weighted
### KNN test with KD tree Algo 

def nn_kd_tree(nn,data):
    neigh = NearestNeighbors(n_neighbors=nn,radius = 0.4,algorithm = 'kd_tree',metric = 'euclidean',leaf_size = 40).fit(data)
    distances,indices = neigh.kneighbors(data)
    return distances,indices

distances,indices = nn_kd_tree(nn,df)

### select the nearest 3 neighbors based on real-time available user
df_thd = pd.DataFrame(distances)
threshold = df_thd[number].mean()

def find_neighbors(df_model):
    #put indices into dataframe
    #sample_cluster = pd.DataFrame(indices)
    #create matched market cluster 
    df_model['Recommendation_flag'] = 'NA'
    for x in range(0,len(indices)):
        if df_model.crypto_user_flag.iloc[x] == 1:
            for i in range(1,nn):
                if distances[x][i] <= threshold:
                    df_model['Recommendation_flag'][indices[x][i]] = 1
        else:
            pass
    return

