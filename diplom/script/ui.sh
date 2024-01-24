#!/bin/bash
cd ../../
pwd
pytest -s -v ./diplom/tests/test_dollar.py --alluredir=results
