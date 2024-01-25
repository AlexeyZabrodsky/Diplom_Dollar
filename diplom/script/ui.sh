#!/bin/bash
cd ../../
pytest -s -v ./diplom/tests/test_dollar.py --alluredir=results
