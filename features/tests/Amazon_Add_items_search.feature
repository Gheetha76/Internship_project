# Created by Gheethvijay at 8/11/23
Feature: Testing amazon search by adding more items


  Scenario Outline:Verify by adding an item in amazon search
     Given Open Amazon page
     When Testing for <product>
     Then Verify searching <result> is correct
    Examples:
    |product              |result          |
    |ipad                 |"ipad"          |
#    |iphone               |"iphone"        |
#    |apple tv             |"apple tv"      |
