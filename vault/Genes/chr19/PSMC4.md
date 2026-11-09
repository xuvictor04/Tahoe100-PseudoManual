---
symbol: "PSMC4"
type: "gene"
col: 265
ensembl_id: "ENSG00000013275"
name: "proteasome 26S subunit, ATPase 4"
location: "19q13.11-q13.13"
module: 72
arm: "+"
pooled_cpm: 61.73
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# PSMC4

*proteasome 26S subunit, ATPase 4* — 19q13.11-q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (16 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 4.19× (z +16.4, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.733× (z -5.1, q 2e-04, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMC5]] (+0.70, fdr 7e-06), [[PSMC1]] (+0.68, fdr 7e-06), [[VCP]] (+0.68, fdr 7e-06); moves opposite to [[ARHGAP12]] (-0.53, fdr 1e-05), [[SNX30]] (-0.47, fdr 5e-05), [[TMEM131L]] (-0.47, fdr 3e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 18 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 265.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **4.19×** | +16.4 | 0e+00 | 47/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.80×** | +15.3 | 0e+00 | 47/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.98×** | +14.9 | 0e+00 | 48/48 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.67×** | +11.2 | 5e-27 | 39/43 (A-427, PANC-1, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.54×** | +10.6 | 2e-24 | 48/48 (HT-29, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.17×** | +8.2 | 3e-14 | 38/42 (SW480, NCI-H460, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.04×** | +8.1 | 4e-14 | 38/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.01×** | +8.0 | 1e-13 | 44/46 (PANC-1, NCI-H460, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.60×** | +7.8 | 4e-13 | 46/48 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.98×** | +7.8 | 4e-13 | 40/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.55×** | +7.1 | 8e-11 | 37/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.77×** | +6.5 | 4e-09 | 39/48 (PANC-1, A-427, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.73×** | +6.0 | 9e-08 | 42/48 (HOP62, PANC-1, …) | two highest doses | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.93×** | +5.8 | 3e-07 | 41/43 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **1.68×** | +5.7 | 5e-07 | 28/38 (SW480, HCT15, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.58×** | +5.1 | 1e-05 | 37/49 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.91×** | +3.5 | 0.012 | 24/48 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.32×** | +2.9 | 0.071 | 17/48 (SW480, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 265.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.733×** | -5.1 | 2e-04 | 35/48 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.720×** | -3.8 | 0.040 | 32/48 (KATO III, hTERT-HPNE, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 265. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 494 | 11 (6 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.20× (z +15.7) | — |
| [[NCI-H460 (line)]] | wt | 25.8 | 7 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.73× (z +11.6) | — |
| [[SW480 (line)]] | alt | 31.8 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.70× (z +12.7) | — |
| [[HT-29 (line)]] | alt | 38.2 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.24× (z +14.1) | — |
| [[A-172 (line)]] | wt | 39.3 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.73× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 33.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.63× (z +13.5) | — |
| [[HOP62 (line)]] | alt | 33.8 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.06× (z +14.8) | — |
| [[LoVo (line)]] | wt | 27.6 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.95× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 29.3 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.52× (z +12.1) | — |
| [[NCI-H1792 (line)]] | alt | 35.8 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.65× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 32.8 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.18× (z +10.3) | — |
| [[A-427 (line)]] | wt | 47.5 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.54× (z +10.3) | — |
| [[A549 (line)]] | wt | 57.1 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.67× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 27.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.06× (z +9.2) | — |
| [[C32 (line)]] | wt | 25.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.30× (z +11.1) | — |
| [[COLO 205 (line)]] | alt | 18.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 10.3× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 27.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.96× (z +12.8) | — |
| [[KATO III (line)]] | alt | 35.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.00× (z +12.5) | — |
| [[LS 180 (line)]] | wt | 32.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.09× (z +12.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 34.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.57× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 19.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.39× (z +11.9) | — |
| [[NCI-H2347 (line)]] | alt | 33.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.16× (z +12.5) | — |
| [[SW1417 (line)]] | alt | 31.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.90× (z +10.3) | — |
| [[H4 (line)]] | wt | 43.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.76× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 58.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.50× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 33.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.30× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 23.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.56× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 64.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.81× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 68.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.94× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 41.1 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.79× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 20.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.65× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 25.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.13× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 51.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.00× (z +8.5) | — |
| [[SW48 (line)]] | wt | 33.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.40× (z +9.0) | — |
| [[A498 (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 265), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMC5]] | +0.70 | +0.73 / +0.64 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMC1]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[VCP]] | +0.68 | +0.65 / +0.70 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 855 |
| [[PSMD13]] | +0.67 | +0.71 / +0.69 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MTORC1_SIGNALING; STRING 999 |
| [[PSMD8]] | +0.65 | +0.67 / +0.57 | both halves | 1e-05 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[ABCB8]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 | pathway: ABC-family protein mediated transport |
| [[PSMC3]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMD11]] | +0.62 | +0.57 / +0.64 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMB7]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 998 |
| [[PSMD6]] | +0.62 | +0.65 / +0.52 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMD3]] | +0.62 | +0.69 / +0.58 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[HSP90AA2P]] | +0.61 | +0.66 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP12]] | -0.53 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[SNX30]] | -0.47 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[TMEM131L]] | -0.47 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.0, -10.5); signed map (-28.2, -27.7). **Vector** length 76.5, 22.1% of its response variance represented; |z| ≥ 3 in 1,125 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.8 | +14.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.6 | +16.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.2 | +15.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +10.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.0 | +5.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.0 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -5.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | -3.6 | +4.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -3.1 | +8.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -2.5 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.7 | -0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit, ATPase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11-q13.13 — chr19:39,971,165-39,981,764 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TBP7, S6, MGC8570, MGC13687, MGC23214, TBP-7, RPT3; previously MIP224 |
| Gene groups (HGNC) | AAA ATPases; Proteasome |
| Hallmark sets | GLYCOLYSIS, MTORC1_SIGNALING, MYC_TARGETS_V1 |
| Reactome | 169 pathways, smallest: Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC); Cross-presentation of soluble exogenous antigens (endosomes) |
| Matched by | ensembl_id |

**Function**, from UniProt [P43686](https://www.uniprot.org/uniprotkb/P43686) (26S proteasome regulatory subunit 6B):

> Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair. PSMC4 belongs to …

**Summary**, from NCBI Gene [5704](https://www.ncbi.nlm.nih.gov/gene/5704):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9551](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9551) · Entrez [5704](https://www.ncbi.nlm.nih.gov/gene/5704) · UniProt [P43686](https://www.uniprot.org/uniprotkb/P43686) · Ensembl [ENSG00000013275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000013275)

## Data

Gene col 265: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 265); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 265, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 265]; `tensor/DDL_lfc|DDL_z.npy` [265]; `embed/gene_vectors.npy` [265]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 265 or target_col == 265). Every well: [[PSMC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
