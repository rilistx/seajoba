from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def menu_button(
        # role: str,
        # premium: bool,
        sizes: tuple[int] = (2, ),
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(
        InlineKeyboardButton(
            text='🧭 Create Vacancy',
            callback_data='create'
        )
    )
    keyboard.add(
        InlineKeyboardButton(
            text='🧭 Your Vacancies',
            callback_data='database'
        )
    )
    keyboard.add(
        InlineKeyboardButton(
            text='🧭 Marine Database',
            callback_data='database'
        )
    )
    keyboard.add(
        InlineKeyboardButton(
            text='🧭 About Us',
            callback_data='about'
        )
    )
    keyboard.add(
        InlineKeyboardButton(
            text='🧭 Profile',
            callback_data='profile'
        )
    )
    keyboard.add(
        InlineKeyboardButton(
            text='⚙️ Support',
            callback_data='support'
        )
    )

    return keyboard.adjust(*sizes).as_markup()
