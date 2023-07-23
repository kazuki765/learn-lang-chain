run-gpt-web:
	@make install
	@poetry run streamlit run src/index.py

run-gpt-custom:
	@make install
	@poetry run streamlit run src/customgpt.py

install:
	@poetry install