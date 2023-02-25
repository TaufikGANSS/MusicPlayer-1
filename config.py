"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("29717887")
        self.API_HASH: str = os.environ.get("dbceb604465fabeb200f43b2fd32770d")
        self.SESSION: str = os.environ.get("1BVtsOLABuzhXHd3R3C2E-2tblAkS5JyU0LRHhWhSyTZKtINGe0xLs4YyBiSSBvY0xmdX7pjsjCeMa1Ph6vixYQFJCkkiBC92FfUl3Ls0q97PqKtbkj4uzcLkj_4sByYYbCdoJFWHfwnP4Rbl4V503lPH8EYxFF1eJpliWzGmb5Wrz50wQ6JQ3VGK-pJdfGgGTXqC_FqarH9QqIbKpqy_10BW3Z0sqsXwdSCXUDVJtRCdHAHcfSzZswIKBHRKjEPgpjinQ6zrWWYV5jqp_IjWmRPSytX4Le5CBmNLzuNoknneBokuE0sq5G2mT9ttC2ldlKBNl5ied0ihsuu47uL3Wti1ndQktI0=")
        self.BOT_TOKEN: str = os.environ.get("6038053134:AAF70JiVG5iFbMgLlMfXBlS5IJw5kUez_9Q")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", " ").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
