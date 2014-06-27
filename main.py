import sys
import hipchat

if len(sys.argv) < 7 :
  print 'There should be 7 arguments'
  sys.exit(1)

token = str(sys.argv[1])
room_id = str(sys.argv[2])
from_name  = str(sys.argv[3])
message  = str(sys.argv[4])
color = str(sys.argv[5])
notify = str(sys.argv[6])
target_branch = str(sys.argv[7])
build_branch = str(sys.argv[8])

if str(notify) == 'true':
    notify = '1'
if not target_branch in build_branch:
    notify = '0'
if target_branch == 'all':
    notify = '1'

hipster = hipchat.HipChat(token=token)

hipster.method('rooms/message',
                method='POST',
                parameters={
                    'room_id': room_id,
                    'from': from_name,
                    'message': message,
                    'color': color,
                    'notify': notify
                    }
                )
