---
symbol: "NPEPL1"
type: "gene"
col: 13265
ensembl_id: "ENSG00000215440"
name: "aminopeptidase like 1"
location: "20q13.32"
module: 126
arm: "+"
pooled_cpm: 13.88
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# NPEPL1

*aminopeptidase like 1* — 20q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.03× (z +8.9, q 2e-16, up in 19 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.26× (z +3.5, q 0.068, up in 15 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.402× (z -19.5, q 0e+00, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EME2]] (+0.69, fdr 7e-06), [[ZNF514]] (+0.65, fdr 1e-05), [[CERS2]] (+0.64, fdr 1e-05); moves opposite to [[TMEM205]] (-0.59, fdr 4e-05), [[KRT10]] (-0.59, fdr 2e-05, ⚠ KRT10 in the vector space only through flagged drug-doses), [[UQCR10]] (-0.58, fdr 1e-04, ⚠ UQCR10 in the vector space only through flagged drug-doses), [[KRTCAP2]] (-0.55, fdr 1e-04), [[INIP]] (-0.55, fdr 3e-05).
> It is in [[Module 126]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13265.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +8.9 | 2e-16 | 19/23 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.89×** | +8.9 | 2e-16 | 26/37 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +7.8 | 1e-12 | 19/29 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.068 | 15/47 (SW480, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13265.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.402×** | -19.5 | 0e+00 | 39/46 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.478×** | -11.1 | 2e-26 | 38/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.531×** | -9.6 | 2e-19 | 35/44 (BT-474, J82, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.552×** | -9.0 | 4e-17 | 28/47 (SNU-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.506×** | -8.6 | 7e-16 | 35/45 (MIA PaCa-2, SNU-1, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.581×** | -8.2 | 2e-14 | 25/47 (BT-474, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.638×** | -6.8 | 9e-10 | 24/47 (MIA PaCa-2, SW48, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.445×** | -6.4 | 1e-08 | 26/46 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.665×** | -6.2 | 4e-08 | 25/48 (MIA PaCa-2, HEC-1-A, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.700×** | -5.4 | 4e-06 | 19/43 (SW48, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.785×** | -3.7 | 0.013 | 16/48 (SW48, SW1417, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.787×** | -3.4 | 0.035 | 13/46 (SNU-1, NCI-H460, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.801×** | -3.3 | 0.035 | 17/45 (NCI-H460, NCI-H1573, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.664×** | -3.2 | 0.050 | 10/44 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.669×** | -3.2 | 0.057 | 11/47 (SW48, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13265. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 32.9 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -15.5) |
| [[BT-474 (line)]] | alt | 35.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -16.6) |
| [[J82 (line)]] | alt | 14.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -14.2) |
| [[A549 (line)]] | wt | 14.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 6.17 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0988× (z -11.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.279× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 15.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -17.1) |
| [[PANC-1 (line)]] | alt | 10.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -13.2) |
| [[SNU-1 (line)]] | wt | 34.0 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0914× (z -11.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.244× (z -11.2) |
| [[SW48 (line)]] | wt | 29.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -10.2) |
| [[A-172 (line)]] | wt | 9.80 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 7.54 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 7.98 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -10.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HepG2_C3A (line)]] | wt | 14.4 | 0 | 1 | — | [[crizotinib (drug)]] 0.05 µM 0.0812× (z -9.7) |
| [[HOP62 (line)]] | alt | 12.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -12.2) |
| [[Hs 766T (line)]] | wt | 24.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -14.6) |
| [[HT-29 (line)]] | alt | 7.74 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 6.58 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0470× (z -9.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H2030 (line)]] | alt | 6.88 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.5 µM 0.0584× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 24.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -10.8) |
| [[RKO (line)]] | wt | 23.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 17.5 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.146× (z -9.3) |
| [[SNU-423 (line)]] | alt | 8.17 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.119× (z -8.7) |
| [[A-427 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13265), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EME2]] | +0.69 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[ZNF514]] | +0.65 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[CERS2]] | +0.64 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[LY6G5B]] | +0.61 | +0.36 / +0.66 | both halves | 9e-05 |  |
| [[ABCF2]] | +0.60 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[WIZ]] | +0.60 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[AP1G2-AS1]] | +0.60 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[SPRYD4]] | +0.60 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[U2AF2]] | +0.59 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[IDUA]] | +0.59 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[METTL3]] | +0.59 | +0.57 / +0.49 | both halves | 2e-05 |  |
| [[SNHG22]] | +0.59 | +0.51 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM205]] | -0.59 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[KRT10]] ⚠ | -0.59 | -0.49 / -0.48 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UQCR10]] ⚠ | -0.58 | -0.34 / -0.54 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[KRTCAP2]] | -0.55 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[INIP]] | -0.55 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[COX7B]] | -0.55 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[POLR2J]] ⚠ | -0.55 | -0.44 / -0.43 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BTG1]] | -0.54 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ETFB]] | -0.54 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[ATP5PO]] ⚠ | -0.54 | -0.37 / -0.47 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ROMO1]] | -0.54 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[COX8A]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[SLC25A4]] | -0.54 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[LAGE3]] | -0.53 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[ATP5PD]] | -0.53 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[INAFM1]] | -0.52 | -0.41 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.682). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.2, -26.4); signed map (-11.9, -36.3). **Vector** length 66.0, 10.8% of its response variance represented; |z| ≥ 3 in 928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +0.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.5 | -19.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -1.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.2 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -0.2 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | aminopeptidase like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.32 — chr20:58,689,131-58,719,238 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11583, bA261P9.2 |
| Gene groups (HGNC) | Aminopeptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDH3](https://www.uniprot.org/uniprotkb/Q8NDH3) (Probable aminopeptidase NPEPL1):

> Probably catalyzes the removal of unsubstituted N-terminal amino acids from various peptides.

**Summary**, from NCBI Gene [79716](https://www.ncbi.nlm.nih.gov/gene/79716):

> Predicted to enable peptidase activity. Predicted to be involved in proteolysis. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16244](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16244) · Entrez [79716](https://www.ncbi.nlm.nih.gov/gene/79716) · UniProt [Q8NDH3](https://www.uniprot.org/uniprotkb/Q8NDH3) · Ensembl [ENSG00000215440](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215440)

## Data

Gene col 13265: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13265); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13265, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13265]; `tensor/DDL_lfc|DDL_z.npy` [13265]; `embed/gene_vectors.npy` [13265]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13265 or target_col == 13265). Every well: [[NPEPL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPEPL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
