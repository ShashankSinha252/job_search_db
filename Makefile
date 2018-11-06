add:
	python3 db_create.py
	python3 db_add.py

read:
	python3 db_read.py

clean:
	rm -f job.db
	rm -rf __pycache__

.PHONY: add clean read
