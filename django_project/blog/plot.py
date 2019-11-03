import numpy as np
import matplotlib.pyplot as plt

def plot(neu_c1,neg_c1,pos_c1,neu_c2,neg_c2,pos_c2,pis1,nis1,pis2,nis2,title1,title2):
	plt.figure()	
	C1 = [neu_c1,neg_c1,pos_c1]
	S1 = ['Neutral', 'Negative','Positive']
	colors1 = ['#cfd8dc', '#ef6c00','#c6ff00']
	plt.pie(C1, labels=S1, colors=colors1, startangle=90,autopct='%.1f%%')
	plt.title(title1)
	plt.savefig('/home/sumeet/django_project/blog/static/blog/test1.png')

	plt.figure()
	C2 = [neu_c2,neg_c2,pos_c2]
	S2 = ['Neutral', 'Negative','Positive']
	colors2 = ['#cfd8dc', '#ef6c00','#c6ff00']
	plt.pie(C2, labels=S2,colors=colors2, startangle=90,autopct='%.1f%%')
	plt.title(title2)
	plt.savefig('/home/sumeet/django_project/blog/static/blog/test2.png')

	plt.figure()
	N = 2
	pos = (pos_c1,pos_c2)
	fig, ax = plt.subplots()
	ind = np.arange(N)    # the x locations for the groups
	width = 0.35         # the width of the bars
	p1 = ax.bar(ind, pos, width, color='y')
	neg = (neg_c1,neg_c2)
	p2 = ax.bar(ind + width, neg, width,color='r')
	ax.set_title('Positive/Negative tweets per party')
	ax.set_xticks(ind + width / 2)
	ax.set_xticklabels((title1, title2))
	ax.legend((p1[0], p2[0]), ('Positive','Negative'))
	ax.autoscale_view()
	plt.xlabel('Name of selected parties')
	plt.ylabel('Number of tweets')
	plt.savefig('/home/sumeet/django_project/blog/static/blog/bar.png')

	plt.figure()	
	C1 = [pis1,nis1]
	S1 = ['+InfluencerScore','-InfluencerScore']
	colors1 = ['#c6ff00','#ef6c00']
	plt.pie(C1, labels=S1, colors=colors1, startangle=90,autopct='%.1f%%')
	plt.title(title1)
	plt.savefig('/home/sumeet/django_project/blog/static/blog/mod1.png')

	plt.figure()
	C2 = [pis2,nis2]
	S2 = ['+InfluencerScore','-InfluencerScore']
	colors2 = ['#c6ff00','#ef6c00']
	plt.pie(C2, labels=S2,colors=colors2, startangle=90,autopct='%.1f%%')
	plt.title(title2)
	plt.savefig('/home/sumeet/django_project/blog/static/blog/mod2.png')