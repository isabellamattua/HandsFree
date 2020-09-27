#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def run_quickstart():
    # [START vision_quickstart]
    import io
    import os

    # Imports the Google Cloud client library
    # [START vision_python_migration_import]
    from google.cloud import vision
    from google.cloud.vision import types
    # [END vision_python_migration_import]

    # Instantiates a client
    # [START vision_python_migration_client]
    client = vision.ImageAnnotatorClient()
    # [END vision_python_migration_client]

    # The name of the image file to annotate
    file_name = os.path.abspath('resources/wakeupcat.jpg')

    # Loads the image into memory
    client = vision.ImageAnnotatorClient()

    path = "resources\\frame198.jpg"

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print('Texts:')
    listOfSize = []
    greatestSize = -1
    plate = ""
    TOLERANCE = 0.2
    plateIndex = -1

    if not texts:
        quit()

    for text in texts[1:]:
        #print('\n"{}"'.format(text.description))

        firstY = text.bounding_poly.vertices[1].y
        secondY = text.bounding_poly.vertices[2].y
        size = secondY - firstY
        listOfSize.append(size)
        #print(size)

    index=0
    for size in listOfSize:
        if size > greatestSize:
            greatestSize = size
            indexOfGreatest = index
            #print(plate)
        index = index + 1

    indexOfGreatest +=1
    #plate = texts[indexOfGreatest].description

    toleranceMORE = greatestSize + greatestSize * TOLERANCE
    toleranceLESS = greatestSize - greatestSize * TOLERANCE

    index = 1
    for size in listOfSize:
        if index != indexOfGreatest:
            if toleranceLESS < size < toleranceMORE:
                #plate = plate + texts[index].description
                plateIndex = index
        index +=1


    if plateIndex == -1:
        plate = plate + texts[indexOfGreatest].description
    else:

        if indexOfGreatest < plateIndex:
            plate = plate + texts[indexOfGreatest].description+  plate + texts[plateIndex].description
        else:
            plate = plate + texts[plateIndex].description + texts[indexOfGreatest].description


    print(plate)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))




if __name__ == '__main__':
    print(run_quickstart())