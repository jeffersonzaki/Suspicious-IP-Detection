# Suspicious IP Address Detection
There are many people that try to get around certain access retrictions using a proxy or VPN. This can be a good thing, and also a good thing. This project tries to figure out if we can detect if someone is using a proxy or not. This will allow you to see the risk factor of an IP Address being at high risk or low risk of being an anonymous proxy, allowing users to put certain temporary bans on high risk proxies.

<p align="center">
  <img src="https://woocommerce.com/wp-content/uploads/2014/09/anti-fraud.jpg">
</p>

## Summary of Contents
- [Data](https://github.com/jeffersonzaki/Suspicious-IP-Detection/tree/main/Data) - IP Address data

- [Scripts](https://github.com/jeffersonzaki/Suspicious-IP-Detection/tree/main/Scripts) - Python Scripts

- [Gitattributes](https://github.com/jeffersonzaki/Suspicious-IP-Detection/blob/main/.gitattributes) - Ignore large files

- [Gitignore](https://github.com/jeffersonzaki/Suspicious-IP-Detection/blob/main/.gitignore) - Ignore specific files

- [Exploratory Data Analysis](https://github.com/jeffersonzaki/Suspicious-IP-Detection/blob/main/EDA.ipynb) - Exploring IP data and changing the form of income

- [ReadMe](https://github.com/jeffersonzaki/Suspicious-IP-Detection/blob/main/README.md) - Project description

- [Machine Learning](https://github.com/jeffersonzaki/Suspicious-IP-Detection/blob/main/machine_learning.ipynb) - Contains multiple machine learning models

- [Neural Networks](https://github.com/jeffersonzaki/Suspicious-IP-Detection/blob/main/neural_networks.ipynb) - Contains 2 neural networks to learn data

## Project Member
- [Zaki Jefferson](https://github.com/jeffersonzaki)

## Project Scenario
When you own/control an online webservice then you will most likely run into people that use proxies to hide from you line of sight. This can be for their own privacy protection, but it can also be used for malpractice. If you want to protect yourself, your customers, and your business then you should be on the look out to see the risk of a certain proxy, and figure out what that proxy has done in the past, insuring that your interest is protected.

## Responsibilities
- Retrieve and manipulate data

- Perform EDA and data cleaning

- Perform a convolutional neural network and a Long Short Term Memeory neural network

- Perform classificaiton using sklearn machine learning models

## Data
The data that was collected is a large file which was not able to be brought onto github. Links to the datasets used will be provided:
- [IP2LOCATION Lite](https://lite.ip2location.com/database/px10-ip-proxytype-country-region-city-isp-domain-usagetype-asn-lastseen-threat-residential) - Able to retrieve csv files or a rar file of IPV4 and IPV6 Addresses

- [Data Hub](https://datahub.io/core/geoip2-ipv4#data-cli) - Able to obtain a csv file of IPV4 Geolocation Addresses which are proxies and non-proxies.
