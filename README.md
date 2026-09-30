# notify

An Ansible collection that posts webhook notifications (Discord/Slack-compatible) for deployment events.

## Scope

This collection holds a single role, `notify`, extracted out of [Nomadintosh](https://github.com/anultravioletaurora/Nomadintosh) so it can be shared without duplicating it into [Nomaduntu](https://github.com/anultravioletaurora/nomaduntu) too. It has no playbook of its own — consumers `include_role`/`import_role` it by its fully-qualified name from their own playbooks.

## Requirements

- Ansible 2.15+
- No external collection dependencies — the role only uses `ansible.builtin` modules.

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
- name: Send notification
  ansible.builtin.include_role:
    name: cosmonautical.notify.notify
  vars:
    notify_webhook_message: "Deployment completed on {{ inventory_hostname }}."
    notifications: "{{ my_notifications_vault_var }}"
```

See [`roles/notify/README.md`](roles/notify/README.md) for the full variable reference.

## Consumers

- [Nomadintosh](https://github.com/anultravioletaurora/Nomadintosh) — `roles/nomad/tasks/install.yml`, `roles/software_update/tasks/main.yml`
- [Nomaduntu](https://github.com/anultravioletaurora/nomaduntu) — depends on this collection; no call site wired in yet
- [Nomadable](https://github.com/anultravioletaurora/Nomadable) — depends on this collection so it's available to both child playbooks it composes

## Versioning

Follows [semantic versioning](https://semver.org/); see [CHANGELOG.md](CHANGELOG.md), format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
