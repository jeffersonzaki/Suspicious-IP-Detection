# ----------------------IMPORTS------------------
import pandas as pd
import numpy as np
import os

# Graphing
import matplotlib.pyplot as plt
import seaborn as sns

# IP Address
import ipaddress as ip

# Encoding
from sklearn.preprocessing import LabelBinarizer

# Machine Learning
from sklearn.model_selection import train_test_split

# NLP
import texthero as hero
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# ---------------------------------------------------

# ---------------------DATASETS----------------------
ipv4_df = pd.read_csv("Data/ipv4.csv")
ipv4_proxy_df = pd.read_csv("Data/IP2PROXY-IPV4.CSV")
# ---------------------------------------------------

# ----------------------CLEANING DATA-----------------------
# Renaming the two columns that will be kept
ipv4_proxy_df.rename(columns={"16778241": "IP_Networks", "PUB": "is_anonymous_proxy"}, inplace=True)
# Removing all columns except IP_Networks and is_anonymous_proxy
ipv4_proxy_df = ipv4_proxy_df[["IP_Networks", "is_anonymous_proxy"]]

# Changing data type on ipv4_df in the is_anonymous_proxy to a string
ipv4_df["is_anonymous_proxy"] = ipv4_df["is_anonymous_proxy"].astype(str)
# Changing data type to a string
ipv4_proxy_df["is_anonymous_proxy"] = ipv4_proxy_df["is_anonymous_proxy"].astype(str)

# Converting ipv4 proxy IP_Networks columns in IP addresses
ipv4_proxy_df["IP_Networks"] = ipv4_proxy_df["IP_Networks"].apply(lambda x: ip.IPv4Address(x).exploded)
# Changing the values of the is_anonymous_proxy to True
ipv4_proxy_df["is_anonymous_proxy"] = ipv4_proxy_df["is_anonymous_proxy"].replace(to_replace="PUB", value="True")

# Using a lambda function to get IP addresses from the specified column
ipv4_df["IP_Networks"] = ipv4_df["IP_Networks"].apply(lambda x: ip.ip_interface(x).ip.exploded)

# Perfoming a concat
ipv4_new_df = pd.concat(objs=[ipv4_df, ipv4_proxy_df], axis=0, ignore_index=True)

# Getting rows that are equal to True and rows that are equal to Flase
ipv4_True = ipv4_new_df.loc[ipv4_new_df["is_anonymous_proxy"] == "True"]
ipv4_False = ipv4_new_df.loc[ipv4_new_df["is_anonymous_proxy"] == "False"]
# Randomly selecting 100_000 rows from each dataframe of True and False
ipv4_random_true = ipv4_True.sample(n=20_000, random_state=1)
ipv4_random_false = ipv4_False.sample(n=20_000, random_state=1)
# Combining True and False datasets
ipv4_final_df = pd.concat(objs=[ipv4_random_false, ipv4_random_true], join="inner", axis=0, ignore_index=True)

# Replacing the period with an empty string to combine into one number
ipv4_final_df["IP_Networks"] = ipv4_final_df["IP_Networks"].apply(lambda x: x.replace(".", ""))

# Independent and Dependent Variable
X = ipv4_final_df[["IP_Networks"]]
y = ipv4_final_df[["is_anonymous_proxy"]]
# Turning X and y into numpy arrays for neural networks
# X = X.to_numpy()
# y = y.to_numpy()

# Train, test, and validation split on data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
# Creating validation split
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=1)

# Using LabelBinarizer for IP Addresses
lb = LabelBinarizer()  # Instantiating class
lb_ip = LabelBinarizer()
# Encoding dependent variable
y_train = lb.fit_transform(y_train)
y_test = lb.fit_transform(y_test)
y_val = lb.fit_transform(y_val)
# Using NLP 
# X_train = lb_ip.fit_transform(X_train)
# X_test = lb_ip.fit_transform(X_test)
# X_val = lb_ip.fit_transform(X_val)
# Transforming data to numpy array
X_train = X_train.apply(lambda x: np.array(x))  # Changing list into an array of numbers
X_test = X_test.apply(lambda x: np.array(x))
X_val = X_val.apply(lambda x: np.array(x))
# ----------------------------------------------------------------------------------