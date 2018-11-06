add:
	python3 db_create.py
	python3 db_add.py

read:
	python3 db_read.py

clean:
	rm -f job.db

.PHONY: add clean read
