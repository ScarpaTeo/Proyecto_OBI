# -*- coding: utf-8 *-*
from db_conn import DBConn


class Pais:

    def __init__(self):
        self.id = 0
        self.pais = ''
        self.abbr = ''
        self.db = DBConn()

    def create(self):
        """Crear un nuevo registro"""
        query = "INSERT INTO paises (id, pais, abbr) VALUES (null, %s, %s)"
        values = (self.pais, self.abbr)
        self.db.ejecutar(query, values)

    def update(self):
        """Actualizar un registro existente"""
        query = "UPDATE paises SET pais = %s, abbr = %s WHERE id = %s"
        values = (self.pais, self.abbr, self.id)
        return self.db.ejecutar(query, values)

    def read_all(self):
        """Leer todos los registros"""
        query = "SELECT id, pais, abbr FROM paises"
        return self.db.ejecutar(query)

    def read(self):
        query = "SELECT id, pais, abbr FROM paises WHERE id = %d"
        values = (self.id)
        return self.db.ejecutar(query, values)

    def delete(self):
        """Elimina uno o todos los registros"""
        query = "DELETE FROM paises WHERE id = %s"
        values = self.id
        return self.db.ejecutar(query, values)
