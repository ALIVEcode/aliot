import pathlib

from setuptools import find_packages, setup
import aliot

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

if __name__ == "__main__":
    setup(name='aliot-py',
          author='Mathis Laroche, Enric Soldevila',
          author_email="alivecode.developers@gmail.com",
          version=aliot.__version__,
          description='Aliot-py is the python implementation of the Aliot library, an'
                      ' IOT library made to work with the ALIVEIoT ecosystem (see https://alivecode.ca/iot)',
          long_description=README,
          long_description_content_type="text/markdown",
          classifiers=[
              "Programming Language :: Python :: 3",
              "Programming Language :: Python :: 3.10",
          ],
          url="https://github.com/ALIVEcode/aliot.git",
          packages=find_packages(
              include=['aliot.', 'aliot.*']),
          include_package_data=True,
          python_requires=">=3.10",
          install_requires=["websocket-client",
                            "rich",
                            "click",
                            "requests"
                            ],
          setup_requires="setuptools",
          entry_points={
              "console_scripts": ["aliot = aliot.core._cli.aliot_cli:main"]
          },
          )
