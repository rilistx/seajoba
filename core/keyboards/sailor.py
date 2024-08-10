from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def sailor_cancel_button(
        *,
        change: bool,
        sizes: tuple[int] = (1, ),
):
    keyboard = InlineKeyboardBuilder()

    if change:
        keyboard.add(
            InlineKeyboardButton(
                text='Don\'t change',
                callback_data='sailor_change',
            )
        )

    keyboard.add(
        InlineKeyboardButton(
            text='Cancel',
            callback_data='sailor_cancel',
        )
    )

    return keyboard.adjust(*sizes).as_markup()


def sailor_return_button(
        *,
        change: bool,
        sizes: tuple[int] = (1, 2, ),
):
    keyboard = InlineKeyboardBuilder()

    if change:
        keyboard.add(
            InlineKeyboardButton(
                text='Don\'t change',
                callback_data='sailor_change',
            )
        )

    keyboard.add(
        InlineKeyboardButton(
            text='Return',
            callback_data='sailor_return',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Cancel',
            callback_data='sailor_cancel',
        )
    )

    return keyboard.adjust(*sizes).as_markup()


def sailor_whatsapp_button(
        *,
        change: bool,
        sizes: tuple[int] = (1, 2, 2, ),
):
    keyboard = InlineKeyboardBuilder()

    if change:
        keyboard.add(
            InlineKeyboardButton(
                text='Don\'t change',
                callback_data='sailor_change',
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
            callback_data='sailor_return',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Cancel',
            callback_data='sailor_cancel',
        )
    )

    return keyboard.adjust(*sizes).as_markup()


def sailor_nationality_button(
        *,
        change: bool,
        page: int,
        nationality_button: list,
        pagination_button: dict,
):
    keyboard = InlineKeyboardBuilder()

    sizes = tuple()

    if change:
        keyboard.add(
            InlineKeyboardButton(
                text='Don\'t change',
                callback_data='sailor_change',
            )
        )

        sizes += (1, )

    for nationality in nationality_button:
        keyboard.add(
            InlineKeyboardButton(
                text=f"{nationality.nationality}",
                callback_data=f'nationality_confirm_{nationality.id}'
            )
        )

    sizes += tuple(2 for _ in range(len(nationality_button) // 2))

    if len(nationality_button) % 2:
        sizes += (1, )

    for text, action in pagination_button.items():
        if action == "next":
            keyboard.add(
                InlineKeyboardButton(
                    text=f"{text}",
                    callback_data=f'nationality_next_{page + 1}'
                )
            )
        elif action == "prev":
            keyboard.add(
                InlineKeyboardButton(
                    text=f"{text}",
                    callback_data=f'nationality_next_{page - 1}'
                )
            )

    if len(pagination_button):
        sizes += (len(pagination_button), )

    keyboard.add(
        InlineKeyboardButton(
            text='Return',
            callback_data='sailor_return',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Cancel',
            callback_data='sailor_cancel',
        )
    )

    sizes += (2, )

    return keyboard.adjust(*sizes).as_markup()


def sailor_position_button(
        *,
        change: bool,
        page: int,
        positions_button: list,
        pagination_button: dict,
):
    keyboard = InlineKeyboardBuilder()

    sizes = tuple()

    if change:
        keyboard.add(
            InlineKeyboardButton(
                text='Don\'t change',
                callback_data='sailor_change',
            )
        )

        sizes += (1, )

    for position in positions_button:
        keyboard.add(
            InlineKeyboardButton(
                text=f"{position.name}",
                callback_data=f'position_confirm_{position.id}'
            )
        )

    sizes += (1, )

    for text, action in pagination_button.items():
        if action == "next":
            keyboard.add(
                InlineKeyboardButton(
                    text=f"{text}",
                    callback_data=f'position_next_{page + 1}'
                )
            )
        elif action == "prev":
            keyboard.add(
                InlineKeyboardButton(
                    text=f"{text}",
                    callback_data=f'position_next_{page - 1}'
                )
            )

    if len(pagination_button):
        sizes += (len(pagination_button), )

    keyboard.add(
        InlineKeyboardButton(
            text='Return',
            callback_data='sailor_return',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Cancel',
            callback_data='sailor_cancel',
        )
    )

    sizes += (2, )

    return keyboard.adjust(*sizes).as_markup()


def sailor_rank_button(
        *,
        change: bool,
        page: int,
        ranks_button: list,
        pagination_button: dict,
):
    keyboard = InlineKeyboardBuilder()

    sizes = tuple()

    if change:
        keyboard.add(
            InlineKeyboardButton(
                text='Don\'t change',
                callback_data='sailor_change',
            )
        )

        sizes += (1, )

    for rank in ranks_button:
        keyboard.add(
            InlineKeyboardButton(
                text=f"{rank.name}",
                callback_data=f'rank_confirm_{rank.id}'
            )
        )

    sizes += tuple(2 for _ in range(len(ranks_button) // 2))

    if len(ranks_button) % 2:
        sizes += (1, )

    for text, action in pagination_button.items():
        if action == "next":
            keyboard.add(
                InlineKeyboardButton(
                    text=f"{text}",
                    callback_data=f'rank_next_{page + 1}'
                )
            )
        elif action == "prev":
            keyboard.add(
                InlineKeyboardButton(
                    text=f"{text}",
                    callback_data=f'rank_next_{page - 1}'
                )
            )

    if len(pagination_button):
        sizes += (len(pagination_button), )

    keyboard.add(
        InlineKeyboardButton(
            text='Return',
            callback_data='sailor_return',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Cancel',
            callback_data='sailor_cancel',
        )
    )

    sizes += (2, )

    return keyboard.adjust(*sizes).as_markup()


def sailor_experience_button(
        *,
        change: bool,
        sizes: tuple[int] = (1, 2, 2, ),
):
    keyboard = InlineKeyboardBuilder()

    if change:
        keyboard.add(
            InlineKeyboardButton(
                text='Don\'t change',
                callback_data='sailor_change',
            )
        )

    keyboard.add(
        InlineKeyboardButton(
            text='Yes',
            callback_data='experience_yes',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Not',
            callback_data='experience_not',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Return',
            callback_data='sailor_return',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Cancel',
            callback_data='sailor_cancel',
        )
    )

    return keyboard.adjust(*sizes).as_markup()


def sailor_fleet_button(
        *,
        change: bool,
        page: int,
        fleets_button: list,
        pagination_button: dict,
):
    keyboard = InlineKeyboardBuilder()

    sizes = tuple()

    if change:
        keyboard.add(
            InlineKeyboardButton(
                text='Don\'t change',
                callback_data='sailor_change',
            )
        )

        sizes += (1, )

    for fleet in fleets_button:
        keyboard.add(
            InlineKeyboardButton(
                text=f"{fleet.name}",
                callback_data=f'fleet_confirm_{fleet.id}'
            )
        )

    sizes += tuple(2 for _ in range(len(fleets_button) // 2))

    if len(fleets_button) % 2:
        sizes += (1, )

    for text, action in pagination_button.items():
        if action == "next":
            keyboard.add(
                InlineKeyboardButton(
                    text=f"{text}",
                    callback_data=f'fleet_next_{page + 1}'
                )
            )
        elif action == "prev":
            keyboard.add(
                InlineKeyboardButton(
                    text=f"{text}",
                    callback_data=f'fleet_next_{page - 1}'
                )
            )

    if len(pagination_button):
        sizes += (len(pagination_button), )

    keyboard.add(
        InlineKeyboardButton(
            text='Return',
            callback_data='sailor_return',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Cancel',
            callback_data='sailor_cancel',
        )
    )

    sizes += (2, )

    return keyboard.adjust(*sizes).as_markup()


def sailor_purpose_button(
        *,
        change: bool,
        page: int,
        purposes_button: list,
        pagination_button: dict,
):
    keyboard = InlineKeyboardBuilder()

    sizes = tuple()

    if change:
        keyboard.add(
            InlineKeyboardButton(
                text='Don\'t change',
                callback_data='sailor_change',
            )
        )

        sizes += (1, )

    for purpose in purposes_button:
        keyboard.add(
            InlineKeyboardButton(
                text=f"{purpose.name}",
                callback_data=f'purpose_confirm_{purpose.id}'
            )
        )

    sizes += tuple(2 for _ in range(len(purposes_button) // 2))

    if len(purposes_button) % 2:
        sizes += (1, )

    for text, action in pagination_button.items():
        if action == "next":
            keyboard.add(
                InlineKeyboardButton(
                    text=f"{text}",
                    callback_data=f'purpose_next_{page + 1}'
                )
            )
        elif action == "prev":
            keyboard.add(
                InlineKeyboardButton(
                    text=f"{text}",
                    callback_data=f'purpose_next_{page - 1}'
                )
            )

    if len(pagination_button):
        sizes += (len(pagination_button), )

    keyboard.add(
        InlineKeyboardButton(
            text='Return',
            callback_data='sailor_return',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Cancel',
            callback_data='sailor_cancel',
        )
    )

    sizes += (2, )

    return keyboard.adjust(*sizes).as_markup()


def sailor_vessel_button(
        *,
        change: bool,
        page: int,
        vessels_button: list,
        pagination_button: dict,
):
    keyboard = InlineKeyboardBuilder()

    sizes = tuple()

    if change:
        keyboard.add(
            InlineKeyboardButton(
                text='Don\'t change',
                callback_data='sailor_change',
            )
        )

        sizes += (1, )

    for vessel in vessels_button:
        keyboard.add(
            InlineKeyboardButton(
                text=f"{vessel.name}",
                callback_data=f'vessel_confirm_{vessel.id}'
            )
        )

    sizes += tuple(2 for _ in range(len(vessels_button) // 2))

    if len(vessels_button) % 2:
        sizes += (1, )

    for text, action in pagination_button.items():
        if action == "next":
            keyboard.add(
                InlineKeyboardButton(
                    text=f"{text}",
                    callback_data=f'vessel_next_{page + 1}'
                )
            )
        elif action == "prev":
            keyboard.add(
                InlineKeyboardButton(
                    text=f"{text}",
                    callback_data=f'vessel_next_{page - 1}'
                )
            )

    if len(pagination_button):
        sizes += (len(pagination_button), )

    keyboard.add(
        InlineKeyboardButton(
            text='Return',
            callback_data='sailor_return',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Cancel',
            callback_data='sailor_cancel',
        )
    )

    sizes += (2, )

    return keyboard.adjust(*sizes).as_markup()


def sailor_confirm_button(
        *,
        sizes: tuple[int] = (1, 2, ),
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(
        InlineKeyboardButton(
            text='Confirm',
            callback_data='sailor_confirm',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Return',
            callback_data='sailor_return',
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            text='Cancel',
            callback_data='sailor_cancel',
        )
    )

    return keyboard.adjust(*sizes).as_markup()
