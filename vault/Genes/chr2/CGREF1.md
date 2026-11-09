---
symbol: "CGREF1"
type: "gene"
col: 6108
ensembl_id: "ENSG00000138028"
name: "cell growth regulator with EF-hand domain 1"
location: "2p23.3"
module: 176
arm: "+"
pooled_cpm: 5.68
n_lines_expressing: 40
n_dd_up: 10
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# CGREF1

*cell growth regulator with EF-hand domain 1* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.18× (z +13.8, q 3e-40, up in 16 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.51× (z +6.9, q 9e-10, up in 19 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.417× (z -14.8, q 0e+00, down in 26 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASIC1]] (+0.71, fdr 1e-05), [[PODXL2]] (+0.69, fdr 7e-06), [[MPV17L]] (+0.63, fdr 1e-05); moves opposite to [[UBXN4]] (-0.51, fdr 4e-05), [[XRN1]] (-0.51, fdr 6e-05), [[ZFYVE16]] (-0.49, fdr 2e-05).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PODXL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6108.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.18×** | +13.8 | 3e-40 | 16/19 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +11.4 | 1e-27 | 7/10 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +7.3 | 4e-11 | 10/13 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +6.9 | 9e-10 | 19/36 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +5.2 | 2e-05 | 13/35 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.2 | 0.002 | 6/33 (BT-474, RKO, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.54×** | +3.7 | 0.019 | 1/27 (PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.023 | 3/32 (NCI-H23, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.34×** | +3.5 | 0.031 | 11/37 (SW480, A549, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.090 | 6/35 (LS 180, HS-578T, …) | two highest doses |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | 1.31× | +3.0 | 0.12 | 3/29 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.29× | +3.0 | 0.12 | 5/35 (NCI-H2030, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, none with an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6108.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.417×** | -14.8 | 0e+00 | 26/33 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.288×** | -14.3 | 7e-44 | 28/36 (LS 180, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.432×** | -10.0 | 2e-21 | 21/37 (PANC-1, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.499×** | -8.3 | 2e-14 | 19/34 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.552×** | -6.7 | 2e-09 | 15/33 (LS 180, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.615×** | -5.8 | 6e-07 | 20/36 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.618×** | -5.7 | 7e-07 | 17/34 (PANC-1, HCT15, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.626×** | -5.6 | 2e-06 | 14/36 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.636×** | -5.4 | 4e-06 | 18/37 (PANC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.637×** | -5.4 | 4e-06 | 17/36 (SNU-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.706×** | -4.2 | 0.002 | 12/37 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.755×** | -3.4 | 0.036 | 8/37 (SNU-1, HOP62, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | **0.825×** | -3.3 | 0.046 | 8/37 (SHP-77, A498, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.597×** | -3.2 | 0.052 | 4/34 (MIA PaCa-2, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.766×** | -3.2 | 0.053 | 10/36 (NCI-H2030, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6108. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 13.0 | 4 (4 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 11.1× (z +17.6) ⚠ cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -18.6) |
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -18.7) |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.0786× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 14.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -16.4) |
| [[SW1417 (line)]] | alt | 11.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -13.1) |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 2 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0969× (z -9.4) |
| [[PANC-1 (line)]] | alt | 7.46 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -10.3) |
| [[SNU-1 (line)]] | wt | 16.3 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.107× (z -8.9) |
| [[SW48 (line)]] | wt | 9.81 | 0 | 2 | — | [[Bestatin (drug)]] 5 µM 0.0676× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 2.98 | 0 | 1 | — | [[Berbamine (dihydrochloride) (drug)]] 5 µM 0.0464× (z -8.8) |
| [[BT-474 (line)]] | alt | 4.54 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0998× (z -10.4) |
| [[C32 (line)]] | wt | 6.42 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0523× (z -9.2) |
| [[HT-29 (line)]] | alt | 3.85 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0963× (z -10.2) |
| [[LoVo (line)]] | wt | 5.37 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.116× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[NCI-H23 (line)]] | alt | 11.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0813× (z -11.8) |
| [[RKO (line)]] | wt | 5.79 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0665× (z -9.4) |
| [[A-172 (line)]] | wt | 0.975 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.848 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.964 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.861 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.853 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.975 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.827 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6108), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASIC1]] | +0.71 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[PODXL2]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[MPV17L]] | +0.63 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[GLB1L2]] | +0.63 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[AIF1L]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 | same gene group |
| [[NSUN5P1]] | +0.61 | +0.46 / +0.68 | both halves | 2e-05 |  |
| [[SLC46A1]] | +0.60 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[LHX6]] | +0.60 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[LINC01357]] | +0.60 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[MTARC1]] | +0.60 | +0.36 / +0.72 | both halves | 9e-05 |  |
| [[SEPTIN3]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[MCOLN2]] | +0.59 | +0.37 / +0.64 | both halves | 7e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBXN4]] | -0.51 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[XRN1]] | -0.51 | -0.38 / -0.59 | both halves | 6e-05 |  |
| [[ZFYVE16]] | -0.49 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[DCTN2]] | -0.49 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[SNRNP27]] | -0.48 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[PPP1R12A]] | -0.48 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[SHOC2]] | -0.48 | -0.50 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PODXL2]] | B | PODXL2 activity raises CGREF1's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 2.00× lower at baseline in the lines without PODXL2 | 0.018 | ⚠ within organs, on part of the lines |
| [[LAMC3]] | B | LAMC3 activity raises CGREF1's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.59× lower at baseline in the lines without LAMC3 | 0.071 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[B4GALNT4]] | B | B4GALNT4 activity raises CGREF1's level | lines that do not express B4GALNT4 (18) vs lines expressing it (32) | 1.60× lower at baseline in the lines without B4GALNT4 | 0.082 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CGREF1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[PRR5]], [[PRR5-ARHGAP8]] | C | PRR5, PRR5-ARHGAP8 activity raises CGREF1's level | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (46) | 2.92× lower at baseline in the lines without PRR5, PRR5-ARHGAP8 | 0.072 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.728). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.4, 41.6); signed map (-7.3, -57.4). **Vector** length 56.9, 9.13% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +13.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.4 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.1 | +0.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.6 | -14.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.8 | -14.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.8 | -8.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | cell growth regulator with EF-hand domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:27,098,889-27,119,128 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGR11 |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99674](https://www.uniprot.org/uniprotkb/Q99674) (Cell growth regulator with EF hand domain protein 1):

> Mediates cell-cell adhesion in a calcium-dependent manner (By similarity). Able to inhibit growth in several cell lines.

**Summary**, from NCBI Gene [10669](https://www.ncbi.nlm.nih.gov/gene/10669):

> Predicted to enable calcium ion binding activity. Predicted to be involved in negative regulation of cell population proliferation. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16962](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16962) · Entrez [10669](https://www.ncbi.nlm.nih.gov/gene/10669) · UniProt [Q99674](https://www.uniprot.org/uniprotkb/Q99674) · Ensembl [ENSG00000138028](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138028)

## Data

Gene col 6108: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6108); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6108, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6108]; `tensor/DDL_lfc|DDL_z.npy` [6108]; `embed/gene_vectors.npy` [6108]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6108 or target_col == 6108). Every well: [[CGREF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CGREF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
