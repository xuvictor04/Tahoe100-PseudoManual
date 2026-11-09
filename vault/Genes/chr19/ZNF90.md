---
symbol: "ZNF90"
type: "gene"
col: 13158
ensembl_id: "ENSG00000213988"
name: "zinc finger protein 90"
location: "19p12"
module: 91
arm: "+"
pooled_cpm: 5.33
n_lines_expressing: 22
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 3
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# ZNF90

*zinc finger protein 90* — 19p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.47× (z +13.4, q 2e-38, up in 0 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.91× (z +10.2, q 3e-22, up in 9 of 19 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (PANC-1 0.183×, AN3 CA 0.0806×, Panc 03.27 0.116×, J82 0.208×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.139×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.104×; ⚠ toxic; transcription drop); [[Decitabine (drug)]] 0.5 µM in 1 line (AN3 CA 0.138×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF257]] (+0.74, fdr 7e-06), [[ZNF732]] (+0.68, fdr 7e-06), [[ZNF736]] (+0.63, fdr 3e-05); moves opposite to [[MIR22HG]] (-0.46, fdr 3e-05), [[FER1L4]] (-0.45, fdr 1e-04), [[DLGAP4]] (-0.44, fdr 3e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[ZNF682]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13158.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.47×** | +13.4 | 2e-38 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.92×** | +12.0 | 7e-31 | 0/15 | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +10.2 | 3e-22 | 9/19 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.05×** | +8.1 | 1e-13 | 13/18 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +8.0 | 1e-13 | 10/19 (PANC-1, NCI-H661, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +7.6 | 3e-12 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +7.1 | 1e-10 | 5/17 (J82, H4, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.79×** | +6.5 | 5e-09 | 15/19 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +5.9 | 2e-07 | 10/17 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +5.5 | 2e-06 | 5/19 (HOP62, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.97×** | +5.4 | 3e-06 | 0/13 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +5.2 | 1e-05 | 0/15 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.23×** | +4.7 | 1e-04 | 1/5 (PANC-1) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.52×** | +4.7 | 1e-04 | 14/18 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.44×** | +3.9 | 0.004 | 5/18 (HOP62, BT-474, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.008 | 7/18 (J82, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.008 | 7/18 (H4, J82, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.014 | 8/18 (SNU-423, J82, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.031 | 1/14 (SK-MEL-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.035 | 7/18 (J82, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +3.1 | 0.049 | 9/18 (J82, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.68×** | +3.0 | 0.052 | 8/17 (SNU-423, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.059 | 2/18 (J82, LS 180) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.44×** | +2.9 | 0.080 | 1/17 (SK-MEL-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.30×** | +2.9 | 0.080 | 1/17 (PANC-1) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13158.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (PANC-1 0.183×, AN3 CA 0.0806×, Panc 03.27 0.116×, J82 0.208×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.139×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.104×; ⚠ toxic; transcription drop); [[Decitabine (drug)]] 0.5 µM in 1 line (AN3 CA 0.138×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Malotilate (drug)]] 0.5 µM |  | 0.745× | -3.4 | 0.44 | 9/18 (AN3 CA, SK-MEL-2, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 5 µM |  | 0.829× | -3.0 | 0.52 | 1/19 (NCI-H661) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13158. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 21.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -12.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 57.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0806× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Decitabine (drug)]] 0.5 µM 0.138× (z -8.8) |
| [[H4 (line)]] | wt | 12.5 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0657× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 27.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -10.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -11.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -12.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -9.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.683 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.349 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.543 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.410 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.432 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.639 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.489 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.605 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.528 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.445 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13158), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF257]] | +0.74 | +0.68 / +0.75 | both halves | 7e-06 | same gene group |
| [[ZNF732]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 | same gene group |
| [[ZNF736]] | +0.63 | +0.46 / +0.64 | both halves | 3e-05 | same gene group |
| [[ZNF738]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 | same gene group |
| [[ZNF680]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 | same gene group |
| [[SASS6]] | +0.56 | +0.34 / +0.63 | both halves | 1e-04 |  |
| [[LIN9]] | +0.56 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[ZNF726]] | +0.55 | +0.43 / +0.56 | both halves | 3e-05 | same gene group |
| [[RBL1]] | +0.54 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[ZNF138]] | +0.54 | +0.46 / +0.53 | both halves | 3e-05 | same gene group |
| [[ZNF519]] | +0.54 | +0.35 / +0.59 | both halves | 1e-04 | same gene group |
| [[ZNF273]] | +0.54 | +0.35 / +0.63 | both halves | 1e-04 | same gene group |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR22HG]] | -0.46 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[FER1L4]] | -0.45 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[DLGAP4]] | -0.44 | -0.43 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZNF90's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF736]] | C | ZNF736 activity raises ZNF90's level | lines that do not express ZNF736 (19) vs lines expressing it (31) | 2.85× lower at baseline in the lines without ZNF736 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, C19orf18, IQCA1; co-absent with the target |
| [[ZNF682]] | C | ZNF682 activity raises ZNF90's level | lines that do not express ZNF682 (20) vs lines expressing it (30) | 3.44× lower at baseline in the lines without ZNF682 | 0.012 | ⚠ within organs, on part of the lines; also absent: ZNF93, ZNF90, SCUBE3; co-absent with the target |
| [[ZNF486]] | C | ZNF486 activity raises ZNF90's level | lines that do not express ZNF486 (22) vs lines expressing it (28) | 2.03× lower at baseline in the lines without ZNF486 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000267383, CDK15, ENSG00000287335; co-absent with the target |
| [[ZNF85]] | C | ZNF85 activity raises ZNF90's level | lines that do not express ZNF85 (17) vs lines expressing it (33) | 3.35× lower at baseline in the lines without ZNF85 | 0.031 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF66, ZNF726; co-absent with the target |
| [[ZNF726]] | C | ZNF726 activity raises ZNF90's level | lines that do not express ZNF726 (20) vs lines expressing it (30) | 2.85× lower at baseline in the lines without ZNF726 | 0.036 | ⚠ within organs, on part of the lines; also absent: SUSD5, RNF150, BVES; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF682]] | C | ZNF90 activity raises ZNF682's level | lines that do not express ZNF90 (28) vs lines expressing it (22) | 3.75× lower at baseline in the lines without ZNF90 | 0.005 | ⚠ within organs, on part of the lines; also absent: LINC02008, NRK, CARMN; co-absent with the target |
| [[ZNF486]] | C | ZNF90 activity raises ZNF486's level | lines that do not express ZNF90 (28) vs lines expressing it (22) | 2.42× lower at baseline in the lines without ZNF90 | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC02008, NRK, CARMN; co-absent with the target |
| [[ZNF726]] | C | ZNF90 activity raises ZNF726's level | lines that do not express ZNF90 (28) vs lines expressing it (22) | 2.61× lower at baseline in the lines without ZNF90 | 0.079 | ⚠ within organs, on part of the lines; also absent: LINC02008, NRK, CARMN; co-absent with the target |

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.529). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-46.6, -47.0); signed map (-41.1, -35.2). **Vector** length 33.1, 6.34% of its response variance represented; |z| ≥ 3 in 408 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Regulation of endogenous retroelements by KRAB-ZFP proteins* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | +1.4 | +3.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.3 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.3 | +1.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +1.1 | +3.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.1 | +1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.0 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +3.5 |
| fall | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.9 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -0.7 | +3.7 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.7 | -2.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.7 | +1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.7 | +1.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.6 | -1.0 |
|  | [[palbociclib (drug)]] 5 µM |  | -0.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 90 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p12 — chr19:20,077,994-20,127,076 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HTF9 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03938](https://www.uniprot.org/uniprotkb/Q03938) (Zinc finger protein 90):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7643](https://www.ncbi.nlm.nih.gov/gene/7643):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of DNA-templated transcription. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13165](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13165) · Entrez [7643](https://www.ncbi.nlm.nih.gov/gene/7643) · UniProt [Q03938](https://www.uniprot.org/uniprotkb/Q03938) · Ensembl [ENSG00000213988](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213988)

## Data

Gene col 13158: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13158); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13158, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13158]; `tensor/DDL_lfc|DDL_z.npy` [13158]; `embed/gene_vectors.npy` [13158]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13158 or target_col == 13158). Every well: [[ZNF90 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF90.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
