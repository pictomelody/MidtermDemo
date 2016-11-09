\version "2.16.0"  % necessary for upgrading to future LilyPond versions.
\header{  title = "testSheet-Horizon.ly"  subtitle = "pictoMelody"  }{
  <<
    \new Staff
      \relative c'
      {
        \key ees
        \major
        \clef "treble"
        \time 4/4
          b4 a4 b2 b2 
          f2 
          b2 b4 a4 b2 
          b4 c4 b4 c4 
          e4 f4 d4 c4 d2 
          b2 
          b4 c4 b4 a4 b2 
          b2 b2 b2 
          g2 
          d4 e4 b4 a4 b2 
          b2 c4 d4 
          a2 
          d4 c4 d2 b4 c4 
          d2 b4 c4 
          b4 c4 b4 a4 b2 
          b4 a4 b2 b2 b2 
          b4 a4 b2 d4 c4 d2 
          e2 
          b4 c4 b2 
          b4 c4 b4 c4 
          a2 
          c2 b4 c4 
          d2 
          b4 a4 b2 b2 
          b4 c4 e4 f4 
          f4 g4 d4 c4 d2 
          d4 c4 d2 b2 f2 
          b4 c4 f4 e4 f2 
          e4 d4 e2 a2 g2 
          b4 a4 b2 f4 e4 f2 
          a4 b4 f2 b2 
          b4 a4 b2 c4 b4 c2 
              }
    \new Staff
      {
        \key ees
        \major
        \clef "bass"
        \time 4/4
          <a c e>2
          <c e g>2
          <a c e>2
          <c e g>2
          <a c e>2
          <c e g>2
          <a c e>2
          <c e g>2
          <a c e>2
          <c e g>2
          <a c e>2
          <c e g>2
          <a c e>2
          <c e g>2
          <a c e>2
          <c e g>2
          <e g b>2
          <a c e>2
          <e g b>2
          <f a c>2
          <e g b>2
          <a c e>2
          <e g b>2
          <f a c>2
          <e g b>2
          <a c e>2
          <e g b>2
          <f a c>2
          <e g b>2
          <a c e>2
          <e g b>2
          <f a c>2
          <g b d>2
          <c e g>2
          <g b d>2
          <a c e>2
          <g b d>2
          <c e g>2
          <g b d>2
          <a c e>2
          <g b d>2
          <c e g>2
          <g b d>2
          <a c e>2
          <g b d>2
          <c e g>2
          <g b d>2
          <a c e>2
          <b d f>2
          <e g b>2
          <g b d>2
          <f a c>2
          <b d f>2
          <e g b>2
          <g b d>2
          <f a c>2
          <b d f>2
          <e g b>2
          <g b d>2
          <f a c>2
          <b d f>2
          <e g b>2
          <g b d>2
          <f a c>2
    } >>
}