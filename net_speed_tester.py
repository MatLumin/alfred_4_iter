import time;
import requests;
import random;

HEADER = {'Cache-Control': 'no-cache'};
HEADER_RESPONSIBLE_FOR_FILE_SIZE = "Content-length";
SAMPLE_FILE_URLS = [
	"https://commons.wikimedia.org/wiki/Commons:Photo_challenge#/media/File:Lake_Huron_sunset.jpg",
	"https://commons.wikimedia.org/wiki/Commons:Photo_challenge#/media/File:Ocean_wave_in_Narragansett,_Rhode_Island.jpg",
	"https://commons.wikimedia.org/wiki/Commons:Photo_challenge#/media/File:Sunset_at_Galveston_Beach,_Texas.jpg",
	"https://commons.wikimedia.org/wiki/Commons:Photo_challenge#/media/File:Sunset_at_Holland_Beach,_Michigan.jpg",
	"https://commons.wikimedia.org/wiki/Commons:Photo_challenge#/media/File:Waves_crashing_on_rocks_at_Windansea_Beach,_San_Diego,_California.jpg",
	"https://commons.wikimedia.org/wiki/Commons:Photo_challenge#/media/File:Amr20-174.jpg",
	];
UNIT_OF_CONTENT_LENGTH_IN_BITS = 8;
MEGA_BYTE_COEF = 10**6;

def give_me_a_random_file_url()->str:
	return random.choice(SAMPLE_FILE_URLS);


def get_file_size_from_url(url:str)->int:
	resp:requests.response = requests.head(url);
	return int(resp.headers[HEADER_RESPONSIBLE_FOR_FILE_SIZE]);


def just_get_file_and_return_nothing(url:str)->None:
	requests.get(url, headers=HEADER);
	return None;


def get_net_speed_in_bytes()->float:
	RAND_URL:str = give_me_a_random_file_url();
	FILE_SIZE_IN_BYTES = get_file_size_from_url(url=RAND_URL);
	print(F"file size is {FILE_SIZE_IN_BYTES}");
	print(F"trying to get the file");
	START_TIME:int = time.time();
	just_get_file_and_return_nothing(url=RAND_URL);
	END_TIME:int = time.time();	
	print("got the file");
	TOTAL_TIME:int = END_TIME-START_TIME;
	print(f"TOTAL_TIME : {TOTAL_TIME} ");
	NET_SPEED:float = FILE_SIZE_IN_BYTES / TOTAL_TIME;
	print(f"NET_SPEED : {NET_SPEED}");
	return NET_SPEED;

def get_net_speed_in_mega_bytes()->float:
	return 



print(get_net_speed_in_mega_bytes());


