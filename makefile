run-web:
	@make install
	@poetry run streamlit run src/index.py

run-web-custom:
	@make install
	@poetry run streamlit run src/customgpt.py

run-summarizer:
	@make install
	@poetry run streamlit run src/summarizer.py

run-youtube-summarizer:
	@make install
	@poetry run streamlit run src/youtube_summarizer.py

run-youtube-summarizer-long:
	@make install
	@poetry run streamlit run src/youtube_summarizer_long.py

install:
	@poetry install