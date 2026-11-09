---
symbol: "PTCD3"
type: "gene"
col: 5294
ensembl_id: "ENSG00000132300"
name: "pentatricopeptide repeat domain 3"
location: "2p11.2"
module: 17
arm: "+"
pooled_cpm: 88.0
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# PTCD3

*pentatricopeptide repeat domain 3* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.59× (z +23.4, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.178×, HEC-1-A 0.451×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.419×, COLO 205 0.343×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Fluvoxamine (drug)]] 0.5 µM in 1 line (SW 1088 0.0505×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL1]] (+0.61, fdr 1e-05), [[ELP3]] (+0.59, fdr 9e-06), [[METTL17]] (+0.58, fdr 6e-05); moves opposite to [[ZBTB46]] (-0.61, fdr 7e-06), [[MIR22HG]] (-0.58, fdr 9e-05), [[DNMT3A]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PRPF39]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5294.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.59×** | +23.4 | 0e+00 | 48/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.88×** | +22.0 | 0e+00 | 46/48 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.41×** | +21.7 | 0e+00 | 48/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.97×** | +16.7 | 0e+00 | 46/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.96×** | +16.6 | 0e+00 | 48/48 (A-172, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.75×** | +13.8 | 2e-41 | 43/48 (LS 180, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.72×** | +12.9 | 4e-36 | 46/49 (LoVo, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.67×** | +12.6 | 1e-34 | 40/48 (NCI-H23, KATO III, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.43×** | +11.5 | 1e-28 | 41/48 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.60×** | +11.1 | 4e-27 | 41/48 (LoVo, NCI-H23, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +10.6 | 2e-24 | 39/48 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.50×** | +9.6 | 4e-20 | 33/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.43×** | +8.8 | 5e-17 | 36/48 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.41×** | +8.5 | 8e-16 | 34/48 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +8.1 | 2e-14 | 38/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +6.0 | 5e-08 | 31/48 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.26×** | +5.8 | 2e-07 | 26/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +5.6 | 5e-07 | 17/48 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +5.2 | 5e-06 | 23/48 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +4.7 | 6e-05 | 24/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.18× | +3.8 | 0.003 | 14/48 (SW 900, A549, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.13× | +3.0 | 0.051 | 6/48 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.26×** | +2.9 | 0.054 | 13/47 (MIA PaCa-2, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5294.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.178×, HEC-1-A 0.451×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-427 0.419×, COLO 205 0.343×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Fluvoxamine (drug)]] 0.5 µM in 1 line (SW 1088 0.0505×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 0.868× | -3.5 | 0.24 | 20/48 (KATO III, LS 180, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.875× | -3.3 | 0.24 | 16/47 (LS 180, SW 900, …) | two highest doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.876× | -3.2 | 0.28 | 16/47 (H4, KATO III, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.883× | -3.1 | 0.28 | 7/47 (AN3 CA, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5294. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 79.1 | 13 (9 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.30× (z +15.5) | — |
| [[NCI-H23 (line)]] | alt | 132 | 11 (7 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +14.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.35× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.530× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 90.4 | 11 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +15.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.85× (z +13.7) | — |
| [[SW480 (line)]] | alt | 134 | 9 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.89× (z +18.2) | — |
| [[HOP62 (line)]] | alt | 78.8 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +12.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.69× (z +11.9) | — |
| [[HT-29 (line)]] | alt | 62.3 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +15.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.45× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 61.5 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +14.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.48× (z +14.8) | — |
| [[NCI-H1792 (line)]] | alt | 109 | 7 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.10× (z +15.5) | — |
| [[PANC-1 (line)]] | alt | 88.2 | 7 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.43× (z +12.9) | — |
| [[HEC-1-A (line)]] | alt | 86.0 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +13.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.53× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.451× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 60.9 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.76× (z +18.2) | — |
| [[A498 (line)]] | wt | 83.3 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.10× (z +15.0) | — |
| [[AsPC-1 (line)]] | alt | 77.7 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.37× (z +17.0) | — |
| [[HS-578T (line)]] | alt | 52.1 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.88× (z +12.8) | — |
| [[LS 180 (line)]] | wt | 103 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.44× (z +17.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.39× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 91.1 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +14.2) | — |
| [[A-427 (line)]] | wt | 131 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +13.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.20× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 90.0 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.77× (z +14.6) | — |
| [[LOX-IMVI (line)]] | wt | 82.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.85× (z +11.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 121 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.27× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 64.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.27× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.178× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 69.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +9.9) | — |
| [[COLO 205 (line)]] | alt | 77.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.66× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 85.1 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.20× (z +11.8) | — |
| [[Hs 766T (line)]] | wt | 53.8 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.48× (z +13.1) | — |
| [[J82 (line)]] | alt | 50.1 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.62× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 71.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +10.8) | — |
| [[RKO (line)]] | wt | 118 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.20× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 90.6 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.42× (z +12.2) | — |
| [[SHP-77 (line)]] | alt | 94.5 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.92× (z +12.6) | — |
| [[BT-474 (line)]] | alt | 71.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.71× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 106 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.51× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 114 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.21× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 65.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.43× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 67.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.96× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 92.5 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 102 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.32× (z +11.1) | — |
| [[C32 (line)]] | wt | 60.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 60.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW 1088 (line)]] | alt | 77.4 | 0 | 1 | — | [[Fluvoxamine (drug)]] 0.5 µM 0.0505× (z -10.8) |
| [[AN3 CA (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 82.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 128 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5294), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL1]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 866 |
| [[ELP3]] | +0.59 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[METTL17]] | +0.58 | +0.38 / +0.60 | both halves | 6e-05 | STRING 857 |
| [[NUFIP1]] | +0.55 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[DHODH]] | +0.55 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[NUBPL]] | +0.55 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[DYNC2H1]] | +0.55 | +0.34 / +0.52 | both halves | 1e-04 |  |
| [[NDUFS2]] | +0.54 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[WDR11]] | +0.54 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[MRS2]] | +0.54 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[GEMIN5]] | +0.54 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[ZZZ3]] | +0.53 | +0.49 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB46]] | -0.61 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[MIR22HG]] | -0.58 | -0.37 / -0.69 | both halves | 9e-05 |  |
| [[DNMT3A]] | -0.54 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[RAB4B]] | -0.54 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[SPAG5-AS1]] | -0.52 | -0.23 / -0.53 | both halves | 5e-04 |  |
| [[MAPK6]] | -0.52 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[MICALL1]] | -0.52 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[JOSD1]] | -0.52 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[SLC23A3]] | -0.50 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[NFATC1]] | -0.50 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[MAFG]] | -0.49 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[ADGRL1-AS1]] | -0.48 | -0.30 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRPF39]] | C | PRPF39's natural level weakens PTCD3's drug response | PRPF39's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.03; direction not clear | 0.061 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.563). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.2, -4.9); signed map (-27.7, -13.7). **Vector** length 79.7, 22.1% of its response variance represented; |z| ≥ 3 in 1,227 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.5 | +10.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.4 | +3.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.9 | +5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +11.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.4 | +23.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +0.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.1 | +0.4 |
|  | [[Sonidegib (drug)]] 0.5 µM |  | +1.9 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.7 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.5 | -2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -0.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -2.7 |
|  | [[Infigratinib (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | pentatricopeptide repeat domain 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:86,106,223-86,142,157 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20758, DKFZp666K071, mS39 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Pentatricopeptide repeat containing; Small nucleolar RNA protein coding host genes; Small subunit mitochondrial ribosomal proteins |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EY7](https://www.uniprot.org/uniprotkb/Q96EY7) (Small ribosomal subunit protein mS39):

> Mitochondrial RNA-binding protein that has a role in mitochondrial translation.

**Summary**, from NCBI Gene [55037](https://www.ncbi.nlm.nih.gov/gene/55037):

> Enables rRNA binding activity and ribosomal small subunit binding activity. Involved in mitochondrial translation. Located in mitochondrial matrix. Implicated in combined oxidative phosphorylation deficiency 51. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24717) · Entrez [55037](https://www.ncbi.nlm.nih.gov/gene/55037) · UniProt [Q96EY7](https://www.uniprot.org/uniprotkb/Q96EY7) · Ensembl [ENSG00000132300](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132300)

## Data

Gene col 5294: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5294); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5294, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5294]; `tensor/DDL_lfc|DDL_z.npy` [5294]; `embed/gene_vectors.npy` [5294]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5294 or target_col == 5294). Every well: [[PTCD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTCD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
