---
symbol: "SYTL2"
type: "gene"
col: 6026
ensembl_id: "ENSG00000137501"
name: "synaptotagmin like 2"
location: "11q14.1"
module: 224
arm: "+"
pooled_cpm: 48.33
n_lines_expressing: 43
n_dd_up: 42
n_dd_down: 28
n_dd_up_clean: 40
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 6
direction_downstream: 11
tags: ["gene", "module/224"]
generated_by: "tahoemap"
---

# SYTL2

*synaptotagmin like 2* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.07× (z +13.4, q 4e-38, up in 37 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.559× (z -7.6, q 1e-11, down in 24 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.564× (z -7.5, q 2e-11, down in 28 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLK2]] (+0.61, fdr 7e-06), [[EXT1]] (+0.61, fdr 1e-05), [[CPA4]] (+0.60, fdr 1e-05); moves opposite to [[PXYLP1]] (-0.54, fdr 3e-05), [[DPY19L3]] (-0.52, fdr 1e-05), [[TMEM164]] (-0.51, fdr 3e-05).
> It is in [[Module 224]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MYOF]] → it (grade B ⚠); 11 go from it, the strongest it → [[PLD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 2 with an alert ⚠; shown: the 15 strongest. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6026.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.07×** | +13.4 | 4e-38 | 37/41 (SW1417, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.07×** | +9.5 | 9e-19 | 27/41 (AsPC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.03×** | +9.2 | 7e-18 | 32/41 (SW1417, J82, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.99×** | +8.9 | 6e-17 | 28/41 (AsPC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.97×** | +8.8 | 2e-16 | 37/41 (SW1417, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +8.7 | 5e-16 | 25/40 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.89×** | +8.3 | 8e-15 | 28/41 (AsPC-1, J82, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.76×** | +7.1 | 1e-10 | 25/40 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.64×** | +6.8 | 6e-10 | 26/41 (NCI-H1573, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.53×** | +6.6 | 2e-09 | 26/41 (NCI-H1573, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.52×** | +6.0 | 9e-08 | 25/41 (NCI-H1573, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.39×** | +5.9 | 1e-07 | 26/41 (LoVo, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +5.7 | 4e-07 | 17/40 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.55×** | +5.7 | 5e-07 | 28/40 (C32, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.37×** | +5.7 | 5e-07 | 24/41 (NCI-H1573, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6026.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.559×** | -7.6 | 1e-11 | 24/41 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.564×** | -7.5 | 2e-11 | 28/41 (LoVo, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.579×** | -7.2 | 2e-10 | 27/41 (LoVo, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.613×** | -6.4 | 2e-08 | 23/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.622×** | -6.2 | 6e-08 | 23/41 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.646×** | -5.4 | 6e-06 | 24/41 (BT-474, H4, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.668×** | -5.3 | 1e-05 | 21/41 (H4, NCI-H460, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.684×** | -5.0 | 4e-05 | 19/41 (H4, A498, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.766×** | -5.0 | 4e-05 | 23/40 (BT-474, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.700×** | -4.7 | 2e-04 | 22/41 (A498, H4, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.722×** | -4.3 | 1e-03 | 19/41 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.731×** | -4.1 | 0.002 | 18/41 (LoVo, H4, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.738×** | -4.0 | 0.002 | 20/41 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.807×** | -4.0 | 0.002 | 22/41 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.738×** | -4.0 | 0.002 | 18/41 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.729×** | -4.0 | 0.002 | 18/41 (H4, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6026. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 108 | 0 | 20 (1 ⚠) | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0887× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 81.9 | 1 | 17 (4 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.60× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -12.5) |
| [[A498 (line)]] | wt | 54.5 | 0 | 11 | — | [[Triamcinolone (drug)]] 0.5 µM 0.177× (z -12.1) |
| [[BT-474 (line)]] | alt | 237 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -14.2) |
| [[LoVo (line)]] | wt | 55.0 | 2 | 5 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.45× (z +11.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.221× (z -13.3) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.246× (z -12.9) |
| [[SW1417 (line)]] | alt | 114 | 3 | 4 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.84× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -11.9) |
| [[J82 (line)]] | alt | 28.8 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 3.36× (z +11.1) | — |
| [[LOX-IMVI (line)]] | wt | 44.9 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.168× (z -9.8) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.184× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 21.5 | 4 | 0 | [[Trametinib (drug)]] 5 µM 7.06× (z +11.4) | — |
| [[PANC-1 (line)]] | alt | 152 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.230× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.319× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 16.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 12.1× (z +11.7) | — |
| [[C32 (line)]] | wt | 132 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.05 µM 2.99× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 84.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.162× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.265× (z -9.0) |
| [[A-172 (line)]] | wt | 109 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.21× (z +10.1) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 16.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 49.8 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.91× (z +11.6) | — |
| [[A549 (line)]] | wt | 17.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.80× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 13.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.15× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 20.1 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 5.99× (z +8.5) | — |
| [[SW48 (line)]] | wt | 44.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.137× (z -9.1) |
| [[A-427 (line)]] | wt | 7.53 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.44 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.50 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.71 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6026), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLK2]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[EXT1]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CPA4]] | +0.60 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[LIMA1]] | +0.60 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[TNFRSF11B]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[NR3C1]] | +0.59 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[MMP13]] | +0.58 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[DST]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[AHR]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[DUSP14]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[TNFRSF9]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[SYNPO]] | +0.55 | +0.58 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PXYLP1]] | -0.54 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[DPY19L3]] | -0.52 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[TMEM164]] | -0.51 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[SEC14L2]] | -0.48 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[UBE2Q2]] | -0.48 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[SLC19A2]] | -0.47 | -0.38 / -0.38 | both halves | 6e-05 |  |
| [[RPGR]] | -0.45 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[SMG1P5]] | -0.45 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[NFATC2IP]] | -0.45 | -0.42 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYOF]] | B | MYOF activity raises SYTL2's level | lines that do not express MYOF (6) vs lines expressing it (44) | 3.65× lower at baseline in the lines without MYOF | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |
| [[MAP2K1]] | B | MAP2K1 activity lowers SYTL2's level | compounds that target MAP2K1: 4 of 4 raise it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 8.1% of all compounds | 0.042 | ⚠ off-target possible; 4 compounds |
| [[NR3C1]] | B | NR3C1 activity lowers SYTL2's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[PTGR1]] | B | PTGR1 activity raises SYTL2's level | lines that do not express PTGR1 (8) vs lines expressing it (42) | 2.02× lower at baseline in the lines without PTGR1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ANXA2, ZNF717 |
| [[RASEF]] | B | RASEF activity raises SYTL2's level | lines that do not express RASEF (20) vs lines expressing it (30) | 1.90× lower at baseline in the lines without RASEF | 0.091 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[ATXN1]] | C | ATXN1 activity raises SYTL2's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 4.00× lower at baseline in the lines without ATXN1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLD1]] | B | SYTL2 activity raises PLD1's level | lines that do not express SYTL2 (7) vs lines expressing it (43) | 3.87× lower at baseline in the lines without SYTL2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent |
| [[RASEF]] | B | SYTL2 activity raises RASEF's level | lines that do not express SYTL2 (7) vs lines expressing it (43) | 4.50× lower at baseline in the lines without SYTL2 | 0.016 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent |
| [[PRSS23]] | B | SYTL2 activity raises PRSS23's level | lines that do not express SYTL2 (7) vs lines expressing it (43) | 2.95× lower at baseline in the lines without SYTL2 | 0.029 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent |
| [[LXN]] | B | SYTL2 activity raises LXN's level | lines that do not express SYTL2 (7) vs lines expressing it (43) | 1.99× lower at baseline in the lines without SYTL2 | 0.050 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent |
| [[PLOD2]] | B | SYTL2 activity raises PLOD2's level | lines that do not express SYTL2 (7) vs lines expressing it (43) | 5.23× lower at baseline in the lines without SYTL2 | 0.054 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent |
| [[KIAA1217]] | B | SYTL2 activity raises KIAA1217's level | lines that do not express SYTL2 (7) vs lines expressing it (43) | 2.60× lower at baseline in the lines without SYTL2 | 0.071 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent |
| [[PTPDC1]] | B | SYTL2 activity lowers PTPDC1's level | lines that do not express SYTL2 (7) vs lines expressing it (43) | 1.51× higher at baseline in the lines without SYTL2 | 0.076 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent |
| cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM | B | SYTL2 activity lowers the cells' numbers under Tirabrutinib (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express SYTL2 (7) vs lines expressing it (41) | the lines without SYTL2: 1.23× the cells of the other lines | 0.077 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent |
| [[SPTLC3]] | B | SYTL2 activity raises SPTLC3's level | lines that do not express SYTL2 (7) vs lines expressing it (43) | 2.77× lower at baseline in the lines without SYTL2 | 0.081 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent |
| [[NFATC2IP]] | B | SYTL2 activity lowers NFATC2IP's level | lines that do not express SYTL2 (7) vs lines expressing it (43) | 1.54× higher at baseline in the lines without SYTL2 | 0.087 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent |
| [[ATXN1]] | C | SYTL2 activity raises ATXN1's level | lines that do not express SYTL2 (7) vs lines expressing it (43) | 4.69× lower at baseline in the lines without SYTL2 | 0.004 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 224]] — hypoxia; 9 genes; every member is in the + arm (projection on the module's main direction 0.827). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.8, 18.2); signed map (32.0, 33.5). **Vector** length 117, 32.5% of its response variance represented; |z| ≥ 3 in 1,566 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.8 | +13.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.6 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.5 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.4 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.2 | +7.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.0 | +6.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.9 | +6.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -4.9 | -4.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.7 | -4.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.5 | -3.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -4.5 | -5.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.4 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | synaptotagmin like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:85,694,224-85,811,159 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20163, FLJ21219, KIAA1597, exophilin-4, CHR11SYT, SLP2, SGA72M, MGC102768 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Synaptotagmin like tandem C2 proteins |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 3 pathways, smallest: Regulation of MITF-M-dependent genes involved in pigmentation; MITF-M-dependent gene expression; MITF-M-regulated melanocyte development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCH5](https://www.uniprot.org/uniprotkb/Q9HCH5) (Synaptotagmin-like protein 2):

> Isoform 1 acts as a RAB27A effector protein and plays a role in cytotoxic granule exocytosis in lymphocytes. It is required for cytotoxic granule docking at the immunologic synapse. Isoform 4 binds phosphatidylserine (PS) and phosphatidylinositol-4,5-bisphosphate (PIP2) and promotes the recruitment of glucagon-containing granules to the cell membrane in pancreatic alpha cells. Binding to PS is inhibited by Ca(2+) while binding to PIP2 is Ca(2+) insensitive.

**Summary**, from NCBI Gene [54843](https://www.ncbi.nlm.nih.gov/gene/54843):

> The protein encoded by this gene is a synaptotagmin-like protein (SLP) that belongs to a C2 domain-containing protein family. The SLP homology domain (SHD) of this protein has been shown to specifically bind the GTP-bound form of Ras-related protein Rab-27A (RAB27A). This protein plays a role in RAB27A-dependent vesicle trafficking and controls melanosome distribution in the cell periphery. Alternative splicing results in multiple transcript variants encoding distinct isoforms.[provided by …

**Accessions** — [HGNC:15585](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15585) · Entrez [54843](https://www.ncbi.nlm.nih.gov/gene/54843) · UniProt [Q9HCH5](https://www.uniprot.org/uniprotkb/Q9HCH5) · Ensembl [ENSG00000137501](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137501)

## Data

Gene col 6026: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6026); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6026, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6026]; `tensor/DDL_lfc|DDL_z.npy` [6026]; `embed/gene_vectors.npy` [6026]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6026 or target_col == 6026). Every well: [[SYTL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYTL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
