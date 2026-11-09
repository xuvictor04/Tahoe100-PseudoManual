---
symbol: "CPSF4"
type: "gene"
col: 8394
ensembl_id: "ENSG00000160917"
name: "cleavage and polyadenylation specific factor 4"
location: "7q22.1"
module: 199
arm: "+"
pooled_cpm: 15.38
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/199"]
generated_by: "tahoemap"
---

# CPSF4

*cleavage and polyadenylation specific factor 4* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.81× (z +9.3, q 7e-18, up in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.81× (z +9.2, q 7e-18, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.665× (z -8.8, q 9e-16, down in 30 of 47 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-172 0.328×, Panc 03.27 0.257×, NCI-H2347 0.379×, PANC-1 0.460×; ⚠ cell-cycle shift, explains ~48% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.183×, KATO III 0.194×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 0.122×; ⚠ toxic; transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (BT-474 0.185×); [[Naproxen (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0996×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (NCI-H1573 0.251×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR5]] (+0.69, fdr 7e-06), [[TRABD]] (+0.67, fdr 1e-05), [[NTAQ1]] (+0.66, fdr 4e-05); moves opposite to [[AK9]] (-0.68, fdr 9e-06), [[DZIP3]] (-0.65, fdr 3e-05), [[BPTF]] (-0.65, fdr 9e-06).
> It is in [[Module 199]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8394.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.81×** | +9.3 | 7e-18 | 36/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.81×** | +9.2 | 7e-18 | 36/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +8.5 | 4e-15 | 38/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.58×** | +6.8 | 1e-09 | 24/42 (NCI-H460, RKO, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +5.9 | 5e-07 | 28/47 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +4.8 | 2e-04 | 16/47 (PANC-1, A549, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +4.6 | 4e-04 | 15/45 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +4.2 | 0.002 | 18/48 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.31×** | +4.2 | 0.002 | 15/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.29×** | +4.0 | 0.004 | 16/47 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.030 | 13/47 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +3.4 | 0.030 | 10/48 (RKO, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.077 | 13/48 (MIA PaCa-2, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8394.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-172 0.328×, Panc 03.27 0.257×, NCI-H2347 0.379×, PANC-1 0.460×; ⚠ cell-cycle shift, explains ~48% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.183×, KATO III 0.194×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 0.122×; ⚠ toxic; transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (BT-474 0.185×); [[Naproxen (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0996×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (NCI-H1573 0.251×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.665×** | -8.8 | 9e-16 | 30/47 (A-172, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.583×** | -8.1 | 2e-13 | 27/47 (SK-MEL-2, A-172, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.672×** | -6.2 | 1e-07 | 26/47 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.730×** | -4.9 | 1e-04 | 19/39 (A-172, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.913× | -4.8 | 2e-04 | 5/48 (HS-578T, SW 900, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.739×** | -4.5 | 6e-04 | 14/28 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.801×** | -3.5 | 0.043 | 13/47 (C32, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8394. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 18.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -10.4) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A498 (line)]] | wt | 17.8 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[BT-474 (line)]] | alt | 15.6 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.185× (z -9.8) |
| [[COLO 205 (line)]] | alt | 6.75 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0806× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0996× (z -9.2) |
| [[KATO III (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 13.8 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.251× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -10.0) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H460 (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -15.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -10.2) ⚠ cell-cycle shift, explains ~48% of this change |
| [[PANC-1 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -9.2) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 1 | — | [[LJI308 (drug)]] 0.05 µM 0.173× (z -8.7) |
| [[SW 900 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.301× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8394), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR5]] | +0.69 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[TRABD]] | +0.67 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[NTAQ1]] | +0.66 | +0.74 / +0.42 | both halves | 4e-05 |  |
| [[SNRNP40]] | +0.66 | +0.69 / +0.62 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions |
| [[FBXW2]] | +0.65 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[GNA12]] | +0.64 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[USB1]] | +0.64 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[NIPA2]] | +0.64 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[FAM20B]] | +0.64 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[RNF4]] | +0.63 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[TBC1D24]] | +0.63 | +0.70 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AK9]] | -0.68 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[DZIP3]] | -0.65 | -0.73 / -0.46 | both halves | 3e-05 |  |
| [[BPTF]] | -0.65 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[SGO1-AS1]] | -0.64 | -0.70 / -0.47 | both halves | 2e-05 |  |
| [[ANKRD26]] | -0.64 | -0.70 / -0.40 | both halves | 5e-05 |  |
| [[DNAH12]] | -0.64 | -0.69 / -0.44 | both halves | 3e-05 |  |
| [[ABCA10]] | -0.63 | -0.70 / -0.41 | both halves | 4e-05 |  |
| [[SLC22A1]] | -0.63 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[FBXO48]] | -0.63 | -0.69 / -0.53 | both halves | 1e-05 |  |
| [[HHLA3]] | -0.63 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[HELQ]] | -0.63 | -0.70 / -0.39 | both halves | 6e-05 |  |
| [[NBPF10]] | -0.62 | -0.66 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 199]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.725). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.2, -25.2); signed map (-42.7, -11.1). **Vector** length 75.7, 12.9% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | +4.2 | +6.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.1 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.8 | +9.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +2.8 | +4.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.4 | +0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -7.8 | -8.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -7.0 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -6.9 | -6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -3.9 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.2 | -0.4 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.2 | -2.2 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | cleavage and polyadenylation specific factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:99,438,922-99,457,373 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NAR, CPSF30 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; Cleavage and polyadenylation specific factor subunits |
| Reactome | 17 pathways, smallest: Processing of Intronless Pre-mRNAs; Processing of Capped Intronless Pre-mRNA; RNA Polymerase II Transcription Termination |
| Matched by | ensembl_id |

**Function**, from UniProt [O95639](https://www.uniprot.org/uniprotkb/O95639) (Cleavage and polyadenylation specificity factor subunit 4):

> Component of the cleavage and polyadenylation specificity factor (CPSF) complex that play a key role in pre-mRNA 3'-end formation, recognizing the AAUAAA signal sequence and interacting with poly(A) polymerase and other factors to bring about cleavage and poly(A) addition. CPSF4 binds RNA polymers with a preference for poly(U).

**Summary**, from NCBI Gene [10898](https://www.ncbi.nlm.nih.gov/gene/10898):

> Inhibition of the nuclear export of poly(A)-containing mRNAs caused by the influenza A virus NS1 protein requires its effector domain. The NS1 effector domain functionally interacts with the cellular 30 kDa subunit of cleavage and polyadenylation specific factor 4, an essential component of the 3' end processing machinery of cellular pre-mRNAs. In influenza virus-infected cells, the NS1 protein is physically associated with cleavage and polyadenylation specific factor 4, 30kD subunit. Binding …

**Accessions** — [HGNC:2327](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2327) · Entrez [10898](https://www.ncbi.nlm.nih.gov/gene/10898) · UniProt [O95639](https://www.uniprot.org/uniprotkb/O95639) · Ensembl [ENSG00000160917](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160917)

## Data

Gene col 8394: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8394); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8394, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8394]; `tensor/DDL_lfc|DDL_z.npy` [8394]; `embed/gene_vectors.npy` [8394]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8394 or target_col == 8394). Every well: [[CPSF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPSF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
