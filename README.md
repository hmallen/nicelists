# nicemessages

I needed to parse some json messages from the Coinmarketcap API via pymarketcap (https://github.com/mondeja/pymarketcap) and turn them into a nice output for Slack messages. While this is basically project-specific at the moment, I do hope to turn it into a more useful set of tools eventually.

<b>Usage:</b>

```python
from pymarketcap import Pymarketcap
from nicemessages import NiceMessages

cmc = Pymarketcap()
nm = NiceMessages()

currency_data = cmc.currency('ZIL')
formatted_rows = nm.cmc_to_rows(currency_data)
even_columns = nm.even_columns(formatted_rows)

"""
## Example Output ##

# formatted_rows #
*Name:* Zilliqa
*Market Cap:* 866632381.981
*Rank:* #25
*24h Volume:* 25719700.0
*Price:* 0.118244
*Source Code:* https://github.com/Zilliqa/Zilliqa
*Websites:*
    https://www.zilliqa.com/
*Chats:*
    https://t.me/zilliqachat
*Explorers:*
    https://etherscan.io/token/0x05f4a42e251f2d52b8ed15e9fedaacfcef1fad27
    https://ethplorer.io/address/0x05f4a42e251f2d52b8ed15e9fedaacfcef1fad27

# even_rows #
*Name:*        Zilliqa
*Market Cap:*  866632381.981
*Rank:*        #25
*24h Volume:*  25719700.0
*Price:*       0.118244
*Source Code:* https://github.com/Zilliqa/Zilliqa
*Websites:*
    https://www.zilliqa.com/
*Chats:*
    https://t.me/zilliqachat
*Explorers:*
    https://etherscan.io/token/0x05f4a42e251f2d52b8ed15e9fedaacfcef1fad27
    https://ethplorer.io/address/0x05f4a42e251f2d52b8ed15e9fedaacfcef1fad27
"""
```
