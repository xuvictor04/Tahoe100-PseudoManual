---
symbol: "EPN1"
type: "gene"
col: 726
ensembl_id: "ENSG00000063245"
name: "epsin 1"
location: "19q13.42"
module: 2
arm: "+"
pooled_cpm: 49.58
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# EPN1

*epsin 1* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.21× (z +18.0, q 0e+00, up in 44 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.50× (z +9.2, q 5e-18, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.685× (z -8.3, q 5e-14, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INTS1]] (+0.69, fdr 1e-05), [[DPP9]] (+0.68, fdr 7e-06), [[TUBGCP6]] (+0.68, fdr 1e-05); moves opposite to [[RPP25L]] (-0.60, fdr 5e-05), [[SCAF11]] (-0.59, fdr 2e-05), [[TMEM17]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 726.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.21×** | +18.0 | 0e+00 | 44/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +15.5 | 0e+00 | 37/40 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +9.7 | 6e-20 | 30/43 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +9.2 | 5e-18 | 37/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +8.4 | 5e-15 | 1/49 (NCI-H661) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +8.3 | 1e-14 | 33/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +7.3 | 2e-11 | 28/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.51×** | +4.9 | 8e-05 | 24/49 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.22×** | +4.5 | 4e-04 | 21/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Pentoxifylline (drug)]] 0.5 µM |  | **1.20×** | +4.2 | 0.002 | 20/48 (HT-29, hTERT-HPNE, …) | two highest doses | position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM |  | **1.22×** | +4.1 | 0.002 | 16/48 (HOP62, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.8 | 0.007 | 11/35 (A-172, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | 1.15× | +3.2 | 0.057 | 14/47 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.069 | 11/47 (KATO III, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 726.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.685×** | -8.3 | 5e-14 | 38/48 (NCI-H23, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.709×** | -7.6 | 1e-11 | 32/48 (AN3 CA, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.754×** | -6.5 | 2e-08 | 26/47 (Panc 03.27, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.768×** | -6.0 | 2e-07 | 27/48 (A-427, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.837× | -5.6 | 2e-06 | 20/48 (KATO III, C32, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.786×** | -5.3 | 1e-05 | 24/47 (A-427, C-33 A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.847× | -5.3 | 1e-05 | 25/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.841× | -3.8 | 0.009 | 15/49 (A-427, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.895× | -3.5 | 0.024 | 9/48 (AsPC-1, A-427, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.866× | -3.3 | 0.054 | 18/48 (A-427, SNU-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.888× | -3.2 | 0.062 | 10/48 (A-427, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.866× | -3.0 | 0.12 | 11/48 (A-427, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 726. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 43.2 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +15.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.01× (z +9.6) | — |
| [[A-172 (line)]] | wt | 74.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +11.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 48.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.05 µM 0.433× (z -8.5) |
| [[A498 (line)]] | wt | 80.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +14.3) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 66.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.81× (z +13.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 34.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +12.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 47.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +12.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 69.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.30× (z +9.3) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 63.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +11.2) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 41.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 44.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 38.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.332× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 29.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.25× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 46.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +11.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 65.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +16.2) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 62.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +12.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 44.0 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0986× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 64.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 54.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 36.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.83× (z +10.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 47.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 76.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.27× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 34.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 43.5 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.107× (z -9.6) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 37.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 5 µM 0.0610× (z -9.3) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 30.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 47.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 98.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 47.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 726), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS1]] | +0.69 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[DPP9]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[TUBGCP6]] | +0.68 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[SBF1]] | +0.68 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[EHBP1L1]] | +0.68 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[INTS11]] | +0.67 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[PPP4C]] | +0.67 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[CPSF1]] | +0.66 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[FBRSL1]] | +0.65 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[PCNX3]] | +0.65 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[AP1M1]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 | STRING 675 |
| [[AMPD2]] | +0.64 | +0.61 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP25L]] | -0.60 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[SCAF11]] | -0.59 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[TMEM17]] | -0.58 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[CGAS]] | -0.57 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[KIAA1586]] | -0.57 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[NFYB]] | -0.57 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[SDSL]] | -0.57 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[RBM43]] | -0.56 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[ARL14EP]] | -0.56 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[PLEKHF2]] | -0.55 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[C1orf131]] | -0.54 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[BTN2A3P-1]] | -0.54 | -0.50 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.630). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (9.1, -26.4); signed map (-50.4, 1.5). **Vector** length 103, 24.2% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.8 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +18.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +9.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.8 | +8.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +2.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.5 | -6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.4 | -8.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -3.6 | -5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.2 | -5.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.1 | -7.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | epsin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,675,226-55,709,858 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Epsin family |
| Reactome | 7 pathways, smallest: EGFR downregulation; Signaling by EGFR; Cargo recognition for clathrin-mediated endocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6I3](https://www.uniprot.org/uniprotkb/Q9Y6I3) (Epsin-1):

> Binds to membranes enriched in phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2). Modifies membrane curvature and facilitates the formation of clathrin-coated invaginations (By similarity). Regulates receptor-mediated endocytosis.

**Summary**, from NCBI Gene [29924](https://www.ncbi.nlm.nih.gov/gene/29924):

> This gene encodes a member of the epsin protein family. The encoded protein binds clathrin and is involved in the endocytosis of clathrin-coated vesicles. Loss of function of this gene is associated with reduced tumor growth and progression in certain cancer types. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:21604](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21604) · Entrez [29924](https://www.ncbi.nlm.nih.gov/gene/29924) · UniProt [Q9Y6I3](https://www.uniprot.org/uniprotkb/Q9Y6I3) · Ensembl [ENSG00000063245](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000063245)

## Data

Gene col 726: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 726); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 726, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 726]; `tensor/DDL_lfc|DDL_z.npy` [726]; `embed/gene_vectors.npy` [726]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 726 or target_col == 726). Every well: [[EPN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
