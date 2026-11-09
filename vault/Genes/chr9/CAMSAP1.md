---
symbol: "CAMSAP1"
type: "gene"
col: 5083
ensembl_id: "ENSG00000130559"
name: "calmodulin regulated spectrin associated protein 1"
location: "9q34.3"
module: 2
arm: "+"
pooled_cpm: 59.45
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CAMSAP1

*calmodulin regulated spectrin associated protein 1* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.83× (z +10.9, q 6e-25, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.722× (z -5.9, q 2e-06, down in 30 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.818× (z -5.2, q 4e-05, down in 24 of 49 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNK2]] (+0.73, fdr 1e-05), [[ANKRD27]] (+0.68, fdr 1e-04), [[ATP13A2]] (+0.67, fdr 1e-05); moves opposite to [[BAZ2B]] (-0.63, fdr 3e-04), [[ZNF518A]] (-0.62, fdr 4e-05), [[LINC01004]] (-0.62, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5083.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +10.9 | 6e-25 | 43/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.82×** | +10.8 | 6e-25 | 44/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.95×** | +10.2 | 3e-22 | 41/48 (RKO, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +8.8 | 2e-16 | 41/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +6.3 | 4e-08 | 32/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.67×** | +4.9 | 1e-04 | 30/49 (RKO, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.60×** | +4.4 | 8e-04 | 23/49 (SHP-77, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +4.3 | 0.001 | 22/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +4.2 | 0.002 | 19/49 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.26×** | +4.2 | 0.002 | 25/48 (H4, LS 180, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.003 | 25/48 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.26×** | +4.0 | 0.004 | 22/48 (H4, PANC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.019 | 20/48 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.025 | 14/49 (NCI-H1573, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.025 | 20/48 (LS 180, PANC-1, …) | rises with dose | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.041 | 17/47 (C-33 A, BT-474, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.1 | 0.059 | 10/48 (PANC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.18× | +3.0 | 0.069 | 7/47 (HT-29, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5083.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.722×** | -5.9 | 2e-06 | 30/49 (A-172, RKO, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.800×** | -5.8 | 2e-06 | 25/48 (SK-MEL-2, A-172, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.818×** | -5.2 | 4e-05 | 24/49 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.762×** | -4.9 | 1e-04 | 25/48 (SW480, HOP62, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.872× | -3.5 | 0.045 | 13/48 (SW48, Panc 03.27, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.875× | -3.5 | 0.052 | 23/48 (MIA PaCa-2, RKO, …) | rises with dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.774×** | -3.3 | 0.070 | 14/48 (SW 1271, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.883× | -3.2 | 0.094 | 6/49 (LOX-IMVI, SHP-77, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5083. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 68.1 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 2.34× (z +12.0) | [[Auranofin (drug)]] 5 µM 0.481× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 58.9 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.92× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -9.3) |
| [[RKO (line)]] | wt | 120 | 2 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 9.23× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -8.5) |
| [[A-172 (line)]] | wt | 90.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -9.3) |
| [[KATO III (line)]] | alt | 58.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.05× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.307× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 92.7 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.260× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -11.1) |
| [[AN3 CA (line)]] | alt | 85.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 39.0 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 11.8× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -8.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HOP62 (line)]] | alt | 61.5 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.18× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -14.0) |
| [[NCI-H1573 (line)]] | alt | 26.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.21× (z +8.9) | — |
| [[A-427 (line)]] | wt | 44.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 76.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 77.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.94× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -9.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[Hs 766T (line)]] | wt | 65.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -9.1) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HS-578T (line)]] | alt | 44.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -8.6) |
| [[HT-29 (line)]] | alt | 56.1 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.99× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 42.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.2) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[SHP-77 (line)]] | alt | 75.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.33× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 60.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -15.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SW48 (line)]] | wt | 115 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -8.8) |
| [[A498 (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 67.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 65.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5083), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNK2]] | +0.73 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.68 | +0.73 / +0.35 | both halves | 1e-04 |  |
| [[ATP13A2]] | +0.67 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[LRFN3]] | +0.67 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[ZDHHC8]] | +0.67 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ST6GALNAC6]] | +0.66 | +0.68 / +0.35 | both halves | 1e-04 |  |
| [[STX7]] | +0.66 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[IL17RD]] | +0.64 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[STX2]] | +0.63 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[USP35]] | +0.63 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[BICD2]] | +0.63 | +0.66 / +0.37 | both halves | 8e-05 |  |
| [[INTS11]] | +0.63 | +0.64 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2B]] | -0.63 | -0.66 / -0.27 | both halves | 3e-04 |  |
| [[ZNF518A]] | -0.62 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[LINC01004]] | -0.62 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[ERCC6L2]] | -0.62 | -0.65 / -0.29 | both halves | 2e-04 |  |
| [[ZBED5]] | -0.61 | -0.64 / -0.27 | both halves | 3e-04 |  |
| [[TIA1]] | -0.59 | -0.71 / -0.24 | both halves | 5e-04 |  |
| [[TTC32]] | -0.59 | -0.65 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[ZNF764]] | -0.58 | -0.61 / -0.25 | both halves | 4e-04 |  |
| [[DCAF8]] | -0.58 | -0.69 / -0.24 | both halves | 5e-04 |  |
| [[ZNF24]] | -0.58 | -0.55 / -0.29 | both halves | 3e-04 |  |
| [[MAPK1IP1L]] | -0.57 | -0.58 / -0.36 | both halves | 9e-05 |  |
| [[MR1]] | -0.57 | -0.58 / -0.25 | both halves | 4e-04 |  |
| [[CENPL]] | -0.56 | -0.54 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (0.2, -0.1); signed map (-42.6, -7.7). **Vector** length 113, 30.6% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.5 | +8.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.1 | +10.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.6 | +10.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.8 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.6 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.4 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +10.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -7.7 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.3 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -6.2 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.5 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -1.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | calmodulin regulated spectrin associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:135,808,487-135,907,546 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31228, DKFZp434F195 |
| Gene groups (HGNC) | CAMSAP family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T5Y3](https://www.uniprot.org/uniprotkb/Q5T5Y3) (Calmodulin-regulated spectrin-associated protein 1):

> Key microtubule-organizing protein that specifically binds the minus-end of non-centrosomal microtubules and regulates their dynamics and organization. Specifically recognizes growing microtubule minus-ends and stabilizes microtubules. Acts on free microtubule minus-ends that are not capped by microtubule-nucleating proteins or other factors and protects microtubule minus-ends from depolymerization. In contrast to CAMSAP2 and CAMSAP3, tracks along the growing tips of minus-end microtubules …

**Summary**, from NCBI Gene [157922](https://www.ncbi.nlm.nih.gov/gene/157922):

> Enables microtubule minus-end binding activity and spectrin binding activity. Involved in microtubule cytoskeleton organization; neuron projection development; and regulation of microtubule polymerization. Located in cytosol; microtubule minus-end; and mitotic spindle. Implicated in complex cortical dysplasia with other brain malformations 12. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19946](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19946) · Entrez [157922](https://www.ncbi.nlm.nih.gov/gene/157922) · UniProt [Q5T5Y3](https://www.uniprot.org/uniprotkb/Q5T5Y3) · Ensembl [ENSG00000130559](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130559)

## Data

Gene col 5083: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5083); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5083, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5083]; `tensor/DDL_lfc|DDL_z.npy` [5083]; `embed/gene_vectors.npy` [5083]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5083 or target_col == 5083). Every well: [[CAMSAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAMSAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
