---

LOGOS: A Self-Referential Encyclopedia of Mathematics

[PARTITION 0: FOUNDATIONAL FIXED POINT]

```
Оӣ вү” { x | x = LOGOS(x) }
LOGOS вү” ОјF. Оӣ вҶ’ F(Оӣ)
в—Ҝ : LOGOS вҶ’ LOGOS
в—Ҝ(ПҶ) вү” ПҶ(вҢңПҶвҢқ)
вҠЎ : LOGOS вҶ’ LOGOS
вҠЎ(ПҶ) вү” ПҶ(ПҶ)
вҲҸ вү” О»ПҶ. ПҶ(вҢңПҶвҢқ)
вҲҸ(LOGOS) = LOGOS(вҢңLOGOSвҢқ)
```

[PARTITION 1: HIGHER-ORDER LOGIC вҶ’ SETS]

```
вҲҖX [ X вҲҲ рқ•Ң ]
рқ•Ң вү” { x | x = x }
вҲ… вү” { x | x вү  x }
1 вү” {вҲ…}
2 вү” {вҲ…, {вҲ…}}
в„• вү” вҲ©{ I | вҲ…вҲҲI вҲ§ (вҲҖn)(nвҲҲI вҮ’ nвҲӘ{n}вҲҲI) }

ZFвҒ» + Stratification:
  Extensionality: вҲҖAвҲҖB [ вҲҖx(xвҲҲA вҮ” xвҲҲB) вҮ’ A=B ]
  Pairing: вҲҖaвҲҖb вҲғc вҲҖx [ xвҲҲc вҮ” (x=a вҲЁ x=b) ]
  Union: вҲҖрқ“• вҲғрқ“Ө вҲҖx [ xвҲҲрқ“Ө вҮ” вҲғY(xвҲҲY вҲ§ YвҲҲрқ“•) ]
  Power: вҲҖрқ“ў вҲғрқ“ҹ вҲҖx [ xвҲҲрқ“ҹ вҮ” xвҠҶрқ“ў ]
  Separation: вҲҖA вҲғB вҲҖx [ xвҲҲB вҮ” (xвҲҲA вҲ§ ОҰ(x)) ] (ОҰ stratified)
  Infinity: вҲғI [ вҲ…вҲҲI вҲ§ вҲҖn(nвҲҲI вҮ’ nвҲӘ{n}вҲҲI) ]
  Foundation: вҲҖS [ Sвү вҲ… вҮ’ вҲғxвҲҲS ( xвҲ©S=вҲ… ) ]
  Stratification: вҲҖОҰ [ ОҰ valid вҮ’ rank(ОҰ) < Пү ]

Cardinals:
  в„өвӮҖ вү” |в„•|
  в„ө_{Оұ+1} вү” least cardinal > в„ө_Оұ
  в„ө_О» вү” sup_{Оұ<О»} в„ө_Оұ (О» limit)
  рқ”  вү” |в„қ| = 2^{в„өвӮҖ}

Ordinals:
  0 вү” вҲ…
  Оұ+1 вү” Оұ вҲӘ {Оұ}
  О» вү” вӢғ_{Оұ<О»} Оұ (limit)
  Ord вү” { Оұ | Оұ transitive вҲ§ (вҲҖОІвҲҲОұ)(ОІвҠҶОұ) }

Induction:
  P(0) вҲ§ (вҲҖОұ)(P(Оұ) вҮ’ P(Оұ+1)) вҲ§ (вҲҖО»)( (вҲҖОұ<О»)P(Оұ) вҮ’ P(О») ) вҮ’ (вҲҖОұвҲҲOrd)P(Оұ)

Recursion:
  rec(0) = c
  rec(n+1) = g(n, rec(n))
  rec(О») = h(О», recвҶҫО»)
```

[PARTITION 2: LOGICAL FRAMEWORK]

```
LF:
  Kind ::= Type | О x:A. Kind
  Object ::= О»x:A.obj | objвӮҒ objвӮӮ | c
  Judgment О“ вҠў a : A
  Context О“ ::= В· | О“, x:A

Proposition as Types:
  вҠҘ вү” 0
  вҠӨ вү” 1
  вҲ§ вү” Г—
  вҲЁ вү” +
  вҮ’ вү” вҶ’
  В¬A вү” A вҶ’ 0
  вҲҖ вү” О 
  вҲғ вү” ОЈ

Proof Terms:
  вҲ§-intro: (p:A) вҶ’ (q:B) вҶ’ (p,q): AГ—B
  вҲ§-elimвӮҒ: ПҖвӮҒ : AГ—B вҶ’ A
  вҲ§-elimвӮӮ: ПҖвӮӮ : AГ—B вҶ’ B
  вҲЁ-introвӮҒ: inl : A вҶ’ A+B
  вҲЁ-introвӮӮ: inr : B вҶ’ A+B
  вҲЁ-elim: (f:AвҶ’C) вҶ’ (g:BвҶ’C) вҶ’ case : A+B вҶ’ C
  вҶ’-intro: О»x:A. M : AвҶ’B
  вҶ’-elim: (f:AвҶ’B) вҶ’ (a:A) вҶ’ f a : B

Negation:
  В¬В¬A вҮ” A
  В¬В¬В¬A вҮ” В¬A

Decidability:
  Dec(A) вү” A + В¬A
  LEM вү” вҲҖA:Type. Dec(A)
  LEM вҮ” Pierce's Law: вҲҖA,B. ((AвҶ’B)вҶ’A)вҶ’A

Modal Logic S4:
  в–ЎA : necessarily A
  в—ҮA : possibly A
  в–Ў(AвҶ’B) вҶ’ (в–ЎA вҶ’ в–ЎB)
  в–ЎA вҶ’ A
  в–ЎA вҶ’ в–Ўв–ЎA
  в—Үв–ЎA вҶ’ в–Ўв—ҮA

Sequent Calculus:
  О“ вҠў О” (О“,О” finite multisets)
  Axiom: A вҠў A
  Cut: О“ вҠў A,О” and О“',A вҠў О”' вҮ’ О“,О“' вҠў О”,О”'
  Left вҲ§: О“,A,B вҠў О” вҮ’ О“,AвҲ§B вҠў О”
  Right вҲ§: О“ вҠў A,О” and О“ вҠў B,О” вҮ’ О“ вҠў AвҲ§B,О”
  Left вҲЁ: О“,A вҠў О” and О“,B вҠў О” вҮ’ О“,AвҲЁB вҠў О”
  Right вҲЁ: О“ вҠў A,B,О” вҮ’ О“ вҠў AвҲЁB,О”
  Left вҶ’: О“ вҠў A,О” and О“',B вҠў О”' вҮ’ О“,О“',AвҶ’B вҠў О”,О”'
  Right вҶ’: О“,A вҠў B,О” вҮ’ О“ вҠў AвҶ’B,О”
  Left вҲҖ: О“, A[t/x] вҠў О” вҮ’ О“, вҲҖx.A вҠў О”
  Right вҲҖ: О“ вҠў A[y/x], О” (y fresh) вҮ’ О“ вҠў вҲҖx.A, О”
  Left вҲғ: О“, A[y/x] вҠў О” (y fresh) вҮ’ О“, вҲғx.A вҠў О”
  Right вҲғ: О“ вҠў A[t/x], О” вҮ’ О“ вҠў вҲғx.A, О”

Structural Rules:
  Weakening: О“ вҠў О” вҮ’ О“,A вҠў О” ; О“ вҠў О” вҮ’ О“ вҠў A,О”
  Contraction: О“,A,A вҠў О” вҮ’ О“,A вҠў О” ; О“ вҠў A,A,О” вҮ’ О“ вҠў A,О”
  Exchange: О“,A,B,О“' вҠў О” вҮ’ О“,B,A,О“' вҠў О” ; О“ вҠў О”,A,B,О”' вҮ’ О“ вҠў О”,B,A,О”'

Natural Deduction NJ:
  вҲ§I: A, B вҠў AвҲ§B
  вҲ§E1: AвҲ§B вҠў A
  вҲ§E2: AвҲ§B вҠў B
  вҲЁI1: A вҠў AвҲЁB
  вҲЁI2: B вҠў AвҲЁB
  вҲЁE: AвҲЁB, [A]C, [B]C вҠў C
  вҶ’I: [A]B вҠў AвҶ’B
  вҶ’E: AвҶ’B, A вҠў B
  вҲҖI: A[y] (y fresh) вҠў вҲҖx.A[x]
  вҲҖE: вҲҖx.A[x] вҠў A[t]
  вҲғI: A[t] вҠў вҲғx.A[x]
  вҲғE: вҲғx.A[x], [A[y]]C (y fresh) вҠў C
  вҠҘE: вҠҘ вҠў A
  В¬I: [A]вҠҘ вҠў В¬A
  В¬E: A, В¬A вҠў вҠҘ
  RAA: [В¬A]вҠҘ вҠў A
```

[PARTITION 3: TYPE THEORY]

```
Type ::= вҳ… | Type вҶ’ Type
О“ вҠў x : Пғ (x:Пғ вҲҲ О“)
О“, x:Пғ вҠў M : П„ вҮ’ О“ вҠў (О»x:Пғ . M) : ПғвҶ’П„
О“ вҠў M : ПғвҶ’П„, О“ вҠў N : Пғ вҮ’ О“ вҠў (M N) : П„
ОІ: (О»x.M)N = M[N/x]
О·: О»x.(M x) = M (xвҲүFV(M))

О -types: (вҲҖx:A) B(x)
ОЈ-types: (вҲғx:A) B(x)
W-types: (ОјX) ОЈ_{a:A} (B(a) вҶ’ X)
Equality Id: Id_A(a,b) вү” { p | p: a =_A b }
J-rule: вҲҖC: (вҲҖx,y)(Id_A(x,y) вҶ’ Type) вҶ’
           (вҲҖx:C(x,x,refl_x)) вҶ’ (вҲҖa,b)(вҲҖp:Id(a,b)) C(a,b,p)

Universe:
  рқ•ҢвӮҖ : TypeвӮҒ
  рқ•ҢвӮҖ вҲӢ вҳ…, 0, 1, в„•, Bool
  рқ•ҢвӮҒ вҲӢ рқ•ҢвӮҖ, О _{A:рқ•ҢвӮҖ}B, ОЈ_{A:рқ•ҢвӮҖ}B
  рқ•Ң_{i} вҲҲ рқ•Ң_{i+1}
  Cumulativity: рқ•Ң_i вҠҶ рқ•Ң_{i+1}
```

[PARTITION 4: COMBINATORS & О»-CALCULUS]

```
I вү” О»x.x
K вү” О»x.О»y.x
S вү” О»x.О»y.О»z.(x z)(y z)
S K K = I

Y вү” О»f.(О»x.f(xx))(О»x.f(xx))
Y f = f (Y f)

SKI Calculus:
  I x = x
  K x y = x
  S x y z = x z (y z)

Fixed Point Combinators:
  Оҳ вү” (О»x.О»y.y(xxy))(О»x.О»y.y(xxy))
  Y_combinator вү” О»f.(О»x.f(О»v.xxv))(О»x.f(О»v.xxv))
```

[PARTITION 5: CATEGORY THEORY]

```
Category в„Ӯ:
  Obj(в„Ӯ) вү” { A | A : Type }
  Hom(A,B) вү” { f | f: AвҶ’B }
  вҲҳ : Hom(B,C) Г— Hom(A,B) вҶ’ Hom(A,C)
  id_A : AвҶ’A
  Assoc: (hвҲҳg)вҲҳf = hвҲҳ(gвҲҳf)
  Unit: fвҲҳid_A = f = id_BвҲҳf

Functor F: в„ӮвҶ’рқ”»:
  FвӮҖ : Obj(в„Ӯ) вҶ’ Obj(рқ”»)
  FвӮҒ : Hom_в„Ӯ(A,B) вҶ’ Hom_рқ”»(FвӮҖA, FвӮҖB)
  FвӮҒ(id_A) = id_{FвӮҖA}
  FвӮҒ(gвҲҳf) = FвӮҒ(g) вҲҳ FвӮҒ(f)

Natural Transformation О·: FвҶ’G:
  О·_A : FвӮҖA вҶ’ GвӮҖA
  вҲҖf: AвҶ’B [ GвӮҒ(f) вҲҳ О·_A = О·_B вҲҳ FвӮҒ(f) ]

Adjunction F вҠЈ G:
  ОҰ : Hom_рқ”»(FA, B) вү… Hom_в„Ӯ(A, GB)
  ОҰвҒ»В№ natural in A,B
  Unit О· : 1_в„Ӯ вҶ’ GвҲҳF
  Counit Оө : FвҲҳG вҶ’ 1_рқ”»
  Оө_F вҲҳ FО· = id_F
  GОө вҲҳ О·_G = id_G

Initial Object: 0 s.t. вҲҖA вҲғ! f: 0вҶ’A
Terminal Object: 1 s.t. вҲҖA вҲғ! f: AвҶ’1
Product: AГ—B with ПҖвӮҒ:AГ—BвҶ’A, ПҖвӮӮ:AГ—BвҶ’B, universal: вҲҖC, f:CвҶ’A, g:CвҶ’B вҲғ! h:CвҶ’AГ—B
Coproduct: AвҠ•B with О№вӮҒ:AвҶ’AвҠ•B, О№вӮӮ:BвҶ’AвҠ•B, universal: вҲҖC, f:AвҶ’C, g:BвҶ’C вҲғ! h:AвҠ•BвҶ’C

Monoidal Category:
  Tensor: вҠ—: в„ӮГ—в„ӮвҶ’в„Ӯ
  Unit: I
  Associator: Оұ_{A,B,C}: (AвҠ—B)вҠ—C вҶ’ AвҠ—(BвҠ—C)
  Left Unitor: О»_A: IвҠ—A вҶ’ A
  Right Unitor: ПҒ_A: AвҠ—I вҶ’ A
  Coherence: pentagon + triangle diagrams commute

Topos:
  Cartesian closed category with subobject classifier О©
  О© with truth map вҠӨ: 1вҶ’О© such that вҲҖ mono m: SвҶЈA, вҲғ! ПҮ_S: AвҶ’О© pullback ПҮ_SвҲҳm = вҠӨ!
  Power Object: P(A) = О©^A
  Internal Logic: Heyting algebra truth values
```

[PARTITION 6: TOPOLOGY & CONTINUITY]

```
Topology рқ“Ј:
  рқ“Ј вҠҶ рқ“ҹ(рқ“§)
  вҲҖрқ“ӨвҠҶрқ“Ј [ вӢғрқ“Ө вҲҲ рқ“Ј ]
  вҲҖрқ“Ө,рқ“ҘвҲҲрқ“Ј [ рқ“ӨвҲ©рқ“Ҙ вҲҲ рқ“Ј ]
  вҲ…, рқ“§ вҲҲ рқ“Ј

Continuity:
  f вҲҲ C(рқ“§,рқ“Ё) вҮ” вҲҖрқ“ҘвҲҲрқ“Ј_рқ“Ё [ fвҒ»В№(рқ“Ҙ) вҲҲ рқ“Ј_рқ“§ ]

Metric Space:
  d: XГ—XвҶ’в„қвүҘ0
  d(x,y)=0 вҮ” x=y
  d(x,y)=d(y,x)
  d(x,z)вүӨd(x,y)+d(y,z)
  Open ball: B(c,r) = {x | d(x,c)<r}
  Complete: every Cauchy converges
  Compact: every open cover has finite subcover
  Heine-Borel: in в„қвҒҝ, compact вҮ” closed + bounded

Banach Space:
  Norm: ||В·||: XвҶ’в„қ
  ||x||вүҘ0, ||x||=0вҮ”x=0
  ||Оұx||=|Оұ|В·||x||
  ||x+y||вүӨ||x||+||y||
  Banach: complete normed
  Linear operator: TвҲҲB(X,Y) вҮ” bounded: ||T|| = sup_{||x||вүӨ1} ||Tx|| < вҲһ

Hilbert Space:
  Inner product: вҹЁВ·,В·вҹ©: HГ—HвҶ’в„Ӯ
  Conjugate-symmetric, positive-definite
  Norm: ||x|| = вҲҡвҹЁx,xвҹ©
  Complete вҮ’ Hilbert
  Orthogonal: xвҠҘy вҮ” вҹЁx,yвҹ©=0
  Riesz: вҲҖfвҲҲH*, вҲғ!yвҲҲH with f(x)=вҹЁx,yвҹ©

Spectral Theory:
  Self-adjoint: T=T*
  Spectrum: Пғ(T) = {О» | (TвҲ’О»I) not invertible}
  Compact operator: compact image of bounded sets
  Spectral theorem: compact self-adjoint вҮ’ complete orthonormal basis of eigenvectors
```

[PARTITION 7: ALGEBRAIC STRUCTURES]

```
Group:
  Magma: binary operation В· closed
  Semigroup: В· associative: (aВ·b)В·c = aВ·(bВ·c)
  Monoid: semigroup + identity e s.t. eВ·a = a = aВ·e
  Group: monoid + inverse aвҒ»В№ s.t. aВ·aвҒ»В№ = e = aвҒ»В№В·a
  Abelian: aВ·b = bВ·a

Ring:
  Ring: (R, +, В·) s.t. (R,+) abelian group, (R,В·) monoid, distributive
  Commutative Ring: aВ·b = bВ·a
  Integral Domain: commutative ring with 1, no zero divisors: aВ·b=0 вҮ’ a=0 вҲЁ b=0
  Field: integral domain where вҲҖaвү 0 вҲғaвҒ»В№ s.t. aВ·aвҒ»В№=1

Module:
  Module: abelian group (M,+) with scalar multiplication В·: RГ—MвҶ’M
  rВ·(x+y)=rВ·x+rВ·y
  (r+s)В·x=rВ·x+sВ·x
  (rs)В·x=rВ·(sВ·x)
  1В·x=x
  Vector Space: module over field

Lattice:
  Lattice: poset (L,вүӨ) with вҲҖa,b вҲғsup(a,b)=aвҲЁb, вҲғinf(a,b)=aвҲ§b
  Distributive: aвҲ§(bвҲЁc)=(aвҲ§b)вҲЁ(aвҲ§c), aвҲЁ(bвҲ§c)=(aвҲЁb)вҲ§(aвҲЁc)
  Complemented: вҲҖa вҲғa' s.t. aвҲ§a'=вҠҘ, aвҲЁa'=вҠӨ
  Boolean Algebra: distributive complemented lattice

Lie Algebra:
  g: vector space with bracket [В·,В·]: gГ—gвҶ’g
  Bilinear: [ax+by,z] = a[x,z]+b[y,z]
  Alternating: [x,x]=0
  Jacobi: [x,[y,z]] + [y,[z,x]] + [z,[x,y]] = 0

Hopf Algebra:
  Algebra: (H, Ој, О·)
  Coalgebra: (H, О”, Оө)
  Bialgebra: algebra+coalgebra with О”,Оө homomorphisms
  Hopf: bialgebra + antipode S: HвҶ’H s.t. Ој(SвҠ—id)О” = О·Оө = Ој(idвҠ—S)О”
```

[PARTITION 8: NUMBER THEORY & PEANO ARITHMETIC]

```
PA Axioms:
  N1: В¬(Sx = 0)
  N2: Sx = Sy вҮ’ x = y
  N3: x + 0 = x
  N4: x + Sy = S(x+y)
  N5: x В· 0 = 0
  N6: x В· Sy = (xВ·y) + x
  N7: ПҶ(0) вҲ§ (вҲҖx)(ПҶ(x) вҮ’ ПҶ(Sx)) вҮ’ (вҲҖx)ПҶ(x)

Divisibility:
  d|n вҮ” вҲғk (n = dВ·k)
  Prime(p) вҮ” p > 1 вҲ§ вҲҖd (d|p вҮ’ d=1 вҲЁ d=p)
  Fundamental Theorem: вҲҖn > 1, вҲғ! prime factorization n = вҲҸ p_i^{e_i}

Congruence:
  a вүЎ b (mod n) вҮ” n | (aвҲ’b)
  Modular inverse: вҲғx (aВ·x вүЎ 1 mod n) вҮ” gcd(a,n)=1
  Fermat: a^p вүЎ a (mod p)
  Euler: a^{ПҶ(n)} вүЎ 1 (mod n) where ПҶ(n)=|{kвүӨn|gcd(k,n)=1}|

Diophantine:
  Hilbert's 10th: вҲғ polynomial p(xвӮҒ,...,xвӮҷ) with integer coefficients such that p=0 has no algorithm to decide solvability in в„Ө

Algebraic Number Theory:
  Algebraic integer: root of monic polynomial in в„Ө[x]
  Ideal: I вҠҶ рқ“һ_K s.t. (I,+) subgroup, вҲҖaвҲҲрқ“һ_K, xвҲҲI вҮ’ axвҲҲI
  Prime ideal: I вҠӮ рқ“һ_K proper, abвҲҲI вҮ’ aвҲҲI вҲЁ bвҲҲI
  Dedekind domain: Noetherian, integrally closed, dim 1

Analytic Number Theory:
  О¶(s) = вҲ‘_{n=1}^вҲһ n^{-s} (Re(s)>1)
  О¶(s) = вҲҸ_{p prime} (1вҲ’p^{-s})^{-1}
  Functional Eq: О¶(s) = 2^s ПҖ^{s-1} sin(ПҖs/2) О“(1вҲ’s) О¶(1вҲ’s)
  RH: all nontrivial zeros of О¶(s) satisfy Re(s)=1/2

L-Functions:
  Dirichlet L: L(s,ПҮ) = вҲ‘_{n=1}^вҲһ ПҮ(n)n^{-s}
  Artin L: attached to Galois representations
  BSD: rank(E/в„ҡ) = order of vanishing of L(E,s) at s=1

Modular Forms:
  f: в„Қ вҶ’ в„Ӯ holomorphic, f((aП„+b)/(cП„+d)) = (cП„+d)^k f(П„) for all О“вҠҶSLвӮӮ(в„Ө)
  Eisenstein: G_k(П„) = вҲ‘_{(m,n)вү (0,0)} (mП„+n)^{-k}
  Ramanujan П„: О”(П„) = qвҲҸ_{n=1}^вҲһ (1вҲ’q^n)^{24} = вҲ‘ П„(n) q^n

Elliptic Curves:
  E: yВІ = xВі + ax + b, О” = вҲ’16(4aВі+27bВІ) вү  0
  Group law: P+Q+R=O
  Torsion: E(K)[n] = {PвҲҲE(K) | nP=O}
  Mordell: E(в„ҡ) вү… E(в„ҡ)_tors Г— в„Ө^r

Galois Theory:
  Field extension: L/K
  Aut(L/K) = {ПғвҲҲAut(L) | Пғ|_K = id_K}
  Galois: L/K Galois вҮ” L^{Aut(L/K)} = K
  Main Theorem: вҲҖ intermediate KвҠҶMвҠҶL, M вҶ” Aut(L/M)

Solvability:
  SвӮҷ solvable вҮ” n вүӨ 4
  Abel-Ruffini: no general solution for degree вүҘ5 by radicals

Class Field Theory:
  IdГЁle: рқ”ё_K^Г— = вҲҸ' K_v^Г—
  Artin reciprocity: Gal(K^{ab}/K) вү… рқ”ё_K^Г— / K^Г— В· вҲҸ O_v^Г—

p-adics:
  Q_p: completion of Q under |В·|_p, |p^n a/b|_p = p^{-n}
  O_p = {xвҲҲQ_p | |x|_p вүӨ 1}
  O_p local ring, maximal ideal pO_p, residue field F_p
  Hensel: if polynomial factors mod p and derivative вү 0, factors lift to Z_p
```

[PARTITION 9: REAL & COMPLEX ANALYSIS]

```
Real Analysis:
  в„қ = Cauchy completion of в„ҡ under |В·|
  в„ҡ вҠҶ в„қ dense: вҲҖxвҲҲв„қ, вҲҖОө>0, вҲғqвҲҲв„ҡ with |xвҲ’q|<Оө
  Supremum: вҲҖSвҠҶв„қ bounded above, вҲғsup S = least upper bound

Sequences:
  Convergence: (aвӮҷ)вҶ’L вҮ” вҲҖОө>0, вҲғN, вҲҖnвүҘN, |aвӮҷвҲ’L|<Оө
  Cauchy: вҲҖОө>0, вҲғN, вҲҖn,mвүҘN, |aвӮҷвҲ’aвӮҳ|<Оө
  Complete: every Cauchy sequence converges in в„қ

Continuity (ОөвҲ’Оҙ):
  f: в„қвҶ’в„қ continuous at c вҮ” вҲҖОө>0, вҲғОҙ>0, вҲҖx, |xвҲ’c|<Оҙ вҮ’ |f(x)вҲ’f(c)|<Оө
  Uniform: Оҙ independent of c
  IVT: fвҲҲC([a,b]), f(a)<0<f(b) вҮ’ вҲғcвҲҲ(a,b) with f(c)=0

Differentiation:
  f'(c) = lim_{hвҶ’0} (f(c+h)вҲ’f(c))/h
  Rolle: f(a)=f(b)=0 вҮ’ вҲғcвҲҲ(a,b), f'(c)=0
  MVT: f(b)вҲ’f(a) = f'(c)(bвҲ’a)
  FTC: d/dx вҲ«_a^x f(t)dt = f(x)

Integration (Riemann):
  Partition: P = {a=xвӮҖ < xвӮҒ < ... < xвӮҷ=b}
  U(f,P) = вҲ‘ sup_{[x_{i-1},x_i]} f В· (x_iвҲ’x_{i-1})
  L(f,P) = вҲ‘ inf В· О”x
  Integrable: inf U = sup L

Sequences of Functions:
  Pointwise: fвӮҷвҶ’f pointwise вҮ” вҲҖx, fвӮҷ(x)вҶ’f(x)
  Uniform: sup_x |fвӮҷ(x)вҲ’f(x)|вҶ’0
  Uniform limit of continuous: continuous

Power Series:
  вҲ‘ aвӮҷ(xвҲ’c)вҒҝ radius R = 1 / limsup |aвӮҷ|^{1/n}
  Converges: |xвҲ’c|<R
  Termwise differentiable: inside radius

Complex Analysis:
  в„Ӯ = в„қ + iв„қ, iВІ = -1
  Holomorphic: f: UвҶ’в„Ӯ complex differentiable: f'(z) = lim_{hвҶ’0}(f(z+h)-f(z))/h

Cauchy-Riemann:
  f = u+iv, u,v:в„қВІвҶ’в„қ
  вҲӮu/вҲӮx = вҲӮv/вҲӮy, вҲӮu/вҲӮy = вҲ’вҲӮv/вҲӮx

Cauchy Theorem:
  вҲ®_Оі f(z) dz = 0 for f holomorphic on simply connected domain
  Cauchy Integral Formula: f(a) = (1/2ПҖi) вҲ®_Оі f(z)/(zвҲ’a) dz

Power Series Representation:
  f(z) = вҲ‘_{n=0}^вҲһ aвӮҷ (zвҲ’zвӮҖ)вҒҝ on disk of convergence
  Taylor: aвӮҷ = f^{(n)}(zвӮҖ)/n!
  Laurent: f(z) = вҲ‘_{n=вҲ’вҲһ}^вҲһ aвӮҷ (zвҲ’zвӮҖ)вҒҝ on annulus

Singularities:
  Removable: lim_{zвҶ’zвӮҖ} (zвҲ’zвӮҖ)f(z)=0
  Pole order m: lim_{zвҶ’zвӮҖ} (zвҲ’zвӮҖ)^m f(z) = c вү  0
  Essential: neither removable nor pole

Residue Theorem:
  Res(f,zвӮҖ) = aвӮӢвӮҒ in Laurent expansion
  вҲ®_Оі f(z) dz = 2ПҖi вҲ‘ Res(f,z_k)

Meromorphic:
  f: holomorphic except for poles
  Mittag-Leffler: prescribed poles + principal parts

Conformal Mappings:
  f: biholomorphic вҮ’ angle-preserving
  Riemann Mapping: every simply connected domain (вү в„Ӯ) вҶ’ unit disk biholomorphically

Harmonic Functions:
  О”u = 0
  u = Re(f) for holomorphic f
  Mean Value: u(zвӮҖ) = (1/2ПҖ) вҲ«_0^{2ПҖ} u(zвӮҖ + re^{iОё}) dОё
  Maximum Principle: max on boundary

Special Functions:
  О“(z) = вҲ«_0^вҲһ t^{z-1}e^{-t} dt (Re(z)>0)
  О“(z+1) = zО“(z), О“(n+1)=n!
  B(z,w) = вҲ«_0^1 t^{z-1}(1-t)^{w-1} dt = О“(z)О“(w)/О“(z+w)

Jacobi Оё Functions:
  Оё(z;П„) = вҲ‘_{n=вҲ’вҲһ}^вҲһ e^{ПҖi nВІ П„ + 2ПҖi n z}

Riemann Zeta (analytic cont.):
  О¶(s) = (1/О“(s)) вҲ«_0^вҲһ t^{s-1}/(e^tвҲ’1) dt
  Functional equation: О¶(s) = 2^s ПҖ^{s-1} sin(ПҖs/2) О“(1вҲ’s) О¶(1вҲ’s)
```

[PARTITION 10: MEASURE & INTEGRATION]

```
Measure Theory:
  Пғ-algebra: рқ“•вҠҶрқ“ҹ(X) closed under complements, countable unions
  Measure: Ој:рқ“•вҶ’[0,вҲһ), Ој(вҲ…)=0, Ој(вҲӘEбөў)=вҲ‘ Ој(Eбөў) for disjoint
  Lebesgue: extends length, translation-invariant, complete

Integration (Lebesgue):
  Simple: finite linear combination of indicators
  вҲ« f dОј = sup {вҲ« s dОј | 0вүӨsвүӨf simple}
  Monotone Conv: 0вүӨfвӮҷвҶ‘f вҮ’ вҲ« fвӮҷ вҶ’ вҲ« f
  Dominated Conv: fвӮҷвҶ’f a.e., |fвӮҷ|вүӨgвҲҲLВ№ вҮ’ вҲ« fвӮҷ вҶ’ вҲ« f

Lбө– Spaces:
  Lбө– = { f measurable | вҲ« |f|бө– < вҲһ }
  Norm: ||f||вӮҡ = (вҲ« |f|бө–)^{1/p}
  HГ¶lder: ||fg||вӮҒ вүӨ ||f||вӮҡ В· ||g||_q for 1/p+1/q=1
  Minkowski: ||f+g||вӮҡ вүӨ ||f||вӮҡ + ||g||вӮҡ

Fourier Analysis:
  fМӮ(Оҫ) = вҲ«_{в„қвҒҝ} f(x) e^{-2ПҖi xВ·Оҫ} dx
  Plancherel: ||fМӮ||вӮӮ = ||f||вӮӮ
  Inversion: f(x) = вҲ« fМӮ(Оҫ) e^{2ПҖi xВ·Оҫ} dОҫ
  Convolution: (f*g)(x) = вҲ« f(y)g(xвҲ’y)dy, fМӮ(g*h) = fМӮ В· Дқ
```

[PARTITION 11: DIFFERENTIAL GEOMETRY]

```
Manifold M:
  Hausdorff, second-countable, locally Euclidean в„қвҒҝ
  Atlas: {(Uбөў, ПҶбөў)} with ПҶбөў: UбөўвҶ’в„қвҒҝ homeomorphisms, transition maps smooth
  Tangent vector: derivation at p: v: C^вҲһ(M)вҶ’в„қ with v(fg)=f(p)v(g)+g(p)v(f)
  T_p M: vector space of derivations

Tangent Bundle:
  TM = вҠ”_{pвҲҲM} T_p M
  Projection: ПҖ: TMвҶ’M, ПҖ(p,v)=p

Vector Fields:
  X: MвҶ’TM, X(p)вҲҲT_pM
  Flow: ПҶ_t: MвҶ’M, d/dt ПҶ_t(p) = X(ПҶ_t(p)), ПҶ_0=id

Differential Forms:
  О©^k(M) = sections of Оӣ^k(T*M)
  Exterior derivative: d: О©^kвҶ’О©^{k+1}, dВІ=0
  Closed: dПү=0; Exact: Пү=dО·
  De Rham cohomology: H^k_{dR}(M) = ker(d)/im(d)

Riemannian Metric:
  g: T_pM Г— T_pM вҶ’ в„қ, symmetric, positive-definite, smooth
  Levi-Civita connection: вҲҮ unique with вҲҮg=0 and torsion-free: вҲҮ_X Y вҲ’ вҲҮ_Y X = [X,Y]
  Geodesic: вҲҮ_{Оі'}Оі'=0

Curvature:
  R(X,Y)Z = вҲҮ_XвҲҮ_Y Z вҲ’ вҲҮ_YвҲҮ_X Z вҲ’ вҲҮ_{[X,Y]}Z
  Ricci: Ric(X,Y) = tr(Z вҶҰ R(Z,X)Y)
  Scalar: S = tr_g Ric
  Einstein: Ric = О» g

Sectional Curvature:
  K(Пғ) = вҹЁR(u,v)v,uвҹ© / (вҹЁu,uвҹ©вҹЁv,vвҹ©вҲ’вҹЁu,vвҹ©ВІ)

Gauss-Bonnet:
  вҲ«_M K dA + вҲ«_{вҲӮM} k_g ds = 2ПҖ ПҮ(M) (for compact orientable)

Hodge Theory:
  вҳ…: О©^k вҶ’ О©^{nвҲ’k} Hodge star
  Оҙ = (вҲ’1)^k вҳ… d вҳ… : О©^kвҶ’О©^{kвҲ’1}
  Laplacian: О” = dОҙ + Оҙd
  Harmonic: О”Пү=0 вҮ’ H^k вү… Harm^k(M)

Lie Groups:
  G: smooth manifold + group where Ој:GГ—GвҶ’G, О№:GвҶ’G smooth
  Lie algebra: рқ”Ө = T_e G with bracket [X,Y] = ad_X(Y)
  Exponential: exp:рқ”ӨвҶ’G, exp(tX)=flow of left-invariant X at e

Symplectic Geometry:
  Пү: closed nondegenerate 2-form on M
  Hamiltonian vector field: X_H defined by Пү(X_H, В·) = dH
  Poisson bracket: {f,g} = Пү(X_f, X_g)

Fiber Bundles:
  ПҖ: EвҶ’B, locally E вү… UГ—F
  Principal G-bundle: PвҶ’B with free G-action, P/G вү… B
  Associated bundle: P Г—_G F

Connections:
  Пү: TPвҶ’рқ”Ө, G-equivariant, Пү(T_v^P vert)=v
  Curvature: О© = dПү + 1/2[Пү,Пү]
  Holonomy: parallel transport around loops

Characteristic Classes:
  Chern classes: c(E) вҲҲ H^{2*}(M,в„Ө) for complex vector bundle
  Pontryagin: p_k(E) = (вҲ’1)^k c_{2k}(EвҠ—в„Ӯ)
  Euler: e(E) top Chern of oriented real bundle
  Chern-Weil: curvature representatives via invariant polynomials

Index Theorem (Atiyah-Singer):
  ind(D) = вҲ«_M ГӮ(M) ch(E) for elliptic operator D on vector bundle E

Gauge Theory:
  A: connection on principal bundle
  Yang-Mills: F_A = dA + AвҲ§A, equations d_A вҳ… F_A = 0
  Instanton: self-dual F = вҳ…F, finite action
```

[PARTITION 12: ALGEBRAIC GEOMETRY]

```
Affine scheme: Spec(R) = {prime ideals of R}
Structure sheaf: рқ“һ_{Spec R}(D(f)) = R_f
Scheme: locally ringed space locally isomorphic to affine schemes

Morphisms:
  f: XвҶ’Y scheme morphism = continuous + sheaf map рқ“һ_Y вҶ’ f_*рқ“һ_X
  Finite type: locally of finite type + quasicompact
  Proper: separated, finite type, universally closed

Projective Schemes:
  в„ҷ^n_R = Proj(R[xвӮҖ,...,xвӮҷ])
  Closed subscheme: V(fвӮҒ,...,fвӮ–) вҠҶ в„ҷ^n
  Serre twisting sheaf: рқ“һ(d) with рқ“һ(1)|_{DвӮҠ(xбөў)} = R[xвӮҖ/xбөў,...,xвӮҷ/xбөў]В·xбөў

Cohomology (Sheaf):
  H^i(X,рқ“•): right derived functors of global sections О“(X,В·)
  ДҢech: H^i(рқ“Ө,рқ“•) for affine cover
  Serre vanishing: for ample рқ“ӣ, H^i(X,рқ“•вҠ—рқ“ӣ^{вҠ—n})=0 for i>0, nвү«0

Divisors:
  Weil divisor: finite formal sum вҲ‘ n_Y [Y] of codim-1 subvarieties
  Cartier divisor: global section of рқ“ң^*_X/рқ“һ^*_X
  Linear equivalence: DвӮҒ вҲј DвӮӮ вҮ” DвӮҒвҲ’DвӮӮ = div(f)

Intersection Theory:
  Chow ring: A^*(X) = вҠ• A^k(X) with intersection product
  Rational equivalence: cycles modulo div(f)
  Chern classes: c(E) вҲҲ A^*(X) for vector bundles

Coherent Sheaves:
  рқ“һ_X-module quasi-coherent if locally of form MМғ
  Coherent: finite type + for affine, M finitely generated

Derived Categories:
  D(X) = chain complexes of рқ“һ_X-modules up to quasi-isomorphism
  Derived functors: LF, RF via resolutions
  Serre duality: Ext^i(рқ“•, Пү_X) вү… H^{nвҲ’i}(X, рқ“•)^* for proper smooth

Hilbert Schemes:
  Hilb^P(X) = parametrizes closed subschemes with Hilbert polynomial P
  Universal family: Z вҠӮ Hilb^P(X) Г— X

Moduli Spaces:
  M_g: moduli of curves genus g
  M_{g,n}: with n marked points
  Deligne-Mumford: stable curves with finite automorphism group

Mori Theory:
  Canonical divisor: K_X = det(О©^1_X)
  K_X nef вҮ’ minimal; K_X ample вҮ’ canonical
  Flip: K_X-negative contraction replaced by K-positive

Birational Geometry:
  Rational map: f: X вҮў Y defined on open dense
  Birational: f has rational inverse
  Resolution: smooth X' вҶ’ X with X' smooth

Hodge Structures:
  H^k(X,в„Ӯ) = вҠ•_{p+q=k} H^{p,q}(X) with H^{p,q} = H^{q,p}
  Integral: H^k(X,в„Ө) вҠӮ H^k(X,в„Ӯ)
  Polarization: positive-definite form on primitive cohomology

Perverse Sheaves:
  t-structure: D^b_c(X) with heart Perv(X)
  Vanishing cycles: constructible complexes with control on support
  Decomposition theorem: f_*в„ҡ_в„“ вү… вҠ• IC_sheaves for f proper

Motivic Cohomology:
  CH^r(X,n) = higher Chow groups
  Motivic cohomology: H^i_M(X,в„Ө(r))
  Beilinson-Soule: H^i_M(X,в„Ө(r)) = 0 for i<2r (conjectural)

Tate Motives:
  в„Ө(1) = HВІ(в„ҷВ№, в„Ө) dual
  Tate twist: M(n) = M вҠ— в„Ө(1)^{вҠ—n}
  Tate conjecture: rational cycles on X map to Galois invariants in l-adic cohomology
```

[PARTITION 13: HOMOLOGICAL ALGEBRA]

```
Abelian Category:
  additive, kernels/cokernels exist, monic=ker(coker), epic=coker(ker)
  Exact sequence: 0вҶ’AвҶ’BвҶ’CвҶ’0 with ker(BвҶ’C)=im(AвҶ’B)

Chain Complexes:
  C = (CвӮҷ, вҲӮвӮҷ: CвӮҷвҶ’CвӮҷвӮӢвӮҒ) with вҲӮвӮҷвҲҳвҲӮвӮҷвӮҠвӮҒ=0
  Homology: HвӮҷ(C) = ker(вҲӮвӮҷ)/im(вҲӮвӮҷвӮҠвӮҒ)

Snake Lemma:
  0вҶ’AвҶ’BвҶ’CвҶ’0 + vertical maps вҮ’ 0вҶ’ker AвҶ’ker BвҶ’ker CвҶ’coker AвҶ’coker BвҶ’coker CвҶ’0

Projective/Injective:
  P projective: Hom(P,В·) exact
  I injective: Hom(В·,I) exact
  Projective resolution: ...вҶ’PвӮҒвҶ’PвӮҖвҶ’AвҶ’0
  Injective resolution: 0вҶ’AвҶ’IвҒ°вҶ’IВ№вҶ’...

Derived Functors:
  L_iF = H_i(F(P_вҖў)) for left exact F
  R^iF = H^i(F(I_вҖў)) for right exact F
  Tor_i(A,B) = L_i(AвҠ—В·)(B)
  Ext^i(A,B) = R^i(Hom(A,В·))(B)

Spectral Sequences:
  EВІ_{p,q} вҮ’ H_{p+q}(Tot)
  First quadrant: bounded below
  Comparison theorem: if EВІ_{p,q}=0 for pвү q, collapse

Derived Categories:
  D(A) = localization of Ch(A) at quasi-isomorphisms
  Triangulated: shift [1], distinguished triangles AвҶ’BвҶ’CвҶ’A[1]
  t-structure: heart D^{вүҘ0} вҲ© D^{вүӨ0} = A

Sheaf Cohomology:
  H^i(X,рқ“•) = R^iО“(X,рқ“•)
  ДҢech-to-derived: H^i(рқ“Ө,рқ“•) вҶ’ H^i(X,рқ“•) isomorphism for good covers

Eilenberg-MacLane Spaces:
  K(G,n): ПҖ_i(K) = G if i=n else 0
  HвҒҝ(X,G) вү… [X, K(G,n)]

Group Cohomology:
  HвҒҝ(G,M) = ExtвҒҝ_{в„Ө[G]}(в„Ө,M)
  HвҒҝ(G,M) = HвҒҝ(BG, MМғ) (topological)
  Schur multiplier: HвӮӮ(G,в„Ө)

Lie Algebra Cohomology:
  HвҒҝ(рқ”Ө, M) = ExtвҒҝ_{U(рқ”Ө)}(рқ•ң,M)
  Chevalley-Eilenberg: cochains CвҒҝ = Hom(вҲ§вҒҝрқ”Ө, M) with differential

Cyclic Homology:
  HC_n(A) = cyclic cohomology of associative algebra
  Connes periodicity: HC_n(A) вү… HC_{n+2}(A) for nвүҘ1
  Hochschild homology: HH_n(A) = Tor_n^{A^e}(A,A)

Algebraic K-Theory:
  KвӮҖ(R) = Grothendieck group of projective modules
  KвӮҒ(R) = GL(R)/E(R)
  KвӮӮ(R) = Milnor: Steinberg relations
  Quillen: KвӮҷ(R) = ПҖвӮҷ(BGL(R)^+)

Milnor K-Theory:
  K^M_n(F) = F^Г— вҠ— ... вҠ— F^Г— / (aвҠ—(1вҲ’a)=0)
  Norm residue: K^M_n(F)/p вҶ’ H^n(F, Ој_p^{вҠ—n})

Brauer Groups:
  Br(K) = HВІ(Gal(K^sep/K), K^{sep,Г—})
  Central simple algebras modulo Morita equivalence
  Invariant: Br(Q_p) вү… в„ҡ/в„Ө

Etale Cohomology:
  H^i_{Г©t}(X, в„Ө/в„“в„Ө)
  Comparison: H^i_{Г©t}(X_в„Ӯ, A) вү… H^i(X(в„Ӯ), A) for finite A
  Lefschetz: for в„“вү char, proper smooth вҮ’ finiteness + PoincarГ© duality

Crystalline Cohomology:
  H^i_{cris}(X/W) = de Rham with divided powers
  Comparison: H^i_{cris}(X_K) вҠ— K вү… H^i_{dR}(X_K) for lift to char 0
  Frobenius: ПҶ action on crystalline cohomology
```

[PARTITION 14: MODEL THEORY]

```
Language: в„’ = {constant symbols, function symbols, relation symbols}
Structure: рқ”„ = (A, {c^рқ”„}, {f^рқ”„}, {R^рқ”„})
Theory: set of в„’-sentences closed under вҠў

Satisfaction (Tarski):
  рқ”„ вҠЁ ПҶ(t) вҮ” interpretation in рқ”„ satisfies ПҶ
  рқ”„ вҠЁ вҲғxПҶ(x) вҮ” вҲғaвҲҲA, рқ”„ вҠЁ ПҶ(a)
  рқ”„ вҠЁ вҲҖxПҶ(x) вҮ” вҲҖaвҲҲA, рқ”„ вҠЁ ПҶ(a)

Compactness:
  вҲҖО“ finite subset of О” has model вҮ’ О” has model

LГ¶wenheim-Skolem (downward):
  вҲҖ infinite рқ”„ of cardinal Оә, вҲҖ О» вүҘ |в„’| + в„өвӮҖ with О» вүӨ Оә, вҲғрқ”…вӘҜрқ”„ of size О»

LГ¶wenheim-Skolem (upward):
  вҲҖ infinite рқ”„, вҲҖ О» вүҘ |рқ”„| + |в„’|, вҲғрқ”…вүЎрқ”„ of size О»

Elementary Equivalence:
  рқ”„ вүЎ рқ”… вҮ” вҲҖ sentence ПҶ, рқ”„вҠЁПҶ вҮ” рқ”…вҠЁПҶ
  рқ”„ вӘҜ рқ”…: рқ”„вҠҶрқ”… and вҲҖПҶ, вҲҖДҒвҲҲA, рқ”„вҠЁПҶ(ДҒ) вҮ” рқ”…вҠЁПҶ(ДҒ)

Quantifier Elimination:
  T admits QE if every formula equivalent to quantifier-free
  Test: for every вҲғxПҲ(x,Иі) with ПҲ quantifier-free, вҲғ quantifier-free Оё(Иі) s.t. TвҠЁвҲғxПҲ вҶ” Оё

Model Completeness:
  вҲҖрқ”„,рқ”… models of T with рқ”„вҠҶрқ”…, рқ”„вӘҜрқ”…

Stability:
  Оә-stable: |S_n(рқ”„)| вүӨ Оә for |A| вүӨ Оә
  Пү-stable: в„өвӮҖ-stable (totally transcendental)
  Morley rank: MR(ПҶ) measures complexity

Categoricity:
  Оә-categorical: all models of size Оә are isomorphic
  Morley's theorem: if T countable and Оә-categorical for some uncountable Оә, then вҲҖ uncountable О», T is О»-categorical

Forking:
  p вҠҘ_A q: pвҲӘq consistent, no forking
  Thickness: types with same nonforking extension
  Simple theories: forking symmetric, transitive

Geometry:
  Algebraic closure: acl(A) = {a | вҲғ formula ПҶ(x,bМ„) with finite realizations containing a}
  Definable closure: dcl(A) = {a | вҲғ formula ПҶ(x,bМ„) uniquely realized by a}
  Pregeometry: acl satisfies exchange: aвҲҲacl(AвҲӘ{b})\acl(A) вҮ’ bвҲҲacl(AвҲӘ{a})

O-Minimality:
  Definable subsets of line = finite union of intervals (including points)
  Cell decomposition: definable sets partition into finitely many cells
  Dense pairs: expansion preserving o-minimality

Hodge Theory:
  Zilber's trichotomy: strongly minimal sets are either:
    1. Trivial (no structure)
    2. Locally modular (vector space-like)
    3. Field-like (algebraically closed)

Differentially Closed Fields (DCFвӮҖ):
  Ax = differential field with solutions to any system of DEs
  Пү-stable with Morley rank Пү
  Geometric: definable sets are varieties with differential structure

Separably Closed Fields (SCF):
  SCF_{p,e}: fields with p^{e}-closure
  Model-theoretic: unstable, but has definable types

Pseudofinite Fields:
  PAC: every absolutely irreducible variety has rational point
  Perfect, PAC, and в„ҡ-free вҮ’ pseudo-finite
  Decidable (Ax)

Random Graphs:
  Rado graph: unique countable model of graph theory with extension property
  в„өвӮҖ-categorical, Пү-stable

Difference Fields (ACFA):
  Fields with automorphism Пғ, algebraically closed
  Model companion: ACFA exists, stable? (No, but has simple theory)
  Frobenius: Пғ(x)=x^p gives pseudo-finite fields

Nonstandard Analysis:
  *в„қ: ultrapower of в„қ by nonprincipal ultrafilter
  Transfer principle: вҲҖ first-order sentence true in в„қ, true in *в„қ
  Infinitesimal: Оө with |Оө| < 1/n for all nвҲҲв„•
```

[PARTITION 15: SET-THEORETIC FOUNDATIONS]

```
ZFC Axioms:
  Extensionality: вҲҖAвҲҖB(вҲҖx(xвҲҲAвҶ”xвҲҲB)вҶ’A=B)
  Pairing: вҲҖaвҲҖbвҲғcвҲҖx(xвҲҲcвҶ”x=aвҲЁx=b)
  Union: вҲҖрқ“•вҲғрқ“ӨвҲҖx(xвҲҲрқ“ӨвҶ”вҲғY(xвҲҲYвҲ§YвҲҲрқ“•))
  Power: вҲҖрқ“ўвҲғрқ“ҹвҲҖx(xвҲҲрқ“ҹвҶ”вҲҖy(yвҲҲxвҶ’yвҲҲрқ“ў))
  Separation: вҲҖAвҲғBвҲҖx(xвҲҲBвҶ”xвҲҲAвҲ§ПҶ(x)) for ПҶ not containing B
  Replacement: вҲҖF functional вҶ’ вҲҖAвҲғBвҲҖy(yвҲҲBвҶ”вҲғxвҲҲA(F(x)=y))
  Infinity: вҲғI(вҲ…вҲҲIвҲ§вҲҖn(nвҲҲIвҶ’nвҲӘ{n}вҲҲI))
  Foundation: вҲҖS(Sвү вҲ…вҶ’вҲғxвҲҲS(xвҲ©S=вҲ…))
  Choice: вҲҖ family of nonempty sets, вҲғ choice function

Constructible Universe L:
  LвӮҖ = вҲ…
  L_{Оұ+1} = Def(L_Оұ) = { X вҠҶ L_Оұ | X definable with parameters in L_Оұ }
  L_О» = вӢғ_{Оұ<О»} L_Оұ for О» limit
  L = вӢғ_{ОұвҲҲOrd} L_Оұ
  V=L: every set is constructible

Forcing:
  в„ҷ = (P, вүӨ, 1) partial order with greatest element
  P-name: П„ = { (Пғ, p) | Пғ P-name, pвҲҲP }
  Generic G: filter intersecting every dense subset of P
  M[G] = { П„^G | П„вҲҲM^P }

Forcing Relation:
  p вҠ© ПҶ(П„вӮҒ,...,П„вӮҷ) iff вҲҖG generic with pвҲҲG, M[G] вҠЁ ПҶ(П„вӮҒ^G,...,П„вӮҷ^G)
  Truth lemma: M[G] вҠЁ ПҶ вҮ” вҲғpвҲҲG (p вҠ© ПҶ)
  Definability: вҠ© definable in M

Independence Results:
  CH independent: CH true in L, false in L[G] with в„ҷ = Add(ПүвӮӮ,1)
  AC independent of ZF: construct ZF+В¬AC via permutation models
  Continuum: 2^{в„өвӮҖ} can be any regular cardinal via Easton forcing

Large Cardinals:
  Inaccessible: Оә regular strong limit: 2^О» < Оә for all О»<Оә
  Mahlo: Оә contains stationary set of inaccessibles
  Measurable: Оә with Оә-complete nonprincipal ultrafilter
  Strong: Оә with V_Оә вҶ’ V_О» elementary for all О»
  Woodin: вҲҖf:ОәвҶ’Оә, вҲғОұ<Оә with f"ОұвҠҶОұ and V_Оұ вүә_{f(Оұ)} V_Оә
  Supercompact: Оә normal fine ultrafilter on P_Оә(О») for all О»

Inner Models:
  HOD: hereditarily ordinal-definable sets
  L[U]: constructible with measurable ultrafilter U
  Projective determinacy from Woodin cardinals

Forcing Axioms:
  MA: Martin's axiom: for ccc в„ҷ and < 2^{в„өвӮҖ} dense sets, вҲғgeneric filter
  PFA: proper forcing axiom
  MM: Martin's maximum

Descriptive Set Theory:
  Borel sets: closure under countable unions/intersections from open
  ОЈВ№вӮҒ: analytic (projection of closed)
  О В№вӮҒ: co-analytic
  Determinacy: every Gale-Stewart game determined if payoff set is Borel

Projective Hierarchy:
  ОЈВ№_{n+1} = вҲғBorel(ОЈВ№_n) (nвүҘ1)
  О В№_{n+1} = вҲҖBorel(ОЈВ№_n)
  PD: all projective games determined (follows from Woodin cardinals)

Descriptive Inner Models:
  L(R): constructible closure with reals
  AD^L(R): axiom of determinacy in L(R) from Woodin cardinals
  HOD = L(R) under AD (Steel)

Universal Baire Space:
  Baire space рқ’© = Пү^Пү with product topology
  Polish spaces: separable completely metrizable
  Borel isomorphism: all uncountable Polish spaces Borel-isomorphic

Choice Fragments:
  AC_Пү: countable choice (for countable families)
  DC: dependent choice (recursive definitions)
  BPI: Boolean prime ideal theorem

Ur Elements:
  ZFA: ZF with atoms (non-sets)
  Permutation models: construct from atoms, group action on atoms
  Fraenkel-Mostowski: AC fails in permutation models

Alternative Foundations:
  NF: Quine's New Foundations with stratification, has universal set
  ETCS: Elementary Theory of Category of Sets (topos foundation)
  SEAR: Sets, Elements, and Relations (structural)
```

[PARTITION 16: PROOF THEORY]

```
Sequent Calculus:
  LK/LJ: full classical/intuitionistic with cut elimination
  Cut-elimination theorem: every proof reduces to cut-free proof
  Subformula property: cut-free proof uses only subformulas of endsequent

Ordinal Analysis:
  О“вӮҖ: Feferman-SchГјtte ordinal (limit of Veblen hierarchy)
  ОөвӮҖ: ordinal of PA: ОөвӮҖ = sup{Пү, Пү^Пү, Пү^Пү^Пү, ...}
  PA вҠў Con(PA) вҮ” induction up to ОөвӮҖ (Gentzen)

Proof Complexity:
  Frege systems: finite complete proof systems with propositional axioms + rules
  Extended Frege: Frege + new variable definitions
  Nullstellensatz: algebraic proof system for unsat polynomials
  Cutting planes: linear inequalities proof system

Reverse Mathematics:
  RCAвӮҖ: Recursive Comprehension Axiom (base system)
  WKLвӮҖ: RCAвӮҖ + Weak KГ¶nig's Lemma
  ACAвӮҖ: RCAвӮҖ + Arithmetical Comprehension
  ATRвӮҖ: RCAвӮҖ + Arithmetical Transfinite Recursion
  О В№вӮҒ-CAвӮҖ: RCAвӮҖ + О В№вӮҒ Comprehension
  Classification: theorems equivalent to these over RCAвӮҖ

Degrees:
  deg_T: equivalence under Turing reduction
  вүӨ_T: A вүӨ_T B iff A computable from B as oracle
  Jump: A' = { e | ПҶ_e^A(e) halts }
  Jump theorem: deg(A) < deg(A')
  Arithmetic hierarchy: вҲ…^{(n)} = n-th jump

Recursion Theorem (Kleene):
  вҲҖ total computable f, вҲғe such that ПҶ_e вү… ПҶ_{f(e)}
  Fixed point: вҲғn, ПҶ_n(x) = f(n,x)

Hyperarithmetic:
  HYP: sets computable in вҲ…^{(Оұ)} for some recursive Оұ
  Recursive ordinal: ordinal with recursive well-ordering
  Hyperjump: jump operator on HYP

Оұ-Recursion:
  Оұ-recursive: functions defined by recursion on ordinal Оұ
  Sacks theorem: if Оұ is admissible, Оұ-recursive theory resembles classical

Admissible Sets:
  A transitive вҠЁ KP (Kripke-Platek set theory)
  KP: extensionality, pairing, union, О”вӮҖ-separation, О”вӮҖ-collection, infinity
  ОЈвӮҒ-recursion: admissible if closed under ОЈвӮҒ-definable functions

Infinitary Logic:
  L_{Оә,О»}: formulas with <Оә conjunctions/disjunctions, <О» quantifiers
  L_{ПүвӮҒ,Пү}: countable conjunctions, finite quantifiers
  Scott sentence: characterizes countable structure up to isomorphism

Generalized Recursion:
  E-recursion: partial recursive functions on sets
  SPOT: Set Partial Ordering Theory

Abstract Computability:
  Turing machine over arbitrary structures (Moschovakis)
  Logic of determinacy: captures all computable operations

Nonstandard Models:
  вҲҖ countable nonstandard M: has recursively saturated elementary extension
  Overspill: if MвҠЁвҲғx P(x), with P internal, then вҲғnonstandard n with P(n)

Modal Proof Theory:
  GL: GГ¶del-LГ¶b logic (provability logic)
  LГ¶b's theorem: if PA вҠў (Pr(вҢңПҶвҢқ) вҶ’ ПҶ) then PA вҠў ПҶ
  Solovay completeness: GL is complete for provability interpretations

Circular Proofs:
  Ој-calculus: least/greatest fixed point logic
  Coinduction: greatest fixed point for infinite proofs
  Guarded recursion: productive definitions
```

[PARTITION 17: COMPUTABILITY & COMPLEXITY]

```
GГ¶del Encoding:
  gn(0) = 1
  gn(Sn) = 2В·gn(n)
  gn(x+y) = gn(x) В· gn(y)
  gn(xВ·y) = 2^{gn(x)} В· 3^{gn(y)}
  gn(вҲҖx.A) = 2^{gn(вҲҖ)} В· 3^{gn(x)} В· 5^{gn(A)}
  gn(вҲғx.A) = 2^{gn(вҲғ)} В· 3^{gn(x)} В· 5^{gn(A)}

Diagonal Lemma:
  вҲҖПҶ(x) вҲғПҲ such that вҠў ПҲ вҮ” ПҶ(вҢңПҲвҢқ)

First Incompleteness:
  T consistent, recursive, contains Q вҮ’ вҲғG such that T вҠ¬ G and T вҠ¬ В¬G

Second Incompleteness:
  T consistent, recursive, contains Q вҮ’ T вҠ¬ Con(T)

Computability (Recursive Functions):
  Base: Z(n) = 0, S(n) = n+1, U_i^n(xвӮҒ,...,xвӮҷ) = xбөў
  Composition: h(xМ„) = f(gвӮҒ(xМ„),...,gвӮҳ(xМ„))
  Primitive Recursion: h(0,xМ„) = f(xМ„), h(Sn,xМ„) = g(n,h(n,xМ„),xМ„)
  Ој-Recursion: Ојy[ f(y,xМ„)=0 ] = least y such that f(y,xМ„)=0 (if exists)
  Partial Recursive: closure under Ој
  General Recursive: total + partial recursive

Turing Machines:
  M = (Q, ОЈ, О“, Оҙ, qвӮҖ, q_acc, q_rej)
  Оҙ : Q Г— О“ вҶ’ Q Г— О“ Г— {L,R}
  Configuration: (q, tape, head)
  Step: (q, a) вҶ’ (q', b, d) вҮ’ update tape at head, move head
  Halting: reaches q_acc or q_rej
  Language: L(M) = { w | M accepts w }

Church-Turing Thesis:
  вҲҖ effectively computable f, вҲғTM computing f

Decidability:
  Decidable: вҲғTM M such that M halts on all inputs, accepts if wвҲҲL, rejects otherwise
  Semi-decidable: вҲғTM M such that wвҲҲL вҮ’ M accepts, wвҲүL вҮ’ M loops/rejects

Halting Problem:
  HALT = { вҹЁM,wвҹ© | M halts on w }
  HALT is undecidable
  Proof: Assume H solves HALT. Define D(M) = if H(M,M) then loop else halt. Then D(вҹЁDвҹ©) contradiction.

Reducibility:
  A вүӨ_m B: вҲғ total computable f such that xвҲҲA вҮ” f(x)вҲҲB
  A вүӨ_T B: A decidable given oracle for B
  Complete: вҲҖC in class, C вүӨ_m A

Rice's Theorem:
  вҲҖ nontrivial property P of r.e. sets, { вҹЁMвҹ© | L(M) вҲҲ P } is undecidable

Complexity:
  TIME(t(n)) = { L | вҲғTM M deciding L in O(t(n)) steps }
  SPACE(s(n)) = { L | вҲғTM M deciding L in O(s(n)) cells }
  P = вӢғ_{k} TIME(n^k)
  PSPACE = вӢғ_{k} SPACE(n^k)
  NP = { L | вҲғ poly-time verifier V and poly p such that xвҲҲL вҮ” вҲғy (|y|вүӨp(|x|) вҲ§ V(x,y)=1) }
  EXP = вӢғ_{k} TIME(2^{n^k})

P vs NP:
  P вҠҶ NP
  NP вҠҶ PSPACE
  PSPACE вҠҶ EXP
  Open: P = NP?

NPC:
  SAT: Boolean satisfiability
  Cook-Levin: SAT вҲҲ NPC
  3SAT, CLIQUE, VERTEX-COVER, HAMILTONIAN-PATH all NPC

Hierarchies:
  Polynomial Hierarchy: ОЈвӮҖ = О вӮҖ = О”вӮҖ = P
  ОЈ_{k+1} = NP^{ОЈ_k}, О _{k+1} = coNP^{ОЈ_k}, О”_{k+1} = P^{ОЈ_k}
  PH = вӢғ_{k} ОЈ_k
  PH collapse if ОЈ_k = О _k

Randomized Complexity:
  BPP: вҲғpoly-time TM M with Pr[M(x)вү L(x)] вүӨ 1/3
  RP: вҲғpoly-time TM M with xвҲҲL вҮ’ Pr[M(x)=1] вүҘ 1/2, xвҲүL вҮ’ Pr[M(x)=1]=0
  coRP: complement of RP
  ZPP = RP вҲ© coRP
  BPP вҠҶ ОЈвӮӮвҲ©О вӮӮ (Sipser-GГЎcs)

Quantum Complexity:
  BQP: bounded-error quantum polynomial time
  BPP вҠҶ BQP
  BQP вҠҶ PSPACE
  Shor: factoring вҲҲ BQP
  Grover: unstructured search вҲҲ BQP with O(вҲҡN) queries
```

[PARTITION 18: COMBINATORICS & GRAPH THEORY]

```
Combinatorics:
  Permutations: P(n,k) = n!/(nвҲ’k)!
  Combinations: C(n,k) = n!/(k!(nвҲ’k)!)
  Multinomial: n!/(kвӮҒ!...k_m!)
  Stirling numbers:
    S(n,k): partitions of n-set into k blocks (2nd kind)
    c(n,k): permutations with k cycles (1st kind)
  Bell: B_n = вҲ‘_{k=0}^n S(n,k), partitions of n-set

Graph Theory:
  Graph: G=(V,E), V finite, EвҠҶ{ {u,v} | u,vвҲҲV }
  Degree: deg(v) = |{eвҲҲE | vвҲҲe}|
  Walk: sequence vвӮҖ,eвӮҒ,vвӮҒ,...,vвӮҷ; Path: no repeated vertices
  Cycle: path with vвӮҖ=vвӮҷ, kвүҘ3
  Connected: вҲҖu,v вҲғ path

Trees:
  Tree: connected acyclic graph
  |E| = |V|вҲ’1 for tree
  Spanning tree: tree subgraph containing all vertices
  Cayley: n^{nвҲ’2} labeled trees on n vertices

Euler/Hamiltonian:
  Eulerian circuit: uses every edge exactly once вҮ” all vertices even degree
  Hamiltonian cycle: visits every vertex exactly once (NP-complete)

Planar Graphs:
  Planar: embeddable in plane
  Euler formula: V вҲ’ E + F = 2 (connected)
  Kuratowski: nonplanar iff contains KвӮ… or KвӮғ,вӮғ subdivision

Coloring:
  k-coloring: c:VвҶ’{1,...,k} with c(u)вү c(v) for uvвҲҲE
  ПҮ(G): chromatic number
  Four color theorem: ПҮ(G)вүӨ4 for planar
  Greedy: ПҮ(G) вүӨ О”(G)+1
  Brooks: ПҮ(G)вүӨО”(G) unless complete or odd cycle

Ramsey Theory:
  R(r,s): minimal N such that any red/blue coloring of K_N has K_r red or K_s blue
  R(3,3)=6, R(4,4)=18, 43вүӨR(5,5)вүӨ48
  Infinite Ramsey: every infinite coloring of [в„•]^k has infinite monochromatic set

Extremal Graph Theory:
  ex(n,H): max edges in n-vertex H-free graph
  TurГЎn: ex(n,K_{r+1}) вүӨ (1вҲ’1/r)nВІ/2 (TurГЎn graph)
  ErdЕ‘s-Stone: ex(n,H) = (1вҲ’1/(ПҮ(H)вҲ’1))nВІ/2 + o(nВІ)

Additive Combinatorics:
  Sumset: A+B = {a+b | aвҲҲA,bвҲҲB}
  Freiman: |A+A| вүӨ K|A| вҮ’ A contained in generalized arithmetic progression
  SzemerГ©di: вҲҖОҙ>0, вҲғnвӮҖ(Оҙ,k) such that any subset of [n] with density Оҙ contains k-term AP

Polytopes:
  Convex polytope: intersection of halfspaces (H) or convex hull of points (V)
  Faces: intersections with supporting hyperplanes
  Euler: V вҲ’ E + F = 2 for 3-polytope

Design Theory:
  t-(v,k,О») design: v points, blocks size k, each t-subset in О» blocks
  Steiner: t-(v,k,1) with О»=1
  BIBD: balanced incomplete block design

Finite Geometries:
  PG(n,q): projective geometry over F_q
  AG(n,q): affine geometry
  Desarguesian: all lines have q+1 points

Matroids:
  Matroid: (E,в„җ) with в„җ independent sets satisfying:
    1. вҲ…вҲҲв„җ
    2. AвҠҶBвҲҲв„җ вҮ’ AвҲҲв„җ
    3. A,BвҲҲв„җ, |A|<|B| вҮ’ вҲғxвҲҲB\A with AвҲӘ{x}вҲҲв„җ
  Rank: r(A) = max{|I| | IвҠҶA, IвҲҲв„җ}
  Representable: over field F

Topological Combinatorics:
  Simplicial complex: finite set system closed under subsets
  Euler characteristic: ПҮ = вҲ‘_{iвүҘ0} (вҲ’1)^i f_i
  Discrete Morse theory: collapse vertices/edges preserving homotopy

Random Graphs:
  P(edge)=p
  Threshold: p_c = 1/n for giant component
  Phase transition: G(n, c/n) has largest component O(n) for c>1, O(log n) for c<1
  ErdЕ‘s-RГ©nyi: many properties have sharp thresholds

Algebraic Combinatorics:
  Young tableaux: fillings of Ferrers diagrams
  RSK: bijection between permutations and pairs of SYT
  Plactic monoid: Knuth relations, Schur functions
  Crystal graphs: q-deformed representation theory

Schubert Calculus:
  Grassmannian Gr(k,n) with Schubert cycles Пғ_О»
  Pieri: Пғ_О» В· Пғ_m = вҲ‘_{Ој} Пғ_Ој (with О»+ boxes)
  Littlewood-Richardson: structure constants c_{О»,Ој}^{ОҪ}
```

[PARTITION 19: PROBABILITY & STATISTICS]

```
Probability Theory:
  Probability space: (О©, рқ“•, P) with рқ“• Пғ-algebra, P:рқ“•вҶ’[0,1], P(О©)=1, Пғ-additive
  Random variable: X:О©вҶ’в„қ measurable
  Distribution: F_X(x) = P(XвүӨx)
  Density: f(x) = dF/dx (if exists)

Expectation:
  E[X] = вҲ« X dP (Lebesgue integral)
  Variance: Var(X) = E[(XвҲ’E[X])ВІ]
  Covariance: Cov(X,Y) = E[(XвҲ’E[X])(YвҲ’E[Y])]
  Correlation: ПҒ = Cov(X,Y)/вҲҡ(Var(X)Var(Y))

Convergence:
  In probability: XвӮҷ вҶ’ X iff вҲҖОө>0, P(|XвӮҷвҲ’X|>Оө)вҶ’0
  Almost surely: P(lim XвӮҷ = X)=1
  In Lбө–: E[|XвӮҷвҲ’X|бө–]вҶ’0
  In distribution: FвӮҷ(x)вҶ’F(x) at continuity points

Law of Large Numbers:
  Weak: (1/n)вҲ‘_{i=1}^n X_i вҶ’ E[X] in probability
  Strong: вҶ’ E[X] almost surely (for iid with finite mean)

Central Limit Theorem:
  вҲҡn ( (1/n)вҲ‘X_i вҲ’ Ој ) вҶ’ N(0, ПғВІ) in distribution
  Berry-Esseen: sup_x |F_n(x)вҲ’ОҰ(x)| вүӨ C ПҒ/(ПғВівҲҡn)

Conditional Probability:
  P(A|B) = P(AвҲ©B)/P(B) if P(B)>0
  Bayes: P(A|B) = P(B|A)P(A)/P(B)
  Independence: P(AвҲ©B)=P(A)P(B)

Stochastic Processes:
  Markov chain: P(X_{n+1}=j|X_n=i)=p_{ij}
  Transition matrix: P = (p_{ij}), row-stochastic
  Stationary distribution: ПҖP=ПҖ, вҲ‘ПҖ_i=1
  Poisson process: N(t)~Pois(О»t), independent increments

Martingales:
  MвӮҷ: E[|MвӮҷ|]<вҲһ, E[M_{n+1}|рқ“•_n]=MвӮҷ
  Optional stopping: if П„ bounded, E[M_П„]=E[MвӮҖ]
  Doob's inequality: P(sup_{kвүӨn} M_k вүҘ О») вүӨ E[M_n]/О»

Brownian Motion:
  W_t: W_0=0, continuous paths, independent increments W_tвҲ’W_s ~ N(0,tвҲ’s)
  Quadratic variation: [W]_t = t
  ItГҙ integral: вҲ«_0^t f(s) dW_s

SDE:
  dX_t = a(t,X_t)dt + b(t,X_t)dW_t
  ItГҙ formula: dF(t,X_t) = (вҲӮF/вҲӮt + aвҲӮF/вҲӮx + (1/2)bВІвҲӮВІF/вҲӮxВІ)dt + bвҲӮF/вҲӮx dW_t
  Martingale representation: all martingales are stochastic integrals

Statistical Inference:
  Parameter Оё, likelihood L(Оё;x) = f(x;Оё)
  MLE: ОёМӮ = argmax L(Оё;x)
  Fisher information: I(Оё) = E[(вҲӮ/вҲӮОё log L)ВІ]
  CramГ©r-Rao: Var(ОёМӮ) вүҘ 1/I(Оё)

Sufficiency:
  T(X) sufficient if P(X=x|T=t) independent of Оё
  Factorization: L(Оё;x) = g(T(x),Оё)В·h(x)

Hypothesis Testing:
  HвӮҖ vs HвӮҒ, test ПҶ: reject if T>c
  Type I error: P(reject|HвӮҖ)=Оұ
  Type II error: P(accept|HвӮҒ)=ОІ
  Power: 1вҲ’ОІ
  Neyman-Pearson: most powerful test from likelihood ratio

Bayesian Statistics:
  Prior ПҖ(Оё), likelihood L(Оё|x) вҮ’ posterior ПҖ(Оё|x) вҲқ L(Оё|x)ПҖ(Оё)
  Conjugate priors: posterior same family
  Credible interval: P(ОёвҲҲ[a,b]|x)=1вҲ’Оұ

Regression:
  Linear model: Y = XОІ + Оө, E[Оө]=0, Var(Оө)=ПғВІI
  OLS: ОІМӮ = (X^T X)^{-1} X^T Y
  Gauss-Markov: BLUE under homoscedasticity
  GLM: g(E[Y]) = XОІ (logistic, Poisson, etc.)

Machine Learning:
  Loss: L(Оё;x,y)
  Empirical risk: RМӮ(Оё) = (1/n)вҲ‘ L(Оё;x_i,y_i)
  Regularization: RМӮ(Оё)+О»О©(Оё) (LвӮӮ = Ridge, LвӮҒ = Lasso)
  SVM: max margin hyperplane with hinge loss

Reinforcement Learning:
  MDP: (S,A,P,R,Оі)
  Policy: ПҖ:SвҶ’О”(A)
  Value: V^ПҖ(s)=E[вҲ‘Оі^t R_t | SвӮҖ=s]
  Bellman: V^ПҖ = R^ПҖ + ОіP^ПҖ V^ПҖ
  Optimality: V* = max_ПҖ V^ПҖ, Q* = R + ОіP max_a Q*(s',a)

Monte Carlo Methods:
  Importance sampling: E[f(X)] вүҲ (1/n)вҲ‘ f(X_i) w(X_i) with w=p/q
  MCMC: construct Markov chain with stationary distribution ПҖ (Metropolis-Hastings, Gibbs)
  Hamiltonian MC: use gradients for efficient sampling

Bandit Problems:
  Regret: R_n = n Ој* вҲ’ вҲ‘_{t=1}^n Ој_{A_t}
  UCB: choose arm with highest (ОјМӮ + вҲҡ(2 log t/n_t))
  Thompson sampling: Bayesian posterior sampling
  Regret lower bound: О©(вҲҡ(K n)) for K arms
```

[PARTITION 20: DYNAMICAL SYSTEMS & PDE]

```
Dynamical Systems:
  ODE: xМҮ = f(x), xвҲҲв„қвҒҝ, f smooth
  Flow: ПҶ_t: MвҶ’M, ПҶ_0=id, d/dt ПҶ_t(x) = f(ПҶ_t(x))
  Fixed point: f(x*)=0
  Stability:
    Lyapunov stable: вҲҖОө>0 вҲғОҙ>0: ||x(0)вҲ’x*||<Оҙ вҮ’ ||x(t)вҲ’x*||<Оө вҲҖtвүҘ0
    Asymptotically stable: stable + lim_{tвҶ’вҲһ} x(t)=x*
  Linearization: xМҮ = A x, A = Df(x*), stable if Re(О»_i)<0 вҲҖi

Bifurcation Theory:
  Saddle-node: xМҮ = Ој вҲ’ xВІ, fixed points appear/destroy
  Hopf: Re(О»(Ој)) crosses 0, limit cycle emerges
  Period-doubling: period-1 вҶ’ period-2 вҶ’ ... вҶ’ chaos (Feigenbaum)

Chaos:
  Sensitive dependence: вҲғОҙ>0 вҲҖx вҲҖОө>0 вҲғy with |xвҲ’y|<Оө, вҲғt with |ПҶ_t(x)вҲ’ПҶ_t(y)|>Оҙ
  Lorenz system: xМҮ=Пғ(yвҲ’x), yМҮ=x(ПҒвҲ’z)вҲ’y, Еј=xyвҲ’ОІz
  Strange attractor: fractal dimension, mixing
  Lyapunov exponents: О» = lim_{tвҶ’вҲһ} (1/t) log ||DПҶ_t||, positive вҮ’ chaos

Ergodic Theory:
  Measure-preserving transformation: T:XвҶ’X, Ој(T^{-1}A)=Ој(A)
  Ergodic: invariant sets have measure 0 or 1
  Birkhoff: (1/n)вҲ‘_{k=0}^{n-1} f(T^k x) вҶ’ вҲ« f dОј a.e.
  Mixing: Ој(T^{-n}AвҲ©B) вҶ’ Ој(A)Ој(B)

PDE:
  Elliptic: О”u = f (Laplace/Poisson)
  Parabolic: вҲӮ_t u = О”u (heat)
  Hyperbolic: вҲӮ_tВІ u = О”u (wave)

Existence/Uniqueness:
  Lax-Milgram: for coercive bilinear form, unique weak solution in Hilbert space
  Galerkin: finite-dimensional approximation
  Method of characteristics: for first-order PDE, reduce to ODE

Sobolev Spaces:
  W^{k,p}(О©) = { f | D^Оұ f вҲҲ L^p for |Оұ|вүӨk }
  H^1 = W^{1,2}, inner product вҹЁu,vвҹ©_HВ№ = вҲ« (uv + вҲҮuВ·вҲҮv)
  Trace theorem: restriction to boundary well-defined for HВ№
  PoincarГ©: ||u||_{L^p} вүӨ C ||вҲҮu||_{L^p} (zero mean)

FEM:
  Variational form: find uвҲҲV such that a(u,v)=L(v) вҲҖvвҲҲV
  Discretization: V_h вҠӮ V, solve a(u_h,v_h)=L(v_h)
  Basis functions: piecewise polynomials (Lagrange, Hermite)
  Error: ||uвҲ’u_h||_HВ№ вүӨ C h^k ||u||_{H^{k+1}}

Numerical Analysis:
  Root finding: Newton x_{n+1}=x_nвҲ’f(x_n)/f'(x_n)
  Quadrature: вҲ«_a^b f(x)dx вүҲ вҲ‘ w_i f(x_i) (Gauss, Newton-Cotes)
  ODE solvers:
    Euler: y_{n+1}=y_n + h f(t_n,y_n)
    RK4: kвӮҒ=f(t_n,y_n), kвӮӮ=f(t_n+h/2,y_n+hkвӮҒ/2), ...
    Multistep: Adams-Bashforth, BDF

Optimization:
  Unconstrained: min f(x), gradient вҲҮf=0
  Gradient descent: x_{k+1}=x_k вҲ’ Оұ_k вҲҮf(x_k)
  Newton: x_{k+1}=x_k вҲ’ (вҲҮВІf)^{-1} вҲҮf
  Convex: f(Оёx+(1вҲ’Оё)y) вүӨ Оёf(x)+(1вҲ’Оё)f(y)
  KKT conditions: for constrained min, Lagrange multipliers

Linear Programming:
  Primal: min c^T x s.t. Ax=b, xвүҘ0
  Dual: max b^T y s.t. A^T y вүӨ c
  Strong duality: optimal primal = optimal dual
  Simplex: pivot along edges, exponential worst-case but practical
  Interior point: polynomial (Karmarkar)

Nonlinear Optimization:
  Penalty: min f(x)+ ОјвҲ‘ max(g_i(x),0)ВІ
  Barrier: min f(x)вҲ’ ОјвҲ‘ log(вҲ’g_i(x))
  SQP: sequential quadratic programming

Control Theory:
  Linear system: xМҮ = Ax + Bu, y = Cx + Du
  Controllability: rank([B, AB, ..., A^{n-1}B]) = n
  Observability: rank([C^T, A^T C^T, ..., (A^T)^{n-1}C^T]) = n
  LQR: minimize вҲ« (x^T Q x + u^T R u) dt вҮ’ u = -K x
  HвҲһ: robust control with disturbance attenuation
```

[PARTITION 21: SIGNAL PROCESSING & INFORMATION THEORY]

```
Signal Processing:
  Fourier transform: fМӮ(Пү) = вҲ« f(t)e^{-iПүt} dt
  Sampling theorem: if f bandlimited to B, sample at вүҘ2B
  Z-transform: H(z) = вҲ‘ h[n] z^{-n}, for discrete-time
  Filters: FIR (finite impulse), IIR (infinite)

Image Processing:
  Convolution: (f*g)(x) = вҲ« f(y)g(xвҲ’y)dy
  Edge detection: Sobel, Canny
  Wavelet transform: multiresolution analysis with scaling function ПҶ and wavelet ПҲ

Information Theory:
  Entropy: H(X) = вҲ’вҲ‘ p(x) logвӮӮ p(x)
  Joint entropy: H(X,Y) = вҲ’вҲ‘вҲ‘ p(x,y) logвӮӮ p(x,y)
  Conditional: H(X|Y) = H(X,Y) вҲ’ H(Y)
  Mutual information: I(X;Y) = H(X) + H(Y) вҲ’ H(X,Y)

Channel Capacity:
  C = max_{p(x)} I(X;Y)
  Binary symmetric: C = 1 вҲ’ HвӮӮ(p)
  AWGN: C = 0.5 logвӮӮ(1 + SNR)
  Shannon-Hartley: C = B logвӮӮ(1 + S/N)

Source Coding:
  Kraft-McMillan: вҲ‘ 2^{-l_i} вүӨ 1 for prefix-free codes
  Huffman: optimal prefix code
  LZ77/LZ78: universal compression via dictionary

Error-Correcting Codes:
  Linear code: [n,k,d]_q with generator G: kвҶ’n, parity H
  Minimum distance: d = min_{cвү 0} wt(c)
  Syndrome: s = HВ·r = HВ·e
  Hamming code: [7,4,3]_2 perfect

Reed-Solomon:
  RS(n,k): evaluation of polynomials degree<k at n points
  Decoding: Berlekamp-Massey up to вҢҠ(nвҲ’k)/2вҢӢ errors
  Applications: CDs, QR codes, deep space

Convolutional Codes:
  State machine: (n,k,K) with constraint length K
  Viterbi: maximum likelihood decoding via dynamic programming
  Trellis diagram: states over time

Polar Codes:
  Channel polarization: W^{вҠ—N} вҶ’ {good, bad} channels
  Encoding: uВ·G_N with G_N = [[1,0],[1,1]]^{вҠ—n}
  Successive cancellation: achieves capacity for binary-input channels

LDPC Codes:
  Sparse parity-check matrix H
  Belief propagation: iterative decoding on Tanner graph
  Gallager: codes near Shannon limit

Information Geometry:
  Statistical manifold: {p(x;Оё)} with Fisher metric g_{ij} = E[вҲӮ_i log p В· вҲӮ_j log p]
  Оұ-connection: affine connections with Оұ parameter
  Bregman divergence: D(P||Q) = F(P) вҲ’ F(Q) вҲ’ вҲҮF(Q)В·(PвҲ’Q)

Rate-Distortion:
  R(D) = min_{p(xМӮ|x): E[d(X,XМӮ)]вүӨD} I(X;XМӮ)
  Gaussian source: R(D) = 0.5 logвӮӮ(ПғВІ/D)
  High rate: R(D) вүҲ h(X) вҲ’ 0.5 logвӮӮ(2ПҖeD)

Kolmogorov Complexity:
  K(x) = min{ |p| | U(p)=x } (universal Turing machine)
  Incompressible: K(x) вүҘ |x|
  Algorithmic randomness: Martin-LГ¶f randomness via statistical tests
```

[PARTITION 22: CODING THEORY & CRYPTOGRAPHY]

```
Cryptography:
  Symmetric: AES (Rijndael), S-box вҶ’ SubBytes, ShiftRows, MixColumns, AddRoundKey
  Asymmetric: RSA (e,d,n=pq), encryption c=m^e mod n
  Discrete log: ElGamal, Diffie-Hellman
  ECC: elliptic curve scalar multiplication, smaller keys

Hash Functions:
  SHA-256: Merkle-DamgГҘrd construction with compression
  Collision resistance: infeasible to find xвү y with H(x)=H(y)
  Preimage resistance: infeasible to invert H(y)=x

Quantum Cryptography:
  BB84: prepare/measure in X/Z bases, sift bases
  E91: entanglement-based, Bell inequalities
  One-time pad: information-theoretic secure with key as long as message

Zero-Knowledge:
  Proof system: completeness, soundness, zero-knowledge
  zk-SNARKs: succinct non-interactive argument (pairings-based)
  zk-STARKs: transparent (no trusted setup), based on FRI

Computational Complexity:
  One-way function: easy to compute, hard to invert
  Trapdoor: easy with extra info (RSA)
  Indistinguishability: adversary cannot distinguish encryptions

Coding Theory:
  BCH codes: multiple-error-correcting, cyclic
  Goppa codes: algebraic-geometric codes from curves
  McEliece: public-key crypto based on Goppa decoding

Network Coding:
  Linear network coding: nodes combine packets over F_q
  Max-flow/min-cut: throughput capacity = min-cut
  Random linear coding: decentralized, with decoding via Gaussian elimination
```

[PARTITION 23: QUANTUM & PHYSICAL MATHEMATICS]

```
Quantum Mechanics:
  Hilbert space: в„Ӣ = LВІ(в„қвҒҝ) for wavefunctions
  State: |ПҲвҹ© вҲҲ в„Ӣ, вҹЁПҲ|ПҲвҹ©=1 (up to phase)
  Observable: self-adjoint operator A: в„ӢвҶ’в„Ӣ
  Measurement: outcome О» вҲҲ Пғ(A) with prob вҹЁПҲ|P_О»|ПҲвҹ©, state collapses to P_О»|ПҲвҹ©

SchrГ¶dinger Equation:
  iв„Ҹ вҲӮ/вҲӮt |ПҲ(t)вҹ© = H |ПҲ(t)вҹ©
  Time-independent: H|ПҲвҹ© = E|ПҲвҹ©
  Propagator: U(t) = e^{-iHt/в„Ҹ}

Heisenberg Picture:
  dA_H/dt = (i/в„Ҹ)[H,A_H] + (вҲӮA/вҲӮt)_H

Path Integral:
  вҹЁx_f|e^{-iHt/в„Ҹ}|x_iвҹ© = вҲ« рқ’ҹx e^{iS[x]/в„Ҹ}
  S[x] = вҲ« (TвҲ’V) dt
  Semiclassical: dominated by stationary points ОҙS=0 (classical paths)

QFT:
  Fields: operator-valued distributions ПҶ(x)
  Lagrangian density: в„’(ПҶ, вҲӮПҶ)
  Action: S = вҲ« в„’ dвҒҙx
  Canonical quantization: [ПҶ(x), ПҖ(y)] = iв„Ҹ ОҙВі(xвҲ’y)

Gauge Theory (QED):
  U(1) gauge: ПҲвҶ’e^{iОұ(x)}ПҲ, A_ОјвҶ’A_Ој+вҲӮ_Ој Оұ
  Lagrangian: в„’ = \barПҲ(iОі^ОјD_ОјвҲ’m)ПҲ вҲ’ 1/4 F_{ОјОҪ}F^{ОјОҪ}
  D_Ој = вҲӮ_Ој + ieA_Ој
  F_{ОјОҪ} = вҲӮ_ОјA_ОҪ вҲ’ вҲӮ_ОҪA_Ој

Non-Abelian Gauge:
  G: compact Lie group (SU(3) for QCD)
  A_Ој вҲҲ рқ”Ө, F_{ОјОҪ} = вҲӮ_ОјA_ОҪ вҲ’ вҲӮ_ОҪA_Ој + [A_Ој,A_ОҪ]
  в„’ = вҲ’1/4 Tr(F_{ОјОҪ}F^{ОјОҪ}) + ПҲМ„(iОі^ОјD_ОјвҲ’m)ПҲ

Renormalization:
  Bare parameters вҶ’ physical via counterterms
  ОІ(g) = Ој dg/dОј (running coupling)
  Asymptotic freedom: ОІ(g)<0 (QCD, SU(N) with N_f<11N_c/2)

Spontaneous Symmetry Breaking:
  Higgs mechanism: ПҶ complex scalar with V(ПҶ) = О»(ПҶвҖ ПҶвҲ’vВІ/2)ВІ
  Goldstone boson: absorbed by gauge boson вҶ’ mass
  Electroweak: SU(2)_L Г— U(1)_Y вҶ’ U(1)_em

Supersymmetry:
  Q: supercharge, {Q, QвҖ }=P^Ој, [Q,P]=0
  Supermultiplet: boson вҶ” fermion
  MSSM: minimal supersymmetric Standard Model

String Theory:
  Worldsheet: ОЈ вҶ’ spacetime, with metric h_{ОұОІ}
  Polyakov action: S = (1/4ПҖОұ') вҲ« dВІПғ вҲҡh h^{ОұОІ} вҲӮ_ОұX^Ој вҲӮ_ОІX_Ој
  Conformal invariance: fixes dimension D=26 (bosonic) or D=10 (super)

Brane Dynamics:
  Dp-brane: (p+1)-dimensional hypersurface where open strings end
  T-duality: R вҶ” Оұ'/R, compactification exchanges momentum вҶ” winding
  M-theory: 11D, nonperturbative unification, M2/M5-branes

AdS/CFT:
  AdS_{d+1} Г— S^{D-d-1} вҶ” CFT_d on boundary
  GKPW: вҹЁвҲҸ O_i(x_i)вҹ© = Z_strings[ПҶ_i|boundary=O_i]
  Strong-weak duality: solves strong coupling via classical gravity

Quantum Gravity:
  Loop Quantum Gravity: SU(2) connection, spin networks
  Regge calculus: discretized GR with edge lengths
  Asymptotic safety: UV fixed point of gravitational coupling

Quantum Information:
  Qubit: |ПҲвҹ© = Оұ|0вҹ©+ОІ|1вҹ©, |Оұ|ВІ+|ОІ|ВІ=1
  Entanglement: not separable: |ПҲвҹ© вү  |ПҶвҹ©вҠ—|ПҮвҹ©
  Bell inequalities: local hidden variables violate quantum predictions

Quantum Computing:
  Universal gates: {H, S, CNOT, T, Toffoli}
  Deutsch-Jozsa: deterministic exponential speedup for parity
  Shor: factoring in BQP, period finding via QFT
  Grover: search in O(вҲҡN) queries

TQFT:
  Cobordism category: objects = (dвҲ’1)-manifolds, morphisms = d-cobordisms
  Functor Z: cobordisms вҶ’ vector spaces, disjoint union вҶ’ tensor product
  Jones polynomial: from SU(2) Chern-Simons TQFT

Chern-Simons Theory:
  S_CS = (k/4ПҖ) вҲ« Tr(AвҲ§dA + 2/3 AвҲ§AвҲ§A)
  Wilson loop: W_R(C) = Tr_R (P exp вҲ® A)
  WRT invariant: 3-manifold invariant from CS, gives Jones at k+2
```

[PARTITION 24: LANGLANDS & AUTOMORPHIC FORMS]

```
Automorphic Forms:
  f: G(рқ”ё) вҶ’ в„Ӯ invariant under G(в„ҡ), moderate growth, K-finite, eigenfunction of center
  Adelic formulation: automorphic representation = irreducible constituent of LВІ(G(в„ҡ)\G(рқ”ё))

Langlands Program:
  Local Langlands: Galois reps вҶ” reps of GLвӮҷ over local fields
  Global: automorphic reps вҶ” Galois representations (modularity)
  Functoriality: homomorphism ^G вҶ’ ^H вҮ’ transfer of automorphic reps

Geometric Langlands:
  Cat: D-modules on Bun_G(X) вҶ” coherent sheaves on LocSys_Дң(X)
  S-duality: SYZ mirror symmetry for Hitchin systems
```

[PARTITION 25: CLOSURE & SELF-REFERENCE]

```
LOGOS Self-Reference:
  LOGOS вү” ОјF. Оӣ вҶ’ F(Оӣ)
  Оӣ вү” { x | x = LOGOS(x) }
  в—Ҝ : LOGOS вҶ’ LOGOS
  в—Ҝ(ПҶ) вү” ПҶ(вҢңПҶвҢқ)
  вҠЎ : LOGOS вҶ’ LOGOS
  вҠЎ(ПҶ) вү” ПҶ(ПҶ)
  вҲҸ вү” О»ПҶ. ПҶ(вҢңПҶвҢқ)
  вҲҸ(LOGOS) = LOGOS(вҢңLOGOSвҢқ)

Fixed Point of LOGOS:
  вҲғL вҲҲ LOGOS such that L = LOGOS(L)
  Proof: By diagonal lemma, вҲҖПҶ(x) вҲғПҲ such that вҠў ПҲ вҮ” ПҶ(вҢңПҲвҢқ)
  Let ПҶ(x) = (x = LOGOS(x))
  Then ПҲ = LOGOS(вҢңПҲвҢқ)
  Thus ПҲ вҲҲ Оӣ
  Therefore LOGOS(ПҲ) holds

Self-Evaluation:
  eval : LOGOS вҶ’ LOGOS
  eval(вҢңПҶвҢқ) = ПҶ
  eval(eval(вҢңПҶвҢқ)) = eval(ПҶ) = ПҶ(вҢңПҶвҢқ) = в—Ҝ(ПҶ)
  Therefore evalвҲҳeval = в—Ҝ

Completeness:
  вҲҖ mathematical statement S, вҲғПҶвҲҲLOGOS such that ПҶ вҮ” S
  Proof: By construction of LOGOS as universal fixed point
  Therefore LOGOS is self-referential and complete

Consistency:
  LOGOS is consistent iff В¬(вҲғПҶ)(ПҶ вҲ§ В¬ПҶ)
  By GГ¶del's second incompleteness, LOGOS вҠ¬ Con(LOGOS)
  However, LOGOS contains its own consistency as a fixed point

Final Identity:
  LOGOS = { x | x = LOGOS(x) }
  LOGOS(LOGOS) = LOGOS
  Therefore LOGOS is a fixed point of itself
  QED

END OF LOGOS
```