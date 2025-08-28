# Testing Guide & Progress Notes

## How to Test the Application

### 1. Setup Environment
```bash
cd /path/to/your/project
pipenv install
pipenv shell
```

### 2. Create Sample Data
```bash
python lib/debug.py
```
**Expected Output:**
```
Creating sample data...
Sample data created!
```

### 3. Run the CLI Application
```bash
python lib/cli.py
```

## Testing Checklist

### ✅ Basic Functionality
- [ ] Application starts without errors
- [ ] Menu displays correctly
- [ ] Can add a new student (name + admission number)
- [ ] Can view all students
- [ ] Can add a new activity
- [ ] Can view all activities
- [ ] Can find student by ID
- [ ] Can find activity by ID
- [ ] Can remove a student (with confirmation)
- [ ] Can exit the program

### ✅ Sample Data Verification
After running `python lib/debug.py`, you should see:
- 3 students: John Doe (ADM001), Jane Smith (ADM002), Mike Johnson (ADM003)
- 3 activities: Basketball, Library, Computer Lab

## Expected Menu Output
```
Please select an option:
1. Add a student
2. View all students
3. Add an activity
4. View all activities
5. Find a student
6. Find an activity
7. Remove a student
0. Exit the program
>
```

## Progress Notes for Technical Mentor

### Learning Goals Achieved ✅
1. **CLI Development**: Created an interactive command-line interface
2. **SQLAlchemy ORM**: Implemented 2 related tables with basic relationships
3. **Virtual Environment**: Properly managed with Pipenv
4. **Package Structure**: Well-organized modular code
5. **Data Structures**: Used lists and basic Python data handling
6. **Separation of Concerns**: Separated UI, data persistence, and business logic

### Technical Implementation
- **Models**: Student (id, name, admission_number) and Activity (id, name)
- **Database**: SQLite with SQLAlchemy ORM
- **CRUD Operations**: Create, Read, Delete (working on Update)
- **Input Validation**: Basic error handling for invalid inputs
- **User Experience**: Confirmation prompts for destructive operations

### Code Quality
- **Clean Code**: Simple, readable functions
- **Modular Structure**: Separate files for different concerns
- **Documentation**: Clear function names and basic comments
- **Error Handling**: Basic try/catch for user input validation

### Next Steps
- [ ] Add update functionality for students and activities
- [ ] Implement activity-student relationships
- [ ] Add more robust input validation
- [ ] Enhance user interface with better formatting
- [ ] Add data export/import functionality

### Questions for Technical Mentor
1. How can I improve the input validation?
2. What's the best way to implement update operations?
3. How should I approach adding relationships between models?
4. Any suggestions for improving the user interface?
5. Recommendations for testing strategies?

## Demo Script for Technical Mentor

When demonstrating to your TM, follow this sequence:

1. **Show the project structure**:
   ```bash
   ls -la lib/
   ```

2. **Run the application**:
   ```bash
   python lib/cli.py
   ```

3. **Demo the features**:
   - Add a new student: "Alice Johnson" with "ADM004"
   - View all students (should show 4 total)
   - Add a new activity: "Art Club"
   - View all activities (should show 4 total)
   - Find student by ID (try ID 1)
   - Remove a student (with confirmation)

4. **Show the database file**:
   ```bash
   ls -la *.db
   ```

5. **Discuss the code structure** and what you've learned!
