This project is a simple POC to test google search feature

It contains only one feature but with 3 scenarios

├── features
│   ├── geckodriver.log
│   ├── Google.feature
│   └── steps
│       └── google_step.py
└── ReadMe.txt

This the folder structure

To run the above:
1. Ensure prequisites  like behave and selenium is installed
2.. Navigate to the folder conatining the feature file ie .../Behave_Selenium_POC/features
3. Type 'behave' in the terminal.

The whole automation written in Selenium will execute. There is no other command required.
If you was to test independant steps files you can just pass the other steps but using 'Assert True' like i have done in 2-3 of them.

Practises and Notes:

I have also displyed the concept of resuability where there are 3 scenarios in the fature file with
3 Given statements
3 Then statements
2 When statements

So idealy you would have 8 steps.
But since the 'Given' definitions are common for all 3 scenarios(Ref to the given statement in Feature file), there are only 6 step definitions we have written in the step file.
Similarly we can ensure we use the exact same annotations and look for similarities in step definition so that the no of steps can be optimised and resuee whereevr possible.
These are good practises and reduces conplexity..
