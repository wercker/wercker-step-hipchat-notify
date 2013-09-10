# hipchat-notify

Send a message to a HipChat room... with color!

# What's new

- Add support for color for passed and failed messages (thanks adams-sarah)
- Add support for 'notify' for passed and failed messages

# Options

* `token` (required) Your HipChat token.
* `room-id` (required) The id of the HipChat room.
* `passed-message` (optional) The message which will be shown on a passed build or deploy.
* `failed-message` (optional) The message which will be shown on a failed build or deploy.
* `passed-color` (optional, default: `green`) The color of a passed build/deploy message in HipChat.
* `failed-color` (optional, default: `red`) The color of a failed build/deploy message in HipChat.
* `passed-notify` (optional, default: `false`) If this is `true` the passed build/deploy message will make HipChat notify the user.
* `failed-notify` (optional, default: `true`) If this is `true` the passed build/deploy message will make HipChat notify the user.
* `from-name` (optional, default: `wercker`) Use this option to override the name that will appear in the room as sender.
* `on` (optional, default: `always`) When should this step send a message. Possible values: `always` and `failed`.

# Example

Add HIPCHAT_TOKEN as deploy target or application environment variable.

```yaml
build:
  after-steps:
    - hipchat-notify:
        token: $HIPCHAT_TOKEN
        room-id: id
        from-name: name
```

# License

The MIT License (MIT)

Copyright (c) 2013 wercker

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Changelog

## 0.1.6

- Add support for color for passed and failed messages (thanks adams-sarah)
- Add support for 'notify' for passed and failed messages

## 0.1.5

*Broken*

## 0.1.4

- Fix example in readme
- Update readme
