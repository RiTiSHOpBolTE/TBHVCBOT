from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN","5562514845:AAGt1HR8jsuYQpenluDM1JaTSoMBd817wbE")
BOT_NAME = getenv("BOT_NAME","⏤͟͟͞͞★𝑻𝑩𝑯ꗄ𝑴𝑼𝑺𝑰𝑪➺")
BOT_USERNAME = getenv("BOT_USERNAME", "TBH_MUSIC_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@HUNTER_IS_BACK")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "EAGLE_MAFIA_CLUB")
DURATION_LIMIT = int(getenv("DURATION_LIMIT","300"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/4d83f2e52df49e973e18d.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/4d83f2e52df49e973e18d.jpg")
SESSION_NAME = getenv("SESSION_NAME","BQA-cOfpFvDJpq5wUtxrKkIgU8yViN7YxCaW7y0gP6S5V90R7YPlE-AMfIuGhe8Uj4A2c8Dr0puBOd7h-aXQrSzjXdJQdr0uorVFkoLdFJ87uctVlWjjlQQVIGX0Bf5FytWIOOR1txQMl6U64xuMrr73O5IMHScv9fW6p6jkT5Oo5KJ-fSfFSNa5PqggZnJ7Sw0Li6OOkkfjQRXBF9pX4Ha-al0vX4MinZ-U5NroNeQqkAYgtRoGV0USjd43DUhzo1WiuRzeI40WvcjEnB4atGBXa7lg9DoE0woKslgAlgJnw-BS8pTQCGanH57vJ0A4RJIuGI-IOgc7jIAy75bsXZVOAAAAAS_xwkcA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1761766352").split()))
