# hipchat-notify

Send a message to a HipChat room

## Options

### required

* `token` - Your HipChat token.
* `room-id` - The id of the HipChat room.

### optional

* `passed-message` - Use this option to override the default passed message.
* `failed-message` -  Use this option to override the default failed message.
* `from-name` - Use this option to override the name that will appear in the room as sender. Default is `wercker`.
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


