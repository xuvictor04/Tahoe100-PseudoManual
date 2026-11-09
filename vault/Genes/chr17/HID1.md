---
symbol: "HID1"
type: "gene"
col: 9550
ensembl_id: "ENSG00000167861"
name: "HID1 domain containing"
location: "17q25.1"
module: 49
arm: "+"
pooled_cpm: 5.9
n_lines_expressing: 39
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 9
direction_downstream: 1
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# HID1

*HID1 domain containing* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.30× (z +8.5, q 7e-15, up in 23 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.641× (z -4.6, q 0.003, down in 14 of 35 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.454× (z -4.3, q 0.006, down in 12 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW 900 0.118×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.237×; ⚠ toxic; transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0948×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED9]] (+0.62, fdr 1e-05), [[SEC61B]] (+0.61, fdr 1e-05), [[SEC11C]] (+0.60, fdr 2e-05); moves opposite to [[PRORP]] (-0.57, fdr 3e-05), [[TBC1D5]] (-0.57, fdr 7e-05), [[ZNF124]] (-0.54, fdr 2e-04).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[EPHA10]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ARVCF]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9550.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.30×** | +8.5 | 7e-15 | 23/36 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +7.3 | 7e-11 | 24/34 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +5.0 | 1e-04 | 15/34 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +3.8 | 0.025 | 14/33 (HOP62, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.043 | 12/30 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.043 | 8/33 (LS 180, CFPAC-1, …) | rises with dose | position effect removed |
| [[Cyclosporin A (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.071 | 8/33 (SW480, NCI-H1573, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9550.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW 900 0.118×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.237×; ⚠ toxic; transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0948×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.641×** | -4.6 | 0.003 | 14/35 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.454×** | -4.3 | 0.006 | 12/32 (LoVo, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.731× | -3.2 | 0.20 | 4/33 (SW480, HCT15, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | 0.737× | -3.1 | 0.20 | 12/30 (NCI-H460, LoVo, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.738× | -3.1 | 0.20 | 10/33 (KATO III, NCI-H1792, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.745× | -3.0 | 0.22 | 8/33 (A-172, SW480, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9550. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 9.93 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0948× (z -8.6) |
| [[LoVo (line)]] | wt | 16.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -8.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.118× (z -9.3) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.513 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.595 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.688 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.613 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.907 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.770 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.974 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9550), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED9]] | +0.62 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[SEC61B]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[SEC11C]] | +0.60 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[CREB3L2]] | +0.59 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[WIPI1]] | +0.59 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[GFPT1]] | +0.59 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[SELENOS]] | +0.58 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[RNF187]] | +0.58 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[FICD]] | +0.58 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[PIGH]] | +0.57 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[ARFGAP3]] | +0.56 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[FXR2]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRORP]] | -0.57 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[TBC1D5]] | -0.57 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[ZNF124]] | -0.54 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[AFG1L]] | -0.53 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[TFAM]] | -0.53 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[SNX5]] | -0.53 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[MRPS7]] | -0.52 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[UTP20]] | -0.52 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ANAPC1]] | -0.52 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ZRANB3]] | -0.50 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[RIF1]] | -0.49 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[DARS2]] | -0.49 | -0.38 / -0.44 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA10]] | B | EPHA10 activity raises HID1's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 2.99× lower at baseline in the lines without EPHA10 | 0.030 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |
| [[AGR2]] | B | AGR2 activity raises HID1's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 2.21× lower at baseline in the lines without AGR2 | 0.035 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[TMEM125]] | B | TMEM125 activity raises HID1's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 3.34× lower at baseline in the lines without TMEM125 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[IRF6]] | B | IRF6 activity raises HID1's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 2.75× lower at baseline in the lines without IRF6 | 0.069 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers HID1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers HID1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SYTL1]] | B | SYTL1 activity raises HID1's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 2.68× lower at baseline in the lines without SYTL1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[GALNT3]] | B | GALNT3 activity raises HID1's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 2.97× lower at baseline in the lines without GALNT3 | 0.087 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[ESRP1]] | B | ESRP1 activity raises HID1's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 2.89× lower at baseline in the lines without ESRP1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARVCF]] | B | HID1 activity raises ARVCF's level | lines that do not express HID1 (11) vs lines expressing it (39) | 1.94× lower at baseline in the lines without HID1 | 0.089 | ⚠ within organs, on part of the lines; also absent: NRARP, HAP1, FAM169A; its own permutation p |

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.7, -37.7); signed map (-54.6, 14.6). **Vector** length 58.2, 11.2% of its response variance represented; |z| ≥ 3 in 569 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.6 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.5 | +3.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.4 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +1.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | +1.8 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.0 | -3.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.9 | -3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 5 µM |  | -1.4 | -0.2 |
|  | [[Busulfan (drug)]] 5 µM |  | -1.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | HID1 domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:74,950,742-74,973,166 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DMC1, HID-1; previously C17orf28 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IV36](https://www.uniprot.org/uniprotkb/Q8IV36) (Protein HID1):

> Plays a role in the biogenesis of large dense core vesicles (LDCVs) at the trans-Golgi network; necessary for the proper sorting of cargo into LDCVs and is required for proper regulated exocytosis (also known as regulated secretory pathway).

**Summary**, from NCBI Gene [283987](https://www.ncbi.nlm.nih.gov/gene/283987):

> Predicted to act upstream of or within several processes, including insulin processing; secretory granule maturation; and vacuole fusion, non-autophagic. Located in Golgi apparatus; cytoplasmic microtubule; and cytosol. Implicated in developmental and epileptic encephalopathy 105. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15736](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15736) · Entrez [283987](https://www.ncbi.nlm.nih.gov/gene/283987) · UniProt [Q8IV36](https://www.uniprot.org/uniprotkb/Q8IV36) · Ensembl [ENSG00000167861](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167861)

## Data

Gene col 9550: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9550); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9550, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9550]; `tensor/DDL_lfc|DDL_z.npy` [9550]; `embed/gene_vectors.npy` [9550]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9550 or target_col == 9550). Every well: [[HID1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HID1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
