from mootdx.quotes import Quotes

client = Quotes.factory(market='std')
# client.k(symbol="600300", begin="2017-07-03", end="2017-07-10")

# 前复权
data =  client.k(symbol="600300", begin="2017-07-03", end="2025-01-10", adjust='qfq')

print(data)