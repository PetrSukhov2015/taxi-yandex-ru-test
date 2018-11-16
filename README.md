# taxi-yandex-ru-test

## tests

https://taxi.yandex.ru/#index
Tests for taxi yandex

|id   |prior   |name   |steps   |result   |label|
| --- | ------ | ----- | ------ | ------- | --- |
| 1  | blocker  | search test positive | fill from,to,phone, call taxi, put code,check order  |  order is completed | automatization|
| 2 | blocker  | search test  | don't fill anything, call taxi  | error message  | automatization|
| 3  |  critical | search test   | click demo with default from  | check order  | automatization|
| 4  |  blocker | search test bound val1  | set near state adresses, choose  10 min  | check order  | manual|
| 5  |  blocker | search test  bound val1  | set far state adresses, choose requirements with condition | check order  | manual|

## autotests
### environmanet
```
windows
chrome
chromedriver
set path to chrome driver in helper\driver.py
python 3.7
```
### installation
```
git clone https://github.com/PetrSukhov2015/taxi-yandex-ru-test.git
pip install seleneium allure pytest
py.test test.py
```

### kit
- **test.py** - test suite
- **page** - pages for page object pattern
- **helper** - helpers (P.S. in driver.py set valid path for chromedriver)
- **locator** - dom locators
- **driver** - dir for web drivers, apk and ipa
- **result** - report dir

