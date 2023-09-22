'''Constants
'''

PORNO_TERMS_STR = '''
    sex|porn|xx|banlinh|quyong|checkerviet|maulon|jav|prn|baocaosu|xhamster|viet69|
    tinhduc|thudam|spank|strip|loz|phimheo|ditnhau|ditme|henta|xvideo|quaylen|chinababe|
    gaigu|gaigoi|gaixinh|xnxx|vlx|cliphot|sieudamtv|heomup|chongtoico|phimcapba|londep|
    lontv|lauxanh|fuck|tuoinung|buoito|kynuviet|gaikhoehang|gaidam|chinaav|nguoilon
'''
NONPORNO_TERMS_STR = '''
    java|google|youtube|twitter|reddit|facebook|shopee|pinterest
'''

PORNO_TERMS = tuple(term.strip() for term in PORNO_TERMS_STR.split("|"))
NONPORNO_TERMS = tuple(term.strip() for term in NONPORNO_TERMS_STR.split("|"))
