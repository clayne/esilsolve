from . import simlibc

replacements = {
    "sym.imp.printf":  simlibc.puts, # TODO actually do this mess
    "sym.imp.puts":    simlibc.puts,
    "sym.imp.memcpy":  simlibc.memcpy, 
    "sym.imp.memmove": simlibc.memmove, 
    "sym.imp.memset":  simlibc.memset, 
    "sym.imp.memchr":  simlibc.memchr, 
    "sym.imp.memrchr": simlibc.memrchr, 
    "sym.imp.memcmp":  simlibc.memcmp, 
    "sym.imp.bcopy":   simlibc.bcopy, 
    "sym.imp.bzero":   simlibc.bzero, 
    "sym.imp.memfrob": simlibc.memfrob, 
    "sym.imp.strcmp":  simlibc.strcmp, 
    "sym.imp.strchr":  simlibc.strchr, 
    "sym.imp.strrchr": simlibc.strrchr, 
    "sym.imp.index":   simlibc.strchr, 
    "sym.imp.rindex":  simlibc.strrchr, 
    "sym.imp.strstr":  simlibc.strstr, 
    "sym.imp.strlen":  simlibc.strlen, 
    "sym.imp.strnlen": simlibc.strnlen, 
    "sym.imp.strcpy":  simlibc.strcpy,
    "sym.imp.stpcpy":  simlibc.stpcpy,
    "sym.imp.strdup":  simlibc.strdup,
    "sym.imp.strdupa": simlibc.strdupa,
    "sym.imp.strndup": simlibc.strndup,
    "sym.imp.strndupa":simlibc.strndupa,
    "sym.imp.strncpy": simlibc.strncpy,
    "sym.imp.strcat":  simlibc.strcat,
    "sym.imp.strncat": simlibc.strncat,  
    "sym.imp.gets":    simlibc.gets,
    "sym.imp.fgets":   simlibc.fgets,
    "sym.imp.getenv":  simlibc.nothin,  
    "sym.imp.malloc":  simlibc.malloc, 
    "sym.imp.calloc":  simlibc.calloc, 
    "sym.imp.free":    simlibc.free, 
    "sym.imp.getpid":  simlibc.getpid, 
    "sym.imp.fork":    simlibc.fork, 
    "sym.imp.open":    simlibc.open, 
    "sym.imp.close":   simlibc.close, 
    "sym.imp.read":    simlibc.read, 
    "sym.imp.write":   simlibc.write, 
    "sym.imp.fileno":  simlibc.fileno, 
    "sym.imp.fopen":   simlibc.fopen, 
    "sym.imp.fclose":  simlibc.fclose, 
    "sym.imp.fread":   simlibc.fread, 
    "sym.imp.fwrite":  simlibc.fwrite, 
    "sym.imp.lseek":   simlibc.lseek, 
    "sym.imp.access":  simlibc.access, 
    "sym.imp.stat":    simlibc.stat, 
    "sym.imp.atoi":    simlibc.atoi, 
    "sym.imp.atol":    simlibc.atol, 
    "sym.imp.strtol":  simlibc.atol,
    "sym.imp.strtoul": simlibc.atol, 
    "sym.imp.strtoll": simlibc.atoll, 
    "sym.imp.strtoull":simlibc.atoll, 
    "sym.imp.isupper": simlibc.isupper, 
    "sym.imp.islower": simlibc.islower, 
    "sym.imp.isalpha": simlibc.isalpha, 
    "sym.imp.isdigit": simlibc.isdigit, 
    "sym.imp.isalnum": simlibc.isalnum, 
    "sym.imp.isblank": simlibc.isblank,
    "sym.imp.iscntrl": simlibc.iscntrl, 
    "sym.imp.islower": simlibc.islower,  
    "sym.imp.toupper": simlibc.toupper, 
    "sym.imp.tolower": simlibc.tolower, 
    "sym.imp.gettext": simlibc.ret_arg1,
    "sym.imp.dgettext":simlibc.ret_arg2,
    "sym.imp.dcgettext": simlibc.ret_arg2,
    "sym.imp.abs":       simlibc.abs, 
    "sym.imp.labs":      simlibc.labs,
    "sym.imp.llabs":     simlibc.labs, 
    "sym.imp.div":       simlibc.div, 
    "sym.imp.ldiv":      simlibc.ldiv,
    "sym.imp.lldiv":     simlibc.ldiv, 
    "sym.imp.rand":      simlibc.rand,
    "sym.imp.random":    simlibc.rand,
    "sym.imp.srand":     simlibc.srand,
    "sym.imp.srandom":   simlibc.srand,
    "sym.imp.fflush":    simlibc.fflush,
    "sym.imp.sleep":     simlibc.sleep,
    "sym.imp.nanosleep": simlibc.nothin, # TODO idk
    "sym.imp.abort":     simlibc.abort,
    "sym.imp.ptrace":    simlibc.nothin,
    "sym.imp.getopt":    simlibc.ret_negone,
    "sym.imp.getopt_long":        simlibc.ret_negone,
    "sym.imp.getopt_long_only":   simlibc.ret_negone,
    "sym.imp.gethostname":        simlibc.gethostname,
    "sym.imp.getpagesize":        simlibc.getpagesize,
    "sym.imp.is_selinux_enabled": simlibc.nothin,
    "sym.imp.__stack_chk_fail":   simlibc.abort,
    "sym.imp.quick_exit":         simlibc.simexit,
    "sym.imp.exit":               simlibc.simexit
}
