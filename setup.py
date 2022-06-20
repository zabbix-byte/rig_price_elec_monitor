from setuptools import setup
from setuptools import find_packages

setup(
    name='rig_price_elec_monitor',
    packages=find_packages(),
    version='0.1.0',
    description='RIG DOWN, OPTIMIZE YOUR RIG!',
    author='Vasile Ichim Ovidiu | zabbix | zabbix@ztrunk.space',
    install_requires=['requests'],
    entry_points = {
        'console_scripts': [
            'rig_price_elec_monitor = scripts.__main__:main'
        ]
    }
)