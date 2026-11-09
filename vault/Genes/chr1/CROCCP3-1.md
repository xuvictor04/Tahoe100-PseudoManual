---
symbol: "CROCCP3-1"
type: "gene"
col: 16515
ensembl_id: "ENSG00000290842"
name: ""
location: ""
module: 2
arm: "+"
pooled_cpm: 11.49
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 10
direction_downstream: 1
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CROCCP3-1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.380× (z -16.3, q 0e+00, down in 38 of 44 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.415× (z -10.4, q 3e-23, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CROCCP3]] (+0.78, fdr 7e-06, ⚠ same locus), [[SLC41A3]] (+0.67, fdr 7e-06), [[BCAP31]] (+0.63, fdr 1e-05), [[ITGB1BP1]] (+0.60, fdr 1e-05); moves opposite to [[PTPRR]] (-0.58, fdr 1e-05), [[ARHGEF38]] (-0.57, fdr 1e-05), [[PLCH1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[CASP10]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CDC42BPB]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16515.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.33× | +3.3 | 0.39 | 7/44 (SW48, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.31× | +3.2 | 0.39 | 8/45 (HT-29, AN3 CA, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16515.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.380×** | -16.3 | 0e+00 | 38/44 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.304×** | -13.6 | 1e-39 | 38/45 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.415×** | -10.4 | 3e-23 | 32/45 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.437×** | -9.8 | 1e-20 | 37/47 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.493×** | -8.4 | 5e-15 | 33/43 (SK-MEL-2, PANC-1, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.819×** | -8.2 | 2e-14 | 34/47 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.542×** | -7.3 | 3e-11 | 23/45 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.550×** | -6.8 | 6e-10 | 27/39 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.399×** | -5.7 | 7e-07 | 26/46 (NCI-H23, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.430×** | -5.2 | 9e-06 | 21/44 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.651×** | -5.1 | 2e-05 | 26/46 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.666×** | -4.8 | 7e-05 | 24/46 (NCI-H1573, SK-MEL-2, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.667×** | -4.8 | 7e-05 | 23/46 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.696×** | -4.3 | 7e-04 | 20/46 (PANC-1, SK-MEL-2, …) | two highest doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.522×** | -4.0 | 0.002 | 17/42 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.731×** | -3.7 | 0.007 | 15/46 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.748×** | -3.2 | 0.040 | 18/46 (SK-MEL-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.772×** | -3.1 | 0.066 | 8/47 (A-172, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16515. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 18.6 | 0 | 7 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0381× (z -17.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -10.5) |
| [[PANC-1 (line)]] | alt | 16.9 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0712× (z -20.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -12.4) |
| [[A-427 (line)]] | wt | 22.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -13.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.194× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 22.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -16.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.221× (z -11.0) |
| [[J82 (line)]] | alt | 13.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0993× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -9.6) |
| [[HS-578T (line)]] | alt | 15.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 8.21 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0997× (z -13.0) |
| [[A-172 (line)]] | wt | 13.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -11.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A549 (line)]] | wt | 11.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -14.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[C-33 A (line)]] | alt | 34.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 12.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.1) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H1573 (line)]] | alt | 16.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0831× (z -14.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.208× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 22.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -13.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SK-MEL-2 (line)]] | alt | 15.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0356× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SNU-1 (line)]] | wt | 16.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -9.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.106× (z -8.7) |
| [[A498 (line)]] | wt | 6.02 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -8.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[C32 (line)]] | wt | 9.81 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0890× (z -9.8) |
| [[Hs 766T (line)]] | wt | 9.20 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -9.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[hTERT-HPNE (line)]] | wt | 8.56 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0677× (z -8.9) |
| [[LS 180 (line)]] | wt | 9.23 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 8.47 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.110× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -8.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW48 (line)]] | wt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0864× (z -10.1) |
| [[AN3 CA (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16515), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP3]] | +0.78 | +0.73 / +0.81 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SLC41A3]] | +0.67 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[BCAP31]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[ITGB1BP1]] | +0.60 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[PACS2]] | +0.59 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[BCL7C]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[STX2]] | +0.58 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[CRLF3]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[CTNNBIP1]] | +0.57 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[PPM1F]] | +0.57 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[TSPAN17]] | +0.57 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[MAPK1]] | +0.57 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[TTC7B]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRR]] | -0.58 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[ARHGEF38]] | -0.57 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[PLCH1]] | -0.57 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[RASSF6]] | -0.57 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[EFNA1]] | -0.55 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[TNFRSF14-AS1]] | -0.54 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[IKBKE]] | -0.53 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[METTL25B]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[TRAFD1]] | -0.51 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[TMPRSS3]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[TMEM205]] | -0.51 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[PDZK1IP1]] | -0.51 | -0.46 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASP10]] | B | CASP10 activity lowers CROCCP3-1's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 1.58× higher at baseline in the lines without CASP10 | 0.011 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[BDKRB2]] | B | BDKRB2 activity weakens CROCCP3-1's drug response | lines that do not express BDKRB2 (18) vs lines expressing it (29) | the lines without BDKRB2 respond 1.54× as strongly (z diff -1.80); strongest at Harringtonine 0.5 µM: 0.37x vs 0.64x (z diff -2.8) | 0.014 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003; target measured in part of the lines; artifact flags |
| [[BDKRB2]] | B | BDKRB2 activity lowers CROCCP3-1's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 1.66× higher at baseline in the lines without BDKRB2 | 0.018 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[RASSF6]] | B | RASSF6 activity lowers CROCCP3-1's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 1.57× higher at baseline in the lines without RASSF6 | 0.025 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[PTPRB]] | B | PTPRB activity lowers CROCCP3-1's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 1.44× higher at baseline in the lines without PTPRB | 0.034 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[LNX1]] | B | LNX1 activity weakens CROCCP3-1's drug response | lines that do not express LNX1 (20) vs lines expressing it (27) | the lines without LNX1 respond 1.32× as strongly (z diff -1.15); strongest at Harringtonine 5 µM: 0.19x vs 0.33x (z diff -2.5) | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8; target measured in part of the lines; artifact flags |
| [[TNFRSF14-AS1]] | B | TNFRSF14-AS1 activity lowers CROCCP3-1's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 1.45× higher at baseline in the lines without TNFRSF14-AS1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[GNAZ]] | B | GNAZ activity raises CROCCP3-1's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.32× lower at baseline in the lines without GNAZ | 0.074 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[ETS2]] | B | ETS2 activity lowers CROCCP3-1's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 1.77× higher at baseline in the lines without ETS2 | 0.079 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[TNFRSF14-AS1]] | B | TNFRSF14-AS1 activity weakens CROCCP3-1's drug response | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (24) | the lines without TNFRSF14-AS1 respond 1.39× as strongly (z diff -1.30); strongest at Harringtonine 0.5 µM: 0.41x vs 0.66x (z diff -2.5) | 0.093 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB; target measured in part of the lines; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC42BPB]] | C | CROCCP3-1's natural level strengthens CDC42BPB's drug response | CROCCP3-1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.22; direction not clear | 0.054 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.522). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-5.2, -22.6); signed map (-45.8, -5.8). **Vector** length 65.8, 11.3% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.8 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +1.8 | +1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +0.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.1 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.1 | -1.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.3 | -13.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -5.1 | -16.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -10.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.0 | -7.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | +1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.5 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -1.1 |

## What is on record

> [!warning] No registry record
> CROCCP3-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16515: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16515); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16515, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16515]; `tensor/DDL_lfc|DDL_z.npy` [16515]; `embed/gene_vectors.npy` [16515]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16515 or target_col == 16515). Every well: [[CROCCP3-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CROCCP3-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
