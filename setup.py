from distutils.core import setup
import py2exe
setup(
	console=[{
		'script': 'main.py',
        'icon_resources': [(0, 'droplet.ico')],
		'dest_base': 'droplet'
	}]
)
