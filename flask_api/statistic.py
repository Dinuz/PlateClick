import numpy as np
import pickle
from os import listdir
from scipy.stats import sem
from scipy.stats import ttest_rel
from scipy.stats import pearsonr
from scipy.stats import shapiro
from scipy.stats import wilcoxon

pc = list() # PlateClick accept rate
rd = list() # Random accept rate

print "Number of participants: " + str(len(listdir("../user/")))

for user_f in listdir("../user/"):
	with open("../user/" + user_f, "r") as f_handle:
		user = pickle.load(f_handle)
		positive_samples_set = set(user.test_images_positive)
		positive_noway = 0

        	for n_i in user.test_images_selection["noway"]:
                	if user.test_images_list[int(n_i[11:]) - 1] in positive_samples_set:
                		positive_noway += 1
		pc.append(float(10 - positive_noway) / 10)
		rd.append(float(10 - (len(user.test_images_selection["noway"]) - positive_noway)) / 10)

print "PlateClick Mean: " + str(np.mean(pc))
print "PlateClick SEM: " + str(sem(np.array(pc)))
print "PlateClick list: " + str(pc)
print "Random Mean: " + str(np.mean(rd))
print "Random SEM: " + str(sem(np.array(rd)))
print "Random list: " + str(rd)
print "SW Test P: " + str(shapiro(pc+rd)[1])
t_s, p_v = wilcoxon(pc, rd)
print "P value: " + str(p_v)
# print "Effect size: " + str(t_s * (( 2 * (1 - pearsonr(pc, rd)[0]) / len(pc) ) ** (0.5)))
