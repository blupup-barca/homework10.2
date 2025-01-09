# Проект "Виджет операций"

## Описание
Проект будет на бекенде готовить данные для отображения в виджете с несколькими последними успешными банковскими операциями клиента

## Установка
1. Клонируйте репозиторий
2. Установите зависимости

## Использование

### Функции проекта:
- **mask_account_card**: принимает строку, содержащую тип и номер карты или счета. Возвращает строку с замаскированным номером карты/счета
- **get_date**: принимает строку с датой в формате iso 8601. Возвращает строку с датой в формате ДД.ММ.ГГГГ
- **filter_by_state**: Принимает список словарей и опционально значение для ключа state. Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению (по умолчанию - "EXECUTED")
- **sort_by_date**: Принимает список словарей. Возвращает новый список, отсротированный по дате. По умолчанию сортировка идет по убыванию, чтобы изменить порядок - при вызове функции вторым аргументом необходимо передать булевое значение "False"
- **filter_by_currency**: Принимает список словарей, представляющих транзакции. Возвращает по одному словарю из списка, в котором валюта операции соответствует заданной (по умолчанию USD, для изменения вторым аргументом надо передать буквенный код интересующей валюты, например "RUB"
- **transaction_descriptions**: Принимает список словарей, представляющих транзакции. Возвращает описания (description) каждой операции из списка по одному
- **card_number_generator**: Генерирует 16-значные номера карт в рамках заданнного диапазона. При вызове генератора первым аргументом передаем начальное значение генерации диапазона, вторым аргументом передаем конечное значение диапазона (включительно). То есть, если передать в качестве аргументов значения 1 и 5, то будут сгенерированы номера карт: "0000 0000 0000 0001", "0000 0000 0000 0002" и далее пока не дойдет до "0000 0000 0000 0005" На вход может принимать как данные в формате int, так и в формате string
### Проверка линтерами Flake8 и mypy
Линтеры *Flake8* и *mypy* находят 5 ошибjr в функциональном коде

### Тестирование
Тестами покрыто 98% кода. Все тесты завершаются ожидаемым образом

## Команда проекта:
* Александра Черникова — Back-End 
## Контакт для связи с командой разработки:
* chernikova.sasha@yandex.ru
## Источники
[Программа создана при поддержке онлайн-школы] (skypro@skyeng.ru) ![(По домашнему заданию)] (<?xml version="1.0" encoding="UTF-8"?> <svg xmlns="http://www.w3.org/2000/svg" width="182" height="29" viewBox="0 0 182 29" fill="none"> <rect x="100.923" width="80.5983" height="28.0342" rx="14.0171" fill="white" fill-opacity="0.05"></rect> <path d="M113.399 18.6446C115.431 18.6446 116.945 17.1447 116.945 15.0001C116.945 12.8555 115.431 11.3557 113.399 11.3557C111.366 11.3557 109.852 12.8555 109.852 15.0001C109.852 17.1447 111.366 18.6446 113.399 18.6446ZM113.399 17.355C112.179 17.355 111.254 16.4158 111.254 15.0001C111.254 13.5844 112.179 12.6453 113.399 12.6453C114.618 12.6453 115.543 13.5844 115.543 15.0001C115.543 16.4158 114.618 17.355 113.399 17.355ZM121.094 18.5044V12.7854H123.365V11.4959H117.422V12.7854H119.693V18.5044H121.094ZM127.548 10.4306C127.548 11.8323 128.319 12.6593 129.272 13.3181L130.38 14.089C131.095 14.5796 131.627 15.1403 131.627 16.0094C131.627 16.8504 131.081 17.355 130.211 17.355C129.356 17.355 128.796 16.7382 128.796 15.743V15.0562H127.394V15.8411C127.394 17.6494 128.656 18.6446 130.211 18.6446C131.767 18.6446 133.029 17.7194 133.029 15.8411C133.029 14.4815 132.258 13.6825 131.319 13.0237L130.183 12.2107C129.497 11.7482 128.95 11.2576 128.95 10.4306C128.95 9.58953 129.455 9.14098 130.197 9.14098C130.982 9.14098 131.473 9.61756 131.473 10.6969V11.2996H132.875V10.6548C132.875 8.76252 131.697 7.85141 130.197 7.85141C128.74 7.85141 127.548 8.59431 127.548 10.4306ZM135.984 7.99158H134.583V18.5044H135.984V14.8179L139.335 18.5044H141.115L137.568 14.6917L140.862 11.4959L138.998 11.4959L135.984 14.6076V7.99158ZM145.339 19.2894L148.101 11.4959H146.699L144.681 17.369L142.648 11.4959H141.246L144.022 19.2753C143.573 20.3687 143.097 20.8873 142.214 20.8873C141.877 20.8873 141.555 20.8172 141.288 20.7331V21.9666C141.555 22.0507 141.947 22.1208 142.34 22.1208C144.064 22.1208 144.751 20.9574 145.339 19.2894ZM155.537 15.4767C155.551 15.3225 155.565 15.1683 155.565 15.0001C155.565 12.8555 154.107 11.3557 152.116 11.3557C150.126 11.3557 148.668 12.8555 148.668 15.0001C148.668 17.1447 150.126 18.6446 152.116 18.6446C153.728 18.6446 154.948 17.8456 155.382 16.4018H153.868C153.588 17.0326 153.027 17.4111 152.172 17.4111C150.995 17.4111 150.21 16.6962 150.042 15.4767H155.537ZM152.116 12.5892C153.238 12.5892 154.009 13.29 154.177 14.4675H150.056C150.224 13.29 150.981 12.5892 152.116 12.5892ZM161.885 14.6777V18.5044H163.287V14.3974C163.287 12.3369 162.151 11.3557 160.623 11.3557C159.698 11.3557 158.927 11.7902 158.493 12.6032V11.4959H157.091V18.5044H158.493V14.6777C158.493 13.29 159.138 12.5892 160.189 12.5892C161.24 12.5892 161.885 13.29 161.885 14.6777ZM168.101 18.6446C169.04 18.6446 169.853 18.196 170.4 17.4531V18.5605C170.4 19.9061 169.643 20.8593 168.353 20.8593C167.26 20.8593 166.503 20.1724 166.321 19.1211H164.905C165.157 20.9294 166.517 22.1488 168.353 22.1488C170.274 22.1488 171.801 20.6911 171.801 18.5605V11.4959H170.4V12.5471C169.853 11.8042 169.04 11.3557 168.101 11.3557C166.181 11.3557 164.737 12.8555 164.737 15.0001C164.737 17.1447 166.181 18.6446 168.101 18.6446ZM168.269 17.355C167.05 17.355 166.139 16.4158 166.139 15.0001C166.139 13.5844 167.05 12.6453 168.269 12.6453C169.489 12.6453 170.4 13.5844 170.4 15.0001C170.4 16.4158 169.489 17.355 168.269 17.355Z" fill="white"></path> <path d="M2.46829 20.0297C1.0319 20.8594 6.10352e-05 20.168 6.10352e-05 18.9382C6.10352e-05 17.629 6.10352e-05 13.7008 6.10352e-05 13.7008C6.10352e-05 13.7008 6.10352e-05 9.77258 6.10352e-05 8.46338C6.10352e-05 7.23357 1.03126 6.54216 2.46829 7.37185C4.70543 8.66376 11.4162 12.5408 11.4162 12.5408C12.3085 13.0561 12.3085 14.3448 11.4162 14.8602C11.4162 14.8608 4.70543 18.7378 2.46829 20.0297Z" fill="#00C1FF"></path> <path d="M9.85464 20.0293C8.41825 20.8589 7.38641 20.1675 7.38641 18.9377C7.38641 17.6285 7.38641 13.7003 7.38641 13.7003C7.38641 13.7003 7.38641 9.77209 7.38641 8.46289C7.38641 7.23308 8.41761 6.54167 9.85464 7.37136C12.0425 8.63511 18.6061 12.427 18.6061 12.427C19.5861 12.9929 19.5861 14.4077 18.6061 14.9737C18.6054 14.9737 12.0425 18.7655 9.85464 20.0293Z" fill="#BCEC30"></path> <mask id="mask0_18110_11854" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="7" y="7" width="13" height="14"> <path d="M9.85464 20.0293C8.41825 20.8589 7.38641 20.1675 7.38641 18.9377C7.38641 17.6285 7.38641 13.7003 7.38641 13.7003C7.38641 13.7003 7.38641 9.77209 7.38641 8.46289C7.38641 7.23308 8.41761 6.54167 9.85464 7.37136C12.0425 8.63511 18.6061 12.427 18.6061 12.427C19.5861 12.9929 19.5861 14.4077 18.6061 14.9737C18.6054 14.9737 12.0425 18.7655 9.85464 20.0293Z" fill="#6FE4FF"></path> </mask> <g mask="url(#mask0_18110_11854)"> <g filter="url(#filter0_f_18110_11854)"> <path d="M2.46841 20.03C1.03202 20.8597 0.000183105 20.1683 0.000183105 18.9385C0.000183105 17.6293 0.000183105 13.701 0.000183105 13.701C0.000183105 13.701 0.000183105 9.77282 0.000183105 8.46363C0.000183105 7.23382 1.03138 6.54241 2.46841 7.3721C4.70556 8.66401 11.4164 12.541 11.4164 12.541C12.3087 13.0564 12.3087 14.3451 11.4164 14.8604C11.4164 14.8611 4.70556 18.7381 2.46841 20.03Z" fill="#99D100"></path> </g> </g> <path d="M24.1428 16.0382L24.3931 15.4684C24.5637 15.081 24.8708 14.9784 25.2575 15.2633C25.9968 15.8103 27.2138 16.2091 28.8403 16.2091C30.2279 16.2091 30.8193 15.8559 30.8193 15.4342C30.8193 14.9556 30.3302 14.8303 29.5227 14.7277L27.6801 14.4884C25.4622 14.1921 24.3476 13.3944 24.3476 12.0042C24.3476 10.5113 25.5646 9.32617 28.3853 9.32617C29.9549 9.32617 30.9672 9.56548 31.6269 9.81618C32.3548 10.1011 32.4572 10.3404 32.4572 10.933V11.7079C32.4572 12.1865 32.2866 12.346 31.8202 12.346H31.297C30.8193 12.346 30.6601 12.1751 30.6601 11.7079V11.4572C30.353 11.3546 29.5909 11.2065 28.7038 11.2065C27.1455 11.2065 26.3949 11.4913 26.3949 11.97C26.3949 12.3232 26.8498 12.5284 27.6801 12.6423L29.4886 12.8816C31.6724 13.1551 32.8325 13.8161 32.8325 15.4115C32.8325 17.0296 31.297 18.0666 28.5559 18.0666C26.5427 18.0666 24.9276 17.4285 24.2793 16.8359C24.0518 16.608 24.0177 16.3231 24.1428 16.0382Z" fill="white"></path> <path d="M44.1142 17.9294H43.1815C42.7266 17.9294 42.5787 17.861 42.3512 17.5192L40.5996 14.9323C40.3494 14.5791 40.1561 14.4879 39.6329 14.4879H37.8813V17.2912C37.8813 17.7699 37.7107 17.9294 37.2443 17.9294H36.5733C36.0956 17.9294 35.9363 17.7585 35.9363 17.2912V8.88125H35.3108C34.8331 8.88125 34.6738 8.71032 34.6738 8.2431V7.67331C34.6738 7.1947 34.8444 7.03516 35.3108 7.03516H37.2557C37.7334 7.03516 37.8927 7.20609 37.8927 7.67331V12.5962H39.4623C39.9855 12.5962 40.1674 12.5165 40.429 12.1518L41.8963 9.88407C42.1351 9.5308 42.283 9.46243 42.7379 9.46243H43.6706C44.1824 9.46243 44.2734 9.87267 43.9891 10.2943L42.3512 12.7786C42.1806 13.0179 41.9759 13.2686 41.7825 13.4737C41.9873 13.6446 42.2716 13.9295 42.3854 14.1005L44.4327 17.1203C44.717 17.5192 44.6146 17.9294 44.1142 17.9294Z" fill="white"></path> <path d="M47.4425 19.479V18.9206C47.4425 18.442 47.6131 18.2825 48.0794 18.2825H48.887C49.376 18.2825 49.6149 18.1799 49.7969 17.7925L49.8992 17.5759L46.0321 10.2485C45.7933 9.80411 45.9866 9.47363 46.4871 9.47363H47.3629C47.8178 9.47363 48.0225 9.5534 48.1932 9.88388L49.8083 13.2114C50.1836 13.9749 50.6044 14.8524 50.9343 15.6159C51.2755 14.8752 51.6622 14.0205 52.0262 13.2798L53.6754 9.88388C53.8233 9.5648 54.0507 9.47363 54.5057 9.47363H55.3815C55.8933 9.47363 56.0753 9.8155 55.8364 10.2485L51.4347 18.6243C50.9229 19.593 50.3428 20.1286 49.0235 20.1286H48.0567C47.6017 20.1286 47.4425 19.9576 47.4425 19.479Z" fill="white"></path> <path d="M67.7301 13.7021C67.7301 16.3915 65.7397 18.0666 63.0554 18.0666C61.8953 18.0666 61.0081 17.7817 60.3826 17.4285V19.7304C60.3826 20.209 60.2119 20.3686 59.7456 20.3686H59.0746C58.5969 20.3686 58.4376 20.1976 58.4376 19.7304V11.3204H57.8121C57.3343 11.3204 57.1751 11.1495 57.1751 10.6823V10.1125C57.1751 9.63385 57.3457 9.47432 57.8121 9.47432H59.4499C59.9276 9.47432 60.0868 9.64525 60.0868 10.1125V10.1581C60.7238 9.73642 61.6906 9.32617 63.0554 9.32617C65.7397 9.33757 67.7301 11.0127 67.7301 13.7021ZM65.7056 13.7021C65.7056 12.1295 64.443 11.252 62.8734 11.252C61.7474 11.252 60.8261 11.7307 60.3939 12.1181V15.2975C60.8375 15.6849 61.7474 16.1636 62.8734 16.1636C64.443 16.1522 65.7056 15.2747 65.7056 13.7021Z" fill="white"></path> <path d="M78.3273 13.041C78.3273 13.5196 78.1567 13.6791 77.6903 13.6791H77.0193C76.5416 13.6791 76.3823 13.5424 76.3823 13.041C76.3823 11.7875 75.9046 11.2291 74.7672 11.2291C73.6867 11.2291 72.7882 11.9014 72.2877 12.7219V17.2916C72.2877 17.7702 72.1171 17.9297 71.6508 17.9297H70.9797C70.502 17.9297 70.3428 17.7588 70.3428 17.2916V11.3202H69.7172C69.2395 11.3202 69.0803 11.1493 69.0803 10.6821V10.1123C69.0803 9.63369 69.2509 9.47415 69.7172 9.47415H71.355C71.8328 9.47415 71.992 9.64508 71.992 10.1123V10.6593C72.5948 9.98695 73.5161 9.3374 75.0857 9.3374C77.3832 9.3374 78.3273 10.7049 78.3273 13.041Z" fill="white"></path> <path d="M79.5344 13.7019C79.5344 11.1949 81.65 9.3374 84.4593 9.3374C87.2459 9.3374 89.3501 11.1949 89.3501 13.7019C89.3501 16.2204 87.2346 18.0779 84.4593 18.0779C81.65 18.0779 79.5344 16.2204 79.5344 13.7019ZM87.4166 13.7019C87.4166 12.2433 86.1313 11.1835 84.4593 11.1835C82.7532 11.1835 81.468 12.2547 81.468 13.7019C81.468 15.172 82.7532 16.2432 84.4593 16.2432C86.1427 16.2432 87.4166 15.172 87.4166 13.7019Z" fill="white"></path> <defs> <filter id="filter0_f_18110_11854" x="-1.02393" y="5.9854" width="14.1336" height="15.4313" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"> <feFlood flood-opacity="0" result="BackgroundImageFix"></feFlood> <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"></feBlend> <feGaussianBlur stdDeviation="0.512059" result="effect1_foregroundBlur_18110_11854"></feGaussianBlur> </filter> </defs> </svg> ![Group_1321317003](https://github.com/Andrej22071999/poetry_dz/assets/174843439/b08a22aa-61c0-4545-8380-fab9174dd809)
) 