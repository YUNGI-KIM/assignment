from pathlib import Path
from urllib.request import urlretrieve
base_url = "https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/data/"
data_path = Path() / "data"
data_path.mkdir(parents=True, exist_ok=True)
def myWget(filename):
    # 다운로드 대상 파일 경로
    file_url = base_url + filename

    # 저장 경로와 파일명
    target_path = data_path / filename

    return urlretrieve(file_url, target_path)
def shopping(shop_file):
    target_path = myWget(shop_file)[0]
    shop = open(target_path,'r')

    shop_dict = {}

    for line in shop:
        try:
            (product, price) = line.strip().split() 
            shop_dict[product] = int(price.replace("원","")) 
        except:
            continue
    shop.close()

    return shop_dict
def item_price(shop_file, item):
    target_path = myWget(shop_file)[0]
    shop = open(target_path,'r')

    shop_dict = {}

    for line in shop:
        try:
            (product, price) = line.strip().split() 
            shop_dict[product] = int(price.replace("원","")) 
        except:
            continue
    shop.close()
    
    return shop_dict[item]