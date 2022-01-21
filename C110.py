import pandas as pd
import plotly.figure_factory as ff
import statistics as st
import random

df=pd.read_csv("data.csv")
temp_list=df["temp"].tolist()

temp_mean=st.mean(temp_list)
temp_median=st.median(temp_list)
temp_mode=st.mode(temp_list)
temp_stdev=st.stdev(temp_list)

print(temp_mean,temp_median,temp_mode)
print("standard deviation of population ", temp_stdev)

def showfig(data):
    fig=ff.create_distplot([data],["temp"],show_hist=False)

    fig.show()

def random_sampling(counter):
    dataset=[]    
    for i in range(0,counter):
        random_index=random.randint(0,len(temp_list)-1)
        dataset.append(temp_list[random_index])
    sample_mean=st.mean(dataset)
    return(sample_mean) 

def sampling_distribution():
    random_set_of_means=[]
    for i in range(0,1000):
        mean_value=random_sampling(400)
        random_set_of_means.append(mean_value)
    sampling_mean=st.mean(random_set_of_means)
    print("mean of samples",sampling_mean)     
    sampling_stdev=st.stdev(random_set_of_means)  
    print("standard deviation of sampling ",sampling_stdev)

    showfig(random_set_of_means)   


sampling_distribution()