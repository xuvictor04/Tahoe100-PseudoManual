---
symbol: "C2CD3"
type: "gene"
col: 9581
ensembl_id: "ENSG00000168014"
name: "C2 domain containing 3 centriole elongation regulator"
location: "11q13.4"
module: 20
arm: "+"
pooled_cpm: 51.48
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# C2CD3

*C2 domain containing 3 centriole elongation regulator* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.48× (z +25.5, q 0e+00, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.83× (z +12.3, q 1e-32, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 0.104×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.126×; ⚠ toxic; cell-cycle shift, explains ~81% of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (SW 1271 0.0913×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.484×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A-427 0.436×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HCFC1]] (+0.68, fdr 2e-05), [[ZNF407]] (+0.67, fdr 4e-05), [[TUBA1B]] (+0.63, fdr 1e-05); moves opposite to [[SNHG7]] (-0.64, fdr 1e-05), [[SNHG8]] (-0.63, fdr 1e-05), [[RP9]] (-0.62, fdr 4e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 21 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9581.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.48×** | +25.5 | 0e+00 | 47/48 (A-172, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **3.30×** | +24.4 | 0e+00 | 48/48 (A-172, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.84×** | +21.3 | 0e+00 | 47/48 (A-172, AsPC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.63×** | +14.0 | 2e-42 | 41/48 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +12.3 | 1e-32 | 44/48 (BT-474, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.77×** | +11.2 | 5e-27 | 39/47 (SW480, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +9.8 | 8e-21 | 41/47 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +9.4 | 5e-19 | 41/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +9.3 | 8e-19 | 25/48 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.60×** | +9.2 | 1e-18 | 35/49 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +8.2 | 1e-14 | 35/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +8.2 | 2e-14 | 33/48 (SW480, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +7.7 | 4e-13 | 33/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.96×** | +7.2 | 3e-11 | 34/49 (MIA PaCa-2, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.42×** | +7.1 | 4e-11 | 33/48 (SW480, LoVo, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +6.5 | 2e-09 | 28/48 (HCT15, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.35×** | +6.1 | 3e-08 | 30/47 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +5.5 | 1e-06 | 24/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +5.4 | 1e-06 | 25/48 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.9 | 2e-05 | 25/48 (HOP62, RKO, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +4.6 | 8e-05 | 21/48 (A-172, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +4.4 | 3e-04 | 22/48 (A-172, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +4.3 | 3e-04 | 19/48 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9581.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 0.104×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.126×; ⚠ toxic; cell-cycle shift, explains ~81% of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (SW 1271 0.0913×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.484×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (A-427 0.436×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.839× | -5.1 | 2e-04 | 18/48 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.841× | -3.6 | 0.10 | 15/48 (J82, A-427, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 0.897× | -3.2 | 0.28 | 12/48 (J82, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9581. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 33.1 | 6 (5 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 11.3× (z +18.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 6.77× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.104× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change |
| [[BT-474 (line)]] | alt | 95.0 | 8 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.49× (z +15.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 39.5 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +19.4) | — |
| [[NCI-H460 (line)]] | wt | 36.1 | 8 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.61× (z +14.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.8) | — |
| [[SW480 (line)]] | alt | 72.2 | 8 (6 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.72× (z +14.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.6) | — |
| [[LoVo (line)]] | wt | 37.5 | 6 (5 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.05× (z +11.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +11.0) | — |
| [[A-172 (line)]] | wt | 44.1 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.89× (z +19.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 7.71× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 52.4 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.30× (z +14.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW1417 (line)]] | alt | 57.2 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.13× (z +11.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +8.6) | — |
| [[A498 (line)]] | wt | 25.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +16.8) | — |
| [[A549 (line)]] | wt | 43.2 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.95× (z +14.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.99× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 39.5 | 2 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.85× (z +9.2) ⚠ cell-cycle shift, explains ~25% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.126× (z -13.7) ⚠ toxic; cell-cycle shift, explains ~81% of this change |
| [[LS 180 (line)]] | wt | 41.2 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.63× (z +14.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 31.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.4) | — |
| [[NCI-H2347 (line)]] | alt | 33.6 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.61× (z +15.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 47.5 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +13.4) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SNU-423 (line)]] | alt | 31.8 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.10× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW 900 (line)]] | alt | 47.2 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.09× (z +12.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.91× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 26.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.21× (z +11.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HEC-1-A (line)]] | alt | 44.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.33× (z +15.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[Hs 766T (line)]] | wt | 34.6 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.32× (z +12.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HT-29 (line)]] | alt | 51.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.68× (z +14.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[J82 (line)]] | alt | 75.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.65× (z +9.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1573 (line)]] | alt | 50.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +9.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 75.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.45× (z +11.4) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[RKO (line)]] | wt | 42.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.88× (z +10.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[RPMI-7951 (line)]] | alt | 47.6 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.83× (z +10.9) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SNU-1 (line)]] | wt | 44.5 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.54× (z +10.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.99× (z +8.8) | — |
| [[A-427 (line)]] | wt | 83.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -10.5) |
| [[HOP62 (line)]] | alt | 27.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.59× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[KATO III (line)]] | alt | 55.1 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.93× (z +10.8) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HCT15 (line)]] | alt | 49.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.99× (z +9.3) | — |
| [[hTERT-HPNE (line)]] | wt | 29.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.34× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +10.4) | — |
| [[SW 1271 (line)]] | alt | 92.9 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0913× (z -11.0) |
| [[AN3 CA (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9581), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCFC1]] | +0.68 | +0.64 / +0.47 | both halves | 2e-05 | pathway: Organelle biogenesis and maintenance |
| [[ZNF407]] | +0.67 | +0.76 / +0.41 | both halves | 4e-05 |  |
| [[TUBA1B]] | +0.63 | +0.55 / +0.51 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium |
| [[XRCC5]] | +0.61 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[TARDBP]] | +0.59 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[CDK2]] | +0.58 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[PSMD1]] | +0.58 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[TRRAP]] | +0.57 | +0.36 / +0.55 | both halves | 9e-05 |  |
| [[SNRPB]] | +0.57 | +0.69 / +0.26 | both halves | 4e-04 |  |
| [[MCM8]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[TYMS]] | +0.56 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[BANF1]] | +0.56 | +0.43 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG7]] | -0.64 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[SNHG8]] | -0.63 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[RP9]] | -0.62 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[SNHG11]] | -0.60 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[SNHG32]] | -0.59 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[NFKBIL1]] | -0.59 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[EPB41L4A-AS1]] | -0.59 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[CDK7]] | -0.58 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[ATF4]] | -0.58 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[PRPF39]] | -0.58 | -0.67 / -0.23 | both halves | 5e-04 |  |
| [[ZNF14]] | -0.57 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[GAS5]] | -0.57 | -0.49 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers C2CD3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.420). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.9, -30.1); signed map (10.0, -45.1). **Vector** length 83.0, 20.2% of its response variance represented; |z| ≥ 3 in 1,246 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.1 | +12.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +5.3 | +9.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.3 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +8.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +9.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.2 | +1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +4.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.2 | +1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | +2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | +9.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.7 | -5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | +0.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.7 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | C2 domain containing 3 centriole elongation regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:74,012,718-74,171,210 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586P0123 |
| Gene groups (HGNC) | C2 domain containing; Centriolar satellite proteins |
| Reactome | 4 pathways, smallest: Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4AC94](https://www.uniprot.org/uniprotkb/Q4AC94) (C2 domain-containing protein 3):

> Component of the centrioles that acts as a positive regulator of centriole elongation. Promotes assembly of centriolar distal appendage, a structure at the distal end of the mother centriole that acts as an anchor of the cilium, and is required for recruitment of centriolar distal appendages proteins CEP83, SCLT1, CEP89, FBF1 and CEP164. Not required for centriolar satellite integrity or RAB8 activation. Required for primary cilium formation. Required for sonic hedgehog/SHH signaling and for …

**Summary**, from NCBI Gene [26005](https://www.ncbi.nlm.nih.gov/gene/26005):

> This gene encodes a protein that functions as a regulator of centriole elongation. Studies of the orthologous mouse protein show that it promotes centriolar distal appendage assembly and is also required for the recruitment of other ciliogenic proteins, including intraflagellar transport proteins. Mutations in this gene cause orofaciodigital syndrome XIV (OFD14), a ciliopathy resulting in malformations of the oral cavity, face and digits. Alternative splicing of this gene results in multiple …

**Accessions** — [HGNC:24564](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24564) · Entrez [26005](https://www.ncbi.nlm.nih.gov/gene/26005) · UniProt [Q4AC94](https://www.uniprot.org/uniprotkb/Q4AC94) · Ensembl [ENSG00000168014](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168014)

## Data

Gene col 9581: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9581); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9581, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9581]; `tensor/DDL_lfc|DDL_z.npy` [9581]; `embed/gene_vectors.npy` [9581]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9581 or target_col == 9581). Every well: [[C2CD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C2CD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
