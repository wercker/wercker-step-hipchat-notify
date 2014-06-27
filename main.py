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

post_to_room = False

if str(notify) == 'true':
    notify = True
if not target_branch in build_branch:
    post_to_room = False
if target_branch == 'all' or target_branch == build_branch:
    post_to_room = True

if not post_to_room:
    print 'Build branch:{build_branch} is not a target of hipchat-notify. target_branch: {target_branch}'.format(
            build_branch=build_branch,
            target_branch=target_branch
            )
    sys.exit(0)

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
