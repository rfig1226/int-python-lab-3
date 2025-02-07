# missing import statements should be added here
import wikipedia
import cv2

from images import get_wikipedia_page_thumbnail_url, download_image_from_url


def prompt_for_image():
    """
    Prompts the user for the name of a Wikipedia page and obtains the URL of the thumbnail image of the page.

    return url, page_name: str, str
    """
    try:
        query = input("Enter name of a personality: ")
        results = wikipedia.search(query, results=3)
        select = input(
            f"Select a name from the following list: \n\n1. {results[0]}\n2. {results[1]}\n3. {results[2] } \nEnter the number of the desired name: "
        )

        page_title = results[int(select) - 1]
        url = get_wikipedia_page_thumbnail_url(page_title)

        print(url)
        return url
    except Exception as e:
        print(f"Error: Unable to find image for the given name: {e}")
        return None, None


def convert_image_to_cartoon(image_path):
    """
    Converts an image to a cartoon given the image_path.
    """

    color = cv2.bilateralFilter(image_path, 9, 200, 200)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    cv2.imwrite(image_path, cartoon)


if __name__ == "__main__":

    url = prompt_for_image()
    image = download_image_from_url(url, "new_image")
    convert_image_to_cartoon(image)
