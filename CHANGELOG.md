# Changelog

All notable changes to this project are documented here. Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); this project follows [semantic versioning](https://semver.org/).

## [0.0.1] - 2026-09-30

### Added

- Initial release. `notify` role extracted verbatim out of Nomadintosh's `roles/notify` (the production one it actually used — a separate, drifted, unused `tasks/notify.yml` duplicate was left behind and deleted rather than carried over) so it can be shared with Nomaduntu without a circular collection dependency on Nomadable.
