---
symbol: "PPP6C"
type: "gene"
col: 4066
ensembl_id: "ENSG00000119414"
name: "protein phosphatase 6 catalytic subunit"
location: "9q33.3"
module: 118
arm: "+"
pooled_cpm: 55.58
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# PPP6C

*protein phosphatase 6 catalytic subunit* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.02× (z +26.8, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.939× (z -6.4, q 1e-07, down in 0 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.881× (z -5.1, q 9e-05, down in 14 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (AsPC-1 0.212×, Panc 03.27 0.272×, A-427 0.252×, KATO III 0.392×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.384×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.349×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Clopidogrel (drug)]] 0.5 µM in 1 line (SW 1088 0.0495×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM7]] (+0.61, fdr 1e-05), [[LSM1]] (+0.61, fdr 1e-05), [[BRAP]] (+0.60, fdr 1e-05); moves opposite to [[GLS]] (-0.50, fdr 3e-05), [[TRIM36]] (-0.49, fdr 4e-05), [[PEAK1]] (-0.47, fdr 5e-05).
> It sits in the **+** arm of [[Module 118]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4066.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.02×** | +26.8 | 0e+00 | 48/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.55×** | +18.9 | 0e+00 | 45/48 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +15.7 | 0e+00 | 41/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +11.6 | 7e-29 | 38/48 (A-172, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +11.0 | 3e-26 | 42/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +10.9 | 7e-26 | 37/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +10.3 | 5e-23 | 34/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +10.0 | 8e-22 | 39/48 (HEC-1-A, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.39×** | +9.4 | 4e-19 | 37/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +9.3 | 5e-19 | 36/48 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +8.6 | 3e-16 | 38/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.35×** | +8.5 | 7e-16 | 33/48 (MIA PaCa-2, SW480, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +8.5 | 8e-16 | 33/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +7.5 | 3e-12 | 29/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | **1.28×** | +7.1 | 4e-11 | 29/47 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.007 | 13/49 (PANC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4066.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (AsPC-1 0.212×, Panc 03.27 0.272×, A-427 0.252×, KATO III 0.392×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.384×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.349×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Clopidogrel (drug)]] 0.5 µM in 1 line (SW 1088 0.0495×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -6.4 | 1e-07 | 0/49 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.881× | -5.1 | 9e-05 | 14/48 (SHP-77, A-172, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.876× | -3.8 | 0.024 | 17/48 (SHP-77, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.877× | -3.8 | 0.024 | 9/48 (H4, LoVo, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.882× | -3.6 | 0.037 | 8/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.798×** | -3.4 | 0.074 | 10/48 (J82, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4066. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 72.6 | 8 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.68× (z +19.3) | — |
| [[PANC-1 (line)]] | alt | 40.1 | 7 | 0 | [[TAK-901 (drug)]] 5 µM 6.09× (z +13.3) | — |
| [[A-172 (line)]] | wt | 63.3 | 4 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.70× (z +17.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 67.2 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 8.09× (z +14.8) | — |
| [[LOX-IMVI (line)]] | wt | 61.6 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 6.95× (z +12.6) | — |
| [[NCI-H460 (line)]] | wt | 64.1 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 6.59× (z +15.0) | — |
| [[A498 (line)]] | wt | 57.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +12.9) | — |
| [[COLO 205 (line)]] | alt | 68.6 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.1× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 64.7 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.74× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[LoVo (line)]] | wt | 46.7 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 9.16× (z +13.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 52.1 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 16.0× (z +14.8) | — |
| [[Panc 03.27 (line)]] | alt | 61.1 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.06× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[RKO (line)]] | wt | 82.5 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.72× (z +10.8) | — |
| [[A-427 (line)]] | wt | 36.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[A549 (line)]] | wt | 55.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 80.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.74× (z +11.1) | — |
| [[HOP62 (line)]] | alt | 46.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.46× (z +13.5) | — |
| [[LS 180 (line)]] | wt | 55.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.09× (z +12.1) | — |
| [[NCI-H23 (line)]] | alt | 52.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.02× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 40.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[C-33 A (line)]] | alt | 62.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.05× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 63.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.74× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 58.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.49× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 39.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.86× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 52.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.45× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 51.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.51× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 50.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.29× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 47.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.98× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 90.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.25× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 50.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.52× (z +9.5) | — |
| [[SW 1088 (line)]] | alt | 47.0 | 0 | 1 | — | [[Clopidogrel (drug)]] 0.5 µM 0.0495× (z -8.7) |
| [[SW1417 (line)]] | alt | 70.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.75× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 56.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4066), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM7]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[LSM1]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[BRAP]] | +0.60 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[ZNF16]] | +0.59 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[LMAN2L]] | +0.59 | +0.61 / +0.53 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[USF3]] | +0.59 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[CDK11B]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[DNAJC7]] | +0.59 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[PSMC1]] | +0.58 | +0.60 / +0.54 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[ALKBH1]] | +0.57 | +0.72 / +0.44 | both halves | 3e-05 |  |
| [[EMC3]] | +0.57 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ZNF322]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLS]] | -0.50 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[TRIM36]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[PEAK1]] | -0.47 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[TFRC]] | -0.45 | -0.53 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.560). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-26.3, -10.0); signed map (-6.6, -11.9). **Vector** length 76.4, 15.6% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.8 | +26.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.2 | +18.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.7 | +0.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.6 | +8.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +3.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +0.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.7 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.4 | -2.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.4 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -0.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 6 catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:125,146,573-125,189,939 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PP6 |
| Gene groups (HGNC) | Protein phosphatase catalytic subunits |
| Reactome | 11 pathways, smallest: Telomere Extension By Telomerase; Extension of Telomeres; COPII-mediated vesicle transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O00743](https://www.uniprot.org/uniprotkb/O00743) (Serine/threonine-protein phosphatase 6 catalytic subunit):

> Catalytic subunit of protein phosphatase 6 (PP6). PP6 is a component of a signaling pathway regulating cell cycle progression in response to IL2 receptor stimulation. N-terminal domain restricts G1 to S phase progression in cancer cells, in part through control of cyclin D1. During mitosis, regulates spindle positioning. Down-regulates MAP3K7 kinase activation of the IL1 signaling pathway by dephosphorylation of MAP3K7. Also participates in the innate immune defense against viruses by …

**Summary**, from NCBI Gene [5537](https://www.ncbi.nlm.nih.gov/gene/5537):

> This gene encodes the catalytic subunit of protein phosphatase, a component of a signaling pathway regulating cell cycle progression. Splice variants encoding different protein isoforms exist. The pseudogene of this gene is located on chromosome X. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9323](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9323) · Entrez [5537](https://www.ncbi.nlm.nih.gov/gene/5537) · UniProt [O00743](https://www.uniprot.org/uniprotkb/O00743) · Ensembl [ENSG00000119414](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119414)

## Data

Gene col 4066: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4066); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4066, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4066]; `tensor/DDL_lfc|DDL_z.npy` [4066]; `embed/gene_vectors.npy` [4066]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4066 or target_col == 4066). Every well: [[PPP6C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP6C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
