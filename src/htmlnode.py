class HTMLNode():
    def __init__(self, tag: str | None = None, value: str | None = None, children: list | None = None, props: dict| None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        return "".join(list(map(lambda item: " " + item[0] + '="' + item[1] + '"', self.props.items())))
        
    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props and type(self) == type(other):
            return True
        return False
    
    def __repr__(self):
        return f"HTMLNode: tag:{self.tag}, value:{self.value}, children:{self.children}, props:{self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str | None,  props = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None or self.tag == "":
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict | None = None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None or self.tag == "":
            raise ValueError("All parent nodes must have a tag")
        if self.children is None:
            raise ValueError("All parent nodes must have children")
        if len(self.children) == 0:
            raise ValueError("All parent nodes must have at least one children")
        if not self.__children_have_value(self.children):
            raise ValueError("At least one children is missing a value")
        result = ""
        for child in self.children:
            result += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"
            
        
    def __children_have_value(self, childs: list):
        a = True
        for child in childs:
            if type(child) == ParentNode:
                a = a & self.__children_have_value(child.children)
            else:
                a = a and child.value != "" and child.value != None
        return a
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"