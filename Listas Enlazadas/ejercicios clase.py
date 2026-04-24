from lista_doblemente_enlazada import DoublyLinkedList, NodeD

def remove_even_positions(dll):
    index = 0
    current = dll.head
    while current:
        next_node = current.next
        if index % 2 == 0:
            if current.prev == dll.head:
                new_head = current.next
                new_head.prev = None
            else:
                prev_node = current.prev
                prev_node.next = next_node
                if next_node:
                    next_node.prev = prev_node

            current.next = None
            current.prev = None 

            dll.size -= 1

        current = next_node
        index += 1
    
    return new_head

#Historial Navegador

class BrowserHistory:
    def __init__(self, homepage: NodeD) -> None:
        self.history_pages = DoublyLinkedList()
        self.history_pages.append(homepage)
        self.current_page = self.history_pages.head

    def __str__(self):
        result =[]
        for nodo in self.history_pages:
            if nodo == self.current_page:
                result.append(f'[{nodo.value}]')
            else:
                result.append(str(nodo.value))
        return ' <--> '.join(result)
    
    def visit_new_page(self, url: str) -> None:
        self.history_pages.append(NodeD(url))
        self.current_page = self.history_pages.tail

    def delete_pages(self, current_page):
        while current_page.next:
            next_page = current_page.next
            current_page.next = None
            next_page.prev = None
            self.history_pages.size -= 1
            current_page = next_page

    def go_back(self, steps: int) -> str:
        while steps > 0 and self.current_page.prev:
            self.current_page = self.current_page.prev
            steps -= 1
        return self.current_page.value

    def next_pages(self, steps: int) -> str:
        while steps > 0 and self.current_page.next:
            self.current_page = self.current_page.next
            steps -= 1
        return self.current_page.value
    


chrome = BrowserHistory(NodeD("google.com"))
chrome.visit_new_page("facebook.com")
chrome.visit_new_page("X.com")

chrome.go_back(1)

chrome.visit_new_page("instagram.com")


print(chrome)