---
symbol: "PNPLA7"
type: "gene"
col: 5093
ensembl_id: "ENSG00000130653"
name: "patatin like domain 7, lysophospholipase"
location: "9q34.3"
module: 38
arm: "+"
pooled_cpm: 21.41
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# PNPLA7

*patatin like domain 7, lysophospholipase* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.51× (z +11.5, q 6e-28, up in 46 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.05× (z +8.2, q 9e-14, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.301× (z -9.7, q 1e-19, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERFL]] (+0.62, fdr 2e-05), [[SLC23A3]] (+0.61, fdr 1e-05), [[GAL3ST1]] (+0.58, fdr 1e-05); moves opposite to [[UQCC2]] (-0.53, fdr 4e-05), [[RPUSD3]] (-0.48, fdr 4e-05), [[MRPL12]] (-0.46, fdr 6e-05).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5093.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.51×** | +11.5 | 6e-28 | 46/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +8.2 | 9e-14 | 37/47 (NCI-H460, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.70×** | +4.1 | 0.008 | 25/47 (Hs 766T, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +3.9 | 0.011 | 27/47 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 1.51× | +3.3 | 0.11 | 22/47 (MIA PaCa-2, NCI-H460, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.50× | +3.2 | 0.11 | 20/47 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.46× | +3.0 | 0.20 | 20/47 (MIA PaCa-2, HEC-1-A, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5093.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.301×** | -9.7 | 1e-19 | 43/47 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.315×** | -9.4 | 2e-18 | 42/47 (H4, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.322×** | -9.2 | 7e-18 | 39/47 (H4, COLO 205, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.342×** | -8.4 | 7e-15 | 36/46 (SNU-423, A498, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.416×** | -7.1 | 1e-10 | 33/46 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.428×** | -6.9 | 5e-10 | 38/47 (hTERT-HPNE, COLO 205, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.446×** | -6.6 | 4e-09 | 35/47 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.448×** | -6.5 | 5e-09 | 37/47 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.511×** | -5.5 | 3e-06 | 33/47 (HT-29, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.516×** | -5.2 | 1e-05 | 27/43 (J82, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.585×** | -4.4 | 6e-04 | 25/47 (HOP62, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.606×** | -4.1 | 0.002 | 29/48 (HOP62, H4, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.614×** | -3.8 | 0.005 | 23/45 (HT-29, A-172, …) | all doses, flat |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.624×** | -3.8 | 0.005 | 24/48 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.641×** | -3.6 | 0.011 | 22/47 (MIA PaCa-2, A-172, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.70 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5093. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 20.0 | 2 (1 ⚠) | 6 (4 ⚠) | [[Adagrasib (drug)]] 0.05 µM 2.46× (z +14.3) ⚠ position not correctable · without an alert: [[Auranofin (drug)]] 5 µM 13.5× (z +12.0) | [[Homoharringtonine (drug)]] 0.05 µM 0.0642× (z -12.7) |
| [[H4 (line)]] | wt | 38.6 | 0 | 7 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0110× (z -19.6) |
| [[A-172 (line)]] | wt | 53.2 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0868× (z -18.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.139× (z -10.6) |
| [[HT-29 (line)]] | alt | 33.8 | 0 | 5 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.113× (z -11.4) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.182× (z -9.0) |
| [[PANC-1 (line)]] | alt | 23.9 | 1 (1 ⚠) | 4 (3 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.56× (z +9.4) ⚠ position not correctable | [[Digitoxin (drug)]] 5 µM 0.164× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.172× (z -10.7) |
| [[COLO 205 (line)]] | alt | 78.7 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0885× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.165× (z -9.3) |
| [[A-427 (line)]] | wt | 27.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.54× (z +9.0) ⚠ position not correctable | [[Harringtonine (drug)]] 0.5 µM 0.194× (z -9.6) |
| [[A498 (line)]] | wt | 26.9 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.125× (z -10.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.206× (z -8.5) |
| [[A549 (line)]] | wt | 25.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 12.0 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0723× (z -12.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[J82 (line)]] | alt | 22.9 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0475× (z -15.2) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[hTERT-HPNE (line)]] | wt | 15.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0351× (z -13.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Vilanterol (drug)]] 0.05 µM 0.0660× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 17.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.85× (z +10.4) ⚠ position not correctable | [[Digitoxin (drug)]] 5 µM 0.170× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[RKO (line)]] | wt | 21.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0938× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SNU-423 (line)]] | alt | 25.6 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0732× (z -11.4) ⚠ cell-cycle shift, explains ~40% of this change |
| [[BT-474 (line)]] | alt | 22.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.07× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 21.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +8.9) | — |
| [[LoVo (line)]] | wt | 26.7 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.57× (z +9.5) ⚠ position not correctable | — |
| [[LOX-IMVI (line)]] | wt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 11.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.45× (z +13.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0854× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H460 (line)]] | wt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 47.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.203× (z -9.0) |
| [[AN3 CA (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5093), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERFL]] | +0.62 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[SLC23A3]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[GAL3ST1]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[TNXB]] | +0.57 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[ISY1-RAB43]] | +0.57 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[KLC4]] | +0.57 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[HSF4]] | +0.57 | +0.31 / +0.65 | both halves | 2e-04 |  |
| [[AKAP17A]] | +0.56 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[ING5]] | +0.55 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[SARM1]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[YJEFN3]] | +0.54 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SPACDR]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCC2]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[RPUSD3]] | -0.48 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[MRPL12]] | -0.46 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[R3HDM1]] | -0.46 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[YTHDC2]] | -0.46 | -0.21 / -0.54 | both halves | 7e-04 |  |
| [[SPECC1L]] | -0.44 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[MPHOSPH6]] | -0.44 | -0.34 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.509). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.0, -21.7); signed map (11.9, 10.5). **Vector** length 75.9, 16.0% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +3.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +1.7 | -1.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.6 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +1.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +2.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.7 | -7.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -5.1 | -8.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -9.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.2 | -6.9 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.2 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -3.6 |
|  | [[Riluzole hydrochloride (drug)]] 0.05 µM |  | -2.0 | -1.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.8 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -5.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | patatin like domain 7, lysophospholipase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,459,952-137,550,402 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ43070, FLJ31318, FLJ44279, RP11-48C7.2, NTEL1, NTE-R1; previously C9orf111 |
| Gene groups (HGNC) | Patatin like phospholipase domain containing |
| Reactome | 4 pathways, smallest: Glycerophospholipid catabolism; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZV29](https://www.uniprot.org/uniprotkb/Q6ZV29) (Patatin-like phospholipase domain-containing protein 7):

> Lysophospholipase which preferentially deacylates unsaturated lysophosphatidylcholine (C18:1), generating glycerophosphocholine. Also can deacylate, to a lesser extent, lysophosphatidylethanolamine (C18:1), lysophosphatidyl-L-serine (C18:1) and lysophosphatidic acid (C16:0).

**Summary**, from NCBI Gene [375775](https://www.ncbi.nlm.nih.gov/gene/375775):

> Human patatin-like phospholipases, such as PNPLA7, have been implicated in regulation of adipocyte differentiation and have been induced by metabolic stimuli (Wilson et al., 2006 [PubMed 16799181]).[supplied by OMIM, Jun 2008]

**Accessions** — [HGNC:24768](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24768) · Entrez [375775](https://www.ncbi.nlm.nih.gov/gene/375775) · UniProt [Q6ZV29](https://www.uniprot.org/uniprotkb/Q6ZV29) · Ensembl [ENSG00000130653](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130653)

## Data

Gene col 5093: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5093); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5093, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5093]; `tensor/DDL_lfc|DDL_z.npy` [5093]; `embed/gene_vectors.npy` [5093]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5093 or target_col == 5093). Every well: [[PNPLA7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNPLA7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
