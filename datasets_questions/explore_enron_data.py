#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
import pdb
import locale

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#mark = enron_data.keys()[0]


poi_count = 0
for key, person in enron_data.iteritems():
    if person["poi"] == 1:
        poi_count +=1

print "POI_COUNT:%i" % poi_count

#What is the total value of the stock belonging to James Prentice?
james = "Prentice James".upper()
total_stock = enron_data[james]['total_stock_value']

print james + " total stock: " + str(total_stock)

#How many email messages do we have from Wesley Colwell to persons of interest?
colwell = "Colwell Wesley".upper()
#print enron_data[colwell].keys()
print colwell + " from messages: " + str(enron_data[colwell]["from_this_person_to_poi"])

#What's the value of stock options exercised by Jeffrey K Skilling?
jeff = "Skilling Jeffrey K".upper()
#print enron_data[jeff].keys()
print jeff + "exercised_stock_options: " + str(enron_data[jeff]["exercised_stock_options"])

#Of these three individuals (Lay, Skilling and Fastow), who took home the most money
ken = "Lay Kenneth L".upper()
andrew = "FASTOW ANDREW S"

#for key in enron_data.keys():
    #if "FASTOW" in key:
        #print key

maximum = 0
for guy in [jeff, ken, andrew]:
    guy_total = enron_data[guy]["total_payments"]
    if guy_total > maximum:
        maximum = guy_total
        max_guy = guy

print max_guy + " took home the most money: " + str(maximum)

# How is unfiled featured denoted
#for key, person in enron_data.iteritems():
    #for key, label in person.iteritems():
        #print label

# How many people hava a qualified sallary

salaried_count = 0
for key, person in enron_data.iteritems():
    if person["salary"] != "NaN":
        salaried_count += 1

print "Number of people with Salary: " + str(salaried_count)

# How many people have a qualified email address
count = 0
for key, person in enron_data.iteritems():
    if person["email_address"] != "NaN":
        count += 1

print "Number of people with email_address: " + str(count)

print enron_data[key].keys()

# what percentage of people in the data set have NaN in their total payments
total_count = len(enron_data.keys())

total_payments_count = 0
for key, person in enron_data.iteritems():
    if person["total_payments"] != "NaN":
        total_payments_count += 1


percent_no_total_payments = float(total_count - total_payments_count)/total_count * 100

print "percent of people without total payments: " + str(percent_no_total_payments)

# what percentage of poi in the data set have NaN in their total payments
total_count = len(enron_data.keys())

count = 0
for key, person in enron_data.iteritems():
    if person["total_payments"] == "NaN" and person["poi"] == 1:
        count += 1

percent = float(count)/poi_count * 100

print "Percent of poi without total payments: " + str(percent)

# If you added 10 more people all poi, with NaN what would new counts be
new_total = total_count+10

print "New Total: " +  str(new_total)
print "New Total NaN total payments: " + str(new_total - total_payments_count)

new_poi_count = poi_count + 10
print "New Total POI: " +  str(new_poi_count)

