# notify

An Ansible collection of per-service modules for posting deployment notifications.

## Scope

One module per notification service — `discord` today, with room to add `slack`/`telegram`/`matrix`/etc. as needed. Extracted out of [Nomadintosh](https://github.com/anultravioletaurora/Nomadintosh)'s generic `notify` role so it can be shared without duplicating it into [Nomaduntu](https://github.com/anultravioletaurora/nomaduntu) too.

## Requirements

- Ansible 2.15+
- No external collection dependencies — every module only uses `ansible.module_utils` from `ansible-core`.

## Installation

```zsh
ansible-galaxy collection install cosmonautical.notify
```

Or pin it in a consumer's `collections/requirements.yml`:

```yaml
collections:
  - name: cosmonautical.notify
    version: ">=0.0.1"
```

## Usage

```yaml
- name: Send a Discord notification
  cosmonautical.notify.discord:
    id: "{{ discord_webhook_id }}"
    token: "{{ discord_webhook_token }}"
    message: "Deployment completed on {{ inventory_hostname }}."
  no_log: true
```

Send to a vaulted list of webhooks with `loop:`:

```yaml
- name: Send to every webhook in a vaulted list
  cosmonautical.notify.discord:
    id: "{{ item.id }}"
    token: "{{ item.token }}"
    message: "Deployment completed on {{ inventory_hostname }}."
  loop: "{{ discord_webhooks }}"
  delegate_to: localhost
  no_log: true
```

See each module's own documentation for its full option reference (`ansible-doc cosmonautical.notify.discord`), or [`plugins/modules/discord.py`](plugins/modules/discord.py).

## Consumers

- [Nomadintosh](https://github.com/anultravioletaurora/Nomadintosh) — `roles/nomad/tasks/install.yml`, `roles/software_update/tasks/main.yml`
- [Nomaduntu](https://github.com/anultravioletaurora/nomaduntu) — depends on this collection; no call site wired in yet
- [Nomadable](https://github.com/anultravioletaurora/Nomadable) — depends on this collection so it's available to both child playbooks it composes

## Versioning

Follows [semantic versioning](https://semver.org/); see [CHANGELOG.md](CHANGELOG.md), format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
