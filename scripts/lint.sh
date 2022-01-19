#!/bin/bash
pylint $(find . -name "*.py" | xargs)