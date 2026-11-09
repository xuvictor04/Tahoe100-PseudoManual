---
symbol: "HSPBP1"
type: "gene"
col: 5435
ensembl_id: "ENSG00000133265"
name: "HSPA (Hsp70) binding protein 1"
location: "19q13.42"
module: 4
arm: "+"
pooled_cpm: 15.73
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# HSPBP1

*HSPA (Hsp70) binding protein 1* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.20× (z +12.4, q 1e-32, up in 32 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.49× (z +6.2, q 4e-08, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.721× (z -5.2, q 6e-05, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX10]] (+0.69, fdr 7e-06), [[DUS3L]] (+0.66, fdr 7e-06), [[TRMT1]] (+0.63, fdr 7e-06); moves opposite to [[LACTB]] (-0.49, fdr 3e-05), [[HOTAIRM1]] (-0.49, fdr 3e-05), [[ING2]] (-0.48, fdr 3e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5435.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.20×** | +12.4 | 1e-32 | 32/40 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +12.1 | 2e-31 | 19/25 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +9.8 | 2e-20 | 24/32 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.71×** | +8.4 | 7e-15 | 35/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.70×** | +8.3 | 1e-14 | 30/46 (NCI-H460, LoVo, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +6.7 | 2e-09 | 26/41 (KATO III, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +6.2 | 4e-08 | 26/47 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +6.0 | 1e-07 | 27/47 (PANC-1, A-427, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +5.4 | 5e-06 | 24/47 (SW1417, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.40×** | +5.3 | 7e-06 | 22/46 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +5.1 | 2e-05 | 21/47 (HT-29, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.34×** | +4.6 | 2e-04 | 18/43 (NCI-H2347, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.21×** | +4.1 | 0.002 | 9/48 (NCI-H460, HS-578T, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.64×** | +4.1 | 0.002 | 12/47 (RPMI-7951, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.40×** | +3.8 | 0.007 | 10/44 (LOX-IMVI, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.54×** | +3.6 | 0.012 | 9/41 (A498, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.6 | 0.012 | 14/48 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.015 | 10/45 (NCI-H460, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.52×** | +3.4 | 0.017 | 5/45 (NCI-H460, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.51×** | +3.4 | 0.017 | 8/46 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 1.14× | +3.0 | 0.070 | 8/48 (HS-578T, RPMI-7951, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.30×** | +2.9 | 0.070 | 6/45 (A498, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5435.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.721×** | -5.2 | 6e-05 | 25/48 (HEC-1-A, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.707×** | -5.2 | 6e-05 | 22/46 (HOP62, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.834× | -4.1 | 0.008 | 17/48 (A498, SK-MEL-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.786×** | -3.8 | 0.020 | 18/47 (Panc 03.27, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.790×** | -3.5 | 0.047 | 14/46 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.805×** | -3.4 | 0.054 | 11/46 (CHP-212, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.802×** | -3.2 | 0.086 | 6/47 (SW 1271, NCI-H23, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.676×** | -3.2 | 0.086 | 10/48 (NCI-H23, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 0.812× | -3.1 | 0.11 | 15/46 (SHP-77, NCI-H2030, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | 0.827× | -3.0 | 0.14 | 15/45 (C-33 A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5435. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 18.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.42× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 22.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.99× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 16.6 | 0 | 1 | — | [[Vortioxetine (drug)]] 0.5 µM 0.0607× (z -8.5) |
| [[HCT15 (line)]] | alt | 16.5 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.149× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 9.42 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0797× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -13.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 12.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW48 (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0885× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5435), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX10]] | +0.69 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[DUS3L]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[TRMT1]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 | STRING 536 |
| [[POLR1A]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 | STRING 741 |
| [[TIMM50]] | +0.61 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[ARMC6]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[SARS2]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[MRPS27]] | +0.60 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[WARS2]] | +0.60 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[DHX37]] | +0.59 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[WDR18]] | +0.59 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[INO80]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LACTB]] | -0.49 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[HOTAIRM1]] | -0.49 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ING2]] | -0.48 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[HYCC2]] | -0.48 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[SMIM14]] | -0.47 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[FGFR1OP2]] | -0.47 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[HABP4]] | -0.47 | -0.51 / -0.44 | both halves | 3e-05 | STRING 521 |
| [[ARL6IP4]] | -0.47 | -0.40 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises HSPBP1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises HSPBP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.511). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-14.6, -33.1); signed map (1.1, -46.6). **Vector** length 62.3, 10.1% of its response variance represented; |z| ≥ 3 in 761 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.0 | +12.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +6.0 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.2 | -5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -4.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.0 | -5.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.9 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[Cyclosporin A (drug)]] 5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | HSPA (Hsp70) binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,262,223-55,280,381 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FES1 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZL4](https://www.uniprot.org/uniprotkb/Q9NZL4) (Hsp70-binding protein 1):

> Inhibits HSPA1A chaperone activity by changing the conformation of the ATP-binding domain of HSPA1A and interfering with ATP binding. Interferes with ubiquitination mediated by STUB1 and inhibits chaperone-assisted degradation of immature CFTR.

**Summary**, from NCBI Gene [23640](https://www.ncbi.nlm.nih.gov/gene/23640):

> Enables molecular sequestering activity and ubiquitin protein ligase binding activity. Involved in positive regulation of proteasomal ubiquitin-dependent protein catabolic process and positive regulation of protein ubiquitination. Is active in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24989) · Entrez [23640](https://www.ncbi.nlm.nih.gov/gene/23640) · UniProt [Q9NZL4](https://www.uniprot.org/uniprotkb/Q9NZL4) · Ensembl [ENSG00000133265](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133265)

## Data

Gene col 5435: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5435); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5435, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5435]; `tensor/DDL_lfc|DDL_z.npy` [5435]; `embed/gene_vectors.npy` [5435]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5435 or target_col == 5435). Every well: [[HSPBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
