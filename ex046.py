import datetime
import time

import emoji

segundos = time.time()

for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
print("BOOOOOM!!!!!")

print(emoji.emojize(":party_popper:"*20))
print(emoji.emojize(":fireworks:"*20))