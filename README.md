# hipchat-notify

Send a message to an HipChat room

## Options

### required

* `token` - Your HipChat token.
* `room-id` - The id of the HipChat room.
* `from-name` - The name that will appear in the room as sender.

### optional

* `passed-message` - Use this option to override the default passed message.
* `failed-message` -  Use this option to override the default failed message.
* `on` - Possible values: `always` and `failed`, default `always`



Example
--------

Add HIPCHAT_TOKEN as deploy target or application environment variable.


    build:
        after-steps:
            - hipchat-notify:
                token: $HIPCHAT_TOKEN
                room_id: id
                from-name: name


