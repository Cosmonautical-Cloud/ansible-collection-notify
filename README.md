# notify

An Ansible collection of per-service roles for posting deployment notifications.

## Scope

One role per notification service — `discord` today, with room to add `slack`/`telegram`/`matrix`/etc. as needed. Extracted out of [Nomadintosh](https://github.com/anultravioletaurora/Nomadintosh)'s generic `notify` role so it can be shared without duplicating it into [Nomaduntu](https://github.com/anultravioletaurora/nomaduntu) too. It has no playbook of its own — consumers `include_role`/`import_role` a role by its fully-qualified name from their own playbooks.

## Requirements

- Ansible 2.15+
- No external collection dependencies — every role only uses `ansible.builtin` modules.

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
- name: Send Discord notification
  ansible.builtin.include_role:
    name: cosmonautical.notify.discord
  vars:
    discord_message: "Deployment completed on {{ inventory_hostname }}."
    discord_webhooks: "{{ my_discord_webhooks_vault_var }}"
```

See each role's own README for its full variable reference:

- [`roles/discord/README.md`](roles/discord/README.md)

## Consumers

- [Nomadintosh](https://github.com/anultravioletaurora/Nomadintosh) — `roles/nomad/tasks/install.yml`, `roles/software_update/tasks/main.yml`
- [Nomaduntu](https://github.com/anultravioletaurora/nomaduntu) — depends on this collection; no call site wired in yet
- [Nomadable](https://github.com/anultravioletaurora/Nomadable) — depends on this collection so it's available to both child playbooks it composes

## Versioning

Follows [semantic versioning](https://semver.org/); see [CHANGELOG.md](CHANGELOG.md), format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
