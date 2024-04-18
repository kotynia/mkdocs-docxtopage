import fnmatch
import re
import os
import sys
import mkdocs
import mkdocs.plugins
import mkdocs.structure.files
import mammoth

class Exclude(mkdocs.plugins.BasePlugin):
    """A mkdocs plugin that converts docx files to markdown file with html contents."""



    def on_files(self, files, config):
        # globs = self.config['glob'] or []
        # if not isinstance(globs, list):
        #     globs = [globs]
        # regexes = self.config['regex'] or []
        # if not isinstance(regexes, list):
        #     regexes = [regexes]
        out = []
        # def include(name):
        #     for g in globs:
        #         if fnmatch.fnmatchcase(name, g):
        #             return False
        #     for r in regexes:
        #         if re.match(r, name):
        #             return False
        #     return True
        for i in files:
            name = i.src_path
            if name.endswith(".docx"):
                with open(i.src_path, "rb") as docx_file:
                    result = mammoth.convert_to_html(docx_file)
                    html = result.value # The generated HTML
                    messages = result.messages # Any messages, such as warnings during conversion
                
                # Write the HTML content to a .md file instead of a .docx file
                base = os.path.splitext(i.dest_path)[0]
                new_name = base + '.md'
                    
                with open(new_name, 'w', encoding='utf-8') as f:
                    f.write(html)
                    
                i.dest_path = new_name
                
                ##continue #skip

            # Windows reports filenames as eg.  a\\b\\c instead of a/b/c.
            # To make the same globs/regexes match filenames on Windows and
            # other OSes, let's try matching against converted filenames.
            # On the other hand, Unix actually allows filenames to contain
            # literal \\ characters (although it is rare), so we won't
            # always convert them.  We only convert if os.sep reports
            # something unusual.  Conversely, some future mkdocs might
            # report Windows filenames using / separators regardless of
            # os.sep, so we *always* test with / above.
            # if os.sep != '/':
            #     namefix = name.replace(os.sep, '/')
            #     if not include(namefix):
            #         continue
            out.append(i)
        return mkdocs.structure.files.Files(out)
