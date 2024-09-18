from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Информация')],
        [KeyboardButton(text='Рассчитать')],
        [KeyboardButton(text='Купить')],
    ], resize_keyboard=True)

produkt_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Анальгин', callback_data='Analgin')],
        [InlineKeyboardButton(text='Витамин В12', callback_data='Vitamin B12')],
        [InlineKeyboardButton(text='Ибупрофен', callback_data='Ibuprofen')],
        [InlineKeyboardButton(text='Фестал', callback_data='Festal')],
    ])

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb.add(button)
kb.add(button2)


@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=start_menu)


@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    await message.answer(text='Выберите продукт для покупки:', reply_markup=produkt_menu)


@dp.callback_query_handler(lambda call: call.data in ['Analgin', 'Vitamin B12', 'Ibuprofen', 'Festal'])
async def show_product_info(call: types.CallbackQuery):
    product_info = {
        'Analgin': {
            'name': 'Анальгин',
            'description': 'Анальгин - это эффективное обезболивающее лекарственное средство, '
                           'которое используется для снятия различных видов болей. '
                           'Он содержит активное вещество метамизол натрия, который обладает анальгезирующим, '
                           'жаропонижающим и спазмолитическим действием. Препарат может применяться при зубной, '
                           'головной, мышечной боли, а также при женских болезнях, артритах, радикулите и '
                           'других болезнях. Анальгин 500 мг выпускается в виде таблеток. '
                           'Доза зависит от выраженности боли или лихорадки, '
                           'а также индивидуальной восприимчивости к действию анальгетиков. '
                           'Таблетки следует проглатывать целиком, запивая достаточным количеством жидкости '
                           '(например, стаканом воды). Продолжительность приема не более 5 дней в качестве '
                           'обезболивающего средства и не более 3 дней в качестве жаропонижающего. '
                           'Перед применением рекомендуется проконсультироваться с врачом.',
            'price': 100,
            'image': 'F:\\Documents\\Proekty\\Доработка_бота\\Анальгин.png'
        },
        'Vitamin B12': {
            'name': 'Витамин В12',
            'description': 'Витамин В12 - главная функция цианокобаламина — его участие в развитии клеток крови.'
                           ' Недостаток витамина В12 приводит к замедлению образования и снижению количества '
                           'новых элементов крови.'
                           'Еще одна функция витамина В12 — участие в образовании нервных волокон, '
                           'где он выступает в роли строительного материала для формирования '
                           'оболочки нервной клетки. Обмен белков, необходимых для роста и развития клеток, '
                           'также не обходится без цианокобаламина. Кроме того, витамин B12 нужен для '
                           'образования активной формы фолиевой кислоты и предотвращения '
                           'кислородного голодания клеток. Он синтезируется лишь микроорганизмами и '
                           'полностью отсутствует в растительной пище.',
            'price': 200,
            'image': 'F:\\Documents\\Proekty\\Доработка_бота\\Витамин В12.png'
        },
        'Ibuprofen': {
            'name': 'Ибупрофен',
            'description': 'Ибупрофен - это лекарственный препарат, предназначенный для снижения боли, '
                           'воспаления и жара. Препарат доступен в виде таблеток, покрытых оболочкой. '
                           'Он содержит 200 мг ибупрофена в одной таблетке. '
                           'Применяется взрослыми и детьми старше 12 лет по назначению врача. '
                           'Рекомендуется принимать таблетки после еды, запивая достаточным количеством воды. '
                           'Ибупрофен 200 мг является эффективным и безопасным препаратом при соблюдении '
                           'рекомендаций по дозировке и применению.',
            'price': 300,
            'image': 'F:\\Documents\\Proekty\\Доработка_бота\\Ибупрофен.png'
        },
        'Festal': {
            'name': 'Фестал',
            'description': 'Фестал - недостаточность внешнесекреторной функции поджелудочной железы при '
                           'хроническом панкреатите в сочетании с билиарной недостаточностью вследствие различных '
                           'патологических состояний, клинически проявляющиеся нарушениями переваривания пищи, '
                           'метеоризмом, склонностью к запорам, в составе комбинированной терапии при: 1) диффузных '
                           'заболеваниях печени - алкогольных и токсических поражениях печени, циррозе печени; '
                           '2) больших потерях желчных кислот (у пациентов после холецистэктомии); '
                           '3) нарушении циркуляции желчных кислот, наблюдающемся при дискинезиях '
                           'желчевыводящих путей, дисбактериозах, мальабсорбции; '
                           '4) нарушении нейрогуморальной регуляции процессов желчеобразования и '
                           'желчеотделения при хронических заболеваниях желудочно-кишечного '
                           'тракта - хроническом гастрите, хроническом дуодените, хроническом холецистите; '
                           'Для улучшения переваривания пищи у пациентов с нормальной функцией '
                           'желудочно-кишечного тракта в случае погрешностей в питании, '
                           'а также при нарушениях жевательной функции, вынужденной длительной иммобилизации, '
                           'малоподвижном образе жизни. Подготовка к рентгенологическому и '
                           'ультразвуковому исследованию органов брюшной полости.',
            'price': 400,
            'image': 'F:\\Documents\\Proekty\\Доработка_бота\\Фестал.png'
        }
    }

    product = product_info[call.data]

    buy_button = InlineKeyboardButton(text='Купить', callback_data=f'buy_{call.data}')
    buy_menu = InlineKeyboardMarkup().add(buy_button)

    with open(product['image'], 'rb') as img:
        await bot.send_photo(
            chat_id=call.message.chat.id,
            photo=img,
            caption=f"Название: {product['name']}\nОписание: {product['description']}\nЦена: {product['price']} руб.",
            reply_markup=buy_menu
        )


@dp.callback_query_handler(lambda call: call.data.startswith('buy_'))
async def handle_purchase(call: types.CallbackQuery):
    product_code = call.data.split('_')[1]

    product_names = {
        'Analgin': 'Анальгин',
        'Vitamin B12': 'Витамин В12',
        'Ibuprofen': 'Ибупрофен',
        'Festal': 'Фестал'
    }

    product_name = product_names.get(product_code, 'Продукт')

    await call.message.answer(f'Вы успешно приобрели {product_name}!')
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer(
        'Формула расчёта калорий:\n10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161'
    )
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост (в см):')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес (в кг):')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    weight = data['weight']
    growth = data['growth']
    age = data['age']

    result = (10 * weight) + (6.25 * growth) - (5 * age) - 161
    await message.answer(f'Ваша норма калорий: {result:.2f} ккал в день.')
    await state.finish()


@dp.message_handler(text='Информация')
async def inform(message: types.Message):
    await message.answer('Информация о боте!', reply_markup=start_menu)


@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer(text='Выберите опцию:', reply_markup=kb)


@dp.message_handler()
async def all_message(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
