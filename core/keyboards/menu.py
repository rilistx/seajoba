from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from core.components.redirector import MenuData, ChoiceData


def user_button(
        *,
        role: str,
        user_id: int,
        premium: bool,
        sizes: tuple[int] = (1, 1, 1, 2, 1, )
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
                text='📌 Job for you',
                callback_data='selection' if premium else 'premium',
            )
        )

        keyboard.add(
            InlineKeyboardButton(
                text='⭐️ Favourites',
                callback_data='favorite',
            )
        )

    else:
        keyboard.add(
            InlineKeyboardButton(
                text='🆕 Create vacancy',
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
                text='🗃 Marine database',
                callback_data='database' if premium else 'premium',
            )
        )

    keyboard.add(
        InlineKeyboardButton(
            text='ℹ️ About us',
            callback_data=MenuData(
                key='about',
                level=0,
            ).pack()
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='🧑‍💻 Profile',
            callback_data=MenuData(
                key='profile',
                level=4,
                user_id=user_id,
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


def admin_button(
        *,
        premium: bool,
        sizes: tuple[int] = (2, 1, 2, )
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(
        InlineKeyboardButton(
            text='Company',
            callback_data=MenuData(
                key='company',
                level=1,
            ).pack()
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Charter',
            callback_data=MenuData(
                key='charter',
                level=1,
            ).pack()
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text=f'{'💎   Change premium   💎' if premium else '💎   Activate premium   💎'}',
            callback_data=ChoiceData(
                key='premium',
                method='change' if premium else 'activate',
            ).pack()
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Vacancy',
            callback_data=MenuData(
                key='vacancy',
                level=9,
            ).pack()
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='User',
            callback_data=MenuData(
                key='user',
                level=9,
            ).pack()
        )
    )

    return keyboard.adjust(*sizes).as_markup()


def about_button(
        *,
        sizes: tuple[int] = (2, ),
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(
        InlineKeyboardButton(
            text='📺 News',
            url='https://t.me/SeaJobaNews',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='💬 Forum',
            url='https://t.me/SeaJobaForum',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='🧭 Menu',
            callback_data=MenuData(
                key='menu',
                level=0,
            ).pack()
        )
    )

    return keyboard.adjust(*sizes).as_markup()


def support_button(
        *,
        sizes: tuple[int] = (2,),
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
            text='💬 Forum',
            url='https://t.me/SeaJobaForum/28',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='🧭 Menu',
            callback_data=MenuData(
                key='menu',
                level=0,
            ).pack()
        )
    )

    return keyboard.adjust(*sizes).as_markup()
