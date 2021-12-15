// Generated from c:\Users\Xeno\Desktop\CS-Projects\Other Repos\ParserProject\python.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class pythonParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, VAR=24, NUMBER=25, 
		LETTER=26, STRING=27, ARITHMETIC=28, STR=29, INT=30, STRADD=31, DIGIT=32, 
		LOWER=33, UPPER=34, COMMENT=35, OP=36, ASSIGN=37, NL=38, WS=39, INDENT=40, 
		DEDENT=41;
	public static final int
		RULE_prog = 0, RULE_expression = 1, RULE_variableExpression = 2, RULE_evaluatorExpression = 3, 
		RULE_ifExpression = 4, RULE_whileExpression = 5, RULE_forExpression = 6, 
		RULE_printStatement = 7, RULE_iterable = 8, RULE_block = 9;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "expression", "variableExpression", "evaluatorExpression", "ifExpression", 
			"whileExpression", "forExpression", "printStatement", "iterable", "block"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'!'", "'<='", "'<'", "'=='", "'>'", "'>='", "'!='", "'and'", "'or'", 
			"'not'", "'if'", "'('", "')'", "':'", "'elif'", "'else'", "'while'", 
			"'for'", "'in'", "'print('", "'range('", "','", "'break'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"VAR", "NUMBER", "LETTER", "STRING", "ARITHMETIC", "STR", "INT", "STRADD", 
			"DIGIT", "LOWER", "UPPER", "COMMENT", "OP", "ASSIGN", "NL", "WS", "INDENT", 
			"DEDENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "python.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public pythonParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(pythonParser.EOF, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(23);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__10) | (1L << T__16) | (1L << T__17) | (1L << T__19) | (1L << VAR))) != 0)) {
				{
				{
				setState(20);
				expression();
				}
				}
				setState(25);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(26);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public VariableExpressionContext variableExpression() {
			return getRuleContext(VariableExpressionContext.class,0);
		}
		public IfExpressionContext ifExpression() {
			return getRuleContext(IfExpressionContext.class,0);
		}
		public WhileExpressionContext whileExpression() {
			return getRuleContext(WhileExpressionContext.class,0);
		}
		public ForExpressionContext forExpression() {
			return getRuleContext(ForExpressionContext.class,0);
		}
		public PrintStatementContext printStatement() {
			return getRuleContext(PrintStatementContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_expression);
		try {
			setState(33);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(28);
				variableExpression();
				}
				break;
			case T__10:
				enterOuterAlt(_localctx, 2);
				{
				setState(29);
				ifExpression();
				}
				break;
			case T__16:
				enterOuterAlt(_localctx, 3);
				{
				setState(30);
				whileExpression();
				}
				break;
			case T__17:
				enterOuterAlt(_localctx, 4);
				{
				setState(31);
				forExpression();
				}
				break;
			case T__19:
				enterOuterAlt(_localctx, 5);
				{
				setState(32);
				printStatement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableExpressionContext extends ParserRuleContext {
		public List<TerminalNode> VAR() { return getTokens(pythonParser.VAR); }
		public TerminalNode VAR(int i) {
			return getToken(pythonParser.VAR, i);
		}
		public TerminalNode ASSIGN() { return getToken(pythonParser.ASSIGN, 0); }
		public TerminalNode STRING() { return getToken(pythonParser.STRING, 0); }
		public TerminalNode ARITHMETIC() { return getToken(pythonParser.ARITHMETIC, 0); }
		public TerminalNode NUMBER() { return getToken(pythonParser.NUMBER, 0); }
		public TerminalNode NL() { return getToken(pythonParser.NL, 0); }
		public VariableExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableExpression; }
	}

	public final VariableExpressionContext variableExpression() throws RecognitionException {
		VariableExpressionContext _localctx = new VariableExpressionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_variableExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			match(VAR);
			setState(36);
			match(ASSIGN);
			setState(37);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << NUMBER) | (1L << STRING) | (1L << ARITHMETIC))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(39);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(38);
				match(NL);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EvaluatorExpressionContext extends ParserRuleContext {
		public List<TerminalNode> VAR() { return getTokens(pythonParser.VAR); }
		public TerminalNode VAR(int i) {
			return getToken(pythonParser.VAR, i);
		}
		public List<TerminalNode> NUMBER() { return getTokens(pythonParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(pythonParser.NUMBER, i);
		}
		public List<TerminalNode> ARITHMETIC() { return getTokens(pythonParser.ARITHMETIC); }
		public TerminalNode ARITHMETIC(int i) {
			return getToken(pythonParser.ARITHMETIC, i);
		}
		public EvaluatorExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_evaluatorExpression; }
	}

	public final EvaluatorExpressionContext evaluatorExpression() throws RecognitionException {
		EvaluatorExpressionContext _localctx = new EvaluatorExpressionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_evaluatorExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << NUMBER) | (1L << ARITHMETIC))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(44);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				{
				setState(42);
				match(T__0);
				}
				break;
			case T__1:
			case T__2:
			case T__3:
			case T__4:
			case T__5:
			case T__6:
				{
				setState(43);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__5) | (1L << T__6))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(46);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << NUMBER) | (1L << ARITHMETIC))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(56);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__7) | (1L << T__8) | (1L << T__9))) != 0)) {
				{
				{
				setState(47);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__7) | (1L << T__8) | (1L << T__9))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(48);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << NUMBER) | (1L << ARITHMETIC))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(51);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__0:
					{
					setState(49);
					match(T__0);
					}
					break;
				case T__1:
				case T__2:
				case T__3:
				case T__4:
				case T__5:
					{
					setState(50);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__5))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(53);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << NUMBER) | (1L << ARITHMETIC))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(58);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IfExpressionContext extends ParserRuleContext {
		public List<EvaluatorExpressionContext> evaluatorExpression() {
			return getRuleContexts(EvaluatorExpressionContext.class);
		}
		public EvaluatorExpressionContext evaluatorExpression(int i) {
			return getRuleContext(EvaluatorExpressionContext.class,i);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public IfExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifExpression; }
	}

	public final IfExpressionContext ifExpression() throws RecognitionException {
		IfExpressionContext _localctx = new IfExpressionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_ifExpression);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(59);
			match(T__10);
			setState(61);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__11) {
				{
				setState(60);
				match(T__11);
				}
			}

			setState(63);
			evaluatorExpression();
			setState(65);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__12) {
				{
				setState(64);
				match(T__12);
				}
			}

			setState(67);
			match(T__13);
			setState(68);
			block();
			}
			setState(83);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(70);
					match(T__14);
					setState(72);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__11) {
						{
						setState(71);
						match(T__11);
						}
					}

					setState(74);
					evaluatorExpression();
					setState(76);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__12) {
						{
						setState(75);
						match(T__12);
						}
					}

					setState(78);
					match(T__13);
					setState(79);
					block();
					}
					} 
				}
				setState(85);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			}
			setState(89);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(86);
				match(T__15);
				setState(87);
				match(T__13);
				setState(88);
				block();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WhileExpressionContext extends ParserRuleContext {
		public EvaluatorExpressionContext evaluatorExpression() {
			return getRuleContext(EvaluatorExpressionContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WhileExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileExpression; }
	}

	public final WhileExpressionContext whileExpression() throws RecognitionException {
		WhileExpressionContext _localctx = new WhileExpressionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_whileExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(91);
			match(T__16);
			setState(92);
			evaluatorExpression();
			setState(93);
			match(T__13);
			setState(94);
			block();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ForExpressionContext extends ParserRuleContext {
		public List<TerminalNode> VAR() { return getTokens(pythonParser.VAR); }
		public TerminalNode VAR(int i) {
			return getToken(pythonParser.VAR, i);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public IterableContext iterable() {
			return getRuleContext(IterableContext.class,0);
		}
		public ForExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forExpression; }
	}

	public final ForExpressionContext forExpression() throws RecognitionException {
		ForExpressionContext _localctx = new ForExpressionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_forExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(96);
			match(T__17);
			setState(97);
			match(VAR);
			setState(98);
			match(T__18);
			setState(101);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				{
				setState(99);
				match(VAR);
				}
				break;
			case T__20:
				{
				setState(100);
				iterable();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(103);
			match(T__13);
			setState(104);
			block();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PrintStatementContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(pythonParser.STRING, 0); }
		public TerminalNode VAR() { return getToken(pythonParser.VAR, 0); }
		public TerminalNode NUMBER() { return getToken(pythonParser.NUMBER, 0); }
		public TerminalNode ARITHMETIC() { return getToken(pythonParser.ARITHMETIC, 0); }
		public TerminalNode STRADD() { return getToken(pythonParser.STRADD, 0); }
		public TerminalNode NL() { return getToken(pythonParser.NL, 0); }
		public PrintStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printStatement; }
	}

	public final PrintStatementContext printStatement() throws RecognitionException {
		PrintStatementContext _localctx = new PrintStatementContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_printStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(106);
			match(T__19);
			setState(107);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << NUMBER) | (1L << STRING) | (1L << ARITHMETIC) | (1L << STRADD))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(108);
			match(T__12);
			}
			setState(111);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				setState(110);
				match(NL);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IterableContext extends ParserRuleContext {
		public List<TerminalNode> NUMBER() { return getTokens(pythonParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(pythonParser.NUMBER, i);
		}
		public List<TerminalNode> VAR() { return getTokens(pythonParser.VAR); }
		public TerminalNode VAR(int i) {
			return getToken(pythonParser.VAR, i);
		}
		public List<TerminalNode> ARITHMETIC() { return getTokens(pythonParser.ARITHMETIC); }
		public TerminalNode ARITHMETIC(int i) {
			return getToken(pythonParser.ARITHMETIC, i);
		}
		public IterableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_iterable; }
	}

	public final IterableContext iterable() throws RecognitionException {
		IterableContext _localctx = new IterableContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_iterable);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(113);
			match(T__20);
			setState(118);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				setState(114);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << NUMBER) | (1L << ARITHMETIC))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case 2:
				{
				setState(115);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << NUMBER) | (1L << ARITHMETIC))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(116);
				match(T__21);
				setState(117);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << VAR) | (1L << NUMBER) | (1L << ARITHMETIC))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			}
			setState(120);
			match(T__12);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public TerminalNode INDENT() { return getToken(pythonParser.INDENT, 0); }
		public TerminalNode NL() { return getToken(pythonParser.NL, 0); }
		public TerminalNode DEDENT() { return getToken(pythonParser.DEDENT, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_block);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
			match(INDENT);
			setState(132);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
			case T__16:
			case T__17:
			case T__19:
			case VAR:
				{
				{
				setState(124); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(123);
						expression();
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(126); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				setState(129);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
				case 1:
					{
					setState(128);
					match(T__22);
					}
					break;
				}
				}
				}
				break;
			case T__22:
				{
				setState(131);
				match(T__22);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(135);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				{
				setState(134);
				match(NL);
				}
				break;
			}
			setState(138);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				{
				setState(137);
				match(DEDENT);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3+\u008f\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\3\2\7\2\30\n\2\f\2\16\2\33\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3$\n"+
		"\3\3\4\3\4\3\4\3\4\5\4*\n\4\3\5\3\5\3\5\5\5/\n\5\3\5\3\5\3\5\3\5\3\5\5"+
		"\5\66\n\5\3\5\7\59\n\5\f\5\16\5<\13\5\3\6\3\6\5\6@\n\6\3\6\3\6\5\6D\n"+
		"\6\3\6\3\6\3\6\3\6\3\6\5\6K\n\6\3\6\3\6\5\6O\n\6\3\6\3\6\3\6\7\6T\n\6"+
		"\f\6\16\6W\13\6\3\6\3\6\3\6\5\6\\\n\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b"+
		"\3\b\3\b\5\bh\n\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\tr\n\t\3\n\3\n\3\n"+
		"\3\n\3\n\5\ny\n\n\3\n\3\n\3\13\3\13\6\13\177\n\13\r\13\16\13\u0080\3\13"+
		"\5\13\u0084\n\13\3\13\5\13\u0087\n\13\3\13\5\13\u008a\n\13\3\13\5\13\u008d"+
		"\n\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\b\4\2\32\33\35\36\4\2\32\33"+
		"\36\36\3\2\4\t\3\2\n\f\3\2\4\b\5\2\32\33\35\36!!\2\u009b\2\31\3\2\2\2"+
		"\4#\3\2\2\2\6%\3\2\2\2\b+\3\2\2\2\n=\3\2\2\2\f]\3\2\2\2\16b\3\2\2\2\20"+
		"l\3\2\2\2\22s\3\2\2\2\24|\3\2\2\2\26\30\5\4\3\2\27\26\3\2\2\2\30\33\3"+
		"\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\34\3\2\2\2\33\31\3\2\2\2\34\35\7"+
		"\2\2\3\35\3\3\2\2\2\36$\5\6\4\2\37$\5\n\6\2 $\5\f\7\2!$\5\16\b\2\"$\5"+
		"\20\t\2#\36\3\2\2\2#\37\3\2\2\2# \3\2\2\2#!\3\2\2\2#\"\3\2\2\2$\5\3\2"+
		"\2\2%&\7\32\2\2&\'\7\'\2\2\')\t\2\2\2(*\7(\2\2)(\3\2\2\2)*\3\2\2\2*\7"+
		"\3\2\2\2+.\t\3\2\2,/\7\3\2\2-/\t\4\2\2.,\3\2\2\2.-\3\2\2\2/\60\3\2\2\2"+
		"\60:\t\3\2\2\61\62\t\5\2\2\62\65\t\3\2\2\63\66\7\3\2\2\64\66\t\6\2\2\65"+
		"\63\3\2\2\2\65\64\3\2\2\2\66\67\3\2\2\2\679\t\3\2\28\61\3\2\2\29<\3\2"+
		"\2\2:8\3\2\2\2:;\3\2\2\2;\t\3\2\2\2<:\3\2\2\2=?\7\r\2\2>@\7\16\2\2?>\3"+
		"\2\2\2?@\3\2\2\2@A\3\2\2\2AC\5\b\5\2BD\7\17\2\2CB\3\2\2\2CD\3\2\2\2DE"+
		"\3\2\2\2EF\7\20\2\2FG\5\24\13\2GU\3\2\2\2HJ\7\21\2\2IK\7\16\2\2JI\3\2"+
		"\2\2JK\3\2\2\2KL\3\2\2\2LN\5\b\5\2MO\7\17\2\2NM\3\2\2\2NO\3\2\2\2OP\3"+
		"\2\2\2PQ\7\20\2\2QR\5\24\13\2RT\3\2\2\2SH\3\2\2\2TW\3\2\2\2US\3\2\2\2"+
		"UV\3\2\2\2V[\3\2\2\2WU\3\2\2\2XY\7\22\2\2YZ\7\20\2\2Z\\\5\24\13\2[X\3"+
		"\2\2\2[\\\3\2\2\2\\\13\3\2\2\2]^\7\23\2\2^_\5\b\5\2_`\7\20\2\2`a\5\24"+
		"\13\2a\r\3\2\2\2bc\7\24\2\2cd\7\32\2\2dg\7\25\2\2eh\7\32\2\2fh\5\22\n"+
		"\2ge\3\2\2\2gf\3\2\2\2hi\3\2\2\2ij\7\20\2\2jk\5\24\13\2k\17\3\2\2\2lm"+
		"\7\26\2\2mn\t\7\2\2no\7\17\2\2oq\3\2\2\2pr\7(\2\2qp\3\2\2\2qr\3\2\2\2"+
		"r\21\3\2\2\2sx\7\27\2\2ty\t\3\2\2uv\t\3\2\2vw\7\30\2\2wy\t\3\2\2xt\3\2"+
		"\2\2xu\3\2\2\2yz\3\2\2\2z{\7\17\2\2{\23\3\2\2\2|\u0086\7*\2\2}\177\5\4"+
		"\3\2~}\3\2\2\2\177\u0080\3\2\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081"+
		"\u0083\3\2\2\2\u0082\u0084\7\31\2\2\u0083\u0082\3\2\2\2\u0083\u0084\3"+
		"\2\2\2\u0084\u0087\3\2\2\2\u0085\u0087\7\31\2\2\u0086~\3\2\2\2\u0086\u0085"+
		"\3\2\2\2\u0087\u0089\3\2\2\2\u0088\u008a\7(\2\2\u0089\u0088\3\2\2\2\u0089"+
		"\u008a\3\2\2\2\u008a\u008c\3\2\2\2\u008b\u008d\7+\2\2\u008c\u008b\3\2"+
		"\2\2\u008c\u008d\3\2\2\2\u008d\25\3\2\2\2\26\31#).\65:?CJNU[gqx\u0080"+
		"\u0083\u0086\u0089\u008c";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}