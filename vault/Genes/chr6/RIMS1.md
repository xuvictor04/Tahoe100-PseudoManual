---
symbol: "RIMS1"
type: "gene"
col: 1267
ensembl_id: "ENSG00000079841"
name: "regulating synaptic membrane exocytosis 1"
location: "6q13"
module: 19
arm: "+"
pooled_cpm: 4.83
n_lines_expressing: 32
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 2
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# RIMS1

*regulating synaptic membrane exocytosis 1* — 6q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.62× (z +21.9, q 0e+00, up in 14 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Medroxyprogesterone acetate (drug)]] 0.05 µM: 0.628× (z -4.7, q 0.002, down in 8 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 0.160×, A-427 0.123×); [[Budesonide (drug)]] 0.05 µM in 1 line (SW 900 0.108×); [[Docetaxel (drug)]] 0.05 µM in 1 line (SW 900 0.116×; ⚠ transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 0.191×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE1C]] (+0.69, fdr 7e-06), [[LINC00922]] (+0.69, fdr 7e-06), [[PCDH15]] (+0.69, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[EPB41L3]] → it (grade B ⚠); 2 go from it, the strongest it → [[INHBA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1267.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.62×** | +21.9 | 0e+00 | 14/21 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.94×** | +15.4 | 0e+00 | 19/26 (NCI-H23, BT-474, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.60×** | +13.7 | 2e-40 | 15/21 (NCI-H23, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.11×** | +11.5 | 2e-28 | 15/25 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.80×** | +10.4 | 2e-23 | 19/24 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +9.9 | 6e-21 | 1/8 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.58×** | +9.6 | 6e-20 | 3/13 (Hs 766T, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.69×** | +9.3 | 2e-18 | 1/8 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +6.6 | 3e-09 | 14/20 (NCI-H23, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +5.6 | 1e-06 | 0/19 | top dose only | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +5.5 | 2e-06 | 8/23 (SHP-77, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +5.0 | 2e-05 | 3/25 (SHP-77, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +5.0 | 3e-05 | 15/27 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.5 | 3e-04 | 5/18 (NCI-H2030, HS-578T, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.001 | 2/26 (HOP62, NCI-H661) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.005 | 9/26 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +3.7 | 0.007 | 12/27 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.34×** | +3.0 | 0.067 | 4/26 (NCI-H23, BT-474, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1267.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 0.160×, A-427 0.123×); [[Budesonide (drug)]] 0.05 µM in 1 line (SW 900 0.108×); [[Docetaxel (drug)]] 0.05 µM in 1 line (SW 900 0.116×; ⚠ transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H460 0.191×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.628×** | -4.7 | 0.002 | 8/24 (BT-474, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1267. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 30.3 | 0 | 3 (1 ⚠) | — | [[Budesonide (drug)]] 0.05 µM 0.108× (z -10.1) |
| [[BT-474 (line)]] | alt | 4.67 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 9.98× (z +8.8) | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 0.0440× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 6.45 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 12.8× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 35.3 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -9.6) |
| [[A-427 (line)]] | wt | 11.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -8.7) |
| [[C32 (line)]] | wt | 1.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.5× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 3.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.24× (z +8.8) | — |
| [[A-172 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.883 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.942 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.908 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.975 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.17 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1267), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE1C]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[LINC00922]] | +0.69 | +0.65 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[PCDH15]] | +0.69 | +0.66 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[MARCHF1]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[KCNJ6]] | +0.69 | +0.58 / +0.71 | both halves | 8e-06 | pathway: Neuronal System |
| [[NKAIN2]] | +0.65 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[GAP43]] | +0.64 | +0.45 / +0.68 | both halves | 3e-05 | **novel candidate** |
| [[LSAMP]] | +0.64 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[LINC01035]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[ASXL3]] | +0.64 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[RAB3C]] | +0.62 | +0.59 / +0.64 | both halves | 7e-06 | STRING 716 |
| [[DPP10]] | +0.62 | +0.64 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPB41L3]] | B | EPB41L3 activity raises RIMS1's level | lines that do not express EPB41L3 (34) vs lines expressing it (16) | 2.41× lower at baseline in the lines without EPB41L3 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PAX3, ROBO2, PTH2R |
| [[TOP2A]] | B | TOP2A activity lowers RIMS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RAB3C]] | B | RAB3C activity raises RIMS1's level | lines that do not express RAB3C (31) vs lines expressing it (19) | 2.06× lower at baseline in the lines without RAB3C | 0.043 | ⚠ within organs, on part of the lines; also absent: VGF, SCG3, CDH10; maybe low, not absent |
| [[DPP10]] | B | DPP10 activity raises RIMS1's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 2.36× lower at baseline in the lines without DPP10 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent |
| [[EPHA5-AS1]] | B | EPHA5-AS1 activity raises RIMS1's level | lines that do not express EPHA5-AS1 (28) vs lines expressing it (22) | 2.48× lower at baseline in the lines without EPHA5-AS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: EPHA5, ADAM23, TRPC4 |
| [[GAP43]] | B | GAP43 activity raises RIMS1's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 1.66× lower at baseline in the lines without GAP43 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent |
| [[ADGRB3]] | B | ADGRB3 activity raises RIMS1's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 2.19× lower at baseline in the lines without ADGRB3 | 0.098 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4 |
| [[VIPR2]] | C | VIPR2 activity raises RIMS1's level | lines that do not express VIPR2 (32) vs lines expressing it (18) | 2.16× lower at baseline in the lines without VIPR2 | 0.006 | ⚠ within organs, on part of the lines; also absent: DPP10, KCNH5, ASXL3; maybe low, not absent; co-absent with the target |
| [[NALF1]] | C | NALF1 activity raises RIMS1's level | lines that do not express NALF1 (28) vs lines expressing it (22) | 2.50× lower at baseline in the lines without NALF1 | 0.016 | ⚠ within organs, on part of the lines; also absent: EPHA5, COL3A1, ENSG00000248837; co-absent with the target |
| [[NCAM2]] | C | NCAM2 activity raises RIMS1's level | lines that do not express NCAM2 (24) vs lines expressing it (26) | 2.46× lower at baseline in the lines without NCAM2 | 0.044 | ⚠ within organs, on part of the lines; also absent: MMP16, ADGRB3, FAP; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INHBA]] | B | RIMS1 activity raises INHBA's level | lines that do not express RIMS1 (18) vs lines expressing it (32) | 4.18× lower at baseline in the lines without RIMS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ELOVL4, GLRB, RNF150; maybe low, not absent |
| [[VIPR2]] | C | RIMS1 activity raises VIPR2's level | lines that do not express RIMS1 (18) vs lines expressing it (32) | 1.83× lower at baseline in the lines without RIMS1 | 0.099 | ⚠ within organs, on part of the lines; also absent: ELOVL4, GLRB, RNF150; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.2, 34.3); signed map (42.1, 38.7). **Vector** length 52.7, 10.4% of its response variance represented; |z| ≥ 3 in 670 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +15.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +9.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.9 | +10.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +21.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +3.0 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.5 | +0.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -1.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | regulating synaptic membrane exocytosis 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q13 — chr6:71,886,550-72,403,150 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RIM, KIAA0340, RIM1; previously RAB3IP2, CORD7 |
| Gene groups (HGNC) | Regulating synaptic membrane exocytosis family; PDZ domain containing |
| Reactome | 9 pathways, smallest: Acetylcholine Neurotransmitter Release Cycle; GABA synthesis, release, reuptake and degradation; Norepinephrine Neurotransmitter Release Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UR5](https://www.uniprot.org/uniprotkb/Q86UR5) (Regulating synaptic membrane exocytosis protein 1):

> Rab effector involved in exocytosis (By similarity). May act as scaffold protein that regulates neurotransmitter release at the active zone. Essential for maintaining normal probability of neurotransmitter release and for regulating release during short-term synaptic plasticity (By similarity). Plays a role in dendrite formation by melanocytes.

**Summary**, from NCBI Gene [22999](https://www.ncbi.nlm.nih.gov/gene/22999):

> The protein encoded by this gene is a RAS gene superfamily member that regulates synaptic vesicle exocytosis. This gene also plays a role in the regulation of voltage-gated calcium channels during neurotransmitter and insulin release. Mutations have suggested a role cognition and have been identified as the cause of cone-rod dystrophy type 7. Multiple transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:17282](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17282) · Entrez [22999](https://www.ncbi.nlm.nih.gov/gene/22999) · UniProt [Q86UR5](https://www.uniprot.org/uniprotkb/Q86UR5) · Ensembl [ENSG00000079841](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079841)

## Data

Gene col 1267: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1267); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1267, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1267]; `tensor/DDL_lfc|DDL_z.npy` [1267]; `embed/gene_vectors.npy` [1267]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1267 or target_col == 1267). Every well: [[RIMS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIMS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
