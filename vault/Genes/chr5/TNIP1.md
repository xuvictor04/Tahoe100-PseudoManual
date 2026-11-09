---
symbol: "TNIP1"
type: "gene"
col: 7037
ensembl_id: "ENSG00000145901"
name: "TNFAIP3 interacting protein 1"
location: "5q33.1"
module: 14
arm: "+"
pooled_cpm: 251.14
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 14
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# TNIP1

*TNFAIP3 interacting protein 1* — 5q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.03× (z +16.3, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.318× (z -25.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFAIP2]] (+0.67, fdr 1e-05), [[NFKBIA]] (+0.64, fdr 3e-05), [[CSF1]] (+0.64, fdr 2e-05); moves opposite to [[FAM20B]] (-0.47, fdr 5e-04), [[VKORC1L1]] (-0.44, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[CXCL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7037.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.03×** | +16.3 | 0e+00 | 49/49 (HOP62, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.50×** | +8.7 | 9e-16 | 29/48 (HOP62, Panc 03.27, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +8.1 | 7e-14 | 30/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.88×** | +7.4 | 2e-11 | 28/38 (HOP62, HS-578T, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.84×** | +7.1 | 1e-10 | 42/48 (HEC-1-A, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.21×** | +5.9 | 3e-07 | 23/48 (Panc 03.27, BT-474, …) | top dose only | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +5.6 | 2e-06 | 0/50 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.24×** | +4.7 | 2e-04 | 25/48 (BT-474, NCI-H1792, …) | rises with dose | composition shift |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.24×** | +4.4 | 7e-04 | 27/48 (HEC-1-A, LoVo, …) | inconsistent across doses | position effect removed |
| [[Minodronic acid (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.002 | 29/48 (NCI-H460, A-172, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change | 1.20× | +4.0 | 0.003 | 23/48 (BT-474, NCI-H1792, …) | rises with dose |  |
| [[Cyclosporin A (drug)]] 5 µM |  | 1.18× | +3.8 | 0.008 | 19/48 (LoVo, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.16× | +3.3 | 0.036 | 18/48 (BT-474, NCI-H1792, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.064 | 13/47 (H4, A-172, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Cyclosporin A (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.064 | 10/48 (A549, LoVo, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7037.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.318×** | -25.6 | 0e+00 | 48/48 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.416×** | -19.6 | 0e+00 | 48/48 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.417×** | -19.6 | 0e+00 | 48/48 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.568×** | -12.7 | 1e-34 | 43/48 (HT-29, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.555×** | -12.7 | 1e-34 | 40/47 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.572×** | -12.0 | 4e-31 | 34/44 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.638×** | -10.1 | 7e-22 | 45/48 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.668×** | -8.9 | 5e-17 | 34/49 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.679×** | -8.7 | 3e-16 | 41/48 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.768×** | -8.3 | 4e-15 | 30/49 (A549, HT-29, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.718×** | -7.4 | 7e-12 | 39/48 (AsPC-1, HOP62, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.550×** | -7.0 | 1e-10 | 37/49 (SK-MEL-2, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.757×** | -6.1 | 4e-08 | 32/48 (SW1417, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.835× | -5.7 | 4e-07 | 24/48 (RKO, J82, …) | top dose only | low cells (technical?) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.790×** | -5.3 | 5e-06 | 33/49 (HepG2/C3A, AsPC-1, …) | inconsistent across doses |  |
| [[Fumaric acid (drug)]] 0.5 µM |  | **0.823×** | -4.3 | 6e-04 | 20/48 (SNU-423, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.833× | -4.1 | 0.002 | 21/48 (SNU-423, HS-578T, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.836× | -4.0 | 0.002 | 21/49 (HT-29, SNU-423, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.725×** | -3.8 | 0.005 | 25/48 (AsPC-1, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.889× | -3.7 | 0.005 | 6/48 (C-33 A, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Afatinib (drug)]] 0.5 µM |  | 0.886× | -3.5 | 0.010 | 3/49 (NCI-H2347, HS-578T, …) | two highest doses | noisy plate (z scaled) |
| [[Riluzole hydrochloride (drug)]] 0.05 µM |  | 0.854× | -3.5 | 0.010 | 11/48 (PANC-1, BT-474, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.865× | -3.3 | 0.028 | 13/48 (HS-578T, SNU-423, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7037. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 383 | 8 (6 ⚠) | 8 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.9× (z +17.7) | [[Panobinostat (drug)]] 5 µM 0.187× (z -22.2) |
| [[A-172 (line)]] | wt | 481 | 5 (2 ⚠) | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.51× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.239× (z -19.1) |
| [[A498 (line)]] | wt | 358 | 4 (3 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +12.5) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.95× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.306× (z -16.8) |
| [[BT-474 (line)]] | alt | 122 | 10 (8 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +16.7) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 12.4× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -10.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 294 | 4 (1 ⚠) | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.50× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.377× (z -14.9) |
| [[AsPC-1 (line)]] | alt | 326 | 3 (2 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.9) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.50× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.217× (z -20.2) |
| [[CFPAC-1 (line)]] | alt | 520 | 3 (2 ⚠) | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.69× (z +14.0) | [[Panobinostat (drug)]] 5 µM 0.385× (z -14.6) |
| [[SNU-423 (line)]] | alt | 415 | 4 (3 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +16.0) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.40× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.248× (z -16.9) |
| [[PANC-1 (line)]] | alt | 203 | 4 (2 ⚠) | 5 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.70× (z +13.5) | [[Panobinostat (drug)]] 5 µM 0.314× (z -16.2) |
| [[HS-578T (line)]] | alt | 414 | 4 (1 ⚠) | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.55× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.200× (z -19.7) |
| [[HT-29 (line)]] | alt | 325 | 1 | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.80× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.215× (z -18.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.254× (z -17.1) |
| [[LoVo (line)]] | wt | 230 | 3 (2 ⚠) | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.16× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.313× (z -17.6) |
| [[NCI-H1573 (line)]] | alt | 264 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.86× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -18.2) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.215× (z -16.8) |
| [[Panc 03.27 (line)]] | alt | 367 | 5 (3 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +19.0) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.74× (z +16.9) | [[Auranofin (drug)]] 5 µM 0.450× (z -12.0) |
| [[A549 (line)]] | wt | 569 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -24.3) |
| [[H4 (line)]] | wt | 296 | 2 | 5 | [[TAK-901 (drug)]] 5 µM 8.23× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.256× (z -15.0) |
| [[J82 (line)]] | alt | 270 | 3 (2 ⚠) | 4 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.58× (z +13.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.65× (z +13.5) | [[Panobinostat (drug)]] 5 µM 0.306× (z -17.6) |
| [[KATO III (line)]] | alt | 126 | 4 (4 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.4) ⚠ cell-cycle shift, explains ~85% of this change | [[Panobinostat (drug)]] 5 µM 0.279× (z -16.3) |
| [[NCI-H2347 (line)]] | alt | 264 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.10× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.403× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.447× (z -10.9) |
| [[RKO (line)]] | wt | 147 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -13.7) |
| [[Hs 766T (line)]] | wt | 301 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.95× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.261× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 198 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.03× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.349× (z -13.9) |
| [[RPMI-7951 (line)]] | alt | 239 | 4 (1 ⚠) | 2 | [[TAK-901 (drug)]] 5 µM 12.8× (z +15.2) | [[Panobinostat (drug)]] 0.5 µM 0.443× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 210 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.320× (z -14.2) |
| [[hTERT-HPNE (line)]] | wt | 224 | 3 (1 ⚠) | 2 | [[TAK-901 (drug)]] 5 µM 7.39× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.389× (z -11.0) |
| [[LS 180 (line)]] | wt | 169 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 4.72× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.283× (z -16.5) |
| [[NCI-H1792 (line)]] | alt | 275 | 3 (3 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 2.72× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change | [[Panobinostat (drug)]] 5 µM 0.428× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 114 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -17.0) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.256× (z -16.2) |
| [[SW 900 (line)]] | alt | 175 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 6.05× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.308× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 211 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 4.60× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.268× (z -17.5) |
| [[NCI-H460 (line)]] | wt | 269 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 5.88× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.248× (z -16.0) |
| [[SW1417 (line)]] | alt | 207 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 3.33× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.400× (z -13.8) |
| [[C32 (line)]] | wt | 97.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.297× (z -12.5) |
| [[SW480 (line)]] | alt | 116 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.307× (z -16.8) |
| [[A-427 (line)]] | wt | 91.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.319× (z -12.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.471× (z -8.5) |
| [[C-33 A (line)]] | alt | 77.4 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.312× (z -9.3) |
| [[COLO 205 (line)]] | alt | 138 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -10.1) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.364× (z -9.4) |
| [[HCT15 (line)]] | alt | 152 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -10.4) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.365× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 158 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.86× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.468× (z -9.3) |
| [[SHP-77 (line)]] | alt | 82.2 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.352× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 193 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.3) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[SNU-1 (line)]] | wt | 139 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.402× (z -8.5) |
| [[SW 1271 (line)]] | alt | 294 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -11.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 294 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 292 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 393 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 124 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7037), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFAIP2]] | +0.67 | +0.55 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NFKBIA]] | +0.64 | +0.46 / +0.65 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 565 |
| [[CSF1]] | +0.64 | +0.48 / +0.61 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[STAT5A]] | +0.64 | +0.46 / +0.65 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NINJ1]] | +0.62 | +0.57 / +0.60 | both halves | 9e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ICAM1]] | +0.61 | +0.62 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CX3CL1]] | +0.61 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[BCL3]] | +0.61 | +0.46 / +0.62 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 427 |
| [[IRF1]] | +0.61 | +0.47 / +0.60 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[EFNA1]] | +0.60 | +0.44 / +0.63 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ZC3H12A]] | +0.60 | +0.55 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[IRF2]] | +0.59 | +0.35 / +0.63 | both halves | 1e-04 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM20B]] | -0.47 | -0.24 / -0.48 | both halves | 5e-04 |  |
| [[VKORC1L1]] | -0.44 | -0.42 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL3]] | B | CXCL3 activity raises TNIP1's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 1.89× lower at baseline in the lines without CXCL3 | 0.001 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[NEURL3]] | B | NEURL3 activity raises TNIP1's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 2.12× lower at baseline in the lines without NEURL3 | 0.005 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[IL15]] | B | IL15 activity raises TNIP1's level | lines that do not express IL15 (10) vs lines expressing it (40) | 1.87× lower at baseline in the lines without IL15 | 0.006 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[LINC02605]] | B | LINC02605 activity raises TNIP1's level | lines that do not express LINC02605 (15) vs lines expressing it (35) | 1.78× lower at baseline in the lines without LINC02605 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000285744, FAR2, ENSG00000285517 |
| [[CSF3]] | B | CSF3 activity raises TNIP1's level | lines that do not express CSF3 (27) vs lines expressing it (23) | 1.77× lower at baseline in the lines without CSF3 | 0.020 | ⚠ within organs, on part of the lines; also absent: CCBE1, LOX, RRAD |
| [[TNFAIP2]] | B | TNFAIP2 activity raises TNIP1's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.75× lower at baseline in the lines without TNFAIP2 | 0.030 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[CXCL3]] | B | CXCL3 activity strengthens TNIP1's drug response | lines that do not express CXCL3 (14) vs lines expressing it (35) | the lines without CXCL3 respond 0.65× as strongly (z diff +1.81); rises at some drug-doses, falls at others (40% from rises): Harringtonine 5 µM: 0.88x vs 1.60x (z diff +5.3); Dinaciclib 5 µM: 0.78x vs 0.53x (z diff +3.9); Dinaciclib 0.5 µM: 0.82x vs 0.62x (z diff +2.9) | 0.046 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[CXCL1]] | B | CXCL1 activity raises TNIP1's level | lines that do not express CXCL1 (17) vs lines expressing it (33) | 1.45× lower at baseline in the lines without CXCL1 | 0.048 | ⚠ within organs, on part of the lines; also absent: CCL20, CDCP1, C15orf48 |
| [[HLA-F]] | B | HLA-F activity raises TNIP1's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 1.38× lower at baseline in the lines without HLA-F | 0.055 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[ZC3H12A]] | B | ZC3H12A activity raises TNIP1's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 2.50× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[CXCL1]] | B | CXCL1 activity strengthens TNIP1's drug response | lines that do not express CXCL1 (17) vs lines expressing it (32) | the lines without CXCL1 respond 0.68× as strongly (z diff +1.34); rises at some drug-doses, falls at others (29% from rises): Dinaciclib 5 µM: 0.73x vs 0.53x (z diff +3.7); Harringtonine 5 µM: 1.04x vs 1.54x (z diff +3.5); Dinaciclib 0.5 µM: 0.78x vs 0.61x (z diff +3.0) | 0.081 | ⚠ within organs, on part of the lines; also absent: CCL20, CDCP1, C15orf48; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[IL15]] | B | IL15 activity strengthens TNIP1's drug response | lines that do not express IL15 (10) vs lines expressing it (39) | the lines without IL15 respond 0.63× as strongly (z diff +1.86); rises at some drug-doses, falls at others (47% from rises): Harringtonine 5 µM: 0.77x vs 1.55x (z diff +6.3); Dinaciclib 5 µM: 0.72x vs 0.56x (z diff +3.1); Topotecan (hydrochloride) 5 µM: 0.74x vs 0.54x (z diff +3.0) | 0.081 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.689). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.7, 4.9); signed map (43.6, 7.4). **Vector** length 119, 40.3% of its response variance represented; |z| ≥ 3 in 1,459 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.51 to 17).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +8.0 | +8.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.3 | +8.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.9 | +16.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | -0.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +5.7 | -8.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.9 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +7.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.3 | -12.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.0 | -7.4 |
|  | [[EX229 (drug)]] 5 µM |  | -6.0 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.3 | -3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.9 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | TNFAIP3 interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.1 — chr5:151,029,945-151,093,577 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NAF1, KIAA0113, ABIN-1, VAN |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 2 pathways, smallest: Ovarian tumor domain proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15025](https://www.uniprot.org/uniprotkb/Q15025) (TNFAIP3-interacting protein 1):

> Inhibits NF-kappa-B activation and TNF-induced NF-kappa-B-dependent gene expression by regulating TAX1BP1 and A20/TNFAIP3-mediated deubiquitination of IKBKG; proposed to link A20/TNFAIP3 to ubiquitinated IKBKG. Involved in regulation of EGF-induced ERK1/ERK2 signaling pathway; blocks MAPK3/MAPK1 nuclear translocation and MAPK1-dependent transcription. Increases cell surface CD4(T4) antigen expression. Involved in the anti-inflammatory response of macrophages and positively regulates TLR-induced …

**Summary**, from NCBI Gene [10318](https://www.ncbi.nlm.nih.gov/gene/10318):

> This gene encodes an A20-binding protein which plays a role in autoimmunity and tissue homeostasis through the regulation of nuclear factor kappa-B activation. Mutations in this gene have been associated with psoriatic arthritis, rheumatoid arthritis, and systemic lupus erythematosus. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:16903](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16903) · Entrez [10318](https://www.ncbi.nlm.nih.gov/gene/10318) · UniProt [Q15025](https://www.uniprot.org/uniprotkb/Q15025) · Ensembl [ENSG00000145901](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145901)

## Data

Gene col 7037: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7037); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7037, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7037]; `tensor/DDL_lfc|DDL_z.npy` [7037]; `embed/gene_vectors.npy` [7037]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7037 or target_col == 7037). Every well: [[TNIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
