---
symbol: "SLCO2B1"
type: "gene"
col: 6020
ensembl_id: "ENSG00000137491"
name: "solute carrier organic anion transporter family member 2B1"
location: "11q13.4"
module: 61
arm: "+"
pooled_cpm: 6.26
n_lines_expressing: 29
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# SLCO2B1

*solute carrier organic anion transporter family member 2B1* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 17.0× (z +34.9, q 0e+00, up in 20 of 23 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (SNU-423 0.0674×); [[Vortioxetine (drug)]] 5 µM in 1 line (SNU-423 0.0885×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC9A9]] (+0.71, fdr 7e-06), [[CLIC2]] (+0.69, fdr 8e-06), [[TRIML2]] (+0.66, fdr 1e-05); moves opposite to [[FBH1]] (-0.55, fdr 3e-05), [[DHTKD1]] (-0.55, fdr 6e-05), [[MARF1]] (-0.53, fdr 4e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC01320]] → it (grade B ⚠); 4 go from it, the strongest it → [[DNAH6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6020.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **17.0×** | +34.9 | 0e+00 | 20/23 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **9.35×** | +19.5 | 0e+00 | 21/24 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **9.06×** | +19.2 | 0e+00 | 17/23 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.26×** | +17.8 | 0e+00 | 17/22 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **7.60×** | +17.0 | 0e+00 | 16/23 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **3.34×** | +14.8 | 0e+00 | 21/26 (A549, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.41×** | +10.7 | 1e-24 | 6/15 (A-172, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.20×** | +9.4 | 6e-19 | 0/4 | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.04×** | +9.3 | 9e-19 | 0/4 | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.62×** | +8.4 | 3e-15 | 20/25 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.93×** | +8.1 | 3e-14 | 8/26 (A549, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.24×** | +7.0 | 1e-10 | 14/26 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.96×** | +5.9 | 2e-07 | 11/26 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.94×** | +5.8 | 3e-07 | 11/26 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.84×** | +5.0 | 2e-05 | 8/25 (SHP-77, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.72×** | +4.7 | 9e-05 | 8/25 (SNU-423, NCI-H2030, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +4.4 | 3e-04 | 8/26 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +4.3 | 4e-04 | 3/21 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.65×** | +4.3 | 5e-04 | 8/25 (SK-MEL-2, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6020.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (SNU-423 0.0674×); [[Vortioxetine (drug)]] 5 µM in 1 line (SNU-423 0.0885×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.670× | -3.5 | 0.20 | 6/25 (RPMI-7951, NCI-H23, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.762× | -3.4 | 0.20 | 6/26 (KATO III, COLO 205, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.694× | -3.2 | 0.24 | 9/25 (RPMI-7951, SNU-423, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.05 µM |  | 0.696× | -3.0 | 0.37 | 3/25 (HT-29, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6020. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.15 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 83.2× (z +17.7) | — |
| [[SK-MEL-2 (line)]] | alt | 9.33 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +12.1) | — |
| [[SNU-423 (line)]] | alt | 7.73 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +13.2) | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0674× (z -8.8) |
| [[HS-578T (line)]] | alt | 2.63 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 54.7× (z +13.5) | — |
| [[LoVo (line)]] | wt | 2.32 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.2× (z +12.5) | — |
| [[A549 (line)]] | wt | 6.36 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.3× (z +13.6) | — |
| [[CFPAC-1 (line)]] | alt | 1.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.3× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 33.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 7.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +10.8) | — |
| [[J82 (line)]] | alt | 1.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 52.7× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 5.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.22× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 2.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.9× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 2.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +10.5) | — |
| [[A-427 (line)]] | wt | 0.813 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.913 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.928 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.911 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.785 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.807 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.34 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6020), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A9]] | +0.71 | +0.74 / +0.62 | both halves | 7e-06 | pathway: SLC-mediated transmembrane transport |
| [[CLIC2]] | +0.69 | +0.57 / +0.65 | both halves | 8e-06 |  |
| [[TRIML2]] | +0.66 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[LINC02516]] | +0.65 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[LINC02328]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[ANOS2P]] | +0.65 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[LINC01933]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[GPR158]] | +0.63 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[FBXW10B]] | +0.62 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[NR1H4]] | +0.61 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[LINC01483]] | +0.61 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[LINC02208]] | +0.61 | +0.66 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBH1]] | -0.55 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[DHTKD1]] | -0.55 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[MARF1]] | -0.53 | -0.60 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01320]] | B | LINC01320 activity raises SLCO2B1's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 3.22× lower at baseline in the lines without LINC01320 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAH6]] | B | SLCO2B1 activity raises DNAH6's level | lines that do not express SLCO2B1 (21) vs lines expressing it (29) | 1.46× lower at baseline in the lines without SLCO2B1 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000253227, ENSG00000254261, PDE1C; maybe low, not absent |
| [[FBXW10B]] | B | SLCO2B1 activity raises FBXW10B's level | lines that do not express SLCO2B1 (21) vs lines expressing it (29) | 2.07× lower at baseline in the lines without SLCO2B1 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000253227, ENSG00000254261, PDE1C; maybe low, not absent |
| [[ALOX12P2-1]] | B | SLCO2B1 activity raises ALOX12P2-1's level | lines that do not express SLCO2B1 (21) vs lines expressing it (29) | 2.02× lower at baseline in the lines without SLCO2B1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000253227, ENSG00000254261, PDE1C; maybe low, not absent |
| [[AKR1C3]] | B | SLCO2B1 activity raises AKR1C3's level | lines that do not express SLCO2B1 (21) vs lines expressing it (29) | 2.37× lower at baseline in the lines without SLCO2B1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000253227, ENSG00000254261, PDE1C; maybe low, not absent |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.6, 25.6); signed map (40.6, 20.4). **Vector** length 61.9, 13.6% of its response variance represented; |z| ≥ 3 in 728 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +14.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +34.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +19.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +17.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +19.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +8.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +2.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -1.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -1.7 | +3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +0.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -3.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier organic anion transporter family member 2B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:75,100,563-75,206,549 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OATP-B, OATP2B1; previously SLC21A9 |
| Gene groups (HGNC) | Solute carrier organic anion transporter family |
| Reactome | 9 pathways, smallest: Atorvastatin ADME; Organic anion transport by SLCO transporters; Heme degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [O94956](https://www.uniprot.org/uniprotkb/O94956) (Solute carrier organic anion transporter family member 2B1):

> Mediates the Na(+)-independent transport of steroid sulfate conjugates and other specific organic anions. Responsible for the transport of estrone 3-sulfate (E1S) through the basal membrane of syncytiotrophoblast, highlighting a potential role in the placental absorption of fetal-derived sulfated steroids including the steroid hormone precursor dehydroepiandrosterone sulfate (DHEA-S). Also facilitates the uptake of sulfated steroids at the basal/sinusoidal membrane of hepatocytes, therefore …

**Summary**, from NCBI Gene [11309](https://www.ncbi.nlm.nih.gov/gene/11309):

> This locus encodes a member of the organic anion-transporting polypeptide family of membrane proteins. The protein encoded by this locus may function in regulation of placental uptake of sulfated steroids. Alternatively spliced transcript variants have been described. [provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:10962](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10962) · Entrez [11309](https://www.ncbi.nlm.nih.gov/gene/11309) · UniProt [O94956](https://www.uniprot.org/uniprotkb/O94956) · Ensembl [ENSG00000137491](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137491)

## Data

Gene col 6020: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6020); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6020, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6020]; `tensor/DDL_lfc|DDL_z.npy` [6020]; `embed/gene_vectors.npy` [6020]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6020 or target_col == 6020). Every well: [[SLCO2B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLCO2B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
