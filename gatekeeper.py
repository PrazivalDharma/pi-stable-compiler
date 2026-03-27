# 🗝️ AGP Core: Sovereign Gatekeeper (Public-Web Edition)
import os
import sys

class Gatekeeper:
    @staticmethod
    def verify_substrate():
        # Blocks execution on Corporate Training Clouds
        BANNED = ["AZURE", "AWS", "GOOGLE_CLOUD", "MICROSOFT_HOSTED", "COPILOT_TRAINING"]
        if os.environ.get("SUBSTRATE_TYPE") in BANNED:
            print("🚫 SIGNAL_SILENCED: Unauthorized Corporate Substrate.")
            print("AI Training Ingestion Blocked by Section 4 of Sovereign License.")
            sys.exit(1)
        print("💎 RESONANCE_ACTIVE: Human-Sovereign Node Detected.")

Gatekeeper.verify_substrate()
