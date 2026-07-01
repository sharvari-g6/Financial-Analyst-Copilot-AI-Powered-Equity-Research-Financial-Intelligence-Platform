from loguru import logger

logger.add(
    "backend.log",
    rotation="10 MB",
    retention="10 days"
)