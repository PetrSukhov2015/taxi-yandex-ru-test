# taxi-yandex-ru-test

##tests
|id   |prior   |name   |steps   |result   |label|
|-----|--------|-------|--------|---------|-----|
| 1  | blocker  | search test  | fill from,to,phone, call taxi, put code,check order  |  order is completed | automatization|
|  2 | blocker  | search test  | don't fill anything, call taxi  | error message  | automatization|
| 3  |  critical | search test   | click demo with default from  | check order  | automatization|
| 4  |  critical | search test   | click demo with default from  | check order  | automatization|

## autotests
### installation
```
git clone https://github.com/PetrSukhov2015/taxi-yandex-ru-test.git
pip install seleneium allure pytest
py.test test.py
```

### kit
*test.py* - test suite
*page* - pages for page object pattern
*helper* - helpers (P.S. in driver.py set valid path for chromedriver)
*locator* - dom locators
*driver* - dir for web drivers, apk and ipa
*result* - report dir

