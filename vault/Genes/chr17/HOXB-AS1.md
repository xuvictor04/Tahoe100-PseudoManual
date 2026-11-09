---
symbol: "HOXB-AS1"
type: "gene"
col: 13738
ensembl_id: "ENSG00000230148"
name: "HOXB cluster antisense RNA 1"
location: "17q21.32"
module: 35
arm: "+"
pooled_cpm: 7.06
n_lines_expressing: 36
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 7
direction_downstream: 9
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# HOXB-AS1

*HOXB cluster antisense RNA 1* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.60× (z +16.6, q 0e+00, up in 23 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.440× (z -10.1, q 4e-21, down in 27 of 33 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXB-AS3]] (+0.67, fdr 1e-05, ⚠ same locus), [[SPEN-AS1]] (+0.67, fdr 2e-05), [[UPK2]] (+0.67, fdr 3e-05), [[HOXB7]] (+0.67, fdr 5e-05); moves opposite to [[RRP1B]] (-0.60, fdr 5e-05), [[RPUSD1]] (-0.56, fdr 3e-04), [[PHB1]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[HOXB4]] → it (grade B ⚠); 9 go from it, the strongest it → [[HOXC8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13738.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.60×** | +16.6 | 0e+00 | 23/29 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +7.6 | 1e-11 | 16/29 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +6.6 | 8e-09 | 15/26 (LOX-IMVI, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +5.7 | 1e-06 | 12/30 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.8 | 2e-04 | 12/31 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.007 | 6/32 (C32, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.25×** | +3.9 | 0.007 | 10/32 (C32, RKO, …) | top dose only | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.035 | 9/30 (A498, H4, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.30× | +3.1 | 0.11 | 6/13 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.28× | +3.1 | 0.12 | 3/32 (SW480, C-33 A, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.41× | +3.0 | 0.12 | 2/30 (RPMI-7951, SHP-77) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.30× | +3.0 | 0.12 | 5/17 (SW1417, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13738.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.440×** | -10.1 | 4e-21 | 27/33 (C-33 A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.467×** | -9.3 | 3e-18 | 23/32 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.481×** | -9.0 | 6e-17 | 25/32 (PANC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.581×** | -6.6 | 4e-09 | 18/32 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.604×** | -6.2 | 7e-08 | 16/31 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.421×** | -5.6 | 3e-06 | 14/29 (NCI-H1573, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.637×** | -5.5 | 3e-06 | 16/33 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.686×** | -4.3 | 1e-03 | 13/30 (A498, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.558×** | -3.7 | 0.012 | 12/30 (RKO, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.743×** | -3.6 | 0.016 | 12/31 (SW480, A498, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.753×** | -3.5 | 0.027 | 11/31 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.825×** | -3.3 | 0.045 | 7/32 (NCI-H1573, H4, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.771×** | -3.2 | 0.067 | 5/32 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.774×** | -3.1 | 0.072 | 12/32 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Folic acid (drug)]] 5 µM |  | 0.838× | -3.0 | 0.091 | 5/33 (C-33 A, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13738. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 9.29 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +12.7) | [[AZD2858 (drug)]] 0.5 µM 0.0829× (z -10.1) ⚠ toxic |
| [[A498 (line)]] | wt | 14.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -13.2) ⚠ cell-cycle shift, explains ~94% of this change |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.204× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 9.02 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.156× (z -9.4) ⚠ toxic · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 0.168× (z -9.4) |
| [[A-172 (line)]] | wt | 5.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.72× (z +13.6) | — |
| [[A549 (line)]] | wt | 4.42 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0719× (z -9.0) |
| [[C-33 A (line)]] | alt | 21.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -9.3) |
| [[C32 (line)]] | wt | 14.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 3.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +8.5) | — |
| [[KATO III (line)]] | alt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 20.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +17.4) | — |
| [[RKO (line)]] | wt | 8.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.99× (z +11.2) | — |
| [[SW1417 (line)]] | alt | 8.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.59× (z +11.8) | — |
| [[SW48 (line)]] | wt | 11.5 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0943× (z -8.6) |
| [[A-427 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.998 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.990 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.975 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13738), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXB-AS3]] | +0.67 | +0.55 / +0.57 | both halves | 1e-05 | same gene group; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SPEN-AS1]] | +0.67 | +0.47 / +0.52 | both halves | 2e-05 | same gene group |
| [[UPK2]] | +0.67 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[HOXB7]] | +0.67 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[TSTD3]] | +0.67 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[C2CD5-AS1]] | +0.67 | +0.48 / +0.54 | both halves | 2e-05 | same gene group |
| [[SHOX2]] | +0.66 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[COPZ2]] | +0.65 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[LRRC8C-DT]] | +0.64 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[DICER1-AS1]] | +0.64 | +0.52 / +0.41 | both halves | 4e-05 | same gene group |
| [[ICA1L]] | +0.63 | +0.59 / +0.36 | both halves | 1e-04 |  |
| [[MALINC1]] | +0.63 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[FEZ1]] | +0.63 | +0.52 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP1B]] | -0.60 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[RPUSD1]] | -0.56 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[PHB1]] | -0.55 | -0.46 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXB4]] | B | HOXB4 activity raises HOXB-AS1's level | lines that do not express HOXB4 (12) vs lines expressing it (38) | 1.92× lower at baseline in the lines without HOXB4 | 0.026 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HOXC8]] | B | HOXC8 activity raises HOXB-AS1's level | lines that do not express HOXC8 (11) vs lines expressing it (39) | 2.23× lower at baseline in the lines without HOXC8 | 0.027 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC6, IRX5 |
| [[TNFRSF10C]] | B | TNFRSF10C activity lowers HOXB-AS1's level | lines that do not express TNFRSF10C (17) vs lines expressing it (33) | 1.75× higher at baseline in the lines without TNFRSF10C | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC01426, PTGES, C1R; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers HOXB-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[NR2F1]] | B | NR2F1 activity raises HOXB-AS1's level | lines that do not express NR2F1 (8) vs lines expressing it (42) | 2.26× lower at baseline in the lines without NR2F1 | 0.046 | ⚠ within organs, on part of the lines; also absent: NR2F1-AS1, PCDH15; maybe low, not absent |
| [[ZIC1]] | B | ZIC1 activity raises HOXB-AS1's level | lines that do not express ZIC1 (34) vs lines expressing it (16) | 1.77× lower at baseline in the lines without ZIC1 | 0.050 | ⚠ within organs, on part of the lines; also absent: PCDH18, MDGA2, DCN |
| [[HOXB2]] | C | HOXB2 activity raises HOXB-AS1's level | lines that do not express HOXB2 (21) vs lines expressing it (29) | 2.81× lower at baseline in the lines without HOXB2 | 2e-04 | ⚠ within organs, on part of the lines; also absent: HOXB-AS1, SOX2, JAKMIP2-AS1; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXC8]] | B | HOXB-AS1 activity raises HOXC8's level | lines that do not express HOXB-AS1 (14) vs lines expressing it (36) | 2.45× lower at baseline in the lines without HOXB-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: MAP1A, HOXB2, ADAMTS18 |
| [[HOXC6]] | B | HOXB-AS1 activity raises HOXC6's level | lines that do not express HOXB-AS1 (14) vs lines expressing it (36) | 2.25× lower at baseline in the lines without HOXB-AS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: MAP1A, HOXB2, ADAMTS18 |
| [[GAD1]] | B | HOXB-AS1 activity raises GAD1's level | lines that do not express HOXB-AS1 (14) vs lines expressing it (36) | 1.83× lower at baseline in the lines without HOXB-AS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: MAP1A, HOXB2, ADAMTS18 |
| [[LINC02608]] | B | HOXB-AS1 activity lowers LINC02608's level | lines that do not express HOXB-AS1 (14) vs lines expressing it (36) | 1.27× higher at baseline in the lines without HOXB-AS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: MAP1A, HOXB2, ADAMTS18 |
| [[TNFRSF10C]] | B | HOXB-AS1 activity lowers TNFRSF10C's level | lines that do not express HOXB-AS1 (14) vs lines expressing it (36) | 1.81× higher at baseline in the lines without HOXB-AS1 | 0.088 | ⚠ within organs, on part of the lines; also absent: MAP1A, HOXB2, ADAMTS18 |
| [[HOXB-AS3]] | B | HOXB-AS1 activity raises HOXB-AS3's level | lines that do not express HOXB-AS1 (14) vs lines expressing it (36) | 1.29× lower at baseline in the lines without HOXB-AS1 | 0.096 | ⚠ within organs, on part of the lines; also absent: MAP1A, HOXB2, ADAMTS18 |
| [[GOLGA8B]] | B | HOXB-AS1 activity raises GOLGA8B's level | lines that do not express HOXB-AS1 (14) vs lines expressing it (36) | 1.30× lower at baseline in the lines without HOXB-AS1 | 0.096 | ⚠ within organs, on part of the lines; also absent: MAP1A, HOXB2, ADAMTS18 |
| [[ZIC1]] | B | HOXB-AS1 activity raises ZIC1's level | lines that do not express HOXB-AS1 (14) vs lines expressing it (36) | 2.57× lower at baseline in the lines without HOXB-AS1 | 0.096 | ⚠ within organs, on part of the lines; also absent: MAP1A, HOXB2, ADAMTS18 |
| [[HOXB2]] | C | HOXB-AS1 activity raises HOXB2's level | lines that do not express HOXB-AS1 (14) vs lines expressing it (36) | 2.84× lower at baseline in the lines without HOXB-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: MAP1A, HOXB2, ADAMTS18; co-absent with the target |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.654). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (4.4, 25.5); signed map (35.8, -4.0). **Vector** length 55.9, 10.2% of its response variance represented; |z| ≥ 3 in 632 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +16.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +7.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.5 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +0.4 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.9 | -10.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -9.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.5 | -9.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.7 | -6.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -3.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | HOXB cluster antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q21.32 — chr17:48,543,551-48,551,250 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43744](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43744) · Entrez [100874362](https://www.ncbi.nlm.nih.gov/gene/100874362) · Ensembl [ENSG00000230148](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000230148)

## Data

Gene col 13738: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13738); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13738, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13738]; `tensor/DDL_lfc|DDL_z.npy` [13738]; `embed/gene_vectors.npy` [13738]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13738 or target_col == 13738). Every well: [[HOXB-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXB-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
