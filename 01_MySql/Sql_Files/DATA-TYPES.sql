CREATE TABLE IF NOT EXISTS all_datatypes_master (
    -- ====================================================================
    -- 1. NUMERIC DATA TYPES (Exact & Approximate Numbers)
    -- ====================================================================
    
    -- TINYINT: Very small integer (-128 to 127 signed, 0 to 255 unsigned)
    tiny_col TINYINT COMMENT 'Stores tiny integers, commonly used for flags or small status codes.',

    -- SMALLINT: Small integer (-32,768 to 32,767)
    small_col SMALLINT COMMENT 'Stores small range integers like department codes or low-scale counts.',

    -- INT / INTEGER: Standard integer (~ -2 billion to +2 billion)
    int_col INT COMMENT 'Standard integer type, frequently used for IDs and sequential counts.',

    -- BIGINT: Large integer (For massive counts, timestamps, or unique system IDs)
    bigint_col BIGINT COMMENT 'Large integer type used for high-volume transactions or record counts.',

    -- DECIMAL(p, s) / NUMERIC: Exact fixed-point numbers (p = precision, s = scale)
    decimal_col DECIMAL(10, 2) COMMENT 'Exact numeric type for currency or financial values; 10 total digits, 2 after decimal.',

    -- FLOAT: Approximate floating-point number (Single precision)
    float_col FLOAT COMMENT 'Approximate numeric type for scientific measurements with single precision.',

    -- DOUBLE / REAL: Approximate floating-point number (Double precision)
    double_col DOUBLE COMMENT 'Approximate numeric type for high-precision scientific or mathematical data.',


    -- ====================================================================
    -- 2. CHARACTER & STRING DATA TYPES (Textual Data)
    -- ====================================================================

    -- CHAR(n): Fixed-length character string (Padded with spaces if shorter than n)
    char_col CHAR(10) COMMENT 'Fixed-length string; always occupies exact specified bytes (e.g., country codes like IND).',

    -- VARCHAR(n): Variable-length character string (Only uses space for actual characters)
    varchar_col VARCHAR(100) COMMENT 'Variable-length string for names, emails, or text fields up to n characters.',

    -- TEXT / LONGTEXT: Large variable-length character text (For large blocks of text/articles)
    text_col TEXT COMMENT 'Large text type used for storing long descriptions, articles, or logs.',


    -- ====================================================================
    -- 3. DATE & TIME DATA TYPES (Temporal Data)
    -- ====================================================================

    -- DATE: Format YYYY-MM-DD
    date_col DATE COMMENT 'Stores calendar date information without time (Format: YYYY-MM-DD).',

    -- TIME: Format HH:MM:SS
    time_col TIME COMMENT 'Stores time of day information (Format: HH:MM:SS).',

    -- DATETIME: Format YYYY-MM-DD HH:MM:SS (Combines date and time)
    datetime_col DATETIME COMMENT 'Stores both date and time values together without timezone awareness.',

    -- TIMESTAMP: Format YYYY-MM-DD HH:MM:SS (Timezone-sensitive, auto-updates often)
    timestamp_col TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Stores date and time with timezone conversion, ideal for audit logs.',

    -- YEAR: Format YYYY (2 or 4 digits)
    year_col YEAR COMMENT 'Stores year data efficiently in a 4-digit or 2-digit format.',


    -- ====================================================================
    -- 4. BINARY & BLOB DATA TYPES (Raw Bytes & Media)
    -- ====================================================================

    -- BINARY(n): Fixed-length binary byte strings
    binary_col BINARY(50) COMMENT 'Fixed-length raw binary byte storage.',

    -- VARBINARY(n): Variable-length binary byte strings
    varbinary_col VARBINARY(255) COMMENT 'Variable-length raw binary byte storage.',

    -- BLOB (Binary Large Object): For storing images, audio, documents, or encrypted blocks
    blob_col BLOB COMMENT 'Binary Large Object used to store raw files like images, PDFs, or encrypted data.',


    -- ====================================================================
    -- 5. SPECIALTY DATA TYPES (Logical, Collections, & Structured Data)
    -- ====================================================================

    -- BOOLEAN (TINYINT(1) equivalent in many SQL engines): True/False values
    boolean_col BOOLEAN COMMENT 'Stores logical truth values (TRUE, FALSE, or NULL).',

    -- ENUM: String object with a value chosen from a permitted list of explicitly listed options
    enum_col ENUM('Low', 'Medium', 'High') COMMENT 'Restricts column input to a predefined list of string values.',

    -- JSON: Structured JSON document storage
    json_col JSON COMMENT 'Stores semi-structured JSON documents for flexible key-value or nested data handling.',

    -- ====================================================================
    -- 6. TABLE CONSTRAINTS
    -- ====================================================================
    
    -- Defining the Primary Key constraint at the table level using the standard INT column
    CONSTRAINT pk_all_datatypes PRIMARY KEY (int_col)

); -- This command creates a comprehensive blueprint table named 'all_datatypes_master' incorporating every major SQL data type category (Numeric, String, Temporal, Binary, and Specialty) with inline field comments for structured documentation.