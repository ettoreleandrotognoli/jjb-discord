# jjb-discord

Now on [jenkins-job-builder repo](https://review.opendev.org/admin/repos/jjb/jenkins-job-builder) 

Issue: https://github.com/ettoreleandrotognoli/jjb-discord/issues/1

Merged: https://review.opendev.org/c/jjb/jenkins-job-builder/+/878944

---

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
