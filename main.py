class Notebook:
    def __init__(self):
        self.notes:list[Note] = []

    def add_note(self, text, title, id):
        self.notes.append(Note(text, title, id))

    def find_note(self, **kwargs):
        '''
        Search argument for kwargs
        note_attribute=value
        e.g. id=23
        '''
        return next(self.__iterNote(**kwargs))

    def __iterNote(self, **kwargs):
        return (note for note in self.notes if note.match(**kwargs))

    def __iter__(self):
        ''' Returns the Iterator object '''
        return NotebookIterator(self)
    
class Note:
    def __init__(self, text, title, id):
        self.text = text
        self.title = title
        self.id = id

    def match(self, **kwargs):
        return all(getattr(self, key) == val for (key, val) in kwargs.items())

class NotebookIterator:
    '''iterates over the Notes in a Notebook'''
    def __init__(self, notebook):
        self._notebook = notebook
        self._index = 0

    def __next__(self):
        '''returns the next Entry.text in Note'''
        if self._index < len(self._notebook.notes):
            return_value = (
                self._notebook.notes[self._index].id,
                self._notebook.notes[self._index].title,
                self._notebook.notes[self._index].text,
                )
            self._index += 1
            return return_value
        raise StopIteration


if __name__ == "__main__":

    notes_to_add = [
        "this is the first note",
        "this is the second note",
        "boy I wish I should autmoate this",
        "and now we're really starting to add some content"
    ]

    titles = [
        "The First",
        "The Second",
        "The Third",
        "The Fourth"
    ]
    
    note_ids = [23, 83, 1234, 125]

    notebook = Notebook()

    for i, note in enumerate(notes_to_add):
        notebook.add_note(note, titles[i], note_ids[i])

    print(notebook.find_note(id=1234).text)
    print(notebook.find_note(title=titles[0]).text)
