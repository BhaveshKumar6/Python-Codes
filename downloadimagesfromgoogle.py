from google_images_download import google_images_download   # importing the library

response = google_images_download.googleimagesdownload()    # intialise response

arguments = {"keywords":"bike","limit":5,"print_urls":True} # creating list of arguments
paths = response.download(arguments)                        # passing the arguments to the function
print(paths)                                                # printing absolute paths of the downloaded images
