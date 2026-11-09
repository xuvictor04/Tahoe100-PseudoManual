---
symbol: "FAM120B"
type: "gene"
col: 3383
ensembl_id: "ENSG00000112584"
name: "family with sequence similarity 120 member B"
location: "6q27"
module: 45
arm: "-"
pooled_cpm: 115.24
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# FAM120B

*family with sequence similarity 120 member B* — 6q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.35× (z +4.8, q 6e-04, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.465× (z -11.2, q 3e-26, down in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.399× (z -7.6, q 2e-12, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP3K7]] (+0.64, fdr 9e-06), [[GON4L]] (+0.63, fdr 7e-06), [[GPATCH2L]] (+0.62, fdr 1e-05); moves opposite to [[CXADR]] (-0.62, fdr 1e-05), [[CYB5A]] (-0.59, fdr 1e-05), [[PRKAR2B]] (-0.58, fdr 2e-05).
> It sits in the **-** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3383.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.35×** | +4.8 | 6e-04 | 35/48 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +4.8 | 6e-04 | 31/48 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.5 | 0.001 | 28/48 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.18× | +3.7 | 0.027 | 24/49 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.063 | 22/48 (SHP-77, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.19 | 18/48 (A-427, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3383.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.465×** | -11.2 | 3e-26 | 44/49 (SW48, SW480, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.511×** | -10.6 | 5e-24 | 44/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.494×** | -10.0 | 4e-21 | 40/44 (C-33 A, J82, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.498×** | -9.9 | 9e-21 | 43/47 (HepG2/C3A, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.526×** | -9.4 | 6e-19 | 40/45 (hTERT-HPNE, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.399×** | -7.6 | 2e-12 | 47/49 (PANC-1, C32, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.606×** | -7.1 | 1e-10 | 38/48 (NCI-H2030, NCI-H1792, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.449×** | -6.6 | 2e-09 | 35/48 (C32, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.670×** | -6.3 | 1e-08 | 37/48 (LS 180, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.682×** | -5.6 | 1e-06 | 32/48 (AN3 CA, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.849× | -3.7 | 0.013 | 19/48 (AsPC-1, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.802×** | -3.1 | 0.082 | 21/47 (HepG2/C3A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~92% of this change | **0.822×** | -3.1 | 0.082 | 23/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3383. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 206 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.287× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.196× (z -11.9) |
| [[SW480 (line)]] | alt | 132 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.531× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 85.1 | 2 (1 ⚠) | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.9) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.268× (z -15.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 96.3 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.241× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.333× (z -10.3) |
| [[C32 (line)]] | wt | 149 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -13.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.360× (z -10.4) |
| [[H4 (line)]] | wt | 125 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.176× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.172× (z -8.5) |
| [[J82 (line)]] | alt | 98.8 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -19.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 154 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.275× (z -15.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 113 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.338× (z -12.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 147 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -15.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 148 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.261× (z -14.6) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 124 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.331× (z -10.8) ⚠ toxic |
| [[SW1417 (line)]] | alt | 98.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -14.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 116 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.207× (z -8.8) |
| [[HCT15 (line)]] | alt | 192 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -14.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 115 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.202× (z -17.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 127 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -10.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 98.6 | 0 | 3 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.380× (z -10.0) ⚠ transcription drop; cell-cycle shift, explains ~92% of this change |
| [[SW48 (line)]] | wt | 125 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0330× (z -23.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 131 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -20.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -12.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 140 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.169× (z -14.7) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 106 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 0.05 µM 0.355× (z -10.3) |
| [[SHP-77 (line)]] | alt | 141 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 181 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -14.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -14.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 73.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.327× (z -9.0) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 169 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.129× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 86.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.376× (z -9.4) ⚠ cell-cycle shift, explains ~43% of this change |
| [[COLO 205 (line)]] | alt | 94.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.264× (z -11.7) ⚠ toxic |
| [[HS-578T (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 89.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.439× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.412× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.0994× (z -13.1) |
| [[RKO (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.372× (z -9.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 132 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 79.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 151 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3383), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K7]] | +0.64 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[GON4L]] | +0.63 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[GPATCH2L]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[TTC17]] | +0.61 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[PDCD6]] | +0.61 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[MIATNB]] | +0.60 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[GOSR2]] | +0.59 | +0.56 / +0.64 | both halves | 1e-05 | same gene group |
| [[SENP5]] | +0.59 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[PRR14L]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ATG7]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[TMEM11-DT]] | +0.57 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[TTLL3]] | +0.57 | +0.49 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXADR]] | -0.62 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[CYB5A]] | -0.59 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[PRKAR2B]] | -0.58 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[THRA]] | -0.58 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[TM7SF3]] | -0.57 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[EHMT2]] | -0.56 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[TMEM185A]] | -0.56 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[SLC25A12]] | -0.55 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[SLC25A30]] | -0.55 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[SMG7]] | -0.55 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[SLC44A2]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[KCTD3]] | -0.55 | -0.53 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers FAM120B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **-** arm (projection on the module's main direction -0.607). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-13.8, 1.4); signed map (-19.0, -0.2). **Vector** length 88.7, 28.8% of its response variance represented; |z| ≥ 3 in 961 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.3 | +1.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | -1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.7 | -1.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.7 | +0.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.5 | -10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.8 | -11.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.7 | -9.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.7 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.4 | -9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | +1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.2 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -6.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 120 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q27 — chr6:170,290,703-170,407,067 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PGCC1, CCPG, SAN1; previously KIAA1838 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; PIN-like domain superfamily |
| Reactome | 5 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; Adipogenesis; PPARA activates gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EK7](https://www.uniprot.org/uniprotkb/Q96EK7) (Constitutive coactivator of peroxisome proliferator-activated receptor gamma):

> Functions as a transactivator of PPARG and ESR1. Functions in adipogenesis through PPARG activation (By similarity).

**Summary**, from NCBI Gene [84498](https://www.ncbi.nlm.nih.gov/gene/84498):

> Predicted to be involved in fat cell differentiation and peroxisome proliferator activated receptor signaling pathway. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21109](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21109) · Entrez [84498](https://www.ncbi.nlm.nih.gov/gene/84498) · UniProt [Q96EK7](https://www.uniprot.org/uniprotkb/Q96EK7) · Ensembl [ENSG00000112584](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112584)

## Data

Gene col 3383: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3383); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3383, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3383]; `tensor/DDL_lfc|DDL_z.npy` [3383]; `embed/gene_vectors.npy` [3383]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3383 or target_col == 3383). Every well: [[FAM120B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM120B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
