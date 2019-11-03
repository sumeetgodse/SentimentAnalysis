from blog.sentiment import *
from blog.bjptest import *
from blog.congtest import *
from blog.ncptest import *
from blog.aaptest import *
from blog.tmctest import *
from blog.bsptest import *
from blog.cpimtest import *
from blog.plot import *


clf=joblib.load( '/home/sumeet/Desktop/project/svmClassifier.pkl')

def viewsshort(code1,code2):

	if code1==1:
		test1 = pd.read_csv("/home/sumeet/Desktop/DATATEST/BJP/bjpt.csv")
	if code1==2:
		test1 = pd.read_csv("/home/sumeet/Desktop/DATATEST/CONGRESS/congt.csv")
	if code1==3:
		test1 = pd.read_csv("/home/sumeet/Desktop/DATATEST/NCP/ncpt.csv")
	if code1==4:
		test1 = pd.read_csv("/home/sumeet/Desktop/DATATEST/AAP/aapt.csv")
	if code1==5:
		test1 = pd.read_csv("/home/sumeet/Desktop/DATATEST/TMC/tmct.csv")
	if code1==6:
		test1 = pd.read_csv("/home/sumeet/Desktop/DATATEST/BSP/bspt.csv")
	if code1==7:
		test1 = pd.read_csv("/home/sumeet/Desktop/DATATEST/CPIM/cpimt.csv")

	if code2==1:
		test2 = pd.read_csv("/home/sumeet/Desktop/DATATEST/BJP/bjpt.csv")
	if code2==2:
		test2 = pd.read_csv("/home/sumeet/Desktop/DATATEST/CONGRESS/congt.csv")
	if code2==3:
		test2 = pd.read_csv("/home/sumeet/Desktop/DATATEST/NCP/ncpt.csv")
	if code2==4:
		test2 = pd.read_csv("/home/sumeet/Desktop/DATATEST/AAP/aapt.csv")
	if code2==5:
		test2 = pd.read_csv("/home/sumeet/Desktop/DATATEST/TMC/tmct.csv")
	if code2==6:
		test2 = pd.read_csv("/home/sumeet/Desktop/DATATEST/BSP/bspt.csv")
	if code2==7:
		test2 = pd.read_csv("/home/sumeet/Desktop/DATATEST/CPIM/cpimt.csv") 

	test1['pol'] = test1['Text'].apply(sentiment_func)
	test1['sentiment'] = test1['pol'].apply(polarity_func)
	targets_test1 = test1.sentiment.apply(sentiment2target)

	if code1==1:
		X_train, X_test1, y_train, y_test = getTrainingAndTestDataBJP(targets_test1)
	if code1==2:
		X_train, X_test1, y_train, y_test = getTrainingAndTestDataCON(targets_test1)
	if code1==3:
		X_train, X_test1, y_train, y_test = getTrainingAndTestDataNCP(targets_test1)
	if code1==4:
		X_train, X_test1, y_train, y_test = getTrainingAndTestDataAAP(targets_test1)
	if code1==5:
		X_train, X_test1, y_train, y_test = getTrainingAndTestDataTMC(targets_test1)
	if code1==6:
		X_train, X_test1, y_train, y_test = getTrainingAndTestDataBSP(targets_test1)
	if code1==7:
		X_train, X_test1, y_train, y_test = getTrainingAndTestDataCPIM(targets_test1)

	X_test1 = processTweets( X_test1)
	#x=clf.score(X_test,y_test)
	y_pred1 = clf.predict(X_test1)
	test1['Predictions']=y_pred1
	neg_c1=test1.loc[test1.Predictions == -1, 'Predictions'].count()
	pos_c1=test1.loc[test1.Predictions == 1, 'Predictions'].count()
	neu_c1=test1.loc[test1.Predictions == 0, 'Predictions'].count()

	test1['inf_score'] = test1['RetweetCount'] + test1['UserFollowersCount']
	test1['bio'] = test1.UserDescription.str.contains('AAP|BJP|INC|CPI|NCP|BSP|AITC|TMC|Aam Aadmi Party|Bharatiya Janata Party|Indian National Congress|Nationalist Congress Party|Communist Party Of India|Trinamool Congress|Bahujan Samaj Party',case = False ,regex=True)
	test1.loc[(test1.bio == True), 'inf_score'] = test1['inf_score']*0.8

	pis1 = test1['inf_score'][test1['Predictions'] == 1].sum()
	nis1 = test1['inf_score'][test1['Predictions'] == -1].sum()
	#test1.to_csv('mod.csv')


	test2['pol'] = test2['Text'].apply(sentiment_func)
	test2['sentiment'] = test2['pol'].apply(polarity_func)
	targets_test2 = test2.sentiment.apply(sentiment2target)

	if code2==1:
		X_train, X_test2, y_train, y_test = getTrainingAndTestDataBJP(targets_test2)
	if code2==2:
		X_train, X_test2, y_train, y_test = getTrainingAndTestDataCON(targets_test2)
	if code2==3:
		X_train, X_test2, y_train, y_test = getTrainingAndTestDataNCP(targets_test2)
	if code2==4:
		X_train, X_test2, y_train, y_test = getTrainingAndTestDataAAP(targets_test2)
	if code2==5:
		X_train, X_test2, y_train, y_test = getTrainingAndTestDataTMC(targets_test2)
	if code2==6:
		X_train, X_test2, y_train, y_test = getTrainingAndTestDataBSP(targets_test2)
	if code2==7:
		X_train, X_test2, y_train, y_test = getTrainingAndTestDataCPIM(targets_test2)

	X_test2 = processTweets( X_test2)
	#x=clf.score(X_test,y_test)
	y_pred2 = clf.predict(X_test2)
	test2['Predictions']=y_pred2
	neg_c2=test2.loc[test2.Predictions == -1, 'Predictions'].count()
	pos_c2=test2.loc[test2.Predictions == 1, 'Predictions'].count()
	neu_c2=test2.loc[test2.Predictions == 0, 'Predictions'].count()



	test2['inf_score'] = test2['RetweetCount'] + test2['UserFollowersCount']
	test2['bio'] = test2.UserDescription.str.contains('AAP|BJP|INC|CPI|NCP|BSP|AITC|TMC|Aam Aadmi Party|Bharatiya Janata Party|Indian National Congress|Nationalist Congress Party|Communist Party Of India|Trinamool Congress|Bahujan Samaj Party',case = False ,regex=True)
	test2.loc[(test2.bio == True), 'inf_score'] = test2['inf_score']*0.8

	pis2 = test2['inf_score'][test2['Predictions'] == 1].sum()
	nis2 = test2['inf_score'][test2['Predictions'] == -1].sum()

	if (code1==1 and code2==2) or (code1==2 and code2==1):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"Bharatiya Janata Party","Indian National Congress")
	if (code1==1 and code2==3) or (code1==3 and code2==1):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"Bharatiya Janata Party","Nationalist Congress Party")
	if (code1==1 and code2==4) or (code1==4 and code2==1):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"Bharatiya Janata Party","Aam Aadmi Party")
	if (code1==1 and code2==5) or (code1==5 and code2==1):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"Bharatiya Janata Party","All India Trinamool Congress")
	if (code1==1 and code2==6) or (code1==6 and code2==1):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"Bharatiya Janata Party","Bahujan Samaj Party")
	if (code1==1 and code2==7) or (code1==7 and code2==1):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"Bharatiya Janata Party","Communist Party of India (M)")

	if (code1==2 and code2==3) or (code1==3 and code2==2):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"Indian National Congress","Nationalist Congress Party")
	if (code1==2 and code2==4) or (code1==4 and code2==2):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"Indian National Congress","Aam Aadmi Party")
	if (code1==2 and code2==5) or (code1==5 and code2==2):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"Indian National Congress","All India Trinamool Congress")
	if (code1==2 and code2==6) or (code1==6 and code2==2):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"Indian National Congress","Bahujan Samaj Party")
	if (code1==2 and code2==7) or (code1==7 and code2==2):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"Indian National Congress","Communist Party of India (M)")

	if (code1==3 and code2==4) or (code1==4 and code2==3):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"Nationalist Congress Party","Aam Aadmi Party")
	if (code1==3 and code2==5) or (code1==5 and code2==3):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"Nationalist Congress Party","All India Trinamool Congress")
	if (code1==3 and code2==6) or (code1==6 and code2==3):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"Nationalist Congress Party","Bahujan Samaj Party")
	if (code1==3 and code2==7) or (code1==7 and code2==3):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"Nationalist Congress Party","Communist Party of India (M)")

	if (code1==4 and code2==5) or (code1==5 and code2==4):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"Aam Aadmi Party","All India Trinamool Congress")
	if (code1==4 and code2==6) or (code1==6 and code2==4):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"Aam Aadmi Party","Bahujan Samaj Party")
	if (code1==4 and code2==7) or (code1==7 and code2==4):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"Aam Aadmi Party","Communist Party of India (M)")

	if (code1==5 and code2==6) or (code1==6 and code2==5):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"All India Trinamool Congress","Bahujan Samaj Party")
	if (code1==5 and code2==7) or (code1==7 and code2==5):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"All India Trinamool Congress","Communist Party of India (M)")

	if (code1==6 and code2==7) or (code1==7 and code2==6):
		plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,"Bahujan Samaj Party","Communist Party of India (M)")

	return neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2
