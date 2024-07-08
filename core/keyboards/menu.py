from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def menu_user_button(
        role: str,
        premium: bool,
        sizes: tuple[int] = (1, 1, 1, 2, 1, ),
):
    keyboard = InlineKeyboardBuilder()

    if role == 'sailor':
        keyboard.add(
            InlineKeyboardButton(
                text='🔎 Job search',
                callback_data='search',
            )
        )
        keyboard.add(
            InlineKeyboardButton(
                text='⭐️ Favourites',
                callback_data='favorite',
            )
        )
        keyboard.add(
            InlineKeyboardButton(
                text=f'{'📌' if premium else '💎'} Job for you',
                callback_data='selection' if premium else 'premium',
            )
        )
    else:
        keyboard.add(
            InlineKeyboardButton(
                text=f'{'🆕' if premium else '💎'} Create vacancy',
                callback_data='create' if premium else 'premium',
            )
        )
        keyboard.add(
            InlineKeyboardButton(
                text='📁 Your vacancies',
                callback_data='browse',
            )
        )
        keyboard.add(
            InlineKeyboardButton(
                text=f'{'🗃' if premium else '💎'} Marine database',
                callback_data='database' if premium else 'premium',
            )
        )
    keyboard.add(
        InlineKeyboardButton(
            text='ℹ️ About us',
            callback_data='about',
        )
    )
    keyboard.add(
        InlineKeyboardButton(
            text='🧑‍💻 Profile',
            callback_data='profile',
        )
    )
    keyboard.add(
        InlineKeyboardButton(
            text='⚙️ Support',
            callback_data='support',
        )
    )

    return keyboard.adjust(*sizes).as_markup()


def menu_admin_button(
        sizes: tuple[int] = (1, ),
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(
        InlineKeyboardButton(
            text='⚙️ Support',
            callback_data='support',
        )
    )

    return keyboard.adjust(*sizes).as_markup()
