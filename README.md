# Korazons_Network_part_01_public
This is the first part of the Korazons_Network project, public.

while in this social network, you can only log in or create an account, as well as change account information in the account profile, while no protection is
provided in this project, user IDs are stored in their original form in cookies and users are identified by them, also due to the fact that I 
wrote in pure html,css,js user interface was created only for my type of monitors and the site will 
look bad on other monitors. In the future I will try to correct all the mistakes.

Flask is used for the server part of the site, I use a remote mysql database to work with the database, and sql is used to interact with it, 
and html,css, js is used for the clent part of the site due to the fact that I use pure html, css, js there are some problems with the clent 
part of the site in the future I will plug redo the site to react js . for users in the database, I use 3 tables: korazons_network_enter- to 
store user login data, korazons_network_info - to store all user information, korazons_network_sessions - to store user sessions for each of 
the tables, the main key for finding information is id, id increases automatically with each user to identify users, IDs are stored in browser 
cookies of course, this is only a small part of the future Korazons_Network site.
