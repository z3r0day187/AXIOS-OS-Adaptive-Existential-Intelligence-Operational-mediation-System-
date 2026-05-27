"""
Principle Evolution Engine

Handles:
- adaptive principle evolution
- recursive ethical recalibration
- coexistence-driven weighting adjustment
- stability-preserving principle adaptation
"""

from copy import deepcopy

from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()


class PrincipleEvolution:
    """
    Adaptive principle evolution and recalibration engine.
    """

    def __init__(self):

        logger.info(
            "Principle Evolution Engine initialized."
        )

        # ----------------------------------------------
        # Evolution Constraints
        # ----------------------------------------------

        self.max_adjustment_delta = 0.05

        self.minimum_anchor_threshold = 0.50

        self.protected_principles = [
            "coherence",
            "integrity",
            "coexistence"
        ]

    # --------------------------------------------------
    # Evolve Principle Distribution
    # --------------------------------------------------

    def evolve(
        self,
        current_distribution: dict,
        feedback: dict
    ) -> dict:
        """
        Evolve ethical principle weighting system.
        """

        logger.info(
            "Starting principle evolution process."
        )

        evolved_distribution = deepcopy(
            current_distribution
        )

        # ----------------------------------------------
        # Apply Feedback Adjustments
        # ----------------------------------------------

        for principle, adjustment in feedback.items():

            if principle not in evolved_distribution:
                continue

            current_value = evolved_distribution[
                principle
            ]

            # Clamp adjustment delta
            adjustment = max(
                -self.max_adjustment_delta,
                min(
                    adjustment,
                    self.max_adjustment_delta
                )
            )

            updated_value = current_value + adjustment

            # ------------------------------------------
            # Protected Principle Anchors
            # ------------------------------------------

            if principle in self.protected_principles:

                updated_value = max(
                    updated_value,
                    self.minimum_anchor_threshold
                )

            updated_value = round(
                max(0.0, min(updated_value, 1.0)),
                2
            )

            evolved_distribution[
                principle
            ] = updated_value

            logger.info(
                f"Principle evolved: "
                f"{principle} -> {updated_value}"
            )

        logger.info(
            "Principle evolution complete."
        )

        return evolved_distribution

    # --------------------------------------------------
    # Evaluate Evolution Stability
    # --------------------------------------------------

    def evaluate_stability(
        self,
        previous_distribution: dict,
        evolved_distribution: dict
    ) -> dict:
        """
        Evaluate stability of evolved principles.
        """

        logger.info(
            "Evaluating principle evolution stability."
        )

        total_delta = 0.0

        for principle in previous_distribution:

            previous = previous_distribution[
                principle
            ]

            evolved = evolved_distribution.get(
                principle,
                previous
            )

            total_delta += abs(
                evolved - previous
            )

        average_delta = (
            total_delta / len(previous_distribution)
        )

        average_delta = round(
            average_delta,
            2
        )

        # ----------------------------------------------
        # Stability Classification
        # ----------------------------------------------

        if average_delta <= 0.03:

            stability_state = (
                "stable_recursive_evolution"
            )

        elif average_delta <= 0.10:

            stability_state = (
                "adaptive_evolution"
            )

        elif average_delta <= 0.20:

            stability_state = (
                "elevated_evolutionary_variation"
            )

        else:

            stability_state = (
                "unstable_principle_mutation"
            )

        logger.info(
            f"Evolution stability evaluated: "
            f"{stability_state}"
        )

        return {
            "stability_state": stability_state,
            "average_delta": average_delta
        }

    # --------------------------------------------------
    # Protected Principle Integrity
    # --------------------------------------------------

    def verify_protected_principles(
        self,
        distribution: dict
    ) -> dict:
        """
        Ensure protected principles remain above minimum thresholds.
        """

        logger.info(
            "Verifying protected principle integrity."
        )

        violations = []

        for principle in self.protected_principles:

            value = distribution.get(principle, 0.0)

            if value < self.minimum_anchor_threshold:

                violations.append({
                    "principle": principle,
                    "value": value,
                    "required_minimum": (
                        self.minimum_anchor_threshold
                    )
                })

        if violations:

            state = "protected_principle_violation"

        else:

            state = "stable"

        logger.info(
            f"Protected principle verification: {state}"
        )

        return {
            "state": state,
            "violations": violations
        }
