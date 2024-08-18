"""Support for MelCloud device sensors."""

from __future__ import annotations

import dataclasses
from collections.abc import Callable
from typing import Any

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry

from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import MelCloudDevice
from .const import DOMAIN
from .pymelcloud import DEVICE_TYPE_ATA, DEVICE_TYPE_ATW


@dataclasses.dataclass(frozen=True, kw_only=True)
class MelcloudBinarySensorEntityDescription(BinarySensorEntityDescription):
    """Describes Melcloud binary sensor entity."""

    value_fn: Callable[[Any], float]
    enabled: Callable[[Any], bool]


ATA_BINARY_SENSORS: tuple[MelcloudBinarySensorEntityDescription, ...] = (
    MelcloudBinarySensorEntityDescription(
        key="error_state",
        translation_key="error_state",
        device_class=BinarySensorDeviceClass.PROBLEM,
        value_fn=lambda x: x.device.has_error,
        enabled=lambda x: True,
    ),
)
ATW_BINARY_SENSORS: tuple[MelcloudBinarySensorEntityDescription, ...] = (
    MelcloudBinarySensorEntityDescription(
        key="error_state",
        translation_key="error_state",
        device_class=BinarySensorDeviceClass.PROBLEM,
        value_fn=lambda x: x.device.has_error,
        enabled=lambda x: True,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up MELCloud device binary sensors based on config_entry."""
    mel_devices = hass.data[DOMAIN].get(entry.entry_id)

    entities: list[MelDeviceBinarySensor] = [
        MelDeviceBinarySensor(mel_device, description)
        for description in ATA_BINARY_SENSORS
        for mel_device in mel_devices[DEVICE_TYPE_ATA]
        if description.enabled(mel_device)
    ] + [
        MelDeviceBinarySensor(mel_device, description)
        for description in ATW_BINARY_SENSORS
        for mel_device in mel_devices[DEVICE_TYPE_ATW]
        if description.enabled(mel_device)
    ]

    async_add_entities(entities, True)


class MelDeviceBinarySensor(BinarySensorEntity):
    """Representation of a Binary Sensor."""

    entity_description: MelcloudBinarySensorEntityDescription
    _attr_has_entity_name = True

    def __init__(
        self,
        api: MelCloudDevice,
        description: MelcloudBinarySensorEntityDescription,
    ) -> None:
        """Initialize the binary sensor."""
        self._api = api
        self.entity_description = description

        self._attr_unique_id = f"{api.device.serial}-{api.device.mac}-{description.key}"
        self._attr_device_info = api.device_info

    @property
    def is_on(self) -> bool | False:
        """Return the state of the binary sensor."""
        return self.entity_description.value_fn(self._api)

    async def async_update(self) -> None:
        """Retrieve latest state."""
        await self._api.async_update()
