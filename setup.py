from setuptools import setup

setup(
    name='avocado',
    version='0.1',
    description='Photometric Classification of Astronomical Transients and '
    'Variables With Biased Spectroscopic Samples',
    url='http://github.com/kboone/avocado',
    author='Kyle Boone',
    author_email='kboone@berkeley.edu',
    license='BSD',
    packages=['avocado'],
    data_files=[('avocado', ['avocado/avocado_settings.json'])]

)
