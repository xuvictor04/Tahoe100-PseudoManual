---
symbol: "NAPRT"
type: "gene"
col: 7223
ensembl_id: "ENSG00000147813"
name: "nicotinate phosphoribosyltransferase"
location: "8q24.3"
module: 1
arm: "+"
pooled_cpm: 5.81
n_lines_expressing: 41
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# NAPRT

*nicotinate phosphoribosyltransferase* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.97× (z +13.4, q 4e-38, up in 10 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 1.82× (z +4.3, q 0.002, up in 13 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.698× (z -5.1, q 1e-04, down in 18 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.246×); [[Clotrimazole (drug)]] 0.5 µM in 1 line (HS-578T 0.0693×); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.0946×; ⚠ toxic); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (RKO 0.0938×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CISD3]] (+0.58, fdr 3e-05), [[MLST8]] (+0.57, fdr 3e-05), [[PWWP2B]] (+0.57, fdr 2e-05); moves opposite to [[MESD]] (-0.57, fdr 4e-05), [[GLUD1P3]] (-0.55, fdr 4e-05), [[NUCB2]] (-0.49, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EPPK1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MROH6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7223.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.97×** | +13.4 | 4e-38 | 10/10 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.97×** | +11.0 | 1e-25 | 21/21 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.82×** | +9.7 | 8e-20 | 11/16 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.82×** | +4.3 | 0.002 | 13/31 (SW1417, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +4.3 | 0.002 | 9/25 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.77×** | +4.1 | 0.004 | 9/33 (Hs 766T, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.0 | 0.006 | 11/26 (NCI-H2030, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.023 | 6/36 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +3.4 | 0.041 | 2/16 (SW1417, SW480) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.093 | 6/36 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.1 | 0.093 | 6/26 (HCT15, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +3.1 | 0.099 | 5/25 (AsPC-1, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (drug)]] 0.05 µM |  | 1.38× | +3.0 | 0.11 | 5/32 (HEC-1-A, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7223.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.246×); [[Clotrimazole (drug)]] 0.5 µM in 1 line (HS-578T 0.0693×); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.0946×; ⚠ toxic); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (RKO 0.0938×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -5.1 | 1e-04 | 18/32 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.669×** | -4.1 | 0.013 | 10/37 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.527× | -3.4 | 0.13 | 12/33 (PANC-1, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 5 µM |  | 0.802× | -3.2 | 0.20 | 7/36 (C-33 A, RKO, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.553× | -3.1 | 0.20 | 10/31 (BT-474, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.739× | -3.1 | 0.21 | 12/35 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7223. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 8.16 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0946× (z -10.1) ⚠ toxic |
| [[HCT15 (line)]] | alt | 8.08 | 0 | 1 | — | [[Auranofin (drug)]] 0.5 µM 0.0600× (z -9.3) |
| [[HS-578T (line)]] | alt | 4.57 | 0 | 1 | — | [[Clotrimazole (drug)]] 0.5 µM 0.0693× (z -10.4) |
| [[HT-29 (line)]] | alt | 25.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -11.4) |
| [[RKO (line)]] | wt | 11.4 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0938× (z -10.1) |
| [[A-172 (line)]] | wt | 0.859 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.960 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.900 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.922 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7223), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CISD3]] | +0.58 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[MLST8]] | +0.57 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[PWWP2B]] | +0.57 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[DRG2]] | +0.56 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[MROH6]] | +0.55 | +0.59 / +0.58 | both halves | 7e-06 | STRING 568; ⚠ same locus (2.0 kb, same strand: neighbours can correlate without regulation) |
| [[DECR2]] | +0.55 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[PRXL2B]] | +0.55 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[BCS1L]] | +0.55 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PIGO]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[KDM5D]] | +0.53 | +0.43 / +0.44 | both halves | 4e-05 |  |
| [[PSMG1]] | +0.53 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[PIP4P1]] | +0.53 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[ZNF512B]] | +0.53 | +0.51 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MESD]] | -0.57 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[GLUD1P3]] | -0.55 | -0.40 / -0.54 | both halves | 4e-05 |  |
| [[NUCB2]] | -0.49 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ING2-DT]] | -0.48 | -0.20 / -0.43 | both halves | 7e-04 |  |
| [[PCGF3-AS1]] | -0.48 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[ZFC3H1]] | -0.47 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[KPNB1-DT]] | -0.47 | -0.23 / -0.45 | both halves | 5e-04 |  |
| [[RHCE]] | -0.47 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[PPP1R26-AS1]] | -0.46 | -0.26 / -0.41 | both halves | 4e-04 |  |
| [[TPTEP2-CSNK1E]] | -0.46 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[GNAS]] | -0.46 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[PDIA3]] | -0.45 | -0.38 / -0.42 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPPK1]] | B | EPPK1 activity raises NAPRT's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 1.97× lower at baseline in the lines without EPPK1 | 0.012 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[KDM5D]] | B | KDM5D activity lowers NAPRT's level | lines that do not express KDM5D (30) vs lines expressing it (20) | 1.86× higher at baseline in the lines without KDM5D | 0.026 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MROH6]] | B | NAPRT activity raises MROH6's level | lines that do not express NAPRT (9) vs lines expressing it (41) | 2.00× lower at baseline in the lines without NAPRT | 0.066 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.326). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-46.0, 17.6); signed map (-1.6, -34.8). **Vector** length 45.2, 6.70% of its response variance represented; |z| ≥ 3 in 587 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +9.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.6 | +3.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.4 | +3.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.0 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +0.8 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.7 | +4.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Adenosine (drug)]] 0.5 µM |  | -1.1 | -1.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.0 | -3.0 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | nicotinate phosphoribosyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,574,785-143,578,649 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PP3856; previously NAPRT1 |
| Gene groups (HGNC) | Ligases; Phosphoribosyltransferases |
| Reactome | 5 pathways, smallest: Nicotinate metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6XQN6](https://www.uniprot.org/uniprotkb/Q6XQN6) (Nicotinate phosphoribosyltransferase):

> Catalyzes the first step in the biosynthesis of NAD from nicotinic acid, the ATP-dependent synthesis of beta-nicotinate D-ribonucleotide from nicotinate and 5-phospho-D-ribose 1-phosphate. Helps prevent cellular oxidative stress via its role in NAD biosynthesis.

**Summary**, from NCBI Gene [93100](https://www.ncbi.nlm.nih.gov/gene/93100):

> Nicotinic acid (NA; niacin) is converted by nicotinic acid phosphoribosyltransferase (NAPRT; EC 2.4.2.11) to NA mononucleotide (NaMN), which is then converted to NA adenine dinucleotide (NaAD), and finally to nicotinamide adenine dinucleotide (NAD), which serves as a coenzyme in cellular redox reactions and is an essential component of a variety of processes in cellular metabolism including response to stress (Hara et al., 2007).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:30450](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30450) · Entrez [93100](https://www.ncbi.nlm.nih.gov/gene/93100) · UniProt [Q6XQN6](https://www.uniprot.org/uniprotkb/Q6XQN6) · Ensembl [ENSG00000147813](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147813)

## Data

Gene col 7223: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7223); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7223, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7223]; `tensor/DDL_lfc|DDL_z.npy` [7223]; `embed/gene_vectors.npy` [7223]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7223 or target_col == 7223). Every well: [[NAPRT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAPRT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
