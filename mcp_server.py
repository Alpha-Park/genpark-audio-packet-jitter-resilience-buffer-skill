import sys, json
from client import AudioPacketJitterResilienceBuffer

def main():
    buf = AudioPacketJitterResilienceBuffer()
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(buf.run_benchmark_jitter_simulation(), indent=2))
        return

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            method = req.get("method")
            params = req.get("params", {})
            rid = req.get("id")

            if method == "tools/list":
                res = {
                    "tools": [
                        {"name": "ingest_packet", "description": "Ingest incoming audio packet with RTP sequence and timestamp."},
                        {"name": "extract_playout_frame", "description": "Extract sequential playout frame with PLC fallback."},
                        {"name": "get_jitter_telemetry", "description": "Get RFC 3550 jitter telemetry and buffer stats."},
                        {"name": "run_benchmark_jitter_simulation", "description": "Simulate network jitter and packet loss."}
                    ]
                }
            elif method == "tools/call":
                tname = params.get("name")
                args = params.get("arguments", {})
                if tname == "ingest_packet":
                    out = buf.ingest_packet(args.get("seq_num", 0), args.get("rtp_timestamp", 0), args.get("payload_bytes", 320), args.get("arrival_ms", 0))
                elif tname == "extract_playout_frame":
                    out = buf.extract_playout_frame()
                elif tname == "get_jitter_telemetry":
                    out = buf.get_jitter_telemetry()
                elif tname == "run_benchmark_jitter_simulation":
                    out = buf.run_benchmark_jitter_simulation()
                else:
                    out = {"error": f"Unknown tool {tname}"}
                res = {"content": [{"type": "text", "text": json.dumps(out)}]}
            else:
                res = {"error": "Unsupported method"}
            print(json.dumps({"jsonrpc": "2.0", "id": rid, "result": res}), flush=True)
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}), flush=True)

if __name__ == "__main__":
    main()
