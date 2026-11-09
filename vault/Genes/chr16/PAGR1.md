---
symbol: "PAGR1"
type: "gene"
col: 15968
ensembl_id: "ENSG00000280789"
name: "PAXIP1 associated glutamate rich protein 1"
location: "16p11.2"
module: 91
arm: "+"
pooled_cpm: 14.78
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 26
n_dd_up_clean: 0
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# PAGR1

*PAXIP1 associated glutamate rich protein 1* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.19× (z +8.0, q 7e-13, up in 15 of 48 measured lines) ⚠ position not correctable. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.331× (z -14.9, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HIRIP3]] (+0.65, fdr 9e-06), [[DYNC2I2]] (+0.54, fdr 4e-05), [[CTCF]] (+0.53, fdr 2e-05); moves opposite to [[SWT1]] (-0.50, fdr 3e-04), [[TALAM1]] (-0.47, fdr 5e-05), [[MAP1LC3B]] (-0.46, fdr 5e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15968.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +8.0 | 7e-13 | 15/48 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +6.3 | 9e-08 | 24/39 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +5.3 | 3e-05 | 20/44 (SW1417, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +3.9 | 0.015 | 14/33 (A-172, LS 180, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.21×** | +3.7 | 0.025 | 12/48 (SW1417, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15968.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.331×** | -14.9 | 0e+00 | 44/48 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.433×** | -11.3 | 5e-27 | 37/47 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.444×** | -10.9 | 2e-25 | 33/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.650×** | -8.2 | 4e-14 | 31/47 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.557×** | -7.9 | 4e-13 | 32/46 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.560×** | -7.8 | 6e-13 | 30/47 (SW480, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.567×** | -7.6 | 2e-12 | 30/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.576×** | -7.4 | 8e-12 | 34/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.583×** | -7.2 | 3e-11 | 30/48 (C-33 A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.570×** | -7.1 | 6e-11 | 34/48 (SK-MEL-2, HCT15, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.590×** | -7.1 | 7e-11 | 38/47 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.638×** | -6.0 | 8e-08 | 28/47 (NCI-H23, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.648×** | -5.8 | 3e-07 | 28/47 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.449×** | -5.6 | 7e-07 | 21/37 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.728×** | -4.3 | 8e-04 | 21/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.732×** | -4.2 | 1e-03 | 19/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.748×** | -3.9 | 0.003 | 13/48 (NCI-H2030, SW1417, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15968. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 20.8 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -10.3) |
| [[SW480 (line)]] | alt | 14.6 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.220× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.188× (z -9.2) |
| [[SNU-1 (line)]] | wt | 14.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0430× (z -11.8) |
| [[A498 (line)]] | wt | 17.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -10.8) |
| [[PANC-1 (line)]] | alt | 18.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.268× (z -10.3) |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0748× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -9.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -10.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -8.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -9.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 12.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.166× (z -10.2) |
| [[KATO III (line)]] | alt | 24.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 9.36 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.153× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 6.02 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0927× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~22% of this change |
| [[NCI-H460 (line)]] | wt | 9.98 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.237× (z -8.6) |
| [[RKO (line)]] | wt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 14.6 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0581× (z -13.3) |
| [[A-172 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15968), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIRIP3]] | +0.65 | +0.61 / +0.57 | both halves | 9e-06 | STRING 704 |
| [[DYNC2I2]] | +0.54 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[CTCF]] | +0.53 | +0.46 / +0.59 | both halves | 2e-05 | pathway: Activation of HOX genes during differentiation; STRING 522 |
| [[CENPB]] | +0.53 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[SUV39H1]] | +0.53 | +0.61 / +0.41 | both halves | 4e-05 | pathway: Epigenetic regulation of gene expression |
| [[FBXO5]] | +0.52 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[HROB]] | +0.52 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[INTS5]] | +0.51 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[CAND1]] | +0.51 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[IRF2BP1]] | +0.51 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[FOXRED1]] | +0.50 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[MGAT2]] | +0.50 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SWT1]] | -0.50 | -0.62 / -0.29 | both halves | 3e-04 |  |
| [[TALAM1]] | -0.47 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[MAP1LC3B]] | -0.46 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[SNX3]] | -0.46 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[FTL]] | -0.44 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[MALAT1]] | -0.43 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[EIF1]] | -0.43 | -0.49 / -0.27 | both halves | 3e-04 |  |
| [[CLN8]] | -0.43 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[PSAP]] | -0.42 | -0.35 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.419). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-42.1, -44.1); signed map (-45.4, -50.2). **Vector** length 55.6, 8.56% of its response variance represented; |z| ≥ 3 in 843 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | -3.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +1.9 | -3.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.6 | +5.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.4 | +8.0 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +0.9 | +0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +0.9 | +0.3 |
|  | [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | +0.7 | -0.3 |
|  | [[crizotinib (drug)]] 5 µM |  | +0.7 | -1.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.6 | -7.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | -10.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.7 | -7.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -14.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.5 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -6.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | PAXIP1 associated glutamate rich protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:29,816,152-29,822,489 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4606, GAS, PA1; previously C16orf53 |
| Reactome | 12 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; Activation of HOX genes during differentiation; Activation of anterior HOX genes in hindbrain development during early embryogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTK6](https://www.uniprot.org/uniprotkb/Q9BTK6) (PAXIP1-associated glutamate-rich protein 1):

> Its association with the histone methyltransferase MLL2/MLL3 complex is suggesting a role in epigenetic transcriptional activation. However, in association with PAXIP1/PTIP is proposed to function at least in part independently of the MLL2/MLL3 complex. Proposed to be recruited by PAXIP1 to sites of DNA damage where the PAGR1:PAXIP1 complex is required for cell survival in response to DNA damage independently of the MLL2/MLL3 complex. However, its function in DNA damage has been questioned (By …

**Summary**, from NCBI Gene [79447](https://www.ncbi.nlm.nih.gov/gene/79447):

> Enables nuclear estrogen receptor binding activity. Involved in positive regulation of cell cycle G1/S phase transition; positive regulation of intracellular estrogen receptor signaling pathway; and positive regulation of transcription by RNA polymerase II. Located in nucleus. Part of MLL3/4 complex. Biomarker of esophagus squamous cell carcinoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28707](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28707) · Entrez [79447](https://www.ncbi.nlm.nih.gov/gene/79447) · UniProt [Q9BTK6](https://www.uniprot.org/uniprotkb/Q9BTK6) · Ensembl [ENSG00000280789](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000280789)

## Data

Gene col 15968: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15968); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15968, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15968]; `tensor/DDL_lfc|DDL_z.npy` [15968]; `embed/gene_vectors.npy` [15968]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15968 or target_col == 15968). Every well: [[PAGR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAGR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
