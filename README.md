# jjb-discord

Jenkins job builder for Discord Notifier

[discord-notifier](https://plugins.jenkins.io/discord-notifier/)@[1.4.14](https://github.com/jenkinsci/discord-notifier-plugin/tree/v1.4.14)

# Getting started

```yaml
- project:
    publishers:
      - discord-notifier:
          webhook-url: "https://discord.com/api/webhooks/..."
          enable-url-linking: true
          send-start-notification: true
          status-title: "Title"
```
