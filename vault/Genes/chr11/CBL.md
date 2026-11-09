---
symbol: "CBL"
type: "gene"
col: 3134
ensembl_id: "ENSG00000110395"
name: "Cbl proto-oncogene"
location: "11q23.3"
module: 2
arm: "+"
pooled_cpm: 134.32
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CBL

*Cbl proto-oncogene* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.55× (z +14.8, q 0e+00, up in 39 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.51× (z +13.8, q 6e-41, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.740× (z -14.5, q 1e-44, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP18]] (+0.64, fdr 1e-05), [[NIPA1]] (+0.64, fdr 1e-05), [[TSPAN17]] (+0.63, fdr 2e-05); moves opposite to [[QTRT1]] (-0.62, fdr 1e-05), [[BCLAF1]] (-0.60, fdr 3e-05), [[YJU2]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3134.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +14.8 | 0e+00 | 39/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +13.8 | 6e-41 | 39/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +13.3 | 3e-38 | 42/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +13.0 | 1e-36 | 39/48 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +13.0 | 1e-36 | 43/48 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +11.5 | 9e-29 | 40/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +11.5 | 1e-28 | 37/48 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +11.1 | 6e-27 | 38/48 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +10.8 | 1e-25 | 29/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +10.6 | 1e-24 | 40/49 (NCI-H1573, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +9.6 | 4e-20 | 34/48 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +8.7 | 2e-16 | 35/48 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +8.6 | 5e-16 | 31/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +7.9 | 2e-13 | 28/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +6.8 | 5e-10 | 31/45 (NCI-H2030, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +6.1 | 3e-08 | 22/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.21×** | +5.9 | 9e-08 | 23/48 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +5.5 | 1e-06 | 30/49 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3134.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.740×** | -14.5 | 1e-44 | 30/48 (NCI-H1573, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.733×** | -9.8 | 4e-20 | 34/45 (KATO III, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.635×** | -8.1 | 1e-13 | 29/49 (HOP62, SW1417, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.887× | -5.8 | 9e-07 | 14/48 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | 0.871× | -4.6 | 6e-04 | 17/48 (NCI-H1573, HEC-1-A, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.909× | -4.5 | 6e-04 | 6/49 (NCI-H23, HCT15, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.878× | -4.4 | 7e-04 | 22/49 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.790×** | -4.2 | 0.002 | 12/38 (Panc 03.27, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.885× | -4.2 | 0.002 | 8/48 (NCI-H1792, HepG2/C3A, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.899× | -3.6 | 0.015 | 7/47 (NCI-H2347, hTERT-HPNE, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.904× | -3.5 | 0.025 | 6/48 (Hs 766T, HT-29, …) | all doses, stronger at high dose |  |
| [[Arbutin (drug)]] 0.05 µM |  | 0.897× | -3.5 | 0.025 | 13/48 (Panc 03.27, LS 180, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.824×** | -3.4 | 0.025 | 15/47 (AsPC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.906× | -3.4 | 0.029 | 6/48 (RPMI-7951, LS 180, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 0.907× | -3.4 | 0.029 | 8/48 (NCI-H1573, hTERT-HPNE, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.833× | -3.2 | 0.039 | 17/48 (Hs 766T, SW1417, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 0.5 µM |  | 0.910× | -3.2 | 0.039 | 5/48 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.912× | -3.2 | 0.047 | 9/48 (NCI-H1573, A-172, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.914× | -3.1 | 0.054 | 6/48 (HOP62, A-172, …) | all doses, flat |  |
| [[Artesunate (drug)]] 0.05 µM |  | 0.914× | -3.1 | 0.054 | 1/48 (BT-474) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3134. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 224 | 0 | 19 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -24.0) |
| [[CFPAC-1 (line)]] | alt | 77.9 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.53× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 113 | 5 (2 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 2.16× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.636× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 184 | 3 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.06× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.586× (z -11.3) |
| [[KATO III (line)]] | alt | 183 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.02× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -18.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 102 | 4 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 2.11× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.574× (z -12.5) |
| [[SW480 (line)]] | alt | 185 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.01× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +13.5) | — |
| [[H4 (line)]] | wt | 90.1 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.95× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.84× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 161 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.629× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 121 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 1.80× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 242 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 1.92× (z +14.4) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 1.76× (z +12.8) | — |
| [[SNU-423 (line)]] | alt | 96.1 | 2 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 1.96× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.86× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.635× (z -8.8) |
| [[J82 (line)]] | alt | 124 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -12.5) |
| [[LS 180 (line)]] | wt | 92.1 | 1 | 1 | [[Auranofin (drug)]] 5 µM 1.99× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.559× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 178 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +8.9) | [[Cobimetinib (drug)]] 5 µM 0.538× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 175 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 216 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.586× (z -10.3) |
| [[SW1417 (line)]] | alt | 174 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.70× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 1.63× (z +9.5) | — |
| [[A-172 (line)]] | wt | 96.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -15.7) |
| [[A549 (line)]] | wt | 96.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.522× (z -8.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 167 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 121 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.343× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 109 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.06× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 245 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 125 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 86.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.658× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.23× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.99× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.346× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 96.8 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0833× (z -9.4) |
| [[SW48 (line)]] | wt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -9.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 74.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 177 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 86.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 98.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 138 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3134), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP18]] | +0.64 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[NIPA1]] | +0.64 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[TSPAN17]] | +0.63 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[SLC27A4]] | +0.62 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[TPST2]] | +0.61 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[DOP1B]] | +0.59 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[PIP5K1C]] | +0.59 | +0.48 / +0.52 | both halves | 2e-05 | pathway: Clathrin-mediated endocytosis |
| [[CORO7]] | +0.59 | +0.67 / +0.39 | both halves | 5e-05 |  |
| [[EPS15]] | +0.58 | +0.69 / +0.41 | both halves | 4e-05 | pathway: Bacterial Infection Pathways; STRING 766 |
| [[TMEM184B]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[NOL4L]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[PIP4K2A]] | +0.57 | +0.62 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QTRT1]] | -0.62 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[BCLAF1]] | -0.60 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[YJU2]] | -0.60 | -0.67 / -0.40 | both halves | 4e-05 |  |
| [[RPRD1B]] | -0.60 | -0.34 / -0.64 | both halves | 1e-04 |  |
| [[NDUFA5]] | -0.60 | -0.69 / -0.48 | both halves | 2e-05 |  |
| [[LUC7L2]] | -0.59 | -0.34 / -0.63 | both halves | 1e-04 |  |
| [[MCCC2]] | -0.58 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[TRMO]] | -0.58 | -0.68 / -0.35 | both halves | 1e-04 |  |
| [[INTS14]] | -0.57 | -0.64 / -0.37 | both halves | 8e-05 |  |
| [[CC2D2A]] | -0.55 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[RBM23]] | -0.55 | -0.67 / -0.27 | both halves | 3e-04 |  |
| [[ATP5PB]] | -0.55 | -0.58 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.402). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-1.2, 3.5); signed map (-23.8, 19.7). **Vector** length 131, 40.3% of its response variance represented; |z| ≥ 3 in 1,426 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.1 | +13.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +10.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.7 | +9.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +7.2 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.8 | +10.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.0 | +5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.0 | +5.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.7 | +4.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -14.7 | -14.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -11.1 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -9.0 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.0 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.0 | -9.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -4.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Arbutin (drug)]] 0.05 µM |  | -2.2 | -3.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | Cbl proto-oncogene |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:119,206,298-119,313,926 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RNF55, c-Cbl; previously CBL2 |
| Gene groups (HGNC) | Ring finger proteins; Cbl proto-oncogene family |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, KRAS_SIGNALING_UP |
| Reactome | 47 pathways, smallest: FLT3 signaling by CBL mutants; PTK6 Regulates RTKs and Their Effectors AKT1 and DOK1; Interleukin-6 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P22681](https://www.uniprot.org/uniprotkb/P22681) (E3 ubiquitin-protein ligase CBL):

> E3 ubiquitin-protein ligase that acts as a negative regulator of many signaling pathways by mediating ubiquitination of cell surface receptors. Accepts ubiquitin from specific E2 ubiquitin-conjugating enzymes, and then transfers it to substrates promoting their degradation by the proteasome. Recognizes activated receptor tyrosine kinases, including KIT, FLT1, FGFR1, FGFR2, PDGFRA, PDGFRB, CSF1R, EPHA8 and KDR and mediates their ubiquitination to terminate signaling. Recognizes membrane-bound …

**Summary**, from NCBI Gene [867](https://www.ncbi.nlm.nih.gov/gene/867):

> This gene is a proto-oncogene that encodes a RING finger E3 ubiquitin ligase. The encoded protein is one of the enzymes required for targeting substrates for degradation by the proteasome. This protein mediates the transfer of ubiquitin from ubiquitin conjugating enzymes (E2) to specific substrates. This protein also contains an N-terminal phosphotyrosine binding domain that allows it to interact with numerous tyrosine-phosphorylated substrates and target them for proteasome degradation. As …

**Accessions** — [HGNC:1541](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1541) · Entrez [867](https://www.ncbi.nlm.nih.gov/gene/867) · UniProt [P22681](https://www.uniprot.org/uniprotkb/P22681) · Ensembl [ENSG00000110395](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110395)

## Data

Gene col 3134: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3134); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3134, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3134]; `tensor/DDL_lfc|DDL_z.npy` [3134]; `embed/gene_vectors.npy` [3134]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3134 or target_col == 3134). Every well: [[CBL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
