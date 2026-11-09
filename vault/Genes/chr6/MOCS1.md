---
symbol: "MOCS1"
type: "gene"
col: 4554
ensembl_id: "ENSG00000124615"
name: "molybdenum cofactor synthesis 1"
location: "6p21.2"
module: 15
arm: "-"
pooled_cpm: 2.61
n_lines_expressing: 36
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# MOCS1

*molybdenum cofactor synthesis 1* — 6p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.90× (z +5.8, q 3e-06, up in 13 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.331× (z -14.2, q 7e-43, down in 25 of 27 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF527]] (+0.65, fdr 1e-04), [[COMMD2]] (+0.60, fdr 4e-05), [[CHST10]] (+0.60, fdr 1e-05); moves opposite to [[ASH1L]] (-0.65, fdr 2e-05), [[MED13]] (-0.63, fdr 3e-05), [[DNASE1]] (-0.62, fdr 2e-05).
> It sits in the **-** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 4 go from it, the strongest it → [[HIF1AN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4554.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +5.8 | 3e-06 | 13/33 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +5.5 | 9e-06 | 15/33 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +5.1 | 6e-05 | 14/30 (NCI-H460, HS-578T, …) | two highest doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +4.6 | 7e-04 | 12/33 (Panc 03.27, HS-578T, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +4.3 | 0.002 | 11/33 (HEC-1-A, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +4.3 | 0.002 | 12/33 (NCI-H2347, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | 1.40× | +3.0 | 0.19 | 1/33 (HS-578T) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4554.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.331×** | -14.2 | 7e-43 | 25/27 (Panc 03.27, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.400×** | -8.0 | 4e-13 | 13/26 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.417×** | -7.9 | 4e-13 | 14/22 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.425×** | -7.5 | 1e-11 | 13/23 (HS-578T, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.608×** | -6.4 | 2e-08 | 15/26 (C32, A-172, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.507×** | -6.2 | 7e-08 | 18/33 (J82, H4, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.656×** | -3.8 | 0.011 | 15/31 (SNU-423, J82, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.662×** | -3.7 | 0.013 | 10/31 (NCI-H1573, SNU-423, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.474×** | -3.5 | 0.025 | 11/29 (SHP-77, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.705×** | -3.2 | 0.084 | 9/33 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | 0.708× | -3.0 | 0.13 | 6/18 (HEC-1-A, MIA PaCa-2, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4554. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 7.67 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0652× (z -11.0) |
| [[C32 (line)]] | wt | 5.81 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0854× (z -12.0) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 7.09 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0897× (z -14.1) |
| [[A-172 (line)]] | wt | 2.69 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0932× (z -10.3) ⚠ cell-cycle shift, explains ~67% of this change |
| [[CFPAC-1 (line)]] | alt | 2.67 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 8.70 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0592× (z -14.7) |
| [[HOP62 (line)]] | alt | 5.35 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 3.85 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0780× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 3.13 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 8.85 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -8.6) ⚠ cell-cycle shift, explains ~67% of this change |
| [[SNU-423 (line)]] | alt | 4.37 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0845× (z -11.6) |
| [[A-427 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.970 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.214 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.166 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.944 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.241 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.186 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.795 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.192 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.239 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.885 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.244 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.163 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4554), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF527]] | +0.65 | +0.35 / +0.72 | both halves | 1e-04 |  |
| [[COMMD2]] | +0.60 | +0.40 / +0.52 | both halves | 4e-05 |  |
| [[CHST10]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[RSAD1]] | +0.60 | +0.46 / +0.44 | both halves | 3e-05 | same gene group; STRING 490 |
| [[ETNK2]] | +0.59 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[SAAL1]] | +0.59 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[ZNF473]] | +0.58 | +0.36 / +0.60 | both halves | 9e-05 |  |
| [[SUGT1P4-STRA6LP]] | +0.58 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[ZNF232]] | +0.58 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[PTPRS]] | +0.58 | +0.44 / +0.39 | both halves | 5e-05 |  |
| [[TOX2]] | +0.58 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[STRA6LP]] | +0.58 | +0.44 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASH1L]] | -0.65 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[MED13]] | -0.63 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[DNASE1]] | -0.62 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[PPP1R15B-AS1]] | -0.61 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[C2orf76]] | -0.59 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[GALNT7-DT]] | -0.58 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[KIAA2026]] | -0.58 | -0.20 / -0.63 | both halves | 7e-04 |  |
| [[NIFK-AS1]] | -0.57 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[CCDC90B-AS1]] | -0.57 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[TTC41P]] | -0.57 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[NEK8]] | -0.57 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[FAM174B]] | -0.56 | -0.38 / -0.40 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers MOCS1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers MOCS1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises MOCS1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HEYL]] | B | HEYL activity raises MOCS1's level | lines that do not express HEYL (25) vs lines expressing it (25) | 1.15× lower at baseline in the lines without HEYL | 0.084 | ⚠ within organs, on part of the lines; also absent: HCG11, GAL, LRRN2 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HIF1AN]] | B | MOCS1 activity raises HIF1AN's level | lines that do not express MOCS1 (13) vs lines expressing it (36) | 1.14× lower at baseline in the lines without MOCS1 | 0.048 | ⚠ within organs, on part of the lines; also absent: SNRPN, MYH10, ANKRD6 |
| [[ARHGAP15]] | B | MOCS1 activity lowers ARHGAP15's level | lines that do not express MOCS1 (13) vs lines expressing it (36) | 1.01× higher at baseline in the lines without MOCS1 | 0.086 | ⚠ within organs, on part of the lines; also absent: SNRPN, MYH10, ANKRD6 |
| [[CSNK1G1]] | B | MOCS1 activity raises CSNK1G1's level | lines that do not express MOCS1 (13) vs lines expressing it (36) | 1.11× lower at baseline in the lines without MOCS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: SNRPN, MYH10, ANKRD6 |
| [[RAB6B]] | C | MOCS1 activity raises RAB6B's level | lines that do not express MOCS1 (13) vs lines expressing it (36) | 2.63× lower at baseline in the lines without MOCS1 | 0.036 | ⚠ within organs, on part of the lines; also absent: SNRPN, MYH10, ANKRD6; co-absent with the target |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **-** arm (projection on the module's main direction -0.436). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-1.3, 19.5); signed map (-25.4, -15.3). **Vector** length 43.3, 5.84% of its response variance represented; |z| ≥ 3 in 779 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.4 | +5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.8 | +5.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.7 | +4.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.7 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | -0.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.9 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.9 | +2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +0.7 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -14.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -7.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.7 | -8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -1.4 | -6.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.1 | -0.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -0.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | molybdenum cofactor synthesis 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:39,899,578-39,934,551 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MOCOD, MOCS1A, MOCS1B |
| Gene groups (HGNC) | Radical S-adenosylmethionine domain containing; Molybdenum cofactor synthesis proteins |
| Reactome | 3 pathways, smallest: Molybdenum cofactor biosynthesis; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZB8](https://www.uniprot.org/uniprotkb/Q9NZB8) (Molybdenum cofactor biosynthesis protein 1):

> Isoform MOCS1A and isoform MOCS1B probably form a complex that catalyzes the conversion of 5'-GTP to cyclic pyranopterin monophosphate (cPMP). MOCS1A catalyzes the cyclization of GTP to (8S)-3',8-cyclo-7,8-dihydroguanosine 5'-triphosphate and MOCS1B catalyzes the subsequent conversion of (8S)-3',8-cyclo-7,8-dihydroguanosine 5'-triphosphate to cPMP.; [Isoform 9]: Has very weak catalytic activity.

**Summary**, from NCBI Gene [4337](https://www.ncbi.nlm.nih.gov/gene/4337):

> Molybdenum cofactor biosynthesis is a conserved pathway leading to the biological activation of molybdenum. The protein encoded by this gene is involved in this pathway. This gene was originally thought to produce a bicistronic mRNA with the potential to produce two proteins (MOCS1A and MOCS1B) from adjacent open reading frames. However, only the first open reading frame (MOCS1A) has been found to encode a protein from the putative bicistronic mRNA, whereas additional splice variants are likely …

**Accessions** — [HGNC:7190](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7190) · Entrez [4337](https://www.ncbi.nlm.nih.gov/gene/4337) · UniProt [Q9NZB8](https://www.uniprot.org/uniprotkb/Q9NZB8) · Ensembl [ENSG00000124615](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124615)

## Data

Gene col 4554: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4554); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4554, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4554]; `tensor/DDL_lfc|DDL_z.npy` [4554]; `embed/gene_vectors.npy` [4554]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4554 or target_col == 4554). Every well: [[MOCS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOCS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
