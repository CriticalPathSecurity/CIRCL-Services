# circl
A collection of Python scripts for querying CIRCL services.
https://www.circl.lu/services/

Imports the requests and json modules, which are necessary for making HTTP requests and handling JSON data, respectively.

Defines a log_to_json function that takes two arguments: data, which is the JSON data to be saved, and an optional filename with a default value of "response_log.json". This function creates a new file with the specified filename, and writes the JSON data to the file with a 4-space indentation for readability.

Sets the auth_str variable to an authentication string which contains the username and password separated by a colon.

Defines the base url for making requests to the "circl.lu" API.

Asks the user to input a query and stores it in the query variable.

Splits the auth_str variable into a tuple containing the username and password, and assigns it to the auth variable.

Makes an HTTP GET request to the API using the concatenated url and query variables, and provides the auth tuple for authentication. The API's response is stored in the response variable.

Prints the text of the API's response.

Converts the response text into a JSON object using the json() method and stores it in the response_json variable.

Calls the log_to_json function with the response_json data, saving the JSON data to a file named "response_log.json".
