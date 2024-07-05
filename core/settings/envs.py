from environs import Env


# This class defines environment variables from the ./env file
class Envs:
    env = Env()
    env.read_env('.env')

    @classmethod
    def get_bot_token(cls) -> str:
        return cls.env.str("BOT_TOKEN")

    @classmethod
    def get_pay_token(cls) -> str:
        return cls.env.str("PAY_TOKEN")

    @classmethod
    def get_admin_id(cls) -> int:
        return cls.env.int("ADMIN_ID")

    @classmethod
    def get_forum_id(cls) -> int:
        return cls.env.int("FORUM_ID")

    @classmethod
    def get_postgres_data(cls) -> dict:
        return {
            'pg_name': cls.env.str("POSTGRES_DB"),
            'pg_user': cls.env.str("POSTGRES_USER"),
            'pg_pass': cls.env.str("POSTGRES_PASSWORD"),
            'pg_host': cls.env.str("POSTGRES_HOST"),
        }

    @classmethod
    def get_redis_data(cls) -> dict:
        return {
            'redis_name': cls.env.str("REDIS_NAME"),
            'redis_host': cls.env.str("REDIS_HOST"),
            'redis_port': cls.env.str("REDIS_PORT"),
        }


my_envs = Envs()
