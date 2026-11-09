---
symbol: "OCA2"
type: "gene"
col: 2408
ensembl_id: "ENSG00000104044"
name: "OCA2 melanosomal transmembrane protein"
location: "15q12-q13.1"
module: 82
arm: "+"
pooled_cpm: 3.33
n_lines_expressing: 32
n_dd_up: 28
n_dd_down: 4
n_dd_up_clean: 22
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# OCA2

*OCA2 melanosomal transmembrane protein* — 15q12-q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.06× (z +22.9, q 0e+00, up in 16 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.564× (z -5.8, q 5e-06, down in 11 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GABRG3]] (+0.59, fdr 1e-05), [[VAT1L]] (+0.59, fdr 1e-05), [[NOL4]] (+0.59, fdr 1e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[RET]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2408.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.06×** | +22.9 | 0e+00 | 16/23 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.96×** | +13.7 | 2e-40 | 22/28 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.39×** | +12.3 | 2e-32 | 19/27 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.16×** | +11.5 | 3e-28 | 18/26 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.07×** | +11.2 | 4e-27 | 23/28 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.14×** | +11.0 | 4e-26 | 1/4 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.93×** | +10.7 | 7e-25 | 1/10 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.95×** | +10.0 | 1e-21 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.18×** | +7.8 | 4e-13 | 18/27 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.18×** | +7.8 | 4e-13 | 7/24 (A498, A549, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.15×** | +7.6 | 1e-12 | 14/24 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.86×** | +6.2 | 3e-08 | 6/26 (LOX-IMVI, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +5.5 | 2e-06 | 5/21 (SW480, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +5.3 | 4e-06 | 6/24 (BT-474, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +5.2 | 7e-06 | 6/17 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.8 | 5e-05 | 2/28 (HEC-1-A, NCI-H1573) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +4.6 | 1e-04 | 5/15 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.36×** | +4.5 | 2e-04 | 10/24 (NCI-H23, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2408.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.564×** | -5.8 | 5e-06 | 11/22 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.573×** | -5.6 | 6e-06 | 16/27 (NCI-H23, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Captopril (drug)]] 0.5 µM |  | **0.691×** | -3.7 | 0.034 | 3/27 (HEC-1-A, HCT15, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.695×** | -3.7 | 0.034 | 11/27 (H4, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.805× | -3.1 | 0.20 | 10/27 (NCI-H661, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2408. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 23.0 | 1 (1 ⚠) | 6 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.77× (z +9.9) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.0792× (z -18.3) |
| [[LOX-IMVI (line)]] | wt | 32.8 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0396× (z -17.7) |
| [[H4 (line)]] | wt | 13.2 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.0531× (z -9.2) |
| [[PANC-1 (line)]] | alt | 2.17 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 24.1× (z +9.7) | [[Digitoxin (drug)]] 0.05 µM 0.0570× (z -8.7) |
| [[HOP62 (line)]] | alt | 4.86 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0422× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 28.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0704× (z -16.3) |
| [[HEC-1-A (line)]] | alt | 1.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +9.6) | — |
| [[SW480 (line)]] | alt | 1.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.95× (z +9.9) | — |
| [[A-172 (line)]] | wt | 0.786 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.949 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.896 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.557 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.881 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.614 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.811 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.667 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.603 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.844 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.617 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.600 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.836 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.615 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2408), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABRG3]] | +0.59 | +0.53 / +0.66 | both halves | 1e-05 | STRING 522 |
| [[VAT1L]] | +0.59 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[NOL4]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[LRRC63]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[TRIM9]] | +0.56 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[TCF4]] | +0.55 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[TMEM108]] | +0.54 | +0.36 / +0.51 | both halves | 9e-05 |  |
| [[ASXL3]] | +0.54 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ST6GALNAC3]] | +0.53 | +0.29 / +0.55 | both halves | 3e-04 |  |
| [[LPAR3]] | +0.53 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[LINC01524]] | +0.52 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[TMEM266]] | +0.52 | +0.41 / +0.63 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers OCA2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PAX3]] | B | PAX3 activity raises OCA2's level | lines that do not express PAX3 (38) vs lines expressing it (12) | 3.56× lower at baseline in the lines without PAX3 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, ENSG00000241168 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RET]] | B | OCA2 activity raises RET's level | lines that do not express OCA2 (18) vs lines expressing it (32) | 1.06× lower at baseline in the lines without OCA2 | 0.025 | ⚠ within organs, on part of the lines; also absent: BEX4, STAC, ATP10A; maybe low, not absent |
| [[SLIT3]] | B | OCA2 activity raises SLIT3's level | lines that do not express OCA2 (18) vs lines expressing it (32) | 2.87× lower at baseline in the lines without OCA2 | 0.042 | ⚠ within organs, on part of the lines; also absent: BEX4, STAC, ATP10A; maybe low, not absent |
| [[ESYT3]] | B | OCA2 activity raises ESYT3's level | lines that do not express OCA2 (18) vs lines expressing it (32) | 1.42× lower at baseline in the lines without OCA2 | 0.067 | ⚠ within organs, on part of the lines; also absent: BEX4, STAC, ATP10A; maybe low, not absent |
| [[SYT9]] | B | OCA2 activity raises SYT9's level | lines that do not express OCA2 (18) vs lines expressing it (32) | 1.77× lower at baseline in the lines without OCA2 | 0.093 | ⚠ within organs, on part of the lines; also absent: BEX4, STAC, ATP10A; maybe low, not absent |
| [[UBE2Q2P13]] | C | OCA2 activity raises UBE2Q2P13's level | lines that do not express OCA2 (18) vs lines expressing it (32) | 2.24× lower at baseline in the lines without OCA2 | 0.077 | ⚠ within organs, on part of the lines; also absent: BEX4, STAC, ATP10A; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.5, 22.4); signed map (35.7, 42.6). **Vector** length 52.2, 9.53% of its response variance represented; |z| ≥ 3 in 930 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +10.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +22.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +7.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +1.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -5.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -0.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | OCA2 melanosomal transmembrane protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q12-q13.1 — chr15:27,754,875-28,099,315 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BEY, BEY1, BEY2, EYCL, SLC13B1; previously D15S12, P, EYCL3, EYCL2 |
| Gene groups (HGNC) | Solute carrier family 13 |
| Reactome | 10 pathways, smallest: Assembly and release of respiratory syncytial virus (RSV) virions; Melanin biosynthesis; Respiratory syncytial virus genome replication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04671](https://www.uniprot.org/uniprotkb/Q04671) (P protein):

> Contributes to a melanosome-specific anion (chloride) current that modulates melanosomal pH for optimal tyrosinase activity required for melanogenesis and the melanosome maturation. One of the components of the mammalian pigmentary system. May serve as a key control point at which ethnic skin color variation is determined. Major determinant of brown and/or blue eye color. Seems to regulate the post-translational processing of tyrosinase, which catalyzes the limiting reaction in melanin …

**Summary**, from NCBI Gene [4948](https://www.ncbi.nlm.nih.gov/gene/4948):

> This gene encodes the human homolog of the mouse p (pink-eyed dilution) gene. The encoded protein is believed to be an integral membrane protein involved in small molecule transport, specifically tyrosine, which is a precursor to melanin synthesis. It is involved in mammalian pigmentation, where it may control skin color variation and act as a determinant of brown or blue eye color. Mutations in this gene result in type 2 oculocutaneous albinism. Alternative splicing results in multiple …

**Accessions** — [HGNC:8101](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8101) · Entrez [4948](https://www.ncbi.nlm.nih.gov/gene/4948) · UniProt [Q04671](https://www.uniprot.org/uniprotkb/Q04671) · Ensembl [ENSG00000104044](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104044)

## Data

Gene col 2408: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2408); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2408, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2408]; `tensor/DDL_lfc|DDL_z.npy` [2408]; `embed/gene_vectors.npy` [2408]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2408 or target_col == 2408). Every well: [[OCA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OCA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
