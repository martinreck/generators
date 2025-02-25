# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# EVSE Bricklet communication config

from generators.configs.commonconstants import THRESHOLD_OPTION_CONSTANT_GROUP
from generators.configs.commonconstants import add_callback_value_function
from generators.configs.openhab_commonconfig import *

com = {
    'author': 'Olaf Lüke <olaf@tinkerforge.com>',
    'api_version': [2, 0, 2],
    'category': 'Bricklet',
    'device_identifier': 2159,
    'name': 'EVSE',
    'display_name': 'EVSE',
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': 'TBD',
        'de': 'TBD'
    },
    'released': False,
    'documented': False,
    'discontinued': False,
    'features': [
        'device',
        'comcu_bricklet',
        'bricklet_get_identity'
    ],
    'constant_groups': [],
    'packets': [],
    'examples': []
}

com['constant_groups'].append({
'name': 'IEC61851 State',
'type': 'uint8',
'constants': [('A', 0),
              ('B', 1),
              ('C', 2),
              ('D', 3),
              ('EF', 4)]
})

com['constant_groups'].append({
'name': 'LED State',
'type': 'uint8',
'constants': [('Off', 0),
              ('On', 1),
              ('Blinking', 2),
              ('Flicker', 3),
              ('Breathing', 4)]
})

com['constant_groups'].append({
'name': 'Vehicle State',
'type': 'uint8',
'constants': [('Not Connected', 0),
              ('Connected', 1),
              ('Charging', 2),
              ('Error', 3)]
})

com['constant_groups'].append({
'name': 'Contactor State',
'type': 'uint8',
'constants': [('AC1 NLive AC2 NLive', 0),
              ('AC1 Live AC2 NLive', 1),
              ('AC1 NLive AC2 Live', 2),
              ('AC1 Live AC2 Live', 3)]
})

com['constant_groups'].append({
'name': 'Lock State',
'type': 'uint8',
'constants': [('Init', 0),
              ('Open', 1),
              ('Closing', 2),
              ('Close', 3),
              ('Opening', 4),
              ('Error', 5)]
})

com['constant_groups'].append({
'name': 'Error State',
'type': 'uint8',
'constants': [('OK', 0),
              ('Switch', 2),
              ('Calibration', 3),
              ('Contactor', 4),
              ('Communication', 5)]
})

com['constant_groups'].append({
'name': 'Jumper Configuration',
'type': 'uint8',
'constants': [('6A', 0),
              ('10A', 1),
              ('13A', 2),
              ('16A', 3),
              ('20A', 4),
              ('25A', 5),
              ('32A', 6),
              ('Software', 7),
              ('Unconfigured', 8)]
})

com['constant_groups'].append({
'name': 'Charge Release',
'type': 'uint8',
'constants': [('Automatic', 0),
              ('Manual', 1),
              ('Deactivated', 2),
              ('Managed', 3)]
})

com['packets'].append({
'type': 'function',
'name': 'Get State',
'elements': [('IEC61851 State', 'uint8', 1, 'out', {'constant_group': 'IEC61851 State'}),
             ('Vehicle State', 'uint8', 1, 'out', {'constant_group': 'Vehicle State'}),
             ('Contactor State', 'uint8', 1, 'out', {'constant_group': 'Contactor State'}),
             ('Contactor Error', 'uint8', 1, 'out'),
             ('Charge Release', 'uint8', 1, 'out', {'constant_group': 'Charge Release'}),
             ('Allowed Charging Current', 'uint16', 1, 'out'),
             ('Error State', 'uint8', 1, 'out', {'constant_group': 'Error State'}),
             ('Lock State', 'uint8', 1, 'out', {'constant_group': 'Lock State'}),
             ('Time Since State Change', 'uint32', 1, 'out', {'scale': (1, 1000), 'unit': 'Second'}),
             ('Uptime', 'uint32', 1, 'out', {'scale': (1, 1000), 'unit': 'Second'})],
'since_firmware': [2, 0, 5],
'doc': ['bf', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Hardware Configuration',
'elements': [('Jumper Configuration', 'uint8', 1, 'out', {'constant_group': 'Jumper Configuration'}),
             ('Has Lock Switch', 'bool', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Low Level State',
'elements': [('Low Level Mode Enabled', 'bool', 1, 'out'),
             ('LED State', 'uint8', 1, 'out', {'constant_group': 'LED State'}),
             ('CP PWM Duty Cycle', 'uint16', 1, 'out'),
             ('ADC Values', 'uint16', 2, 'out'),
             ('Voltages', 'int16', 3, 'out', {'scale': (1, 1000), 'unit': 'Volt'}), # pe-cp, pe-pp, high voltage pe-cp
             ('Resistances', 'uint32', 2, 'out', {'unit': 'Ohm'}),
             ('GPIO', 'bool', 5, 'out'), # XMC_GPIO_GetInput(EVSE_INPUT_GP_PIN) | (XMC_GPIO_GetInput(EVSE_OUTPUT_GP_PIN) << 1) | (XMC_GPIO_GetInput(EVSE_MOTOR_INPUT_SWITCH_PIN) << 2) | (XMC_GPIO_GetInput(EVSE_RELAY_PIN) << 3) | (XMC_GPIO_GetInput(EVSE_MOTOR_FAULT_PIN) << 4)
],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Max Charging Current',
'elements': [('Max Current', 'uint16', 1, 'in')], # mA (default 32A?)
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Max Charging Current',
'elements': [('Max Current Configured', 'uint16', 1, 'out'),     # mA
             ('Max Current Incoming Cable', 'uint16', 1, 'out'), # mA
             ('Max Current Outgoing Cable', 'uint16', 1, 'out'), # mA
             ('Max Current Managed', 'uint16', 1, 'out')],       # mA
'since_firmware': [2, 0, 6],
'doc': ['bf', {
'en':
"""
* Max Current Configured -> set with :func:`Set Max Charging Current`
* Max Current Incoming Cable -> set with jumper on EVSE
* Max Current Outgoing Cable -> set with resistor between PP/PE (if fixed cable is used)

TODO
""",
'de':
"""
TODO
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Calibrate',
'elements': [('State', 'uint8', 1, 'in'),       # 1, 2
             ('Password', 'uint32', 1, 'in'),   # state 1 = 0x0BB03201, state 2 = 0x0BB03202
             ('Value', 'int32', 1, 'in'),       # high voltage, offset
             ('Success', 'bool', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Start Charging',
'elements': [],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Stop Charging',
'elements': [],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Charging Autostart',
'elements': [('Autostart', 'bool', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Charging Autostart',
'elements': [('Autostart', 'bool', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Managed',
'elements': [('Managed', 'bool', 1, 'out')],
'since_firmware': [2, 0, 6],
'doc': ['bf', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Managed',
'elements': [('Managed', 'bool', 1, 'in'),
             ('Password', 'uint32', 1, 'in')], # To enable: 0x00363702 (mgmt on), to disable: 0x036370FF (mgmt off)
'since_firmware': [2, 0, 6],
'doc': ['bf', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Managed Current',
'elements': [('Current', 'uint16', 1, 'in')], # mA (default 0A)
'since_firmware': [2, 0, 6],
'doc': ['bf', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})


com['packets'].append({
'type': 'function',
'name': 'Get User Calibration',
'elements': [('User Calibration Active', 'bool', 1, 'out'),
             ('Voltage Diff', 'int16', 1, 'out'),
             ('Voltage Mul', 'int16', 1, 'out'),
             ('Voltage Div', 'int16', 1, 'out'),
             ('Resistance 2700', 'int16', 1, 'out'),
             ('Resistance 880', 'int16', 14, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set User Calibration',
'elements': [('Password', 'uint32', 1, 'in'), # 0xCA11B4A0
             ('User Calibration Active', 'bool', 1, 'in'),
             ('Voltage Diff', 'int16', 1, 'in'),
             ('Voltage Mul', 'int16', 1, 'in'),
             ('Voltage Div', 'int16', 1, 'in'),
             ('Resistance 2700', 'int16', 1, 'in'),
             ('Resistance 880', 'int16', 14, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
TODO
""",
'de':
"""
TODO
"""
}]
})
