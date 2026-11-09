---
symbol: "ACAA2"
type: "gene"
col: 9451
ensembl_id: "ENSG00000167315"
name: "acetyl-CoA acyltransferase 2"
location: "18q21.1"
module: 3
arm: "-"
pooled_cpm: 33.85
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# ACAA2

*acetyl-CoA acyltransferase 2* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.55× (z +16.1, q 0e+00, up in 35 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mifepristone (drug)]] 5 µM: 1.47× (z +4.9, q 2e-04, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.473× (z -9.9, q 3e-20, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHYH]] (+0.58, fdr 1e-05), [[BROX]] (+0.56, fdr 1e-05), [[ZSCAN30]] (+0.55, fdr 6e-05); moves opposite to [[TRAPPC4]] (-0.61, fdr 2e-05), [[LSM7]] (-0.55, fdr 4e-05), [[NAA10]] (-0.54, fdr 5e-05, ⚠ NAA10 in the vector space only through flagged drug-doses), [[TRABD]] (-0.53, fdr 5e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9451.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.55×** | +16.1 | 0e+00 | 35/36 (KATO III, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.25×** | +15.6 | 0e+00 | 43/44 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +10.5 | 1e-23 | 38/40 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Mifepristone (drug)]] 5 µM |  | **1.47×** | +4.9 | 2e-04 | 26/47 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **1.44×** | +4.8 | 2e-04 | 25/47 (HT-29, SNU-423, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +4.7 | 3e-04 | 25/47 (HS-578T, AsPC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Rosiglitazone (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.007 | 22/46 (LoVo, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.013 | 24/47 (AsPC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.45× | +3.0 | 0.13 | 9/47 (PANC-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 1.25× | +3.0 | 0.13 | 9/47 (KATO III, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9451.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.473×** | -9.9 | 3e-20 | 45/47 (NCI-H1792, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.509×** | -8.9 | 2e-16 | 41/47 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.526×** | -8.5 | 5e-15 | 39/47 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.553×** | -7.8 | 1e-12 | 39/46 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.702×** | -6.6 | 6e-09 | 29/47 (H4, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.649×** | -5.7 | 1e-06 | 30/47 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.654×** | -5.6 | 2e-06 | 32/46 (SNU-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.677×** | -5.1 | 2e-05 | 30/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.681×** | -5.0 | 3e-05 | 28/47 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.689×** | -4.9 | 5e-05 | 27/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.628×** | -3.2 | 0.071 | 17/47 (A-427, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.785×** | -3.2 | 0.071 | 19/47 (SW48, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9451. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 76.2 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +16.5) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.320× (z -11.2) |
| [[A549 (line)]] | wt | 29.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 37.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.03× (z +12.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 80.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.96× (z +15.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 45.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.05 µM 0.299× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 45.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.292× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.332× (z -8.6) |
| [[PANC-1 (line)]] | alt | 31.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +13.9) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.351× (z -10.0) |
| [[SW480 (line)]] | alt | 26.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +11.1) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 21.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +9.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 32.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 67.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +12.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 60.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.62× (z +11.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 18.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.06× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 28.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.87× (z +12.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 52.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +11.3) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 40.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.60× (z +13.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 55.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.84× (z +11.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.341× (z -9.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 24.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.73× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 21.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 43.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +9.0) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -9.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 51.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.35× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 11.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 53.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +9.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 48.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 17.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.09 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9451), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHYH]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[BROX]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[ZSCAN30]] | +0.55 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[PLS3]] | +0.54 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[ACADM]] | +0.54 | +0.52 / +0.37 | both halves | 7e-05 | pathway: HALLMARK_ADIPOGENESIS; STRING 937 |
| [[NCOA4]] | +0.53 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[SPDYA]] | +0.53 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[YWHAE]] | +0.53 | +0.55 / +0.39 | both halves | 6e-05 |  |
| [[YWHAZ]] | +0.53 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[RNF167]] | +0.51 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[TRAM2-AS1]] | +0.51 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[ATP5PB]] | +0.50 | +0.56 / +0.33 | both halves | 1e-04 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |

## Genes that move opposite

*39 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC4]] | -0.61 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[LSM7]] | -0.55 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[NAA10]] ⚠ | -0.54 | -0.39 / -0.45 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TRABD]] | -0.53 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[MRPL41]] ⚠ | -0.52 | -0.42 / -0.37 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CDC34]] | -0.52 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[CCNQ]] | -0.52 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[LSM2]] | -0.51 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[B4GALT3]] | -0.51 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[KXD1]] | -0.51 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[CTU2]] | -0.51 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[DGCR2]] | -0.51 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[ORAI1]] | -0.49 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[PUSL1]] | -0.49 | -0.37 / -0.42 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ACAA2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ARHGEF37]] | C | ARHGEF37 activity raises ACAA2's level | lines that do not express ARHGEF37 (4) vs lines expressing it (46) | 2.88× lower at baseline in the lines without ARHGEF37 | 0.018 | ⚠ few lines (4 vs 46); across organs; also absent: DBNDD1, RNFT2, ARFGEF3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.459). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-22.2, 21.7); signed map (17.4, -37.0). **Vector** length 66.4, 13.0% of its response variance represented; |z| ≥ 3 in 942 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.8 | +4.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +1.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | -2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +15.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.8 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | -3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +0.8 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | -7.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.0 | -8.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -8.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.0 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -9.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -0.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.7 | -0.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.5 | -0.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | acetyl-CoA acyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:49,782,164-49,813,953 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DSAEC |
| Gene groups (HGNC) | Thioester hydrolases; Acyltransferases |
| Hallmark sets | FATTY_ACID_METABOLISM, ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Mitochondrial Fatty Acid Beta-Oxidation; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [P42765](https://www.uniprot.org/uniprotkb/P42765) (3-ketoacyl-CoA thiolase, mitochondrial):

> In the production of energy from fats, this is one of the enzymes that catalyzes the last step of the mitochondrial beta-oxidation pathway, an aerobic process breaking down fatty acids into acetyl-CoA (Probable). Using free coenzyme A/CoA, catalyzes the thiolytic cleavage of medium- to long-chain unbranched 3-oxoacyl-CoAs into acetyl-CoA and a fatty acyl-CoA shortened by two carbon atoms (Probable). Also catalyzes the condensation of two acetyl-CoA molecules into acetoacetyl-CoA and could be …

**Summary**, from NCBI Gene [10449](https://www.ncbi.nlm.nih.gov/gene/10449):

> The encoded protein catalyzes the last step of the mitochondrial fatty acid beta-oxidation spiral. Unlike most mitochondrial matrix proteins, it contains a non-cleavable amino-terminal targeting signal. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:83](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:83) · Entrez [10449](https://www.ncbi.nlm.nih.gov/gene/10449) · UniProt [P42765](https://www.uniprot.org/uniprotkb/P42765) · Ensembl [ENSG00000167315](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167315)

## Data

Gene col 9451: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9451); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9451, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9451]; `tensor/DDL_lfc|DDL_z.npy` [9451]; `embed/gene_vectors.npy` [9451]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9451 or target_col == 9451). Every well: [[ACAA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACAA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
