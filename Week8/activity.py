import matplotlib.pyplot as plt
import pandas as pd

%matplotlib inline  # jupyter notebook

# Load data
data = pd.read_csv('Standing.csv', sep=',',  names=["time_ms", "x", "y","z"])
print(len(data))

# Plot
plt.figure(figsize = (15,4), dpi=100)
plt.subplot(311)
plt.plot(data['time_ms'],data['x'])
#plt.plot(data['time_ms'][300:320],data['y'][300:320])
#plt.xticks(data['time_ms'][300:320])
plt.xlabel('time (ms)')
plt.ylabel('x')

plt.subplot(312)
plt.plot(data['time_ms'],data['y'])
#plt.plot(data['time_ms'][300:320],data['y'][300:320])
#plt.xticks(data['time_ms'][300:320])
plt.xlabel('time (ms)')
plt.ylabel('y')

plt.subplot(313)
plt.plot(data['time_ms'],data['z'])
#plt.plot(data['time_ms'][300:320],data['y'][300:320])
#plt.xticks(data['time_ms'][300:320])
plt.xlabel('time (ms)')
plt.ylabel('z')

plt.show()