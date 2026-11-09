---
symbol: "MAF1"
type: "gene"
col: 11050
ensembl_id: "ENSG00000179632"
name: "MAF1 negative regulator of RNA polymerase III"
location: "8q24.3"
module: 130
arm: "+"
pooled_cpm: 23.53
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 25
n_dd_up_clean: 2
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# MAF1

*MAF1 negative regulator of RNA polymerase III* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.96× (z +8.2, q 1e-13, up in 39 of 44 measured lines) ⚠ transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +5.7, q 2e-06, up in 28 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 4.64×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 2.65×).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.436× (z -10.1, q 5e-21, down in 39 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.447× (z -9.8, q 4e-20, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDIPT]] (+0.59, fdr 1e-05), [[MKRN1]] (+0.58, fdr 6e-05), [[MEN1]] (+0.56, fdr 1e-05); moves opposite to [[SNRPF]] (-0.53, fdr 3e-05), [[CCDC88A]] (-0.52, fdr 4e-05), [[GGT7]] (-0.47, fdr 1e-04).
> It is in [[Module 130]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11050.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 4.64×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 2.65×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.96×** | +8.2 | 1e-13 | 39/44 (NCI-H2030, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.93×** | +8.0 | 3e-13 | 32/42 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +6.3 | 7e-08 | 22/32 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.7 | 2e-06 | 28/46 (A549, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.004 | 26/48 (LOX-IMVI, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +3.4 | 0.071 | 19/37 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.31× | +3.2 | 0.11 | 17/46 (LOX-IMVI, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.29× | +3.2 | 0.11 | 18/46 (KATO III, LOX-IMVI, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11050.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.436×** | -10.1 | 5e-21 | 39/46 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.447×** | -9.8 | 4e-20 | 47/47 (A549, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.448×** | -9.7 | 4e-20 | 42/47 (AsPC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.467×** | -9.2 | 4e-18 | 43/48 (A498, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.519×** | -7.9 | 2e-13 | 36/47 (A498, AsPC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.658×** | -7.1 | 9e-11 | 31/47 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.561×** | -7.0 | 2e-10 | 40/47 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.607×** | -6.0 | 1e-07 | 33/48 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.637×** | -5.5 | 3e-06 | 32/48 (A498, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.733×** | -5.3 | 7e-06 | 35/48 (A498, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.649×** | -5.2 | 9e-06 | 28/47 (A498, BT-474, …) | all doses, flat | cell-cycle shift (explains ~24% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.508×** | -4.3 | 8e-04 | 26/48 (NCI-H1792, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.726×** | -3.9 | 0.005 | 23/47 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.729×** | -3.6 | 0.013 | 16/48 (SNU-1, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.911× | -3.5 | 0.015 | 4/48 (AN3 CA, BT-474, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.574×** | -3.5 | 0.016 | 22/44 (SW1417, A498, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.756×** | -3.4 | 0.026 | 19/46 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.591×** | -3.3 | 0.026 | 15/46 (A498, RKO, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.617×** | -3.3 | 0.026 | 14/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11050. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 50.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.243× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.376× (z -9.2) |
| [[A549 (line)]] | wt | 25.6 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.240× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 25.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -14.1) |
| [[AsPC-1 (line)]] | alt | 27.8 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.203× (z -10.6) ⚠ unreliable plate only · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.214× (z -10.2) |
| [[HS-578T (line)]] | alt | 39.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 33.1 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.316× (z -9.7) |
| [[PANC-1 (line)]] | alt | 22.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -9.5) |
| [[SW480 (line)]] | alt | 16.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.64× (z +11.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.317× (z -8.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 16.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 17.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.160× (z -9.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 31.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.310× (z -8.8) |
| [[LoVo (line)]] | wt | 20.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.300× (z -8.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.261× (z -9.1) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 14.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.192× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 11.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.232× (z -9.2) |
| [[SW 900 (line)]] | alt | 22.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.208× (z -9.2) |
| [[SW1417 (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.301× (z -9.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11050), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDIPT]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[MKRN1]] | +0.58 | +0.38 / +0.68 | both halves | 6e-05 | pathway: Intracellular signaling by second messengers |
| [[MEN1]] | +0.56 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[PCMTD1]] | +0.55 | +0.38 / +0.61 | both halves | 6e-05 |  |
| [[CSNK2B]] | +0.55 | +0.52 / +0.57 | both halves | 1e-05 | pathway: Intracellular signaling by second messengers |
| [[BROX]] | +0.54 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[MAT2B]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[KIAA1191]] | +0.54 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[JMY]] | +0.54 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[TDP2]] | +0.54 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[FBXO8]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[CORO1B]] | +0.52 | +0.50 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPF]] | -0.53 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[CCDC88A]] | -0.52 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[GGT7]] | -0.47 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[CELF1]] | -0.46 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[LUC7L3]] | -0.45 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[ADRA1B]] | -0.44 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[DGKD]] | -0.43 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[SYP]] | -0.43 | -0.35 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.529). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-17.7, -21.7); signed map (-17.9, 8.1). **Vector** length 94.5, 22.8% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +5.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.7 | +8.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +4.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.0 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.6 | +1.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.0 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.2 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.0 | -10.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.6 | -9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.5 | -9.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.5 | -3.9 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -3.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.5 | -3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | MAF1 negative regulator of RNA polymerase III |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,104,420-144,107,611 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp586G1123 |
| Reactome | 4 pathways, smallest: Regulation of PTEN gene transcription; PTEN Regulation; PIP3 activates AKT signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H063](https://www.uniprot.org/uniprotkb/Q9H063) (Repressor of RNA polymerase III transcription MAF1 homolog):

> Plays a role in the repression of RNA polymerase III-mediated transcription in response to changing nutritional, environmental and cellular stress conditions to balance the production of highly abundant tRNAs, 5S rRNA, and other small non-coding RNAs with cell growth and maintenance. Also plays a key role in cell fate determination by promoting mesorderm induction and adipocyte differentiation (By similarity). Mechanistically, associates with the RNA polymerase III clamp and thereby impairs its …

**Summary**, from NCBI Gene [84232](https://www.ncbi.nlm.nih.gov/gene/84232):

> This gene encodes a protein that is similar to Maf1, a Saccharomyces cerevisiae protein highly conserved in eukaryotic cells. Yeast Maf1 is a negative effector of RNA polymerase III (Pol III). It responds to changes in the cellular environment and represses pol III transcription. Biochemical studies identified the initiation factor TFIIIB as a target for Maf1-dependent repression. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24966](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24966) · Entrez [84232](https://www.ncbi.nlm.nih.gov/gene/84232) · UniProt [Q9H063](https://www.uniprot.org/uniprotkb/Q9H063) · Ensembl [ENSG00000179632](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179632)

## Data

Gene col 11050: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11050); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11050, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11050]; `tensor/DDL_lfc|DDL_z.npy` [11050]; `embed/gene_vectors.npy` [11050]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11050 or target_col == 11050). Every well: [[MAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
