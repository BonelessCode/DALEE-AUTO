# Dall-E Mini Image Generation Script

Back in the middle of 2022, DALL-E was one of the most innovative Art generation out there which could produce extremely satisfying results for our time. 
Here are some examples which were generated on [Hugging Face](https://huggingface.co/spaces/dalle-mini/dalle-mini) at the time : 

![dallemini2022-6-2914-39-53-880eb1f-e1656510067492](https://github.com/BonelessCode/DALEE-AUTO/assets/59204911/a0e42789-7866-4a5c-9fd3-dca36dbc13d2)
![dallemini2022-6-2912-8-42-e9c0cda-e1656500996375](https://github.com/BonelessCode/DALEE-AUTO/assets/59204911/b158fb29-ef54-4c19-99e4-e8a7e67dc5a2)

Due to its suddent growth in popularity, many users accessed the free version, DALL-E MINI. Thish caused frequents overloads of servers and tremendous wait times. This repository consists of a small script made using Selenium (Python) to allow you to bypass the waiting times by sending requests as long as your request was not fulfilled.

To use it, you had to change the following line to your query
```
box.send_keys("futuristic astronaut")
```
in the file main.py and launch the file. An automated version of Google Chrome is opened and loops the request on the Hugging Face website until it was fulfilled.
