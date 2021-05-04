import random

PROXY_GATEWAY_POOL = [
    "91.207.61.211:45785:Selsmartitalia:C2x6QnA", "91.211.116.154:45785:Selsmartitalia:C2x6QnA",
    "91.217.90.228:45785:Selsmartitalia:C2x6QnA", "185.252.25.162:45785:Selsmartitalia:C2x6QnA",
    "185.230.89.68:45785:Selsmartitalia:C2x6QnA"
]

proxy = random.choice(PROXY_GATEWAY_POOL)
pxy = 'http://{2}:{3}@{0}:{1}'.format(*proxy.split(':'))
