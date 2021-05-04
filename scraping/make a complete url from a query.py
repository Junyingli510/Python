from urllib.parse import urlencode

url = "http://in-stjoseph-assessor.governmax.com/propertymax/search_property.asp?l_nm=owner&user=guest_in-stjoseph-assessor&pass=manatron&sid={}"

query = {
    'l_nm': 'owner',
    'user': 'guest_in-stjoseph-assessor',
    'pass': 'manatron',
    'sid': 'F83D36C5F0094B86B4BE9307649DA66F'
}

query_encoded = urlencode(query)
new_url = "http://in-stjoseph-assessor.governmax.com/propertymax/search_property.asp?" + query_encoded
print(new_url)