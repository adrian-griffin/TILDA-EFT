import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
import sqlite3
import pandas as pd
import requests

global item_list
def refresh_database():
    global item_list
    with open(str(dir_path)+"\\"+"item_info.sql","w+") as f:
        currentdata = f.read()
        cleardata = ""
        f.write(cleardata)
        f.close()


    item_dbpy = sqlite3.connect(str(dir_path)+"\\"+"item_info.sql")
    c = item_dbpy.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS items
        (id text primary key, name text, shortName text, avg24hPrice real, wikiLink text, iconLink text, width real,
        fleaMarketFee real, height real, lastLowPrice real)
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS usedInTasks
        (id text, name text, tasks)
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS sellFor
        (id text, name text, vendor text, price text, currency text)
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS buyFor
        (id text, name text, vendor text, price text, currency text)
    ''')


    def run_query(query):
        response = requests.post('https://api.tarkov.dev/graphql', json={'query': query})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))
    #main.win_m.item_desc.setText(QCoreApplication.translate("MainWindow", u"Attempting Item Database Update!", None))
    api_query = """
    {
            items {
            name
            id
            shortName
            avg24hPrice
            wikiLink
            iconLink
            width
            height
            fleaMarketFee
            lastLowPrice
            usedInTasks{
                    name
                    }
            sellFor{
                    vendor{
                    name
                    }
                    price
                    currency
                    }
            buyFor{
                    vendor{
                    name
                    }                
                    price
                    currency
                    }   
            }
    }"""


    api_result = run_query(api_query)

    item_list = []
    pytem_dict = {}
    pytem_dict.clear()
    item_dict = api_result['data']['items']
    item_list.clear()

    i=0
    while i < len(item_dict):
        item_name = item_dict[i]['name']
        item_name = item_name.replace('"','')
        short_name = item_dict[i]['shortName']
        short_name = short_name.replace('"','')
        item_subitems = {}
        item_subitems.clear()

        item_list.append(item_name)
        pytem_dict[str(item_name)] = item_subitems
        
        if item_dict[i]['id'] == None:
            item_dict[i]['id'] = "0"
        if short_name == None:
            short_name = ""
        if item_dict[i]['avg24hPrice'] == None:
            item_dict[i]['avg24hPrice'] = 0
        if item_dict[i]['wikiLink'] == None:
            item_dict[i]['wikiLink'] = "0"
        if item_dict[i]['lastLowPrice'] == None:
            item_dict[i]['lastLowPrice'] = 0
        if item_dict[i]['iconLink'] == None:
            item_dict[i]['iconLink'] = "0"
        if item_dict[i]['width'] == None:
            item_dict[i]['width'] = 0
        if item_dict[i]['height'] == None:
            item_dict[i]['height'] = 0
        if item_dict[i]['fleaMarketFee'] == None:
            item_dict[i]['fleaMarketFee'] = 0


        #item_subitems['usedInTasks'] = item_dict[i]['usedInTasks']
        #item_subitems['sellFor'] = item_dict[i]['sellFor']
        #item_subitems['buyFor'] = item_dict[i]['buyFor']


        c.execute('''INSERT INTO items VALUES ('''+'"'+str(item_dict[i]['id'])+'"'+''','''+'"'+str(item_name)+'"'+''','''+'"'+str(short_name)+'"'+''','''+str(item_dict[i]['''avg24hPrice'''])+''',
            '''+'"'+str(item_dict[i]['wikiLink'])+'"'+''','''+'"'+str(item_dict[i]['iconLink'])+'"'+''','''+str(item_dict[i]['width'])+''','''+str(item_dict[i]['fleaMarketFee'])+''',
            '''+str(item_dict[i]['height'])+''','''+str(item_dict[i]['lastLowPrice'])+")")


        task_dict = item_dict[i]['usedInTasks']
        task_string = ""
        try:
            for j in task_dict:
                task_string = task_string+str(j['name'])+","
            c.execute('''INSERT INTO usedInTasks VALUES ('''+'"'+str(item_dict[i]['id'])+'"'+''','''+'"'+str(item_name)+'"'+''','''+'"'+task_string+'"'+")")
        except:
            pass




####
        sellFor_dict = item_dict[i]["sellFor"]

        try:
            for s in sellFor_dict:
                sell_vendor = s["vendor"]["name"]
                sell_price = s["price"]
                sell_currency = s["currency"]
                #print('''INSERT INTO sellFor VALUES ('''+'"'+str(item_dict[i]['id'])+'"'+''','''+'"'+str(item_name)+'"'+''','''+'"'+str(sell_vendor)+'"'+''','''+'"'+str(sell_price)+'"'+''','''+'"'+str(sell_currency)+'"'+")")
                c.execute('''INSERT INTO sellFor VALUES ('''+'"'+str(item_dict[i]['id'])+'"'+''','''+'"'+str(item_name)+'"'+''','''+'"'+str(sell_vendor)+'"'+''','''+'"'+str(sell_price)+'"'+''','''+'"'+str(sell_currency)+'"'+")")
                
        except:
            pass

    
        buyFor_dict = item_dict[i]["buyFor"]

        try:
            for b in buyFor_dict:
                buy_vendor = b["vendor"]["name"]
                buy_price = b["price"]
                buy_currency = b["currency"]
                #print('''INSERT INTO sellFor VALUES ('''+'"'+str(item_dict[i]['id'])+'"'+''','''+'"'+str(item_name)+'"'+''','''+'"'+str(sell_vendor)+'"'+''','''+'"'+str(sell_price)+'"'+''','''+'"'+str(sell_currency)+'"'+")")
                c.execute('''INSERT INTO buyFor VALUES ('''+'"'+str(item_dict[i]['id'])+'"'+''','''+'"'+str(item_name)+'"'+''','''+'"'+str(buy_vendor)+'"'+''','''+'"'+str(buy_price)+'"'+''','''+'"'+str(buy_currency)+'"'+")")
                #print(buy_currency,buy_price,buy_vendor)
        except:
            pass

        i+=1

    item_dbpy.commit()


    for row in item_dbpy.execute('SELECT name FROM items'):
        item_list.append(row[0])
    


    print("refreshed db")





    item_dbpy.close()

    

#refresh_database()