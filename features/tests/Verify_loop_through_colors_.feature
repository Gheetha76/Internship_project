# Created by Gheethvijay at 8/16/23
Feature: Test for selecting colors of a product using loop
         and to verify if each color selected is clickable.



#  Scenario:Verify if the selected product's colors is clickable
#    Given  Open Amazon product B07BJKRR25 page
#    Then   Verify that the user can click on each color and select it

  @smoke
  Scenario Outline: Select a product from Closing category and hover over New Arrivals
    Given Open Amazon page
    When Inputting a <item>
    Then Select one product hoodie
    When Hover over New Arrivals
    Then Verify that the user sees the deals
    Examples:
      | item             |
      | hoodie for girls |

