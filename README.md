# hipchat-notify

The hipchat notify step sends a message based on the build or deploy outcome. It supports sending a message for passed and failed builds, and for passed and failed deploys. For the failed builds or deploys to work though, you need to add it to the after-steps section of a build or deploy, to ensure it gets run.

# What's new

- Add support for `text` format.

# Options

* `token` (required) Your HipChat token.
* `room-id` (required) The id of the HipChat room. (retrieve yours from https://www.hipchat.com/rooms/ids)
* `passed-message` (optional) The message which will be shown on a passed build or deploy.
* `failed-message` (optional) The message which will be shown on a failed build or deploy.
* `passed-color` (optional, default: `green`) The color of a passed build/deploy message in HipChat.
* `failed-color` (optional, default: `red`) The color of a failed build/deploy message in HipChat.
* `passed-notify` (optional, default: `false`) If this is `true` the passed build/deploy message will make HipChat notify the user.
* `failed-notify` (optional, default: `true`) If this is `true` the passed build/deploy message will make HipChat notify the user.
* `from-name` (optional, default: `wercker`) Use this option to override the name that will appear in the room as sender.
* `on` (optional, default: `always`) When should this step send a message. Possible values: `always` and `failed`.
* `message-format` (optional, default: `html`) Send the noticiation in `html` or `text` message format. `html` message format support links, but does not support emoticons. `text` message format supports emoticons, but does not support links.

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

# Changelog

## 1.0.4

- Add support for `text` message format.

## 1.0.3

- Fix bug if `from-name` contains a space (thanks @anfedorov)

## 1.0.2

- Remove emoticons introduced by version `1.0.1`.

## 1.0.1

- Add more icons to the default messages

## 1.0.0

- Add links to application and build/deploy

## 0.1.6

- Add support for color for passed and failed messages (thanks adams-sarah)
- Add support for 'notify' for passed and failed messages

## 0.1.5

*Broken*

## 0.1.4

- Fix example in readme
- Update readme
