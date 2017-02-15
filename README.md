# selenium-uchiwa

This is dsfaa selenium unit test to check uchiwa

To set up the selenium environment you can take a look at https://gist.github.com/jbadiapa/921c7719c59bfd89cf862fd6bef07d6d

To run the unit test selenium and the firefox plugin are needed.

Before running the test you need to set up 3 arguments:
- username
- password
- uchiwa ip

```
python uchiwa_test.py
.F........
======================================================================
FAIL: test_uchiwa_3_overcloud (__main__.UchiwaSelenium)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "uchiwa_test.py", line 109, in test_uchiwa_3_overcloud
    self._uchiwa_search('overcloud', '3 Items')
  File "uchiwa_test.py", line 103, in _uchiwa_search
    assert items in search.text
AssertionError

----------------------------------------------------------------------
Ran 10 tests in 55.423s

FAILED (failures=1)

```

