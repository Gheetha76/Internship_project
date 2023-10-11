# Created by Gheethvijay at 8/10/23
Feature: Opening Amazon Best sellers page to verify there are links



  Scenario: Open Amazon Best sellers page and to verify if there are 4 links
     Given  Open Amazon page
     When   Click on best sellers
     Then   Verify this page has 5 top menu
     Then   Verify each 5 top menus pages opens