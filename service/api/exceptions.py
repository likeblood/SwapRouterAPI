import typing as tp
from http import HTTPStatus


class AppException(Exception):
    def __init__(
        self,
        status_code: int,
        error_key: str,
        error_message: str = "",
        error_loc: tp.Optional[tp.Sequence[str]] = None,
    ) -> None:
        self.error_key = error_key
        self.error_message = error_message
        self.error_loc = error_loc
        self.status_code = status_code
        super().__init__()


class AuthorizationError(AppException):
    def __init__(
        self,
        status_code: int = HTTPStatus.UNAUTHORIZED,
        error_key: str = "authorization_error",
        error_message: str = "Authorization failed",
        error_loc: tp.Optional[tp.Sequence[str]] = None,
     ) -> None:
        super().__init__(status_code, error_key, error_message, error_loc)
