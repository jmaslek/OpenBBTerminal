from typing import Optional

from pydantic import BaseModel, Field

from openbb_sdk_core.app.hub.model.hub_session import HubSession


class Profile(BaseModel):
    active: Optional[bool] = Field(default=None)
    username: Optional[str] = Field(default=None)
    password_hash: Optional[str] = Field(default=None)
    hub_session: Optional[HubSession] = Field(default=None)

    class Config:
        validate_assignment = True

    def __repr__(self) -> str:
        return (
            self.__class__.__name__
            + "\n\n"
            + "\n".join([f"{k}: {v}" for k, v in self.dict().items()])
        )