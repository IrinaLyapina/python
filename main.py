"""" 3. Создайте модуль main.py. Из модулей, реализованных в заданиях 1 и 2, сделайте импорт в main.py всех функций.
 Вызовите каждую функцию в main.py и проверьте, что все работает как надо.
 Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.
"""

# импорт всех модулей
import modul, rend

modul.create_dir()
modul.remove_dir()

# импорт функций из задания 1
from modul import create_dir, remove_dir
create_dir()
remove_dir()