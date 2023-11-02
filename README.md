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

#### Install package locally and try the package run.py
```bash
python pip install .
python run.py
```

#### Check the package
```bash
twine check dist/*
```

#### Publish package on Test PyPI
Remember to setup the .pypirc file with the credentials.
```bash
twine upload -r testpypi dist/*
```

#### Install package from testpypi
```bash
python -m pip install --index-url https://test.pypi.org/simple/ hello-world-generator
```

#### Publish package on PyPI
Remember to setup the .pypirc file with the credentials.
```bash
twine upload  dist/*
```