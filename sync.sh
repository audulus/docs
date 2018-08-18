#!/bin/sh
mkdocs build --clean
rsync -avze ssh site/ wtholliday@audulus.com:docs.audulus.com --delete
