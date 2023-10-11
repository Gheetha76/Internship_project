# Created by Gheethvijay at 8/1/23
Feature: Testing if user can sign In when clicking on Returns and orders after logging out

  @smoke
  Scenario: Verify logged out user sees sign In when clicking on Returns and orders
     Given  Open Amazon page
     When   Click on Returns and orders


  Scenario: Sign In page can be opened from SignIn popup
    Given Open Amazon page
    When  Click on button from SignIn popup
    Then  Verify Sign in page opens
   @smoke
  Scenario: Amazon users see sign in button
    Given Open Amazon page
    Then Verify Sign In is clickable
    When Wait for 3 sec
    Then Verify Sign In is clickable
    Then Verify Sign In disappears


