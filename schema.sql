DROP TABLE IF EXISTS image;

CREATE TABLE image (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  name TEXT UNIQUE NOT NULL,
  longitude Decimal(9,6) NOT NULL,
  latitude Decimal(9,6) NOT NULL
);
