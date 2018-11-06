create:
	python3 db_create.py

add:
	python3 db_add.py

dump:
	python3 db_read.py

clean:
	rm -f job.db
	rm -rf __pycache__

.PHONY: add clean dump create
