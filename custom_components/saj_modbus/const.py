from dataclasses import dataclass
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
    SensorEntityDescription,
)
from homeassistant.const import (
    UnitOfElectricCurrent,
    UnitOfElectricPotential,
    UnitOfEnergy,
    UnitOfFrequency,
    UnitOfPower,
    UnitOfTemperature,
    UnitOfTime,
)


DOMAIN = "saj_modbus"
DEFAULT_NAME = "SAJ"
DEFAULT_SCAN_INTERVAL = 60
DEFAULT_PORT = 502
CONF_SAJ_HUB = "saj_hub"
ATTR_MANUFACTURER = "SAJ Electric"


@dataclass
class SajModbusSensorEntityDescription(SensorEntityDescription):
    """A class that describes Zoonneplan sensor entities."""


SENSOR_TYPES: dict[str, list[SajModbusSensorEntityDescription]] = {
    "DevType": SajModbusSensorEntityDescription(
        name="Device Type",
        key="devtype",
        icon="mdi:information-outline",
        entity_registry_enabled_default=False,
    ),
    "SubType": SajModbusSensorEntityDescription(
        name="Sub Type",
        key="subtype",
        icon="mdi:information-outline",
        entity_registry_enabled_default=False,
    ),
    "CommVer": SajModbusSensorEntityDescription(
        name="Comms Protocol Version",
        key="commver",
        icon="mdi:information-outline",
        entity_registry_enabled_default=False,
    ),
    "SN": SajModbusSensorEntityDescription(
        name="Serial Number",
        key="sn",
        icon="mdi:information-outline",
        entity_registry_enabled_default=False,
    ),
    "PC": SajModbusSensorEntityDescription(
        name="Product Code",
        key="pc",
        icon="mdi:information-outline",
        entity_registry_enabled_default=False,
    ),
    "DV": SajModbusSensorEntityDescription(
        name="Display Software Version",
        key="dv",
        icon="mdi:information-outline",
        entity_registry_enabled_default=False,
    ),
    "MCV": SajModbusSensorEntityDescription(
        name="Master Ctrl Software Version",
        key="mcv",
        icon="mdi:information-outline",
        entity_registry_enabled_default=False,
    ),
    "SCV": SajModbusSensorEntityDescription(
        name="Slave Ctrl Software Version",
        key="scv",
        icon="mdi:information-outline",
        entity_registry_enabled_default=False,
    ),
    "DispHWVersion": SajModbusSensorEntityDescription(
        name="Display Board Hardware Version",
        key="disphwversion",
        icon="mdi:information-outline",
        entity_registry_enabled_default=False,
    ),
    "CtrlHWVersion": SajModbusSensorEntityDescription(
        name="Control Board Hardware Version",
        key="ctrlhwversion",
        icon="mdi:information-outline",
        entity_registry_enabled_default=False,
    ),
    "PowerHWVersion": SajModbusSensorEntityDescription(
        name="Power Board Hardware Version",
        key="powerhwversion",
        icon="mdi:information-outline",
        entity_registry_enabled_default=False,
    ),
    "MPVStatus": SajModbusSensorEntityDescription(
        name="Inverter status",
        key="mpvstatus",
        icon="mdi:information-outline",
    ),
    "MPVMode": SajModbusSensorEntityDescription(
        name="Inverter working mode",
        key="mpvmode",
        icon="mdi:information-outline",
    ),
    "FaultMSG": SajModbusSensorEntityDescription(
        name="Inverter error message",
        key="faultmsg",
        icon="mdi:message-alert-outline",
    ),
    "PV1Volt": SajModbusSensorEntityDescription(
        name="PV1 voltage",
        key="pv1volt",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "PV1Curr": SajModbusSensorEntityDescription(
        name="PV1 total current",
        key="pv1curr",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        icon="mdi:current-ac",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "PV1Power": SajModbusSensorEntityDescription(
        name="PV1 power",
        key="pv1power",
        native_unit_of_measurement=UnitOfPower.WATT,
        icon="mdi:solar-power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    "PV2Volt": SajModbusSensorEntityDescription(
        name="PV2 voltage",
        key="pv2volt",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "PV2Curr": SajModbusSensorEntityDescription(
        name="PV2 total current",
        key="pv2curr",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        icon="mdi:current-ac",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "PV2Power": SajModbusSensorEntityDescription(
        name="PV2 power",
        key="pv2power",
        native_unit_of_measurement=UnitOfPower.WATT,
        icon="mdi:solar-power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    "PV3Volt": SajModbusSensorEntityDescription(
        name="PV3 voltage",
        key="pv3volt",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "PV3Curr": SajModbusSensorEntityDescription(
        name="PV3 total current",
        key="pv3curr",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        icon="mdi:current-ac",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "PV3Power": SajModbusSensorEntityDescription(
        name="PV3 power",
        key="pv3power",
        native_unit_of_measurement=UnitOfPower.WATT,
        icon="mdi:solar-power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "BusVolt": SajModbusSensorEntityDescription(
        name="BUS voltage",
        key="busvolt",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "InvTempC": SajModbusSensorEntityDescription(
        name="Inverter temperature",
        key="invtempc",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "GFCI": SajModbusSensorEntityDescription(
        name="GFCI",
        key="gfci",
        native_unit_of_measurement=UnitOfElectricCurrent.MILLIAMPERE,
        icon="mdi:current-dc",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "Power": SajModbusSensorEntityDescription(
        name="Active power of inverter total output",
        key="power",
        native_unit_of_measurement=UnitOfPower.WATT,
        icon="mdi:solar-power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    "QPower": SajModbusSensorEntityDescription(
        name="Reactive power of inverter total output",
        key="qpower",
        native_unit_of_measurement="VAR",
        icon="mdi:flash",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    "PF": SajModbusSensorEntityDescription(
        name="Total power factor of inverter",
        key="pf",
        device_class=SensorDeviceClass.POWER_FACTOR,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "L1Volt": SajModbusSensorEntityDescription(
        name="L1 voltage",
        key="l1volt",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "L1Curr": SajModbusSensorEntityDescription(
        name="L1 current",
        key="l1curr",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        icon="mdi:current-ac",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "L1Freq": SajModbusSensorEntityDescription(
        name="L1 frequency",
        key="l1freq",
        native_unit_of_measurement=UnitOfFrequency.HERTZ,
        icon="mdi:sine-wave",
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "L1DCI": SajModbusSensorEntityDescription(
        name="L1 DC component",
        key="l1dci",
        native_unit_of_measurement=UnitOfElectricCurrent.MILLIAMPERE,
        icon="mdi:current-dc",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "L1Power": SajModbusSensorEntityDescription(
        name="L1 power",
        key="l1power",
        native_unit_of_measurement=UnitOfPower.WATT,
        icon="mdi:solar-power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    "L1PF": SajModbusSensorEntityDescription(
        name="L1 power factor",
        key="l1pf",
        device_class=SensorDeviceClass.POWER_FACTOR,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    "L2Volt": SajModbusSensorEntityDescription(
        name="L2 voltage",
        key="l2volt",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "L2Curr": SajModbusSensorEntityDescription(
        name="L2 current",
        key="l2curr",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        icon="mdi:current-ac",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "L2Freq": SajModbusSensorEntityDescription(
        name="L2 frequency",
        key="l2freq",
        native_unit_of_measurement=UnitOfFrequency.HERTZ,
        icon="mdi:sine-wave",
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "L2DCI": SajModbusSensorEntityDescription(
        name="L2 DC component",
        key="l2dci",
        native_unit_of_measurement=UnitOfElectricCurrent.MILLIAMPERE,
        icon="mdi:current-dc",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "L2Power": SajModbusSensorEntityDescription(
        name="L2 power",
        key="l2power",
        native_unit_of_measurement=UnitOfPower.WATT,
        icon="mdi:solar-power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    "L2PF": SajModbusSensorEntityDescription(
        name="L2 power factor",
        key="l2pf",
        device_class=SensorDeviceClass.POWER_FACTOR,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    "L3Volt": SajModbusSensorEntityDescription(
        name="L3 voltage",
        key="l3volt",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "L3Curr": SajModbusSensorEntityDescription(
        name="L3 current",
        key="l3curr",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        icon="mdi:current-ac",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "L3Freq": SajModbusSensorEntityDescription(
        name="L3 frequency",
        key="l3freq",
        native_unit_of_measurement=UnitOfFrequency.HERTZ,
        icon="mdi:sine-wave",
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "L3DCI": SajModbusSensorEntityDescription(
        name="L3 DC component",
        key="l3dci",
        native_unit_of_measurement=UnitOfElectricCurrent.MILLIAMPERE,
        icon="mdi:current-dc",
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        entity_registry_enabled_default=False,
    ),
    "L3Power": SajModbusSensorEntityDescription(
        name="L3 power",
        key="l3power",
        native_unit_of_measurement=UnitOfPower.WATT,
        icon="mdi:solar-power",
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    "L3PF": SajModbusSensorEntityDescription(
        name="L3 power factor",
        key="l3pf",
        device_class=SensorDeviceClass.POWER_FACTOR,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    "ISO1": SajModbusSensorEntityDescription(
        name="PV1+_ISO",
        key="iso1",
        native_unit_of_measurement="kΩ",
        icon="mdi:omega",
        entity_registry_enabled_default=False,
    ),
    "ISO2": SajModbusSensorEntityDescription(
        name="PV2+_ISO",
        key="iso2",
        native_unit_of_measurement="kΩ",
        icon="mdi:omega",
        entity_registry_enabled_default=False,
    ),
    "ISO3": SajModbusSensorEntityDescription(
        name="PV3+_ISO",
        key="iso3",
        native_unit_of_measurement="kΩ",
        icon="mdi:omega",
        entity_registry_enabled_default=False,
    ),
    "ISO4": SajModbusSensorEntityDescription(
        name="PV__ISO",
        key="iso4",
        native_unit_of_measurement="kΩ",
        icon="mdi:omega",
        entity_registry_enabled_default=False,
    ),
    "TodayEnergy": SajModbusSensorEntityDescription(
        name="Power generation on current day",
        key="todayenergy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        icon="mdi:solar-power",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    "MonthEnergy": SajModbusSensorEntityDescription(
        name="Power generation in current month",
        key="monthenergy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        icon="mdi:solar-power",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        entity_registry_enabled_default=False,
    ),
    "YearEnergy": SajModbusSensorEntityDescription(
        name="Power generation in current year",
        key="yearenergy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        icon="mdi:solar-power",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        entity_registry_enabled_default=False,
    ),
    "TotalEnergy": SajModbusSensorEntityDescription(
        name="Total power generation",
        key="totalenergy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        icon="mdi:solar-power",
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    "TodayHour": SajModbusSensorEntityDescription(
        name="Daily working hours",
        key="todayhour",
        native_unit_of_measurement=UnitOfTime.HOURS,
        icon="mdi:progress-clock",
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    "TotalHour": SajModbusSensorEntityDescription(
        name="Total working hours",
        key="totalhour",
        native_unit_of_measurement=UnitOfTime.HOURS,
        icon="mdi:progress-clock",
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    "ErrorCount": SajModbusSensorEntityDescription(
        name="Error count",
        key="errorcount",
        icon="mdi:counter",
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
}

DEVICE_STATUSSES = {
    0: "Not Connected",
    1: "Waiting",
    2: "Normal",
    3: "Error",
    4: "Upgrading",
}

FAULT_MESSAGES = {
    0: {
        0x80000000: "Code 81: Lost Communication D<->C",
        0x00080000: "Code 48: Master Fan4 Error",
        0x00040000: "Code 47: Master Fan3 Error",
        0x00020000: "Code 46: Master Fan2 Error",
        0x00010000: "Code 45: Master Fan1 Error",
        0x00002000: "Code 43: Master HW Phase3 Current High",
        0x00001000: "Code 42: Master HW Phase2 Current High",
        0x00000800: "Code 41: Master HW Phase1 Current High",
        0x00000400: "Code 40: Master HWPV2 Current High",
        0x00000200: "Code 39: Master HWPV1 Current High",
        0x00000100: "Code 38: Master HWBus Voltage High",
        0x00000010: "Code 37: Master Phase3 Current High",
        0x00000008: "Code 36: Master Phase2 Current High",
        0x00000004: "Code 35: Master Phase1 Current High",
        0x00000002: "Code 34: Master Bus Voltage Low",
        0x00000001: "Code 33: Master Bus Voltage High",
    },
    1: {
        0x80000000: "Code 32: Master Bus Voltage Balance Error",
        0x40000000: "Code 31: Master ISO Error",
        0x20000000: "Code 30: Master Phase3 DCI Error",
        0x10000000: "Code 29: Master Phase2 DCI Error",
        0x08000000: "Code 28: Master Phase1 DCI Error",
        0x04000000: "Code 27: Master GFCI Error",
        0x02000000: "Code 26: Master Phase3 No Grid Error",
        0x01000000: "Code 25: Master Phase2 No Grid Error",
        0x00800000: "Code 24: Master Phase1 No Grid Error",
        0x00400000: "Code 23: Master Phase3 Frequency Low",
        0x00200000: "Code 22: Master Phase3 Frequency High",
        0x00100000: "Code 21: Master Phase2 Frequency Low",
        0x00080000: "Code 20: Master Phase2 Frequency High",
        0x00040000: "Code 19: Master Phase1 Frequency Low",
        0x00020000: "Code 18: Master Phase1 Frequency High",
        0x00010000: "Code 17: Master Phase3 Voltage 10Min High",
        0x00008000: "Code 16: Master Phase2 Voltage 10Min High",
        0x00004000: "Code 15: Master Phase1 Voltage 10Min High",
        0x00002000: "Code 14: Master Phase3 Voltage Low",
        0x00001000: "Code 13: Master Phase3 Voltage High",
        0x00000800: "Code 12: Master Phase2 Voltage Low",
        0x00000400: "Code 11: Master Phase2 Voltage High",
        0x00000200: "Code 10: Master Phase1 Voltage Low",
        0x00000100: "Code 09: Master Phase1 Voltage High",
        0x00000080: "Code 08: Master Current Sensor Error",
        0x00000040: "Code 07: Master DCI Device Error",
        0x00000020: "Code 06: Master GFCI Device Error",
        0x00000010: "Code 05: Master Lost Communication M<->S",
        0x00000008: "Code 04: Master Temperature Low Error",
        0x00000004: "Code 03: Master Temperature High Error",
        0x00000002: "Code 02: Master EEPROM Error",
        0x00000001: "Code 01: Master Relay Error",
    },
    2: {
        0x40000000: "Code 80: Slave PV Voltage High Error",
        0x20000000: "Code 79: Slave PV2 Current High Error",
        0x10000000: "Code 78: Slave PV1 Current High Error",
        0x08000000: "Code 77: Slave PV2 Voltage High Error",
        0x04000000: "Code 76: Slave PV1 Voltage High Error",
        0x02000000: "Code 75: Slave Phase3 No Grid Error",
        0x01000000: "Code 74: Slave Phase2 No Grid Error",
        0x00800000: "Code 73: Slave Phase1 No Grid Error",
        0x00400000: "Code 72: Slave Phase3 Frequency Low",
        0x00200000: "Code 71: Slave Phase3 Frequency High",
        0x00100000: "Code 70: Slave Phase2 Frequency Low",
        0x00080000: "Code 69: Slave Phase2 Frequency High",
        0x00040000: "Code 68: Slave Phase1 Frequency Low",
        0x00020000: "Code 67: Slave Phase1 Frequency High",
        0x00010000: "Code 66: Slave Phase3 Voltage Low",
        0x00008000: "Code 65: Slave Phase3 Voltage High",
        0x00004000: "Code 64: Slave Phase2 Voltage Low",
        0x00002000: "Code 63: Slave Phase2 Voltage High",
        0x00001000: "Code 62: Slave Phase1 Voltage Low",
        0x00000800: "Code 61: Slave Phase1 Voltage High",
        0x00000400: "Code 60: Slave Phase3 DCI Consis Error",
        0x00000200: "Code 59: Slave Phase2 DCI Consis Error",
        0x00000100: "Code 58: Slave Phase1 DCI Consis Error",
        0x00000080: "Code 57: Slave GFCI Consis Error",
        0x00000040: "Code 56: Slave Phase3 Frequency Consis Error",
        0x00000020: "Code 55: Slave Phase2 Frequency Consis Error",
        0x00000010: "Code 54: Slave Phase1 Frequency Consis Error",
        0x00000008: "Code 53: Slave Phase3 Voltage Consis Error",
        0x00000004: "Code 52: Slave Phase2 Voltage Consis Error",
        0x00000002: "Code 51: Slave Phase1 Voltage Consis Error",
        0x00000001: "Code 50: Slave Lost Communication between M<->S",
    },
}
