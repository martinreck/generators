#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
OpenHAB ZIP Generator
Copyright (C) 2019-2020 Erik Fleckstein <erik@tinkerforge.com>

generate_openhab_zip.py: Generator for OpenHAB ZIP

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with this program; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.
"""

import sys

if sys.hexversion < 0x3040000:
    print('Python >= 3.4 required')
    sys.exit(1)

import os
import shutil
import importlib.util
import importlib.machinery

def create_generators_module():
    generators_dir = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]

    if sys.hexversion < 0x3050000:
        generators_module = importlib.machinery.SourceFileLoader('generators', os.path.join(generators_dir, '__init__.py')).load_module()
    else:
        generators_spec = importlib.util.spec_from_file_location('generators', os.path.join(generators_dir, '__init__.py'))
        generators_module = importlib.util.module_from_spec(generators_spec)

        generators_spec.loader.exec_module(generators_module)

    sys.modules['generators'] = generators_module

if 'generators' not in sys.modules:
    create_generators_module()

from generators import common
from generators.openhab import openhab_common

class OpenHABZipGenerator(openhab_common.OpenHABGeneratorTrait, common.ZipGenerator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.tmp_dir        = self.get_zip_dir()
        self.generation_dir = os.path.join(self.tmp_dir, 'generated')
        self.tmp_oh_dir     = os.path.join(self.generation_dir, 'src', 'main', 'java', 'org', 'openhab', 'binding', 'tinkerforge', 'internal', 'device')
        self.tmp_xml_dir    = os.path.join(self.generation_dir, 'src', 'main', 'resources', 'ESH-INF', 'thing')

        #TODO: use os.path.join
        self.relative_file_dests = {
            'about.html':   '.',
            'NOTICE':       '.',
            'pom.xml':      '.',
            'README.md':    '.',
            'changelog.txt':'.',
            'readme.txt':   '.',

            'feature.xml':                  './src/main/feature',
            'binding.xml':                  './src/main/resources/ESH-INF/binding',
            'tinkerforge_xx_XX.properties': './src/main/resources/ESH-INF/i18n',

            'BrickDaemonDiscoveryService.java': './src/main/java/org/openhab/binding/tinkerforge/discovery',

            'TinkerforgeHandlerFactory.java':               './src/main/java/org/openhab/binding/tinkerforge/internal',
            'TinkerforgeChannelTypeProvider.java':          './src/main/java/org/openhab/binding/tinkerforge/internal',
            'TinkerforgeConfigDescriptionProvider.java':    './src/main/java/org/openhab/binding/tinkerforge/internal',
            'TinkerforgeThingTypeProvider.java':            './src/main/java/org/openhab/binding/tinkerforge/internal',
            'TinkerforgeFirmwareProvider.java':             './src/main/java/org/openhab/binding/tinkerforge/internal',
            'FirmwareInfo.java':                            './src/main/java/org/openhab/binding/tinkerforge/internal',
            'Utils.java':                                   './src/main/java/org/openhab/binding/tinkerforge/internal',

            'BrickDaemonHandler.java':                      './src/main/java/org/openhab/binding/tinkerforge/internal/handler',
            'ReachabilityResult.java':                      './src/main/java/org/openhab/binding/tinkerforge/internal/handler',
            'BrickletOutdoorWeatherHandler.java':           './src/main/java/org/openhab/binding/tinkerforge/internal/handler',
            'BrickletOutdoorWeatherSensorHandler.java':     './src/main/java/org/openhab/binding/tinkerforge/internal/handler',
            'BrickletOutdoorWeatherStationHandler.java':    './src/main/java/org/openhab/binding/tinkerforge/internal/handler',
            'BrickletRemoteSwitchHandler.java':             './src/main/java/org/openhab/binding/tinkerforge/internal/handler',
            'CheckedConsumer.java':                         './src/main/java/org/openhab/binding/tinkerforge/internal/handler',
            'RemoteSwitch.java':                            './src/main/java/org/openhab/binding/tinkerforge/internal/handler',
            'BrickletRemoteSwitchWrapperWrapper.java':      './src/main/java/org/openhab/binding/tinkerforge/internal/handler',
            'BrickletRemoteSwitchV2WrapperWrapper.java':    './src/main/java/org/openhab/binding/tinkerforge/internal/handler',
            'Task.java':                                    './src/main/java/org/openhab/binding/tinkerforge/internal/handler',
            'RemoteSwitchDeviceHandler.java':               './src/main/java/org/openhab/binding/tinkerforge/internal/handler',
            'DeviceHandler.java':                           './src/main/java/org/openhab/binding/tinkerforge/internal/handler',

            'BrickDaemonWrapper.java':        './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'BrickDaemonConfig.java':         './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'DefaultActions.java':            './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'DeviceWrapper.java':             './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'SetterRefresh.java':             './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'ListenerReg.java':               './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'DeviceInfo.java':                './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'Helper.java':                    './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'CoMCUFlashable.java':            './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'FlashUtils.java':                './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'StandardFlashable.java':         './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'TngFlashable.java':              './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'StandardFlashHost.java':         './src/main/java/org/openhab/binding/tinkerforge/internal/device',

            'BrickletOutdoorWeatherSensor.java':        './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'BrickletOutdoorWeatherSensorConfig.java':  './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'BrickletOutdoorWeatherStation.java':       './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'BrickletOutdoorWeatherStationConfig.java': './src/main/java/org/openhab/binding/tinkerforge/internal/device',

            'RemoteSocketTypeA.java':       './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'RemoteSocketTypeAConfig.java': './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'RemoteSocketTypeB.java':       './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'RemoteSocketTypeBConfig.java': './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'RemoteSocketTypeC.java':       './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'RemoteSocketTypeCConfig.java': './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'RemoteDimmerTypeB.java':       './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            'RemoteDimmerTypeBConfig.java': './src/main/java/org/openhab/binding/tinkerforge/internal/device',

            os.path.join(self.get_bindings_dir(), 'DeviceWrapperFactory.java'): './src/main/java/org/openhab/binding/tinkerforge/internal/device',
            os.path.join(self.get_bindings_dir(), 'TinkerforgeBindingConstants.java'): './src/main/java/org/openhab/binding/tinkerforge/internal'
        }
        self.file_dests = {os.path.join(self.get_bindings_dir(), '..', k): os.path.normpath(os.path.join(self.generation_dir, *v.split('/'))) for k, v in self.relative_file_dests.items()}

        self.tmp_source_dir                   = os.path.join(self.generation_dir, 'source')
        self.tmp_source_meta_inf_services_dir = os.path.join(self.tmp_source_dir, 'META-INF', 'services')
        self.tmp_examples_dir                 = os.path.join(self.generation_dir, 'examples')

    def prepare(self):
        if self.get_config_name().space != 'Tinkerforge':
            print('### custom configs not supported yet')
            return

        super().prepare()

        os.makedirs(self.generation_dir)

        for directory in self.file_dests.values():
            if not os.path.exists(directory):
                os.makedirs(directory)

    def generate(self, device):
        if self.get_config_name().space != 'Tinkerforge':
            return
        if not device.is_released():
            return

        for file in os.listdir(self.get_bindings_dir()):
            if device.get_category().camel+device.get_name().camel in file and (file.endswith('Config.java') or file.endswith('Actions.java') or file.endswith('Wrapper.java')):
                shutil.copy(os.path.join(self.get_bindings_dir(), file), self.tmp_oh_dir)

    def finish(self):
        if self.get_config_name().space != 'Tinkerforge':
            return

        root_dir = self.get_root_dir()

        for src, dst in self.file_dests.items():
            shutil.copy(src, dst)

        binding_dir = os.path.join(self.get_bindings_dir(), '..', 'openhab2-addons', 'bundles', 'org.openhab.binding.tinkerforge')

        if os.path.isdir(binding_dir):
            print("Binding directory exists from last run, skipping clone of openhab2-addons repo.")
            with common.ChangedDirectory(os.path.join(self.get_bindings_dir(), '..', 'openhab2-addons')):
                common.execute(['git', 'stash'])
            with common.ChangedDirectory(os.path.join(self.get_bindings_dir(), '..', 'openhab2-addons')):
                common.execute(['git', 'pull'])
            with common.ChangedDirectory(os.path.join(self.get_bindings_dir(), '..', 'openhab2-addons')):
                common.execute(['git', 'stash', 'pop'])
        else:
            with common.ChangedDirectory(os.path.join(self.get_bindings_dir(), '..')):
                common.execute(['git', 'clone', '-b', '2.5.x', 'https://github.com/openhab/openhab2-addons', '--depth=1'])

            to_patch = os.path.join(self.get_bindings_dir(), '..', 'openhab2-addons', 'bom', 'openhab-addons', 'pom.xml')
            common.specialize_template(to_patch, to_patch, {'</dependencies>': """
        <dependency>
        <groupId>org.openhab.addons.bundles</groupId>
        <artifactId>org.openhab.binding.tinkerforge</artifactId>
        <version>${project.version}</version>
        </dependency>
    </dependencies>"""})

            to_patch = os.path.join(self.get_bindings_dir(), '..', 'openhab2-addons', 'bundles', 'pom.xml')
            common.specialize_template(to_patch, to_patch, {'</modules>': """
        <module>org.openhab.binding.tinkerforge</module>
    </modules>"""})

        common.recreate_dir(binding_dir)

        for f in [k for (k, v) in self.relative_file_dests.items() if v == '.']:
            shutil.copy(os.path.join(self.generation_dir, f), os.path.join(binding_dir, f))
        shutil.copytree(os.path.join(self.generation_dir, 'src'), os.path.join(binding_dir, 'src'))

        with common.ChangedDirectory(binding_dir):
            common.execute(['mvn', 'spotless:apply', '-Dorg.slf4j.simpleLogger.defaultLogLevel=WARN'])
            common.execute(['mvn', 'clean', 'install', '-Dorg.slf4j.simpleLogger.defaultLogLevel=WARN'])

        # Beta stuff
        zip_dir = os.path.join(self.tmp_dir, 'zip')
        os.makedirs(zip_dir)

        for f in ['changelog.txt', 'readme_de.txt', 'readme_en.txt']:
            shutil.copy(os.path.join(self.get_bindings_dir(), '..', 'beta', f), zip_dir)
        shutil.copytree(os.path.join(binding_dir, 'src'), os.path.join(zip_dir, 'org.openhab.binding.tinkerforge', 'src'))
        shutil.copy(os.path.join(binding_dir, 'target', 'org.openhab.binding.tinkerforge-2.5.9-SNAPSHOT.jar'), zip_dir)

        java_bindings = os.path.join(self.get_root_dir(), 'tinkerforge-2.1.26.jar')

        if not os.path.exists(java_bindings):
            try:
                from urllib.request import urlretrieve
                downloaded_file, _ = urlretrieve('https://search.maven.org/remotecontent?filepath=com/tinkerforge/tinkerforge/2.1.26/tinkerforge-2.1.26.jar')
                shutil.copy(downloaded_file, java_bindings)
            except Exception as e:
                raise common.GeneratorError("Failed to download java bindings.") from e

        shutil.copy(java_bindings, zip_dir)

        self.create_zip_file(zip_dir)

def generate(root_dir, language, internal):
    common.generate(root_dir, language, internal, OpenHABZipGenerator)

if __name__ == '__main__':
    args = common.dockerize('openhab', __file__, add_internal_argument=True)

    generate(os.getcwd(), 'en', args.internal)
