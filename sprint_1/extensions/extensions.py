def main():
    print(extensions(input("File name: ")))

def extensions(user_input):
    image_extensions = ["gif", "jpg", "jpeg", "png"]
    user_output_list = user_input.split(".")
    list_size = len(user_output_list)
    if len(user_output_list) > 1 and user_output_list[list_size - 1] != "bin":
        user_extension = user_output_list[list_size - 1].strip().lower().replace("\n", "")
    else:
        return "application/octet-stream"

    if user_extension in image_extensions:
        if user_extension == "jpg":
            return f"image/jpeg"
        return f"image/{user_extension}"
    if user_extension == "txt":
        return f"text/{user_output_list[0]}"
    return f"application/{user_extension}"

main()