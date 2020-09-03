""""
Goal 

Create a Program that Implements the Voting System from CPG Grey Voting system

The program should include:

The ability to run a vote acording to the alternative vote method
    see : https://youtu.be/3Y3jE3B8HsE?t=76
The ability to have / Define 2 - 7 candidates
Votes are weighted acording to ones number of stocks heald from Total exsisting stocks 
the ability to set a timelimit for voteing, and immediatde calculation and display of vote at that time.
Voters should stay annonymus
Voters must select order of preference ( of item voted on)
If items are left blank , when those items come into play vote is abstained from
Voters can only vote once
voters number of shares should be able to be changed and still hold to the system.
Partial votes must be clearly devided acording to shares / plartial votes are allowed but must have a total of 100% of stock shares accounted for, no more no less
company shares should also be flexable.

"""

"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


(num1 / num2 * 100)  

x=input("Enter a value: " ) 
y=input("Enter total value: ") 
 
#calculating % 
 
P=(x/y) *100 
print (P) 
"""

Exsisting_Total_Shares = 0

def Calc_Shares():
    Exsisting_Total_Shares = sum(all_user.shares)

class Stake_Holder:
    def __init__(self, first_name, last_name, dob, num_of_shares):
        self.name = first_name 
        self.last = last_name
        self.dob = dob  # ddmmyyyy
        self.shares = num_of_shares

def Set_Time_Frame(consensus_deadline):
    datetime.today - consensus_deadline = timedelta
    while timedelta != 0:
        run vote
    -=

def Seek_Consensus():


def share_of_voice(user_id)
    share_of_voice = (alotted_shares / Total_Shares *100)

def Call_Vote( MOTION_NAME, Motion_1, Motion_2, Motion_3, Motion_4 ):


def Stake_Holder(ID , option_1, option_2, option_3,):
    alotted_shares =
    share_of_voice = 
    pass

