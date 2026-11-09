---
symbol: "LRFN4"
type: "gene"
col: 10411
ensembl_id: "ENSG00000173621"
name: "leucine rich repeat and fibronectin type III domain containing 4"
location: "11q13.2"
module: 203
arm: "+"
pooled_cpm: 5.3
n_lines_expressing: 42
n_dd_up: 15
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/203"]
generated_by: "tahoemap"
---

# LRFN4

*leucine rich repeat and fibronectin type III domain containing 4* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.50× (z +6.7, q 1e-08, up in 3 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 2.08× (z +4.0, q 0.007, up in 13 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.312× (z -8.8, q 5e-16, down in 29 of 38 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM65]] (+0.63, fdr 7e-06), [[PAQR7]] (+0.58, fdr 2e-04), [[RILPL1]] (+0.58, fdr 1e-05); moves opposite to [[EIF2AK1]] (-0.58, fdr 1e-05), [[GOLM2]] (-0.52, fdr 2e-04), [[SCOC]] (-0.52, fdr 3e-05).
> It is in [[Module 203]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ZNF600]] → it (grade B ⚠); 6 go from it, the strongest it → [[NDUFB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10411.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.50×** | +6.7 | 1e-08 | 3/9 (NCI-H1792, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.81×** | +4.5 | 0.002 | 14/29 (A-172, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +4.3 | 0.003 | 8/22 (NCI-H1792, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +4.3 | 0.003 | 10/40 (KATO III, A-172, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +4.2 | 0.004 | 15/25 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.08×** | +4.0 | 0.007 | 13/29 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **2.03×** | +3.8 | 0.010 | 16/34 (NCI-H1792, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.92×** | +3.5 | 0.027 | 9/32 (Hs 766T, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.91×** | +3.5 | 0.027 | 7/25 (NCI-H2030, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.89×** | +3.5 | 0.030 | 12/33 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.84×** | +3.3 | 0.049 | 4/35 (SW480, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.83×** | +3.3 | 0.050 | 11/31 (LoVo, HT-29, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.79×** | +3.1 | 0.071 | 7/35 (J82, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.55×** | +3.1 | 0.082 | 6/37 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.48×** | +3.0 | 0.097 | 7/30 (HT-29, NCI-H1792, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.74×** | +3.0 | 0.097 | 6/32 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10411.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.312×** | -8.8 | 5e-16 | 29/38 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.336×** | -8.3 | 4e-14 | 30/39 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.346×** | -8.0 | 2e-13 | 33/39 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.545×** | -6.5 | 1e-08 | 22/35 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.495×** | -5.3 | 1e-05 | 24/39 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.299×** | -3.8 | 0.013 | 15/36 (A-427, hTERT-HPNE, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.618×** | -3.5 | 0.036 | 18/32 (SW1417, KATO III, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.624×** | -3.4 | 0.051 | 16/34 (NCI-H2030, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.630×** | -3.2 | 0.077 | 7/38 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.378× | -3.1 | 0.11 | 15/33 (LOX-IMVI, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.378× | -3.1 | 0.11 | 11/35 (BT-474, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10411. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.74 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -15.2) |
| [[A-427 (line)]] | wt | 9.15 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0203× (z -16.7) |
| [[MIA PaCa-2 (line)]] | alt | 8.27 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0455× (z -13.3) |
| [[SW480 (line)]] | alt | 6.50 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.102× (z -10.9) |
| [[A-172 (line)]] | wt | 11.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.109× (z -10.7) |
| [[A549 (line)]] | wt | 7.71 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 5.93 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0643× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0781× (z -17.8) |
| [[Panc 03.27 (line)]] | alt | 7.22 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -8.6) |
| [[A498 (line)]] | wt | 0.498 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.702 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.565 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10411), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM65]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[PAQR7]] | +0.58 | +0.32 / +0.70 | both halves | 2e-04 |  |
| [[RILPL1]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[NINL]] | +0.58 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[ZNF600]] | +0.56 | +0.31 / +0.59 | both halves | 2e-04 |  |
| [[OXLD1]] | +0.56 | +0.32 / +0.63 | both halves | 1e-04 |  |
| [[RPP25]] | +0.55 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[RAB11FIP3]] | +0.55 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[SEMA4C]] | +0.53 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[MEMO1]] | +0.53 | +0.49 / +0.36 | both halves | 1e-04 |  |
| [[ESRRA]] | +0.53 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[DNLZ]] | +0.53 | +0.41 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2AK1]] | -0.58 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[GOLM2]] | -0.52 | -0.30 / -0.61 | both halves | 2e-04 |  |
| [[SCOC]] | -0.52 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[ACP1]] | -0.51 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[ADD3]] | -0.50 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[MDH1]] | -0.49 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[VAMP7]] | -0.48 | -0.37 / -0.43 | both halves | 9e-05 |  |
| [[SAR1B]] | -0.48 | -0.26 / -0.57 | both halves | 4e-04 |  |
| [[MAGT1]] | -0.48 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[SRP9]] | -0.47 | -0.23 / -0.56 | both halves | 5e-04 |  |
| [[DYNC1LI2]] | -0.47 | -0.29 / -0.50 | both halves | 3e-04 |  |
| [[TPGS2]] | -0.47 | -0.27 / -0.43 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF600]] | B | ZNF600 activity lowers LRFN4's level | lines that do not express ZNF600 (9) vs lines expressing it (41) | 1.50× higher at baseline in the lines without ZNF600 | 0.067 | ⚠ within organs, on part of the lines; also absent: ZNF320, ZNF28, ZNF468 |
| [[HDAC6]] | B | HDAC6 activity raises LRFN4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PRELID3A]] | C | PRELID3A activity raises LRFN4's level | lines that do not express PRELID3A (3) vs lines expressing it (47) | 2.99× lower at baseline in the lines without PRELID3A | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, HCN2, USP31; its own permutation p |
| [[ANKRD13B]] | C | ANKRD13B activity raises LRFN4's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 1.69× lower at baseline in the lines without ANKRD13B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDUFB2]] | B | LRFN4 activity raises NDUFB2's level | lines that do not express LRFN4 (8) vs lines expressing it (42) | 1.29× lower at baseline in the lines without LRFN4 | 0.012 | ⚠ within organs, on part of the lines; also absent: OTULINL, TCEAL3 |
| [[MRPL32]] | B | LRFN4 activity raises MRPL32's level | lines that do not express LRFN4 (8) vs lines expressing it (42) | 1.21× lower at baseline in the lines without LRFN4 | 0.015 | ⚠ within organs, on part of the lines; also absent: OTULINL, TCEAL3 |
| [[COPRS]] | B | LRFN4 activity raises COPRS's level | lines that do not express LRFN4 (8) vs lines expressing it (42) | 1.14× lower at baseline in the lines without LRFN4 | 0.032 | ⚠ within organs, on part of the lines; also absent: OTULINL, TCEAL3 |
| [[SNHG15]] | B | LRFN4 activity raises SNHG15's level | lines that do not express LRFN4 (8) vs lines expressing it (42) | 2.03× lower at baseline in the lines without LRFN4 | 0.053 | ⚠ within organs, on part of the lines; also absent: OTULINL, TCEAL3 |
| [[TMEM30A]] | B | LRFN4 activity raises TMEM30A's level | lines that do not express LRFN4 (8) vs lines expressing it (42) | 1.21× lower at baseline in the lines without LRFN4 | 0.067 | ⚠ within organs, on part of the lines; also absent: OTULINL, TCEAL3 |
| [[ZBTB8A]] | B | LRFN4 activity raises ZBTB8A's level | lines that do not express LRFN4 (8) vs lines expressing it (42) | 1.32× lower at baseline in the lines without LRFN4 | 0.078 | ⚠ within organs, on part of the lines; also absent: OTULINL, TCEAL3 |

## Where it sits

- **Module**: [[Module 203]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-50.1, -3.6); signed map (-9.9, -6.6). **Vector** length 57.9, 10.8% of its response variance represented; |z| ≥ 3 in 670 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +0.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.8 | +2.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.7 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.5 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.5 | -3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.4 | -3.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -2.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.1 | -2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat and fibronectin type III domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,856,647-66,860,475 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3103, SALM3., FIGLER6 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Ig-like cell adhesion molecule family |
| Reactome | 3 pathways, smallest: Synaptic adhesion-like molecules; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PJG9](https://www.uniprot.org/uniprotkb/Q6PJG9) (Leucine-rich repeat and fibronectin type-III domain-containing protein 4):

> Promotes neurite outgrowth in hippocampal neurons. May play a role in redistributing DLG4 to the cell periphery (By similarity).

**Summary**, from NCBI Gene [78999](https://www.ncbi.nlm.nih.gov/gene/78999):

> Predicted to be involved in regulation of postsynaptic density assembly; regulation of presynapse assembly; and synaptic membrane adhesion. Predicted to be located in plasma membrane. Predicted to be active in cell surface; glutamatergic synapse; and postsynaptic density membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28456](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28456) · Entrez [78999](https://www.ncbi.nlm.nih.gov/gene/78999) · UniProt [Q6PJG9](https://www.uniprot.org/uniprotkb/Q6PJG9) · Ensembl [ENSG00000173621](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173621)

## Data

Gene col 10411: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10411); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10411, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10411]; `tensor/DDL_lfc|DDL_z.npy` [10411]; `embed/gene_vectors.npy` [10411]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10411 or target_col == 10411). Every well: [[LRFN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRFN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
