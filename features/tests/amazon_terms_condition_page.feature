# Created by Gheethvijay at 9/11/23
Feature: window handling test case from the class
  And verify that user can open amazon applications from Terms of Conditions




  Scenario Outline: User can open and close Amazon Privacy Notice
    Given Open Amazon Term and Conditions page
    And  Store original window
    When Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify <exp_text> Amazon Privacy Notice page is opened
    And User can close new window and switch back to original
    Examples:
    | exp_text                  |
    |Amazon.com Privacy Notice  |