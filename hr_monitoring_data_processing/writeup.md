## Question 1

Take a look at the file labeled `data/data2.txt`. Why might we have missing values or values that state "NO SIGNAL" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

[We might have missing values or "NO SIGNAL" values because of possible equipment malfunction, maybe the user was not wearing their equipment when heart rate was being measured, or because of death.]

## Question 2

While the "averages.png" and "maximums.png" graphs visualize typical values in our time-series data of heart rates and subsequently describe similar trends, the "stdevs.png" graph visualizes the standard deviations, which results in a graph with less apparent trends. In the context of heart rate, what does the standard deviation describe?

[In the context of heart rate, the standard deviation illustrates how the heart rates measured deviate from the typical maximums and averages.]

## Question 3

Run your `main.py` module and look at the graph labeled "averages.png." Roughly speaking, where do you see the time series experience a significant difference in values along the x-axis? Point out all x-values where you notice a drastic difference in future values.

[Roughly speaking, there is a significant difference between 10 and 30, on the x-axis.]

## Question 4

Do you also notice a corresponding difference in values in the "stdevs.png" graph? If so, do these differences align with the "averages.png" graph? 

[In my opinion, there is slight a corresponding difference in values, in the "stdevs.png" graph but it is between 15 and 30, instead of 10 and 30. These differences somewhat align with the "averages.png" graph.]
