hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

totalMins = mins + dura
resto = totalMins % 60
divisao = ((totalMins // 60)+hour)%24

print(str(divisao) + ":" + str(resto))
