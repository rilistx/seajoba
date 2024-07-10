from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def support_button(
        sizes: tuple[int] = (2, 1, ),
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(
        InlineKeyboardButton(
            text='⚙️ Support',
            url='https://t.me/SeaJobaSupport',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='⚙️ Forum',
            url='https://t.me/SeaJobaForum/28',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='🧭 Menu',
            callback_data='menu',
        )
    )

    return keyboard.adjust(*sizes).as_markup()
