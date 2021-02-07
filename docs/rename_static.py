import os

print('\nRenaming all folders beginning with an underscore...')

if os.path.isdir(r'build\html\_static'):
	os.rename(r'build\html\_static', r'build\html\static')
if os.path.isdir(r'build\html\_sources'):
	os.rename(r'build\html\_sources', r'build\html\sources')

for root, dirs, files in os.walk(r'build\html'):
	for file in files:
		if file.endswith('html'):
			print('  Updating', file)
			filename = os.path.join(root, file)

			with open(filename, 'r') as f:
				htmlcontents = f.read()

			newcontents = htmlcontents.replace('_static/', 'static/').replace('_sources/', 'sources/')

			with open(filename, 'w') as f:
				f.write(newcontents)

print('Updated all files\n')
			