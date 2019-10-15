clean:
	rm -rf out/


copyassets:
	mkdir -p out/assets
	cp -rf source/templates/assets out/


index:
	python app.py


build: clean copyassets index


