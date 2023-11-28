clean:
	rm -rf out/


copyassets:
	mkdir -p out/assets
	cp -rf source/templates/assets out/


index:
	python app.py


build: clean copyassets index


pdf:
	google-chrome --headless --print-to-pdf-no-header --run-all-compositor-stages-before-draw --print-to-pdf=Roberto-Prevato-cv.pdf --no-margins ./out/index.html
