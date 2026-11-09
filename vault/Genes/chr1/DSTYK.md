---
symbol: "DSTYK"
type: "gene"
col: 5408
ensembl_id: "ENSG00000133059"
name: "dual serine/threonine and tyrosine protein kinase"
location: "1q32.1"
module: 3
arm: "+"
pooled_cpm: 64.01
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 7
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# DSTYK

*dual serine/threonine and tyrosine protein kinase* — 1q32.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.543× (z -15.5, q 0e+00, down in 41 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.763× (z -6.9, q 9e-10, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THAP3]] (+0.69, fdr 7e-06), [[ARL8A]] (+0.67, fdr 1e-05), [[RWDD3]] (+0.66, fdr 7e-06); moves opposite to [[HNRNPA3]] (-0.64, fdr 2e-05), [[TRIP13]] (-0.61, fdr 1e-05), [[NCBP1]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CNKSR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5408.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +4.5 | 0.004 | 17/48 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.8 | 0.038 | 12/48 (COLO 205, NCI-H1792, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.7 | 0.042 | 14/48 (hTERT-HPNE, CFPAC-1, …) | two highest doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.14× | +3.4 | 0.088 | 10/48 (AsPC-1, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.11× | +3.3 | 0.12 | 12/48 (HCT15, C32, …) | rises with dose | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.21 | 10/48 (SW480, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5408.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.543×** | -15.5 | 0e+00 | 41/49 (Panc 03.27, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.522×** | -15.3 | 0e+00 | 37/45 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.594×** | -12.7 | 8e-35 | 33/42 (A549, C-33 A, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.763×** | -6.9 | 9e-10 | 28/48 (NCI-H23, HT-29, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.757×** | -6.8 | 1e-09 | 25/47 (SHP-77, NCI-H1573, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.819×** | -6.8 | 1e-09 | 22/48 (A-172, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.596×** | -6.0 | 2e-07 | 27/49 (C32, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.847× | -4.1 | 0.003 | 18/48 (LoVo, NCI-H1792, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.854× | -4.0 | 0.004 | 17/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | 0.863× | -3.7 | 0.010 | 21/47 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.877× | -3.1 | 0.086 | 9/48 (Hs 766T, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5408. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 60.3 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -11.2) ⚠ cell-cycle shift, explains ~71% of this change |
| [[NCI-H460 (line)]] | wt | 103 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -21.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C32 (line)]] | wt | 276 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[Hs 766T (line)]] | wt | 56.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW480 (line)]] | alt | 56.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -17.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 94.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.563× (z -10.3) |
| [[C-33 A (line)]] | alt | 80.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 39.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.290× (z -10.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 78.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.388× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 49.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.419× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[NCI-H2030 (line)]] | alt | 69.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 58.4 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.358× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 79.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -23.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 56.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0732× (z -28.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[AN3 CA (line)]] | alt | 79.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[H4 (line)]] | wt | 48.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HCT15 (line)]] | alt | 49.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0970× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HepG2_C3A (line)]] | wt | 32.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -14.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 58.6 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.561× (z -9.5) |
| [[HT-29 (line)]] | alt | 30.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.344× (z -8.6) |
| [[KATO III (line)]] | alt | 40.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -12.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 43.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.366× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[NCI-H1792 (line)]] | alt | 72.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -10.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 58.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 62.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SHP-77 (line)]] | alt | 48.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.360× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 70.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW 900 (line)]] | alt | 85.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.429× (z -8.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 95.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 94.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5408), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP3]] | +0.69 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[ARL8A]] | +0.67 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[RWDD3]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[SAT2]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[CCDC126]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.65 | +0.57 / +0.65 | both halves | 9e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[LIN7B]] | +0.64 | +0.57 / +0.75 | both halves | 8e-06 |  |
| [[HEIH]] | +0.63 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[RPP21]] | +0.63 | +0.43 / +0.71 | both halves | 3e-05 |  |
| [[C15orf61]] ⚠ | +0.63 | +0.56 / +0.70 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL32]] | +0.62 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[AGO4]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[VPS37D]] | +0.61 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[C16orf87]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPA3]] | -0.64 | -0.48 / -0.69 | both halves | 2e-05 |  |
| [[TRIP13]] | -0.61 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[NCBP1]] | -0.57 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[XRCC5]] | -0.56 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[SPTLC1]] | -0.56 | -0.40 / -0.64 | both halves | 5e-05 |  |
| [[ARHGAP4]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[FAM91A1]] | -0.56 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[HNRNPA2B1]] | -0.56 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[EMC1]] | -0.55 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[SMG1P6]] | -0.55 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[RBBP7]] | -0.54 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[TPM3]] | -0.54 | -0.52 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNKSR1]] | B | CNKSR1 activity lowers DSTYK's level | lines that do not express CNKSR1 (24) vs lines expressing it (26) | 1.32× higher at baseline in the lines without CNKSR1 | 0.059 | ⚠ within organs, on part of the lines; also absent: SPINT1, SLC52A3, ESRP2 |
| [[MARVELD3]] | B | MARVELD3 activity lowers DSTYK's level | lines that do not express MARVELD3 (28) vs lines expressing it (22) | 1.39× higher at baseline in the lines without MARVELD3 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRB3, KDF1, ESRP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.464). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.9, -17.0); signed map (-22.7, 5.7). **Vector** length 99.2, 22.6% of its response variance represented; |z| ≥ 3 in 812 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.2 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.4 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.4 | +3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +3.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +0.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.0 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.8 | -15.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -5.8 | -15.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -5.1 | -12.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -6.8 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | dual serine/threonine and tyrosine protein kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:205,142,505-205,211,702 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0472, DustyPK, RIP5; previously RIPK5, SPG23 |
| Gene groups (HGNC) | DSTYK family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6XUX3](https://www.uniprot.org/uniprotkb/Q6XUX3) (Dual serine/threonine and tyrosine protein kinase):

> Acts as a positive regulator of ERK phosphorylation downstream of fibroblast growth factor-receptor activation. Involved in the regulation of both caspase-dependent apoptosis and caspase-independent cell death. In the skin, it plays a predominant role in suppressing caspase-dependent apoptosis in response to UV stress in a range of dermal cell types. Involved in normal skeletal segmentation and spine formation, via positively regulating late-stage endosomal trafficking in notochord cells (By …

**Summary**, from NCBI Gene [25778](https://www.ncbi.nlm.nih.gov/gene/25778):

> This gene encodes a dual serine/threonine and tyrosine protein kinase which is expressed in multiple tissues. It is thought to function as a regulator of cell death. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:29043](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29043) · Entrez [25778](https://www.ncbi.nlm.nih.gov/gene/25778) · UniProt [Q6XUX3](https://www.uniprot.org/uniprotkb/Q6XUX3) · Ensembl [ENSG00000133059](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133059)

## Data

Gene col 5408: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5408); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5408, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5408]; `tensor/DDL_lfc|DDL_z.npy` [5408]; `embed/gene_vectors.npy` [5408]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5408 or target_col == 5408). Every well: [[DSTYK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DSTYK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
