"""Custom exceptions for Aigram."""

from typing import Optional


class AigramError(Exception):
    """Base exception for Aigram."""
    
    def __init__(self, message: str, details: Optional[str] = None) -> None:
        self.message = message
        self.details = details
        super().__init__(self.message)
    
    def __str__(self) -> str:
        if self.details:
            return f"{self.message}: {self.details}"
        return self.message


class ConfigurationError(AigramError):
    """Raised when there are configuration-related issues."""
    pass


class TelegramError(AigramError):
    """Raised when there are Telegram API-related issues."""
    pass


class AIProcessorError(AigramError):
    """Raised when there are AI processing-related issues."""
    pass


class CacheError(AigramError):
    """Raised when there are cache-related issues."""
    pass


class ValidationError(AigramError):
    """Raised when validation fails."""
    pass
