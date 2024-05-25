from flask import *;
from return_random_file_path_from_dir import return_random_file_path_from_dir;
import random;
import net_speed_tester;


FIRST_PANEL_VIDEOS_DIR_PATH = "./first_panel_videos";
SECOND_PANEL_VIDEOS_DIR_PATH = "./second_panel_videos";

app = Flask("alfred");


def read_file_contet(file_path):
	with open(file_path) as f1:
		return f1.read();


def write_file(file_path, new_contet):
	with open(file_path, "w") as f1:
		f1.write(new_contet);
		return;


def count_surface_dirs_in_directory(dir_path)->int:
	w = os.walk(dir_path);
	path, sub_dirs, files = w.__next__();
	return len(sub_dirs);




@app.route("/main")
def serve_main_page():
	return read_file_contet("main.html")+"<script>"+read_file_contet("segements.js")+"</script>"+read_file_contet("post_segement.html")+"<style>"+read_file_contet("style.css")+"</style>";



@app.route("/get_font_0")
def get_font_0():
	return send_file("font_0.ttf");


@app.route("/set_segements_data", methods=["POST"])
def set_segments_data():
	new_content = request.json["data"];
	write_file("segements.js", new_content);
	return "200";


@app.route("/get_rand_first_panel_video")
def get_rand_first_panel_video():
	return send_file(FIRST_PANEL_VIDEOS_DIR_PATH+"/"+"0.mp4");


@app.route("/get_rand_second_panel_video")
def get_rand_second_panel_video():
	return send_file(SECOND_PANEL_VIDEOS_DIR_PATH+"/"+"0.mp4");


@app.route("/get_main_logo_of_company")
def get_main_logo_of_comapany():
	return send_file("./company_logos/main.png");



@app.route("/get_play_list_nth_video/{id_of_playlist}/{index}")
def get_play_list_nth_video(id_of_playlist, index):
	dir_of_play_list = "./video_playlists/{id_of_playlist}";
	number_of_videos_in_play_list = count_surface_dirs_in_directory(dir_of_play_list);
	if number_of_videos_in_play_list == 0:
		return send_file("./no_video_found.mp4");
	index = index % number_of_videos_in_play_list; 
	return send_file(f"./video_playlists/{id_of_playlist}/{index}.mp4");


@app.route("/return_random_1000000_chars")
def return_random_100_bytes():
	output = "";
	for i1 in range(1000000):
		output += random.choice("abcdefghijklmnopqrstuvwxyz");
	return output;
    
    
@app.route("/get_net_speed_ib_bytes_per_second")
def get_net_speed_ib_bytes_per_second():
    return str(net_speed_tester.get_net_speed_in_bytes());





app.run();
