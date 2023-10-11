# Created by Gheethvijay at 7/29/23
Feature: Test for amazon search
  # Enter feature description here

  Scenario: Verify that a user can search for a table
     Given Open Amazon page
     When Search for table
     Then Verify search result is correct