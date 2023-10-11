# Created by Gheethvijay at 8/11/23
Feature: To test if Customer Service’s page has UI elements



  Scenario: Verify if elements are present in the Customer Service’s UI page
     Given  Open Amazon page
     When   Click on Amazon Customer Service tab
     When   Check for UI elements are visible
     Then   Verify all 11 UI elements
#     Then   Verify all 12 UI elements are enabled
     Then   Check for search help library
     Then   Check for input field to search library
     Then   Check for all help topics
     Then   Verify all 12 links under All help topics


