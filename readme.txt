# pytest . --alluredir=allure-results
# pytest tests/test_show_main_menu_and_all_submenu.py --alluredir=tests/allure_results
# allure.bat serve tests/allure_results

# pytest tests/test_contacts.py --alluredir=allure-results
# allure.bat serve allure-results


# =========================================================
# создать отчёт в заданной директории (allure-report + widgets + summary.json) :
# https://docs.qameta.io/allure-report/#_commandline - здесь описание необходимых опций allure
# allure help
# pytest . --alluredir=allure-results                             - прогнать тесты
# allure.bat generate allure-results -o allure-report --clean     - создать отчёт
# allure.bat open allure-report                                   - открыть отчёт в браузере
# java "-DconfigFile=notifications/telegram.json" -jar notifications/allure-notifications-4.2.1.jar       - скинуть сообщение в телеграм
# =========================================================
