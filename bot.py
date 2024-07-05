import asyncio
import logging

from core import unpacking


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        filename="loger.log",
        filemode="w",
        format="%(asctime)s %(levelname)s %(message)s",
    )

    await unpacking()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('This bot stopped 😈')
