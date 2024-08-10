from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def premium_cancel_button(
        *,
        change: bool,
        sizes: tuple[int] = (1, ),
):
    keyboard = InlineKeyboardBuilder()

    if change:
        keyboard.add(
            InlineKeyboardButton(
                text='Don\'t change',
                callback_data='premium_change',
            )
        )

    keyboard.add(
        InlineKeyboardButton(
            text='Cancel',
            callback_data='premium_cancel',
        )
    )

    return keyboard.adjust(*sizes).as_markup()


def premium_return_button(
        *,
        change: bool,
):
    keyboard = InlineKeyboardBuilder()

    sizes = ()

    if change:
        keyboard.add(
            InlineKeyboardButton(
                text='Don\'t change',
                callback_data='premium_change',
            )
        )

        sizes = (1, )

    keyboard.add(
        InlineKeyboardButton(
            text='Return',
            callback_data='premium_return',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Cancel',
            callback_data='premium_cancel',
        )
    )

    sizes += (2, )

    return keyboard.adjust(*sizes).as_markup()


def premium_confirm_button(
        *,
        sizes: tuple[int] = (1, 2, ),
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(
        InlineKeyboardButton(
            text='Confirm',
            callback_data='premium_confirm',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Return',
            callback_data='premium_return',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Cancel',
            callback_data='premium_cancel',
        )
    )

    return keyboard.adjust(*sizes).as_markup()
