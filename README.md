# Объектно-ориентированное программирование

Объектно-ориентированное программирование, или ООП — это одна из парадигм разработки.

В коде, написанном по парадигме ООП, выделяют четыре основных элемента:

1. Объект.

Часть кода, которая описывает элемент с конкретными характеристиками и функциями. Карточка товара в каталоге интернет-магазина — это объект. 
Кнопка «заказать» — тоже.

2. Класс.

Шаблон, на базе которого можно построить объект в программировании. Например, у интернет-магазина может быть класс «Карточка товара», который описывает 
общую структуру всех карточек. И уже из него создаются конкретные карточки — объекты. 

Классы могут наследоваться друг от друга. Например, есть общий класс «Карточка товара» и вложенные классы, или подклассы: «Карточка бытовой техники», 
«Карточка ноутбука», «Карточка смартфона». Подкласс берёт свойства из родительского класса, например, цену товара, количество штук на складе или производителя. 
При этом имеет свои свойства, например, диагональ дисплея для «Карточки ноутбука» или количество сим-карт для «Карточки смартфона».

3. Метод.

Функция внутри объекта или класса, которая позволяет взаимодействовать с ним или другой частью кода. В примере с карточками товара метод может: 

● Заполнить карточку конкретного объекта нужной информацией. 
● Обновлять количество товара в наличии, сверяясь с БД. 
● Сравнивать два товара между собой. 
● Предлагать купить похожие товары.

4. Атрибут.

Характеристики объекта в программировании — например, цена, производитель или объём оперативной памяти. В классе прописывают, что такие атрибуты есть, а в 
объектах с помощью методов заполняют эти атрибуты данными.

![1](https://avatars.mds.yandex.net/get-lpc/1220100/ccaaa3b8-13a6-4b00-9010-b98cb70f8047/width_1280_q70)

![2](https://avatars.mds.yandex.net/get-lpc/1364677/fcbb82ee-3dee-4a74-a0b6-c7b11ca10122/width_1280_q70)

## Инкапсуляция

Вся информация, которая нужна для работы конкретного объекта, должна храниться внутри этого объекта. Если нужно вносить изменения, методы для этого 
тоже должны лежать в самом объекте — посторонние объекты и классы этого делать не могут. Для внешних объектов доступны только публичные атрибуты и методы. 

Такой принцип обеспечивает безопасность и не даёт повредить данные внутри какого-то класса со стороны. Ещё он помогает избежать случайных зависимостей, 
когда из-за изменения одного объекта что-то ломается в другом.

## Наследование

В этом принципе — вся суть объектно-ориентированного программирования. 

Разработчик создаёт: 

● Класс с определёнными свойствами;

● Подкласс на его основе, который берёт свойства класса и добавляет свои;

● Объект подкласса, который также копирует его свойства и добавляет свои. 

Каждый дочерний элемент наследует методы и атрибуты, прописанные в родительском. Он может использовать их все, отбросить часть или добавить новые.
При этом заново прописывать эти атрибуты и методы не нужно. 

## Полиморфизм

Один и тот же метод может работать по-разному в зависимости от объекта, где он вызван, и данных, которые ему передали. 
Например, метод «Удалить» при вызове в корзине удалит товар только из корзины, а при вызове в карточке товара — удалит саму карточку из каталога. 

То же самое с объектами. Можно использовать их публичные методы и атрибуты в других функциях и быть уверенным, что всё сработает нормально. 

Этот принцип ООП, как и другие, обеспечивает отсутствие ошибок при использовании объектов.

# Преимущества и недостатки

### Преимущества ООП:

● В парадигме объектов легче писать код. Удобно один раз создать класс или метод, а потом его использовать. 
Не нужно повторно переписывать десятки строк кода. Можно пользоваться специальными рекомендациями по написанию ООП-кода — SOLID. 

● Читать код гораздо проще. Даже в чужом коде обычно сразу видны конкретные объекты и методы, их удобно искать, чтобы посмотреть, что именно они делают. 

● Код легче обновлять. Класс или метод достаточно изменить в одном месте, чтобы он изменился во всех наследуемых классах и объектах. 
Не нужно переписывать каждый объект отдельно, выискивая, где именно в коде он расположен. 

● Программистам удобнее работать в команде. Разные люди могут отвечать за разные объекты и при этом пользоваться плодами трудов коллег. 

● Код можно переиспользовать. Один раз написанный класс или объект можно затем переносить в другие проекты. Достаточно однажды написать объект «Кнопка заказа»
и потом можно вставлять его в почти неизменном виде в разные каталоги товаров и мобильные приложения. 

● Шаблоны проектирования. Именно на базе ООП построены готовые решения для взаимодействия классов друг с другом, которые позволяют не писать этот код 
с нуля, а взять шаблон.

### Недостатки ООП:

● Сложность в освоении. ООП сложнее, чем функциональное программирование. Для написания кода в этой парадигме нужно знать гораздо больше. 
Поэтому перед созданием первой рабочей программы придётся освоить много информации: разобраться в классах и наследовании, научиться писать публичные и внутренние 
функции, изучить способы взаимодействия объектов между собой. 

● Громоздкость. Там, где в функциональном программировании хватит одной функции, в ООП нужно создать класс, объект, методы и атрибуты. 
Для больших программ это плюс, так как структура будет понятной, а для маленьких может оказаться лишней тратой времени. 

● Низкая производительность. Объекты потребляют больше памяти, чем простые функции и переменные. Скорость компиляции от этого тоже страдает.
