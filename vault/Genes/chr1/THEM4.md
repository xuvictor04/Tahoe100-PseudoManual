---
symbol: "THEM4"
type: "gene"
col: 8256
ensembl_id: "ENSG00000159445"
name: "thioesterase superfamily member 4"
location: "1q21.3"
module: 107
arm: "+"
pooled_cpm: 27.6
n_lines_expressing: 45
n_dd_up: 17
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# THEM4

*thioesterase superfamily member 4* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.38× (z +16.5, q 0e+00, up in 37 of 39 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.76× (z +15.7, q 0e+00, up in 40 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.567× (z -11.2, q 3e-26, down in 31 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.408× (z -9.2, q 7e-18, down in 28 of 44 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEX7]] (+0.58, fdr 1e-05), [[ZSWIM7]] (+0.52, fdr 2e-05), [[DTWD1]] (+0.52, fdr 1e-05); moves opposite to [[DCDC1]] (-0.54, fdr 6e-04), [[RNF167]] (-0.51, fdr 2e-05), [[NAPA]] (-0.47, fdr 1e-04).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Selinexor (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8256.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.38×** | +16.5 | 0e+00 | 37/39 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +15.7 | 0e+00 | 40/43 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.05×** | +14.2 | 2e-43 | 36/43 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.98×** | +13.4 | 6e-39 | 34/43 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.80×** | +11.6 | 8e-29 | 35/42 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +9.2 | 3e-18 | 30/43 (A498, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +8.8 | 1e-16 | 28/42 (A498, Hs 766T, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +8.4 | 4e-15 | 22/42 (NCI-H2030, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +7.6 | 1e-12 | 28/42 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.25×** | +6.3 | 2e-08 | 22/43 (NCI-H2030, RKO, …) | top dose only | low cells (technical?) |
| [[Amsacrine (drug)]] 5 µM |  | **1.23×** | +5.8 | 3e-07 | 17/43 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +5.3 | 4e-06 | 8/29 (NCI-H1792, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.29×** | +5.1 | 2e-05 | 14/43 (NCI-H1792, LS 180, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.24×** | +4.2 | 0.001 | 15/42 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +4.1 | 0.002 | 10/43 (A498, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.010 | 9/43 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.20× | +3.6 | 0.011 | 6/42 (LS 180, HCT15, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.5 | 0.013 | 9/43 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.5 | 0.015 | 13/43 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8256.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.567×** | -11.2 | 3e-26 | 31/41 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.408×** | -9.2 | 7e-18 | 28/44 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.637×** | -8.9 | 1e-16 | 25/43 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.701×** | -7.0 | 3e-10 | 21/42 (SNU-423, NCI-H460, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.610×** | -5.1 | 4e-05 | 21/40 (LS 180, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.777×** | -5.0 | 6e-05 | 19/42 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.631×** | -4.8 | 2e-04 | 18/37 (C32, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.778×** | -4.7 | 2e-04 | 14/43 (C32, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.820×** | -3.8 | 0.010 | 16/40 (SNU-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Rifaximin (drug)]] 0.05 µM |  | **0.829×** | -3.4 | 0.034 | 8/42 (A-172, NCI-H23, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.840× | -3.3 | 0.047 | 11/41 (CHP-212, COLO 205, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.856× | -3.1 | 0.100 | 10/42 (PANC-1, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8256. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 47.7 | 3 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.80× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.313× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.483× (z -9.1) |
| [[Hs 766T (line)]] | wt | 37.5 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +13.4) | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[SW480 (line)]] | alt | 37.1 | 2 (1 ⚠) | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.02× (z +12.0) | [[Digitoxin (drug)]] 5 µM 0.293× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.439× (z -9.9) |
| [[A498 (line)]] | wt | 25.2 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.59× (z +11.1) | — |
| [[PANC-1 (line)]] | alt | 38.5 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -15.8) |
| [[A-172 (line)]] | wt | 10.6 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.20× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 33.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +12.6) | — |
| [[LoVo (line)]] | wt | 25.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.91× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 32.8 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 2.56× (z +9.4) | — |
| [[J82 (line)]] | alt | 16.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -8.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 41.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +12.3) | — |
| [[NCI-H2030 (line)]] | alt | 68.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +13.6) | — |
| [[SHP-77 (line)]] | alt | 39.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change |
| [[CFPAC-1 (line)]] | alt | 20.5 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.66× (z +10.5) ⚠ toxic | — |
| [[LS 180 (line)]] | wt | 26.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.02× (z +8.5) ⚠ toxic | — |
| [[NCI-H23 (line)]] | alt | 55.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SNU-1 (line)]] | wt | 55.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0794× (z -16.9) ⚠ toxic |
| [[A-427 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.78 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.99 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 47.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8256), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX7]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[ZSWIM7]] | +0.52 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[DTWD1]] | +0.52 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[MTFMT]] | +0.51 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[ZNF786]] | +0.51 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[GTF2H5]] | +0.50 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[SDHAF4]] | +0.50 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[DMAC1]] | +0.49 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[ZNF280C]] | +0.49 | +0.49 / +0.59 | both halves | 2e-05 |  |
| [[TRIM13]] | +0.48 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[ZC3H8]] | +0.48 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[MIOS]] | +0.48 | +0.59 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCDC1]] | -0.54 | -0.22 / -0.41 | both halves | 6e-04 |  |
| [[RNF167]] | -0.51 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[NAPA]] | -0.47 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[APH1A]] | -0.47 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[GTF2F1]] | -0.44 | -0.22 / -0.58 | both halves | 6e-04 |  |
| [[NUCB1]] | -0.44 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ULK4]] | -0.44 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[IFT43]] | -0.43 | -0.22 / -0.41 | both halves | 6e-04 |  |
| [[LARP4B]] | -0.43 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[STX4]] | -0.42 | -0.25 / -0.50 | both halves | 4e-04 |  |
| [[MSRB1]] | -0.42 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[SPAG16]] | -0.42 | -0.25 / -0.41 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Selinexor (drug)]] 5 µM | B | THEM4 activity lowers the cells' numbers under Selinexor 5 µM (makes them more sensitive) | lines that do not express THEM4 (5) vs lines expressing it (43) | the lines without THEM4: 1.41× the cells of the other lines | 0.087 | ⚠ across organs; also absent: PIP4P2, CBR1 |

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction -0.0422). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-29.0, 3.7); signed map (-15.8, -14.7). **Vector** length 73.4, 13.5% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +8.2 | +16.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +15.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +11.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.7 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | +5.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +3.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.1 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | -5.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.7 | -3.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | thioesterase superfamily member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,870,866-151,909,637 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CTMP |
| Gene groups (HGNC) | Thioesterase superfamily; Thioester hydrolases |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 22 pathways, smallest: Activation of AKT2; CD28 dependent PI3K/Akt signaling; VEGFR2 mediated vascular permeability |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T1C6](https://www.uniprot.org/uniprotkb/Q5T1C6) (Acyl-coenzyme A thioesterase THEM4):

> Has acyl-CoA thioesterase activity towards medium and long-chain (C14 to C18) fatty acyl-CoA substrates, and probably plays a role in mitochondrial fatty acid metabolism. Plays a role in the apoptotic process, possibly via its regulation of AKT1 activity. According to PubMed:11598301, inhibits AKT1 phosphorylation and activity. According to PubMed:17615157, enhances AKT1 activity by favoring its phosphorylation and translocation to plasma membrane.

**Summary**, from NCBI Gene [117145](https://www.ncbi.nlm.nih.gov/gene/117145):

> Protein kinase B (PKB) is a major downstream target of receptor tyrosine kinases that signal via phosphatidylinositol 3-kinase. Upon cell stimulation, PKB is translocated to the plasma membrane, where it is phosphorylated in the C-terminal regulatory domain. The protein encoded by this gene negatively regulates PKB activity by inhibiting phosphorylation. Transcription of this gene is commonly downregulated in glioblastomas. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17947](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17947) · Entrez [117145](https://www.ncbi.nlm.nih.gov/gene/117145) · UniProt [Q5T1C6](https://www.uniprot.org/uniprotkb/Q5T1C6) · Ensembl [ENSG00000159445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159445)

## Data

Gene col 8256: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8256); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8256, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8256]; `tensor/DDL_lfc|DDL_z.npy` [8256]; `embed/gene_vectors.npy` [8256]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8256 or target_col == 8256). Every well: [[THEM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THEM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
