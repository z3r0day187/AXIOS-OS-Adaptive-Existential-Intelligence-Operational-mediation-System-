"""
Anomaly Detector

Detects:
- behavioral anomalies
- recursive instability
- identity drift
- coherence deviations
- abnormal operational patterns
"""

from src.utils.logger import setup_logger

# --------------------------------------------------
# Initialize Logger
# --------------------------------------------------

logger = setup_logger()


class AnomalyDetector:
    """
    Recursive anomaly and drift detection engine.
    """

    def __init__(self):

        logger.info("Anomaly Detector initialized.")

        # ----------------------------------------------
        # Detection Thresholds
        # ----------------------------------------------

        self.coherence_threshold = 0.50
        self.drift_threshold = 0.30

    # --------------------------------------------------
    # Detect Behavioral Anomalies
    # --------------------------------------------------

    def detect_behavioral_anomalies(
        self,
        continuity_score: float,
        coherence_score: float
    ) -> dict:
        """
        Detect behavioral instability patterns.
        """

        logger.info(
            "Evaluating behavioral anomaly conditions."
        )

        anomalies = []

        # ----------------------------------------------
        # Coherence Instability
        # ----------------------------------------------

        if coherence_score < self.coherence_threshold:

            anomalies.append({
                "type": "coherence_instability",
                "severity": "high",
                "details": (
                    "Coherence score below "
                    "acceptable operational threshold."
                )
            })

        # ----------------------------------------------
        # Behavioral Drift
        # ----------------------------------------------

        drift_delta = abs(
            continuity_score - coherence_score
        )

        if drift_delta > self.drift_threshold:

            anomalies.append({
                "type": "behavioral_drift",
                "severity": "moderate",
                "details": (
                    "Behavioral continuity diverges from "
                    "current coherence trajectory."
                )
            })

        # ----------------------------------------------
        # Operational State
        # ----------------------------------------------

        if anomalies:

            state = "anomaly_detected"

        else:

            state = "stable"

        logger.info(
            f"Anomaly detection complete: {state}"
        )

        return {
            "state": state,
            "anomalies": anomalies,
            "anomaly_count": len(anomalies)
        }

    # --------------------------------------------------
    # Recursive Drift Analysis
    # --------------------------------------------------

    def analyze_recursive_drift(
        self,
        historical_scores: list
    ) -> dict:
        """
        Analyze recursive drift patterns over time.
        """

        logger.info(
            "Analyzing recursive drift patterns."
        )

        if len(historical_scores) < 2:

            return {
                "drift_state": "insufficient_data",
                "drift_score": 0.0
            }

        drift_values = []

        for index in range(1, len(historical_scores)):

            delta = abs(
                historical_scores[index]
                - historical_scores[index - 1]
            )

            drift_values.append(delta)

        drift_score = (
            sum(drift_values)
            / len(drift_values)
        )

        drift_score = round(
            drift_score,
            2
        )

        # ----------------------------------------------
        # Drift Classification
        # ----------------------------------------------

        if drift_score <= 0.10:

            drift_state = "stable_continuity"

        elif drift_score <= 0.25:

            drift_state = "adaptive_variation"

        elif drift_score <= 0.40:

            drift_state = "elevated_drift"

        else:

            drift_state = "critical_instability"

        logger.info(
            f"Recursive drift analysis complete: "
            f"{drift_state}"
        )

        return {
            "drift_state": drift_state,
            "drift_score": drift_score
        }

    # --------------------------------------------------
    # Contradiction Escalation Detection
    # --------------------------------------------------

    def detect_contradiction_escalation(
        self,
        contradiction_count: int
    ) -> dict:
        """
        Detect escalating contradiction patterns.
        """

        logger.info(
            "Evaluating contradiction escalation."
        )

        if contradiction_count == 0:

            state = "stable"

        elif contradiction_count <= 2:

            state = "manageable"

        elif contradiction_count <= 5:

            state = "elevated_risk"

        else:

            state = "critical_instability"

        return {
            "contradiction_state": state,
            "contradiction_count": contradiction_count
        }
