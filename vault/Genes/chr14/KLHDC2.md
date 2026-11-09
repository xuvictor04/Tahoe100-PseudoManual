---
symbol: "KLHDC2"
type: "gene"
col: 9137
ensembl_id: "ENSG00000165516"
name: "kelch domain containing 2"
location: "14q21.3"
module: 187
arm: "+"
pooled_cpm: 23.29
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 30
n_dd_up_clean: 7
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/187"]
generated_by: "tahoemap"
---

# KLHDC2

*kelch domain containing 2* — 14q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.59× (z +13.0, q 4e-36, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.391× (z -18.7, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.621× (z -9.5, q 9e-19, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO8]] (+0.70, fdr 7e-06), [[EAPP]] (+0.69, fdr 7e-06), [[CDC37L1]] (+0.65, fdr 7e-06); moves opposite to [[SERBP1]] (-0.57, fdr 4e-05), [[NAA15]] (-0.55, fdr 5e-05), [[MIPOL1]] (-0.53, fdr 3e-05).
> It is in [[Module 187]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9137.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +13.0 | 4e-36 | 41/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +5.7 | 5e-06 | 26/48 (NCI-H2030, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 0.001 | 14/48 (RPMI-7951, CFPAC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.009 | 12/48 (A-172, LoVo, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.035 | 11/47 (HEC-1-A, KATO III, …) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.035 | 11/48 (CFPAC-1, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Alpelisib (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.035 | 10/46 (LS 180, SW480, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.035 | 7/44 (PANC-1, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.4 | 0.035 | 14/47 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.038 | 9/48 (SW480, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.054 | 11/47 (BT-474, RKO, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.12× | +3.2 | 0.074 | 6/48 (A549, HT-29, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.11 | 5/48 (HOP62, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 17 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9137.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.391×** | -18.7 | 0e+00 | 47/48 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.621×** | -9.5 | 9e-19 | 34/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.656×** | -8.4 | 1e-14 | 29/47 (NCI-H1792, HOP62, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.446×** | -8.3 | 1e-14 | 32/47 (SHP-77, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.674×** | -7.8 | 5e-13 | 31/48 (AsPC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.673×** | -7.4 | 1e-11 | 27/48 (NCI-H460, J82, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.688×** | -7.4 | 1e-11 | 27/47 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.495×** | -7.2 | 3e-11 | 28/48 (A-427, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.504×** | -7.1 | 1e-10 | 29/46 (A498, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.514×** | -6.9 | 4e-10 | 30/44 (A-427, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.636×** | -6.4 | 7e-09 | 29/48 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.537×** | -6.4 | 7e-09 | 28/47 (A-427, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.742×** | -5.9 | 1e-07 | 24/47 (HT-29, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.736×** | -5.9 | 2e-07 | 25/47 (H4, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.755×** | -5.6 | 9e-07 | 21/48 (NCI-H1792, SW 1088, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.707×** | -4.9 | 3e-05 | 21/48 (SW 1271, MIA PaCa-2, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.847× | -4.7 | 9e-05 | 20/48 (LS 180, HCT15, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.741×** | -4.3 | 6e-04 | 19/48 (AsPC-1, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.753×** | -4.0 | 0.001 | 8/48 (NCI-H460, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9137. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 19.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.351× (z -9.0) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 22.5 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +10.7) | [[Lonafarnib (drug)]] 5 µM 0.113× (z -11.2) ⚠ toxic |
| [[A549 (line)]] | wt | 23.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 34.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SK-MEL-2 (line)]] | alt | 25.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -10.4) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.250× (z -9.7) |
| [[A-172 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.328× (z -8.7) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.350× (z -8.8) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 26.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.123× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[HOP62 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.277× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HT-29 (line)]] | alt | 25.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +12.1) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[KATO III (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.276× (z -8.9) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 14.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.277× (z -10.5) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 17.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.368× (z -8.5) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.329× (z -10.2) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.350× (z -8.9) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9137), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO8]] | +0.70 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[EAPP]] | +0.69 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[CDC37L1]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[C14orf28]] | +0.64 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[CREBRF]] | +0.64 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[TAPT1]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[IKZF5]] | +0.63 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[UBN2]] | +0.63 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[WBP1]] | +0.62 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[TRIM23]] | +0.62 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[JMY]] | +0.62 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[ATOSA]] | +0.62 | +0.44 / +0.65 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERBP1]] | -0.57 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[NAA15]] | -0.55 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[MIPOL1]] | -0.53 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[PITPNB]] | -0.53 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[RNGTT]] | -0.53 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[EIPR1]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[TMEM241]] | -0.52 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[TAF1B]] | -0.51 | -0.41 / -0.54 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 187]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.4, -46.6); signed map (-13.7, 7.5). **Vector** length 91.8, 19.5% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +13.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +3.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.9 | +3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.8 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +5.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.3 | +3.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.2 | +2.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.3 | -18.7 |
|  | [[EX229 (drug)]] 5 µM |  | -5.9 | -8.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.1 | -7.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.1 | -7.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.1 | -6.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.0 | -6.4 |

## What is on record

|  |  |
|---|---|
| Name | kelch domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.3 — chr14:49,768,130-49,786,385 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HCLP-1, LCP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2U9](https://www.uniprot.org/uniprotkb/Q9Y2U9) (Kelch domain-containing protein 2):

> Substrate-recognition component of a Cul2-RING (CRL2) E3 ubiquitin-protein ligase complex of the DesCEND (destruction via C-end degrons) pathway, which recognizes a C-degron located at the extreme C terminus of target proteins, leading to their ubiquitination and degradation. The C-degron recognized by the DesCEND pathway is usually a motif of less than ten residues and can be present in full-length proteins, truncated proteins or proteolytically cleaved forms. The CRL2(KLHDC2) complex …

**Summary**, from NCBI Gene [23588](https://www.ncbi.nlm.nih.gov/gene/23588):

> Enables ubiquitin-like ligase-substrate adaptor activity. Involved in ubiquitin-dependent protein catabolic process via the C-end degron rule pathway. Located in nuclear body and nuclear membrane. Is active in Cul2-RING ubiquitin ligase complex and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20231](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20231) · Entrez [23588](https://www.ncbi.nlm.nih.gov/gene/23588) · UniProt [Q9Y2U9](https://www.uniprot.org/uniprotkb/Q9Y2U9) · Ensembl [ENSG00000165516](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165516)

## Data

Gene col 9137: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9137); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9137, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9137]; `tensor/DDL_lfc|DDL_z.npy` [9137]; `embed/gene_vectors.npy` [9137]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9137 or target_col == 9137). Every well: [[KLHDC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHDC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
