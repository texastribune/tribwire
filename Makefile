MANAGE=python example/manage.py


test:
	$(MANAGE) test tribwire


# quickly reset the tribwire app and only the tribwire app

resetdb:
	$(MANAGE) sqlclear tribwire | $(MANAGE) dbshell
	$(MANAGE) syncdb


.PHONY: test resetdb