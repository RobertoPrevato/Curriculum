clean:
	rm -rf out/


copyassets:
	mkdir -p out/assets
	cp -rf source/templates/assets out/


index:
	python app.py


build: clean copyassets index


pdf:
	google-chrome --headless --run-all-compositor-stages-before-draw --print-to-pdf=curriculum.pdf --no-margins ./out/index.html