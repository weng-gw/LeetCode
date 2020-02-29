class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        if len(dirs)==0:
            return "/"
        print(dirs)
        out = []
        for f in dirs:
            if f=='.' or (not f):
                continue
            elif f=='..':
                if out:
                    out.pop()
            else:
                out.append(f)
        return '/'+'/'.join(out)
