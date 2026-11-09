---
symbol: "PCED1A"
type: "gene"
col: 5350
ensembl_id: "ENSG00000132635"
name: "PC-esterase domain containing 1A"
location: "20p13"
module: 157
arm: "+"
pooled_cpm: 11.4
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# PCED1A

*PC-esterase domain containing 1A* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.82× (z +7.5, q 3e-11, up in 23 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.46× (z +6.8, q 2e-09, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.496× (z -8.8, q 1e-15, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHSA2P]] (+0.71, fdr 1e-05), [[AP1G2-AS1]] (+0.70, fdr 3e-05), [[SRSF5]] (+0.68, fdr 3e-05); moves opposite to [[KIAA1328]] (-0.54, fdr 5e-04), [[GPSM2]] (-0.54, fdr 7e-05), [[PCMT1]] (-0.53, fdr 0.001, ⚠ not reproduced).
> It is in [[Module 157]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5350.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +7.5 | 3e-11 | 23/34 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +7.3 | 6e-11 | 10/17 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.8 | 2e-09 | 25/47 (NCI-H2347, HS-578T, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +5.9 | 6e-07 | 14/26 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.7 | 1e-06 | 26/44 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.35×** | +5.3 | 9e-06 | 25/47 (LS 180, MIA PaCa-2, …) | rises with dose | low cells (technical?); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.028 | 17/45 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.064 | 9/46 (C32, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.3 | 0.064 | 4/28 (SW480, J82, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.064 | 7/42 (LoVo, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Saquinavir (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.10 | 13/43 (HT-29, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5350.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.496×** | -8.8 | 1e-15 | 37/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.511×** | -8.4 | 1e-14 | 35/47 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.540×** | -7.7 | 3e-12 | 32/47 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.606×** | -6.3 | 5e-08 | 29/47 (hTERT-HPNE, NCI-H661, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.386×** | -6.2 | 5e-08 | 27/44 (NCI-H460, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.630×** | -5.8 | 8e-07 | 25/44 (RPMI-7951, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.739×** | -5.3 | 8e-06 | 23/46 (PANC-1, HEC-1-A, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.477×** | -4.8 | 9e-05 | 24/47 (PANC-1, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.711×** | -4.2 | 0.001 | 19/46 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.720×** | -4.1 | 0.002 | 19/46 (NCI-H23, C-33 A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.727×** | -4.0 | 0.004 | 18/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.730×** | -3.9 | 0.004 | 15/47 (PANC-1, SW 1271, …) | all doses, flat | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.581×** | -3.5 | 0.017 | 10/43 (Hs 766T, HS-578T, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.767×** | -3.3 | 0.040 | 17/46 (CHP-212, PANC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.766×** | -3.2 | 0.054 | 19/46 (PANC-1, HEC-1-A, …) | rises with dose | composition shift; position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.628×** | -3.0 | 0.078 | 9/46 (NCI-H23, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.636×** | -3.0 | 0.094 | 3/45 (CFPAC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5350. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 10.0 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.170× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~93% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.183× (z -8.9) |
| [[PANC-1 (line)]] | alt | 18.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -16.0) ⚠ cell-cycle shift, explains ~59% of this change |
| [[H4 (line)]] | wt | 11.2 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0916× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -9.7) ⚠ cell-cycle shift, explains ~59% of this change |
| [[hTERT-HPNE (line)]] | wt | 9.33 | 0 | 1 | — | [[Panobinostat (drug)]] 0.05 µM 0.0682× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 7.66 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0653× (z -8.5) |
| [[SNU-1 (line)]] | wt | 21.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -9.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW1417 (line)]] | alt | 4.36 | 0 | 1 | — | [[Nafamostat (mesylate) (drug)]] 0.5 µM 0.0628× (z -11.0) |
| [[SW480 (line)]] | alt | 21.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.321× (z -9.8) |
| [[A-172 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5350), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 18 of them with an alert (⚠; 18 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHSA2P]] | +0.71 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[AP1G2-AS1]] | +0.70 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[SRSF5]] | +0.68 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[HYI]] | +0.68 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[EME2]] | +0.67 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[KMT2E-AS1]] | +0.65 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[INPPL1]] | +0.62 | +0.34 / +0.52 | both halves | 1e-04 |  |
| [[PNISR-AS1]] | +0.62 | +0.50 / +0.27 | both halves | 3e-04 |  |
| [[TTC32]] | +0.61 | +0.49 / +0.29 | both halves | 2e-04 |  |
| [[SH2B1]] | +0.61 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[CD27-AS1]] | +0.60 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[TGFB3]] | +0.60 | +0.48 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1328]] | -0.54 | -0.41 / -0.23 | both halves | 5e-04 |  |
| [[GPSM2]] | -0.54 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[PCMT1]] | -0.53 | -0.43 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[YIF1B]] | -0.52 | -0.39 / +0.01 | ⚠ not reproduced | 1.00 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PCED1A's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HECTD2]] | B | HECTD2 activity raises PCED1A's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 2.17× lower at baseline in the lines without HECTD2 | 0.065 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[THBS4]] | B | THBS4 activity raises PCED1A's level | lines that do not express THBS4 (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without THBS4 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379, WDR35, AGK; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.2, 22.7); signed map (32.0, -20.6). **Vector** length 67.8, 11.1% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +5.0 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +6.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +5.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +0.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.2 | -8.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.8 | -8.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.3 | -7.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.9 | -6.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.6 | -5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.7 | -2.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | PC-esterase domain containing 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:2,835,314-2,841,190 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA12M19.1, FLJ22376; previously C20orf81, FAM113A |
| Matched by | ensembl_id |

UniProt [Q9H1Q7](https://www.uniprot.org/uniprotkb/Q9H1Q7) carries no function annotation.

**Summary**, from NCBI Gene [64773](https://www.ncbi.nlm.nih.gov/gene/64773):

> The protein encoded by this gene is a member of the GDSL/SGNH superfamily. Members of this family are hydrolytic enzymes with esterase and lipase activity and broad substrate specificity. This protein belongs to the Pmr5-Cas1p-esterase subfamily in that it contains the catalytic triad comprised of serine, aspartate and histidine and lacks two conserved regions (glycine after strand S2 and GxND motif). A pseudogene of this gene has been identified on the long arm of chromosome 2. Alternative …

**Accessions** — [HGNC:16212](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16212) · Entrez [64773](https://www.ncbi.nlm.nih.gov/gene/64773) · UniProt [Q9H1Q7](https://www.uniprot.org/uniprotkb/Q9H1Q7) · Ensembl [ENSG00000132635](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132635)

## Data

Gene col 5350: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5350); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5350, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5350]; `tensor/DDL_lfc|DDL_z.npy` [5350]; `embed/gene_vectors.npy` [5350]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5350 or target_col == 5350). Every well: [[PCED1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCED1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
