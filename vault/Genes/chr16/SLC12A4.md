---
symbol: "SLC12A4"
type: "gene"
col: 4473
ensembl_id: "ENSG00000124067"
name: "solute carrier family 12 member 4"
location: "16q22.1"
module: 101
arm: "+"
pooled_cpm: 22.94
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# SLC12A4

*solute carrier family 12 member 4* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.50× (z +8.5, q 8e-15, up in 26 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.725× (z -6.8, q 8e-09, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LCAT]] (+0.83, fdr 7e-06, ⚠ read-through risk), [[CC2D1B]] (+0.63, fdr 7e-06), [[ARVCF]] (+0.63, fdr 7e-06), [[ARHGDIA]] (+0.59, fdr 1e-05); moves opposite to [[RAVER2]] (-0.56, fdr 1e-05), [[PLBD1]] (-0.52, fdr 3e-05), [[PEBP1]] (-0.51, fdr 3e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HOMER3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4473.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +8.5 | 8e-15 | 26/46 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +6.7 | 5e-09 | 24/46 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.44×** | +5.4 | 1e-05 | 27/47 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 0.003 | 16/46 (HT-29, HS-578T, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.014 | 20/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.014 | 17/47 (NCI-H1573, LoVo, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.015 | 13/45 (HCT15, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.020 | 18/47 (RKO, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.027 | 14/47 (HEC-1-A, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.028 | 14/46 (HT-29, C-33 A, …) | two highest doses | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.24×** | +3.2 | 0.057 | 14/46 (NCI-H1573, HT-29, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.24×** | +3.2 | 0.057 | 11/46 (A-427, SW48, …) | inconsistent across doses | position effect removed |
| [[Fulvestrant (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.089 | 12/46 (NCI-H2030, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.089 | 15/47 (A-427, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4473.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -6.8 | 8e-09 | 26/46 (HEC-1-A, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.751×** | -6.0 | 5e-07 | 23/47 (Hs 766T, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.620×** | -3.7 | 0.032 | 13/46 (NCI-H23, C-33 A, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.749×** | -3.7 | 0.032 | 13/31 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.788×** | -3.6 | 0.042 | 11/47 (NCI-H2030, BT-474, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.769×** | -3.4 | 0.073 | 15/45 (RKO, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.803×** | -3.3 | 0.082 | 12/47 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 5 µM |  | **0.776×** | -3.2 | 0.082 | 14/47 (CHP-212, NCI-H1573, …) | top dose only | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.777×** | -3.2 | 0.082 | 17/46 (A-172, NCI-H1573, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.808×** | -3.2 | 0.086 | 17/47 (HepG2/C3A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.811×** | -3.1 | 0.092 | 17/43 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4473. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 24.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 27.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.238× (z -8.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 27.1 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.16× (z +9.5) | — |
| [[A-427 (line)]] | wt | 36.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 26.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -9.2) |
| [[HOP62 (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.305× (z -9.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -9.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 37.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 20.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -9.3) |
| [[PANC-1 (line)]] | alt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +12.5) | — |
| [[SW1417 (line)]] | alt | 15.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -8.9) |
| [[A-172 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4473), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCAT]] | +0.83 | +0.76 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_XENOBIOTIC_METABOLISM; STRING 628; ⚠ **readthrough risk**: LCAT lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[CC2D1B]] | +0.63 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ARVCF]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ARHGDIA]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[GPSM1]] | +0.58 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[RHOT2]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[IPO13]] | +0.57 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[SLC39A13]] | +0.56 | +0.48 / +0.52 | both halves | 2e-05 | STRING 406 |
| [[RHBDF1]] | +0.56 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TUBB6]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | +0.56 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[FAAP100]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[FAM83G]] | +0.55 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAVER2]] | -0.56 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[PLBD1]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[PEBP1]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ARL6IP5]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[ZNF148]] | -0.49 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[MRPS30]] | -0.48 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[PPP1CB]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[HSF2]] | -0.48 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[SH3BGRL]] | -0.48 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[SCARB2]] | -0.48 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[DENND4C]] | -0.48 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[MRPS30-DT]] | -0.48 | -0.35 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOMER3]] | C | HOMER3 activity raises SLC12A4's level | lines that do not express HOMER3 (3) vs lines expressing it (47) | 2.75× lower at baseline in the lines without HOMER3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CHST3, RGS10, ENSG00000290876; maybe low, not absent; its own permutation p |
| [[PPP3CB]] | C | PPP3CB's natural level strengthens SLC12A4's drug response | PPP3CB's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.16; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[DNAJB5]] | C | DNAJB5 activity raises SLC12A4's level | lines that do not express DNAJB5 (3) vs lines expressing it (47) | 1.92× lower at baseline in the lines without DNAJB5 | 0.094 | ⚠ few lines (3 vs 47); across organs; also absent: CEP170, SRGAP2C, TLCD5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.491). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.7, -0.7); signed map (-4.1, 24.5). **Vector** length 102, 23.6% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +8.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.6 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | -3.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +4.2 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.2 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.9 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.9 | +2.8 |
|  | [[vincristine (drug)]] 5 µM |  | +3.6 | +2.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -3.5 | -6.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.5 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -3.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.9 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.4 | -2.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 12 member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,943,474-67,969,601 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KCC1 |
| Gene groups (HGNC) | Solute carrier family 12 |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 4 pathways, smallest: Cation-coupled Chloride cotransporters; SLC-mediated transport of inorganic anions; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UP95](https://www.uniprot.org/uniprotkb/Q9UP95) (Solute carrier family 12 member 4):

> Mediates electroneutral potassium-chloride cotransport when activated by cell swelling. May contribute to cell volume homeostasis in single cells. May be involved in the regulation of basolateral Cl(-) exit in NaCl absorbing epithelia (By similarity).; [Isoform 4]: No transporter activity.

**Summary**, from NCBI Gene [6560](https://www.ncbi.nlm.nih.gov/gene/6560):

> This gene encodes a member of the SLC12A transporter family. The encoded protein mediates the coupled movement of potassium and chloride ions across the plasma membrane. This gene is expressed ubiquitously. Multiple alternatively spliced transcript variants encoding distinct isoforms have been found for this gene. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:10913](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10913) · Entrez [6560](https://www.ncbi.nlm.nih.gov/gene/6560) · UniProt [Q9UP95](https://www.uniprot.org/uniprotkb/Q9UP95) · Ensembl [ENSG00000124067](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124067)

## Data

Gene col 4473: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4473); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4473, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4473]; `tensor/DDL_lfc|DDL_z.npy` [4473]; `embed/gene_vectors.npy` [4473]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4473 or target_col == 4473). Every well: [[SLC12A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC12A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
