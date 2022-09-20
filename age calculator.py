

def age_cal(dd, mm, yy, cur_d, cur_m, cur_y):
	
	print("\nDate of Birth = ",dd,"/",mm,"/",yy,"\n")
	print("Current Date = ",cur_d,"/",cur_m,"/",cur_y,"\n")

	print("Your Current Age is = ",cur_y-yy," Years ",cur_m-mm," Months ",cur_y-yy," Days ")	


print("\nAge Calculator \n( All Data Should be in Numbers Only ! )\n")


date = int(input("Enter Date of Birth = "))
month = int(input("Enter month of Birth = "))
year = int(input("Enter Year of Birth = "))
	
cur_date = int(input("\nEnter Current Date = "))
cur_mon = int(input("Enter Current Month = "))
cur_yr = int(input("Enter Current Year = "))

age_cal(date, month, year, cur_date, cur_mon, cur_yr) 