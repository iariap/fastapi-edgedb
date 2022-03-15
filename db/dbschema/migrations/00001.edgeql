CREATE MIGRATION m13wdqt3e74ocfo2gwototycp5ewk4l2zaxdphdxuskjiw3ukedrca
    ONTO initial
{
  CREATE EXTENSION edgeql_http VERSION '1.0';
  CREATE EXTENSION graphql VERSION '1.0';
  CREATE TYPE default::Person {
      CREATE REQUIRED PROPERTY first_name -> std::str;
      CREATE PROPERTY last_name -> std::str;
      CREATE PROPERTY full_name := ((((.first_name ++ ' ') ++ .last_name) IF EXISTS (.last_name) ELSE .first_name));
  };
};
