import requests
import time
users = open("./list.txt", 'r', encoding='utf-8')
token = ""
for user in users.readlines():
    split = user.split("#")
    response =requests.post("https://discord.com/api/v9/users/@me/relationships", headers={"authorization":token, "accept":"*/*", "accept-encoding":"gzip, deflate, br", "accept-language":"en-GB,en;q=0.9", "content-lenght":"36", "cookie":"__dcfduid=99b50060abb111ecb128677dfbdae2aa; __sdcfduid=99b50061abb111ecb128677dfbdae2aad47f4f4e73da27f9ba74c789286bed79cc49bd0c8fdd4ed96290c0b11acf0716; OptanonConsent=isIABGlobal=false&datestamp=Thu+Mar+24+2022+20%3A33%3A02+GMT%2B0000+(Greenwich+Mean+Time)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0; locale=en-GB", "origin":"https://discord.com", "referer":"https://discord.com/channels/@me", "sec-fetch-dest":"empty", "sec-fetch-mode":"cors", "sec-fetch-site":"same-origin", "sec-gpc":"1", "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36", "x-context-properties":"eyJsb2NhdGlvbiI6IkFkZCBGcmllbmQifQ==", "x-debug-options":"bugReporterEnabled", "x-discord-locale":"en-GB", "x-super-properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk5LjAuNDg0NC44MyBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTkuMC40ODQ0LjgzIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjEyMDU5NSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="}, json={
    "username": split[0],
    "discriminator": split[1]
}) 
    print (response.text)
    time.sleep(5) #avoid ratelimit init :sunglasses: