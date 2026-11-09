---
symbol: "FBXO38"
type: "gene"
col: 7035
ensembl_id: "ENSG00000145868"
name: "F-box protein 38"
location: "5q32"
module: 7
arm: "+"
pooled_cpm: 73.8
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 24
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# FBXO38

*F-box protein 38* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.67× (z +11.3, q 1e-26, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (17 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.341× (z -16.5, q 0e+00, down in 46 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.420× (z -13.3, q 5e-38, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UTP3]] (+0.75, fdr 7e-06), [[TACO1]] (+0.75, fdr 1e-05), [[ZNF268]] (+0.75, fdr 7e-06); moves opposite to [[TMEM65]] (-0.66, fdr 1e-05), [[DCUN1D4]] (-0.65, fdr 1e-05), [[SEC61A2]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7035.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +11.3 | 1e-26 | 42/47 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.68×** | +7.9 | 6e-13 | 36/48 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.03×** | +5.7 | 2e-06 | 38/47 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +4.9 | 1e-04 | 29/47 (NCI-H1573, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +4.5 | 9e-04 | 26/47 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 1.18× | +3.7 | 0.021 | 18/47 (HT-29, LS 180, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.16 | 17/47 (NCI-H2030, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 17 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7035.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.341×** | -16.5 | 0e+00 | 46/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.420×** | -13.3 | 5e-38 | 42/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.521×** | -10.0 | 2e-21 | 41/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.557×** | -8.6 | 1e-15 | 39/46 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.547×** | -8.6 | 1e-15 | 37/44 (HEC-1-A, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.517×** | -8.4 | 5e-15 | 40/48 (LoVo, CHP-212, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.597×** | -7.9 | 2e-13 | 38/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.586×** | -7.8 | 4e-13 | 34/42 (NCI-H1573, LoVo, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.590×** | -7.7 | 8e-13 | 36/46 (CFPAC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.518×** | -5.3 | 7e-06 | 34/47 (NCI-H1792, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **0.741×** | -4.6 | 2e-04 | 32/47 (SW 1088, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.751×** | -4.4 | 5e-04 | 27/47 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.752×** | -4.4 | 5e-04 | 27/47 (LoVo, KATO III, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.827×** | -4.1 | 0.002 | 20/47 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.766×** | -4.1 | 0.002 | 28/47 (LoVo, NCI-H1573, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.643×** | -3.5 | 0.013 | 23/47 (NCI-H460, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.759×** | -3.0 | 0.063 | 19/47 (Hs 766T, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.813×** | -3.0 | 0.065 | 19/46 (AN3 CA, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7035. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 97.8 | 0 | 10 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -25.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.203× (z -17.6) |
| [[LoVo (line)]] | wt | 213 | 2 | 6 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 11.6× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.214× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[PANC-1 (line)]] | alt | 66.6 | 1 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.130× (z -23.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -21.2) |
| [[HOP62 (line)]] | alt | 60.4 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.9) | [[Digitoxin (drug)]] 5 µM 0.278× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.315× (z -11.9) |
| [[SW480 (line)]] | alt | 67.8 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -24.2) |
| [[HS-578T (line)]] | alt | 63.6 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.4) | [[Digitoxin (drug)]] 5 µM 0.256× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 61.3 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 56.3 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +11.3) | [[Digitoxin (drug)]] 5 µM 0.193× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.377× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 68.3 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -13.5) |
| [[H4 (line)]] | wt | 64.6 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0521× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.205× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 83.4 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.283× (z -11.0) |
| [[LS 180 (line)]] | wt | 73.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.239× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.356× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 82.0 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.109× (z -21.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[SNU-423 (line)]] | alt | 83.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.358× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 69.4 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.352× (z -9.5) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.397× (z -8.8) |
| [[CHP-212 (line)]] | wt | 58.4 | 0 | 3 (3 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0827× (z -12.7) ⚠ transcription drop |
| [[COLO 205 (line)]] | alt | 63.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -13.2) |
| [[HepG2_C3A (line)]] | wt | 60.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.235× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -10.5) |
| [[Hs 766T (line)]] | wt | 85.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.342× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.393× (z -8.7) |
| [[J82 (line)]] | alt | 71.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -13.6) |
| [[SHP-77 (line)]] | alt | 67.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -14.3) |
| [[SW 900 (line)]] | alt | 45.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SW1417 (line)]] | alt | 61.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.306× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.336× (z -10.1) |
| [[A-427 (line)]] | wt | 75.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.357× (z -9.2) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 79.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[hTERT-HPNE (line)]] | wt | 50.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0513× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.288× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 40.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.304× (z -10.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 73.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.341× (z -11.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 119 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0610× (z -13.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 93.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -9.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 61.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.223× (z -13.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 63.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 52.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.362× (z -10.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 64.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.322× (z -11.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 89.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 56.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +11.8) | — |
| [[SK-MEL-2 (line)]] | alt | 99.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.293× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SNU-1 (line)]] | wt | 76.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.230× (z -11.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.91 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 157 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7035), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP3]] | +0.75 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[TACO1]] | +0.75 | +0.81 / +0.55 | both halves | 1e-05 |  |
| [[ZNF268]] | +0.75 | +0.79 / +0.66 | both halves | 7e-06 |  |
| [[MOCS3]] | +0.74 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[ZNF646]] | +0.71 | +0.72 / +0.57 | both halves | 9e-06 |  |
| [[ZNF830]] | +0.70 | +0.77 / +0.56 | both halves | 1e-05 |  |
| [[ZBTB6]] | +0.70 | +0.73 / +0.57 | both halves | 9e-06 |  |
| [[CBLL1]] | +0.70 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[ZBED9]] | +0.70 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[STYXL1]] | +0.70 | +0.77 / +0.56 | both halves | 1e-05 |  |
| [[PYM1]] | +0.70 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[NAIF1]] | +0.69 | +0.73 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM65]] | -0.66 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[DCUN1D4]] | -0.65 | -0.70 / -0.52 | both halves | 1e-05 |  |
| [[SEC61A2]] | -0.64 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[STK32C]] | -0.62 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[STRN]] | -0.61 | -0.73 / -0.36 | both halves | 1e-04 |  |
| [[HDAC3]] | -0.61 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[RFX2]] | -0.60 | -0.62 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-36.8, 9.4); signed map (-1.7, -25.2). **Vector** length 116, 37.0% of its response variance represented; |z| ≥ 3 in 1,061 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.6 | +11.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.5 | +4.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +10.2 | +7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.1 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.8 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.2 | +2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +2.9 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.7 | -16.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.8 | -7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.0 | -10.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.9 | -13.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 38 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:148,383,935-148,442,836 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MOKA, SP329, FLJ13962, Fbx38 |
| Gene groups (HGNC) | F-boxes other |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PIJ6](https://www.uniprot.org/uniprotkb/Q6PIJ6) (F-box only protein 38):

> Substrate recognition component of a SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of PDCD1/PD-1, thereby regulating T-cells-mediated immunity. Required for anti-tumor activity of T-cells by promoting the degradation of PDCD1/PD-1; the PDCD1-mediated inhibitory pathway being exploited by tumors to attenuate anti-tumor immunity and facilitate tumor survival. May indirectly stimulate the activity of …

**Summary**, from NCBI Gene [81545](https://www.ncbi.nlm.nih.gov/gene/81545):

> This gene encodes a large protein that contains an F-box domain and may participate in protein ubiquitination. The encoded protein is a transcriptional co-activator of Krueppel-like factor 7 (Klf7). A heterozygous mutation in this gene was found in individuals with autosomal dominant distal hereditary motor neuronopathy type IID. There is a pseudogene for this gene on chromosome 4. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2013]

**Accessions** — [HGNC:28844](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28844) · Entrez [81545](https://www.ncbi.nlm.nih.gov/gene/81545) · UniProt [Q6PIJ6](https://www.uniprot.org/uniprotkb/Q6PIJ6) · Ensembl [ENSG00000145868](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145868)

## Data

Gene col 7035: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7035); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7035, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7035]; `tensor/DDL_lfc|DDL_z.npy` [7035]; `embed/gene_vectors.npy` [7035]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7035 or target_col == 7035). Every well: [[FBXO38 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO38.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
