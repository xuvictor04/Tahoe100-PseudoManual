---
symbol: "MAFG"
type: "gene"
col: 12335
ensembl_id: "ENSG00000197063"
name: "MAF bZIP transcription factor G"
location: "17q25.3"
module: 50
arm: "+"
pooled_cpm: 55.21
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# MAFG

*MAF bZIP transcription factor G* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.43× (z +17.5, q 0e+00, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRAGC-DT]] (+0.66, fdr 7e-06), [[N4BP2L2]] (+0.64, fdr 1e-05), [[ZBTB8OS]] (+0.63, fdr 1e-05); moves opposite to [[ATP5F1B]] (-0.67, fdr 7e-06), [[ECHS1]] (-0.66, fdr 3e-05), [[SKP2]] (-0.63, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12335.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.43×** | +17.5 | 0e+00 | 46/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.34×** | +14.7 | 0e+00 | 47/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.06×** | +14.0 | 2e-42 | 48/48 (LoVo, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.57×** | +12.8 | 4e-35 | 47/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.86×** | +10.5 | 8e-24 | 47/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.67×** | +9.5 | 3e-19 | 45/47 (KATO III, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.48×** | +9.1 | 8e-18 | 45/47 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.40×** | +8.8 | 1e-16 | 41/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.33×** | +8.5 | 1e-15 | 46/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.28×** | +8.3 | 8e-15 | 47/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +8.0 | 4e-14 | 44/48 (A549, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.15×** | +7.3 | 1e-11 | 41/48 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.15×** | +7.2 | 2e-11 | 45/48 (HEC-1-A, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.10×** | +7.2 | 3e-11 | 43/47 (COLO 205, HOP62, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.02×** | +6.5 | 4e-09 | 38/47 (LoVo, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.79×** | +4.2 | 1e-03 | 36/49 (HOP62, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.51×** | +4.1 | 0.001 | 31/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.003 | 30/47 (NCI-H23, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.004 | 31/49 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12335.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 5 µM |  | 0.698× | -3.6 | 0.17 | 33/48 (A498, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12335. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 59.2 | 13 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.98× (z +20.9) | — |
| [[KATO III (line)]] | alt | 63.0 | 12 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +20.1) | — |
| [[COLO 205 (line)]] | alt | 68.3 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.10× (z +13.2) | — |
| [[HOP62 (line)]] | alt | 33.8 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +17.5) | — |
| [[SW480 (line)]] | alt | 57.0 | 8 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.75× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.77× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 62.9 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +16.3) | — |
| [[LS 180 (line)]] | wt | 50.0 | 7 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.58× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.21× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 78.0 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +17.9) | — |
| [[SW 900 (line)]] | alt | 72.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +17.1) | — |
| [[HepG2_C3A (line)]] | wt | 68.0 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +16.6) | — |
| [[HS-578T (line)]] | alt | 45.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.85× (z +19.3) | — |
| [[NCI-H2347 (line)]] | alt | 39.9 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +17.7) | — |
| [[PANC-1 (line)]] | alt | 65.4 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.67× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.19× (z +12.2) | — |
| [[SNU-423 (line)]] | alt | 67.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +19.1) | — |
| [[A-427 (line)]] | wt | 51.9 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.29× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 4.12× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 31.9 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +14.1) | — |
| [[CFPAC-1 (line)]] | alt | 24.6 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.82× (z +17.1) | — |
| [[HEC-1-A (line)]] | alt | 38.1 | 5 | 0 | [[Auranofin (drug)]] 5 µM 5.66× (z +13.5) | — |
| [[RKO (line)]] | wt | 47.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +11.6) | — |
| [[A-172 (line)]] | wt | 74.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +17.6) | — |
| [[C32 (line)]] | wt | 32.7 | 4 | 0 | [[Auranofin (drug)]] 5 µM 10.5× (z +14.0) | — |
| [[HT-29 (line)]] | alt | 86.0 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.38× (z +12.7) | — |
| [[LoVo (line)]] | wt | 44.7 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.84× (z +15.4) | — |
| [[NCI-H23 (line)]] | alt | 44.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +13.5) | — |
| [[Panc 03.27 (line)]] | alt | 42.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +10.9) | — |
| [[A498 (line)]] | wt | 105 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +17.3) | — |
| [[A549 (line)]] | wt | 40.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +13.9) | — |
| [[Hs 766T (line)]] | wt | 57.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +12.5) | — |
| [[J82 (line)]] | alt | 66.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +15.1) | — |
| [[LOX-IMVI (line)]] | wt | 56.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 65.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 42.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +10.3) | — |
| [[SW1417 (line)]] | alt | 64.2 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.52× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 37.9 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.81× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 5.44× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 59.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 49.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +11.7) | — |
| [[C-33 A (line)]] | alt | 25.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.47× (z +9.7) | — |
| [[H4 (line)]] | wt | 26.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.39× (z +12.8) | — |
| [[HCT15 (line)]] | alt | 41.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.68× (z +11.8) | — |
| [[SHP-77 (line)]] | alt | 42.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.17× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 58.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +12.2) | — |
| [[AN3 CA (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 78.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12335), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAGC-DT]] | +0.66 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[N4BP2L2]] | +0.64 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[ZBTB8OS]] | +0.63 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[MRPL45P2]] | +0.63 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[MAPK6]] | +0.62 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[RAB4B]] | +0.62 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[CREM]] | +0.61 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[PABPN1]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[YBEY]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[RUFY3]] | +0.60 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[NRSN2-AS1]] | +0.60 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[EIF3J-DT]] | +0.60 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5F1B]] | -0.67 | -0.70 / -0.59 | both halves | 7e-06 |  |
| [[ECHS1]] | -0.66 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[SKP2]] | -0.63 | -0.62 / -0.52 | both halves | 1e-05 | pathway: Cellular response to chemical stress |
| [[TTLL12]] | -0.63 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[PGM2]] | -0.62 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[SDHAF3]] | -0.61 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[BCKDK]] | -0.61 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[ATP5F1A]] | -0.60 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[ELP1]] | -0.60 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[TMEM106C]] | -0.60 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[FIGNL1]] | -0.60 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[POT1]] | -0.59 | -0.59 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction -0.398). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.9, 12.3); signed map (0.4, -5.0). **Vector** length 102, 38.1% of its response variance represented; |z| ≥ 3 in 1,136 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.9 | +14.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.4 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.0 | +9.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.8 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +8.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.6 | +1.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.5 | +1.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | +3.3 | +2.7 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | -2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.2 | -1.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | +0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.0 | -0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | +0.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.4 | -1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -0.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | MAF bZIP transcription factor G |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,918,270-81,927,735 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13090, MGC20149 |
| Gene groups (HGNC) | Small MAF bZIP transcription factor family |
| Reactome | 8 pathways, smallest: NFE2L2 regulates pentose phosphate pathway genes; Nuclear events mediated by NFE2L2; KEAP1-NFE2L2 pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [O15525](https://www.uniprot.org/uniprotkb/O15525) (Transcription factor MafG):

> Since they lack a putative transactivation domain, the small Mafs behave as transcriptional repressors when they dimerize among themselves. However, they seem to serve as transcriptional activators by dimerizing with other (usually larger) basic-zipper proteins, such as NFE2, NFE2L1 and NFE2L2, and recruiting them to specific DNA-binding sites. Small Maf proteins heterodimerize with Fos and may act as competitive repressors of the NFE2L2 transcription factor. Transcription factor, component of …

**Summary**, from NCBI Gene [4097](https://www.ncbi.nlm.nih.gov/gene/4097):

> Globin gene expression is regulated through nuclear factor erythroid-2 (NFE2) elements located in enhancer-like locus control regions positioned many kb upstream of alpha- and beta-gene clusters (summarized by Blank et al., 1997 [PubMed 9166829]). NFE2 DNA-binding activity consists of a heterodimer containing a ubiquitous small Maf protein (MafF, MIM 604877; MafG; or MafK, MIM 600197) and the tissue-restricted protein p45 NFE2 (MIM 601490). Both subunits are members of the activator …

**Accessions** — [HGNC:6781](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6781) · Entrez [4097](https://www.ncbi.nlm.nih.gov/gene/4097) · UniProt [O15525](https://www.uniprot.org/uniprotkb/O15525) · Ensembl [ENSG00000197063](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197063)

## Data

Gene col 12335: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12335); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12335, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12335]; `tensor/DDL_lfc|DDL_z.npy` [12335]; `embed/gene_vectors.npy` [12335]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12335 or target_col == 12335). Every well: [[MAFG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAFG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
