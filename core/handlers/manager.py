from aiogram import Bot, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from core.components.paginator import Paginator
from core.components.redirector import MenuData, ManagerData
from core.components.regulator import pages
from core.database.connector.company import company_all
from core.database.connector.manager import manager_one, manager_update, manager_create
from core.filters.manager import ManagerNameFilter, ManagerChangeFilter, ManagerCancelFilter, ManagerReturnFilter, \
    ManagerWhatsappFilter, ManagerPhoneFilter, ManagerEmailFilter, ManagerCompanyNextFilter, \
    ManagerCompanyConfirmFilter, ManagerConfirmFilter
from core.handlers.menu import redirector
from core.keyboards.manager import manager_cancel_button, manager_return_button, manager_whatsapp_button, \
    manager_company_button, manager_confirm_button
from core.states.manager import ManagerState


manager_router = Router()


@manager_router.callback_query(
    ManagerData.filter(),
)
async def name_manager(
        callback: CallbackQuery,
        callback_data: ManagerData,
        session: AsyncSession,
        state: FSMContext,
):
    await state.update_data({
        'user_id': callback_data.user_id,
    })

    if callback_data.method == 'change':
        ManagerState.change = await manager_one(
            session=session,
            user_id=callback_data.user_id,
        )

        text = 'Отправь мне своё имя!'
    else:
        text = 'Отправь мне своё имя!'

    reply_markup = manager_cancel_button(
        change=ManagerState.change,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(ManagerState.NAME)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@manager_router.callback_query(
    ManagerCancelFilter(),
)
async def cancel_manager(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    if ManagerState.change:
        text = f'Ты отменил обновление менеджера!'

    else:
        text = f'Ты отменил создание менеджера!'

    callback_data = MenuData(
        key='profile',
        level=6,
    )

    await callback.answer(
        text=text,
        show_alert=True,
    )

    ManagerState.change = None
    await state.clear()

    return await redirector(
        callback=callback,
        callback_data=callback_data,
        session=session,
    )


@manager_router.callback_query(
    ManagerReturnFilter(),
)
async def return_manager(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    state_position = await state.get_state()

    if state_position == ManagerState.PHONE:
        await state.update_data({
            'first_name': None,
        })

        text = 'Отправь мне своё имя!'

        reply_markup = manager_cancel_button(
            change=ManagerState.change,
        )

        await state.set_state(ManagerState.NAME)

    elif state_position == ManagerState.WHATSAPP:
        await state.update_data({
            'phone': None,
        })

        text = 'Отправь мне свой номер телефона!'

        reply_markup = manager_return_button(
            change=ManagerState.change,
        )

        await state.set_state(ManagerState.PHONE)

    elif state_position == ManagerState.EMAIL:
        await state.update_data({
            'whatsapp': None,
        })

        text = 'Whatsapp yes | not!'

        reply_markup = manager_whatsapp_button(
            change=ManagerState.change,
        )

        await state.set_state(ManagerState.WHATSAPP)

    elif state_position == ManagerState.COMPANY:
        await state.update_data({
            'email': None,
        })

        text = 'Отправь мне электронную почту!'

        reply_markup = manager_return_button(
            change=ManagerState.change,
        )

        await state.set_state(ManagerState.EMAIL)

    else:
        await state.update_data({
            'company_id': None,
            'page': 1,
        })

        companies = await company_all(
            session=session,
        )

        paginator = Paginator(
            array=companies,
            page=1,
            per_page=8,
        )

        companies_button = paginator.get_page()
        pagination_button = pages(
            paginator=paginator,
        )

        text = 'Выбери компанию!'

        reply_markup = manager_company_button(
            change=ManagerState.change,
            page=1,
            companies_button=companies_button,
            pagination_button=pagination_button,
        )

        await state.set_state(ManagerState.COMPANY)

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()

    await state.update_data({
        'massage_id': msg.message_id,
    })


@manager_router.message(
    ManagerState.NAME,
    ManagerNameFilter(),
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

    reply_markup = manager_return_button(
        change=ManagerState.change,
    )

    msg = await message.answer(
        text=text,
        reply_markup=reply_markup,
    )

    await state.set_state(ManagerState.PHONE)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@manager_router.callback_query(
    ManagerState.NAME,
    ManagerChangeFilter(),
)
async def phone_callback_manager(
        callback: CallbackQuery,
        state: FSMContext,
):
    await state.update_data({
        'first_name': ManagerState.change.first_name,
    })

    text = 'Отправь мне свой номер телефона!'

    reply_markup = manager_return_button(
        change=ManagerState.change,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(ManagerState.PHONE)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@manager_router.message(
    ManagerState.PHONE,
    ManagerPhoneFilter(),
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

    reply_markup = manager_whatsapp_button(
        change=ManagerState.change,
    )

    msg = await message.answer(
        text=text,
        reply_markup=reply_markup,
    )

    await state.set_state(ManagerState.WHATSAPP)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@manager_router.callback_query(
    ManagerState.PHONE,
    ManagerChangeFilter(),
)
async def whatsapp_callback_manager(
        callback: CallbackQuery,
        state: FSMContext,
):
    await state.update_data({
        'phone': ManagerState.change.phone,
    })

    text = 'Есть ли у тебя вотсапп!'

    reply_markup = manager_whatsapp_button(
        change=ManagerState.change,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(ManagerState.WHATSAPP)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@manager_router.callback_query(
    ManagerState.WHATSAPP,
    ManagerWhatsappFilter(),
)
async def email_manager(
        callback: CallbackQuery,
        state: FSMContext,
):
    await state.update_data({
        'whatsapp': True if callback.data.split('_')[-1] == 'yes' else False,
    })

    text = 'Отправь мне электронную почту компании!'

    reply_markup = manager_return_button(
        change=ManagerState.change,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()

    await state.set_state(ManagerState.EMAIL)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@manager_router.callback_query(
    ManagerState.WHATSAPP,
    ManagerChangeFilter(),
)
async def email_callback_manager(
        callback: CallbackQuery,
        state: FSMContext,
):
    await state.update_data({
        'whatsapp': ManagerState.change.whatsapp,
    })

    text = 'Отправь мне электронную почту компании!'

    reply_markup = manager_return_button(
        change=ManagerState.change,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(ManagerState.EMAIL)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@manager_router.message(
    ManagerState.EMAIL,
    ManagerEmailFilter(),
)
async def company_manager(
        message: Message,
        bot: Bot,
        session: AsyncSession,
        state: FSMContext,
):
    await state.update_data({
        'email': message.text,
        'page': 1,
    })

    state_data = await state.get_data()

    await message.delete()
    await bot.delete_message(
        chat_id=message.chat.id,
        message_id=state_data['massage_id'],
    )

    companies = await company_all(
        session=session,
    )

    paginator = Paginator(
        array=companies,
        page=1,
        per_page=8,
    )

    companies_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    text = 'Выбери компанию!'

    reply_markup = manager_company_button(
        change=ManagerState.change,
        page=1,
        companies_button=companies_button,
        pagination_button=pagination_button,
    )

    msg = await message.answer(
        text=text,
        reply_markup=reply_markup,
    )

    await state.set_state(ManagerState.COMPANY)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@manager_router.callback_query(
    ManagerState.EMAIL,
    ManagerChangeFilter(),
)
async def company_callback_manager(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    await state.update_data({
        'email': ManagerState.change.email,
        'page': 1,
    })

    companies = await company_all(
        session=session,
    )

    paginator = Paginator(
        array=companies,
        page=1,
        per_page=8,
    )

    companies_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    text = 'Выбери компанию!'

    reply_markup = manager_company_button(
        change=ManagerState.change,
        page=1,
        companies_button=companies_button,
        pagination_button=pagination_button,
    )

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(ManagerState.COMPANY)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@manager_router.callback_query(
    ManagerState.COMPANY,
    ManagerCompanyNextFilter(),
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

    companies = await company_all(
        session=session,
    )

    paginator = Paginator(
        array=companies,
        page=page,
        per_page=8,
    )

    companies_button = paginator.get_page()
    pagination_button = pages(
        paginator=paginator,
    )

    text = 'Выбери компанию!'

    reply_markup = manager_company_button(
        change=ManagerState.change,
        page=page,
        companies_button=companies_button,
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


@manager_router.callback_query(
    ManagerState.COMPANY,
    ManagerCompanyConfirmFilter(),
)
async def confirm_manager(
        callback: CallbackQuery,
        state: FSMContext,
):
    await state.update_data({
        'company_id': int(callback.data.split('_')[-1]),
    })

    text = 'сохранить новую сиви?'

    reply_markup = manager_confirm_button()

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(ManagerState.CONFIRM)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@manager_router.callback_query(
    ManagerState.COMPANY,
    ManagerChangeFilter(),
)
async def confirm_callback_company(
        callback: CallbackQuery,
        state: FSMContext,
):
    await state.update_data({
        'company_id': ManagerState.change.company_id,
    })

    text = 'сохранить новую сиви?'

    reply_markup = manager_confirm_button()

    msg = await callback.message.edit_text(
        text=text,
        reply_markup=reply_markup,
    )

    await callback.answer()
    await state.set_state(ManagerState.CONFIRM)

    await state.update_data({
        'massage_id': msg.message_id,
    })


@manager_router.callback_query(
    ManagerState.CONFIRM,
    ManagerConfirmFilter(),
)
async def finish_manager(
        callback: CallbackQuery,
        session: AsyncSession,
        state: FSMContext,
):
    state_data = await state.get_data()

    if ManagerState.change:
        await manager_update(
            session=session,
            manager_id=ManagerState.change.id,
            first_name=state_data['first_name'],
            phone=state_data['phone'],
            whatsapp=state_data['whatsapp'],
            email=state_data['email'],
            company_id=state_data['company_id'],
        )

        text = f'Данные о сиви были обновлены в базу данных!'

    else:
        await manager_create(
            session=session,
            first_name=state_data['first_name'],
            phone=state_data['phone'],
            whatsapp=state_data['whatsapp'],
            email=state_data['email'],
            company_id=state_data['company_id'],
            user_id=state_data['user_id'],
        )

        text = f'Данные о сиви были записаны в базу данных!'

    await callback.answer(
        text=text,
        show_alert=True,
    )

    callback_data = MenuData(
        key='profile',
        level=6,
    )

    ManagerState.change = None
    await state.clear()

    return await redirector(
        callback=callback,
        callback_data=callback_data,
        session=session,
    )


@manager_router.message(
    StateFilter(ManagerState),
)
async def error_manager(
        message: Message,
        bot: Bot,
        session: AsyncSession,
        state: FSMContext,
):
    state_data = await state.get_data()

    await message.delete()
    await bot.delete_message(
        chat_id=message.chat.id,
        message_id=state_data['massage_id'],
    )

    state_position = await state.get_state()

    if state_position == ManagerState.NAME:
        text = 'не правильное имя'

        reply_markup = manager_cancel_button(
            change=ManagerState.change,
        )

    elif state_position == ManagerState.PHONE:
        text = 'Я тебя не понимаю отправь правильный номер'

        reply_markup = manager_return_button(
            change=ManagerState.change,
        )

    elif state_position == ManagerState.WHATSAPP:
        text = 'выбери да или нет'

        reply_markup = manager_whatsapp_button(
            change=ManagerState.change,
        )

    elif state_position == ManagerState.EMAIL:
        text = 'Я тебя не понимаю отправь правильный почту'

        reply_markup = manager_return_button(
            change=ManagerState.change,
        )

    elif state_position == ManagerState.COMPANY:
        companies = await company_all(
            session=session,
        )

        paginator = Paginator(
            array=companies,
            page=state_data['page'],
            per_page=8,
        )

        companies_button = paginator.get_page()
        pagination_button = pages(
            paginator=paginator,
        )

        text = 'Выбери компанию!'

        reply_markup = manager_company_button(
            change=ManagerState.change,
            page=1,
            companies_button=companies_button,
            pagination_button=pagination_button,
        )

    else:
        text = 'Я тебя не понимаю ты хочешь записать в базу данных?'

        reply_markup = manager_confirm_button()

    msg = await message.answer(
        text=text,
        reply_markup=reply_markup,
    )

    await state.update_data({
        'massage_id': msg.message_id,
    })
