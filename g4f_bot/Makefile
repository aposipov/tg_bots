
all:
		@echo "build and run"

build:
		docker build -t g4f_bot .

run:	build
		docker run --name g4f_cont -v $(PWD)/core_bot/data:/bot/data \
		-d --restart=unless-stopped g4f_bot

clear:
		docker stop g4f_cont
		docker container rm g4f_cont

start:
		python core_bot/main.py