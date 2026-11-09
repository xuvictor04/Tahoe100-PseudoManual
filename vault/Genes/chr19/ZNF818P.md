---
symbol: "ZNF818P"
type: "gene"
col: 15611
ensembl_id: "ENSG00000269001"
name: "zinc finger protein 818, pseudogene"
location: "19q13.42"
module: 10
arm: "+"
pooled_cpm: 2.95
n_lines_expressing: 29
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ZNF818P

*zinc finger protein 818, pseudogene* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.37× (z +9.9, q 2e-20, up in 13 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.370× (z -8.0, q 7e-13, down in 18 of 26 measured lines).
> Its strongest partners by |cos| (52 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 49 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF747]] (+0.66, fdr 4e-05), [[THNSL2]] (+0.65, fdr 8e-05), [[PLBD1-AS1]] (+0.62, fdr 1e-04); moves opposite to [[TXNL4A]] (-0.58, fdr 2e-04), [[L2HGDH]] (-0.53, fdr 5e-04), [[ANAPC5]] (-0.53, fdr 5e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[IDNK]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15611.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +9.9 | 2e-20 | 13/19 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.67×** | +5.9 | 8e-07 | 10/23 (NCI-H23, J82, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +5.9 | 8e-07 | 10/16 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.2 | 2e-05 | 13/25 (PANC-1, Hs 766T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +4.5 | 7e-04 | 5/18 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.61×** | +3.9 | 0.009 | 7/17 (SW 900, J82, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.63×** | +3.8 | 0.010 | 7/19 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.56×** | +3.6 | 0.020 | 7/21 (NCI-H23, SW 900, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +3.5 | 0.024 | 0/4 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +3.3 | 0.065 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.45× | +3.0 | 0.13 | 3/22 (BT-474, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15611.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.370×** | -8.0 | 7e-13 | 18/26 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.516×** | -5.3 | 3e-05 | 13/16 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.550×** | -4.8 | 3e-04 | 11/22 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.336×** | -4.6 | 6e-04 | 13/20 (PANC-1, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.357×** | -4.3 | 0.002 | 12/19 (BT-474, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.629×** | -3.7 | 0.019 | 3/24 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.647×** | -3.5 | 0.040 | 5/22 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.652×** | -3.4 | 0.045 | 8/22 (PANC-1, CFPAC-1, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.679× | -3.1 | 0.12 | 7/21 (PANC-1, SW480, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15611. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.5 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.244× (z -10.2) |
| [[BT-474 (line)]] | alt | 7.46 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0978× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 4.37 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0768× (z -8.6) |
| [[A-172 (line)]] | wt | 0.392 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.144 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.131 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.192 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.445 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.173 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.172 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.187 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.834 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.165 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.200 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.145 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.142 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.168 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.169 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.142 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.767 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.181 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.185 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.172 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.185 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15611), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 47 of them with an alert (⚠; 46 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF747]] | +0.66 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[THNSL2]] | +0.65 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[PLBD1-AS1]] | +0.62 | +0.64 / +0.34 | both halves | 1e-04 |  |
| [[ZNF665]] | +0.61 | +0.61 / +0.46 | both halves | 3e-05 | ⚠ same locus (10.6 kb: neighbours can correlate without regulation) |
| [[ARMCX4]] | +0.59 | +0.66 / +0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[WAC-AS1]] | +0.59 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[CCDC90B-AS1]] | +0.58 | +0.61 / +0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[TSPYL1]] | +0.58 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[TIGD6]] | +0.58 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[IDNK]] | +0.58 | +0.50 / +0.16 | ⚠ not reproduced | 0.001 |  |
| [[EIF5]] | +0.57 | +0.49 / +0.34 | both halves | 1e-04 |  |
| [[CREBBP]] | +0.57 | +0.50 / +0.26 | both halves | 4e-04 |  |
| [[BCDIN3D]] | +0.57 | +0.54 / +0.35 | both halves | 1e-04 |  |
| [[C7orf25]] | +0.57 | +0.53 / +0.35 | both halves | 1e-04 |  |
| [[PATL2]] | +0.57 | +0.61 / +0.23 | both halves | 5e-04 |  |
| [[TMEM202-AS1]] | +0.56 | +0.53 / +0.21 | both halves | 6e-04 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNL4A]] | -0.58 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[L2HGDH]] | -0.53 | -0.47 / -0.23 | both halves | 5e-04 |  |
| [[ANAPC5]] | -0.53 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[TMEM120B]] | -0.51 | -0.48 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[NR2C1]] | -0.51 | -0.57 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZNF818P's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF681]] | B | ZNF681 activity raises ZNF818P's level | lines that do not express ZNF681 (16) vs lines expressing it (34) | 1.94× lower at baseline in the lines without ZNF681 | 0.089 | ⚠ within organs, on part of the lines; also absent: RPSAP58, ZNF649, ZNF793 |
| [[ZNF665]] | C | ZNF665 activity raises ZNF818P's level | lines that do not express ZNF665 (24) vs lines expressing it (26) | 2.94× lower at baseline in the lines without ZNF665 | 6e-04 | ⚠ within organs, on part of the lines; also absent: ZNF93, ZNF818P, ZNF347; co-absent with the target |
| [[ZNF528]] | C | ZNF528 activity raises ZNF818P's level | lines that do not express ZNF528 (21) vs lines expressing it (29) | 2.38× lower at baseline in the lines without ZNF528 | 0.037 | ⚠ within organs, on part of the lines; also absent: ZNF528-AS1, ZNF625, ZNF880; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IDNK]] | B | ZNF818P activity lowers IDNK's level | lines that do not express ZNF818P (21) vs lines expressing it (29) | 1.33× higher at baseline in the lines without ZNF818P | 0.057 | ⚠ within organs, on part of the lines; also absent: ZNF665, ZNF347, ZNF93 |
| [[ZNF681]] | B | ZNF818P activity raises ZNF681's level | lines that do not express ZNF818P (21) vs lines expressing it (29) | 1.89× lower at baseline in the lines without ZNF818P | 0.081 | ⚠ within organs, on part of the lines; also absent: ZNF665, ZNF347, ZNF93 |
| [[ZNF665]] | C | ZNF818P activity raises ZNF665's level | lines that do not express ZNF818P (21) vs lines expressing it (29) | 3.22× lower at baseline in the lines without ZNF818P | 2e-05 | ⚠ within organs, on part of the lines; also absent: ZNF665, ZNF347, ZNF93; co-absent with the target |
| [[ZNF528]] | C | ZNF818P activity raises ZNF528's level | lines that do not express ZNF818P (21) vs lines expressing it (29) | 3.37× lower at baseline in the lines without ZNF818P | 0.027 | ⚠ within organs, on part of the lines; also absent: ZNF665, ZNF347, ZNF93; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.607). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.2, 13.4); signed map (26.5, -12.4). **Vector** length 31.5, 4.69% of its response variance represented; |z| ≥ 3 in 512 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.5 | +5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +9.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.3 | +4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.0 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.8 | +0.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +0.8 | +2.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +0.7 | +2.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | +1.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.1 | -3.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | +0.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -0.8 | -1.7 |
|  | [[EX229 (drug)]] 5 µM |  | -0.8 | -1.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.8 | -2.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 818, pseudogene |
| Locus type | pseudogene |
| Location | 19q13.42 — chr19:53,204,016-53,214,522 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | FLJ46385; previously ZNF818 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZRF7](https://www.uniprot.org/uniprotkb/Q6ZRF7) (Putative zinc finger protein 818):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [390963](https://www.ncbi.nlm.nih.gov/gene/390963):

> Predicted to enable DNA-binding transcription factor activity. Predicted to be involved in DNA-templated transcription and negative regulation of DNA-templated transcription. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33265](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33265) · Entrez [390963](https://www.ncbi.nlm.nih.gov/gene/390963) · UniProt [Q6ZRF7](https://www.uniprot.org/uniprotkb/Q6ZRF7) · Ensembl [ENSG00000269001](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000269001)

## Data

Gene col 15611: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15611); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15611, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15611]; `tensor/DDL_lfc|DDL_z.npy` [15611]; `embed/gene_vectors.npy` [15611]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15611 or target_col == 15611). Every well: [[ZNF818P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF818P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
