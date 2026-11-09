---
symbol: "FERMT3"
type: "gene"
col: 7407
ensembl_id: "ENSG00000149781"
name: "FERM domain containing kindlin 3"
location: "11q13.1"
module: 47
arm: "+"
pooled_cpm: 5.82
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 13
n_dd_up_clean: 16
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# FERMT3

*FERM domain containing kindlin 3* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 4.30× (z +14.8, q 0e+00, up in 38 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.639× (z -4.5, q 0.003, down in 20 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSANTD1]] (+0.74, fdr 7e-06), [[NTRK1]] (+0.70, fdr 7e-06), [[SMIM41]] (+0.70, fdr 7e-06); moves opposite to [[XPA]] (-0.63, fdr 1e-05), [[TAPT1]] (-0.63, fdr 1e-05), [[RCOR3]] (-0.59, fdr 2e-05).
> It is in [[Module 047]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7407.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **4.30×** | +14.8 | 0e+00 | 38/42 (A-172, SW480, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.76×** | +13.4 | 2e-38 | 39/44 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.16×** | +11.0 | 6e-26 | 33/40 (KATO III, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.15×** | +11.0 | 7e-26 | 22/35 (SNU-423, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.86×** | +10.6 | 2e-24 | 34/44 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.72×** | +10.1 | 3e-22 | 32/43 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.44×** | +9.0 | 1e-17 | 28/44 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.40×** | +8.8 | 6e-17 | 29/42 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.33×** | +6.1 | 6e-08 | 21/43 (MIA PaCa-2, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +5.8 | 5e-07 | 14/44 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.78×** | +5.4 | 4e-06 | 6/14 (LOX-IMVI, NCI-H460, …) | all doses, flat | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.68×** | +5.3 | 7e-06 | 16/44 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.63×** | +5.1 | 1e-05 | 6/15 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.40×** | +4.8 | 5e-05 | 14/37 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +4.4 | 3e-04 | 14/36 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.56×** | +4.3 | 7e-04 | 10/42 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Rimonabant (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.020 | 7/43 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.023 | 4/42 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.82×** | +3.2 | 0.041 | 1/31 (PANC-1) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7407.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.639×** | -4.5 | 0.003 | 20/42 (CFPAC-1, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.659×** | -4.2 | 0.007 | 19/45 (NCI-H2030, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.670×** | -4.0 | 0.010 | 20/43 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.676×** | -4.0 | 0.011 | 16/43 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.682×** | -3.9 | 0.013 | 13/42 (A-427, NCI-H2030, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.665×** | -3.7 | 0.018 | 18/43 (SW1417, SW 900, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.678×** | -3.6 | 0.031 | 11/40 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.690×** | -3.5 | 0.037 | 5/44 (HepG2/C3A, RKO, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.714×** | -3.4 | 0.041 | 21/34 (NCI-H2030, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.715×** | -3.4 | 0.041 | 8/44 (HOP62, LOX-IMVI, …) | top dose only | position effect removed |
| [[Anethole trithione (drug)]] 5 µM |  | **0.804×** | -3.1 | 0.093 | 7/44 (CHP-212, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vandetanib (drug)]] 5 µM |  | **0.737×** | -3.1 | 0.093 | 10/43 (KATO III, SW48, …) | top dose only | position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.714×** | -3.1 | 0.093 | 7/44 (SNU-423, SW1417, …) | top dose only | plate-row cell shift; position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | 0.743× | -3.0 | 0.11 | 10/45 (SK-MEL-2, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7407. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 41.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 41.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.80× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 6.89 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0479× (z -12.0) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0774× (z -10.1) |
| [[A-172 (line)]] | wt | 10.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.65× (z +8.5) | — |
| [[J82 (line)]] | alt | 6.30 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -8.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0980× (z -8.6) |
| [[A-427 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7407), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSANTD1]] | +0.74 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[NTRK1]] | +0.70 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[TUBA8]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[CHADL]] | +0.68 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[MPP4]] | +0.68 | +0.61 / +0.77 | both halves | 7e-06 |  |
| [[PIP5KL1]] | +0.68 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[BMP8A]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[SFXN5]] | +0.67 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.67 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[SPTBN5]] | +0.67 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[CSPG5]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPA]] | -0.63 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[TAPT1]] | -0.63 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[RCOR3]] | -0.59 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[FBXL5]] | -0.59 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.56 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[TMEM14C]] | -0.55 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[C6orf89]] | -0.54 | -0.57 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.743). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.2, -20.1); signed map (15.3, 15.0). **Vector** length 80.5, 14.2% of its response variance represented; |z| ≥ 3 in 1,307 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.9 | +14.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +5.1 | +3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.0 | +11.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.7 | +10.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.4 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +8.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.5 | +4.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +6.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.2 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.1 | -4.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.0 | -4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | FERM domain containing kindlin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,205,926-64,223,896 (+) |
| Ensembl biotype | protein_coding |
| Also known as | URP2, KIND3, MIG2B, MGC10966, UNC112C |
| Gene groups (HGNC) | Fermitins; Pleckstrin homology domain containing; FERM domain containing |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UX7](https://www.uniprot.org/uniprotkb/Q86UX7) (Fermitin family homolog 3):

> Plays a central role in cell adhesion in hematopoietic cells. Acts by activating the integrin beta-1-3 (ITGB1, ITGB2 and ITGB3) (By similarity). Required for integrin-mediated platelet adhesion and leukocyte adhesion to endothelial cells. Required for activation of integrin beta-2 (ITGB2) in polymorphonuclear granulocytes (PMNs) (By similarity).; Isoform 2 may act as a repressor of NF-kappa-B and apoptosis.

**Summary**, from NCBI Gene [83706](https://www.ncbi.nlm.nih.gov/gene/83706):

> Kindlins are a small family of proteins that mediate protein-protein interactions involved in integrin activation and thereby have a role in cell adhesion, migration, differentiation, and proliferation. The protein encoded by this gene has a key role in the regulation of hemostasis and thrombosis. This protein may also help maintain the membrane skeleton of erythrocytes. Mutations in this gene cause the autosomal recessive leukocyte adhesion deficiency syndrome-III (LAD-III). Alternative …

**Accessions** — [HGNC:23151](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23151) · Entrez [83706](https://www.ncbi.nlm.nih.gov/gene/83706) · UniProt [Q86UX7](https://www.uniprot.org/uniprotkb/Q86UX7) · Ensembl [ENSG00000149781](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149781)

## Data

Gene col 7407: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7407); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7407, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7407]; `tensor/DDL_lfc|DDL_z.npy` [7407]; `embed/gene_vectors.npy` [7407]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7407 or target_col == 7407). Every well: [[FERMT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FERMT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
