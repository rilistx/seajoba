from sqlalchemy.ext.asyncio import AsyncSession

from core.components.paginator import Paginator
from core.keyboards.menu import user_button, admin_button, about_button, support_button
from core.keyboards.profile import profile_manager_button, profile_sailor_button, profile_company_button


from core.components.paginator import Paginator


def pages(
        *,
        paginator: Paginator,
):
    button = dict()

    if paginator.has_previous():
        # button['◀️'] = 'prev'
        button['<<'] = 'prev'

    if paginator.has_next():
        # button['▶️'] = 'next'
        button['>>'] = 'next'

    return button


async def menu_process(
        *,
        session: AsyncSession,
        key: str,
        user_id: int,
):
    if key == 'menu':
        user = await user_search(
            session=session,
            user_id=user_id,
        )

        if user.role == 'admin':
            caption = '<b>🧭 You are in the main menu!</b>'

            button = admin_button(
                premium=user.premium,
            )
        else:
            caption = '<b>🧭 You are in the main menu!</b>'

            button = user_button(
                role=user.role,
                user_id=user.id,
                premium=user.premium,
            )

    elif key == 'about':
        caption = '<b>🧭 You are in the about us!</b>'

        button = about_button()

    else:
        caption = '<b>🧭 You are in the support!</b>'

        button = support_button()

    return caption, button


async def other_menu_process(
        *,
        key: str,
):
    caption = f'{key.capitalize()} panel!'

    button = other_menu_button(
        key=key,
    )

    return caption, button


async def other_view_process(
        *,
        session: AsyncSession,
        key: str,
        page: int,
):
    if key == 'company':
        object_data = await company_all(
            session=session,
        )

    else:
        object_data = await charter_all(
            session=session,
        )

    if object_data:
        paginator = Paginator(
            array=object_data,
            page=page,
            per_page=8,
        )

        other_button = paginator.get_page()
        pagination_button = pages(
            paginator=paginator,
        )

        caption = f'{key.capitalize()} panel!'

        button = other_view_button(
            key=key,
            page=page,
            other_button=other_button,
            pagination_button=pagination_button,
        )

    else:
        caption = f'{key.capitalize()} panel пусто!'

        button = other_view_button(
            key=key,
            page=page,
        )

    return caption, button


async def other_info_process(
        *,
        session: AsyncSession,
        key: str,
        page: int,
        object_id: int,
):
    if key == 'company':
        company = await company_one(
            session=session,
            company_id=object_id,
        )

        caption = f'Information {key.capitalize()} panel!\n\nName {key}: {company.name}\nInfo {key}: {company.info}'
    else:
        charter = await charter_one(
            session=session,
            charter_id=object_id,
        )

        caption = f'Information {key.capitalize()} panel!\n\nName {key}: {charter.name}\nInfo {key}: {charter.info}'

    button = other_info_button(
        key=key,
        page=page,
        object_id=object_id,
    )

    return caption, button


async def profile_menu_process(
        *,
        session: AsyncSession,
        user_id: int,
):
    user = await user_search(
        session=session,
        user_id=user_id,
    )

    if user.role == 'manager':
        information = await manager_search(
            session=session,
            user_id=user.id
        )

        caption = '<b>Пользовательский профиль менеджера!</b>'

        button = profile_manager_button(
            premium=user.premium,
            user_id=user_id,
            information=information,
        )
    else:
        information = await sailor_search(
            session=session,
            user_id=user.id
        )

        caption = '<b>Пользовательский профиль моряка!</b>'

        button = profile_sailor_button(
            premium=user.premium,
            user_id=user_id,
            information=information,
        )

    return caption, button


async def profile_company_process(
        *,
        session: AsyncSession,
        user_id: int,
):
    manager = await manager_one(
        session=session,
        user_id=user_id,
    )

    company = await company_one(
        session=session,
        company_id=manager.company_id,
    )

    caption = '<b>Информация о компании для менеджера!</b>'
    button = profile_company_button()

    return caption, button


async def profile_notice_process(
        *,
        session: AsyncSession,
        user_id: int,
):
    manager = await manager_one(
        session=session,
        user_id=user_id,
    )

    company = await company_one(
        session=session,
        company_id=manager.company_id,
    )

    caption = '<b>Информация о компании для менеджера!</b>'
    button = profile_company_button()

    return caption, button


async def distributor(
        *,
        session: AsyncSession,
        key: str,
        level: int,
        user_id: int,
        page: int | None = None,
        object_id: int | None = None,
):
    if level == 0:
        return await menu_process(session=session, key=key, user_id=user_id)
    elif level == 1:
        return await other_menu_process(key=key)
    elif level == 2:
        return await other_view_process(session=session, key=key, page=page)
    elif level == 3:
        return await other_info_process(session=session, key=key, page=page, object_id=object_id)
    elif level == 4:
        return await profile_menu_process(session=session, user_id=user_id)
    elif level == 5:
        return await profile_company_process(session=session, user_id=user_id)
    elif level == 6:
        return await profile_notice_process(session=session, user_id=user_id)
