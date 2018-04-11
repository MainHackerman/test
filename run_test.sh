#!/bin/bash

python3 projekt.py < test_values > result.txt && python3 test.py < result.txt && rm result.txt