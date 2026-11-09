---
symbol: "SYPL1"
type: "gene"
col: 164
ensembl_id: "ENSG00000008282"
name: "synaptophysin like 1"
location: "7q22.3"
module: 29
arm: "+"
pooled_cpm: 72.57
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# SYPL1

*synaptophysin like 1* — 7q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.78× (z +10.9, q 9e-25, up in 36 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.40× (z +6.4, q 2e-08, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.578× (z -10.3, q 5e-22, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIAO2A]] (+0.57, fdr 2e-05), [[RAB14]] (+0.54, fdr 2e-05), [[STRADB]] (+0.52, fdr 5e-05); moves opposite to [[ABAT]] (-0.53, fdr 1e-05), [[SUPT6H]] (-0.53, fdr 5e-05), [[FERMT3]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 164.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +10.9 | 9e-25 | 36/49 (Hs 766T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +8.8 | 3e-16 | 38/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.56×** | +8.4 | 9e-15 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +7.6 | 5e-12 | 27/42 (Hs 766T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +7.6 | 5e-12 | 36/47 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +6.4 | 2e-08 | 34/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.34×** | +5.5 | 2e-06 | 32/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.32×** | +4.9 | 8e-05 | 25/45 (Hs 766T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.41×** | +4.6 | 2e-04 | 29/47 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.25×** | +4.1 | 0.002 | 21/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.25×** | +4.1 | 0.002 | 25/47 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.1 | 0.002 | 19/48 (J82, A549, …) | top dose only | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.9 | 0.005 | 23/48 (CFPAC-1, PANC-1, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.060 | 19/48 (LS 180, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 164.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.578×** | -10.3 | 5e-22 | 43/48 (Panc 03.27, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.581×** | -10.2 | 6e-22 | 44/48 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.662×** | -7.7 | 2e-12 | 41/48 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.765×** | -7.1 | 2e-10 | 29/48 (Hs 766T, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.805×** | -5.8 | 9e-07 | 28/48 (NCI-H2347, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.777×** | -4.7 | 2e-04 | 33/48 (Panc 03.27, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.808×** | -4.0 | 0.005 | 24/48 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.819×** | -3.8 | 0.012 | 21/48 (A549, C32, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.805×** | -3.6 | 0.017 | 24/48 (Hs 766T, A-172, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.699×** | -3.5 | 0.025 | 24/49 (A549, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 164. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 220 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +14.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -15.9) |
| [[PANC-1 (line)]] | alt | 67.2 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +14.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.97× (z +9.5) | — |
| [[LoVo (line)]] | wt | 69.0 | 1 (1 ⚠) | 3 | [[Niclosamide (olamine) (drug)]] 5 µM 2.31× (z +9.3) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -14.1) |
| [[LS 180 (line)]] | wt | 88.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 77.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.381× (z -11.2) |
| [[A-172 (line)]] | wt | 74.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.454× (z -8.9) |
| [[A498 (line)]] | wt | 115 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.426× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 87.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.491× (z -9.8) |
| [[SW480 (line)]] | alt | 64.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.482× (z -9.4) |
| [[A-427 (line)]] | wt | 58.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 104 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.473× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 76.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +8.5) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 60.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -10.0) |
| [[J82 (line)]] | alt | 49.8 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.93× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 93.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.22× (z +8.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 70.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 56.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.365× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 56.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 59.9 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.88× (z +9.8) ⚠ toxic | — |
| [[RPMI-7951 (line)]] | alt | 50.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 74.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 57.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 175 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 89.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 99.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 164), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAO2A]] | +0.57 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[RAB14]] | +0.54 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[STRADB]] | +0.52 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[AK3]] | +0.52 | +0.30 / +0.42 | both halves | 2e-04 |  |
| [[CIPC]] | +0.51 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[DCK]] | +0.51 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[PPM1A]] | +0.51 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[RYK]] | +0.51 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[GSTK1]] | +0.50 | +0.31 / +0.55 | both halves | 2e-04 |  |
| [[FDX1]] | +0.50 | +0.60 / +0.21 | both halves | 6e-04 |  |
| [[RNF138]] | +0.50 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[DR1]] | +0.49 | +0.37 / +0.51 | both halves | 9e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABAT]] | -0.53 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[SUPT6H]] | -0.53 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[FERMT3]] | -0.50 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[CSNK1A1]] | -0.50 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[FER1L4]] | -0.49 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[DAP3]] | -0.47 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[ZNF432]] | -0.47 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[CFAP251]] | -0.46 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[TBC1D22A]] | -0.46 | -0.29 / -0.23 | both halves | 5e-04 |  |
| [[SAP30BP]] | -0.46 | -0.47 / -0.24 | both halves | 4e-04 |  |
| [[SAMD4B]] | -0.46 | -0.32 / -0.39 | both halves | 1e-04 |  |
| [[FAM219A]] | -0.46 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises SYPL1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises SYPL1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.482). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-13.1, 14.1); signed map (-19.4, -39.4). **Vector** length 77.0, 17.8% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.1 | +4.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +8.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.4 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +10.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | -0.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +0.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +4.6 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +1.6 | +1.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.5 | -0.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | -4.3 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -2.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.6 | -7.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -0.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -1.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | synaptophysin like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.3 — chr7:106,090,505-106,112,589 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SYPL |
| Gene groups (HGNC) | Synaptophysins; MARVEL domain containing |
| Matched by | ensembl_id |

UniProt [Q16563](https://www.uniprot.org/uniprotkb/Q16563) carries no function annotation.

**Summary**, from NCBI Gene [6856](https://www.ncbi.nlm.nih.gov/gene/6856):

> Predicted to be involved in chemical synaptic transmission. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11507](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11507) · Entrez [6856](https://www.ncbi.nlm.nih.gov/gene/6856) · UniProt [Q16563](https://www.uniprot.org/uniprotkb/Q16563) · Ensembl [ENSG00000008282](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008282)

## Data

Gene col 164: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 164); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 164, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 164]; `tensor/DDL_lfc|DDL_z.npy` [164]; `embed/gene_vectors.npy` [164]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 164 or target_col == 164). Every well: [[SYPL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYPL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
