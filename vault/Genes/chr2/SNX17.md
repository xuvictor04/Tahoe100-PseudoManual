---
symbol: "SNX17"
type: "gene"
col: 3639
ensembl_id: "ENSG00000115234"
name: "sorting nexin 17"
location: "2p23.3"
module: 25
arm: "+"
pooled_cpm: 12.74
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SNX17

*sorting nexin 17* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.40× (z +16.3, q 0e+00, up in 33 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.45× (z +4.9, q 9e-05, up in 21 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.541× (z -8.2, q 1e-13, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX11]] (+0.71, fdr 7e-06), [[COPS6]] (+0.70, fdr 7e-06), [[GPS1]] (+0.67, fdr 7e-06); moves opposite to [[TMSB10]] (-0.57, fdr 1e-05), [[ZBTB7A]] (-0.56, fdr 2e-05), [[PTMAP2]] (-0.56, fdr 4e-05, ⚠ PTMAP2 in the vector space only through flagged drug-doses), [[RPL36]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3639.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.40×** | +16.3 | 0e+00 | 33/35 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.03×** | +14.1 | 1e-42 | 22/23 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.34×** | +13.5 | 2e-39 | 43/48 (A498, A-427, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +10.3 | 1e-22 | 25/30 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +5.8 | 9e-07 | 24/43 (A-427, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +4.9 | 9e-05 | 21/47 (NCI-H2030, HOP62, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +4.3 | 0.002 | 16/48 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +4.0 | 0.005 | 17/43 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.006 | 16/48 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.4 | 0.042 | 9/48 (A-172, NCI-H1792, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.086 | 11/47 (HEC-1-A, A-427, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.26× | +3.0 | 0.12 | 7/48 (RPMI-7951, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3639.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.541×** | -8.2 | 1e-13 | 30/47 (SNU-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.554×** | -7.9 | 1e-12 | 34/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.566×** | -7.6 | 6e-12 | 34/48 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.574×** | -7.4 | 2e-11 | 32/46 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.710×** | -6.5 | 1e-08 | 22/46 (LOX-IMVI, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.761×** | -3.7 | 0.024 | 13/47 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.767×** | -3.6 | 0.031 | 15/47 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.846× | -3.2 | 0.11 | 16/48 (HS-578T, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | 0.793× | -3.1 | 0.12 | 11/48 (J82, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3639. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 12.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +9.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.219× (z -9.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 14.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +12.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.328× (z -8.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 12.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.82× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 19.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +10.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 17.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.04× (z +10.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.23× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -10.2) |
| [[A-172 (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.190× (z -12.0) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 8.55 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0540× (z -10.3) |
| [[H4 (line)]] | wt | 9.03 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0776× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.36× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 6.69 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.14× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 17.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0771× (z -9.6) |
| [[SNU-423 (line)]] | alt | 9.92 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.80× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.126× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~40% of this change |
| [[A-427 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3639), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX11]] | +0.71 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[COPS6]] | +0.70 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[GPS1]] | +0.67 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[PNPO]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[TRUB1]] | +0.66 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[ZNF252P-1]] | +0.65 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[FASTK]] | +0.64 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[NCOA4]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ACTR8]] | +0.64 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ZNF252P]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[MRPL9]] | +0.62 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ATP5PB]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMSB10]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[ZBTB7A]] | -0.56 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[PTMAP2]] ⚠ | -0.56 | -0.63 / -0.42 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL37A]] ⚠ | -0.56 | -0.54 / -0.53 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36AL]] ⚠ | -0.56 | -0.65 / -0.44 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36]] | -0.55 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[RPL18]] ⚠ | -0.54 | -0.53 / -0.53 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS19]] | -0.54 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[RASA4B]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[ATP5F1E]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[CSKMT]] | -0.53 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[RPL35A]] | -0.53 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[RPLP2]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[HIC2]] | -0.52 | -0.44 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.8, -18.4); signed map (-18.6, -41.1). **Vector** length 69.7, 12.0% of its response variance represented; |z| ≥ 3 in 838 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.4 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +16.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +14.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +10.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +4.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.6 | +1.8 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.3 | -8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.8 | -3.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -1.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.9 | -2.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.6 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:27,370,496-27,377,535 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0064 |
| Gene groups (HGNC) | Sorting nexins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15036](https://www.uniprot.org/uniprotkb/Q15036) (Sorting nexin-17):

> Critical regulator of endosomal recycling of numerous surface proteins, including integrins, signaling receptor and channels. Binds to NPxY sequences in the cytoplasmic tails of target cargos. Associates with retriever and CCC complexes to prevent lysosomal degradation and promote cell surface recycling of numerous cargos such as integrins ITGB1, ITGB5 and their associated alpha subunits. Also required for maintenance of normal cell surface levels of APP and LRP1. Interacts with membranes …

**Summary**, from NCBI Gene [9784](https://www.ncbi.nlm.nih.gov/gene/9784):

> This gene encodes a member of the sorting nexin family. Members of this family contain a phox (PX) domain, which is a phosphoinositide binding domain, and are involved in intracellular trafficking. This protein does not contain a coiled coil region, like some family members, but contains a B41 domain. This protein interacts with the cytoplasmic domain of P-selectin, and may function in the intracellular trafficking of P-selectin. Alternative splicing results in multiple transcript variants …

**Accessions** — [HGNC:14979](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14979) · Entrez [9784](https://www.ncbi.nlm.nih.gov/gene/9784) · UniProt [Q15036](https://www.uniprot.org/uniprotkb/Q15036) · Ensembl [ENSG00000115234](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115234)

## Data

Gene col 3639: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3639); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3639, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3639]; `tensor/DDL_lfc|DDL_z.npy` [3639]; `embed/gene_vectors.npy` [3639]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3639 or target_col == 3639). Every well: [[SNX17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
