
#### Basic Query Methods:
```python
find_all                    # Retrieve all records
find_by_id                  # Find by primary key
find_one                    # Find a single record
save                        # Save or update a record
delete_by_id               # Delete by primary key
count                      # Count total records
exists                     # Check if record exists
```

#### Query Methods with Conditions:
```python
find_by_{property}                     # Find by exact match
find_by_{property}_and_{property}      # Multiple conditions with AND
find_by_{property}_or_{property}       # Multiple conditions with OR
find_by_{property}_order_by_{property} # With sorting
find_first_{x}_by_{property}          # Limit results (x is a number)
```

#### Common Operators:
```python
find_by_{property}_contains           # LIKE %value%
find_by_{property}_starts_with       # LIKE value%
find_by_{property}_ends_with         # LIKE %value
find_by_{property}_is_null           # WHERE property IS NULL
find_by_{property}_is_not_null       # WHERE property IS NOT NULL
find_by_{property}_greater_than      # WHERE property > value
find_by_{property}_less_than         # WHERE property < value
find_by_{property}_between           # WHERE property BETWEEN value1 AND value2
find_by_{property}_in                # WHERE property IN (values)
```

### Java Style (camelCase)

#### Basic Query Methods:
```java
findAll                     // Retrieve all records
findById                    // Find by primary key
findOne                     // Find a single record
save                        // Save or update a record
deleteById                  // Delete by primary key
count                       // Count total records
exists                      // Check if record exists
```

#### Query Methods with Conditions:
```java
findBy{Property}                    // Find by exact match
findBy{Property}And{Property}       // Multiple conditions with AND
findBy{Property}Or{Property}        // Multiple conditions with OR
findBy{Property}OrderBy{Property}   // With sorting
findFirst{X}By{Property}           // Limit results (X is a number)
```

#### Common Operators:
```java
findBy{Property}Contains            // LIKE %value%
findBy{Property}StartsWith         // LIKE value%
findBy{Property}EndsWith           // LIKE %value
findBy{Property}IsNull             // WHERE property IS NULL
findBy{Property}IsNotNull          // WHERE property IS NOT NULL
findBy{Property}GreaterThan        // WHERE property > value
findBy{Property}LessThan           // WHERE property < value
findBy{Property}Between            // WHERE property BETWEEN value1 AND value2
findBy{Property}In                 // WHERE property IN (values)
```

## Notes
- All queries are written in CrateDB SQL syntax
- Geographical queries use the GEO_POINT data type for location data
- Time-based queries use DATE_TRUNC for proper datetime handling
