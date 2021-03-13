from urllib import request
google_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1584113866&period2=1615649866&interval=1d&events=history&includeAdjustedClose=true'

def download_data (csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url,"w")
    for line in lines:
        fx.write(line+"\n")
    fx.close()

download_data(google_url)
