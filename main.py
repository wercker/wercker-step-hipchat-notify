import sys
import hipchat

if len(sys.argv) < 6 :
  print 'There should be 6 arguments'
  sys.exit(1)

token = str(sys.argv[1])
room_id = str(sys.argv[2])
from_name  = str(sys.argv[3])
message  = str(sys.argv[4])
color = str(sys.argv[5])

hipster = hipchat.HipChat(token=token)

hipster.method('rooms/message', method='POST', parameters={'room_id': room_id, 'from': from_name, 'message': message, 'color': color})