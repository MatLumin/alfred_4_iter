
import os;
import random;


def list_all_files_from_dir(dir_path):
	output = [];
	for i1 in os.scandir(dir_path):
		output.append(i1.name);
	return output;


def return_random_file_path_from_dir(dir_path):
	random_name = random.choice(list_all_files_from_dir(dir_path));
	return os.path.join(dir_path, random_name);



print(return_random_file_path_from_dir("./first_panel_videos"));