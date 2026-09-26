import sys, json
from client import AudioPacketJitterResilienceBuffer

def main():
    print("Testing AudioPacketJitterResilienceBuffer...")
    buf = AudioPacketJitterResilienceBuffer()
    res = buf.run_benchmark_jitter_simulation()
    print(json.dumps(res, indent=2))
    assert res["benchmark_status"] == "PASSED"
    assert res["plc_triggered"] is True, "PLC should have triggered for missing frame 102"
    print("All Audio Packet Jitter Buffer tests passed successfully!")

if __name__ == "__main__":
    main()
