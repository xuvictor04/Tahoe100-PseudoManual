---
symbol: "CPSF6"
type: "gene"
col: 3244
ensembl_id: "ENSG00000111605"
name: "cleavage and polyadenylation specific factor 6"
location: "12q15"
module: 20
arm: "+"
pooled_cpm: 112.88
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# CPSF6

*cleavage and polyadenylation specific factor 6* — 12q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.67× (z +9.8, q 8e-20, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.780× (z -4.8, q 9e-04, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (SK-MEL-2 0.456×, HEC-1-A 0.556×, CHP-212 0.345×, SW480 0.589×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[DT-061 (drug)]] 5 µM in 1 line (CHP-212 0.0892×); [[Cabozantinib (S-malate) (drug)]] 0.5 µM in 1 line (SW 1088 0.0729×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPA3]] (+0.69, fdr 1e-05), [[DCAF16]] (+0.68, fdr 7e-06), [[CTC1]] (+0.66, fdr 1e-05); moves opposite to [[NRBF2]] (-0.70, fdr 7e-06), [[CCDC174]] (-0.67, fdr 7e-06), [[MED19]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PODXL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3244.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +9.8 | 8e-20 | 42/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +8.8 | 6e-16 | 40/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +8.3 | 2e-14 | 43/47 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +7.6 | 3e-12 | 41/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +6.9 | 7e-10 | 38/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +6.5 | 1e-08 | 33/45 (A549, LS 180, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +6.4 | 1e-08 | 33/44 (SHP-77, LoVo, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +6.1 | 7e-08 | 33/49 (A549, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +5.4 | 3e-06 | 33/48 (A-427, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +5.2 | 1e-05 | 27/48 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +4.4 | 4e-04 | 32/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +4.0 | 0.003 | 26/48 (SW48, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.23×** | +4.0 | 0.003 | 25/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.006 | 22/48 (A-427, SHP-77, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.7 | 0.007 | 0/50 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.009 | 25/49 (KATO III, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3244.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (SK-MEL-2 0.456×, HEC-1-A 0.556×, CHP-212 0.345×, SW480 0.589×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[DT-061 (drug)]] 5 µM in 1 line (CHP-212 0.0892×); [[Cabozantinib (S-malate) (drug)]] 0.5 µM in 1 line (SW 1088 0.0729×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.780×** | -4.8 | 9e-04 | 38/48 (LS 180, A-427, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.859× | -4.2 | 0.007 | 21/49 (SK-MEL-2, HEC-1-A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.807×** | -4.1 | 0.007 | 26/48 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM |  | 0.838× | -3.4 | 0.073 | 21/49 (SW480, KATO III, …) | all doses, flat |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 5 µM |  | 0.838× | -3.4 | 0.073 | 15/48 (NCI-H2347, A-427, …) | all doses, flat |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.849× | -3.2 | 0.15 | 16/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3244. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 135 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +13.2) | — |
| [[KATO III (line)]] | alt | 87.4 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.58× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +10.0) | — |
| [[LoVo (line)]] | wt | 142 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +11.1) | — |
| [[CHP-212 (line)]] | wt | 154 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[DT-061 (drug)]] 5 µM 0.0892× (z -9.7) |
| [[LS 180 (line)]] | wt | 112 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +12.2) | — |
| [[SHP-77 (line)]] | alt | 163 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.15× (z +8.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 93.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 72.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[COLO 205 (line)]] | alt | 71.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 105 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.35× (z +10.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.602× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 109 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1573 (line)]] | alt | 107 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 86.5 | 0 | 1 | — | [[Cabozantinib (S-malate) (drug)]] 0.5 µM 0.0729× (z -9.7) |
| [[SW480 (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.589× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 84.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 158 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 99.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 164 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 113 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 85.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 126 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 154 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 130 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3244), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPA3]] | +0.69 | +0.55 / +0.71 | both halves | 1e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 428 |
| [[DCAF16]] | +0.68 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[CTC1]] | +0.66 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[PABIR2]] | +0.65 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[RPSA]] | +0.63 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[NUDT3]] | +0.63 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[SEH1L]] | +0.62 | +0.59 / +0.65 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[MAT2A]] | +0.62 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[RPS3A]] | +0.61 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[QSOX2]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[DHFR]] | +0.60 | +0.36 / +0.75 | both halves | 9e-05 |  |
| [[LENG8]] | +0.60 | +0.51 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRBF2]] | -0.70 | -0.61 / -0.71 | both halves | 7e-06 |  |
| [[CCDC174]] | -0.67 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[MED19]] | -0.66 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[C14orf119]] | -0.64 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[KBTBD4]] | -0.64 | -0.44 / -0.68 | both halves | 3e-05 |  |
| [[TBCC]] | -0.63 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[ING2]] | -0.62 | -0.47 / -0.69 | both halves | 2e-05 |  |
| [[CPT2]] | -0.61 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[PPCS]] | -0.61 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[RPP25L]] | -0.61 | -0.49 / -0.68 | both halves | 1e-05 |  |
| [[SLC4A1AP]] | -0.61 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[NSMCE3]] | -0.60 | -0.57 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PODXL2]] | B | PODXL2 activity raises CPSF6's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.25× lower at baseline in the lines without PODXL2 | 0.043 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.632). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-27.8, -27.4); signed map (-27.0, -34.8). **Vector** length 113, 31.6% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Formation of the ternary complex, and subsequently, the 43S complex* (reactome, mean cos +0.50 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.9 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.4 | +6.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.6 | +8.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | +3.9 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.2 | +1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +0.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.2 | -4.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -8.2 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.7 | -2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.2 | -4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -1.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | cleavage and polyadenylation specific factor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q15 — chr12:69,239,569-69,274,358 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CFIM, HPBRII-4, HPBRII-7, CFIM68, CFIM72 |
| Gene groups (HGNC) | RNA binding motif containing; Cleavage factor Im complex subunits |
| Reactome | 15 pathways, smallest: Signaling by cytosolic FGFR1 fusion mutants; Processing of Intronless Pre-mRNAs; FGFR1 mutant receptor activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16630](https://www.uniprot.org/uniprotkb/Q16630) (Cleavage and polyadenylation specificity factor subunit 6):

> Component of the cleavage factor Im (CFIm) complex that functions as an activator of the pre-mRNA 3'-end cleavage and polyadenylation processing required for the maturation of pre-mRNA into functional mRNAs. CFIm contributes to the recruitment of multiprotein complexes on specific sequences on the pre-mRNA 3'-end, so called cleavage and polyadenylation signals (pA signals). Most pre-mRNAs contain multiple pA signals, resulting in alternative cleavage and polyadenylation (APA) producing mRNAs …

**Summary**, from NCBI Gene [11052](https://www.ncbi.nlm.nih.gov/gene/11052):

> The protein encoded by this gene is one subunit of a cleavage factor required for 3' RNA cleavage and polyadenylation processing. The interaction of the protein with the RNA is one of the earliest steps in the assembly of the 3' end processing complex and facilitates the recruitment of other processing factors. The cleavage factor complex is composed of four polypeptides. This gene encodes the 68kD subunit. It has a domain organization reminiscent of spliceosomal proteins. [provided by RefSeq, …

**Accessions** — [HGNC:13871](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13871) · Entrez [11052](https://www.ncbi.nlm.nih.gov/gene/11052) · UniProt [Q16630](https://www.uniprot.org/uniprotkb/Q16630) · Ensembl [ENSG00000111605](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111605)

## Data

Gene col 3244: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3244); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3244, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3244]; `tensor/DDL_lfc|DDL_z.npy` [3244]; `embed/gene_vectors.npy` [3244]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3244 or target_col == 3244). Every well: [[CPSF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPSF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
