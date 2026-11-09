---
symbol: "ZNF76"
type: "gene"
col: 769
ensembl_id: "ENSG00000065029"
name: "zinc finger protein 76"
location: "6p21.31"
module: 170
arm: "+"
pooled_cpm: 16.53
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 29
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# ZNF76

*zinc finger protein 76* — 6p21.31

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.515× (z -18.0, q 0e+00, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELMOD3]] (+0.59, fdr 6e-05), [[C2orf42]] (+0.54, fdr 3e-05), [[C15orf40]] (+0.54, fdr 5e-04); moves opposite to [[GLS]] (-0.51, fdr 1e-04), [[EPB41L2]] (-0.50, fdr 1e-04), [[TNIK]] (-0.49, fdr 6e-05).
> It sits in the **+** arm of [[Module 170]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[MTHFS]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 769.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +3.9 | 0.048 | 14/48 (NCI-H23, NCI-H2347, …) | inconsistent across doses |  |
| [[Clotrimazole (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.34 | 7/47 (Hs 766T, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.19× | +3.1 | 0.34 | 9/48 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 769.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.515×** | -18.0 | 0e+00 | 37/47 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.429×** | -16.3 | 0e+00 | 41/48 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.454×** | -15.2 | 0e+00 | 43/47 (NCI-H1792, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.475×** | -14.3 | 2e-44 | 40/48 (HEC-1-A, SW1417, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.597×** | -14.0 | 2e-42 | 39/47 (AsPC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.498×** | -13.4 | 5e-39 | 38/48 (H4, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.521×** | -12.5 | 4e-34 | 30/46 (SW480, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.534×** | -12.1 | 1e-31 | 34/47 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.562×** | -11.1 | 9e-27 | 37/47 (SW480, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.570×** | -10.8 | 2e-25 | 37/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.616×** | -9.3 | 6e-19 | 30/45 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.621×** | -8.8 | 7e-17 | 26/44 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.643×** | -8.5 | 1e-15 | 30/47 (LoVo, HS-578T, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.662×** | -7.9 | 1e-13 | 29/47 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.664×** | -7.6 | 2e-12 | 24/47 (NCI-H1792, H4, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.685×** | -7.3 | 1e-11 | 25/47 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.780×** | -6.7 | 6e-10 | 21/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.569×** | -5.7 | 4e-07 | 18/48 (PANC-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.570×** | -5.7 | 4e-07 | 17/48 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.725×** | -5.4 | 2e-06 | 21/48 (NCI-H460, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.640×** | -4.5 | 2e-04 | 15/45 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.675×** | -3.9 | 0.002 | 13/47 (BT-474, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.864× | -2.8 | 0.088 | 2/47 (hTERT-HPNE, SK-MEL-2) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 769. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 29.5 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -12.4) |
| [[SW480 (line)]] | alt | 18.7 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.264× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.540× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 23.3 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 17.6 | 0 | 5 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.148× (z -12.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.389× (z -8.5) |
| [[HCT15 (line)]] | alt | 30.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib (drug)]] 5 µM 0.0690× (z -8.6) |
| [[HS-578T (line)]] | alt | 19.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -13.1) |
| [[LOX-IMVI (line)]] | wt | 12.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -12.2) |
| [[H4 (line)]] | wt | 14.0 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0623× (z -12.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 24.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -14.3) |
| [[LoVo (line)]] | wt | 11.8 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.262× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.118× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 15.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -10.6) |
| [[A-172 (line)]] | wt | 17.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -8.5) |
| [[A-427 (line)]] | wt | 16.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 13.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0678× (z -22.1) |
| [[C-33 A (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0613× (z -9.2) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -8.7) |
| [[COLO 205 (line)]] | alt | 11.4 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0642× (z -10.2) |
| [[Hs 766T (line)]] | wt | 15.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -10.6) |
| [[HT-29 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -8.7) |
| [[J82 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -11.0) |
| [[KATO III (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 14.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -9.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[RPMI-7951 (line)]] | alt | 20.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -16.6) |
| [[SNU-423 (line)]] | alt | 29.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -14.1) |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.116× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0567× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 769), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELMOD3]] | +0.59 | +0.39 / +0.66 | both halves | 6e-05 |  |
| [[C2orf42]] | +0.54 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[C15orf40]] | +0.54 | +0.24 / +0.51 | both halves | 5e-04 |  |
| [[KLHL12]] | +0.53 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[BMS1P4-1]] | +0.52 | +0.27 / +0.46 | both halves | 3e-04 |  |
| [[PAAF1]] | +0.52 | +0.40 / +0.47 | both halves | 4e-05 |  |
| [[CBY1]] | +0.52 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[TRAPPC13]] | +0.51 | +0.39 / +0.45 | both halves | 5e-05 |  |
| [[MAU2]] | +0.51 | +0.22 / +0.59 | both halves | 6e-04 |  |
| [[TAB1]] | +0.51 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[MORN4]] | +0.51 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[CPSF7]] | +0.50 | +0.32 / +0.47 | both halves | 2e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLS]] | -0.51 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[EPB41L2]] | -0.50 | -0.36 / -0.57 | both halves | 1e-04 |  |
| [[TNIK]] | -0.49 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[KLF12]] | -0.48 | -0.51 / -0.37 | both halves | 8e-05 | same gene group |
| [[IL1RAP]] | -0.48 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[TIAM1]] | -0.47 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[PRKCA]] | -0.47 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[ITGA6]] | -0.44 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[APLP2]] | -0.44 | -0.32 / -0.42 | both halves | 1e-04 |  |
| [[EDA]] | -0.44 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[SPTBN1]] | -0.44 | -0.22 / -0.43 | both halves | 6e-04 |  |
| [[EPB41L5]] | -0.44 | -0.22 / -0.53 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTHFS]] | C | ZNF76's natural level strengthens MTHFS's drug response | ZNF76's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.10; direction not clear | 0.074 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.457). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-26.0, 21.3); signed map (-12.7, -14.8). **Vector** length 51.4, 7.18% of its response variance represented; |z| ≥ 3 in 1,112 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +4.5 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | -0.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +1.5 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.3 | +1.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.3 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.7 | -10.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -14.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.5 | -9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.5 | -2.8 |
|  | [[EX229 (drug)]] 5 µM |  | -1.4 | -4.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -5.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | +0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 76 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:35,258,909-35,295,985 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Zfp523, ZNF523; previously D6S229E |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [P36508](https://www.uniprot.org/uniprotkb/P36508) (Zinc finger protein 76):

> Transcription factor that regulates expression of genes transcribed by both RNA polymerases II and III. Specifically recognizes and binds the Staf-binding site (SBS), a consensus DNA-binding motif present in many promoters. Able to activate expression of small nuclear RNA (snRNA) transcribed by RNA polymerases II and III. Also regulates expression of mRNAs and acts as a DNA-binding transcription repressor that inhibits the activity of the TATA-binding protein (TBP).

**Summary**, from NCBI Gene [7629](https://www.ncbi.nlm.nih.gov/gene/7629):

> Enables DNA-binding transcription activator activity, RNA polymerase II-specific; DNA-binding transcription repressor activity, RNA polymerase II-specific; and sequence-specific double-stranded DNA binding activity. Involved in negative regulation of transcription by RNA polymerase II and positive regulation of transcription by RNA polymerase II. Is active in chromatin. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13149](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13149) · Entrez [7629](https://www.ncbi.nlm.nih.gov/gene/7629) · UniProt [P36508](https://www.uniprot.org/uniprotkb/P36508) · Ensembl [ENSG00000065029](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065029)

## Data

Gene col 769: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 769); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 769, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 769]; `tensor/DDL_lfc|DDL_z.npy` [769]; `embed/gene_vectors.npy` [769]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 769 or target_col == 769). Every well: [[ZNF76 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF76.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
