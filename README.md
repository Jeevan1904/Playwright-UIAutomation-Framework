# Playwright-UIAutomation-Framework
UI Automation framework using playwright - Learning and POC

Features to be included:

* Record and play [Codegen] - Done | code-gen.py
* Page Object Models - Done | page_objects module/folder (keeps adding)
* Project Structure - Done | (keeps updating)
    * Main Directories
        * page_objects - To store the locators per each page.
        * reports - To store the reports and logs if any.
        * test_data - 
        * tests - folder to maintain all the tests
        * utilities - any re-usable code (might not be required as all the re-usable code goes into fixtures)
* Pytest Framework
    * markers - In Progress | Built-in and custom markers defined in pytest.ini file | Rem: Use for regular tests
* Reports - Done
    * Command | pytest --template=html1/index.html --report=report.html
* Parallel execution - Done
    * pytest -n <number of CPUs>
* Pytest Fixtures - Ongoing work
    * setup fixture - Done
    * teardown fixture - Done
    * Utility fixtures - based on need
* Screenshots - Done
    * --screenshot | Whether to automatically capture a screenshot after each test. | on, off, only-on-failure
* Video Recordings - Done
    * --video | Whether to record video for each test. | on, off, retain-on-failure
* Tracing and Debugging - Not Started
* Datadriven testing - In Progress | External file data pending
    * pytest.mark.parameterize(<parameter>, <parameter values([{}, {}]))
* CI/CD Integration - Not Started
