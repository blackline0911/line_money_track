import re

def linepay_transactions(path):
    with open(path, encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    transactions = []
    current = {}

    data_pattern = re.compile(r'^20\d{2}\.\d{2}\.\d{2}')
    time_money_pattern = re.compile(r'(\d{2}:\d{2}).*NT\$ ?([\d,]+)')
    shop_pattern = re.compile(r'^商店名稱: ?(.*)')

    for line in lines:
        if data_pattern.match(line):
            if current:
                transactions.append(current)
                current = {}
            current['date'] = line.split()[0]
        elif match:=time_money_pattern.search(line):
            current['time'] = match.group(1)
            current['amount'] = int(match.group(2).replace(',',''))
        elif '付款完成' in line:
            continue
        elif match := shop_pattern.match(line):
            current['shop'] = match.group(1)
    if current:
        transactions.append(current)
    return transactions

t = linepay_transactions(r"C:\Users\kevin\Downloads\[LINE]LINE錢包test.txt")
print(t)
