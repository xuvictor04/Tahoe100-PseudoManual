---
symbol: "RHOBTB1"
type: "gene"
col: 1019
ensembl_id: "ENSG00000072422"
name: "Rho related BTB domain containing 1"
location: "10q21.2"
module: 106
arm: "+"
pooled_cpm: 12.29
n_lines_expressing: 42
n_dd_up: 11
n_dd_down: 23
n_dd_up_clean: 11
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# RHOBTB1

*Rho related BTB domain containing 1* — 10q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.88× (z +11.2, q 3e-26, up in 31 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.395× (z -11.7, q 9e-29, down in 28 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.436× (z -10.4, q 3e-23, down in 33 of 40 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCOLCE2]] (+0.58, fdr 3e-05), [[DZIP1L]] (+0.58, fdr 1e-04), [[SIRPA]] (+0.57, fdr 5e-05); moves opposite to [[MFSD4B]] (-0.51, fdr 5e-04), [[ATG7]] (-0.45, fdr 5e-05), [[PDPK1]] (-0.44, fdr 1e-04).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NRCAM]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SLC39A8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1019.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.88×** | +11.2 | 3e-26 | 31/40 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +8.4 | 9e-15 | 27/38 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +6.7 | 3e-09 | 25/38 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +5.3 | 1e-05 | 19/40 (HOP62, SW480, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.006 | 11/38 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.38×** | +3.9 | 0.008 | 10/38 (C32, A-172, …) | inconsistent across doses | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.80×** | +3.9 | 0.009 | 13/39 (SW480, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.057 | 14/39 (A498, SK-MEL-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.057 | 8/38 (SW 900, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.075 | 12/38 (A-172, PANC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.084 | 7/38 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1019.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.395×** | -11.7 | 9e-29 | 28/37 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.544×** | -10.8 | 7e-25 | 29/38 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.436×** | -10.4 | 3e-23 | 33/40 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.487×** | -9.0 | 2e-17 | 25/37 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.512×** | -8.4 | 5e-15 | 30/38 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.541×** | -7.4 | 1e-11 | 22/38 (NCI-H460, A549, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.361×** | -6.7 | 2e-09 | 23/39 (SW 900, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.652×** | -5.4 | 5e-06 | 20/38 (SW 900, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.699×** | -4.5 | 4e-04 | 17/38 (NCI-H460, HS-578T, …) | two highest doses |  |
| [[Artesunate (drug)]] 5 µM |  | **0.793×** | -4.1 | 0.002 | 14/40 (SHP-77, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.730×** | -4.0 | 0.004 | 14/38 (SK-MEL-2, H4, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.804×** | -3.9 | 0.005 | 12/39 (SW480, NCI-H460, …) | top dose only | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **0.564×** | -3.8 | 0.007 | 17/36 (KATO III, A498, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.738×** | -3.7 | 0.009 | 19/39 (NCI-H460, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.749×** | -3.6 | 0.010 | 15/38 (NCI-H460, NCI-H661, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.745×** | -3.6 | 0.013 | 16/38 (J82, PANC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.599×** | -3.4 | 0.022 | 13/36 (SW480, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.604×** | -3.3 | 0.024 | 9/38 (SW 900, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.634×** | -3.0 | 0.070 | 9/35 (Hs 766T, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.784×** | -2.9 | 0.079 | 6/40 (NCI-H460, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1019. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.8 | 0 | 10 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -13.6) |
| [[A549 (line)]] | wt | 21.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 9.44 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 4.62× (z +12.1) | — |
| [[A-172 (line)]] | wt | 41.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 31.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -10.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -9.3) |
| [[HT-29 (line)]] | alt | 13.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.117× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 10.5 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.36× (z +10.5) | [[Digitoxin (drug)]] 5 µM 0.160× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 20.9 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0293× (z -19.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[CFPAC-1 (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0634× (z -13.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -8.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-427 (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 56.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1019), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCOLCE2]] | +0.58 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[DZIP1L]] | +0.58 | +0.61 / +0.36 | both halves | 1e-04 |  |
| [[SIRPA]] | +0.57 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[SLC35D1]] | +0.56 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[GNAI1]] | +0.55 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[SLC39A8]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[HECW2]] | +0.51 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[ADGRG2]] | +0.50 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[GAB3]] | +0.50 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[P3H2-AS1]] | +0.50 | +0.42 / +0.33 | both halves | 1e-04 |  |
| [[TRIM7]] | +0.50 | +0.37 / +0.30 | both halves | 2e-04 |  |
| [[DIPK1A]] | +0.49 | +0.41 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD4B]] | -0.51 | -0.42 / -0.24 | both halves | 5e-04 |  |
| [[ATG7]] | -0.45 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[PDPK1]] | -0.44 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[GALE]] | -0.42 | -0.45 / -0.26 | both halves | 4e-04 |  |
| [[CD82]] | -0.41 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[RAPGEF6]] | -0.40 | -0.42 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRCAM]] | B | NRCAM activity raises RHOBTB1's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 1.89× lower at baseline in the lines without NRCAM | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC39A8]] | B | RHOBTB1 activity raises SLC39A8's level | lines that do not express RHOBTB1 (8) vs lines expressing it (42) | 2.87× lower at baseline in the lines without RHOBTB1 | 0.049 | ⚠ within organs, on part of the lines; also absent: KLF12, LAMB1, PLCB4 |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.304). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.2, 30.8); signed map (17.5, 23.0). **Vector** length 72.1, 14.6% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +11.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.7 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.4 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.9 | +1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +2.2 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.6 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.3 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.1 | -7.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.5 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | Rho related BTB domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.2 — chr10:60,869,438-61,001,440 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0740 |
| Gene groups (HGNC) | Rho family GTPases; BTB domain containing |
| Reactome | 5 pathways, smallest: RHOBTB1 GTPase cycle; RHOBTB GTPase Cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

UniProt [O94844](https://www.uniprot.org/uniprotkb/O94844) carries no function annotation.

**Summary**, from NCBI Gene [9886](https://www.ncbi.nlm.nih.gov/gene/9886):

> The protein encoded by this gene belongs to the Rho family of the small GTPase superfamily. It contains a GTPase domain, a proline-rich region, a tandem of 2 BTB (broad complex, tramtrack, and bric-a-brac) domains, and a conserved C-terminal region. The protein plays a role in small GTPase-mediated signal transduction and the organization of the actin filament system. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:18738](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18738) · Entrez [9886](https://www.ncbi.nlm.nih.gov/gene/9886) · UniProt [O94844](https://www.uniprot.org/uniprotkb/O94844) · Ensembl [ENSG00000072422](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072422)

## Data

Gene col 1019: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1019); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1019, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1019]; `tensor/DDL_lfc|DDL_z.npy` [1019]; `embed/gene_vectors.npy` [1019]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1019 or target_col == 1019). Every well: [[RHOBTB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHOBTB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
