# DS_Project

Свой проект я посвятил изучению состояния развития спортивного плавания в различных регионах России. Шаги можно описать примерно так:

1. Первым делом я собрал информацию по количеству бассейнов в каждом регионе. Такую информацию я нашёл на сайте Всероссийской федерации плавания, правда, данные эти за 2019 год. Запарсил с помощью Scrapy. Файл паука — old_pools_spider.py, а собранные данные — это файл pools_2019.json. Кстати, в ходе парсинга пришлось прибегнуть к использованию регулярок: иначе не удавалось избавиться от непонятных символов для отступов и пропусков.

2. Воспользовался готовым geojson датасетом c границами регионов России и их населением.
   - Далее пробовал разными способами пробовал оценить, как количество бассейнов в регионе зависит от населения региона. Для этого строил визуализации, считал корреляции.
   - Создал простую предсказательную модель количества бассейнов по населению региона.
   - Нанёс данные на интерактивную карту

3. Но в большей степени меня интересовало именно развити спортивного плавания, поэтому я также с помощью Scrapy запарсил https://msrfinfo.ru/ — сайт с цифрами и аналитикой развития спорта в России. В частности, собрал оттуда данные по Мастерам спорта России по плаванию в разных регионах.
   - Впоследствии придумал несколько разных метрик для оценки развития плавания
   - Вновь визуализировал заивисмости различных переменных, считал корреляции
   - Нанёс эти новые данные на новую карту

4. Все-все собранные данные поместил в базу данных SQL. С помощью SQL запросов пытался отыскивать интересную информацию, фильтровать, сравнивать, сортировать, находить наиболее преуспевающие в плавании (по различным моим метрикам) регионы.

5. Скромно описал итоги своего анализа.

В самом ноутбуке тоже оставлял комментарии по поводу того, что делаю. Возможно, не всё в должной степени ёмко описал здесь, но подробнее на некоторых деталях останавливался в ноутбуке.
