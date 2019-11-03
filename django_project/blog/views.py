from django.shortcuts import render
from django.http import HttpResponse
from matplotlib import pyplot as plt
from blog.sentiment import *
from blog.viewsshort import *


import csv
import os
import re
import nltk
import scipy
import sklearn.metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

#clf=joblib.load( '/home/sumeet/Desktop/project/svmClassifier.pkl')



def front(request):
	return render(request,'blog/front.html')

def home(request):
	return render(request,'blog/home.html')

def algo(request):
	return render(request,'blog/algo.html')

def bjp_inc(request):

	'''
	...test1 = pd.read_csv("/home/sumeet/Desktop/DATATEST/BJP/bjpt.csv") 
	test1['pol'] = test1['Text'].apply(sentiment_func)
	test1['sentiment'] = test1['pol'].apply(polarity_func)
	targets_test1 = test1.sentiment.apply(sentiment2target)
	X_train, X_test1, y_train, y_test = getTrainingAndTestDataBJP(targets_test1)
	X_test1 = processTweets( X_test1)
	#x=clf.score(X_test,y_test)
	y_pred1 = clf.predict(X_test1)
	test1['Predictions']=y_pred1
	neg_c1=test1.loc[test1.Predictions == -1, 'Predictions'].count()
	pos_c1=test1.loc[test1.Predictions == 1, 'Predictions'].count()
	neu_c1=test1.loc[test1.Predictions == 0, 'Predictions'].count()
	
	test2 = pd.read_csv("/home/sumeet/Desktop/DATATEST/CONGRESS/congt.csv") 
	test2['pol'] = test2['Text'].apply(sentiment_func)
	test2['sentiment'] = test2['pol'].apply(polarity_func)
	targets_test2 = test2.sentiment.apply(sentiment2target)
	X_train, X_test2, y_train, y_test = getTrainingAndTestDataCON(targets_test2)
	X_test2 = processTweets( X_test2)
	#x=clf.score(X_test,y_test)
	y_pred2 = clf.predict(X_test2)
	test2['Predictions']=y_pred2
	neg_c2=test2.loc[test2.Predictions == -1, 'Predictions'].count()
	pos_c2=test2.loc[test2.Predictions == 1, 'Predictions'].count()
	neu_c2=test2.loc[test2.Predictions == 0, 'Predictions'].count()

	plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,"Bharatiya Janata Party","Indian National Congress")...
	'''
	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(1,2)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def bjp_ncp(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(1,3)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def bjp_aap(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(1,4)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def bjp_tmc(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(1,5)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def bjp_bsp(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(1,6)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def bjp_cpim(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(1,7)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def inc_ncp(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(2,3)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def inc_aap(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(2,4)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def inc_tmc(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(2,5)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def inc_bsp(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(2,6)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def inc_cpim(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(2,7)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def ncp_aap(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(3,4)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def ncp_tmc(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(3,5)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def ncp_bsp(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(3,6)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def ncp_cpim(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(3,7)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)


def aap_tmc(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(4,5)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def aap_bsp(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(4,6)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def aap_cpim(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(4,7)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def tmc_bsp(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(5,6)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def tmc_cpim(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(5,7)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def bsp_cpim(request):

	neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2=viewsshort(6,7)

	posts=[{'pos':pos_c1,'neg':neg_c1,'neu':neu_c1,'pis':pis1,'nis':nis1},{'pos':pos_c2,'neg':neg_c2,'neu':neu_c2,'pis':pis2,'nis':nis2}]
	context={'posts':posts}
	return render(request,'blog/res.html',context)

def live(request):
	return render(request,'blog/live.html')

def liveres(request):
	input=request.POST['input']
	posts=[{'inp1':input}]
	context={'posts':posts}
	return render(request,'blog/liveres.html',context)
