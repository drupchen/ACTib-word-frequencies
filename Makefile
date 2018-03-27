.PHONY: help
help:
	@echo "download				download the ACTib collection from Zenodo"

.PHONY: download
download:
		-rm ./ACTib*
		mkdir ./ACTib
		wget https://zenodo.org/record/823707/files/DharmaDownloadPostSegmented.zip -O DharmaDownload.zip
		unzip DharmaDownload.zip -d ./ACTib
		-rm DharmaDownload.zip
		wget https://zenodo.org/record/823707/files/DrikungChetsangPostSegmented.zip -O DrikungChetsang.zip
		unzip DrikungChetsang.zip -d ./ACTib
		-rm DrikungChetsang.zip
		wget https://zenodo.org/record/823707/files/eKangyurPostSegmented.zip -O eKangyur.zip
		unzip eKangyur.zip -d ./ACTib
		-rm eKangyur.zip
		wget https://zenodo.org/record/823707/files/GuruLamaWorksPostSegmented.zip -O GuruLamaWorks.zip
		unzip GuruLamaWorks.zip -d ./ACTib
		-rm GuruLamaWorks.zip
		wget https://zenodo.org/record/823707/files/KarmaDelekPostSegmented.zip -O KarmaDelek.zip
		unzip KarmaDelek.zip -d ./ACTib
		-rm KarmaDelek.zip
		wget https://zenodo.org/record/823707/files/OCR2017PostSegmented.zip -O OCR2017.zip
		unzip OCR2017.zip -d ./ACTib
		-rm OCR2017.zip
		wget https://zenodo.org/record/823707/files/PalriParkhangPostSegmented.zip -O PalriParkhang.zip
		unzip PalriParkhang.zip -d ./ACTib
		-rm PalriParkhang.zip
		wget https://zenodo.org/record/823707/files/ShechenPostSegmented.zip -O Shechen.zip
		unzip Shechen.zip -d ./ACTib
		-rm Shechen.zip
		wget https://zenodo.org/record/823707/files/VajraVidyaPostSegmented.zip -O VajraVidya.zip
		unzip VajraVidya.zip -d ./ACTib
		-rm VajraVidya.zip
		wget https://zenodo.org/record/823707/files/VariousPostSegmented.zip -O Various.zip
		unzip Various.zip -d ./ACTib
		-rm Various.zip
		-rm ./ACTib/__MACOSX
