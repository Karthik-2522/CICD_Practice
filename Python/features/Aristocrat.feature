Feature: User login functionality
Scenario: 1 Successful login
Given I am on the Demo Login Page
When I fill the account information for account standardUser into the Username field and Password field
And I click the Login Button
Then I am redirected to the Demo Main Page 
And I Verify the App Logo exists 

Scenario: 2 Failed Login
Given I am on the Demo Login Page
When I fill the account information for account LockedOutUser into the Username field and Password field
And I click the Login Button
Then I Verifiy the Error Message Contains the text "Sorry, this user has been banned. "

Scenario: 3 Extract Data *
Given I am logged in 
When I am on the inventory page 
Then I extract content from the web page 
And Save it to a text file
Then I log out 
And I verify I am on the Login page again