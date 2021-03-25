# code_finalproject_researchmethods

## Using the code 
I would not clone the repository, because it will use a lot of space. I wanted to create a virtual environment, so you would always use the right versions of the packages I used, but I could not get this to work. I think if you are going to clone the repository, you will have that directory containing the virtual environment on your computer as well, even though I deleted it from the repository.

## Getting your data
To obtain the data used in the paper, you need to have an account for Karora of the University of Groningen. There you can run the `script.py` file. Before you are able to run that program you have to upload the script. Open the terminal and log in on Karora. On Karora you need to run the following command to upload the script.

```
scp /the/path/to/the/script/on/your/computer/script.py s1234567@karora.let.rug.nl:~/
```

The file will be in your root folder on your karora account. From there you will need to run the script on the tweets. These tweets should contain the text of the tweet and the date: 

```
zless /net/corpora/twitter2/Tweets/2021/01/*.out.gz | /net/corpora/twitter2/tools/tweet2tab text date | python3 script.py
```

The first part will give you the tweets for the first month of 2021, the second part will get the text and data of that tweet and the third part is the script. Do this for every month. 

Running the script for the three monhts, will create three JSON files. Use `ls` to get the names of the files and download them back to your computer. 

```
scp s4372344@karora.let.rug.nl:~/output_privacy_data_2021-03-12_18:36:34.203242.json /the/path/on/your/own/computer
```

If the name of the file is `output_privacy_data_2021-03-12_18:36:34.203242.json`, it will go to the path on your computer.

## Analyze your data
To get a graph and the values for the chi square test, you should run the python notebook `visualize_results.ipynb` on the JSON files. The names of these files should be changed in the notebook, if you want to run your own data. 
