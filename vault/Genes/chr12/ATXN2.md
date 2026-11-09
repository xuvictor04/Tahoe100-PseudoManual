---
symbol: "ATXN2"
type: "gene"
col: 12924
ensembl_id: "ENSG00000204842"
name: "ataxin 2"
location: "12q24.12"
module: 74
arm: "+"
pooled_cpm: 249.39
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# ATXN2

*ataxin 2* — 12q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.59× (z +14.7, q 0e+00, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.418× (z -27.6, q 0e+00, down in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.681× (z -12.1, q 9e-32, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIP5K1A]] (+0.61, fdr 1e-05), [[YAF2]] (+0.61, fdr 1e-05), [[YY1]] (+0.58, fdr 1e-05); moves opposite to [[HIF1AN]] (-0.55, fdr 2e-05), [[GPN1]] (-0.49, fdr 3e-05), [[GCOM1]] (-0.48, fdr 1e-04).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FOXA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12924.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +14.7 | 0e+00 | 37/48 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +12.9 | 8e-36 | 30/48 (Hs 766T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +11.7 | 2e-29 | 40/48 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +10.6 | 7e-24 | 32/48 (LoVo, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +8.7 | 6e-16 | 30/48 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.27×** | +7.4 | 2e-11 | 28/48 (AsPC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.60×** | +6.8 | 8e-10 | 33/49 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.55×** | +6.4 | 1e-08 | 29/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.21×** | +5.7 | 8e-07 | 23/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +5.2 | 1e-05 | 17/49 (C32, CFPAC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.5 | 3e-04 | 22/48 (C32, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.1 | 0.002 | 16/47 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.13× | +3.8 | 0.007 | 19/48 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.13× | +3.7 | 0.010 | 4/49 (J82, H4, …) | inconsistent across doses |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.017 | 17/48 (MIA PaCa-2, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.11× | +3.2 | 0.039 | 2/47 (NCI-H460, AN3 CA) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12924.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.418×** | -27.6 | 0e+00 | 49/49 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.443×** | -24.8 | 0e+00 | 42/44 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.453×** | -23.2 | 0e+00 | 45/45 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.681×** | -12.1 | 9e-32 | 42/48 (A549, PANC-1, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.731×** | -9.9 | 3e-21 | 34/48 (BT-474, A-427, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.733×** | -9.4 | 3e-19 | 36/47 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -7.6 | 3e-12 | 24/48 (AsPC-1, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.800×** | -7.1 | 1e-10 | 30/48 (J82, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.843× | -5.4 | 4e-06 | 23/48 (A549, SW1417, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.702×** | -5.1 | 2e-05 | 32/47 (NCI-H1792, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.840× | -5.1 | 2e-05 | 21/47 (SNU-1, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.868× | -4.5 | 3e-04 | 18/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.788×** | -4.4 | 5e-04 | 29/48 (SK-MEL-2, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.872× | -4.2 | 0.001 | 18/48 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.765×** | -3.9 | 0.004 | 18/48 (A549, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.928× | -3.3 | 0.029 | 3/48 (A549, NCI-H2030, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.796×** | -3.3 | 0.029 | 15/48 (SW1417, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.903× | -3.2 | 0.037 | 6/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.935× | -3.0 | 0.074 | 1/48 (HS-578T) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12924. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 178 | 6 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.78× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.550× (z -12.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 312 | 1 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.576× (z -11.0) |
| [[HOP62 (line)]] | alt | 200 | 4 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.494× (z -13.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 230 | 3 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.504× (z -11.5) |
| [[A549 (line)]] | wt | 292 | 1 | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.64× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.515× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 308 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.439× (z -15.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 195 | 2 (2 ⚠) | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.511× (z -10.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 186 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +14.6) | — |
| [[HEC-1-A (line)]] | alt | 294 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -19.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 248 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.464× (z -11.0) |
| [[LS 180 (line)]] | wt | 189 | 3 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +11.8) | [[Panobinostat (drug)]] 0.5 µM 0.550× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 349 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +12.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.287× (z -18.5) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 247 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.442× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.556× (z -9.9) |
| [[SW1417 (line)]] | alt | 283 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.545× (z -10.3) |
| [[Hs 766T (line)]] | wt | 163 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.509× (z -9.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 306 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.59× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -22.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 242 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -23.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 348 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -23.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 429 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.623× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 273 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -22.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 330 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.562× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 291 | 1 | 4 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.70× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -32.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.608× (z -8.8) |
| [[SNU-423 (line)]] | alt | 247 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.79× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -17.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 280 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.464× (z -10.9) |
| [[BT-474 (line)]] | alt | 287 | 0 | 4 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.153× (z -13.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.482× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 133 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.8) | — |
| [[HS-578T (line)]] | alt | 181 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.86× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.474× (z -12.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 144 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -14.8) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 421 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 265 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.73× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.579× (z -8.5) |
| [[SW48 (line)]] | wt | 233 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.514× (z -8.6) |
| [[A-172 (line)]] | wt | 218 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -19.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 313 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -20.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 185 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.482× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 231 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 231 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -15.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 187 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.564× (z -9.2) |
| [[RKO (line)]] | wt | 287 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -30.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 224 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.564× (z -9.6) |
| [[SNU-1 (line)]] | wt | 266 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -21.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 256 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -10.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 118 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +13.0) | — |
| [[RPMI-7951 (line)]] | alt | 185 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.393× (z -11.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 322 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -13.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 228 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.486× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 210 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +11.5) | — |
| [[NCI-H2122 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 322 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12924), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIP5K1A]] | +0.61 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[YAF2]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[YY1]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[KIF9-AS1]] | +0.58 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[DNMT3A]] | +0.56 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[ATAD2B]] | +0.56 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[RAB11FIP3]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[NR2F1]] | +0.56 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[BRD3]] | +0.55 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[NCOA1]] | +0.55 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[PCNX1]] | +0.54 | +0.58 / +0.40 | both halves | 4e-05 |  |
| [[FAM193A]] | +0.54 | +0.38 / +0.56 | both halves | 7e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIF1AN]] | -0.55 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[GPN1]] | -0.49 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[GCOM1]] | -0.48 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[LINC03009]] | -0.48 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[DLST]] | -0.47 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[AARS2]] | -0.47 | -0.49 / -0.37 | both halves | 9e-05 |  |
| [[API5]] | -0.46 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[FCHSD1]] | -0.46 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[ECHS1]] | -0.46 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[CYB5R4]] | -0.46 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[RTF2]] | -0.45 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[PLXNB3]] | -0.45 | -0.37 / -0.43 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FOXA2]] | B | FOXA2 activity lowers ATXN2's level | lines that do not express FOXA2 (28) vs lines expressing it (22) | 1.28× higher at baseline in the lines without FOXA2 | 0.015 | ⚠ within organs, on part of the lines; also absent: TFF1, GPX2, F5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.290). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.3, -26.1); signed map (10.3, -3.4). **Vector** length 125, 44.3% of its response variance represented; |z| ≥ 3 in 1,306 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.3 | +4.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.4 | +2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | +5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.0 | +11.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +1.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.3 | -0.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.2 | -1.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -10.1 | -23.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.8 | -7.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.7 | -9.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -6.1 | -9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.9 | -24.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.6 | -1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.9 | -5.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.7 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | ataxin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.12 — chr12:111,443,485-111,599,676 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATX2; previously SCA2, TNRC13 |
| Gene groups (HGNC) | Ataxin 2 family |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99700](https://www.uniprot.org/uniprotkb/Q99700) (Ataxin-2):

> Involved in EGFR trafficking, acting as negative regulator of endocytic EGFR internalization at the plasma membrane.

**Summary**, from NCBI Gene [6311](https://www.ncbi.nlm.nih.gov/gene/6311):

> This gene belongs to a group of genes that is associated with microsatellite-expansion diseases, a class of neurological and neuromuscular disorders caused by expansion of short stretches of repetitive DNA. The protein encoded by this gene has two globular domains near the N-terminus, one of which contains a clathrin-mediated trans-Golgi signal and an endoplasmic reticulum exit signal. The encoded cytoplasmic protein localizes to the endoplasmic reticulum and plasma membrane, is involved in …

**Accessions** — [HGNC:10555](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10555) · Entrez [6311](https://www.ncbi.nlm.nih.gov/gene/6311) · UniProt [Q99700](https://www.uniprot.org/uniprotkb/Q99700) · Ensembl [ENSG00000204842](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204842)

## Data

Gene col 12924: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12924); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12924, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12924]; `tensor/DDL_lfc|DDL_z.npy` [12924]; `embed/gene_vectors.npy` [12924]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12924 or target_col == 12924). Every well: [[ATXN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATXN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
