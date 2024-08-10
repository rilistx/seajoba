from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from core.components.redirector import MenuData, ChoiceData
from core.database.models import Manager, Sailor


def profile_manager_button(
        *,
        user_id: int,
        premium: bool,
        information: Manager,
        sizes: tuple[int] = (1, ),
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(
        InlineKeyboardButton(
            text='Change CV' if information else 'Create CV',
            callback_data=ChoiceData(
                key='manager',
                method='change' if information else 'create',
                object_id=user_id,
            ).pack()
        )
    )

    if information:
        if not premium:
            keyboard.add(
                InlineKeyboardButton(
                    text='Activate premium',
                    callback_data=MenuData(
                        key='charter',
                        level=1,
                    ).pack()
                )
            )

        keyboard.add(
            InlineKeyboardButton(
                text='Information company',
                callback_data=MenuData(
                    key='profile',
                    level=7,
                ).pack()
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


def profile_sailor_button(
        *,
        user_id: int,
        premium: bool,
        information: Sailor,
        sizes: tuple[int] = (1, ),
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(
        InlineKeyboardButton(
            text='Change CV' if information else 'Create CV',
            callback_data=ChoiceData(
                key='sailor',
                method='change' if information else 'create',
                object_id=user_id,
            ).pack()
        )
    )

    if information:
        if not premium:
            keyboard.add(
                InlineKeyboardButton(
                    text='Activate premium',
                    callback_data=MenuData(
                        key='charter',
                        level=1,
                    ).pack()
                )
            )

        keyboard.add(
            InlineKeyboardButton(
                text='Looking for work',
                callback_data=MenuData(
                    key='profile',
                    level=8,
                ).pack()
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


def profile_company_button(
        *,
        sizes: tuple[int] = (2, ),
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(
        InlineKeyboardButton(
            text='⬅️ Back',
            callback_data=MenuData(
                key='profile',
                level=6,
            ).pack()
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


def profile_notify_button(
        *,
        sizes: tuple[int] = (2, ),
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(
        InlineKeyboardButton(
            text='⬅️ Back',
            callback_data=MenuData(
                key='profile',
                level=6,
            ).pack()
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='⬅️ Back',
            callback_data=MenuData(
                key='profile',
                level=6,
            ).pack()
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
