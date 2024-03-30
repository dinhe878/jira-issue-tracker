from neo4j import GraphDatabase

class DataIngester:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_node(self, label, properties):
        with self.driver.session() as session:
            query = f"CREATE (n:{label} $props)"
            session.run(query, props=properties)

    def create_relationship(self, label1, property1, label2, property2, relationship_type):
        with self.driver.session() as session:
            query = (
                f"MATCH (a:{label1} {{property: $prop1}}) "
                f"MERGE (a)-[r:{relationship_type}]->(b:{label2} {{property: $prop2}})"
            )
            session.run(query, prop1=property1, prop2=property2)

if __name__ == "__main__":
    uri = "bolt://10.75.0.78:7687"
    username = "neo4j"
    password = "rEV6UgEk9PiVGE"

    ingester = DataIngester(uri, username, password)

    # Example usage:
    #node_properties = {"property": "value"}
    #ingester.create_node("Label1", node_properties)

    #relationship_properties = {"label1": "value1", "label2": "value2"}
    #ingester.create_relationship("Label1", "value1", "Label2", "value2", "R_TYPE")

    ingester.close()
