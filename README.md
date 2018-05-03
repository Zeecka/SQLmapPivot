# SQLmapPivot
SQLmap Pivot is used to link SQLmap with complex SQL Injections which need programming process

## Example
- You can use SQLmapPivot when you have to encrypt your injection with AES or encode it with weird base.
- You can also use SQLmapPivot when you have captcha to break with OCR
- You can use SQLmapPivot when the injection need multiple requests.

## How does it works ?
The script will create an simple http server at http://localhost/ with a vulnerable parameters "?p=", easy to use for sqlmap or humans.
This parameters is directly linked to the "req" function (parameter "sqli" of the function).
You can easyly craft your SQLi request in this function using "sqli" as injection payload.

`BEERWARE LICENSE`
Zeecka
