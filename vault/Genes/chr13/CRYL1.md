---
symbol: "CRYL1"
type: "gene"
col: 9125
ensembl_id: "ENSG00000165475"
name: "crystallin lambda 1"
location: "13q12.11"
module: 110
arm: "+"
pooled_cpm: 16.73
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 30
n_dd_up_clean: 0
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# CRYL1

*crystallin lambda 1* — 13q12.11

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.281× (z -29.5, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBPF9]] (+0.60, fdr 1e-05), [[FXYD5]] (+0.57, fdr 2e-05), [[NBPF15]] (+0.57, fdr 1e-05); moves opposite to [[DIO2]] (-0.57, fdr 2e-05), [[MYOF]] (-0.55, fdr 1e-05), [[RBM23]] (-0.51, fdr 2e-05).
> It is in [[Module 110]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9125.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.22× | +3.2 | 0.43 | 11/46 (A498, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.2 | 0.43 | 6/48 (A498, NCI-H23, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.21× | +3.0 | 0.49 | 14/46 (A549, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9125.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.281×** | -29.5 | 0e+00 | 45/47 (NCI-H1573, J82, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.358×** | -16.9 | 0e+00 | 37/44 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.322×** | -16.5 | 0e+00 | 41/47 (A-172, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.402×** | -15.0 | 0e+00 | 43/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.467×** | -12.5 | 6e-34 | 37/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.266×** | -11.4 | 5e-28 | 40/47 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.502×** | -10.0 | 1e-21 | 30/42 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.347×** | -9.1 | 7e-18 | 34/44 (RKO, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.588×** | -8.5 | 1e-15 | 28/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.634×** | -7.5 | 4e-12 | 28/47 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.691×** | -5.9 | 2e-07 | 26/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.783×** | -5.7 | 6e-07 | 19/48 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.717×** | -5.5 | 2e-06 | 21/47 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.737×** | -5.0 | 2e-05 | 26/47 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.739×** | -5.0 | 3e-05 | 23/47 (LoVo, SW48, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.758×** | -4.4 | 3e-04 | 17/47 (SW48, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.770×** | -4.1 | 0.001 | 19/47 (C32, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.719×** | -3.9 | 0.003 | 6/48 (PANC-1, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.804×** | -3.6 | 0.009 | 8/47 (AN3 CA, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9125. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.2 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -20.2) |
| [[C32 (line)]] | wt | 38.9 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0972× (z -18.3) |
| [[PANC-1 (line)]] | alt | 13.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -16.2) |
| [[A-172 (line)]] | wt | 18.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -15.8) |
| [[SW480 (line)]] | alt | 15.8 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.166× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.197× (z -12.3) |
| [[LoVo (line)]] | wt | 21.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 15.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0897× (z -19.9) |
| [[RKO (line)]] | wt | 34.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0927× (z -16.3) |
| [[A549 (line)]] | wt | 13.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -17.6) |
| [[J82 (line)]] | alt | 19.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -20.2) |
| [[LS 180 (line)]] | wt | 31.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 23.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.100× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 14.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0912× (z -20.3) |
| [[Panc 03.27 (line)]] | alt | 21.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 21.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -16.6) |
| [[HT-29 (line)]] | alt | 19.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -19.3) |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -11.2) |
| [[SNU-1 (line)]] | wt | 25.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -13.9) |
| [[SNU-423 (line)]] | alt | 17.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -14.3) |
| [[SW1417 (line)]] | alt | 11.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -13.1) |
| [[A-427 (line)]] | wt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -10.7) |
| [[A498 (line)]] | wt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -10.2) |
| [[AN3 CA (line)]] | alt | 29.4 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0858× (z -8.8) |
| [[COLO 205 (line)]] | alt | 69.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.294× (z -9.0) |
| [[H4 (line)]] | wt | 9.09 | 0 | 1 | — | [[Belumosudil (mesylate) (drug)]] 0.05 µM 0.0452× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.172× (z -9.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HOP62 (line)]] | alt | 10.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -15.0) |
| [[Hs 766T (line)]] | wt | 18.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -13.3) |
| [[HS-578T (line)]] | alt | 8.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -9.2) |
| [[KATO III (line)]] | alt | 24.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -12.3) |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.124× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 8.72 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 9.60 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0681× (z -9.8) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SK-MEL-2 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9125), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF9]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[FXYD5]] | +0.57 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[NBPF15]] | +0.57 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[NBPF20]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[LYPLA1]] | +0.56 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[SMAGP]] | +0.56 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[ATP13A2]] | +0.55 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[RASA2]] | +0.55 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[RUSC2]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[APPL2]] | +0.55 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[PPM1F]] | +0.54 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[MOB1B]] | +0.54 | +0.60 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIO2]] | -0.57 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[MYOF]] | -0.55 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[RBM23]] | -0.51 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[SPART-AS1]] | -0.51 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[CDKN1B]] | -0.50 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[BCL9L]] | -0.49 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[HNRNPH2]] | -0.49 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[CFH]] | -0.49 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[THRAP3]] | -0.48 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[KMO]] | -0.48 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[LGALS3]] | -0.48 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[TRIM69]] | -0.48 | -0.54 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.598). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.3, -25.0); signed map (-17.8, 47.2). **Vector** length 68.2, 12.7% of its response variance represented; |z| ≥ 3 in 1,081 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.7 | -1.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.6 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | -1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.3 | -0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.7 | -0.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.5 | -1.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.7 | -16.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -29.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -16.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -9.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | crystallin lambda 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.11 — chr13:20,403,666-20,525,873 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GDH, lambda-CRY, MGC149525, MGC149526 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Oxidoreductases |
| Reactome | 2 pathways, smallest: Formation of xylulose-5-phosphate; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2S2](https://www.uniprot.org/uniprotkb/Q9Y2S2) (Lambda-crystallin homolog):

> Catalyzes the conversion of L-gulonate to 3-dehydro-L-gulonate. It also exhibits low dehydrogenase activity toward L-3-hydroxybutyrate (HBA) and L-threonate. Utilizes NAD as the sole cosubstrate and shows no activity with NADP.

**Summary**, from NCBI Gene [51084](https://www.ncbi.nlm.nih.gov/gene/51084):

> The uronate cycle functions as an alternative glucose metabolic pathway, accounting for about 5% of daily glucose catabolism. The product of this gene catalyzes the dehydrogenation of L-gulonate into dehydro-L-gulonate in the uronate cycle. The enzyme requires NAD(H) as a coenzyme, and is inhibited by inorganic phosphate. A similar gene in the rabbit is thought to serve a structural role in the lens of the eye. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18246](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18246) · Entrez [51084](https://www.ncbi.nlm.nih.gov/gene/51084) · UniProt [Q9Y2S2](https://www.uniprot.org/uniprotkb/Q9Y2S2) · Ensembl [ENSG00000165475](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165475)

## Data

Gene col 9125: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9125); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9125, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9125]; `tensor/DDL_lfc|DDL_z.npy` [9125]; `embed/gene_vectors.npy` [9125]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9125 or target_col == 9125). Every well: [[CRYL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRYL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
