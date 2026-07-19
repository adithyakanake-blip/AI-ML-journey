import matplotlib.pyplot as plt  #Taken data is imaginary
plt.xkcd()
time = ["0:00", "1:00 ", "2:00", "3:00", "4:00", "5:00", "6:00","7:00",]
temperature = ["25.7","26.9","26.4","25.7","25.2","23.4","25.3","26.1"]
humidity = ["45.7","46.9","46.4","45.7","55.2","53.4","65.3","66.1"]
soil_moisture = ["35.7","36.9","36.4","45.4","55.9","53.5","65.5","66.4"]


plt.plot(time, temperature, color="blue", label="Temperature",linestyle='-', marker="o")
plt.plot(time, humidity, color="red", label="Humidity(%)",linestyle='-', marker=".")
plt.plot(time, soil_moisture , color="yellow", label="Soil_moisture(%)",linestyle='-', marker="^")


plt.title("Temperature,humidity,soil_moisture Variation Throughout the Day")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.savefig("line graph")
plt.legend()
plt.show()