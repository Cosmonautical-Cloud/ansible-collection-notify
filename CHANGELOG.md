# Changelog

All notable changes to this project are documented here. Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); this project follows [semantic versioning](https://semver.org/).

## [0.0.1] - 2026-09-30

### Added

- Initial release: the `discord` module, extracted out of Nomadintosh's generic `roles/notify` role (the production one it actually used — a separate, drifted, unused `tasks/notify.yml` duplicate was left behind and deleted rather than carried over) so it can be shared with Nomaduntu without a circular collection dependency on Nomadable. Built as a Python module (`plugins/modules/discord.py`), called directly as `cosmonautical.notify.discord` on a task, rather than a role — a webhook's `id`/`token`, `message`, and `username` are all passed straight as module args, and `token` is marked `no_log` at the argument level so it's redacted regardless of task-level `no_log`. Left room for other notification services (Slack, Telegram, Matrix, etc.) as their own modules later.
