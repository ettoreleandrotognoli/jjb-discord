import xml.etree.ElementTree as XML
from jenkins_jobs.modules.base import Base

"""
<nz.co.jammehcow.jenkinsdiscord.WebhookPublisher plugin="discord-notifier@1.4.14">
      <webhookURL>https://discord.com/api/webhooks/847487134096818237/N9nMAKSZb2L-p79vnCnAcB5x9C15x0dP7mR5oKaUmQ1t0wFjyl3rnEKet-O-wypOe4lV</webhookURL>
      <branchName />
      <statusTitle />
      <thumbnailURL />
      <notes />
      <customAvatarUrl />
      <customUsername />
      <sendOnStateChange>false</sendOnStateChange>
      <enableUrlLinking>false</enableUrlLinking>
      <enableArtifactList>true</enableArtifactList>
      <enableFooterInfo>true</enableFooterInfo>
      <showChangeset>true</showChangeset>
      <sendLogFile>false</sendLogFile>
      <sendStartNotification>false</sendStartNotification>
    </nz.co.jammehcow.jenkinsdiscord.WebhookPublisher>
"""

boolean_options = {
    "send-on-state-change": "sendOnStateChange",
    "enable-url-linking": "enableUrlLinking",
    "enable-artifact-list": "enableArtifactList",
    "enable-footer-info": "enableFooterInfo",
    "show-changeset": "showChangeset",
    "send-log-file": "sendLogFile",
    "send-start-notification": "sendStartNotification",
}

text_options = {
    "webhook-url": "webhookURL",
    "branch-name": "branchName",
    "status-title": "statusTitle",
    "thumbnail-url": "thumbnailURL",
    "notes": "notes",
    "custom-avatar-url": "customAvatarUrl",
    "custom-username": "customUsername",
}

def publisher(registry, xml_parent, data):
    if data is None:
        data = dict()

    notifier = XML.SubElement(
        xml_parent, 'nz.co.jammehcow.jenkinsdiscord.WebhookPublisher '
    )
    notifier.set('plugin', 'discord-notifier@1.4.14')

    for (opt, attr) in text_options.items():
        (XML.SubElement(notifier, attr).text) = data.get(opt)

    for (opt, attr) in boolean_options.items():
        value = 'true' if data.get(opt, False) else 'false'
        (XML.SubElement(notifier, attr).text) = value