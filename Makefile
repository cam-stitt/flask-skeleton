M4   := $(shell which m4)
DEPS := m4/base.m4

.PHONY : all settings alembic

ifeq ($(shell test -f m4/overrides.m4 || echo n),n)
    .PHONY += m4/overrides.m4
else
    DEPS += m4/overrides.m4
endif

all: settings alembic

settings.py: $(DEPS) app_name/settings.py.m4
	m4 $^ > app_name/$@

settings: settings.py

alembic.ini: $(DEPS) alembic.ini.m4
	m4 $^ > $@

alembic: alembic.ini
