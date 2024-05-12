.PHONY: setup_pyenv create_env_train create_env_optimize setup_aircp uninstall_env_train uninstall_env_optimize

target:
	ifeq ($(arg1), Hello)
	@echo "Did you just say Hello?"
	else
	@echo "What?"
	endif

# make can see env vars too
echo_home:
	@echo $(HOME)

# set makefile variables inside targets
var_inside_target:
	$(eval PYENV_HERE=$(shell which pyenv >/dev/null; echo $$?))
	@echo $(PYENV_HERE)


# Setup pyenv
PYENV_VERSION = 3.9
PYENV_TRAIN = ml_train
PYENV_OPTIMIZE = ml_optimize

# The ; \ at the end makes sure the lines are executed in the same "context"
setup_pyenv:
	@if [ $(shell which pyenv >/dev/null; echo $$?) = "0" ]; then \
		echo "pyenv is already installed"; \
	else \
		echo "pyenv not installed, installing it"; \
		curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash; \
		echo 'export PYENV_ROOT="$$HOME/.pyenv"' >> $(HOME)/.bashrc; \
		echo 'export PATH="$$PYENV_ROOT/bin:$$PATH"' >> $(HOME)/.bashrc; \
		echo 'eval "$$(pyenv init -)"' >> $(HOME)/.bashrc; \
		echo 'eval "$$(pyenv virtualenv-init -)"' >> $(HOME)/.bashrc; \
		. $(HOME)/.bashrc; \
	fi
	pyenv install $(PYENV_VERSION) --skip-existing

create_env_train:
	pyenv virtualenv -f $(PYENV_VERSION) $(PYENV_TRAIN)
	. $(PYENV_ROOT)/versions/$(PYENV_TRAIN)/bin/activate \
		&& pip install -r requirements-train.txt --no-deps

create_env_optimize:
	pyenv virtualenv -f $(PYENV_VERSION) $(PYENV_OPTIMIZE)
	. $(PYENV_ROOT)/versions/$(PYENV_OPTIMIZE)/bin/activate \
		&& pip install -r requirements-optimize.txt --no-deps

setup_aircp:
	echo '123!@#' > $(HOME)/aircp_token
	chmod 600 $(HOME)/aircp_token
	curl -s "https://search-airflow-manager.coccoc.com/shared/aircp" -o aircp
	chmod +x aircp

uninstall_env_train:
	pyenv uninstall -f $(PYENV_TRAIN)

uninstall_env_optimize:
	pyenv uninstall -f $(PYENV_OPTIMIZE)
