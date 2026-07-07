# Q1: How do I write a SOQL query with a LIMIT clause in Apex, and what is the maximum LIMIT value?

## Approach: C_context7-no-library
- latency: 4115 ms
- chosenLibrary: /forcedotcom/go-soql
- chosenTitle: SOQL

---

### resolve-library-id picked: /forcedotcom/go-soql (SOQL)

--- resolve-library-id ranking (top of list) ---
Available Libraries:

- Title: SOQL
- Context7-compatible library ID: /forcedotcom/go-soql
- Description: This package provides `soql` tags for Go structs, enabling developers to marshal Go structs into SOQL queries for interacting with the Salesforce API.
- Code Snippets: 435
- Source Reputation: High
- Benchmark Score: 95

--- query-docs against /forcedotcom/go-soql ---
### Using OrderByClause in a Full SOQL Query

Source: https://github.com/forcedotcom/go-soql/blob/master/_autodocs/api-reference-marshalorderbyclause.md

Shows how to integrate the generated ORDER BY clause into a complete SOQL query using the Marshal function. This example includes select, where, order by, limit, and offset clauses.

```go
type SelectColumns struct {
    ID   string `soql:"selectColumn,fieldName=Id"`
    Name string `soql:"selectColumn,fieldName=Name__c"`
}

type QueryCriteria struct {
    Status string `soql:"equalsOperator,fieldName=Status__c"`
}

type SoqlQuery struct {
    SelectClause   SelectColumns  `soql:"selectClause,tableName=Account"
    WhereClause    QueryCriteria  `soql:"whereClause"
    OrderByClause  []soql.Order   `soql:"orderByClause"
}

limit := 10
offset := 0
query := SoqlQuery{
    SelectClause: SelectColumns{},
    WhereClause: QueryCriteria{Status: "Active"},
    OrderByClause: []soql.Order{
        {Field: "Name", IsDesc: false},
    },
}

soqlQuery, err := soql.Marshal(query)
if err != nil {
    log.Fatal(err)
}
fmt.Println(soqlQuery)
// Output: SELECT Id,Name__c FROM Account WHERE Status__c = 'Active' ORDER BY Name__c ASC LIMIT 10 OFFSET 0
```

--------------------------------

### Pagination with LIMIT and OFFSET

Source: https://github.com/forcedotcom/go-soql/blob/master/_autodocs/index.md

Configure LIMIT and OFFSET clauses by including pointer fields for these clauses in your query struct. This allows for controlling the number of records returned and the starting point.

```go
type Query struct {
    SelectClause   SelectClause  `soql:"selectClause,tableName=Account"
    WhereClause    Criteria      `soql:"whereClause"
    OrderByClause  []soql.Order  `soql:"orderByClause"
    LimitClause    *int          `soql:"limitClause"
    OffsetClause   *int          `soql:"offsetClause"
}

limit := 100
offset := 0
```

--------------------------------

### Pagination with LIMIT and OFFSET in Go

Source: https://github.com/forcedotcom/go-soql/blob/master/_autodocs/examples.md

Add pagination to query results by specifying LIMIT and OFFSET values. Ensure OrderByClause is used with LIMIT/OFFSET for predictable results.

```Go
type MyQuery struct {
    SelectClause  SelectClause  `soql:"selectClause,tableName=Account"
    WhereClause   Criteria      `soql:"whereClause"
    OrderByClause []soql.Order  `soql:"orderByClause"
    LimitClause   *int          `soql:"limitClause"
    OffsetClause  *int          `soql:"offsetClause"
}

limit := 100
offset := 50
query := MyQuery{
    SelectClause: SelectClause{},
    WhereClause: Criteria{
        Status: "Active",
    },
    OrderByClause: []soql.Order{
        {Field: "Name", IsDesc: false},
    },
    LimitClause:  &limit,
    OffsetClause: &offset,
}

result, _ := soql.Marshal(query)
// Output: SELECT Id,Name FROM Account WHERE Status__c = 'Active' ORDER BY Name ASC LIMIT 100 OFFSET 50
```

--------------------------------

### Define Basic SOQL Structs

Source: https://github.com/forcedotcom/go-soql/blob/master/README.md

Defines structs for a simple SOQL query including select, where, order by, limit, and offset clauses. These structs use `soql` tags to map fields to SOQL components.

```go
type TestSoqlStruct struct {
	SelectClause  NonNestedStruct   `soql:"selectClause,tableName=SM_SomeObject__c"
	WhereClause   TestQueryCriteria `soql:"whereClause"
	OrderByClause []Order           `soql:"orderByClause"
	LimitClause   *int              `soql:"limitClause"
	OffsetClause  *int              `soql:"offsetClause"
}
type TestQueryCriteria struct {
	IncludeNamePattern          []string `soql:"likeOperator,fieldName=Name__c"
	Roles                       []string `soql:"inOperator,fieldName=Role__c"
}
type NonNestedStruct struct {
	Name          string `soql:"selectColumn,fieldName=Name__c"
	SomeValue     string `soql:"selectColumn,fieldName=SomeValue__c"
}
```

--------------------------------

### Configure LIMIT Clause

Source: https://github.com/forcedotcom/go-soql/blob/master/_autodocs/configuration.md

Marks a field for the LIMIT clause. Must be a pointer to int. A nil pointer results in no LIMIT clause. The default is nil.

```go
type MyQuery struct {
    LimitClause *int `soql:"limitClause"`
}
```
