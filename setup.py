import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AgentLogin",
    version="3.0.0",
    author="taozhengquan",
    author_email="1483906080@qq.com",
    description="A project for Third party login",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhengquantao/ProxyLogin",
    # packages=setuptools.find_packages(),
    packages=['AgentLogin'],
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)