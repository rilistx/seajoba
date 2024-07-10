from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def error_button(
        sizes: tuple[int] = (2, ),
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(
        InlineKeyboardButton(
            text='🧭 Menu',
            callback_data='menu',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='⚙️ Support',
            callback_data='support',
        )
    )

    return keyboard.adjust(*sizes).as_markup()
