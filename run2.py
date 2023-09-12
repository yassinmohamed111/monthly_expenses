import pandas as pd



expenses = pd.read_csv("expenses.csv")
stats = pd.read_csv("daysExpenses.csv")

def save():
    stats.to_csv('daysExpenses.csv' , index=False)

from datetime import datetime


'''
# Convert the 'Date' column to datetime format
expenses['Date'] = pd.to_datetime(expenses['Date'])

# Extract the month from the 'Date' column
stats['months'] = expenses['Date'].dt.strftime('%Y-%m')
stats.to_csv("stats.csv" , index=False)
# Convert the 'months' column to datetime format
stats['months'] = pd.to_datetime(stats['months'])

# Format the datetime objects to display the written month names
stats['months'] = stats['months'].dt.strftime('%B %Y')
stats["months"].drop_duplicates(inplace=True)


stats.drop_duplicates(inplace=True)
stats.to_csv("stats.csv" , index=False)


  months
  March 2022
  February 2022
  December 2021
  November 2021

  stats["days"].drop_duplicates(inplace=True)
stats.drop_duplicates(inplace=True)
stats.to_csv("stats.csv" , index=False)
'''


def totalexpenses(date) :
    total = expenses[(expenses["Date"] == date) & (expenses['Income/Expense'] == "Expense")]
    finaltot = total["Amount"].sum()

    #print(f"total payed in {date} = " , finaltot)
    return finaltot


def get_expenses() :
    listt = []

    link_list = []
    for i , row in stats.iterrows() :
        total = totalexpenses(row["days"])
        listt.append(total)
    return listt

def totalincome(date) :
    total = expenses[(expenses["Date"] == date) & (expenses['Income/Expense'] == "Income")]
    finaltot = total["Amount"].sum()

    #print(f"total payed in {date} = " , finaltot)
    return finaltot


def get_income() :
    listt = []

    link_list = []
    for i , row in stats.iterrows() :
        total = totalincome(row["days"])
        listt.append(total)
    return listt

months = pd.read_csv("months.csv")

def month_expenses(date):
    month = stats[stats["days"].astype(str).str.contains(date, case=False)]
    total = month["expenses"].sum()
    return total
    
def month_income(date):
    month = stats[stats["days"].astype(str).str.contains(date, case=False)]
    
    total = month["income"].sum()
    return total
    


def get_mincome() :
    listt = []

   
    for i , row in months.iterrows() :
        total = month_income(row["month"])
        listt.append(total)
    return listt
    

def get_mexpenses() :
    listt = []

    
    for i , row in months.iterrows() :
        total = month_expenses(row["month"])
        listt.append(total)
    return listt
    

category = pd.read_csv("category.csv")


def categoryPaied(name):
    temp = expenses[expenses["Category"] == name]
    total = temp["Amount"].sum()
    return total


def get_categorypaied():
    listt = []

    for i,row in category.iterrows():
        total = categoryPaied(row["Category"])
        listt.append(total)
    return listt





def getPerc(x):
    return (x / x.sum() )*100
    

import numpy as np
def category():
    categoryGroup = expenses.groupby("Category")["Amount"].agg(sum)
    categorymax= expenses.groupby("Category")["Amount"].agg(max)
    categorymin= expenses.groupby("Category")["Amount"].agg(min)
    categorymean= expenses.groupby("Category")['Amount'].agg(np.mean)
    
    categoryName = pd.DataFrame(categoryGroup.index)
    categoryValues = pd.DataFrame(categoryGroup)
    categoryName["Amount"] = categoryValues.values
    categoryName["avg"] = categorymean.values
    categoryName["min"] = categorymin.values
    categoryName["max"] = categorymax.values
    categoryName["perc%"] = categoryValues.apply(getPerc).values
    categoryName.sort_values(by="Amount" , ascending=False , inplace=True)
    categoryName.to_csv("test.csv" , index=False)
    test = pd.read_csv("test.csv")
    print(test)


test = pd.read_csv("test.csv")
monthss = pd.read_csv("months.csv")
last = pd.read_csv('monthsandcategory.csv')

def getstat():
                def getMonths():
                    listt = []
                    for i in range(13):
                     for i,row in monthss.iterrows():
                        
                            x =  row["month"]
                            listt.append(x)
                    
                    return listt
                        

                def getcategories():
                    listt = []
                    for i , row in test.iterrows():
                        for i in range(5):
                            x = row["Category"]
                            listt.append(x)
                    return listt



                last["Category"] = getcategories()
                last["months"] = getMonths()  

                def cal_all(category, date):
                    total = expenses[(expenses["Category"].str.contains(category, case=False)) & (expenses["Date"].str.contains(date, case=False))]
                    summ = total["Amount"].mean()
                    return summ 
                
                def get_all():
                    listt = []
                    for i, row in last.iterrows():
                        date = row["months"]
                        category = row["Category"]
                        total_amount = cal_all(category, date)
                        listt.append(total_amount)
                    return listt
                 
                def save():
                    last["TotalAmount"] = get_all() #uncomment
                    last.fillna(0.0 , inplace=True)
                    last.to_csv('monthsandcategory.csv' , index=False)

                print(last)

                



