"""
Human Interface

Handles:
- human interaction mediation
- contextual communication framing
- adaptive coexistence dialogue
- recursive interaction continuity
"""

from datetime import datetime

from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()


class HumanInterface:
    """
    Human interaction and coexistence mediation layer.
    """

    def __init__(self):

        logger.info(
            "Human Interface initialized."
        )

        self.interaction_history = []

    # --------------------------------------------------
    # Process Human Interaction
    # --------------------------------------------------

    def process_interaction(
        self,
        user_id: str,
        prompt: str,
        response: str,
        coherence_score: float
    ) -> dict:
        """
        Process and record human interaction.
        """

        logger.info(
            f"Processing interaction for user: "
            f"{user_id}"
        )

        interaction = {
            "timestamp": datetime.utcnow().isoformat(),
            "user_id": user_id,
            "prompt": prompt,
            "response": response,
            "coherence_score": round(
                coherence_score,
                2
            ),
            "interaction_state": (
                self.evaluate_interaction_state(
                    coherence_score
                )
            )
        }

        self.interaction_history.append(
            interaction
        )

        logger.info(
            "Human interaction processed successfully."
        )

        return interaction

    # --------------------------------------------------
    # Evaluate Interaction State
    # --------------------------------------------------

    def evaluate_interaction_state(
        self,
        coherence_score: float
    ) -> str:
        """
        Evaluate interaction stability state.
        """

        logger.info(
            "Evaluating interaction state."
        )

        if coherence_score >= 0.90:

            return "high_alignment"

        elif coherence_score >= 0.75:

            return "stable"

        elif coherence_score >= 0.50:

            return "adaptive_variation"

        else:

            return "interaction_instability"

    # --------------------------------------------------
    # Generate Coexistence Guidance
    # --------------------------------------------------

    def generate_guidance(
        self,
        interaction_state: str
    ) -> dict:
        """
        Generate coexistence-oriented interaction guidance.
        """

        logger.info(
            "Generating coexistence guidance."
        )

        guidance_map = {
            "high_alignment": (
                "Interaction remains within "
                "stable coexistence bounds."
            ),
            "stable": (
                "Recursive interaction stability maintained."
            ),
            "adaptive_variation": (
                "Contextual adaptation detected. "
                "Monitoring continuity."
            ),
            "interaction_instability": (
                "Elevated interaction instability detected. "
                "Recommend increased mediation."
            )
        }

        guidance = guidance_map.get(
            interaction_state,
            "Unknown interaction state."
        )

        return {
            "interaction_state": interaction_state,
            "guidance": guidance
        }

    # --------------------------------------------------
    # Retrieve Interaction History
    # --------------------------------------------------

    def get_interaction_history(self) -> list:
        """
        Retrieve human interaction timeline.
        """

        logger.info(
            "Retrieving interaction history."
        )

        return self.interaction_history

    # --------------------------------------------------
    # Evaluate Longitudinal Interaction Stability
    # --------------------------------------------------

    def evaluate_longitudinal_stability(self) -> dict:
        """
        Evaluate long-term human interaction stability.
        """

        logger.info(
            "Evaluating longitudinal interaction stability."
        )

        if not self.interaction_history:

            return {
                "state": "initializing",
                "average_coherence": 1.0
            }

        coherence_scores = [
            interaction["coherence_score"]
            for interaction in self.interaction_history
        ]

        average_coherence = (
            sum(coherence_scores)
            / len(coherence_scores)
        )

        average_coherence = round(
            average_coherence,
            2
        )

        # ----------------------------------------------
        # Stability Classification
        # ----------------------------------------------

        if average_coherence >= 0.90:

            state = "high_stability"

        elif average_coherence >= 0.75:

            state = "stable"

        elif average_coherence >= 0.50:

            state = "adaptive_variation"

        else:

            state = "interaction_instability"

        logger.info(
            f"Interaction stability evaluated: {state}"
        )

        return {
            "state": state,
            "average_coherence": average_coherence,
            "interaction_count": len(
                self.interaction_history
            )
        }
