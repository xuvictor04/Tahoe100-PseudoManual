---
symbol: "SFXN2"
type: "gene"
col: 7976
ensembl_id: "ENSG00000156398"
name: "sideroflexin 2"
location: "10q24.32"
module: 40
arm: "+"
pooled_cpm: 7.33
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 25
n_dd_up_clean: 3
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# SFXN2

*sideroflexin 2* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.25× (z +15.0, q 0e+00, up in 38 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.340× (z -14.1, q 1e-42, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPY19L3]] (+0.65, fdr 8e-06), [[URI1]] (+0.64, fdr 1e-05), [[ING5]] (+0.64, fdr 1e-05); moves opposite to [[GNGT1]] (-0.55, fdr 4e-05), [[IGSF1]] (-0.54, fdr 2e-05), [[BAZ2B]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7976.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +15.0 | 0e+00 | 38/43 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.25×** | +10.7 | 4e-24 | 34/46 (PANC-1, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.24×** | +10.6 | 5e-24 | 34/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.15×** | +10.0 | 2e-21 | 34/47 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.68×** | +6.6 | 5e-09 | 17/41 (PANC-1, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +5.1 | 3e-05 | 14/47 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.38×** | +4.1 | 0.003 | 2/13 (HT-29, SNU-423) | top dose only | composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.008 | 9/47 (A-172, NCI-H2347, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.30×** | +3.3 | 0.054 | 11/42 (PANC-1, HT-29, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.26× | +3.1 | 0.11 | 8/47 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.26× | +3.1 | 0.11 | 5/44 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7976.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.340×** | -14.1 | 1e-42 | 34/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.359×** | -12.9 | 1e-35 | 34/45 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.410×** | -11.7 | 4e-29 | 32/42 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.470×** | -9.3 | 1e-18 | 29/45 (A498, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.611×** | -9.1 | 9e-18 | 23/44 (KATO III, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.506×** | -8.9 | 4e-17 | 28/45 (A498, HEC-1-A, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.522×** | -8.5 | 1e-15 | 29/46 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.577×** | -7.2 | 4e-11 | 24/46 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.592×** | -6.9 | 4e-10 | 26/47 (A498, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.595×** | -6.8 | 6e-10 | 24/45 (HOP62, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.616×** | -6.3 | 1e-08 | 22/42 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.619×** | -6.3 | 2e-08 | 23/45 (A498, HOP62, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.461×** | -5.3 | 5e-06 | 15/46 (SW480, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.637×** | -4.2 | 0.001 | 3/47 (PANC-1, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.736×** | -3.7 | 0.008 | 12/41 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.757×** | -3.6 | 0.010 | 16/45 (BT-474, SW1417, …) | top dose only |  |
| [[Mozavaptan (drug)]] 0.05 µM |  | **0.763×** | -3.3 | 0.037 | 11/44 (AsPC-1, LS 180, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.781×** | -3.2 | 0.038 | 12/47 (A-172, HEC-1-A, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.773×** | -3.2 | 0.046 | 13/45 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, -0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7976. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 10.8 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -10.2) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.179× (z -10.1) |
| [[SW480 (line)]] | alt | 11.8 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -14.5) |
| [[HOP62 (line)]] | alt | 8.40 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0313× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.111× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 4.50 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.89× (z +8.6) | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0668× (z -8.8) |
| [[BT-474 (line)]] | alt | 7.47 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0429× (z -12.2) |
| [[KATO III (line)]] | alt | 7.61 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -13.3) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.144× (z -8.6) |
| [[SW1417 (line)]] | alt | 9.92 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.107× (z -11.7) |
| [[A-172 (line)]] | wt | 6.98 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -12.5) ⚠ cell-cycle shift, explains ~75% of this change |
| [[A549 (line)]] | wt | 5.44 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.101× (z -8.6) |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0989× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -9.1) ⚠ cell-cycle shift, explains ~75% of this change |
| [[HS-578T (line)]] | alt | 5.09 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0706× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 4.32 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.115× (z -8.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H23 (line)]] | alt | 6.47 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0918× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 6.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +9.1) | — |
| [[RKO (line)]] | wt | 12.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.132× (z -9.2) |
| [[SW 900 (line)]] | alt | 5.71 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0729× (z -8.8) ⚠ cell-cycle shift, explains ~60% of this change |
| [[A-427 (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7976), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY19L3]] | +0.65 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[URI1]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[ING5]] | +0.64 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[CRLS1]] | +0.64 | +0.45 / +0.73 | both halves | 3e-05 |  |
| [[MSTO2P]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[MOGS]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[TMEM243]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[EIF3B]] | +0.62 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[RABEPK]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[ZMYND19]] | +0.61 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[PDIA5]] | +0.61 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[ATAD3A]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNGT1]] | -0.55 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[IGSF1]] | -0.54 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[BAZ2B]] | -0.53 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[ASF1A]] | -0.52 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[TFE3]] | -0.52 | -0.36 / -0.57 | both halves | 9e-05 |  |
| [[PSMA4]] | -0.52 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[AFF4]] | -0.51 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[CARD6]] | -0.51 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[MARCKS]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[DCTN6]] | -0.51 | -0.29 / -0.56 | both halves | 2e-04 |  |
| [[FSIP2]] | -0.51 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[CDKN2B]] | -0.50 | -0.32 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SFXN2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ATXN1]] | B | ATXN1 activity lowers SFXN2's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 1.46× higher at baseline in the lines without ATXN1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[HDAC6]] | B | HDAC6 activity lowers SFXN2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GKAP1]] | C | GKAP1 activity raises SFXN2's level | lines that do not express GKAP1 (3) vs lines expressing it (47) | 1.86× lower at baseline in the lines without GKAP1 | 0.066 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SEMA3F, TMEM132A, SPDL1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (7.0, -31.2); signed map (-47.8, 4.8). **Vector** length 75.8, 13.7% of its response variance represented; |z| ≥ 3 in 1,154 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +15.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.4 | +10.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +2.3 | +6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +2.0 | +4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +1.9 | +10.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.3 | +1.1 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.3 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.9 | -12.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -8.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -8.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -6.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | sideroflexin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:102,714,538-102,743,492 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SLC56A2 |
| Gene groups (HGNC) | Solute carrier family 56, sideroflexins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NB2](https://www.uniprot.org/uniprotkb/Q96NB2) (Sideroflexin-2):

> Mitochondrial amino-acid transporter that mediates transport of serine into mitochondria. Involved in mitochondrial iron homeostasis by regulating heme biosynthesis.

**Summary**, from NCBI Gene [118980](https://www.ncbi.nlm.nih.gov/gene/118980):

> Predicted to enable transmembrane transporter activity. Involved in mitochondrial transmembrane transport. Located in mitochondrial outer membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16086](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16086) · Entrez [118980](https://www.ncbi.nlm.nih.gov/gene/118980) · UniProt [Q96NB2](https://www.uniprot.org/uniprotkb/Q96NB2) · Ensembl [ENSG00000156398](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156398)

## Data

Gene col 7976: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7976); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7976, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7976]; `tensor/DDL_lfc|DDL_z.npy` [7976]; `embed/gene_vectors.npy` [7976]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7976 or target_col == 7976). Every well: [[SFXN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFXN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
