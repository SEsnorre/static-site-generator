class HTMLNode():
    def __init__(self, tag: str | None = None, value: str | None = None, children: list | None = None, props: dict| None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        if self.props == None:
            return ""
        return "".join(list(map(lambda item: " " + item[0] + '="' + item[1] + '"', self.props.items())))
    
    def __repr__(self):
        return f"HTMLNode: tag:{self.tag}, value:{self.value}, children:{self.children}, props:{self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str | None,  props = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None or self.tag == "":
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag = None, value = None, children = None, props = None):
        super().__init__(tag, value, children, props)