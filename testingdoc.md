# API Testing : Covid-19 test reader
## Purpose: To test the accuracy

## Input:
> Mode: POST
### Input file type:
- JSON file

Body data:
```JSON
{
    "image_data": "value"
}
```

### Steps to get value:
1. Find the Image of COVID-19 Test
2. Encrypt the value of the image with base64
3. Input the value `"image_data": "(your value)"`

_Example of values -> see bottom of this page or at the test cases_

---

## Output:
### Output file type:
- JSON file

### Output data:
```JSON
{ "result": "value" }
```

### List of important possible result values:
| Value/Error                                    | Status Code  |  Meaning                                                                           |
| ---------------------------------------------- |:------------:|:----------------------------------------------------------------------------------:|
| "positive"                                     |   `200`      | "The Covid-19 Test in the input image is positive."                                |
| "negative"                                     |   `200`      | "The Covid-19 Test in the input image is negative."                                |
| "invalid"                                      |   `200`      | "The Covid-19 Test in the input image is invalid."                                 |
| "Incorrect padding"                            |   `200`      | "Syntax error in the value of image_data."                                         |
| "membrane is missing from the prediction!"     |   `200`      | "The Covid-19 Test in the input image has missing parts that aren't in the image." |
| "Image type <class 'NoneType'> not supported!" |   `200`      | "The input image has syntax error or the input image is blank."                    |
| "kit is missing from the prediction!"          |   `200`      | "The input image doesn't contain a Covid-19 Test."                                 |
| "Unauthorized"                                 |   `401`      | "The API is no longer operating | closed"                                          |
| "Service Unavailiable"                         |   `503`      | "The Server is down or is having issues."                                          |

##### *(Other error, which isn't important aren't listed here.)*

---
## **Normal test cases(positive, negative, invalid)**

## Test case 1: **Positive** Covid-19 test
### Summary: Sucessfully detected a positive COVID-19 Test.
### Input: 
- base64-encrypted .jpg image with a positive COVID-19 Test(clear and all parts of the testkit is visible).
- [JSON file of this case](https://gist.github.com/Orangeboi69/9440168bf8d885f49789a508f5b0ca6d)

### Expected Results: 
- The result is positive(JSON file with the data: `{"result":"positive"}`)

### Actual Results:
###### Response time: ~11.67 second
```JSON
{
    "result": "positive"
}
```
### **Screenshots**:

![screenshot of the sucessful request and response](https://i.imgur.com/9kSreDw.png "Application shown: Postman")

*Original image* :

![orignal picture](https://www.bundesregierung.de/resource/blob/975228/2216894/f9c0c88eeaee1f23b323856d4b310b69/2023-08-30-corona-antigen-schnelltest-data.jpg "covid 19 test - positive")
---
## Test case 2: **Negative** Covid-19 test
### Summary: Sucessfully detected a negative COVID-19 Test.
### Input: 
- base64-encrypted .png image with a negative COVID-19 Test(clear and all parts of the testkit is visible).
- [JSON file of this case](https://gist.github.com/Orangeboi69/fb88f7166f1e7d4f13a088752f556f19)

### Expected Results: 
- The result is negative(JSON file with the data: `{"result":"negative"}`)

### Actual Results:
###### Response time: ~12.57 second
```JSON
{
    "result": "negative"
}
```
### **Screenshots**:

![screenshot of the negative request and response](https://i.imgur.com/cRvtNMg.png "Application shown: Postman")

*Original image* :

![orignal picture](https://thehill.com/wp-content/uploads/sites/2/2022/06/Screen-Shot-2022-06-28-at-10.31.36-AM-e1661615767132.png?w=1280&h=720&crop=1 "covid 19 test - negative")
---
## Test case 3: **Invalid** Covid-19 test
### Summary: Sucessfully detected a invalid COVID-19 Test.
### Input: 
- random base64-encrypted .png image with no COVID-19 Test in the image.
- [JSON file of this case](https://gist.github.com/Orangeboi69/e628f3dc7c8d8dacae27c480aa2c83e8)

### Expected Results: 
- The result is invalid(JSON file with the data: `{"result":"invalid"}`)

### Actual Results:
###### Response time: ~15.7 second
```JSON
{
    "result": "invalid"
}
```
### **Screenshots**:

![Screenshot of the invalid request and response](https://i.imgur.com/YYi56GW.png "Application shown: Postman")

*Original image* :

![orignal picture](https://i.imgur.com/Bjvk96D.png "covid 19 test - invalid")
---
> By Orange at 20th of November, 2024
> Time of testing: 10/13/2024 - 10/15/2024
> Version 0.2