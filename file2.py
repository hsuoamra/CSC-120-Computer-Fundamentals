top_scores_list = []
LIST_LENGTH = 5
import time
def leaderBoard(num):
  if len(top_scores_list) < 5:
    top_scores_list.append(num)
  else:
    replacement = min (top_scores_list)
    if num > replacement:
      print ("*** New High Score ccreated! ***")
      top_scores_list.remove(min(top_scores_list))
      time.sleep(5)

import time
import random
for i in range(50):
  time.sleep(2)
  num = random.randint (1,50)
  print ("New number generated: " + str(num))
  leaderBoard(num)
  print (sorted(top_scores_list))

