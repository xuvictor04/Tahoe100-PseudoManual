---
symbol: "SKI"
type: "gene"
col: 8117
ensembl_id: "ENSG00000157933"
name: "SKI proto-oncogene"
location: "1p36.33-p36.32"
module: 195
arm: "+"
pooled_cpm: 88.79
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/195"]
generated_by: "tahoemap"
---

# SKI

*SKI proto-oncogene* — 1p36.33-p36.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.10× (z +12.0, q 2e-30, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.628× (z -7.5, q 3e-11, down in 36 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.784× (z -3.9, q 0.012, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBRSL1]] (+0.67, fdr 7e-06), [[POLG]] (+0.64, fdr 9e-06), [[NIBAN2]] (+0.61, fdr 2e-05); moves opposite to [[BBOX1-AS1]] (-0.57, fdr 2e-05), [[ATP6V1A]] (-0.57, fdr 3e-05), [[SMG7]] (-0.55, fdr 2e-05).
> It is in [[Module 195]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8117.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.10×** | +12.0 | 2e-30 | 45/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +9.3 | 3e-18 | 42/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.73×** | +8.9 | 1e-16 | 40/48 (H4, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +8.3 | 2e-14 | 30/48 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.69×** | +4.4 | 0.001 | 30/48 (LOX-IMVI, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.007 | 28/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.50×** | +3.4 | 0.046 | 21/49 (J82, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.046 | 23/48 (LoVo, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.046 | 22/48 (Hs 766T, NCI-H1573, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.23×** | +3.2 | 0.086 | 21/48 (NCI-H1573, C32, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.43× | +3.0 | 0.13 | 20/48 (PANC-1, SHP-77, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8117.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.628×** | -7.5 | 3e-11 | 36/49 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.628×** | -6.9 | 1e-09 | 30/45 (SW48, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.653×** | -6.6 | 7e-09 | 26/44 (C-33 A, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.784×** | -3.9 | 0.012 | 29/48 (HepG2/C3A, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.790×** | -3.7 | 0.029 | 26/47 (HEC-1-A, CHP-212, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.792×** | -3.6 | 0.029 | 25/48 (SW 1088, SW 900, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -3.3 | 0.078 | 16/48 (CFPAC-1, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.872× | -3.1 | 0.13 | 18/48 (HOP62, PANC-1, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.851× | -3.0 | 0.16 | 18/48 (AsPC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8117. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 113 | 10 | 0 | [[Clobetasol propionate (drug)]] 5 µM 3.18× (z +11.6) | — |
| [[LoVo (line)]] | wt | 77.8 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.387× (z -11.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 95.6 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.381× (z -15.1) |
| [[NCI-H1573 (line)]] | alt | 69.9 | 3 | 1 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 3.48× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.146× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 59.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.314× (z -10.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 84.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -13.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 78.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.80× (z +11.8) | — |
| [[A-172 (line)]] | wt | 55.4 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -11.6) |
| [[A549 (line)]] | wt | 64.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0773× (z -21.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 78.9 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.1) | — |
| [[H4 (line)]] | wt | 108 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.72× (z +10.7) | — |
| [[KATO III (line)]] | alt | 75.4 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.87× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -9.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 146 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0894× (z -22.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 124 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -10.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 94.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -11.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 70.4 | 2 (2 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 128 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.95× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 75.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 87.4 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.398× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 86.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -11.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 117 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.435× (z -9.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 90.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.5) | — |
| [[SW 1088 (line)]] | alt | 126 | 0 | 2 (1 ⚠) | — | [[Ivermectin (drug)]] 0.5 µM 0.106× (z -8.7) |
| [[SW48 (line)]] | wt | 117 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.86× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.0696× (z -22.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 47.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.372× (z -9.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 93.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.9) | — |
| [[COLO 205 (line)]] | alt | 123 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 138 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 187 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.380× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[HS-578T (line)]] | alt | 109 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.91× (z +11.3) | — |
| [[HT-29 (line)]] | alt | 105 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.31× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 114 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.1) | — |
| [[J82 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.441× (z -8.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0643× (z -15.4) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 116 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 64.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8117), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBRSL1]] | +0.67 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[POLG]] | +0.64 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[NIBAN2]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[MAPKAPK2]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ARRDC1]] | +0.60 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[SLC16A3]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ACOT7]] | +0.58 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[TBC1D16]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ERRFI1]] | +0.57 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[VAV2]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[SLCO4A1]] | +0.56 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[OSBPL5]] | +0.56 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBOX1-AS1]] | -0.57 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ATP6V1A]] | -0.57 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[SMG7]] | -0.55 | -0.51 / -0.49 | both halves | 2e-05 |  |
| [[FAM111A-DT]] | -0.55 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[ZBED5-AS1]] | -0.53 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[GNGT1]] | -0.52 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[OSGIN2]] | -0.52 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[FAM204A]] | -0.52 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[RAB21]] | -0.52 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[HSF2]] | -0.51 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[DENND2B]] | -0.51 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[MBIP]] | -0.51 | -0.44 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 195]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.588). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.7, -16.2); signed map (-20.7, 42.0). **Vector** length 124, 38.1% of its response variance represented; |z| ≥ 3 in 1,225 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.4 | +12.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +8.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.1 | +3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.0 | +4.4 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | +3.6 | +3.2 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.3 | +2.7 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.3 | +0.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.1 | +1.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.1 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.6 | -3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.0 | -3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -5.3 | -2.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.8 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.5 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.5 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | SKI proto-oncogene |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33-p36.32 — chr1:2,227,388-2,310,213 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SKI transcriptional corepressors |
| Hallmark sets | TGF_BETA_SIGNALING |
| Reactome | 5 pathways, smallest: Signaling by BMP; Downregulation of SMAD2/3:SMAD4 transcriptional activity; Transcriptional activity of SMAD2/SMAD3:SMAD4 heterotrimer |
| Matched by | ensembl_id |

**Function**, from UniProt [P12755](https://www.uniprot.org/uniprotkb/P12755) (Ski oncogene):

> May play a role in terminal differentiation of skeletal muscle cells but not in the determination of cells to the myogenic lineage. Functions as a repressor of TGF-beta signaling.

**Summary**, from NCBI Gene [6497](https://www.ncbi.nlm.nih.gov/gene/6497):

> This gene encodes the nuclear protooncogene protein homolog of avian sarcoma viral (v-ski) oncogene. It functions as a repressor of TGF-beta signaling, and may play a role in neural tube development and muscle differentiation. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:10896](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10896) · Entrez [6497](https://www.ncbi.nlm.nih.gov/gene/6497) · UniProt [P12755](https://www.uniprot.org/uniprotkb/P12755) · Ensembl [ENSG00000157933](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157933)

## Data

Gene col 8117: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8117); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8117, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8117]; `tensor/DDL_lfc|DDL_z.npy` [8117]; `embed/gene_vectors.npy` [8117]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8117 or target_col == 8117). Every well: [[SKI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SKI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
