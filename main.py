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
    notify = True
if not target_branch in build_branch:
    notify = False
if target_branch == 'all':
    notify = True

hipster = hipchat.HipChat(token=token)

hipster.message_room( room_id=room_id,
                      message_from=from_name,
                      message=message,
                      color=color,
                      notify=notify
                    )
