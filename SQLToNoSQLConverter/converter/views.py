from django.shortcuts import render
# from lexer import MyLexer
# from parser import MyParser
from sly import Lexer
from sly import Parser
import sqlparse
ERROR_GLOB = 0
class MyLexer(Lexer):
    # these are set of tokens that are to be exported to the parser
    tokens = {
        ON,
        SUM,
        COUNT,
        AVG,
        MIN,
        MAX,
        REALNUM,
        INTNUM,
        COL_NAME,
        TABLE_NAME,
        STRING,
        CHARACTER,
        IDENTIFIER,
        EQUAL,
        ADDEQ,
        SUBEQ,
        MULEQ,
        DIVEQ,
        MODEQ,
        GTEQ,
        LTEQ,
        NOTEQ,
        ANDEQ,
        OREQ,
        XOREQ,
        ADDOP,
        SUBOP,
        MULOP,
        DIVOP,
        MODOP,
        GTOP,
        LTOP,
        ANDOP,
        OROP,
        XOROP,
        SEPARATORS,
        SEMICOLON,
        COMMA,
        LCB,
        RCB,
        LFB,
        RFB,
        LSB,
        NAMES,
        NUMS,
        RELOP,
        RSB,
        UPDATE,
        BACKUP,
        FROM,
        DISTINCT,
        LIMIT,
        ORDER,
        ADD,
        DATABASE,
        BETWEEN,
        ASC,
        CASE,
        EXISTS,
        AND,
        TRUNCATE,
        PROCEDURE,
        WHERE,
        VALUES,
        ALL,
        HAVING,
        LIKE,
        EXEC,
        CONSTRAINT,
        COLUMN,
        DEFAULT,
        ROWNUM,
        REPLACE,
        IS,
        SET,
        LEFT,
        AS,
        FULL,
        ALTER,
        RIGHT,
        GROUP,
        INTO,
        SHOW,
        ANY,
        NULL,
        BY,
        INSERT,
        SELECT,
        NOT,
        TABLE,
        KEY,
        USE,
        TOP,
        UNION,
        INNER,
        CHECK,
        JOIN,
        FOREIGN,
        PRIMARY,
        IN,
        UNIQUE,
        VIEW,
        DELETE,
        OUTER,
        VARCHAR,
        OR,
        INDEX,
        DROP,
        CREATE,
        SOME,
        DESC,
        BOOL,
        OFFSET
    }

    # Identifiers and keywords
    IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*([.][a-zA-Z_][a-zA-Z0-9_]*)?'

    IDENTIFIER['ADD'] = ADD
    IDENTIFIER['CONSTRAINT'] = CONSTRAINT
    IDENTIFIER['ALTER'] = ALTER
    IDENTIFIER['COLUMN'] = COLUMN
    IDENTIFIER['TABLE'] = TABLE
    IDENTIFIER['AS'] = AS
    IDENTIFIER['ASC'] = ASC
    IDENTIFIER['BACKUP'] = BACKUP
    IDENTIFIER['DATABASE'] = DATABASE
    IDENTIFIER['CASE'] = CASE
    IDENTIFIER['CHECK'] = CHECK
    IDENTIFIER['CREATE'] = CREATE
    IDENTIFIER['INDEX'] = INDEX
    IDENTIFIER['REPLACE'] = REPLACE
    IDENTIFIER['VIEW'] = VIEW
    IDENTIFIER['PROCEDURE'] = PROCEDURE
    IDENTIFIER['UNIQUE'] = UNIQUE
    IDENTIFIER['DEFAULT'] = DEFAULT
    IDENTIFIER['DELETE'] = DELETE
    IDENTIFIER['DESC'] = DESC
    IDENTIFIER['DISTINCT'] = DISTINCT
    IDENTIFIER['DROP'] = DROP
    IDENTIFIER['USE'] = USE
    IDENTIFIER['SHOW'] = SHOW
    IDENTIFIER['EXEC'] = EXEC
    IDENTIFIER['FOREIGN'] = FOREIGN
    IDENTIFIER['KEY'] = KEY
    IDENTIFIER['FROM'] = FROM
    IDENTIFIER['FULL'] = FULL
    IDENTIFIER['OUTER'] = OUTER
    IDENTIFIER['JOIN'] = JOIN
    IDENTIFIER['GROUP'] = GROUP
    IDENTIFIER['BY'] = BY
    IDENTIFIER['HAVING'] = HAVING
    IDENTIFIER['INNER'] = INNER
    IDENTIFIER['INSERT'] = INSERT
    IDENTIFIER['INTO'] = INTO
    IDENTIFIER['SELECT'] = SELECT
    IDENTIFIER['NULL'] = NULL
    IDENTIFIER['IS'] = IS
    IDENTIFIER['LEFT'] = LEFT
    IDENTIFIER['LIMIT'] = LIMIT
    IDENTIFIER['ORDER'] = ORDER
    IDENTIFIER['PRIMARY'] = PRIMARY
    IDENTIFIER['RIGHT'] = RIGHT
    IDENTIFIER['ROWNUM'] = ROWNUM
    IDENTIFIER['TOP'] = TOP
    IDENTIFIER['SET'] = SET
    IDENTIFIER['TRUNCATE'] = TRUNCATE
    IDENTIFIER['UNION'] = UNION
    IDENTIFIER['UPDATE'] = UPDATE
    IDENTIFIER['VALUES'] = VALUES
    IDENTIFIER['WHERE'] = WHERE
    IDENTIFIER['VARCHAR'] = VARCHAR
    IDENTIFIER['ALL'] = ALL
    IDENTIFIER['AND'] = AND
    IDENTIFIER['ANY'] = ANY
    IDENTIFIER['BETWEEN'] = BETWEEN
    IDENTIFIER['EXISTS'] = EXISTS
    IDENTIFIER['IN'] = IN
    IDENTIFIER['LIKE'] = LIKE
    IDENTIFIER['NOT'] = NOT
    IDENTIFIER['OR'] = OR
    IDENTIFIER['SOME'] = SOME
    IDENTIFIER['OFFSET'] = OFFSET
    # EXTRAS
    IDENTIFIER['SUM'] = SUM
    IDENTIFIER['COUNT'] = COUNT
    IDENTIFIER['MIN'] = MIN
    IDENTIFIER['MAX'] = MAX
    IDENTIFIER['AVG'] = AVG
    IDENTIFIER['ON'] = ON

    EQUAL = r'\='
    COMMA = r'\,'

    # Arithmetic Assignment Operators
    ADDEQ = r'\+\='
    SUBEQ = r'\-\='
    MULEQ = r'\*\='
    DIVEQ = r'\/\='
    MODEQ = r'\%\='

    # Comparison Operators
    GTEQ = r'\>\='
    LTEQ = r'\<\='
    NOTEQ = r'\<\>'

    # Bitwise Assignment Operators
    ANDEQ = r'\&\='
    OREQ = r'\|\='
    XOREQ = r'\^\='

    # Arithmetic Operators
    ADDOP = r'\+'
    SUBOP = r'\-'
    MULOP = r'\*'
    DIVOP = r'\/'
    MODOP = r'\%'

    # Comparison Operators
    GTOP = r'\>'
    LTOP = r'\<'

    # Bitwise Operators
    ANDOP = r'\&'
    OROP = r'\|'
    XOROP = r'\^'

    SEPARATORS = r'\,'
    SEMICOLON = r'\;'
    LCB = r'\('
    RCB = r'\)'
    LFB = r'\{'
    RFB = r'\}'
    LSB = r'\['
    RSB = r'\]'

    INTNUM = r'\d+'
    REALNUM = r'\d+.\d+'
    # Should String Have New Line OR NOT..? Problematic
    # \'.*\' matches longest so in between thing cannot be \' .......That's all
    STRING = r'\'([ \t\n\r\f\v]|[^ \'\t\n\r\f\v])+\''
    # STRING = r'\'.*\''
    # @_(r'''("[^"\\]*(\\.[^"\\]*)*"|'[^'\\]*(\\.[^'\\]*)*')''')

    ignore = r'\t '

    def IDENTIFIER(self, t):
        print()
        print("ID: ",t)
        print()
        return t

    @_('TRUE')
    def BOOL(self, t):
        t.value = 1
        return t

    @_('FALSE')
    def BOOL(self, t):
        t.value = 0
        return t

    # @_('UNKNOWN')
    # def BOOL(self,t):
    #     t.value=-
    #     return t

    def INTNUM(self, t):
        t.value = int(t.value)
        return t

    def REALNUM(self, t):
        t.value = float(t.value)
        return t

    # @_(r'''('\d+'|'\\d+.\d+')''')
    # def NUMS(self, t):
    #     return t

    def STRING(self, t):
        l = len(t.value)
        t.value = t.value[1:(l - 1)]
        try:
            t.value = int(t.value)
            t.type = 'INTNUM'
        except ValueError:
            try:
                t.value = float(t.value)
                t.type = 'REALNUM'
            except ValueError:
                t.type = 'STRING'
        return t

    # ignore_comment = r'\#.*'
    @_(r'#.*')
    def COMMENT(self, t):
        pass

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        print('Line %d: Bad Character -> %r' % (self.lineno, t.value[0]))
        self.index += 1
ERROR_NO = 0

class Query():
    # Specs = {}
    # ColumnList = []
    # ValueList = []
    list_of_op = ['=', '<', '<=', '>', '>=', '<>']
    list_of_logicOp = ['and', 'or', 'not']

    reverse_list_of_op = {'=' : '!=', '<': ">=", '<=' : ">", '>' : "<=", '>=' : '<', '<>' : "="}
    reverse_list_of_logicOp = {'and' : 'or', 'or': 'and'}

    def __init__(self):
        self.Specs = {}
        self.ColumnList = []
        self.ValueList = []
        self.TableList = []

    # def convertCode()
    def debugStructure(self):
        print(self.Specs)
        print(self.ColumnList)
        print(self.ValueList)
        print(self.TableList)

    def clearStructure(self):
        self.Specs = {}
        self.ColumnList = []
        self.ValueList = []
        self.TableList = []

    def addToColumnList(self, column_name):
        # check for duplicates
        if (column_name in self.ColumnList):
            return
        self.ColumnList.append(column_name)

    def addToTableList(self, Table_name):
        # check for duplicates
        if (Table_name in self.TableList):
            return
        self.TableList.append(Table_name)

    def addToValueList(self, value):
        self.ValueList.append(value)

    # Solution for issue with NOT LOGICAL OPERATOR
    def convertCondTree(self,tup,val):
        if(tup[0] in self.list_of_op):
            return (self.reverse_list_of_op[tup[0]],tup[1],tup[1])
        elif(tup[0] in self.list_of_op):
            return 
        return

    def createQueryBaseCase(self, tup):
        if (tup[0] == '='):
            return "{\"" + tup[1] + "\" :" + str(tup[2]) + "}"
        elif (tup[0] == '<'):
            return "{\"" + tup[1] + "\" : { \"$lt\" :" + str(tup[2]) + "}" + "}"
        elif (tup[0] == '<='):
            return "{\"" + tup[1] + "\" : { \"$lte\" :" + str(tup[2]) + "}" + "}"
        elif (tup[0] == '>'):
            return "{\"" + tup[1] + "\" : { \"$gt\" :" + str(tup[2]) + "}" + "}"
        elif (tup[0] == '>='):
            return "{\"" + tup[1] + "\" : { \"$gte\" :" + str(tup[2]) + "}" + "}"
        elif (tup[0] == '<>'):
            return "{\"" + tup[1] + "\" : { \"$ne\" :" + str(tup[2]) + "}" + "}"

    def createQueryParameter(self, cond_tree):
        # For Where Clause and stuff
        if (cond_tree == ''):
            return '{' + '}'

        if (cond_tree[0] in self.list_of_op):
            # base case
            return self.createQueryBaseCase(cond_tree)
        elif (cond_tree[0] in self.list_of_logicOp):
            q1 = self.createQueryParameter(cond_tree[1])
            q2 = self.createQueryParameter(cond_tree[2])
            return "{ $" + cond_tree[0] + " : [" + q1 + ',' + q2 + ']}' 
        return '{' + '}'

    def createPythonQueryBaseCase(self,tup):
        temp = tup[1].split('.')
        tab_name = temp[0]
        # Make Necessary Changes to tab_name here
        # tab to item Converter
        if (tup[0] == '='):
            return tab_name + "." + temp[1] + " == " + str(tup[2])
        elif (tup[0] == '<'):
            return tab_name + "." + temp[1] + " < " + str(tup[2])
        elif (tup[0] == '<='):
            return tab_name + "." + temp[1] + " <= " + str(tup[2])
        elif (tup[0] == '>'):
            return tab_name + "." + temp[1] + " > " + str(tup[2])
        elif (tup[0] == '>='):
            return tab_name + "." + temp[1] + " >= " + str(tup[2])
        elif (tup[0] == '<>'):
            return tab_name + "." + temp[1] + " != " + str(tup[2])

    def createPythonQuery(self,cond_tree):
        if (cond_tree == ''):
            return ''
        
        q1 = ''
        q2 = ''
        if (cond_tree[0] in self.list_of_op):
            # base case
            return self.createPythonQueryBaseCase(cond_tree)
        elif (cond_tree[0] in self.list_of_logicOp):
            q1 = self.createPythonQuery(cond_tree[1])
            if(cond_tree[0] != 'not'):
                q2 = self.createPythonQuery(cond_tree[2])
            if(cond_tree[0] == 'not'):
                return "not (" + q1 + ")"
            else:
                return "(" + q1 + ") " + cond_tree[0] + " (" + q2 + ")"
        return ''

    def itemCheck(self,item):
        if('.' in item):
            return True
        return False
    # select sf,asfafaf,asfa,sf from t1,t2;
    def projectSplitter(self):
        projectDict = {}
        for item in self.TableList:
            projectDict[item] = []
        
        for item in self.ColumnList:
            temp = item.split('.')
            projectDict[temp[0]].append(temp[1])
        return projectDict

    def createCrossProductCode(self,cond_tree):
        code = "finalObj = []\n"
        projecter = {}
        if('*' not in self.ColumnList):
            projecter = self.projectSplitter()
        for item in self.TableList:
            check = self.itemCheck(item)
            projectParam = ''
            if(item in projecter):
                projectParam = self.createProjectParameter(projecter[item])
            # else:
            #     print("are we here")
            #     continue
            
            if(check):
                ERROR_NO = 1
                return
            if(projectParam == ""):                    
                code += item + "Res = db." + item + ".find({" + "})\n" 
            else:
                code += item + "Res = db." + item + ".find({" + "}" + ',' + projectParam + ")\n" 
        # Objs are [item]Res, [item1]Res etc...
        tabSpace = '\n\t\t'
        code += "mergeObj0 = " + self.TableList[0] + "Res\n"
        for i in range(0,len(self.TableList)-1):
            # Objs are [itemi] and [itemi+1]
            # Output Needed 
            # mergeObji = []
            # for item1 in tab1:
                # for item2 in tab2:
                    # mergeObji.append()
            code += "mergeObj" + str(i+1) + "=[]\n"
            code += "for item1 in mergeObj"  + str(i) + ":\n\t"
            code += "for item2 in " + self.TableList[i+1] + "Res:\n\t\t"
            code += "item1.update(item2)" + tabSpace
            code += "mergeObj"+ str(i+1) + ".append(item1)" + tabSpace
            code += "#mergeObj" + str(i+1) + " will contain the result\n"
        code += "finalObj = mergeObj" + str(len(self.TableList)-1) + "\n"
        if(cond_tree != ''):
            code += "for item in finalObj:\n\t"
            code += "if(not (" + self.createPythonQuery(cond_tree) + ")):\n\t\t"
            code += "finalObj.remove(item)\n"
        return code

    def createProjectParameter(self,colList):
        # For Select Parameter -> selecting certain columns
        print("col list " + str(colList))
        if ("*" in colList):
            print("project parameter empty")
            return ''
        elif(len(colList) != 0):
            pairs = []
            for col in colList:
                pairs.append(f'\t\t\"{col}\"  :  {1}')
            pairs.append(f'\t\t\"_id\"  :  {1}')
            s = ',\n'
            s = s.join(pairs)
            print("project parameter" + '{' + s + '}')
            return '\n\t{\n' + s + '\n\t}'
        return ''
        
    def createInsertParameter(self):
        # For insert statement
        if (len(self.ColumnList) != len(self.ValueList)):
            return "Error! Query is Wrong.. Either duplicate column or non-matching length of columns and values"
        pairs = []
        for col, val in zip(self.ColumnList, self.ValueList):
            pairs.append(f'\t\t\"{col}\"  :  {val}')
        s = ',\n'
        s = s.join(pairs)
        print("insert parameter" + '{' + s + '}')
        return '\n\t{\n' + s + '\n\t}'

    def createUpdateParameter(self):
        # For Update Parameter
        if (len(self.ColumnList) != len(self.ValueList)):
            return "Error! Query is Wrong.. non-matching length of columns and values"
        pairs = []
        for col, val in zip(self.ColumnList, self.ValueList):
            pairs.append(f'\t\t\"{col}\"  :  {val}')
        s = ',\n'
        s = s.join(pairs)
        # print("update parameter-" + '{$set:{' + s + '},' + '{' + "multi:true" +'}' + '}'
        return '{\n\t$set:{\n' + s + '\n\t},' + '\n\t{\n' + "\t\tmulti:true" +'\n\t}' + '\n}'
    

    def createAggregateParameter(self):
        # For Things like sum avg etc..
        # Dont know scope
        return

    def convertStructToCode(self):
        code = ''
        obj = self.Specs
        if ('type' not in obj):
            return 'Error!! Query is Wrong'

        if (obj['type'] == 'insert'):
            insert_param = self.createInsertParameter()
            return "db." + obj['table_name'] + ".insert(" + insert_param + ')'
        elif (obj['type'] == 'update'):
            update_param = self.createUpdateParameter()
            query_param = self.createQueryParameter(obj['update_cond_tree'])
            return "db." + obj['table_name'] + ".updateMany(" + query_param + ',' + update_param + ')'
        elif (obj['type'] == 'delete'):
            query_param = self.createQueryParameter(obj['delete_cond_tree'])
            return "db." + obj['table_name'] + ".remove(" + query_param + ')'
        elif (obj['type'] == 'select'):
            project_param = self.createProjectParameter(self.ColumnList)
            
            if(obj['join'] == 1):
                # Code For Join and Return
                code += "resultSet = [" + "]\n"
                if(not project_param):
                    code += "res0 = db." + obj['table_name'] + ".find({" + "})\n"
                else:
                    code += "res0 = db." + obj['table_name'] + ".find({" + "}," + project_param + ")\n"
                for i in range(0,len(obj["join_ID_list"])):
                    code += "obj"+ str(i+1) + " = db." + obj["join_ID_list"][i] + ".find({" + "})\n"

                for i in range(0,len(obj["join_ID_list"])):
                    # Here i should do join based on ON condition and join type
                    code += "res" + str(i+1) + " = [" + "]\n"
                    t1 = "res" + str(i)
                    t2 = "obj" + str(i + 1)
                    if(obj["join_type_list"][i] == 'RIGHT'):
                        t1 = "obj" + str(i + 1)
                        t2 = "res" + str(i)
                    code += "for item in "+ t1 + ":\n\t"
                    code += "matched = False\n\t"
                    code += "for item2 in " + t2 + ":\n\t\t"
                    if(obj["join_type_list"][i] == 'INNER'):
                        code += "if(item[\"" + obj["joining_list"][i][0] + "\"] == item2[\"" + obj["joining_list"][i][1] + "\"]):\n\t\t\t"
                        code += "d1 = item.copy()\n\t\t\t"
                        code += "d2 = item2.copy()\n\t\t\t"
                        code += "d2.update(d1)\n\t\t\t"
                        code += "res" + str(i+1) + ".append(d2)\n"

                    elif(obj["join_type_list"][i] == 'LEFT'):
                        code += "if(item[\"" + obj["joining_list"][i][0] + "\"] == item2[\"" + obj["joining_list"][i][1] + "\"]):\n\t\t\t"
                        code += "d1 = item.copy()\n\t\t\t"
                        code += "d2 = item2.copy()\n\t\t\t"
                        code += "d2.update(d1)\n\t\t\t"
                        code += "matched = True\n\t\t\t"
                        code += "res" + str(i+1) + ".append(d2)\n\t"
                        # Checking for Mathced
                        code += "if(matched):\n\t\t\t"
                        code += "d3 = item.copy()\n\t\t\t"
                        code += "res" + str(i+1) + ".append(d3)\n"

                    elif(obj["join_type_list"][i] == 'RIGHT'):
                        code += "if(item[\"" + obj["joining_list"][i][0] + "\"] == item2[\"" + obj["joining_list"][i][1] + "\"]):\n\t\t\t"
                        code += "d1 = item.copy()\n\t\t\t"
                        code += "d2 = item2.copy()\n\t\t\t"
                        code += "d2.update(d1)\n\t\t\t"
                        code += "matched = True\n\t\t\t"
                        code += "res" + str(i+1) + ".append(d2)\n\t"
                        # Checking for Mathced
                        code += "if(matched):\n\t\t\t"
                        code += "d3 = item.copy()\n\t\t\t"
                        code += "res" + str(i+1) + ".append(d3)\n"
                        
                    elif(obj["join_type_list"][i] == 'FULL'):
                        # Cannot be joined
                        print()
                    print()
                code += "resultSet = res" + str(len(obj["join_ID_list"])) + "\n"
                return code

            query_param = self.createQueryParameter(obj['select_cond_tree'])
            # print(project_param)
            # print(query_param)
            if (obj['is_aggr'] == 0):
                if(len(self.TableList) > 1):
                    print()
                    # Code To do Cross Product..!
                    crossProductQuery = self.createCrossProductCode(obj['select_cond_tree']) 
                    return crossProductQuery
                if (not project_param):
                    return "db." + obj['table_name'] + ".find(" + query_param + ')'
                else:
                    return "db." + obj['table_name'] + ".find(" + query_param + ',' + project_param + ')'
        return ''

# There won't be nested queries : 
# reason -> we are not doing cross column querying between self and different tables..! 
# eg : WHERE table.C1 = table2.C2 or table1.c1 = table1.c2
# increases difficulty to a next level...! From a simple query to query 
# transpiler to a query to PL transpiler....

# If cross product is done now then only use is like 
# eg: SELECT * FROM (SELECT * FROM T1 WHERE c1 = 10 and c2 = 20) WHERE C3 = 1
# => SELECT * FROM T1 where c1 = 10 and c2 = 20 and C3 = 1

Q = Query()
list_of_queries = []

qObjList = []

qObjList.append(Q)

qStack = []

# qStack.append(Q)
class MyParser(Parser):
    tokens = MyLexer.tokens

    precedence = (
        ('left', "OR"),
        ('left', "AND"),
        ('left', "NOT"),
    )
    start = 'start1'

    # start - query_list
    @_('query_list')
    def start1(self, p):
        return (p[0], list_of_queries)

    # query_list - query query_list
    @_('query query_list')
    def query_list(self, p):
        # Q.convertCode()
        finalCode = ''
        Q.debugStructure()
        if(len(qObjList) != 1):
            finalCode = "finalObj = " + qObjList[-1].convertStructToCode()
        else:
            code = Q.convertStructToCode()
            list_of_queries.append(code)
        Q.clearStructure()
        return p[0]

    @_('empty')
    def query_list(self, p):
        return

    @_('')
    def empty(self, p):
        pass

    @_('select_stmt SEMICOLON')
    def query(self, p):
        Q.Specs["type"] = "select"
        return "SELECT_STATEMENT"
    
    # @_('table_join SEMICOLON')
    # def query(self,p):
    #     return
    
    @_('update_stmt SEMICOLON')
    def query(self, p):
        Q.Specs["type"] = "update"
        return "UPDATE_STATEMENT"

    @_('insert_stmt SEMICOLON')
    def query(self, p):
        Q.Specs["type"] = "insert"
        return "INSERT_STATEMENT"

    @_('delete_stmt SEMICOLON')
    def query(self, p):
        Q.Specs["type"] = "delete"
        return "DELETE_STATEMENT"

    # --------------- INSERT STATEMENT ---------------
    @_('INSERT INTO IDENTIFIER LCB insert_col_list RCB VALUES LCB val_list RCB')
    def insert_stmt(self, p):
        Q.Specs["table_name"] = p[2]
        return

    @_('insert_col_list COMMA IDENTIFIER')
    def insert_col_list(self, p):
        Q.addToColumnList(p[2])
        # print("Id Printed", p[2])
        return

    @_('IDENTIFIER')
    def insert_col_list(self, p):
        Q.addToColumnList(p[0])
        # print("One Id Printed", p[0])
        return

    @_('val_list COMMA value')
    def val_list(self, p):
        Q.addToValueList(p[2])
        return

    @_('value')
    def val_list(self, p):
        Q.addToValueList(p[0])
        return

    # --------------- INSERT STATEMENT ---------------

    # --------------- TABLE JOIN (self join , cross join , inner join , left join, right join, full outer join) ---------------
    
    # @_('SELECT select_col_list FROM IDENTIFIER join_list SEMICOLON')
    # def opt_table_join(self, p):
    #     return


    # @_('SELECT select_col_list FROM IDENTIFIER join_list SEMICOLON')
    # def opt_table_join(self, p):
    #     return

    # JOIN SYNTAX ___
    # SELECT COl_list FROM TABLE JOIN_TYPE(LEFT JOIN,RIGHT,INNER) IDENTIFIER ON t1.c1 = t2.c2
    # select * from t1 LEFT JOIN t2 on c1=c2 RIGHT JOIN t3 on c2 = c3
    @_('join_list joins IDENTIFIER opt_join_clause')
    def join_list(self, p):
        Q.Specs["join"] = 1
        # Set Error Code Here (Like...)
        if("is_distinct" in Q.Specs and Q.Specs["is_distinct"] == 1):
            ERROR_NO = 1
        if("is_aggr" in Q.Specs and Q.Specs["is_aggr"] == 1):
            ERROR_NO = 1
        if("select_cond_tree" in Q.Specs and Q.Specs["select_cond_tree"] != ''):
            ERROR_NO = 1
        if("limit_value" in Q.Specs):
            ERROR_NO = 1
        Q.Specs["join_ID_list"].append(p[2])
        return
    
    @_('')
    def join_list(self,p):
        Q.Specs["join"] = 0
        Q.Specs["join_type_list"] = []
        Q.Specs["join_ID_list"] = []
        Q.Specs["joining_list"] = []
        return

    @_('INNER JOIN','LEFT JOIN','RIGHT JOIN','FULL OUTER JOIN')
    def joins(self, p):
        Q.Specs["join_type_list"].append(p[0])
        return 

    @_('ON IDENTIFIER EQUAL IDENTIFIER')
    def opt_join_clause(self, p):
        Q.Specs["joining_list"].append((p[1],p[3])) 
        return
    
    # @_('')
    # def opt_join_clause(self, p):
    #     Q.Specs["joining_list"].append("") 
    #     return
    
        
    # @_('IDENTIFIER EQUAL IDENTIFIER','condition')
    # def opt_condition(self, p):
    #     return

    # @_('=')
    # def EQUAL(self, p):
    #     return '='
    
    # --------------- TABLE JOIN (self join , cross join , inner join , left join, right join, full outer join) ---------------

    # --------------- SELECT STATEMENT ---------------
    @_('SELECT is_distinct select_param FROM select_res select_opt_where sort_order opt_limit join_list')
    def select_stmt(self, p):
        # Q.Specs["table_name"] = p[4]
        # Return if select is nest end or not.!
        # if(qStack):
        #     Q = qStack[-1]
        #     qStack.pop()
        # qObjList.append(Q)
        Q.Specs["select_cond_tree"] = p[5]
        return

    @_('LCB select_stmt RCB')
    def select_res(self,p):
        qStack.append(Q)
        Q = Query()
        return

    @_('select_table_list')
    def select_res(self,p):
        return

    @_('IDENTIFIER')
    def select_table_list(self,p):
        Q.Specs["table_name"] = p[0]
        Q.addToTableList(p[0])
        return

    @_('select_table_list COMMA IDENTIFIER')
    def select_table_list(self,p):
        Q.addToTableList(p[2])
        return

    @_('DISTINCT')
    def is_distinct(self, p):
        Q.Specs["is_distinct"] = 1
        return

    @_('')
    def is_distinct(self, p):
        Q.Specs["is_distinct"] = 0
        return

    @_('select_col_list')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"] = 0
        return

    @_('MULOP')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.addToColumnList('*')
        Q.Specs["is_aggr"] = 0
        return

    @_('MAX LCB IDENTIFIER RCB')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"] = 1
        Q.Specs["aggr"] = "MAX"
        Q.Specs["aggr_list"] = p[2]
        return

    @_('MIN LCB IDENTIFIER RCB')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"] = 1
        Q.Specs["aggr"] = "MIN"
        Q.Specs["aggr_list"] = p[2]
        return

    @_('COUNT LCB IDENTIFIER RCB')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"] = 1
        Q.Specs["aggr"] = "COUNT"
        Q.Specs["aggr_list"] = p[2]
        return

    @_('COUNT LCB MULOP RCB')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"] = 1
        Q.Specs["aggr"] = "COUNT"
        Q.Specs["aggr_list"] = p[2]
        return

    @_('SUM LCB IDENTIFIER RCB')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"] = 1
        Q.Specs["aggr"] = "SUM"
        Q.Specs["aggr_list"] = p[2]
        return

    @_('AVG LCB IDENTIFIER RCB')
    def select_param(self, p):
        # Whether it is an aggregate function or not
        Q.Specs["is_aggr"] = 1
        Q.Specs["aggr"] = "AVG"
        Q.Specs["aggr_list"] = p[2]
        return

    @_('select_col_list COMMA IDENTIFIER opt_aliasing')
    def select_col_list(self, p):
        Q.addToColumnList(p[2])
        if (p[3] != ''):
            Q.Specs['alias_map'][p[2]] = p[3]
        return

    @_('IDENTIFIER opt_aliasing')
    def select_col_list(self, p):
        Q.addToColumnList(p[0])
        Q.Specs['alias_map'] = {}
        if (p[1] != ''):
            Q.Specs['alias_map'][p[0]] = p[1]
        return

    @_('AS IDENTIFIER')
    def opt_aliasing(self, p):
        return p[1]

    @_('')
    def opt_aliasing(self, p):
        return ''

    @_('WHERE condition_list')
    def select_opt_where(self, p):
        return p[1]

    @_('IDENTIFIER IS NULL')
    def condition(self, p):
        return ('=', p[0], '')

    @_('IDENTIFIER IS NOT NULL')
    def condition(self, p):
        return ('<>', p[0], '')

    @_('')
    def select_opt_where(self, p):
        return ''

    @_('NOT condition_list')
    def condition_list(self, p):
        return ('not', p[1])

    @_('condition_list AND condition_list')
    def condition_list(self, p):
        return ('and', p[0], p[2])

    @_('condition_list OR condition_list')
    def condition_list(self, p):
        return ('or', p[0], p[2])

    @_('condition')
    def condition_list(self, p):
        return p[0]

    @_('IDENTIFIER EQUAL value', 'IDENTIFIER GTEQ value', 'IDENTIFIER LTEQ value', 'IDENTIFIER GTOP value',
       'IDENTIFIER LTOP value', 'IDENTIFIER NOTEQ value')
    def condition(self, p):
        # print(p[0],p[1],p[2])
        return (p[1], p[0], p[2])

    @_('LCB condition_list RCB')
    def condition(self, p):
        return (p[1])

    @_('ORDER BY ASC')
    def sort_order(self, p):
        Q.Specs["sort_order"] = 0
        return

    @_('ORDER BY DESC')
    def sort_order(self, p):
        Q.Specs["sort_order"] = 1
        return

    @_('')
    def sort_order(self, p):
        Q.Specs["sort_order"] = -1
        return

    @_('LIMIT INTNUM opt_offset')
    def opt_limit(self, p):
        Q.Specs["limit_value"] = p[1]
        return

    @_('')
    def opt_limit(self, p):
        return

    @_('OFFSET INTNUM')
    def opt_offset(self, p):
        Q.Specs["offset"] = p[1]
        return

    @_('')
    def opt_offset(self, p):
        return

    # --------------- SELECT STATEMENT ---------------

    # --------------- DELETE STATEMENT ---------------
    @_('DELETE FROM IDENTIFIER delete_opt_where')
    def delete_stmt(self, p):
        Q.Specs["table_name"] = p[2]
        # Either Empty or a tree of tuple as a node
        Q.Specs["delete_cond_tree"] = p[3]
        return

    @_('WHERE condition_list')
    def delete_opt_where(self, p):
        return p[1]

    @_('')
    def delete_opt_where(self, p):
        return ""

    # --------------- DELETE STATEMENT ---------------

    # --------------- UPDATE STATEMENT ---------------

    @_('UPDATE IDENTIFIER SET col_assigns select_opt_where')
    def update_stmt(self, p):
        Q.Specs["table_name"] = p[1]
        # Either Empty or a tree of tuple as a node
        Q.Specs["update_cond_tree"] = p[4]
        return

    @_('col_assigns COMMA col_assign')
    def col_assigns(self, p):
        return

    @_('col_assign')
    def col_assigns(self, p):
        return

    @_('column_name EQUAL value')
    def col_assign(self, p):
        # adding column = value for update parameter
        Q.addToColumnList(p[0])
        Q.addToValueList(p[2])
        return

    @_('IDENTIFIER')
    def column_name(self, p):
        return p[0]

    @_('INTNUM', 'REALNUM')
    def value(self, p):
        # Q.addToValueList(p[0])
        # print("One val Printed", p[0])
        # print(p[0].type)
        # try:
        #     print(p.STRING)
        #     print("Issue with String")
        # except ValueError:
        #     print("PROBLEM")
        return p[0]

    @_('STRING')
    def value(self, p):
        return "\"" + p[0] + "\""

    # --------------- UPDATE STATEMENT ---------------

    def error(self, p):
        if p:
            print("Syntax error at token", p.type, p.value)
            # Just discard the token and tell the parser it's okay.
            # self.errok()
            ERROR_GLOB = 1
        else:
            print("Syntax error at EOF")

# Create your views here.
def frontend(request):
    query=""
    input = ""
    if 'clear' in request.POST:
        return render(request, 'index.html', {'querystr':"",'value':""})
    if request.POST.get('query'):
        query = request.POST.get('query')
        print("query is ", query)
        input = query
    list_of_queries.clear()
    lex = MyLexer()
    par = MyParser()
    print(input)
    # while True:
    try:
        # # text = input(' Input > ')
        # selectText = '''SELECT abc,cde AS aliases FROM Something WHERE KEKE > 10 OR Top > 50 AND (somee =10 OR kake = 2000);'''
        # deleteText = '''DELETE FROM TAEEE;'''
        # tokenTester = '''
        # INSERT INTO GG (col1,col2,col3,col4,col5) VALUES (10,'asfasfasf',30,40,50);'''
        # updateTester = '''
        # UPDATE Customers
        # SET ContactName='Juan',jj='sine' WHERE Country<'Mexico';'''
        # someString = '''
        # SELECT a,b,c FROM TAB2 WHERE a=1,b=2,c=3;'''
        Q.clearStructure()
        ERROR_GLOB = 0
        result = par.parse(lex.tokenize(input))
        # result = sqlparse.format(result, reindent=True, keyword_case='upper')
        print(result)
        try:
            if(ERROR_GLOB == 1):
                query = input + '\n\n\n' + 'The given query is unsupported or wrong'
                return render(request, 'index.html', {'querystr':input,'value':query})
            print(list_of_queries)
            query = list_of_queries[0]
        except:
            pass
    except EOFError:
        print("EOF Error")
    # ans = sqlparse.format(query, reindent=True, keyword_case='upper')
    return render(request, 'index.html', {'querystr':input,'value':query})

if __name__ == '__main__':
    lexer = MyLexer()
    parser = MyParser()

    # while True:
    try:
        # text = input(' Input > ')
        selectText = '''SELECT abc,cde AS aliases FROM Something WHERE KEKE > 10 OR Top > 50 AND (somee =10 OR kake = 2000);'''
        deleteText = '''DELETE FROM TAEEE;'''
        tokenTester = '''
        INSERT INTO GG (col1,col2,col3,col4,col5) VALUES (10,'asfasfasf',30,40,50);'''
        updateTester = '''
        UPDATE Customers
        SET ContactName='Juan',jj='sine' WHERE Country<'Mexico';'''
        joinText = '''SELECT * FROM T1 INNER JOIN T2 ON T1.col1 = T2.col2;'''
        crossProductText = '''SELECT * FROM T1,T2;'''
        result = parser.parse(lexer.tokenize(crossProductText))
        print(result)
    except EOFError:
        print("EOF Error")
