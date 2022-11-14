from aiogram import Dispatcher, Bot, executor,types
import logging
import database as data

admins_1 = []
admins_2 = []

group_id_1 = int
group_id_2 = int

gl_admin = int

token = ''

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

    if group_id == group_id_1 and usr_id in admins_1:
        data.sql.execute(f"INSERT INTO rul VALUES ('{group_id_1}','')")
        data.db.commit()
        data.sql.execute(f'UPDATE rul SET rules = "{rule}" WHERE group_id = "{group_id_1}"')
        data.db.commit()

        await msg.answer(f'Правила чата были обновлены, теперь они:\n{rule}')


    elif group_id == group_id_2 and usr_id in admins_2:
        data.sql.execute(f"INSERT INTO rul VALUES ('{group_id_2}','')")
        data.db.commit()
        data.sql.execute(f'UPDATE rul SET rules = "{rule}" WHERE group_id = "{group_id_2}"')
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
