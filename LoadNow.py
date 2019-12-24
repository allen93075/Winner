#用panda擷取表格資訊(當下)
import pandas as pd
#def xls 之後print
def xls():
    #url要用的網站
    url = 'https://info512.taifex.com.tw/Future/FusaQuote_Norl.aspx'
    #HTML的table>>[]
    out = pd.read_html(url, encoding='utf-8')[10]
    #out.drop=刪除不要的col
    out = out.drop(range(2, 6), 1)
    out = out.drop(range(7, 9), 1)
    out = out.drop(13, 1)

    return out

