# Created by Gheethvijay at 9/22/23
Feature: Tests for Main page UI


 Scenario: Verify that footer has many links
    Given Open Amazon page
    Then Verify many links are shown in the footer


  Scenario: User can see language options
    Given Open Amazon page
    When Hover over language options
    Then Verify Spanish option present