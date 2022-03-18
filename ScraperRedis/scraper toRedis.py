from bs4 import BeautifulSoup
import time
import requests
import redis
import pickle5 as pickle


r = redis.StrictRedis('localhost')

while True:
    # Get the data from the website
    request = requests.get(f"https://www.blockchain.com/btc/unconfirmed-transactions")
    soup = BeautifulSoup(request.text, features="html.parser")

    counter = 0

    # Loop trough the data
    for EachPart in soup.find_all("div", {"class": "sc-1g6z4xm-0 hXyplo"}):
        hashHTML = EachPart.find('a', {"class": "sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK"})
        hash = hashHTML.text
        names = EachPart.find_all("span", {"class": "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"})
        timeTransaction = names[0].text
        amountBitcoin = names[1].text
        amountDollar = float(names[2].text.replace('$', '').replace(',',''))
        
        #Combine the relevant data in a list an send it to a dataframe
        new_row = {'hash':hash, 'amountBitcoin':amountBitcoin, 'amountDollar':amountDollar, 'time':timeTransaction}
        p_new_row = pickle.dumps(new_row)

        r.set(f"transaction{counter}", p_new_row)

        read_dict = r.get(f"transaction{counter}")
        yourdict = pickle.loads(read_dict)
        print(yourdict)
        
        counter = counter+1


    # Sleep for one minute
    time.sleep(60)

