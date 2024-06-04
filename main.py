mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]


print("missions run:"+str(len(mission_names)))
def count(mission_success):
    return sum(mission_success)
print("mission sucesses: " + str(count(mission_success)))
count=0
for y in mission_success:
    if y==True:
        count=count+1
rate= (count/ 7)*100
rate=round(rate,2)
print("Sucess rate: "+str(rate)+"%")
print("missions run before the year 2000:")
m=0
for z in mission_years:
    if z < 2000:
        print(mission_names[m])
        m=m+1
    else:
        m=m+1
        
            