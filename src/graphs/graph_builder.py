from langgraph.graph import StateGraph
from src.state import State
from langgraph.graph import START,END
from src.nodes import BasicChatbotNode


class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """

        #get the node function
        self.basic_chatbot_node=BasicChatbotNode(self.llm)

        #define the nodes
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        
        #define the edges
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic Chatbot":
            #build the basic chat graph
            self.basic_chatbot_build_graph()
            
        #return the compile
        return self.graph_builder.compile()
