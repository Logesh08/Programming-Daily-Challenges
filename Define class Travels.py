# Define class Travels
# A travel company receives N booking requests. Each booking request contains the source city, the destination city and the number of persons. Each bus in the travels has a maximum of X seats. The program must accept the N booking requests and the value of X as the input. For each booking request, the program must process the request and print the output based on the following conditions.
# - If the number of seats remaining in the bus (from the given source to the given destination) is greater than or equal to the number of persons in the booking request, then the seats must be booked and the program must print "Booked Successfully".
# - Else the program must print "Failed" as the output.

# Your task is to define the class Travels so that the program runs successfully.

# The calling code Hello.py is as given below.
# from travels import Travels

# N, X = map(int, input().split())
# travels = Travels(X)
# for ctr in range(N):
#     src, dest, count = input().strip().split()
#     print("Booked Successfully" if travels.bookTickets(src, dest, int(count)) else "Failed")

# Example Input/Output 1:
# Input:
# 10 5
# Trichy Coimbatore 10
# Chennai Bangalore 2
# Bangalore Chennai 5
# Chennai Bangalore 3
# Coimbatore Trichy 4
# Trichy Coimbatore 1
# Bangalore Chennai 1
# Chennai Bangalore 4
# Trichy Coimbatore 5
# Trichy Coimbatore 2

# Output:
# Failed
# Booked Successfully
# Booked Successfully
# Booked Successfully
# Booked Successfully
# Booked Successfully
# Failed
# Failed
# Failed
# Booked Successfully

# Explanation:
# Here N = 10 and X = 5.
# So the maximum number of tickets that can be booked from one city to another is 5.
# Trichy Coimbatore 10 -> Failed (Maximum 5 tickets can be booked)
# Chennai Bangalore 2 -> Booked Successfully (No tickets booked from Chennai to Bangalore)
# Bangalore Chennai 5 -> Booked Successfully (No tickets booked from Bangalore to Chennai)
# Chennai Bangalore 3 -> Booked Successfully (Only 2 tickets are booked from Chennai to Bangalore. So 3 seats remaining)
# Coimbatore Trichy 4 -> Booked Successfully (No tickets booked from Coimbatore to Trichy)
# Trichy Coimbatore 1 -> Booked Successfully (No tickets booked from Trichy to Coimbatore)
# Bangalore Chennai 1 -> Failed (All 5 tickets are booked from Bangalore to Chennai)
# Chennai Bangalore 4 -> Failed (All 5 tickets are booked from Chennai to Bangalore)
# Trichy Coimbatore 5 -> Failed (Only 4 seats remaining from Trichy to Coimbatore)
# Trichy Coimbatore 2 -> Booked Successfully (Only 1 ticket booked from Trichy to Coimbatore. So 4 seats remaining)

# Example Input/Output 2:
# Input:
# 9 15
# Bangalore Dindigul 8
# Madurai Salem 11
# Bangalore Dindigul 15
# Hosur Bangalore 10
# Hosur Bangalore 3
# Theni Coimbatore 12
# Hosur Bangalore 4
# Theni Hosur 18
# Trichy Theni 1

# Output:
# Booked Successfully
# Booked Successfully
# Failed
# Booked Successfully
# Booked Successfully
# Booked Successfully
# Failed
# Failed
# Booked Successfully









class Travels:
    def __init__(self , x):
        self.x = x
        self.d = {}
    def bookTickets(self, src, dest , count):
        if count>self.x:
            return False
        else:
            d = self.d
            adress = src+dest
            if adress in d.keys():
                if d[adress]+count>self.x:
                    return False
                else:
                    d[adress]+=count
                    return True
            else:
                d[adress] = count
                return True