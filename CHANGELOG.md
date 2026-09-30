# Changelog

All notable changes to this project are documented here. Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); this project follows [semantic versioning](https://semver.org/).

## [0.0.1] - 2026-09-30

### Added

- Initial release: `discord` role, extracted out of Nomadintosh's generic `roles/notify` (the production one it actually used — a separate, drifted, unused `tasks/notify.yml` duplicate was left behind and deleted rather than carried over) so it can be shared with Nomaduntu without a circular collection dependency on Nomadable. Renamed from a generic `notify` role to a service-scoped `discord` role (variables reprefixed `discord_*`, matching the ansible-lint role-name-prefix convention the sibling repos already enforce) to leave room for other notification services (Slack, Telegram, Matrix, etc.) as their own roles later.
