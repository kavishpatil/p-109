import pandas as pd
import statistics
import plotly.figure_factory as ff

df = pd.read_csv("StudentsPerformance.csv")

mathscore = df["mathScore"].tolist()

mean = statistics.mean(mathscore)
median = statistics.median(mathscore)
mode = statistics.mode(mathscore)
sd = statistics.stdev(mathscore)

print(mean)
print(median)
print(mode)
print(sd)

figure = ff.create_distplot([mathscore],["distribution of height"],show_hist=False)
#figure.show()

sd1_start,sd1_end = mean-sd,mean+sd
sd2_start,sd2_end = mean-(2*sd),mean+(2*sd)
sd3_start,sd3_end = mean-(3*sd),mean+(3*sd)

data_in_sd1 = [height for height in mathscore if height>sd1_start and height<sd1_end] 
data_in_sd2 = [height for height in mathscore if height>sd2_start and height<sd2_end]
data_in_sd3 = [height for height in mathscore if height>sd3_start and height<sd3_end]

print(len(data_in_sd1)*100/len(mathscore))
print(len(data_in_sd2)*100/len(mathscore))
print(len(data_in_sd3)*100/len(mathscore))