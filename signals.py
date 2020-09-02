from scipy import signal

import matplotlib.pyplot as plot

import numpy as np

 

# Sampling rate 1000 hz / second

t = np.linspace(0, 10, 1000, endpoint=True)

 

# Plot the square wave signal

#plot.plot(t, (signal.square(2 * np.pi * t) + 1) / 2)
plot.plot(t, (signal.square(np.pi * t) + 1) / 2)
 

# Give a title for the square wave plot

plot.title('Meandr 1 Hz')

 

# Give x axis label for the square wave plot

plot.xlabel('Time')

 

# Give y axis label for the square wave plot

plot.ylabel('Amplitude')

 

plot.grid(True, which='both')

 

# Provide x axis and line color

plot.axhline(y=0, color='k')

 

# Set the max and min values for y axis

plot.ylim(-0.1, 1.1)

 

# Display the square wave drawn

plot.show()