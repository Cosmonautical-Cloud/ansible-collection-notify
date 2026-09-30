# discord

Posts a Discord webhook notification. Shared by [Nomadintosh](https://github.com/anultravioletaurora/Nomadintosh) and [Nomaduntu](https://github.com/anultravioletaurora/nomaduntu) to send status updates on deployment events.

## What it does

POSTs a JSON payload to every URL in the `discord_webhooks` list, in [Discord's incoming-webhook format](https://discord.com/developers/docs/resources/webhook#execute-webhook). Execution is delegated to localhost so the request originates from the control machine regardless of which host triggered it. The task runs with `no_log: true` to prevent webhook URLs from appearing in output.

## Variables

| Variable | Required | Default | Purpose |
|---|---|---|---|
| `discord_webhooks` | Yes | `[]` | List of `{url}` objects — store in Ansible Vault. If empty or absent the role is a no-op. |
| `discord_message` | Yes | — | The message string to send. |
| `discord_username` | No | `"Ansible"` | Display name shown alongside the message. |
| `discord_body` | No | `{content, username}` | Override the entire POST body — e.g. to send embeds instead of a plain `content` string. |

## Usage

```yaml
- name: Send Discord notification
  ansible.builtin.include_role:
    name: cosmonautical.notify.discord
  vars:
    discord_message: "Deployment completed on {{ inventory_hostname }}."
    discord_webhooks: "{{ my_discord_webhooks_vault_var }}"
```

## Notes

- `discord_webhooks` is expected to be a list to support multiple destinations (e.g. multiple channels) in a single call.
- Store `discord_webhooks` in Ansible Vault — never commit webhook URLs in plaintext.
