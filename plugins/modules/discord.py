#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2026, Violet Caulfield
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: discord
short_description: Send a message to a Discord channel via an incoming webhook
version_added: "0.0.1"
description:
  - Posts a message to a Discord channel using an incoming webhook's ID and token.
  - Always reports C(changed), since sending a notification is an action rather than
    idempotent state.
options:
  id:
    description:
      - The webhook's ID — the first path segment after C(/webhooks/) in its URL
        (C(https://discord.com/api/webhooks/<id>/<token>)).
    required: true
    type: str
  token:
    description:
      - The webhook's token — the second path segment. Treated as sensitive and
        omitted from logs.
    required: true
    type: str
  message:
    description:
      - The message content to send. Ignored when O(body) is set.
    required: true
    type: str
  username:
    description:
      - Display name shown alongside the message. Ignored when O(body) is set.
    type: str
    default: Ansible
  body:
    description:
      - Override the entire POST body, e.g. to send embeds instead of a plain
        C(content) string. When set, O(message) and O(username) are ignored.
    type: dict
  api_uri_path:
    description:
      - Discord API base URL, with no trailing slash.
    type: str
    default: https://discord.com/api
  webhook_api_path:
    description:
      - Webhook endpoint path, with no trailing slash, relative to O(api_uri_path).
    type: str
    default: webhooks
  expected_status:
    description:
      - HTTP status codes treated as a successful POST.
    type: list
    elements: int
    default: [200, 204]
  validate_certs:
    description:
      - Whether to validate TLS certificates when posting to the webhook.
    type: bool
    default: true
author:
  - Violet Caulfield
'''

EXAMPLES = r'''
- name: Send a Discord notification
  cosmonautical.notify.discord:
    id: "{{ discord_webhook_id }}"
    token: "{{ discord_webhook_token }}"
    message: "Deployment completed on {{ inventory_hostname }}."
  no_log: true

- name: Send to every webhook in a vaulted list
  cosmonautical.notify.discord:
    id: "{{ item.id }}"
    token: "{{ item.token }}"
    message: "Deployment completed on {{ inventory_hostname }}."
  loop: "{{ discord_webhooks }}"
  delegate_to: localhost
  no_log: true
'''

RETURN = r'''
status:
  description: The HTTP status code returned by Discord.
  type: int
  returned: success
'''

import json

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url


def main():
    module = AnsibleModule(
        argument_spec=dict(
            id=dict(type='str', required=True),
            token=dict(type='str', required=True, no_log=True),
            message=dict(type='str', required=True),
            username=dict(type='str', default='Ansible'),
            body=dict(type='dict'),
            api_uri_path=dict(type='str', default='https://discord.com/api'),
            webhook_api_path=dict(type='str', default='webhooks'),
            expected_status=dict(type='list', elements='int', default=[200, 204]),
            validate_certs=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    url = '%s/%s/%s/%s' % (
        module.params['api_uri_path'],
        module.params['webhook_api_path'],
        module.params['id'],
        module.params['token'],
    )

    body = module.params['body']
    if body is None:
        body = {
            'content': module.params['message'],
            'username': module.params['username'],
        }

    if module.check_mode:
        module.exit_json(changed=True, status=None)

    response, info = fetch_url(
        module,
        url,
        method='POST',
        data=json.dumps(body),
        headers={'Content-Type': 'application/json'},
    )

    status = info.get('status', -1)
    if status not in module.params['expected_status']:
        module.fail_json(
            msg='Discord webhook POST failed with status %s: %s' % (status, info.get('msg', 'unknown error')),
            status=status,
        )

    module.exit_json(changed=True, status=status)


if __name__ == '__main__':
    main()
