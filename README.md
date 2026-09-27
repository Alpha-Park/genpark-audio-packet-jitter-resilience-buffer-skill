# genpark-jitter-buffer

Packet ordering simulation and inter-arrival jitter telemetry.

This is a **packet metadata simulation**, not a WebRTC implementation or audio codec. Timestamps must already be converted to milliseconds, and sequence numbers must be monotonically extended (no RTP wraparound). Missing packets produce markers, not synthesized audio. The caller controls playout timing; target_delay_ms is telemetry, not an enforced timer.

## Install from the GitHub release

Python 3.9 or newer. The library and stdio MCP server have no runtime dependencies.

```sh
python -m pip install https://github.com/Alpha-Park/genpark-audio-packet-jitter-resilience-buffer-skill/releases/download/v1.0.1/genpark_jitter_buffer-1.0.1-py3-none-any.whl
```

PyPI publication is pending account setup. The intended PyPI project is `genpark-jitter-buffer`;
do not assume `pip install genpark-jitter-buffer` is available until the project is published.

## Python usage

```python
from genpark_jitter_buffer import AudioPacketJitterResilienceBuffer
client = AudioPacketJitterResilienceBuffer()
print(client.run_benchmark_jitter_simulation())
```

## MCP stdio configuration

After installing the wheel, configure your MCP client with the installed command:

```json
{
  "mcpServers": {
    "genpark-jitter-buffer": {
      "command": "genpark-jitter-buffer",
      "args": []
    }
  }
}
```

If the command is not on PATH, use its absolute path or `python -m genpark_jitter_buffer`
with the same interpreter where you installed the wheel.
The GitHub release also contains a `.mcpb` bundle for clients supporting desktop extensions.
That bundle requires a Python 3.9+ interpreter on PATH; it bundles the server source.

Available tools: `ingest_packet`, `extract_playout_frame`, `get_jitter_telemetry`, `run_benchmark_jitter_simulation`.
`tools/list` returns required arguments and JSON schemas.
Each MCP process holds its own state. Benchmark tools use isolated instances.

## Development

```sh
python -m unittest discover -s tests
python -m pip install mcp
python tests/check_mcp.py
python -m pip install build twine
python -m build
python -m twine check dist/*
```

`python mcp_server.py --test` runs the deterministic example; it is not a protocol conformance test.
The MCP client check exercises initialize, tools/list, tools/call and ping over stdio.

## Distribution

GitHub source and release artifacts are the primary distribution until PyPI is configured.
Registry submissions are tracked separately; a manifest is not proof of registry acceptance.
See [PUBLISHING.md](PUBLISHING.md) for the repeatable PyPI workflow.

MIT license. Maintained by [GenPark](https://genpark.ai).

<!-- mcp-name: io.github.Alpha-Park/genpark-jitter-buffer -->
