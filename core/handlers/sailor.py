import datetime

from aiogram import Bot, Router
from aiogram.filters import StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from core.components.paginator import Paginator
from core.components.redirector import MenuData, SailorData
from core.components.regulator import pages
from core.database.connector.country import country_all
from core.database.connector.fleet import fleet_all
from core.database.connector.position import position_all
from core.database.connector.purpose import purpose_all, purpose_one
from core.database.connector.rank import rank_all, rank_one
from core.database.connector.sailor import sailor_one, sailor_update, sailor_create
from core.database.connector.vessel import vessel_one, vessel_all
from core.filters.sailor import SailorCancelFilter, SailorNameFilter, SailorChangeFilter, SailorPhoneFilter, \
    SailorWhatsappFilter, SailorEmailFilter, SailorNationalityNextFilter, SailorNationalityConfirmFilter, \
    SailorBirthFilter, SailorPositionConfirmFilter, SailorRankNextFilter, SailorPositionNextFilter, \
    SailorRankConfirmFilter, SailorFleetNextFilter, SailorFleetConfirmFilter, SailorExperienceYesFilter, \
    SailorPurposeNextFilter, SailorPurposeConfirmFilter, SailorVesselNextFilter, SailorVesselConfirmFilter, \
    SailorApplicationFilter, SailorConfirmFilter, SailorExperienceNotFilter
from core.handlers.menu import redirector
from core.keyboards.sailor import sailor_cancel_button, sailor_return_button, sailor_whatsapp_button, \
    sailor_nationality_button, sailor_position_button, sailor_rank_button, sailor_fleet_button, sailor_purpose_button, \
    sailor_experience_button, sailor_vessel_button, sailor_confirm_button
from core.states.sailor import SailorState


sailor_router = Router()


@sailor_router.callback_query(
    SailorData.filter(),
)
async def name_manager(
        callback: CallbackQuery,
        callback_data: SailorData,
        session: AsyncSession,
        state: FSMContext,
):
    await state.update_data({
        'user_id': callback_data.user_id,
    })

    if callback_data.method == 'change':
        SailorState.change = await sailor_one(
            session=session,
            user_id=callback_data.user_id,
        )

        text = 'Отправь мне своё имя!'
    else:
        text = 'Отправь мне своё имя!'

    reply_markup = sailor_cancel_button(
        change=SailorState.change,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.NAME)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorCancelFilter(),
)
async def cancel_manager(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    if SailorState.change:
        text = f'Ты отменил обновление моряка!'

    else:
        text = f'Ты отменил создание моряка!'

    callback_data = MenuData(
        key='profile',
        level=6,
    )

    await callback.answer(
        text=text,
        show_alert=True
    )

    SailorState.change = None
    await state.clear()

    return await redirector(
        callback=callback,
        callback_data=callback_data,
        session=session,
    )


# @sailor_router.callback_query(
#     ManagerReturnFilter(),
# )
# async def return_manager(
#         callback: CallbackQuery,
#         session: AsyncSession,
#         state: FSMContext,
# ):
#     state_position = await state.get_state()
#
#     if state_position == ManagerState.PHONE:
#         await state.update_data({
#             'first_name': None,
#         })
#
#         text = 'Отправь мне своё имя!'
#         reply_markup = manager_cancel_button(
#             change=ManagerState.change,
#         )
#
#         await state.set_state(ManagerState.NAME)
#
#     elif state_position == ManagerState.WHATSAPP:
#         await state.update_data({
#             'phone': None,
#         })
#
#         text = 'Отправь мне свой номер телефона!'
#         reply_markup = manager_return_button(
#             change=ManagerState.change,
#         )
#
#         await state.set_state(ManagerState.PHONE)
#
#     elif state_position == ManagerState.EMAIL:
#         await state.update_data({
#             'whatsapp': None,
#         })
#
#         text = 'Whatsapp yes | not!'
#         reply_markup = manager_whatsapp_button(
#             change=ManagerState.change,
#         )
#
#         await state.set_state(ManagerState.WHATSAPP)
#
#     elif state_position == ManagerState.COMPANY:
#         await state.update_data({
#             'email': None,
#         })
#
#         text = 'Отправь мне электронную почту!'
#         reply_markup = manager_return_button(
#             change=ManagerState.change,
#         )
#
#         await state.set_state(ManagerState.EMAIL)
#
#     else:
#         await state.update_data({
#             'company_id': None,
#             'page': 1,
#         })
#
#         companies = await company_all(
#             session=session,
#         )
#
#         paginator = Paginator(
#             array=companies,
#             page=1,
#             per_page=8,
#         )
#
#         companies_button = paginator.get_page()
#         pagination_button = pages(
#             paginator=paginator,
#         )
#
#         text = 'Выбери компанию!'
#         reply_markup = manager_company_button(
#             change=ManagerState.change,
#             page=1,
#             companies_button=companies_button,
#             pagination_button=pagination_button,
#         )
#
#         await state.set_state(ManagerState.COMPANY)
#
#     msg = await callback.message.edit_text(
#         text=text,
#         reply_markup=reply_markup,
#     )
#
#     await callback.answer()
#
#     await state.update_data({
#         'massage_id': msg.message_id,
#     })


@sailor_router.message(
    SailorState.NAME,
    SailorNameFilter(),
)
async def phone_manager(
        message: Message,
        bot: Bot,
        state: FSMContext,
):
    await state.update_data({
        'first_name': message.text,
    })

    state_data = await state.get_data()

    await message.delete()
    await bot.delete_message(
        chat_id=message.chat.id,
        message_id=state_data['massage_id'],
    )

    text = 'Отправь мне свой номер телефона!'
    reply_markup = sailor_return_button(
        change=SailorState.change,
    )

    msg = await message.answer(
        text=text,
        reply_markup=reply_markup,
    )

    await state.set_state(SailorState.PHONE)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.NAME,
    SailorChangeFilter(),
)
async def phone_callback_manager(
        callback: CallbackQuery,
        state: FSMContext,
):
    await state.update_data({
        'first_name': SailorState.change.first_name,
    })

    text = 'Отправь мне свой номер телефона!'
    reply_markup = sailor_return_button(
        change=SailorState.change,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.PHONE)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.message(
    SailorState.PHONE,
    SailorPhoneFilter(),
)
async def whatsapp_choice_manager(
        message: Message,
        bot: Bot,
        state: FSMContext,
):
    await state.update_data({
        'phone': message.text,
    })

    state_data = await state.get_data()

    await message.delete()
    await bot.delete_message(
        chat_id=message.chat.id,
        message_id=state_data['massage_id'],
    )

    text = 'Есть ли у тебя вотсапп!'
    reply_markup = sailor_whatsapp_button(
        change=SailorState.change,
    )

    msg = await message.answer(
        text=text,
        reply_markup=reply_markup,
    )

    await state.set_state(SailorState.WHATSAPP)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.PHONE,
    SailorChangeFilter(),
)
async def whatsapp_callback_manager(
        callback: CallbackQuery,
        state: FSMContext,
):
    await state.update_data({
        'phone': SailorState.change.phone,
    })

    text = 'Есть ли у тебя вотсапп!'
    reply_markup = sailor_whatsapp_button(
        change=SailorState.change,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.WHATSAPP)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.WHATSAPP,
    SailorWhatsappFilter(),
)
async def email_manager(
        callback: CallbackQuery,
        state: FSMContext,
):
    await state.update_data({
        'whatsapp': True if callback.data.split('_')[-1] == 'yes' else False,
    })

    text = 'Отправь мне электронную почту компании!'
    reply_markup = sailor_return_button(
        change=SailorState.change,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()

    await state.set_state(SailorState.EMAIL)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.WHATSAPP,
    SailorChangeFilter(),
)
async def email_callback_manager(
        callback: CallbackQuery,
        state: FSMContext,
):
    await state.update_data({
        'whatsapp': SailorState.change.whatsapp,
    })

    text = 'Отправь мне электронную почту компании!'
    reply_markup = sailor_return_button(
        change=SailorState.change,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.EMAIL)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.message(
    SailorState.EMAIL,
    SailorEmailFilter(),
)
async def company_sailor(
        message: Message,
        bot: Bot,
        state: FSMContext,
):
    await state.update_data({
        'email': message.text,
    })

    state_data = await state.get_data()

    await message.delete()
    await bot.delete_message(
        chat_id=message.chat.id,
        message_id=state_data['massage_id'],
    )

    text = 'Отправь мне свою дату рождения!'
    reply_markup = sailor_return_button(
        change=SailorState.change,
    )

    msg = await message.answer(
        text=text,
        reply_markup=reply_markup,
    )

    await state.set_state(SailorState.BIRTH)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.EMAIL,
    SailorChangeFilter(),
)
async def date_callback_sailor(
        callback: CallbackQuery,
        state: FSMContext,
):
    await state.update_data({
        'email': SailorState.change.email,
    })

    text = 'Отправь мне свою дату рождения!'
    reply_markup = sailor_return_button(
        change=SailorState.change,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.BIRTH)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.message(
    SailorState.BIRTH,
    SailorBirthFilter(),
)
async def company_manager(
        message: Message,
        bot: Bot,
        session: AsyncSession,
        state: FSMContext,
):
    await state.update_data({
        'birth': message.text,
        'page': 1,
    })

    state_data = await state.get_data()

    await message.delete()
    await bot.delete_message(
        chat_id=message.chat.id,
        message_id=state_data['massage_id'],
    )

    nationality = await country_all(
        session=session,
    )

    paginator = Paginator(
        array=nationality,
        page=1,
        per_page=16,
    )

    nationality_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    text = 'Выбери национальность!'
    reply_markup = sailor_nationality_button(
        change=SailorState.change,
        page=1,
        nationality_button=nationality_button,
        pagination_button=pagination_button,
    )

    msg = await message.answer(
        text=text,
        reply_markup=reply_markup,
    )

    await state.set_state(SailorState.NATIONALITY)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.BIRTH,
    SailorChangeFilter(),
)
async def company_callback_manager(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    await state.update_data({
        'birth': SailorState.change.birth.strftime("%d %m %Y"),
        'page': 1,
    })

    nationality = await country_all(
        session=session,
    )

    paginator = Paginator(
        array=nationality,
        page=1,
        per_page=16,
    )

    nationality_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    text = 'Выбери национальность!'
    reply_markup = sailor_nationality_button(
        change=SailorState.change,
        page=1,
        nationality_button=nationality_button,
        pagination_button=pagination_button,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.NATIONALITY)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.NATIONALITY,
    SailorNationalityNextFilter(),
)
async def company_next_manager(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    page = int(callback.data.split('_')[-1])

    await state.update_data({
        'page': page,
    })

    nationality = await country_all(
        session=session,
    )

    paginator = Paginator(
        array=nationality,
        page=page,
        per_page=16,
    )

    nationality_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    text = 'Выбери национальность!'
    reply_markup = sailor_nationality_button(
        change=SailorState.change,
        page=1,
        nationality_button=nationality_button,
        pagination_button=pagination_button,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.NATIONALITY,
    SailorNationalityConfirmFilter(),
)
async def position_sailor(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    await state.update_data({
        'nationality_id': int(callback.data.split('_')[-1]),
        'page': 1,
    })

    positions = await position_all(
        session=session,
    )

    paginator = Paginator(
        array=positions,
        page=1,
        per_page=8,
    )

    positions_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    text = 'Выбери тип должности!'
    reply_markup = sailor_position_button(
        change=SailorState.change,
        page=1,
        positions_button=positions_button,
        pagination_button=pagination_button,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.POSITION)
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.NATIONALITY,
    SailorChangeFilter(),
)
async def position_callback_sailor(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    await state.update_data({
        'nationality_id': SailorState.change.nationality_id,
        'page': 1,
    })

    positions = await position_all(
        session=session,
    )

    paginator = Paginator(
        array=positions,
        page=1,
        per_page=8,
    )

    positions_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    text = 'Выбери тип должности!'
    reply_markup = sailor_position_button(
        change=SailorState.change,
        page=1,
        positions_button=positions_button,
        pagination_button=pagination_button,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.POSITION)
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.POSITION,
    SailorPositionNextFilter(),
)
async def city_next_company(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    page = int(callback.data.split('_')[-1])

    await state.update_data({
        'page': page,
    })

    positions = await position_all(
        session=session,
    )

    paginator = Paginator(
        array=positions,
        page=1,
        per_page=8,
    )

    positions_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    text = 'Выбери тип должности!'
    reply_markup = sailor_position_button(
        change=SailorState.change,
        page=1,
        positions_button=positions_button,
        pagination_button=pagination_button,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.POSITION,
    SailorPositionConfirmFilter(),
)
async def rank_company(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    await state.update_data({
        'position_id': int(callback.data.split('_')[-1]),
        'page': 1,
    })

    ranks = await rank_all(
        session=session,
        position_id=int(callback.data.split('_')[-1]),
    )

    paginator = Paginator(
        array=ranks,
        page=1,
        per_page=16,
    )

    ranks_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    text = 'Выбери свою должность!'
    reply_markup = sailor_rank_button(
        change=SailorState.change,
        page=1,
        ranks_button=ranks_button,
        pagination_button=pagination_button,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.RANK)
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.POSITION,
    SailorChangeFilter(),
)
async def city_callback_company(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    rank = await rank_one(
        session=session,
        rank_id=SailorState.change.rank_id,
    )

    await state.update_data({
        'position_id': rank.position_id,
        'page': 1,
    })

    ranks = await rank_all(
        session=session,
        position_id=rank.position_id,
    )

    paginator = Paginator(
        array=ranks,
        page=1,
        per_page=16,
    )

    ranks_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    text = 'Выбери свою должность!'
    reply_markup = sailor_rank_button(
        change=SailorState.change,
        page=1,
        ranks_button=ranks_button,
        pagination_button=pagination_button,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.RANK)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.RANK,
    SailorRankNextFilter(),
)
async def city_next_company(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    page = int(callback.data.split('_')[-1])

    await state.update_data({
        'page': page,
    })

    state_data = await state.get_data()

    ranks = await rank_all(
        session=session,
        position_id=state_data['position_id'],
    )

    paginator = Paginator(
        array=ranks,
        page=page,
        per_page=16,
    )

    ranks_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    text = 'Выбери свою должность!'
    reply_markup = sailor_rank_button(
        change=SailorState.change,
        page=page,
        ranks_button=ranks_button,
        pagination_button=pagination_button,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.RANK,
    SailorRankConfirmFilter(),
)
async def rank_company(
        callback: CallbackQuery,
        state: FSMContext,
):
    await state.update_data({
        'rank_id': int(callback.data.split('_')[-1]),
    })

    text = 'Ты работал на флоте?'
    reply_markup = sailor_experience_button(
        change=SailorState.change,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.EXPERIENCE)
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.RANK,
    SailorChangeFilter(),
)
async def rank_company(
        callback: CallbackQuery,
        state: FSMContext,
):
    await state.update_data({
        'rank_id': SailorState.change.rank_id,
    })

    text = 'Ты работал на флоте?'
    reply_markup = sailor_experience_button(
        change=SailorState.change,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.EXPERIENCE)
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.EXPERIENCE,
    SailorExperienceYesFilter(),
)
async def rank_company(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    await state.update_data({
        'page': 1,
    })

    fleets = await fleet_all(
        session=session,
    )

    paginator = Paginator(
        array=fleets,
        page=1,
        per_page=16,
    )

    fleets_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    text = 'Выбери флот!'
    reply_markup = sailor_fleet_button(
        change=SailorState.change,
        page=1,
        fleets_button=fleets_button,
        pagination_button=pagination_button,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.FLEET)
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.EXPERIENCE,
    SailorChangeFilter(),
)
async def rank_company(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    choice = False

    if SailorState.change:
        if SailorState.change.vessel_id:
            choice = True

    if not choice:
        await state.update_data({
            'vessel_id': None,
        })

        text = 'Загрузить апликашку!'
        reply_markup = sailor_return_button(
            change=SailorState.change,
        )

        msg = await callback.message.edit_text(
            text=text,
            reply_markup=reply_markup,
        )

        await callback.answer()
        await state.set_state(SailorState.APPLICATION)
        await state.update_data({
            'massage_id': msg.message_id,
        })

    else:
        await state.update_data({
            'page': 1,
        })

        fleets = await fleet_all(
            session=session,
        )

        paginator = Paginator(
            array=fleets,
            page=1,
            per_page=16,
        )

        fleets_button = paginator.get_page()
        pagination_button = pages(
            paginator=paginator,
        )

        change = False

        if SailorState.change:
            if SailorState.change.vessel_id:
                change = True

        text = 'Выбери флот!'
        reply_markup = sailor_fleet_button(
            change=change,
            page=1,
            fleets_button=fleets_button,
            pagination_button=pagination_button,
        )

        msg = await callback.message.edit_text(
            text=text,
            reply_markup=reply_markup,
        )

        await callback.answer()
        await state.set_state(SailorState.FLEET)
        await state.update_data({
            'massage_id': msg.message_id,
        })


@sailor_router.callback_query(
    SailorState.FLEET,
    SailorFleetNextFilter(),
)
async def city_next_company(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    page = int(callback.data.split('_')[-1])

    await state.update_data({
        'page': page,
    })

    fleets = await fleet_all(
        session=session,
    )

    paginator = Paginator(
        array=fleets,
        page=page,
        per_page=16,
    )

    fleets_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    change = False

    if SailorState.change:
        if SailorState.change.vessel_id:
            change = True

    text = 'Выбери флот!'
    reply_markup = sailor_fleet_button(
        change=change,
        page=1,
        fleets_button=fleets_button,
        pagination_button=pagination_button,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.FLEET,
    SailorFleetConfirmFilter(),
)
async def rank_company(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    await state.update_data({
        'fleet_id': int(callback.data.split('_')[-1]),
        'page': 1,
    })

    purposes = await purpose_all(
        session=session,
        fleet_id=int(callback.data.split('_')[-1])
    )

    paginator = Paginator(
        array=purposes,
        page=1,
        per_page=16,
    )

    purposes_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    change = False

    if SailorState.change:
        if SailorState.change.vessel_id:
            change = True

    text = 'Выбери тип судна!'
    reply_markup = sailor_purpose_button(
        change=change,
        page=1,
        purposes_button=purposes_button,
        pagination_button=pagination_button,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.PURPOSE)
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.FLEET,
    SailorChangeFilter(),
)
async def rank_company(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    vessel = await vessel_one(
        session=session,
        vessel_id=SailorState.change.vessel_id
    )

    purpose = await purpose_one(
        session=session,
        purpose_id=vessel.purpose_id,
    )

    await state.update_data({
        'fleet_id': purpose.fleet_id,
        'page': 1,
    })

    purposes = await purpose_all(
        session=session,
        fleet_id=int(callback.data.split('_')[-1])
    )

    paginator = Paginator(
        array=purposes,
        page=1,
        per_page=16,
    )

    purposes_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    change = False

    if SailorState.change:
        if SailorState.change.vessel_id:
            change = True

    text = 'Выбери тип судна!'
    reply_markup = sailor_purpose_button(
        change=change,
        page=1,
        purposes_button=purposes_button,
        pagination_button=pagination_button,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.PURPOSE)
    await state.update_data({
        'massage_id': msg.message_id,
    })











@sailor_router.callback_query(
    SailorState.PURPOSE,
    SailorPurposeNextFilter(),
)
async def rank_company(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    page = int(callback.data.split('_')[-1])

    await state.update_data({
        'page': page,
    })

    state_data = await state.get_data()

    purposes = await purpose_all(
        session=session,
        fleet_id=state_data['fleet_id'],
    )

    paginator = Paginator(
        array=purposes,
        page=page,
        per_page=16,
    )

    purposes_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    change = False

    if SailorState.change:
        if SailorState.change.vessel_id:
            change = True

    text = 'Выбери тип судна!'
    reply_markup = sailor_purpose_button(
        change=change,
        page=page,
        purposes_button=purposes_button,
        pagination_button=pagination_button,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.PURPOSE,
    SailorPurposeConfirmFilter(),
)
async def rank_company(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    await state.update_data({
        'purpose_id': int(callback.data.split('_')[-1]),
        'page': 1,
    })

    vessels = await vessel_all(
        session=session,
        purpose_id=int(callback.data.split('_')[-1]),
    )

    paginator = Paginator(
        array=vessels,
        page=1,
        per_page=16,
    )

    vessels_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    change = False

    if SailorState.change:
        if SailorState.change.vessel_id:
            change = True

    text = 'Выбери судно!'
    reply_markup = sailor_vessel_button(
        change=change,
        page=1,
        vessels_button=vessels_button,
        pagination_button=pagination_button,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.VESSEL)
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.PURPOSE,
    SailorChangeFilter(),
)
async def city_next_company(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    vessel = await vessel_one(
        session=session,
        vessel_id=SailorState.change.vessel_id
    )

    await state.update_data({
        'purpose_id': vessel.purpose_id,
        'page': 1,
    })

    vessels = await vessel_all(
        session=session,
        purpose_id=vessel.purpose_id,
    )

    paginator = Paginator(
        array=vessels,
        page=1,
        per_page=16,
    )

    vessels_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    change = False

    if SailorState.change:
        if SailorState.change.vessel_id:
            change = True

    text = 'Выбери судно!'
    reply_markup = sailor_vessel_button(
        change=change,
        page=1,
        vessels_button=vessels_button,
        pagination_button=pagination_button,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.VESSEL)
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.VESSEL,
    SailorVesselNextFilter(),
)
async def rank_company(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    page = int(callback.data.split('_')[-1])

    await state.update_data({
        'page': page,
    })

    state_data = await state.get_data()

    vessels = await vessel_all(
        session=session,
        purpose_id=state_data['purpose_id']
    )

    paginator = Paginator(
        array=vessels,
        page=page,
        per_page=16,
    )

    vessels_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    change = False

    if SailorState.change:
        if SailorState.change.vessel_id:
            change = True

    text = 'Выбери тип судна!'
    reply_markup = sailor_vessel_button(
        change=change,
        page=page,
        vessels_button=vessels_button,
        pagination_button=pagination_button,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.EXPERIENCE,
    SailorExperienceNotFilter(),
)
async def rank_company(
        callback: CallbackQuery,
        state: FSMContext,
):
    await state.update_data({
        'vessel_id': None,
    })

    text = 'Загрузить апликашку!'
    reply_markup = sailor_return_button(
        change=SailorState.change,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.APPLICATION)
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.VESSEL,
    SailorVesselConfirmFilter(),
)
async def rank_company(
        callback: CallbackQuery,
        state: FSMContext,
):
    await state.update_data({
        'vessel_id': int(callback.data.split('_')[-1]),
    })

    text = 'Загрузить апликашку!'
    reply_markup = sailor_return_button(
        change=SailorState.change,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.APPLICATION)
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.VESSEL,
    SailorChangeFilter(),
)
async def rank_company(
        callback: CallbackQuery,
        state: FSMContext,
):
    await state.update_data({
        'vessel_id': SailorState.change.vessel_id,
    })

    text = 'Загрузить апликашку!'
    reply_markup = sailor_return_button(
        change=SailorState.change,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.APPLICATION)
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.message(
    SailorState.APPLICATION,
    SailorApplicationFilter(),
)
async def rank_company(
        message: Message,
        bot: Bot,
        state: FSMContext,
):
    await state.update_data({
        'application': message.document.file_id,
    })

    state_data = await state.get_data()

    await message.delete()
    await bot.delete_message(
        chat_id=message.chat.id,
        message_id=state_data['massage_id'],
    )

    text = 'Сохранить данные?!'
    reply_markup = sailor_confirm_button()

    msg = await message.answer(
        text=text,
        reply_markup=reply_markup,
    )

    await state.set_state(SailorState.CONFIRM)
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.APPLICATION,
    SailorChangeFilter(),
)
async def rank_company(
        callback: CallbackQuery,
        state: FSMContext,
):
    await state.update_data({
        'application': SailorState.change.application,
    })

    text = 'Сохранить данные?!'
    reply_markup = sailor_confirm_button()

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(SailorState.CONFIRM)
    await state.update_data({
        'massage_id': msg.message_id,
    })


@sailor_router.callback_query(
    SailorState.CONFIRM,
    SailorConfirmFilter(),
)
async def finish_company(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    state_data = await state.get_data()

    if SailorState.change:
        await sailor_update(
            session=session,
            first_name=state_data['first_name'],
            phone=state_data['phone'],
            whatsapp=state_data['whatsapp'],
            email=state_data['email'],
            birth=datetime.datetime.strptime(state_data['birth'], "%d %m %Y"),
            nationality_id=state_data['nationality_id'],
            rank_id=state_data['rank_id'],
            vessel_id=state_data['vessel_id'],
            application=state_data['application'],
            openwork=SailorState.change.openwork,
            user_id=state_data['user_id'],
        )

        text = f'Данные о моряке были обновлены в базу данных!'
    else:
        await sailor_create(
            session=session,
            first_name=state_data['first_name'],
            phone=state_data['phone'],
            whatsapp=state_data['whatsapp'],
            email=state_data['email'],
            birth=datetime.datetime.strptime(state_data['birth'], "%d %m %Y"),
            nationality_id=state_data['nationality_id'],
            rank_id=state_data['rank_id'],
            vessel_id=state_data['vessel_id'],
            application=state_data['application'],
            user_id=state_data['user_id'],
        )

        text = f'Данные о моряке были записаны в базу данных!'

    callback_data = MenuData(
        key='profile',
        level=6,
    )

    await callback.answer(
        text=text,
        show_alert=True
    )

    SailorState.change = None
    await state.clear()

    return await redirector(
        callback=callback,
        callback_data=callback_data,
        session=session,
    )

# @manager_router.message(
#     StateFilter(ManagerState),
# )
# async def error_manager(
#         message: Message,
#         bot: Bot,
#         session: AsyncSession,
#         state: FSMContext,
# ):
#     state_data = await state.get_data()
#
#     await message.delete()
#     await bot.delete_message(
#         chat_id=message.chat.id,
#         message_id=state_data['massage_id'],
#     )
#
#     state_position = await state.get_state()
#
#     if state_position == ManagerState.NAME:
#         text = 'не правильное имя'
#         reply_markup = manager_cancel_button(
#             change=ManagerState.change,
#         )
#     elif state_position == ManagerState.PHONE:
#         text = 'Я тебя не понимаю отправь правильный номер'
#         reply_markup = manager_return_button(
#             change=ManagerState.change,
#         )
#     elif state_position == ManagerState.WHATSAPP:
#         text = 'выбери да или нет'
#         reply_markup = manager_whatsapp_button(
#             change=ManagerState.change,
#         )
#     elif state_position == ManagerState.EMAIL:
#         text = 'Я тебя не понимаю отправь правильный почту'
#         reply_markup = manager_return_button(
#             change=ManagerState.change,
#         )
#     elif state_position == ManagerState.COMPANY:
#         companies = await company_all(
#             session=session,
#         )
#
#         paginator = Paginator(
#             array=companies,
#             page=state_data['page'],
#             per_page=8,
#         )
#
#         companies_button = paginator.get_page()
#         pagination_button = pages(
#             paginator=paginator,
#         )
#
#         text = 'Выбери компанию!'
#         reply_markup = manager_company_button(
#             change=ManagerState.change,
#             page=1,
#             companies_button=companies_button,
#             pagination_button=pagination_button,
#         )
#     else:
#         text = 'Я тебя не понимаю ты хочешь записать в базу данных?'
#         reply_markup = manager_confirm_button()
#
#     msg = await message.answer(
#         text=text,
#         reply_markup=reply_markup,
#     )
#
#     await state.update_data({
#         'massage_id': msg.message_id,
#     })
