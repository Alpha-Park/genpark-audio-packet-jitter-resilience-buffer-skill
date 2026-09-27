import unittest
from genpark_jitter_buffer import AudioPacketJitterResilienceBuffer as Client

class CoreTests(unittest.TestCase):

    def test_order_loss_and_jitter(self):
        c = Client()
        c.ingest_packet(100, 1000, 320, 1020)
        c.ingest_packet(102, 1040, 320, 1076)
        self.assertEqual(c.get_jitter_telemetry()["estimated_jitter_ms"], 1.0)
        self.assertEqual(c.extract_playout_frame()["seq_num"], 100)
        self.assertTrue(c.extract_playout_frame()["is_synthetic_plc"])
        self.assertEqual(c.extract_playout_frame()["seq_num"], 102)
    def test_out_of_order(self):
        c = Client()
        for seq in [10,12,11]: c.ingest_packet(seq,seq*20,320,seq*20+5)
        self.assertEqual([c.extract_playout_frame()["seq_num"] for _ in range(3)], [10,11,12])
    def test_empty_and_bounded(self):
        c = Client(max_buffer_frames=2)
        self.assertEqual(c.extract_playout_frame()["status"], "EMPTY")
        for seq in range(8): c.ingest_packet(seq,seq*20,320,seq*20)
        self.assertLessEqual(c.get_jitter_telemetry()["current_buffer_frames"],2)

if __name__ == "__main__": unittest.main()
