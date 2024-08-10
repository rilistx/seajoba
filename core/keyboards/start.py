from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton


def role_button(
        *,
        sizes: tuple[int] = (2, ),
):
    keyboard = ReplyKeyboardBuilder()

    keyboard.add(
        KeyboardButton(
            text='👨‍✈️ Sailor',
        )
    )

    keyboard.add(
        KeyboardButton(
            text='👩‍💼 Manager',
        )
    )

    return keyboard.adjust(*sizes).as_markup(
        resize_keyboard=True,
        one_time_keyboard=True,
    )
