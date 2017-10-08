import glob
import random
import shutil
from pathlib import Path

SECRET_KEY_SYMBOLS = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'


def generate_secret_key():
    return ''.join(
        random.SystemRandom().choice(SECRET_KEY_SYMBOLS) for i in range(50)
    )


def replace_string_recursively(old, new):
    for file in Path().glob('**/*'):
        if file.is_file():
            with file.open() as f:
                contents = f.read()
            if old not in contents:
                continue

            contents = contents.replace(old, new)
            with file.open('w') as f:
                f.write(contents)


def remove_recursively(pattern):
    for file in Path().glob('**/' + glob.escape(pattern)):
        if file.is_file():
            file.unlink()
        else:
            shutil.rmtree(file)


secret_key = generate_secret_key()
replace_string_recursively('[[ hooks.secret ]]', secret_key)
remove_recursively('[[ hooks.remove ]]')
