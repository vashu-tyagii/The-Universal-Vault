-- Create a new table projects with: project_id (PK), project_name, department_id (FK to departments), budget (DECIMAL).
CREATE TABLE IF NOT EXISTS projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(50) NOT NULL,
    department_id INT,
    budget decimal(10, 2) NOT NULL,
    constraint fk_department FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
-- Add a CHECK constraint ensuring budget is always positive.
-- ALTER TABLE projects ADD CONSTRAINT chk_budget CHECK (budget > 0);
-- Insert 3 rows into projects.
-- INSERT INTO projects(project_id, project_name, department_id, budget)
-- VALUES (1, 'Project Alpha', 1, 10000.00),
--     (2, 'Project Beta', 2, 20000.00),
--     (3, 'Project Gamma', 3, 15000.00);
-- Update one project's budget by increasing it 15%.
-- UPDATE projects SET budget = budget * 1.15 WHERE project_id = 1;
-- Delete one project by project_id.
DELETE from projects
where project_id = 3;
-- Add a new column status (VARCHAR) to projects, then drop it again.