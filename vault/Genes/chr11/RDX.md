---
symbol: "RDX"
type: "gene"
col: 6052
ensembl_id: "ENSG00000137710"
name: "radixin"
location: "11q22.3"
module: 104
arm: "+"
pooled_cpm: 177.28
n_lines_expressing: 46
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# RDX

*radixin* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.76× (z +17.2, q 0e+00, up in 40 of 44 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.73× (z +11.7, q 1e-29, up in 39 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.645× (z -9.4, q 3e-18, down in 40 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF115]] (+0.67, fdr 1e-05), [[UBXN2A]] (+0.64, fdr 3e-05), [[HNRNPH3]] (+0.61, fdr 2e-05); moves opposite to [[AMPD2]] (-0.61, fdr 1e-05), [[UBA6]] (-0.60, fdr 3e-05), [[SMG1P2]] (-0.56, fdr 5e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 2 go from it, the strongest it → [[DECR1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6052.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.76×** | +17.2 | 0e+00 | 40/44 (HOP62, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +14.2 | 2e-43 | 43/45 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +11.7 | 1e-29 | 39/44 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +11.4 | 4e-28 | 38/42 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +11.4 | 8e-28 | 39/44 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +11.0 | 6e-26 | 40/44 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.67×** | +10.6 | 3e-24 | 41/44 (SK-MEL-2, RPMI-7951, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +9.8 | 7e-21 | 32/42 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +7.7 | 1e-12 | 36/44 (NCI-H1792, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +7.0 | 2e-10 | 32/43 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +6.6 | 2e-09 | 32/44 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.32×** | +6.0 | 1e-07 | 34/44 (NCI-H1792, BT-474, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.002 | 21/45 (Hs 766T, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | 1.20× | +3.8 | 0.005 | 21/44 (CFPAC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.6 | 0.013 | 17/44 (BT-474, CFPAC-1, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | 1.18× | +3.5 | 0.018 | 17/44 (Panc 03.27, Hs 766T, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.16× | +3.0 | 0.067 | 17/44 (SK-MEL-2, C32, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.10× | +2.9 | 0.087 | 10/44 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.24×** | +2.9 | 0.087 | 11/44 (HEC-1-A, SW 900, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6052.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.645×** | -9.4 | 3e-18 | 40/44 (LOX-IMVI, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.673×** | -8.5 | 6e-15 | 38/44 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.794×** | -4.9 | 2e-04 | 26/44 (LOX-IMVI, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6052. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 186 | 8 (6 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +16.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.07× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.557× (z -8.8) |
| [[PANC-1 (line)]] | alt | 330 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +14.1) | — |
| [[SNU-423 (line)]] | alt | 229 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +20.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +10.4) | — |
| [[SW480 (line)]] | alt | 165 | 6 (4 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +13.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.548× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 224 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +16.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.15× (z +11.0) | — |
| [[LOX-IMVI (line)]] | wt | 253 | 4 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +20.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.80× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.466× (z -11.9) |
| [[H4 (line)]] | wt | 175 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +14.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.32× (z +8.8) | — |
| [[LoVo (line)]] | wt | 123 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +14.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 123 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 202 | 5 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.60× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +11.7) | — |
| [[A-172 (line)]] | wt | 153 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +18.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.27× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.488× (z -9.4) |
| [[A-427 (line)]] | wt | 171 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.18× (z +10.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.522× (z -9.1) |
| [[A498 (line)]] | wt | 203 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +14.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.551× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 90.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +17.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.49× (z +10.6) | — |
| [[C32 (line)]] | wt | 140 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +17.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.76× (z +14.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 185 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +14.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 241 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Phenylephrine (hydrochloride) (drug)]] 5 µM 1.96× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 176 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +14.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +10.6) | — |
| [[A549 (line)]] | wt | 220 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +16.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.451× (z -9.7) |
| [[BT-474 (line)]] | alt | 56.5 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +10.3) | — |
| [[HEC-1-A (line)]] | alt | 264 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +13.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.628× (z -8.6) |
| [[HOP62 (line)]] | alt | 116 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +21.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 170 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +9.9) | — |
| [[J82 (line)]] | alt | 161 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +16.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H23 (line)]] | alt | 161 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +12.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 218 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +10.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.77× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 248 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +17.9) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW1417 (line)]] | alt | 185 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +13.4) | — |
| [[AN3 CA (line)]] | alt | 265 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.163× (z -10.0) |
| [[Hs 766T (line)]] | wt | 122 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.0) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2030 (line)]] | alt | 262 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.91× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 197 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.98× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 241 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.494× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 163 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.78× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 190 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW 1088 (line)]] | alt | 176 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.187× (z -8.8) |
| [[SW48 (line)]] | wt | 73.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 290 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.7 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 17.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 440 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 550 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6052), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF115]] | +0.67 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[UBXN2A]] | +0.64 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[HNRNPH3]] | +0.61 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[VAPA]] | +0.60 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[RHOBTB3]] | +0.58 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[SAMSN1]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[HACD1]] | +0.58 | +0.55 / +0.32 | both halves | 2e-04 |  |
| [[KLHL5]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[NFYB]] | +0.57 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[LSM14A]] | +0.57 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[SREK1]] | +0.57 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[MT1M]] | +0.56 | +0.64 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AMPD2]] | -0.61 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[UBA6]] | -0.60 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[SMG1P2]] | -0.56 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[PLAUR]] | -0.56 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[EIF4EBP1]] | -0.56 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[MYO9B]] | -0.55 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[DHDDS]] | -0.55 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[MTMR14]] | -0.55 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[TBC1D22A]] | -0.54 | -0.57 / -0.40 | both halves | 4e-05 |  |
| [[PDCD6]] | -0.54 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[ATAT1]] | -0.54 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[GNAI3]] | -0.54 | -0.58 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises RDX's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[KLHL5]] | B | KLHL5 activity raises RDX's level | lines that do not express KLHL5 (7) vs lines expressing it (43) | 3.25× lower at baseline in the lines without KLHL5 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2 |
| [[ENAH]] | C | ENAH activity raises RDX's level | lines that do not express ENAH (3) vs lines expressing it (47) | 4.04× lower at baseline in the lines without ENAH | 0.052 | ⚠ few lines (3 vs 47); across organs; also absent: SSBP2, DIP2C, SOX12; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DECR1]] | C | RDX activity lowers DECR1's level | lines that do not express RDX (4) vs lines expressing it (46) | 1.99× higher at baseline in the lines without RDX | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: FSD1L, SOGA1, CITED2; its own permutation p |
| [[ZFR]] | C | RDX activity raises ZFR's level | lines that do not express RDX (4) vs lines expressing it (46) | 1.42× lower at baseline in the lines without RDX | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: FSD1L, SOGA1, CITED2 |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.394). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.6, 10.8); signed map (22.8, -20.6). **Vector** length 123, 41.2% of its response variance represented; |z| ≥ 3 in 1,173 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +8.2 | +17.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.7 | +11.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.2 | +3.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.5 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.7 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.4 | +1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.4 | +1.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -7.0 | -8.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.8 | -9.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.8 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -0.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | +1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | +1.0 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -2.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | radixin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:109,864,295-110,296,712 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DFNB24 |
| Gene groups (HGNC) | FERM domain containing |
| Reactome | 8 pathways, smallest: Recycling pathway of L1; Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea |
| Matched by | ensembl_id |

**Function**, from UniProt [P35241](https://www.uniprot.org/uniprotkb/P35241) (Radixin):

> Probably plays a crucial role in the binding of the barbed end of actin filaments to the plasma membrane.

**Summary**, from NCBI Gene [5962](https://www.ncbi.nlm.nih.gov/gene/5962):

> Radixin is a cytoskeletal protein that may be important in linking actin to the plasma membrane. It is highly similar in sequence to both ezrin and moesin. The radixin gene has been localized by fluorescence in situ hybridization to 11q23. A truncated version representing a pseudogene (RDXP2) was assigned to Xp21.3. Another pseudogene that seemed to lack introns (RDXP1) was mapped to 11p by Southern and PCR analyses. Multiple alternatively spliced transcript variants encoding different isoforms …

**Accessions** — [HGNC:9944](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9944) · Entrez [5962](https://www.ncbi.nlm.nih.gov/gene/5962) · UniProt [P35241](https://www.uniprot.org/uniprotkb/P35241) · Ensembl [ENSG00000137710](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137710)

## Data

Gene col 6052: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6052); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6052, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6052]; `tensor/DDL_lfc|DDL_z.npy` [6052]; `embed/gene_vectors.npy` [6052]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6052 or target_col == 6052). Every well: [[RDX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RDX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
