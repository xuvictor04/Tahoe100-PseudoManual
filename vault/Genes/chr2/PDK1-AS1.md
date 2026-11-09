---
symbol: "PDK1-AS1"
type: "gene"
col: 13441
ensembl_id: "ENSG00000225205"
name: "ITGA6 and PDK1 antisense RNA 1"
location: "2q31.1"
module: 17
arm: "-"
pooled_cpm: 30.78
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 25
n_dd_up_clean: 11
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# PDK1-AS1

*ITGA6 and PDK1 antisense RNA 1* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +12.0, q 3e-30, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.403× (z -21.5, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNT2-AS1]] (+0.64, fdr 3e-05), [[RNF217-AS1]] (+0.63, fdr 6e-05), [[SPRY3]] (+0.62, fdr 2e-05); moves opposite to [[PRPF39]] (-0.64, fdr 3e-05), [[EHMT2]] (-0.62, fdr 5e-05), [[MRPS31P4]] (-0.61, fdr 4e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13441.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +12.0 | 3e-30 | 33/47 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.6 | 2e-08 | 27/48 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +6.5 | 2e-08 | 28/48 (HT-29, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.0 | 2e-07 | 28/48 (HS-578T, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +5.2 | 2e-05 | 23/41 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.2 | 2e-05 | 21/47 (HS-578T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Roxadustat (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.010 | 17/47 (A-172, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +3.8 | 0.010 | 13/35 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.041 | 9/48 (HEC-1-A, Panc 03.27, …) | top dose only | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.062 | 14/47 (SW480, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.20×** | +3.1 | 0.089 | 5/48 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.089 | 3/48 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.094 | 3/45 (MIA PaCa-2, HCT15, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13441.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.403×** | -21.5 | 0e+00 | 42/47 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.370×** | -16.7 | 0e+00 | 42/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.448×** | -13.5 | 3e-39 | 41/48 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.479×** | -11.9 | 2e-30 | 41/47 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.503×** | -11.5 | 1e-28 | 38/47 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.543×** | -10.2 | 1e-22 | 34/48 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.556×** | -9.9 | 5e-21 | 39/48 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.576×** | -9.2 | 2e-18 | 30/47 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.387×** | -8.3 | 5e-15 | 32/48 (LOX-IMVI, CFPAC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.808×** | -5.0 | 3e-05 | 22/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.582×** | -4.7 | 1e-04 | 23/48 (HEC-1-A, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -4.6 | 2e-04 | 6/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.771×** | -4.2 | 0.001 | 20/44 (NCI-H23, J82, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.634×** | -4.0 | 0.003 | 16/46 (HEC-1-A, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.791×** | -3.9 | 0.003 | 22/47 (SNU-1, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.805×** | -3.6 | 0.009 | 17/48 (LOX-IMVI, HCT15, …) | two highest doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.669×** | -3.5 | 0.013 | 18/46 (NCI-H460, HOP62, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13441. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 57.6 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -25.2) |
| [[NCI-H23 (line)]] | alt | 71.7 | 0 | 10 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0750× (z -21.6) |
| [[HEC-1-A (line)]] | alt | 45.0 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -20.3) |
| [[C-33 A (line)]] | alt | 44.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -11.2) |
| [[J82 (line)]] | alt | 39.0 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.199× (z -12.0) |
| [[SNU-423 (line)]] | alt | 36.9 | 0 | 6 | — | [[Belinostat (drug)]] 5 µM 0.222× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 50.9 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -13.5) |
| [[HOP62 (line)]] | alt | 49.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -13.1) |
| [[LOX-IMVI (line)]] | wt | 39.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -13.6) |
| [[HCT15 (line)]] | alt | 40.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -13.7) |
| [[PANC-1 (line)]] | alt | 24.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -16.7) |
| [[SW480 (line)]] | alt | 32.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -14.3) |
| [[LoVo (line)]] | wt | 29.2 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 31.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -12.4) |
| [[HS-578T (line)]] | alt | 14.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +8.5) | [[Belinostat (drug)]] 5 µM 0.191× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 23.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -14.0) |
| [[NCI-H1792 (line)]] | alt | 34.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -18.4) |
| [[Panc 03.27 (line)]] | alt | 31.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -9.4) |
| [[RKO (line)]] | wt | 17.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.0543× (z -14.8) |
| [[RPMI-7951 (line)]] | alt | 26.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 39.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -10.8) |
| [[A-172 (line)]] | wt | 44.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -15.1) |
| [[AsPC-1 (line)]] | alt | 38.3 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.307× (z -9.4) |
| [[H4 (line)]] | wt | 35.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.124× (z -11.4) |
| [[Hs 766T (line)]] | wt | 33.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -10.8) |
| [[KATO III (line)]] | alt | 27.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 16.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -9.3) |
| [[SNU-1 (line)]] | wt | 23.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -10.8) |
| [[A-427 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13441), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNT2-AS1]] | +0.64 | +0.44 / +0.48 | both halves | 3e-05 | same gene group |
| [[RNF217-AS1]] | +0.63 | +0.39 / +0.54 | both halves | 6e-05 | same gene group |
| [[SPRY3]] | +0.62 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[MIATNB]] | +0.62 | +0.38 / +0.65 | both halves | 6e-05 |  |
| [[PHC2-AS1]] | +0.60 | +0.44 / +0.46 | both halves | 3e-05 | same gene group |
| [[ANXA2R-OT1]] | +0.60 | +0.32 / +0.61 | both halves | 2e-04 |  |
| [[SIAH2-AS1]] | +0.60 | +0.24 / +0.50 | both halves | 5e-04 | same gene group |
| [[DARS1-AS1]] | +0.59 | +0.40 / +0.51 | both halves | 5e-05 | same gene group |
| [[ATXN1L]] | +0.59 | +0.27 / +0.57 | both halves | 3e-04 |  |
| [[ZNF407]] | +0.59 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[SLC25A53]] | +0.59 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[ZNF876P]] | +0.58 | +0.45 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF39]] | -0.64 | -0.46 / -0.67 | both halves | 3e-05 |  |
| [[EHMT2]] | -0.62 | -0.40 / -0.64 | both halves | 5e-05 |  |
| [[MRPS31P4]] | -0.61 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[USP2]] | -0.59 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[ALAD]] | -0.59 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[PIP4P1]] | -0.58 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[FAM221A]] | -0.57 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[SLC11A2]] | -0.57 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[DBP]] | -0.57 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[SCRN2]] | -0.57 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[THRA]] | -0.57 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[KBTBD6]] | -0.56 | -0.38 / -0.58 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PDK1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RNF217]] | B | RNF217 activity raises PDK1-AS1's level | lines that do not express RNF217 (9) vs lines expressing it (41) | 1.47× lower at baseline in the lines without RNF217 | 0.034 | ⚠ within organs, on part of the lines; also absent: RNF217-AS1, LRP12, BEX3 |
| [[ITGA2-AS1]] | C | ITGA2-AS1 activity raises PDK1-AS1's level | lines that do not express ITGA2-AS1 (4) vs lines expressing it (46) | 1.74× lower at baseline in the lines without ITGA2-AS1 | 0.041 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYNJ2, ZNF827, NABP1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | PDK1-AS1's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | PDK1-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.491 over the table, 0.086 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.628). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (8.6, 8.3); signed map (19.0, -2.6). **Vector** length 98.4, 24.3% of its response variance represented; |z| ≥ 3 in 1,120 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +12.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.0 | +6.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +2.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.4 | -11.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.8 | -9.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.9 | -8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -21.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.5 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -5.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.5 | -3.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ITGA6 and PDK1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q31.1 — chr2:172,464,262-172,556,596 (-) |
| Ensembl biotype | lncRNA |
| Also known as | lncIHAT, AC078883.3; previously PDK1-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | prev_symbol |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40308](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40308) · Entrez [101929947](https://www.ncbi.nlm.nih.gov/gene/101929947) · Ensembl [ENSG00000225205](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225205)

## Data

Gene col 13441: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13441); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13441, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13441]; `tensor/DDL_lfc|DDL_z.npy` [13441]; `embed/gene_vectors.npy` [13441]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13441 or target_col == 13441). Every well: [[PDK1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDK1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
