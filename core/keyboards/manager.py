from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def manager_cancel_button(
        *,
        change: bool,
        sizes: tuple[int] = (1, ),
):
    keyboard = InlineKeyboardBuilder()

    if change:
        keyboard.add(
            InlineKeyboardButton(
                text='Don\'t change',
                callback_data='manager_change',
            )
        )

    keyboard.add(
        InlineKeyboardButton(
            text='Cancel',
            callback_data='manager_cancel',
        )
    )

    return keyboard.adjust(*sizes).as_markup()


def manager_return_button(
        *,
        change: bool,
        sizes: tuple[int] = (1, 2, ),
):
    keyboard = InlineKeyboardBuilder()

    if change:
        keyboard.add(
            InlineKeyboardButton(
                text='Don\'t change',
                callback_data='manager_change',
            )
        )

    keyboard.add(
        InlineKeyboardButton(
            text='Return',
            callback_data='manager_return',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Cancel',
            callback_data='manager_cancel',
        )
    )

    return keyboard.adjust(*sizes).as_markup()


def manager_whatsapp_button(
        *,
        change: bool,
        sizes: tuple[int] = (1, 2, 2, ),
):
    keyboard = InlineKeyboardBuilder()

    if change:
        keyboard.add(
            InlineKeyboardButton(
                text='Don\'t change',
                callback_data='manager_change',
            )
        )

    keyboard.add(
        InlineKeyboardButton(
            text='Yes',
            callback_data='whatsapp_yes',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Not',
            callback_data='whatsapp_not',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Return',
            callback_data='manager_return',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Cancel',
            callback_data='manager_cancel',
        )
    )

    return keyboard.adjust(*sizes).as_markup()


def manager_company_button(
        *,
        change: bool,
        page: int,
        companies_button: list,
        pagination_button: dict,
):
    keyboard = InlineKeyboardBuilder()

    sizes = tuple()

    if change:
        keyboard.add(
            InlineKeyboardButton(
                text='Don\'t change',
                callback_data='manager_change',
            )
        )

        sizes += (1, )

    for company in companies_button:
        keyboard.add(
            InlineKeyboardButton(
                text=f"{company.name}",
                callback_data=f'company_confirm_{company.id}'
            )
        )

    sizes += tuple(2 for _ in range(len(companies_button) // 2))

    if len(companies_button) % 2:
        sizes += (1, )

    for text, action in pagination_button.items():
        if action == "next":
            keyboard.add(
                InlineKeyboardButton(
                    text=f"{text}",
                    callback_data=f'company_next_{page + 1}'
                )
            )
        elif action == "prev":
            keyboard.add(
                InlineKeyboardButton(
                    text=f"{text}",
                    callback_data=f'company_next_{page - 1}'
                )
            )

    if len(pagination_button):
        sizes += (len(pagination_button), )

    keyboard.add(
        InlineKeyboardButton(
            text='Return',
            callback_data='manager_return',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Cancel',
            callback_data='manager_cancel',
        )
    )

    sizes += (2, )

    return keyboard.adjust(*sizes).as_markup()


def manager_confirm_button(
        *,
        sizes: tuple[int] = (1, 2, ),
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(
        InlineKeyboardButton(
            text='Confirm',
            callback_data='manager_confirm',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Return',
            callback_data='manager_return',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Cancel',
            callback_data='manager_cancel',
        )
    )

    return keyboard.adjust(*sizes).as_markup()
