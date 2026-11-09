---
symbol: "BPNT2"
type: "gene"
col: 2443
ensembl_id: "ENSG00000104331"
name: "3'(2'), 5'-bisphosphate nucleotidase 2"
location: "8q12.1"
module: 20
arm: "+"
pooled_cpm: 95.62
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# BPNT2

*3'(2'), 5'-bisphosphate nucleotidase 2* — 8q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.01× (z +9.9, q 2e-20, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.588× (z -7.0, q 2e-09, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNDC5]] (+0.79, fdr 7e-06), [[TMED7]] (+0.78, fdr 7e-06), [[RPN1]] (+0.76, fdr 7e-06); moves opposite to [[CROCCP2-1]] (-0.74, fdr 7e-06), [[PIGBOS1]] (-0.66, fdr 1e-05), [[TMEM265]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MARVELD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2443.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.01×** | +9.9 | 2e-20 | 47/49 (HEC-1-A, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.66×** | +7.0 | 8e-10 | 40/48 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +5.7 | 2e-06 | 41/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.51×** | +5.6 | 3e-06 | 34/49 (LOX-IMVI, Panc 03.27, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +5.5 | 4e-06 | 40/48 (NCI-H1792, NCI-H23, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +5.4 | 7e-06 | 30/45 (LoVo, A549, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +5.4 | 7e-06 | 41/48 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.43×** | +4.7 | 2e-04 | 25/44 (SW480, LS 180, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.20×** | +3.6 | 0.023 | 22/49 (LOX-IMVI, Panc 03.27, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.085 | 24/47 (SW480, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.085 | 23/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.1 | 0.087 | 20/37 (NCI-H1573, HS-578T, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2443.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.588×** | -7.0 | 2e-09 | 36/48 (J82, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.730×** | -6.1 | 3e-07 | 30/48 (NCI-H2030, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.712×** | -4.5 | 0.001 | 29/47 (NCI-H1573, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.765×** | -3.5 | 0.062 | 27/49 (hTERT-HPNE, HepG2/C3A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.779×** | -3.4 | 0.070 | 28/48 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.719× | -3.2 | 0.10 | 31/49 (Hs 766T, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.847× | -3.2 | 0.10 | 22/48 (A549, Hs 766T, …) | rises with dose | position effect removed |
| [[BAY1125976 (drug)]] 0.5 µM |  | 0.726× | -3.1 | 0.10 | 26/48 (LOX-IMVI, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.727× | -3.1 | 0.10 | 25/48 (SHP-77, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.796× | -3.1 | 0.10 | 25/49 (SW 1088, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2443. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 68.5 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.61× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.63× (z +8.8) | — |
| [[A-427 (line)]] | wt | 52.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.274× (z -11.4) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.486× (z -9.1) |
| [[J82 (line)]] | alt | 108 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -14.0) |
| [[LoVo (line)]] | wt | 71.5 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 92.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 114 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -9.7) |
| [[SW 1088 (line)]] | alt | 91.5 | 0 | 2 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0782× (z -9.2) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Roxadustat (drug)]] 0.5 µM 0.0877× (z -8.8) |
| [[C32 (line)]] | wt | 231 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 6.10× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 82.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 95.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.11× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -8.9) |
| [[HOP62 (line)]] | alt | 196 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -15.9) |
| [[HS-578T (line)]] | alt | 146 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.52× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 82.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -16.2) |
| [[NCI-H23 (line)]] | alt | 121 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.378× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 54.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[RKO (line)]] | wt | 133 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.23× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 113 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -9.8) |
| [[SNU-1 (line)]] | wt | 103 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -10.2) |
| [[SW 900 (line)]] | alt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -9.0) |
| [[SW480 (line)]] | alt | 57.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A-172 (line)]] | wt | 58.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 85.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 95.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 129 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 69.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2443), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC5]] | +0.79 | +0.76 / +0.83 | both halves | 7e-06 |  |
| [[TMED7]] | +0.78 | +0.76 / +0.81 | both halves | 7e-06 |  |
| [[RPN1]] | +0.76 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[TMEM30A]] | +0.74 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[EMC1]] | +0.71 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[UGGT1]] | +0.71 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[DDOST]] | +0.71 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[PDIA3]] | +0.71 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[DPAGT1]] | +0.70 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[ERMP1]] | +0.70 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[GANAB]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[CRKL]] | +0.69 | +0.75 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP2-1]] | -0.74 | -0.69 / -0.77 | both halves | 7e-06 |  |
| [[PIGBOS1]] | -0.66 | -0.51 / -0.72 | both halves | 1e-05 |  |
| [[TMEM265]] | -0.65 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[ATF4]] | -0.64 | -0.58 / -0.67 | both halves | 8e-06 |  |
| [[SMIM26]] ⚠ | -0.64 | -0.50 / -0.72 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS18C]] | -0.64 | -0.57 / -0.68 | both halves | 1e-05 |  |
| [[ZNF503]] | -0.63 | -0.58 / -0.65 | both halves | 8e-06 |  |
| [[ZNF593]] | -0.62 | -0.49 / -0.69 | both halves | 1e-05 |  |
| [[ZNF579]] | -0.61 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[PPIG]] | -0.61 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[FDX2]] | -0.61 | -0.53 / -0.65 | both halves | 1e-05 | pathway: Biological oxidations |
| [[ERVK3-1]] | -0.61 | -0.51 / -0.70 | both halves | 1e-05 |  |
| [[WASHC1]] | -0.60 | -0.55 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MARVELD3]] | B | MARVELD3 activity lowers BPNT2's level | lines that do not express MARVELD3 (28) vs lines expressing it (22) | 1.39× higher at baseline in the lines without MARVELD3 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRB3, KDF1, ESRP2 |
| [[P3H1]] | C | P3H1 activity raises BPNT2's level | lines that do not express P3H1 (4) vs lines expressing it (46) | 1.65× lower at baseline in the lines without P3H1 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEP112, TIMP2, CNTNAP1; maybe low, not absent |
| [[CRTAP]] | C | CRTAP activity raises BPNT2's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.66× lower at baseline in the lines without CRTAP | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.783). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-24.6, -22.9); signed map (-24.2, -39.6). **Vector** length 135, 44.2% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *L13a-mediated translational silencing of Ceruloplasmin expression* (reactome, mean cos +0.50 to 11); *GTP hydrolysis and joining of the 60S ribosomal subunit* (reactome, mean cos +0.50 to 11); *Eukaryotic Translation Elongation* (reactome, mean cos +0.53 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +5.8 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +5.6 | +5.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +9.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +7.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.7 | +2.6 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +2.7 | +2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +2.6 | +2.1 |
|  | [[Lopinavir (drug)]] 5 µM |  | +2.5 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.8 | -6.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.8 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -6.2 | -2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.8 | -4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.4 | -3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.1 | -3.1 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.6 | -3.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.2 | -3.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.0 | -2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.0 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | 3'(2'), 5'-bisphosphate nucleotidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.1 — chr8:56,957,931-56,993,867 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20421, IMPA3, gPAPP; previously IMPAD1 |
| Reactome | 3 pathways, smallest: Cytosolic sulfonation of small molecules; Phase II - Conjugation of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX62](https://www.uniprot.org/uniprotkb/Q9NX62) (Golgi-resident adenosine 3',5'-bisphosphate 3'-phosphatase):

> Exhibits 3'-nucleotidase activity toward adenosine 3',5'-bisphosphate (PAP), namely hydrolyzes adenosine 3',5'-bisphosphate into adenosine 5'-monophosphate (AMP) and a phosphate. May play a role in the formation of skeletal elements derived through endochondral ossification, possibly by clearing adenosine 3',5'-bisphosphate produced by Golgi sulfotransferases during glycosaminoglycan sulfation. Has no activity toward 3'-phosphoadenosine 5'-phosphosulfate (PAPS) or inositol phosphate (IP) …

**Summary**, from NCBI Gene [54928](https://www.ncbi.nlm.nih.gov/gene/54928):

> This gene encodes a member of the inositol monophosphatase family. The encoded protein is localized to the Golgi apparatus and catalyzes the hydrolysis of phosphoadenosine phosphate (PAP) to adenosine monophosphate (AMP). Mutations in this gene are a cause of GRAPP type chondrodysplasia with joint dislocations, and a pseudogene of this gene is located on the long arm of chromosome 1. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:26019](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26019) · Entrez [54928](https://www.ncbi.nlm.nih.gov/gene/54928) · UniProt [Q9NX62](https://www.uniprot.org/uniprotkb/Q9NX62) · Ensembl [ENSG00000104331](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104331)

## Data

Gene col 2443: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2443); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2443, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2443]; `tensor/DDL_lfc|DDL_z.npy` [2443]; `embed/gene_vectors.npy` [2443]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2443 or target_col == 2443). Every well: [[BPNT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BPNT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
