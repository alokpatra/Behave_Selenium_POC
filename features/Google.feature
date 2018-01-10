Feature: Search tab on google

Scenario: Seach button present on google homepage

Given User is on the google homepage
Then User should be able to see the Search button

Scenario: Search textbox is present on google homepage

Given User is on the google homepage
Then User should be able to see the search textbox

Scenario: User can sucessfully search for word on google

Given User is on the google homepage
When User searches for the word 'Python'
And Hits the 'Search' butoon
Then it should return links to python
