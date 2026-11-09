---
symbol: "C1orf52"
type: "gene"
col: 8552
ensembl_id: "ENSG00000162642"
name: "chromosome 1 open reading frame 52"
location: "1p22.3"
module: 142
arm: "+"
pooled_cpm: 56.39
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# C1orf52

*chromosome 1 open reading frame 52* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.80× (z +13.4, q 3e-38, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.609× (z -7.0, q 2e-09, down in 28 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 0.751× (z -4.2, q 0.004, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (HS-578T 0.245×, A498 0.402×, HepG2/C3A 0.250×, NCI-H2347 0.443×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.353×, NCI-H2347 0.446×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.442×; ⚠ cell-cycle shift, explains ~15% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBOX5]] (+0.73, fdr 7e-06), [[RARS2]] (+0.70, fdr 1e-05), [[RNF121]] (+0.69, fdr 7e-06); moves opposite to [[CUX1]] (-0.65, fdr 7e-06), [[ROCK2]] (-0.59, fdr 1e-05), [[ATF7IP]] (-0.59, fdr 3e-05).
> It is in [[Module 142]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8552.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.80×** | +13.4 | 3e-38 | 46/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.04×** | +10.6 | 5e-24 | 42/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.97×** | +9.9 | 8e-21 | 43/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +9.3 | 2e-18 | 35/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.89×** | +9.3 | 2e-18 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.89×** | +9.3 | 2e-18 | 42/48 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +8.4 | 5e-15 | 43/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.76×** | +8.3 | 1e-14 | 45/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +7.9 | 2e-13 | 36/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.78×** | +7.9 | 2e-13 | 39/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.64×** | +7.2 | 4e-11 | 39/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +7.0 | 9e-11 | 36/47 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.15×** | +5.8 | 2e-07 | 34/44 (PANC-1, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +5.7 | 6e-07 | 33/48 (NCI-H1573, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +5.6 | 8e-07 | 25/48 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +5.5 | 2e-06 | 28/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +4.9 | 4e-05 | 28/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.57×** | +4.7 | 8e-05 | 30/49 (PANC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8552.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (HS-578T 0.245×, A498 0.402×, HepG2/C3A 0.250×, NCI-H2347 0.443×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.353×, NCI-H2347 0.446×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.442×; ⚠ cell-cycle shift, explains ~15% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -7.0 | 2e-09 | 28/40 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.709×** | -5.0 | 1e-04 | 23/47 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -4.2 | 0.004 | 4/49 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.751×** | -4.2 | 0.004 | 25/48 (SW 900, A498, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.775×** | -3.7 | 0.021 | 19/48 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.808× | -3.1 | 0.17 | 19/49 (CHP-212, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.745× | -3.1 | 0.17 | 16/48 (A498, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8552. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 53.6 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +13.1) | — |
| [[PANC-1 (line)]] | alt | 98.0 | 7 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.0× (z +13.3) | — |
| [[LoVo (line)]] | wt | 45.7 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.07× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 53.0 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 8.84× (z +9.5) | — |
| [[RKO (line)]] | wt | 158 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.12× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -10.6) ⚠ cell-cycle shift, explains ~15% of this change |
| [[NCI-H23 (line)]] | alt | 62.9 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 31.9 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +10.4) | — |
| [[SK-MEL-2 (line)]] | alt | 57.6 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.70× (z +10.6) | — |
| [[HEC-1-A (line)]] | alt | 41.5 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 7.28× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 36.4 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.90× (z +10.9) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 3.36× (z +10.1) | — |
| [[KATO III (line)]] | alt | 37.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.3× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 54.2 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.4× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 73.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.446× (z -8.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 73.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.402× (z -8.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 35.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.48× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 28.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 17.5× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 30.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -8.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 85.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.85× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 74.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -10.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 51.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 66.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 33.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.51× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 68.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.14× (z +9.8) | — |
| [[A-172 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 53.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 73.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8552), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBOX5]] | +0.73 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[RARS2]] | +0.70 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[RNF121]] | +0.69 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[GPR107]] | +0.65 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.65 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[NDUFAF7]] | +0.65 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[CYB561D2]] | +0.64 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[STARD3]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[GDAP2]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[MED23]] | +0.63 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[USPL1]] | +0.63 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CUX1]] | -0.65 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[ROCK2]] | -0.59 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[ATF7IP]] | -0.59 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[FAM111A]] | -0.58 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[HNRNPK]] | -0.58 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.57 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[SKIL]] | -0.56 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[PSPC1]] | -0.56 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[AGL]] | -0.56 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[HIVEP2]] | -0.56 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[NFIB]] | -0.55 | -0.58 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.758). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.8, -16.8); signed map (-46.4, 6.1). **Vector** length 82.4, 22.3% of its response variance represented; |z| ≥ 3 in 1,131 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.1 | +9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +7.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.6 | +8.3 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.5 | +3.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.3 | +7.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +10.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +4.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +7.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.0 | -0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | +5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.1 | +9.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | +0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -0.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | -4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.6 | +0.8 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 1 open reading frame 52 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:85,249,953-85,259,672 (-) |
| Ensembl biotype | protein_coding |
| Also known as | gm117, FLJ44982 |
| Matched by | ensembl_id |

UniProt [Q8N6N3](https://www.uniprot.org/uniprotkb/Q8N6N3) carries no function annotation.

**Summary**, from NCBI Gene [148423](https://www.ncbi.nlm.nih.gov/gene/148423):

> Enables RNA binding activity. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24871](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24871) · Entrez [148423](https://www.ncbi.nlm.nih.gov/gene/148423) · UniProt [Q8N6N3](https://www.uniprot.org/uniprotkb/Q8N6N3) · Ensembl [ENSG00000162642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162642)

## Data

Gene col 8552: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8552); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8552, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8552]; `tensor/DDL_lfc|DDL_z.npy` [8552]; `embed/gene_vectors.npy` [8552]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8552 or target_col == 8552). Every well: [[C1orf52 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1orf52.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
