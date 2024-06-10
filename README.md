# 1000 JavaScript Tips

<details><summary>1. Use 'const' and 'let' instead of 'var'</summary>
Using 'const' and 'let' helps avoid common pitfalls associated with variable scoping in JavaScript. 'const' is used for variables that should not be reassigned, providing more predictable and maintainable code. 'let' is used for variables that can change, but it is block-scoped, reducing the chances of bugs related to variable hoisting. For more information, refer to the [MDN Web Docs on const](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const) and [MDN Web Docs on let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let).
</details>

<details><summary>2. Sanitize User Input</summary>
Always sanitize user input to prevent security vulnerabilities such as cross-site scripting (XSS) and command injection. Use libraries like [DOMPurify](https://github.com/cure53/DOMPurify) for sanitizing HTML content, and ensure that any data coming from user input is properly validated and sanitized before being processed or displayed. Learn more about XSS prevention on the [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Prevention_Cheat_Sheet.html).
</details>

<details><summary>3. Use Promises and Async/Await for Asynchronous Code</summary>
Promises and async/await provide a cleaner and more readable way to handle asynchronous operations compared to traditional callback functions. They help in writing more maintainable code and reduce the complexity associated with error handling in asynchronous operations. Learn more about [Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) and [async/await](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Async_await) on MDN Web Docs.
</details>

<details><summary>4. Avoid Global Variables</summary>
Global variables can lead to conflicts and hard-to-debug issues, especially in larger codebases. Encapsulate your code within functions or use module patterns to avoid polluting the global namespace. This practice helps in maintaining code modularity and reusability. Read more about best practices in the [MDN Web Docs on Variable Scope](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variable_scope).
</details>

<details><summary>5. Optimize DOM Manipulation</summary>
Frequent DOM manipulation can lead to performance issues. To optimize, batch DOM changes, use document fragments, or leverage virtual DOM libraries like [React](https://reactjs.org/). Minimizing reflows and repaints by reducing direct DOM interactions can significantly improve performance. Check out this [article on DOM manipulation performance](https://www.smashingmagazine.com/2012/11/writing-fast-memory-efficient-javascript/).
</details>

<details><summary>6. Debounce and Throttle Events</summary>
For events that fire frequently (like scroll, resize, or keypress), use debounce or throttle techniques to limit the number of times the event handler executes. This helps in improving performance and preventing excessive function calls. Libraries like [Lodash](https://lodash.com/docs/4.17.15#debounce) provide convenient debounce and throttle methods. Read more about [debouncing and throttling](https://css-tricks.com/debouncing-throttling-explained-examples/) on CSS-Tricks.
</details>

<details><summary>7. Use Strict Mode</summary>
Enable strict mode by adding 'use strict'; at the beginning of your JavaScript files or functions. Strict mode helps in catching common coding errors, prevents the use of certain problematic features, and provides better performance by allowing JavaScript engines to optimize code more effectively. Learn more about strict mode on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode).
</details>

<details><summary>8. Leverage Browser DevTools</summary>
Browser DevTools are powerful tools for debugging, profiling, and optimizing your code. Use features like breakpoints, network analysis, and performance profiling to identify and fix issues more efficiently. Familiarizing yourself with DevTools can greatly enhance your development workflow. Learn more from the [Chrome DevTools documentation](https://developer.chrome.com/docs/devtools/).
</details>

<details><summary>9. Use ES6 Modules</summary>
ES6 modules provide a standardized way to organize and reuse code. They help in maintaining a clean codebase by encapsulating functionality and promoting code reuse. Use 'import' and 'export' statements to manage dependencies and module loading in your JavaScript projects. Read more about ES6 modules on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules).
</details>

<details><summary>10. Handle Errors Gracefully</summary>
Always include error handling in your code to manage potential issues gracefully. Use try/catch blocks for synchronous code and .catch() or async/await with try/catch for asynchronous code. Proper error handling ensures your application can recover from unexpected situations and provide meaningful feedback to users. Learn more about error handling in JavaScript on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#exception_handling_statements).
</details>

<details><summary>11. Use Template Literals</summary>
Template literals provide an easy and readable way to create strings. They allow for embedded expressions and multiline strings, which can simplify string creation and manipulation. Use backticks (\`) to define template literals and include expressions within ${} brackets. Learn more about template literals on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals).
</details>

<details><summary>12. Use the Spread Operator</summary>
The spread operator (...) allows for easy copying and merging of arrays and objects, and can also be used for function arguments. It provides a concise and readable way to manipulate collections of data. Learn more about the spread operator on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax).
</details>

<details><summary>13. Use Default Parameters</summary>
Default parameters allow you to specify default values for function parameters if no arguments are provided. This can simplify function definitions and provide more robust default behavior. Learn more about default parameters on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters).
</details>

<details><summary>14. Use Destructuring Assignment</summary>
Destructuring assignment allows you to unpack values from arrays or properties from objects into distinct variables. This can simplify the extraction of values and make your code more readable. Learn more about destructuring on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment).
</details>

<details><summary>15. Use Arrow Functions</summary>
Arrow functions provide a shorter syntax for writing function expressions and lexically bind the `this` value. This can make your code more concise and predictable. Learn more about arrow functions on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions).
</details>

<details><summary>16. Use Map and Set</summary>
Map and Set are built-in data structures that provide more functionality and performance compared to plain objects and arrays. Use Map for key-value pairs and Set for unique values. Learn more about [Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) and [Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) on MDN Web Docs.
</details>

<details><summary>17. Use for...of Loop</summary>
The for...of loop provides a simpler and more readable way to iterate over iterable objects like arrays, strings, and NodeLists. It avoids the pitfalls of traditional for loops and provides a cleaner syntax. Learn more about the for...of loop on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of).
</details>

<details><summary>18. Use Async Iterators</summary>
Async iterators and the for await...of loop allow you to iterate over asynchronous data sources in a clean and readable manner. This can simplify the handling of asynchronous streams of data. Learn more about async iterators on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of).
</details>

<details><summary>19. Use Optional Chaining</summary>
Optional chaining (?.) allows you to safely access deeply nested properties without having to explicitly check for the existence of each level in the property chain. This can simplify your code and prevent runtime errors. Learn more about optional chaining on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining).
</details>

<details><summary>20. Use Nullish Coalescing</summary>
The nullish coalescing operator (??) provides a way to handle default values when dealing with null or undefined. It is a cleaner alternative to using logical OR (||) for default values. Learn more about nullish coalescing on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_operator).
</details>

<details><summary>21. Use the Rest Parameter</summary>
The rest parameter syntax (...) allows you to represent an indefinite number of arguments as an array. This is useful in functions where you don't know the exact number of arguments beforehand. Learn more about rest parameters on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters).
</details>

<details><summary>22. Use Functional Programming Techniques</summary>
Functional programming techniques like map, filter, and reduce can make your code more concise and easier to understand. They allow you to operate on collections of data in a declarative manner. Learn more about functional programming in JavaScript on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#functional_programming).
</details>

<details><summary>23. Use Object Spread Operator</summary>
The object spread operator (...) allows you to create shallow copies of objects and merge multiple objects into one. This is useful for immutability and combining object properties. Learn more about the object spread operator on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax).
</details>

<details><summary>24. Use Default Case in Switch Statements</summary>
Always include a default case in switch statements to handle unexpected values. This ensures that your code can handle any input, even if it doesn't match any of the specified cases. Learn more about switch statements on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch).
</details>

<details><summary>25. Use Event Delegation</summary>
Event delegation is a technique that allows you to handle events efficiently by attaching a single event listener to a parent element. This listener analyzes bubbled events to find a match on child elements. Learn more about event delegation on [JavaScript.info](https://javascript.info/event-delegation).
</details>

<details><summary>26. Use Local Storage and Session Storage</summary>
Local storage and session storage provide a way to store data on the client side. Local storage persists data across sessions, while session storage only lasts for the duration of the page session. Learn more about local and session storage on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage).
</details>

<details><summary>27. Use the Fetch API</summary>
The Fetch API provides a modern, promise-based way to make network requests. It is a more powerful and flexible alternative to XMLHttpRequest. Learn more about the Fetch API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API).
</details>

<details><summary>28. Use Async Functions for Concurrency</summary>
Async functions, when combined with the await keyword, provide a clean and intuitive way to handle asynchronous operations. They make your code look synchronous and are easier to read and maintain. Learn more about async functions on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function).
</details>

<details><summary>29. Use the Module Pattern</summary>
The module pattern is a design pattern that provides a way to encapsulate private and public methods and variables. It helps in organizing and structuring your code. Learn more about the module pattern on [JavaScript.info](https://javascript.info/modules).
</details>

<details><summary>30. Use Object Destructuring</summary>
Object destructuring allows you to extract properties from objects and bind them to variables. This can make your code more concise and readable. Learn more about object destructuring on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment).
</details>

<details><summary>31. Use Named Parameters</summary>
Using named parameters in your functions can make your code more readable and flexible. Instead of passing a list of arguments, you pass an object with named properties. Learn more about named parameters on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters#using_destructuring_with_default_parameters).
</details>

<details><summary>32. Use the Proxy Object</summary>
The Proxy object allows you to create a proxy for another object, which can intercept and redefine fundamental operations for that object. This can be useful for implementing custom behavior. Learn more about the Proxy object on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy).
</details>

<details><summary>33. Use WeakMap and WeakSet</summary>
WeakMap and WeakSet are collections that allow for weak references to objects. This means that if no other references to an object exist, it can be garbage collected. Learn more about [WeakMap](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap) and [WeakSet](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet) on MDN Web Docs.
</details>

<details><summary>34. Use Generators for Iteration</summary>
Generators are functions that can be paused and resumed, allowing you to define iterative algorithms by writing code that produces a sequence of results. Learn more about generators on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*).
</details>

<details><summary>35. Use Custom Elements</summary>
Custom elements allow you to create your own HTML tags and define their behavior using JavaScript. This is part of the Web Components standard. Learn more about custom elements on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements).
</details>

<details><summary>36. Use Intersection Observer API</summary>
The Intersection Observer API provides a way to asynchronously observe changes in the intersection of a target element with an ancestor element or with a top-level document's viewport. Learn more about the Intersection Observer API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API).
</details>

<details><summary>37. Use the Performance API</summary>
The Performance API provides a way to measure the performance of your web applications. You can use it to track various performance metrics and optimize your code accordingly. Learn more about the Performance API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Performance).
</details>

<details><summary>38. Use the Clipboard API</summary>
The Clipboard API provides a way to interact with the clipboard, enabling you to copy and paste text programmatically. This can be useful for building rich text editors and other interactive applications. Learn more about the Clipboard API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API).
</details>

<details><summary>39. Use the Resize Observer API</summary>
The Resize Observer API provides a way to observe changes to the size of an element. This is useful for responsive design and ensuring your UI adapts to different screen sizes and orientations. Learn more about the Resize Observer API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Resize_Observer_API).
</details>

<details><summary>40. Use the Mutation Observer API</summary>
The Mutation Observer API provides a way to observe changes to the DOM tree. This can be useful for building dynamic user interfaces and ensuring your application responds to changes in the DOM. Learn more about the Mutation Observer API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver).
</details>

<details><summary>41. Use Service Workers</summary>
Service workers provide a way to run scripts in the background and handle network requests, enabling you to create offline-first web applications. Learn more about service workers on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API).
</details>

<details><summary>42. Use IndexedDB for Client-Side Storage</summary>
IndexedDB is a low-level API for storing large amounts of structured data on the client side. It provides a way to store data in a transactional and queryable manner. Learn more about IndexedDB on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API).
</details>

<details><summary>43. Use the Broadcast Channel API</summary>
The Broadcast Channel API provides a way to communicate between browsing contexts (such as iframes, tabs, or workers) that share the same origin. Learn more about the Broadcast Channel API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Broadcast_Channel_API).
</details>

<details><summary>44. Use the Web Animations API</summary>
The Web Animations API provides a way to create complex animations using JavaScript, offering more control and flexibility than CSS animations. Learn more about the Web Animations API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API).
</details>

<details><summary>45. Use the Speech Recognition API</summary>
The Speech Recognition API provides a way to convert speech to text, enabling you to build voice-controlled applications. Learn more about the Speech Recognition API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition).
</details>

<details><summary>46. Use the Speech Synthesis API</summary>
The Speech Synthesis API provides a way to convert text to speech, enabling you to build applications that can speak to the user. Learn more about the Speech Synthesis API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis).
</details>

<details><summary>47. Use the Geolocation API</summary>
The Geolocation API provides a way to get the geographical position of a device. This can be useful for building location-based applications. Learn more about the Geolocation API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API).
</details>

<details><summary>48. Use the Battery Status API</summary>
The Battery Status API provides a way to get information about the battery status of the device. This can be useful for building applications that optimize their behavior based on the battery level. Learn more about the Battery Status API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Battery_Status_API).
</details>

<details><summary>49. Use the Device Orientation API</summary>
The Device Orientation API provides a way to get information about the physical orientation of the device. This can be useful for building applications that respond to device movements. Learn more about the Device Orientation API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Device_Orientation_API).
</details>

<details><summary>50. Use the Network Information API</summary>
The Network Information API provides a way to get information about the network connection of the device. This can be useful for building applications that optimize their behavior based on the network conditions. Learn more about the Network Information API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Network_Information_API).
</details>

<details><summary>51. Use the Payment Request API</summary>
The Payment Request API provides a way to simplify the process of collecting payment information from the user. It enables you to create a consistent and secure payment experience. Learn more about the Payment Request API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Payment_Request_API).
</details>

<details><summary>52. Use the Notifications API</summary>
The Notifications API provides a way to display notifications to the user. This can be useful for keeping the user informed about important events or updates. Learn more about the Notifications API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API).
</details>

<details><summary>53. Use the Vibration API</summary>
The Vibration API provides a way to vibrate the device. This can be useful for providing haptic feedback in your applications. Learn more about the Vibration API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Vibration_API).
</details>

<details><summary>54. Use the Gamepad API</summary>
The Gamepad API provides a way to interact with game controllers. This can be useful for building games or applications that require game controller input. Learn more about the Gamepad API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API).
</details>

<details><summary>55. Use the WebRTC API</summary>
The WebRTC API provides a way to build real-time communication applications, such as video and voice chat. Learn more about the WebRTC API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API).
</details>

<details><summary>56. Use the WebSocket API</summary>
The WebSocket API provides a way to create a persistent connection between the client and the server, enabling real-time communication. Learn more about the WebSocket API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API).
</details>

<details><summary>57. Use the File API</summary>
The File API provides a way to interact with files on the user's device. This can be useful for building applications that need to read or write files. Learn more about the File API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/File_API).
</details>

<details><summary>58. Use the Streams API</summary>
The Streams API provides a way to handle streaming data, enabling you to process data as it is being received. Learn more about the Streams API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Streams_API).
</details>

<details><summary>59. Use the History API</summary>
The History API provides a way to manipulate the browser's session history, enabling you to build single-page applications with a navigation history. Learn more about the History API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/History_API).
</details>

<details><summary>60. Use the Web Audio API</summary>
The Web Audio API provides a way to process and synthesize audio in web applications. It enables you to build complex audio applications and games. Learn more about the Web Audio API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API).
</details>

<details><summary>61. Use the WebGL API</summary>
The WebGL API provides a way to render 3D graphics in web applications. It enables you to build complex visualizations and games. Learn more about the WebGL API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API).
</details>

<details><summary>62. Use the Drag and Drop API</summary>
The Drag and Drop API provides a way to implement drag-and-drop functionality in your web applications. This can be useful for building interactive user interfaces. Learn more about the Drag and Drop API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API).
</details>

<details><summary>63. Use the Shadow DOM</summary>
The Shadow DOM provides a way to encapsulate the internal structure of a web component, ensuring that its styles and behavior do not affect the rest of the document. Learn more about the Shadow DOM on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_shadow_DOM).
</details>

<details><summary>64. Use the File System Access API</summary>
The File System Access API provides a way to read and write files on the user's local file system. This can be useful for building applications that need to manage files locally. Learn more about the File System Access API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/File_System_Access_API).
</details>

<details><summary>65. Use the Ambient Light Sensor API</summary>
The Ambient Light Sensor API provides a way to get information about the ambient light level around the device. This can be useful for building applications that adapt to the lighting conditions. Learn more about the Ambient Light Sensor API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/AmbientLightSensor).
</details>

<details><summary>66. Use the Screen Orientation API</summary>
The Screen Orientation API provides a way to get and set the orientation of the screen. This can be useful for building applications that need to adapt to different screen orientations. Learn more about the Screen Orientation API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Screen_Orientation_API).
</details>

<details><summary>67. Use the Media Session API</summary>
The Media Session API provides a way to customize media notifications and handle media playback actions. This can be useful for building media applications with enhanced user experiences. Learn more about the Media Session API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Media_Session_API).
</details>

<details><summary>68. Use the Picture-in-Picture API</summary>
The Picture-in-Picture API provides a way to display video in a small overlay window that remains on top of other windows. This can be useful for building video applications with enhanced user experiences. Learn more about the Picture-in-Picture API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Picture-in-Picture_API).
</details>

<details><summary>69. Use the Payment Handler API</summary>
The Payment Handler API provides a way to create web-based payment apps that can handle payment requests from other web applications. Learn more about the Payment Handler API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Payment_Handler_API).
</details>

<details><summary>70. Use the Bluetooth API</summary>
The Web Bluetooth API provides a way to connect to Bluetooth devices directly from a web application. This can be useful for building applications that need to interact with Bluetooth peripherals. Learn more about the Bluetooth API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Web_Bluetooth_API).
</details>

<details><summary>71. Use the WebUSB API</summary>
The WebUSB API provides a way to connect to USB devices directly from a web application. This can be useful for building applications that need to interact with USB peripherals. Learn more about the WebUSB API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/USB).
</details>

<details><summary>72. Use the Serial API</summary>
The Web Serial API provides a way to connect to serial devices directly from a web application. This can be useful for building applications that need to interact with serial peripherals. Learn more about the Serial API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Serial).
</details>

<details><summary>73. Use the NFC API</summary>
The Web NFC API provides a way to read and write NFC tags directly from a web application. This can be useful for building applications that need to interact with NFC devices. Learn more about the NFC API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Web_NFC_API).
</details>

<details><summary>74. Use the Background Sync API</summary>
The Background Sync API provides a way to defer actions until the user has a stable internet connection. This can be useful for building applications that need to handle intermittent connectivity. Learn more about the Background Sync API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Background_Sync_API).
</details>

<details><summary>75. Use the Badging API</summary>
The Badging API provides a way to set an application-wide badge, typically shown on the app's icon. This can be useful for providing users with status or notification indicators. Learn more about the Badging API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Badging_API).
</details>

<details><summary>76. Use the Wake Lock API</summary>
The Wake Lock API provides a way to prevent the device from dimming or locking the screen. This can be useful for applications that need to keep the screen on while in use. Learn more about the Wake Lock API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Wake_Lock_API).
</details>

<details><summary>77. Use the Web Share API</summary>
The Web Share API provides a way to share text, links, and files to other apps installed on the device. This can be useful for building applications that need to share content with other apps. Learn more about the Web Share API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/share).
</details>

<details><summary>78. Use the Contact Picker API</summary>
The Contact Picker API provides a way to select contacts from the user's address book. This can be useful for building applications that need to interact with the user's contacts. Learn more about the Contact Picker API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Contact_Picker_API).
</details>

<details><summary>79. Use the Sensor APIs</summary>
The Sensor APIs provide a way to access various sensors on the device, such as the accelerometer, gyroscope, and magnetometer. This can be useful for building applications that need to interact with the device's sensors. Learn more about the Sensor APIs on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Sensor_APIs).
</details>

<details><summary>80. Use the Visual Viewport API</summary>
The Visual Viewport API provides a way to access information about the visual viewport, including its size and position. This can be useful for building responsive web applications that adapt to different screen sizes. Learn more about the Visual Viewport API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Visual_Viewport_API).
</details>

<details><summary>81. Use the WebVR API</summary>
The WebVR API provides a way to create virtual reality experiences in web applications. This can be useful for building immersive web applications that provide VR experiences. Learn more about the WebVR API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/WebVR_API).
</details>

<details><summary>82. Use the WebXR API</summary>
The WebXR API provides a way to create augmented reality and virtual reality experiences in web applications. This can be useful for building immersive web applications that provide AR and VR experiences. Learn more about the WebXR API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API).
</details>

<details><summary>83. Use the Credential Management API</summary>
The Credential Management API provides a way to handle user credentials, such as passwords and federated identities. This can be useful for building applications that require user authentication. Learn more about the Credential Management API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Credential_Management_API).
</details>

<details><summary>84. Use the Web Authentication API</summary>
The Web Authentication API provides a way to use public key cryptography for user authentication. This can be useful for building applications that require strong user authentication. Learn more about the Web Authentication API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API).
</details>

<details><summary>85. Use the Encrypted Media Extensions API</summary>
The Encrypted Media Extensions API provides a way to play encrypted media content in web applications. This can be useful for building applications that need to handle DRM-protected content. Learn more about the Encrypted Media Extensions API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Encrypted_Media_Extensions_API).
</details>

<details><summary>86. Use the Media Source Extensions API</summary>
The Media Source Extensions API provides a way to create streams for playback in web applications. This can be useful for building applications that need to handle adaptive streaming. Learn more about the Media Source Extensions API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Media_Source_Extensions_API).
</details>

<details><summary>87. Use the WebCodecs API</summary>
The WebCodecs API provides a way to encode and decode audio and video in web applications. This can be useful for building applications that need to handle media processing. Learn more about the WebCodecs API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/WebCodecs_API).
</details>

<details><summary>88. Use the WebGPU API</summary>
The WebGPU API provides a way to use the GPU for rendering and computation in web applications. This can be useful for building applications that need to handle high-performance graphics and computations. Learn more about the WebGPU API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API).
</details>

<details><summary>89. Use the WebHID API</summary>
The WebHID API provides a way to interact with human interface devices, such as keyboards and game controllers. This can be useful for building applications that need to handle input from HID devices. Learn more about the WebHID API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/WebHID_API).
</details>

<details><summary>90. Use the WebMIDI API</summary>
The WebMIDI API provides a way to interact with MIDI devices, such as musical instruments. This can be useful for building applications that need to handle input from MIDI devices. Learn more about the WebMIDI API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/MIDIAccess).
</details>

<details><summary>91. Use the WebNFC API</summary>
The WebNFC API provides a way to read and write NFC tags directly from a web application. This can be useful for building applications that need to interact with NFC devices. Learn more about the WebNFC API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Web_NFC_API).
</details>

<details><summary>92. Use the WebOTP API</summary>
The WebOTP API provides a way to handle one-time passwords in web applications. This can be useful for building applications that require user authentication. Learn more about the WebOTP API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/WebOTP_API).
</details>

<details><summary>93. Use the WebUSB API</summary>
The WebUSB API provides a way to connect to USB devices directly from a web application. This can be useful for building applications that need to interact with USB peripherals. Learn more about the WebUSB API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/USB).
</details>

<details><summary>94. Use the Web Serial API</summary>
The Web Serial API provides a way to connect to serial devices directly from a web application. This can be useful for building applications that need to interact with serial peripherals. Learn more about the Web Serial API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Serial).
</details>

<details><summary>95. Use the NFC API</summary>
The Web NFC API provides a way to read and write NFC tags directly from a web application. This can be useful for building applications that need to interact with NFC devices. Learn more about the NFC API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Web_NFC_API).
</details>

<details><summary>96. Use the Background Sync API</summary>
The Background Sync API provides a way to defer actions until the user has a stable internet connection. This can be useful for building applications that need to handle intermittent connectivity. Learn more about the Background Sync API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Background_Sync_API).
</details>

<details><summary>97. Use the Badging API</summary>
The Badging API provides a way to set an application-wide badge, typically shown on the app's icon. This can be useful for providing users with status or notification indicators. Learn more about the Badging API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Badging_API).
</details>

<details><summary>98. Use the Wake Lock API</summary>
The Wake Lock API provides a way to prevent the device from dimming or locking the screen. This can be useful for applications that need to keep the screen on while in use. Learn more about the Wake Lock API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Wake_Lock_API).
</details>

<details><summary>99. Use the Web Share API</summary>
The Web Share API provides a way to share text, links, and files to other apps installed on the device. This can be useful for building applications that need to share content with other apps. Learn more about the Web Share API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/share).
</details>

<details><summary>100. Use the Contact Picker API</summary>
The Contact Picker API provides a way to select contacts from the user's address book. This can be useful for building applications that need to interact with the user's contacts. Learn more about the Contact Picker API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Contact_Picker_API).
</details>

<details><summary>101. Use the Sensor APIs</summary>
The Sensor APIs provide a way to access various sensors on the device, such as the accelerometer, gyroscope, and magnetometer. This can be useful for building applications that need to interact with the device's sensors. Learn more about the Sensor APIs on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Sensor_APIs).
</details>

<details><summary>102. Use the Visual Viewport API</summary>
The Visual Viewport API provides a way to access information about the visual viewport, including its size and position. This can be useful for building responsive web applications that adapt to different screen sizes. Learn more about the Visual Viewport API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Visual_Viewport_API).
</details>

<details><summary>103. Use the WebVR API</summary>
The WebVR API provides a way to create virtual reality experiences in web applications. This can be useful for building immersive web applications that provide VR experiences. Learn more about the WebVR API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/WebVR_API).
</details>

<details><summary>104. Use the WebXR API</summary>
The WebXR API provides a way to create augmented reality and virtual reality experiences in web applications. This can be useful for building immersive web applications that provide AR and VR experiences. Learn more about the WebXR API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API).
</details>

<details><summary>105. Use the Credential Management API</summary>
The Credential Management API provides a way to handle user credentials, such as passwords and federated identities. This can be useful for building applications that require user authentication. Learn more about the Credential Management API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Credential_Management_API).
</details>

<details><summary>106. Use the Web Authentication API</summary>
The Web Authentication API provides a way to use public key cryptography for user authentication. This can be useful for building applications that require strong user authentication. Learn more about the Web Authentication API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API).
</details>

<details><summary>107. Use the Encrypted Media Extensions API</summary>
The Encrypted Media Extensions API provides a way to play encrypted media content in web applications. This can be useful for building applications that need to handle DRM-protected content. Learn more about the Encrypted Media Extensions API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Encrypted_Media_Extensions_API).
</details>

<details><summary>108. Use the Media Source Extensions API</summary>
The Media Source Extensions API provides a way to create streams for playback in web applications. This can be useful for building applications that need to handle adaptive streaming. Learn more about the Media Source Extensions API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Media_Source_Extensions_API).
</details>

<details><summary>109. Use the WebCodecs API</summary>
The WebCodecs API provides a way to encode and decode audio and video in web applications. This can be useful for building applications that need to handle media processing. Learn more about the WebCodecs API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/WebCodecs_API).
</details>

<details><summary>110. Use the WebGPU API</summary>
The WebGPU API provides a way to use the GPU for rendering and computation in web applications. This can be useful for building applications that need to handle high-performance graphics and computations. Learn more about the WebGPU API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API).
</details>

<details><summary>111. Use the WebHID API</summary>
The WebHID API provides a way to interact with human interface devices, such as keyboards and game controllers. This can be useful for building applications that need to handle input from HID devices. Learn more about the WebHID API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/WebHID_API).
</details>

<details><summary>112. Use the WebMIDI API</summary>
The WebMIDI API provides a way to interact with MIDI devices, such as musical instruments. This can be useful for building applications that need to handle input from MIDI devices. Learn more about the WebMIDI API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/MIDIAccess).
</details>

<details><summary>113. Use the WebNFC API</summary>
The WebNFC API provides a way to read and write NFC tags directly from a web application. This can be useful for building applications that need to interact with NFC devices. Learn more about the WebNFC API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Web_NFC_API).
</details>

<details><summary>114. Use the WebOTP API</summary>
The WebOTP API provides a way to handle one-time passwords in web applications. This can be useful for building applications that require user authentication. Learn more about the WebOTP API on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/WebOTP_API).
</details>
