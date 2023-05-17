class Config(object):
    LOGGER = True
    # Get this value from my.telegram.org/apps
        API_ID = 22287815
            API_HASH = "c3743ded78be8cb486e53d7bdc9c6409"
    CASH_API_KEY = "MU7TTKIA7NTWA5W2"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key
    DATABASE_URL = "postgres://iduyuzwt:OP3vNRUi5JHefpgToeeM0HYWAE5lhjNF@mahmud.db.elephantsql.com/iduyuzwt"  # A sql database url from elephantsql.com
    EVENT_LOGS = (-1001943077241)  # Event logs channel to note down important bot level events
    MONGO_DB_URI = "mongodb://omyadav:nxtvenom1122@ac-g6rfbue-shard-00-00.1xa2qqo.mongodb.net:27017,ac-g6rfbue-shard-00-01.1xa2qqo.mongodb.net:27017,ac-g6rfbue-shard-00-02.1xa2qqo.mongodb.net:27017/?ssl=true&replicaSet=atlas-139rpz-shard-0&authSource=admin&retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com
    # Telegraph link of the image which will be shown at start command.
        START_IMG = "https://graph.org/file/f7f0ebdf06b30e0ddd331.jpg"
    SUPPORT_CHAT = "katagiriyuuichibotsupport"  # Your Telegram support group chat username where your users will go and bother you
    TOKEN = "6060458364:AAHrqjC7XQ5shunfntb55PwX9oaJ5OUV4uI"  # Get bot token from @BotFather on Telegram
    TIME_API_KEY = "KDFSAHI8BKJG"  # Get this value from https://timezonedb.com/api
    OWNER_ID = 5057623667  # User id of your telegram account (Must be integer)
    # Optional fields
        BL_CHATS = []  # List of groups that you want blacklisted.
            DRAGONS = [6246358451]  # User id of sudo users
                DEV_USERS = [5149937796]  # User id of dev users
                    DEMONS = [6246358451]  # User id of support users
                        TIGERS = [6246358451]  # User id of tiger users
                            WOLVES = [6246358451]  # User id of whitelist users
    ALLOW_CHATS = True
        ALLOW_EXCL = True
            DEL_CMDS = True
                INFOPIC = True
                    LOAD = []
                        NO_LOAD = []
                            STRICT_GBAN = True
                                TEMP_DOWNLOAD_DIRECTORY = "./"
                                    WORKERS = 8

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
