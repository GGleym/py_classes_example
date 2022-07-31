.PHONY: help
help: ## Show this message.
## -----------------------------------------------------------------------------
		@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

.PHONY: run
run: ##  Run application.
		python main.py