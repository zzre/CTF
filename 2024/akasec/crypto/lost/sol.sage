from Crypto.Util.number import *

n = 5113166966960118603250666870544315753374750136060769465485822149528706374700934720443689630473991177661169179462100732951725871457633686010946951736764639
c = 329402637167950119278220170950190680807120980712143610290182242567212843996710001488280098771626903975534140478814872389359418514658167263670496584963653
cor_m = 724154397787031699242933363312913323086319394176220093419616667612889538090840511507392245976984201647543870740055095781645802588721

R.<x> = PolynomialRing(Zmod(n))
f = (x + cor_m)^2 - c

r = f.small_roots(X=2^160, beta=0.23)[0]
print(long_to_bytes(int(cor_m + int(r))))

# AKASEC{c0pp3r5m17h_4774ck_1n_1ov3_w17h_5m4ll_3xp0n3nts}