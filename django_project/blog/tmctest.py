import sklearn.metrics
from sklearn.model_selection import train_test_split
import csv

def getTrainingAndTestDataTMC(targets_test):
	    X = []
	    y = []
	    X1 = []
	    y1 = []
	    f=open(r'/home/sumeet/Desktop/DATATEST/TMC/tmct.csv','r', encoding='ISO-8859-1')
	    reader = csv.reader(f)
	    for row in reader:
	        X1.append(row[1])
	    
	    for row1 in targets_test:
	        y1.append(row1)
	    X1.pop(0)

	    X_trainR, X_test, y_trainR, y_test = sklearn.model_selection.train_test_split(X1,y1,test_size=1.0, random_state=0, shuffle = False)
	    return X_trainR, X_test, y_trainR,y_test
