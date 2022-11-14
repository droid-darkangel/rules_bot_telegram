from aiogram import Dispatcher, Bot, executor,types
import logging
import database as data

admins_mans_99_years = [873443711, 5444440623]
admin_hearts = [1490294714, 873443711]

mans_99_years_group_id = -1001881199517
hearts_group_id = -1001897792628

gl_admin = 873443711

token = '5404900170:AAG-hQau7mo3a1xtRDkbF8AmRmxnn5OdZK0'

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)



@dp.message_handler(commands=['set_rules'], commands_prefix='!')
async def rules(msg: types.Message):
    group_id = msg.chat.id
    usr_id = msg.from_user.id
    rule = msg.text[10:]

    print(usr_id)
    print(rule)

    if group_id == mans_99_years_group_id and usr_id in admins_mans_99_years:
        data.sql.execute(f"INSERT INTO rul VALUES ('{mans_99_years_group_id}','')")
        data.db.commit()
        data.sql.execute(f'UPDATE rul SET rules = "{rule}" WHERE group_id = "{mans_99_years_group_id}"')
        data.db.commit()

        await msg.answer(f'Правила чата были обновлены, теперь они:\n{rule}')


    elif group_id == hearts_group_id and usr_id in admin_hearts:
        data.sql.execute(f"INSERT INTO rul VALUES ('{hearts_group_id}','')")
        data.db.commit()
        data.sql.execute(f'UPDATE rul SET rules = "{rule}" WHERE group_id = "{hearts_group_id}"')
        data.db.commit()

        await msg.answer(f'Правила чата были обновлены, теперь они:\n{rule}')


    else:
        await msg.answer('Вы не являетесь администратором бота!')




@dp.message_handler(commands=['rules'], commands_prefix = '!')
async def print_rules(msg: types.Message):
    group_id = msg.chat.id
    data.sql.execute(f"SELECT rules FROM rul WHERE group_id = '{group_id}'")
    rule = data.sql.fetchone()[0]

    await msg.answer(f'Правила данного чата:\n{rule}')