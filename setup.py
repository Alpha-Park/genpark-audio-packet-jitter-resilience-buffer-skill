from setuptools import setup, find_packages

setup(
    name="genpark-audio-jitter-buffer",
    version="1.0.0",
    description="Adaptive WebRTC audio packet jitter buffer and packet loss concealment (PLC) engine.",
    long_description=open("README.md", encoding="utf-8").read() if __import__("os").path.exists("README.md") else "Adaptive WebRTC audio packet jitter buffer and packet loss concealment (PLC) engine.",
    long_description_content_type="text/markdown",
    author="GenPark AI Engineering",
    author_email="engineering@genpark.ai",
    url="https://github.com/Alpha-Park/genpark-audio-packet-jitter-resilience-buffer-skill",
    py_modules=["client", "mcp_server"],
    python_requires=">=3.9",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
