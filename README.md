hipchat-notify
===========================

Send a message to an HipChat room


Example
--------
```
    - wouter/hipchat-notify:
        token: $HIPCHAT_TOKEN
        room_id: id
        from_name: name
        message: $WERCKER_APPLICATION_OWNER_NAME/$WERCKER_APPLICATION_NAME build by $WERCKER_STARTED_BY finished
```