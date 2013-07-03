if [ ! -n "$WERCKER_HIPCHAT_NOTIFY_TOKEN" ]; then
  error 'Please specify token property'
  exit 1
fi

if [ ! -n "$WERCKER_HIPCHAT_NOTIFY_ROOM_ID" ]; then
  error 'Please specify room_id property'
  exit 1
fi

if [ ! -n "$WERCKER_HIPCHAT_NOTIFY_FROM_NAME" ]; then
  error 'Please specify from_name property'
  exit 1
fi

if [ ! -n "$WERCKER_HIPCHAT_NOTIFY_MESSAGE" ]; then
  error 'Please specify message property'
  exit 1
fi

python "$WERCKER_STEP_ROOT/main.py" $WERCKER_HIPCHAT_NOTIFY_TOKEN $WERCKER_HIPCHAT_NOTIFY_ROOM_ID $WERCKER_HIPCHAT_NOTIFY_FROM_NAME $WERCKER_HIPCHAT_NOTIFY_MESSAGE
