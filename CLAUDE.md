# Maqueen Python Development Guidelines

## Commands
- Deploy code: `python deploy2maqueen.py <your_file.py>`
- Run single test: `python deploy2maqueen.py test_<feature>.py`
- Run motor test: `python deploy2maqueen.py test_motor.py`
- Run ultrasonic sensor test: `python deploy2maqueen.py test_sensor_ultrasonic.py`
- Run line sensor test: `python deploy2maqueen.py test_sensor_line.py`

## Code Style
- Import structure: Standard library imports first, then hardware-specific imports
- Docstrings: Use Google style docstrings with Args/Returns sections
- Naming: snake_case for functions/variables, UPPER_CASE for constants
- Constants: Define hardware constants at module level
- Error handling: Use try/except blocks with specific exceptions
- Comments: Use Japanese comments for user-facing messages, English for technical details
- Function parameters: Include type hints in docstrings
- Testing: Create separate test files for each component
- Documentation: Include detailed comments about hardware interfaces

## Development Process
- Modularize code into feature-specific files
- Test each component individually before integration
- Follow the roadmap in README.md for development priorities