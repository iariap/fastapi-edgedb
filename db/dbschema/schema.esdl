using extension graphql;
using extension edgeql_http;


module default {
  
  type Person {
    required property first_name -> str;
    property last_name -> str;

    property full_name :=
      .first_name ++ ' ' ++ .last_name
      if exists .last_name
      else .first_name;
  }  
  
};