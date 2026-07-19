"""
Design too based on real world scenarios

Implement a system to ingest “complexes” (packages of >2 instrument legs, each
with a signed ratio) and map them to internal canonical IDs.

A complex is a collection of legs. A leg is defined as (num, id) where num is a
signed integer, and id is the stock id

The following two are examples of complexes, which also happen to be canonical
complexes:

[(-1, A), (1, B)] — sold 1a buy 1b

[(1, A), (-1, B)] — buy 1a sold 1b

Design 3 apis: insertComplex, getComplex, getUniqueComplexes

"""