\version "2.16.0"  % necessary for upgrading to future LilyPond versions.
\header{  title = "testSheet-Horizon.ly"  subtitle = "pictoMelody"  }{
  <<
    \new Staff
      {
        \key e
        \major
        \clef "treble"
        \time 4/4
    b' a' a' b' b' 
          b' b' b' g' 
          d' b' g' a' 
          f' b' c' a' 
          g' b' b' f' 
          g' b' b' d' 
          b' b' b' b' 
          g' b' b' b' 
          b' b' b' b' 
          g' e' b' b' 
          e' a' a' b' 
          b' b' b' b' 
          b' g' g' b' 
          b' f' d' b' 
          b' b' a' b' 
          b' d' b'     }
    \new Staff
      {
        \key e
        \major
        \clef "bass"
        \time 4/4
          <f a c>
          <d f a>
          <f a c>
          <d f a>
          <f a c>
          <d f a>
          <f a c>
          <d f a>
          <f a c>
          <d f a>
          <f a c>
          <d f a>
          <f a c>
          <d f a>
          <f a c>
          <d f a>
          <e g b>
          <a c e>
          <c e g>
          <b d f>
          <e g b>
          <a c e>
          <c e g>
          <b d f>
          <e g b>
          <a c e>
          <c e g>
          <b d f>
          <e g b>
          <a c e>
          <c e g>
          <b d f>
          <f a c>
          <c e g>
          <g b d>
          <c e g>
          <f a c>
          <c e g>
          <g b d>
          <c e g>
          <f a c>
          <c e g>
          <g b d>
          <c e g>
          <f a c>
          <c e g>
          <g b d>
          <c e g>
          <g b d>
          <f a c>
          <b d f>
          <e g b>
          <g b d>
          <f a c>
          <b d f>
          <e g b>
          <g b d>
          <f a c>
          <b d f>
          <e g b>
          <g b d>
          <f a c>
          <b d f>
          <e g b>
    } >>
}