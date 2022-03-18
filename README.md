# Databases Advanced - Louis De Backer, r0808416
All of the exercises of the course Databases Advanced

## What do you need? 
All you need is python3 and some packages. 

Required packages for the scraper:
- BeautifulSoup
- time
- requests
- pandas
- warnings

For mongoDB you also need:
- pymongo

## How to use the scraper?
To use the scraper you need to run the program and it will keep going every minute until you will stop it. 
If you want to stop it you just press CTRL+C or ENTER.

## Screenshots of scraper running
### Scraper
![scraper](https://user-images.githubusercontent.com/74768842/158421235-3c429109-7b9b-4bd4-bf62-c3cc309c4cdd.png)


### Scraper with MongoDB
![mongoDB](https://user-images.githubusercontent.com/74768842/158421249-aa5f1a0e-0e29-4f8a-b2b6-98ec5c907bb2.png)


### Scraper with Redis
#### The data that has been scraped is send to Redis
![toReids](https://user-images.githubusercontent.com/74768842/159017953-4c38087a-ef3e-4e4a-8086-9ab3562a3da7.png)

#### Data is pulled from Redis and send to MongoDB
![fromRedisToMongoDB](https://user-images.githubusercontent.com/74768842/159017931-3a66f207-41f4-419e-9edc-d5f32e09fd72.png)
