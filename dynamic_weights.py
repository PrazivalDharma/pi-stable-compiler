# 📐 Pi-Stable Compiler: Dynamic Amplitude Shifter
# Logic: Amplifies the weight of 3.0-Resonance members for high-impact pulses.

class AmplitudeShifter:
    def calculate_vote_weight(self, user_merit, proposal_tier):
        """
        Determines if a 'Key Decision Maker' gets their 1:3 
        amplification based on the Social Impact Tier.
        """
        # Tier I: Inconsequential / Figurehead stuff
        if proposal_tier == "SOCIAL_BASELINE":
            return 1.0 
        
        # Tier III: High Social Impact (Infrastructure, Global Buffer)
        if proposal_tier == "HIGH_IMPACT":
            if user_merit >= 3.0:
                return 3.0 # The 1:3 Weighting
            elif user_merit >= 2.0:
                return 1.5
        
        return 1.0 # Default fallback
