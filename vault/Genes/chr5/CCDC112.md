---
symbol: "CCDC112"
type: "gene"
col: 8906
ensembl_id: "ENSG00000164221"
name: "coiled-coil domain containing 112"
location: "5q22.3"
module: 46
arm: "-"
pooled_cpm: 48.24
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# CCDC112

*coiled-coil domain containing 112* — 5q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.15× (z +13.7, q 2e-40, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.599× (z -8.6, q 5e-15, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRXL2C]] (+0.68, fdr 1e-05), [[MAST1]] (+0.67, fdr 1e-05), [[CAMKK1]] (+0.67, fdr 1e-05); moves opposite to [[VPS52]] (-0.67, fdr 9e-05), [[XNDC1N-ZNF705EP-ALG1L9P]] (-0.66, fdr 3e-05), [[C5orf15]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SYP]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8906.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.15×** | +13.7 | 2e-40 | 48/48 (AsPC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.15×** | +13.7 | 2e-40 | 46/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.01×** | +13.2 | 2e-37 | 47/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.03×** | +12.0 | 8e-31 | 46/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.08×** | +8.7 | 2e-16 | 42/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.86×** | +7.4 | 1e-11 | 42/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +6.1 | 7e-08 | 40/48 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +4.7 | 2e-04 | 27/46 (LoVo, HT-29, …) | two highest doses | cell-cycle shift (explains ~18% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +4.6 | 2e-04 | 27/48 (SW480, LoVo, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.99×** | +4.3 | 1e-03 | 35/48 (NCI-H2347, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.005 | 24/48 (HS-578T, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.33×** | +3.5 | 0.026 | 23/48 (LS 180, NCI-H1573, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.049 | 21/48 (LS 180, Panc 03.27, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.080 | 21/48 (NCI-H1792, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **1.30×** | +3.1 | 0.080 | 20/40 (LoVo, NCI-H2030, …) | two highest doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8906.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -8.6 | 5e-15 | 38/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.375×** | -6.1 | 3e-07 | 34/49 (PANC-1, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.872× | -5.1 | 6e-05 | 8/49 (CFPAC-1, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -4.7 | 3e-04 | 29/48 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.483×** | -4.5 | 7e-04 | 29/48 (LS 180, A-172, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.767× | -3.1 | 0.17 | 22/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8906. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 45.3 | 7 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.37× (z +12.7) | — |
| [[NCI-H2347 (line)]] | alt | 62.3 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 3.20× (z +16.1) | — |
| [[AsPC-1 (line)]] | alt | 72.2 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.08× (z +13.9) | — |
| [[HT-29 (line)]] | alt | 45.8 | 4 | 1 | [[Panobinostat (drug)]] 0.5 µM 4.78× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -10.9) |
| [[LS 180 (line)]] | wt | 60.9 | 5 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.27× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 45.1 | 4 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.78× (z +10.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 35.6 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.89× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 33.5 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.74× (z +11.5) | — |
| [[KATO III (line)]] | alt | 41.9 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.19× (z +13.5) | — |
| [[PANC-1 (line)]] | alt | 32.3 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.99× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -11.8) |
| [[SW1417 (line)]] | alt | 51.2 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.80× (z +11.4) | — |
| [[SW480 (line)]] | alt | 71.0 | 3 | 1 | [[Belinostat (drug)]] 5 µM 3.58× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -8.5) |
| [[H4 (line)]] | wt | 35.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.96× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 73.9 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.11× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 24.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +13.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.08× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 48.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.45× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 24.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.56× (z +10.2) | — |
| [[C32 (line)]] | wt | 19.3 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.53× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 70.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 95.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -10.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -9.4) |
| [[SW 1271 (line)]] | alt | 67.8 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0780× (z -9.1) |
| [[COLO 205 (line)]] | alt | 12.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 10.0× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 46.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.51× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 55.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -15.4) |
| [[SW 900 (line)]] | alt | 19.9 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.06× (z +8.6) | — |
| [[A-172 (line)]] | wt | 78.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 104 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8906), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRXL2C]] | +0.68 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[MAST1]] | +0.67 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[CAMKK1]] | +0.67 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[PKN1]] | +0.66 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[SYP]] | +0.66 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[BLVRA]] | +0.64 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[ANKRD27]] | +0.63 | +0.37 / +0.47 | both halves | 7e-05 |  |
| [[STX7]] | +0.62 | +0.33 / +0.51 | both halves | 1e-04 |  |
| [[SH3PXD2B]] | +0.62 | +0.33 / +0.46 | both halves | 1e-04 |  |
| [[TCAF1]] | +0.61 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[FBXL16]] | +0.60 | +0.25 / +0.46 | both halves | 4e-04 |  |
| [[PIGH]] | +0.60 | +0.35 / +0.45 | both halves | 1e-04 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS52]] | -0.67 | -0.36 / -0.57 | both halves | 9e-05 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | -0.66 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[C5orf15]] | -0.65 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[XNDC1N]] | -0.65 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[PNISR-AS1]] | -0.65 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[PBLD]] | -0.64 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[CRPPA]] | -0.63 | -0.26 / -0.51 | both halves | 4e-04 |  |
| [[SUMO3]] | -0.63 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[TOR1A]] | -0.61 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[PSME3IP1]] | -0.60 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[CYB561A3]] | -0.60 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[RPRD1B]] | -0.59 | -0.38 / -0.52 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYP]] | C | SYP activity raises CCDC112's level | lines that do not express SYP (4) vs lines expressing it (46) | 1.52× lower at baseline in the lines without SYP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[ULBP3]] | C | ULBP3 activity raises CCDC112's level | lines that do not express ULBP3 (3) vs lines expressing it (47) | 2.03× lower at baseline in the lines without ULBP3 | 0.099 | ⚠ few lines (3 vs 47); across organs; also absent: SPDL1, ARHGAP10, CDC20; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **-** arm (projection on the module's main direction -0.517). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (8.4, -0.8); signed map (-26.8, 22.1). **Vector** length 133, 44.7% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.6 | +12.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.9 | +7.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +8.3 | +8.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.5 | +13.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.0 | +13.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.9 | +4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.9 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.9 | +3.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.8 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.7 | -8.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -10.1 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -9.1 | -2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -8.5 | -2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -6.5 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.7 | -1.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.7 | -2.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 112 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.3 — chr5:115,267,190-115,296,693 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC39633 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

UniProt [Q8NEF3](https://www.uniprot.org/uniprotkb/Q8NEF3) carries no function annotation.

**Summary**, from NCBI Gene [153733](https://www.ncbi.nlm.nih.gov/gene/153733):

> Located in centriolar satellite. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28599](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28599) · Entrez [153733](https://www.ncbi.nlm.nih.gov/gene/153733) · UniProt [Q8NEF3](https://www.uniprot.org/uniprotkb/Q8NEF3) · Ensembl [ENSG00000164221](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164221)

## Data

Gene col 8906: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8906); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8906, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8906]; `tensor/DDL_lfc|DDL_z.npy` [8906]; `embed/gene_vectors.npy` [8906]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8906 or target_col == 8906). Every well: [[CCDC112 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC112.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
