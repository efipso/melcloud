[![](https://img.shields.io/github/release/efipso/melcloud/all.svg?style=for-the-badge)](https://github.com/efipso/melcloud/releases)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/hacs/integration)
[![](https://img.shields.io/github/license/efipso/melcloud?style=for-the-badge)](LICENSE)
[![](https://img.shields.io/badge/MAINTAINER-%40efipso-red?style=for-the-badge)](https://github.com/efipso)
[![](https://img.shields.io/badge/COMMUNITY-FORUM-success?style=for-the-badge)](https://community.home-assistant.io)

# Home Assistant custom integration for MELCloud devices

## Description
A full featured Homeassistant custom component to drive MELCloud devices.

This custom component is based on the native Home Assistant [MELCloud component](https://github.com/home-assistant/core/tree/dev/homeassistant/components/melcloud) v2024.8.1 and on the same underlying [PyMelCloud library](https://github.com/vilppuvuorinen/pymelcloud) v2.5.9.

It's done basically for my own use.

## Custom component additional features
The base code is native Home Assistant [MELCloud component](https://github.com/home-assistant/core/tree/dev/homeassistant/components/melcloud), with the following modifications:

1. [PyMelCloud library](https://github.com/vilppuvuorinen/pymelcloud) are incorporated to this integration, as repository has been archieved and I want to add some modifications to it.
1. Added Outside temperature sensor for ATA Devices (only work when Outside Unit is working)
1. Added WIFI Signal Strength sensor
