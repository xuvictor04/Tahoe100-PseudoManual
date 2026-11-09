---
symbol: "LOXL1-AS1"
type: "gene"
col: 15370
ensembl_id: "ENSG00000261801"
name: "LOXL1 antisense RNA 1"
location: "15q24.1"
module: 82
arm: "+"
pooled_cpm: 3.48
n_lines_expressing: 36
n_dd_up: 6
n_dd_down: 31
n_dd_up_clean: 3
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# LOXL1-AS1

*LOXL1 antisense RNA 1* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.84× (z +7.5, q 5e-11, up in 3 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Temsirolimus (drug)]] 0.5 µM: 1.35× (z +3.9, q 0.022, up in 5 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.395× (z -16.7, q 0e+00, down in 21 of 27 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LOXL1]] (+0.60, fdr 1e-05, ⚠ same locus), [[BVES]] (+0.53, fdr 3e-05), [[CROCCP3-1]] (+0.49, fdr 3e-05), [[CROCCP3]] (+0.49, fdr 6e-05); moves opposite to [[BABAM2]] (-0.49, fdr 3e-05), [[C4BPB]] (-0.45, fdr 5e-04), [[PTPRR]] (-0.44, fdr 1e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[BVES]] → it (grade B ⚠); 3 go from it, the strongest it → [[C4BPB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15370.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +7.5 | 5e-11 | 3/9 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.40×** | +3.9 | 0.022 | 2/10 (SW480, A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.022 | 5/27 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.022 | 4/31 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +3.7 | 0.024 | 2/17 (SNU-423, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.037 | 3/31 (NCI-H1792, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Pentagastrin (drug)]] 0.5 µM |  | 1.26× | +3.0 | 0.21 | 3/28 (A-172, SW48, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15370.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.395×** | -16.7 | 0e+00 | 21/27 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.317×** | -14.4 | 3e-44 | 25/31 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.376×** | -12.4 | 3e-33 | 25/31 (HOP62, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.446×** | -10.3 | 1e-22 | 22/31 (A-172, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.477×** | -9.4 | 5e-19 | 18/32 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.531×** | -7.7 | 9e-13 | 18/31 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.545×** | -7.7 | 9e-13 | 12/27 (NCI-H1792, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.554×** | -7.5 | 4e-12 | 17/31 (A549, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.327×** | -7.4 | 6e-12 | 17/28 (HOP62, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.605×** | -6.1 | 5e-08 | 13/25 (SW480, Panc 03.27, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.403×** | -6.0 | 8e-08 | 11/25 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.715×** | -6.0 | 9e-08 | 14/32 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.607×** | -6.0 | 9e-08 | 13/28 (NCI-H1792, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.620×** | -6.0 | 1e-07 | 13/31 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.628×** | -5.9 | 1e-07 | 15/24 (BT-474, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.701×** | -4.5 | 2e-04 | 10/31 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.724×** | -4.1 | 0.001 | 12/30 (HOP62, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.724×** | -4.0 | 0.002 | 8/31 (NCI-H23, PANC-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15370. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 9.13 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -13.3) |
| [[A-172 (line)]] | wt | 11.1 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.160× (z -10.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 7.56 | 0 | 3 | — | [[Bortezomib (drug)]] 0.05 µM 0.0376× (z -13.9) |
| [[PANC-1 (line)]] | alt | 4.27 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0600× (z -19.6) |
| [[LOX-IMVI (line)]] | wt | 8.92 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -14.4) |
| [[NCI-H1573 (line)]] | alt | 2.92 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0690× (z -11.6) |
| [[SNU-423 (line)]] | alt | 3.74 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0421× (z -10.0) |
| [[SW480 (line)]] | alt | 4.65 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -8.9) |
| [[A-427 (line)]] | wt | 6.30 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0989× (z -9.8) |
| [[BT-474 (line)]] | alt | 5.85 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 5.26 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0576× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 1.74 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 2.59 | 0 | 1 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.0491× (z -8.7) |
| [[SW1417 (line)]] | alt | 2.92 | 0 | 1 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 0.5 µM 0.0669× (z -9.0) |
| [[A498 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.226 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.227 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.292 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.192 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.237 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15370), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LOXL1]] | +0.60 | +0.60 / +0.51 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[BVES]] | +0.53 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[CROCCP3-1]] | +0.49 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[CROCCP3]] | +0.49 | +0.55 / +0.38 | both halves | 6e-05 |  |
| [[SEMA4F]] | +0.48 | +0.54 / +0.33 | both halves | 1e-04 |  |
| [[CACNG4]] | +0.48 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[HYKK]] | +0.48 | +0.47 / +0.24 | both halves | 5e-04 |  |
| [[SLC66A3]] | +0.48 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[CYS1]] | +0.47 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[HEYL]] | +0.47 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[MPZL1]] | +0.47 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[MTCL1]] | +0.46 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[SYT9]] | +0.45 | +0.40 / +0.37 | both halves | 9e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BABAM2]] | -0.49 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[C4BPB]] | -0.45 | -0.45 / -0.24 | both halves | 5e-04 |  |
| [[PTPRR]] | -0.44 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[GCNT3]] | -0.43 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[LMNTD1]] | -0.43 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[DNM3]] | -0.43 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[CPEB4]] | -0.42 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[HDAC8]] | -0.41 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[TMEFF2]] | -0.40 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[ALPK1]] | -0.40 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[NPSR1]] | -0.40 | -0.41 / -0.22 | both halves | 6e-04 |  |
| [[ATXN7L1]] | -0.40 | -0.46 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BVES]] | B | BVES activity raises LOXL1-AS1's level | lines that do not express BVES (19) vs lines expressing it (31) | 1.82× lower at baseline in the lines without BVES | 0.065 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2 |
| [[IGFL2]] | B | IGFL2 activity lowers LOXL1-AS1's level | lines that do not express IGFL2 (38) vs lines expressing it (12) | 1.69× higher at baseline in the lines without IGFL2 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33 |
| [[LOXL1]] | C | LOXL1 activity raises LOXL1-AS1's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 2.71× lower at baseline in the lines without LOXL1 | 0.002 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330; co-absent with the target |
| [[WIPF1]] | C | WIPF1 activity raises LOXL1-AS1's level | lines that do not express WIPF1 (16) vs lines expressing it (34) | 2.27× lower at baseline in the lines without WIPF1 | 0.029 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, GNB4, POPDC3; co-absent with the target |
| [[TSHZ3]], [[TSHZ3-AS1]] | C | TSHZ3, TSHZ3-AS1 activity raises LOXL1-AS1's level | lines that do not express TSHZ3, TSHZ3-AS1 (25) vs lines expressing them (25) | 2.36× lower at baseline in the lines without TSHZ3, TSHZ3-AS1 | 0.072 | ⚠ within organs, on part of the lines; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target; co-absent genes |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C4BPB]] | B | LOXL1-AS1 activity lowers C4BPB's level | lines that do not express LOXL1-AS1 (14) vs lines expressing it (36) | 3.60× higher at baseline in the lines without LOXL1-AS1 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BEX4, ENSG00000255330, LOXL1 |
| [[LOXL1]] | C | LOXL1-AS1 activity raises LOXL1's level | lines that do not express LOXL1-AS1 (14) vs lines expressing it (36) | 3.28× lower at baseline in the lines without LOXL1-AS1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BEX4, ENSG00000255330, LOXL1; co-absent with the target |
| [[WIPF1]] | C | LOXL1-AS1 activity raises WIPF1's level | lines that do not express LOXL1-AS1 (14) vs lines expressing it (36) | 4.74× lower at baseline in the lines without LOXL1-AS1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BEX4, ENSG00000255330, LOXL1; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.305). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.8, 46.7); signed map (-8.7, 21.8). **Vector** length 47.4, 7.32% of its response variance represented; |z| ≥ 3 in 805 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +7.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.8 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.1 | +3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | +1.1 | -1.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.1 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.7 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.7 | +0.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.5 | -9.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -2.0 | -5.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.9 | -7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -1.8 | -4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | -4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -6.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -0.9 | -3.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -0.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | LOXL1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q24.1 — chr15:73,908,071-73,928,248 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44169](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44169) · Entrez [100287616](https://www.ncbi.nlm.nih.gov/gene/100287616) · Ensembl [ENSG00000261801](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261801)

## Data

Gene col 15370: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15370); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15370, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15370]; `tensor/DDL_lfc|DDL_z.npy` [15370]; `embed/gene_vectors.npy` [15370]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15370 or target_col == 15370). Every well: [[LOXL1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LOXL1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
