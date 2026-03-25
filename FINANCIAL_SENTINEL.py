# 🛡️ Financial Sentinel: The Anti-Abuse Logic
# "Wealth is a Tool, Not a Weapon."

class FinancialSentinel:
    def evaluate_withdrawal(self, user_profile, amount, intent):
        """
        Prevents 'Capitalist Spikes' from causing self-destruction.
        """
        literacy_score = user_profile.get_literacy_rating()
        habit_history = user_profile.get_habit_resonance()

        if intent == "HIGH_FRICTION_PURCHASE": # e.g., harmful substances/exploitation
            return "ADVICE: This action lowers your Global Glow. Consult your Caretaker."
        
        if amount > user_profile.safe_limit and literacy_score < 0.8:
            return "ADVICE: Logic-Handshake required from Parent/Mentor. Financial Literacy training recommended."

        return "ACCESS_GRANTED: Resonance maintained."
