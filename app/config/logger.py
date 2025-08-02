import logging

from app.config.settings import settings

logging.basicConfig(
    level=getattr(logging, settings.log_level),
    format="%(asctime)s %(levelname)s:%(name)s [Th-%(thread)d] %(message)s",
)

logger = logging.getLogger(__name__)
