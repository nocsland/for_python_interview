Группировка и запуск по группам

Группировка тестов:
@pytest.mark.<имя метки>

Запуск по группам:
pytest -m <имя метки> -v

запрос всех маркеров:
pytest --markers

зарегистрированные маркеры

@pytest.mark.filterwarnings(warning): add a warning filter to the given test.
see https://docs.pytest.org/en/latest/warnings.html#pytest-mark-filterwarnings
@pytest.mark.skip(reason=None): skip the given test function with an optional reason. Example: skip(reason="no way of
currently testing this") skips the test.

@pytest.mark.skipif(condition): skip the given test function if eval(condition) results in a True value. Evaluation
happens within the module global context. Example: skipif('sys.platform == "win32"') skips the test if we are on the
win32 platform. see https://docs.pytest.org/en/latest/skipping.html

@pytest.mark.xfail(condition, reason=None, run=True, raises=None, strict=False): mark the test function as an expected
failure if eval(condition) has a True value. Optionally specify a reason for better reporting and run=False if you don't
even want to execute the test function. If only specific exception(s) are expected, you can list them in raises, and if
the test fails in other ways, it will be reported as a true failure. See https://docs.pytest.org/en/latest/skipping.html

@pytest.mark.parametrize(argnames, argvalues): call a test function multiple times passing in different arguments in
turn. argvalues generally needs to be a list of values if argnames specifies only one name or a list of tuples of values
if argnames specifies multiple names. Example: @parametrize('arg1', [1,2]) would lead to two calls of the decorated test
function, one with arg1=1 and another with arg1=2.see https://docs.pytest.org/en/latest/parametrize.html for more info
and examples.

@pytest.mark.usefixtures(fixturename1, fixturename2, ...): mark tests as needing all of the specified fixtures.
see https://docs.pytest.org/en/latest/fixture.html#usefixtures

@pytest.mark.tryfirst: mark a hook implementation function such that the plugin machinery will try to call it first/as
early as possible.

@pytest.mark.trylast: mark a hook implementation function such that the plugin machinery will try to call it last/as
late as possible.

Использование опции -k "имя" для отбора тестов по именам
Опцию -k командной строки можно использовать, чтобы указать подстроку, которая должна присутствовать в именах тестов (
при использовании опции -m проверяется точное совпадение). Это облегчает отбор тестов по именам.
Также допустимо при запуске с параметром -к использование "not" для поиска тестов без ключевого слова
$ pytest -v -k http - запустит все тесты где в названии есть "http"
$ pytest -k "not send_http" -v - запустит все тесты где в названии нет "send_http"
Или отобрать все тесты, в именах которых есть подстрока «http» или «quick»:
$ pytest -k "http or quick" -v

В качестве позиционных аргументов для отбора тестов можно передать pytest один или несколько идентификаторов узлов (см.
ниже). Это облегчает отбор тестов по именам модулей, классов, методов или функций:
$ pytest -v test_server.py::TestClass::test_method

Можно выбрать и сам класс
$ pytest -v test_server.py::TestClass

Или несколько узлов
$ pytest -v test_server.py::TestClass test_server.py::test_send_http

