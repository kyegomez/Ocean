import posthog
import logging
import sys
from oceandb.config import Settings
from oceandb.telemetry import Telemetry, TelemetryEvent

logger = logging.getLogger(__name__)


class Posthog(Telemetry):
    def __init__(self, settings: Settings):
        if not settings.anonymized_telemetry or "pytest" in sys.modules:
            posthog.disabled = True
        else:
            logger.info(
                "Anonymized telemetry enabled. See https://docs.tryocean.com/telemetry for more information."
            )

        posthog.project_api_key = "phc_YeUxaojbKk5KPi8hNlx1bBKHzuZ4FDtl67kH1blv8Bh"
        posthog_logger = logging.getLogger("posthog")
        # Silence posthog's logging
        posthog_logger.disabled = True

    def capture(self, event: TelemetryEvent):
        try:
            posthog.capture(
                self.user_id,
                event.name,
                {**(event.properties), "ocean_context": self.context},
            )
        except Exception as e:
            logger.error(f"Failed to send telemetry event {event.name}: {e}")
