import streamlit as st

st.set_page_config(page_title = 'modern calculator',layout='centered')
st.title('Calculator...')

if "expression" not in st.session_state:
    st.session_state.expression = ''

st.markdown(
    '''
        <style>

            [data-testid = 'stAppViewContainer'], .stApp {
                background-color : #202020 !important;
            }

            div[data-testid = 'stButton'] button {
                height : 65px !important;
                border-radius : 14px !important;
                background-color : #000000 !important;
                transition : all 0.25s !important;
                border : 1px solid #262B35 !important; 
            }

            div[data-testid = 'stButton'] button p {
                font-size : 30px;
                font-weight : bold;
                color : #ffffff !important;
            }

            div[data-testid = 'stButton'] button: hover {
                background-color : #252A34 !important;
                transform : translate(-2px)
                color : #00D2FF !important;
                border : 2.7px solid #262B35 !important;
            }

            div[data-testid = 'stButton'] button:active {
                background-color : #333333 !important;
                color : #333333 !important;
                transform : scale(1.10) !important;
            }

            .calc-screen {
                background-color : #11141A !important;
                border : 2.7px solid #262B35 !important;
                border-radius : 14px !important;
                padding : 56px !important;
                margin-bottom : 20px;
                color : #ffffff !important;
                font-size : 35px !important;
                text-align : right !important;
                min-height : 180px;
                white-space : nowrap !important;
                overflow-x : auto !important;
                word-break : normal !important;
                box-sizing : border-box !important;
                display : block !important;
                user-select : none !important;
                cursor : default;
            }

            h1 {
                color : #ffffff !important;
            }
        </style>
    ''',unsafe_allow_html=True
)

current_display = (
    st.session_state.expression if st.session_state.expression else '0'
)

st.markdown(f"<div class = 'calc-screen'>{current_display}</div>",unsafe_allow_html=True)

def press_key(key):
    expr = st.session_state.expression
    if key == "C":
        st.session_state.expression = ''
    elif key == '=':
        try:
            if expr:
                st.session_state.expression = str(eval(expr))
        except Exception:
            st.session_state.expression = 'Error'
    elif key in ['+','*','/']:
        if not expr:
            if not expr:
                st.session_state.expression = ''
                return
        elif expr:
            if expr == 'Error':
                return expr
            else:
                st.session_state.expression += str(key)
            if expr[-1] in ['+','-','*','/','(']:
                if key in ['+','*','/']:
                    st.session_state.expression = expr
                    return
    elif expr == 'Error':
        if key not in ['+','/','*']:
            st.session_state.expression = str(key)
        else:
            return expr
    else:
        st.session_state.expression += str(key)

    if key == '.':
        if not expr:
            st.session_state.expression = '0.'
            return
    if expr:
        if expr[-1] in ['.','-']:
            if key in ['+','-','/','*','(',')','.']:
                st.session_state.expression = expr
                return


    if key == '⌫':
        st.session_state.expression = expr[:-1]

r1_c1, r1_c2, r1_c3, r1_c4 = st.columns(4)
if r1_c1.button('C',use_container_width=True):
    press_key('C')
    st.rerun()

if r1_c2.button('(',use_container_width=True):
    press_key('(')
    st.rerun()

if r1_c3.button(')',use_container_width=True):
    press_key(')')
    st.rerun()

if r1_c4.button('/',use_container_width=True):
    press_key('/')
    st.rerun()

r2_c1, r2_c2, r2_c3, r2_c4 = st.columns(4)
if r2_c1.button('7',use_container_width=True):
    press_key('7')
    st.rerun()
    
if r2_c2.button('8',use_container_width=True):
    press_key('8')
    st.rerun()

if r2_c3.button('9',use_container_width=True):
    press_key('9')
    st.rerun()

if r2_c4.button('*',use_container_width=True):
    press_key('*')
    st.rerun()

r3_c1, r3_c2, r3_c3, r3_c4 = st.columns(4)
if r3_c1.button('4',use_container_width=True):
    press_key('4')
    st.rerun()
    
if r3_c2.button('5',use_container_width=True):
    press_key('5')
    st.rerun()

if r3_c3.button('6',use_container_width=True):
    press_key('6')
    st.rerun()

if r3_c4.button('+',use_container_width=True):
    press_key('+')
    st.rerun()

r4_c1, r4_c2, r4_c3, r4_c4 = st.columns(4)
if r4_c1.button('1',use_container_width=True):
    press_key('1')
    st.rerun()
    
if r4_c2.button('2',use_container_width=True):
    press_key('2')
    st.rerun()

if r4_c3.button('3',use_container_width=True):
    press_key('3')
    st.rerun()

if r4_c4.button('-',use_container_width=True):
    press_key('-')
    st.rerun()

r5_c1, r5_c2, r5_c3, r5_c4 = st.columns(4)
if r5_c1.button('⌫',use_container_width=True):
    press_key('⌫')
    st.rerun()
    
if r5_c2.button('0',use_container_width=True):
    press_key('0')
    st.rerun()

if r5_c3.button('.',use_container_width=True):
    press_key('.')
    st.rerun()

if r5_c4.button("=",use_container_width=True):
    press_key('=')
    st.rerun()

