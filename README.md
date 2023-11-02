# hello-world-generator
Test how to create a python package and publishing it on PyPI.

The package implements a simple function that prints "Hello World!".

#### Test
```bash
pytest
```

#### Lint & Format project
```bash
pylint ./app/hello_world_generator
black ./app/hello_world_generator
```

#### Create distribution
```bash
python setup.py bdist_wheel sdist
```

#### Install package locally
```bash
python pip install .
```