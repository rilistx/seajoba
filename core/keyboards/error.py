from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from core.components.redirector import MenuData


def error_button(
        *,
        sizes: tuple[int] = (2, ),
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(
        InlineKeyboardButton(
            text='🧭 Menu',
            callback_data=MenuData(
                key='menu',
                level=0,
            ).pack()
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='⚙️ Support',
            callback_data=MenuData(
                key='support',
                level=0,
            ).pack()
        )
    )

    return keyboard.adjust(*sizes).as_markup()
