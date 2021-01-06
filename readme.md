CKAN - Frictionless Data
========================


REST interface
--------------

### GET

-   convert?q={ckan-dataset-id} - convert CKAN dataset json to
    datapackge json e.g.
    [/convert?q=0c03fa08-2142-426b-b1ca-fa852f909aa6](/convert?q=0c03fa08-2142-426b-b1ca-fa852f909aa6)
-   convert\_resources?q={ckan-dataset-id} - convert CKAN dataset json
    to datapackage json with resources, also if any of the resources
    files are csv file the tabular data package will be converted. e.g.
    [/convert\_resources?q=grassroots-frictionless-data-test](/convert_resources?q=grassroots-frictionless-data-test)
-   convert_push?q=grassroots-frictionless-data-test&key=example_key - push the generated datapackage.json to ckan.

### Other stuff

-   list\_all/ - view all json in the CKAN, raw json output
-   search?q={string} - search within CKAN, raw json output