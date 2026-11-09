---
symbol: "GATAD2A"
type: "gene"
col: 9472
ensembl_id: "ENSG00000167491"
name: "GATA zinc finger domain containing 2A"
location: "19p13.11"
module: 45
arm: "-"
pooled_cpm: 119.23
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# GATAD2A

*GATA zinc finger domain containing 2A* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.80× (z +11.5, q 5e-28, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.773× (z -5.2, q 1e-04, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTL]] (+0.68, fdr 7e-06), [[KPNA4]] (+0.68, fdr 7e-06), [[ACOT7]] (+0.67, fdr 7e-06); moves opposite to [[SNX2]] (-0.70, fdr 7e-06), [[MBIP]] (-0.68, fdr 7e-06), [[ZNF292]] (-0.67, fdr 1e-05).
> It sits in the **-** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KCNC4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9472.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +11.5 | 5e-28 | 43/48 (NCI-H2347, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.71×** | +10.6 | 1e-23 | 43/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.37×** | +8.8 | 2e-16 | 37/49 (C32, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +8.7 | 4e-16 | 43/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +8.5 | 2e-15 | 40/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.53×** | +8.4 | 5e-15 | 38/48 (SW48, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.48×** | +7.7 | 1e-12 | 41/48 (C32, HCT15, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.46×** | +7.4 | 1e-11 | 40/48 (SNU-1, SW48, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +7.0 | 1e-10 | 43/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.41×** | +6.7 | 9e-10 | 33/48 (NCI-H460, SW480, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +6.6 | 3e-09 | 33/47 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +6.4 | 9e-09 | 33/48 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.36×** | +6.1 | 6e-08 | 35/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +6.0 | 7e-08 | 35/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.29×** | +4.9 | 3e-05 | 29/48 (A549, H4, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +3.9 | 0.003 | 21/48 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.006 | 22/49 (SW480, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.033 | 18/48 (A498, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.061 | 17/48 (A498, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9472.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.773×** | -5.2 | 1e-04 | 34/48 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.621×** | -5.0 | 1e-04 | 32/47 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.774×** | -4.9 | 1e-04 | 30/47 (SW480, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.821×** | -4.0 | 0.011 | 21/48 (RKO, Hs 766T, …) | two highest doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.876× | -3.8 | 0.016 | 14/48 (RKO, AsPC-1, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.877× | -3.7 | 0.017 | 5/48 (NCI-H1792, SW 900, …) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | 0.841× | -3.6 | 0.027 | 25/49 (MIA PaCa-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.838× | -3.6 | 0.027 | 18/48 (KATO III, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.825×** | -3.5 | 0.033 | 21/48 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~4% of this change | 0.850× | -3.3 | 0.058 | 20/48 (H4, SW 1088, …) | inconsistent across doses | low cells (technical?) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.890× | -3.2 | 0.064 | 12/49 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | 0.894× | -3.2 | 0.064 | 15/48 (RKO, SW48, …) | two highest doses | low cells (technical?) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.855× | -3.2 | 0.067 | 17/48 (HOP62, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.857× | -3.1 | 0.074 | 17/48 (KATO III, HOP62, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.755×** | -3.1 | 0.076 | 18/48 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9472. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 84.2 | 12 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.93× (z +17.1) | — |
| [[AsPC-1 (line)]] | alt | 199 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.459× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 70.1 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +19.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.48× (z +15.7) | — |
| [[SW480 (line)]] | alt | 175 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +13.4) | — |
| [[A498 (line)]] | wt | 105 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.38× (z +11.5) | — |
| [[A-172 (line)]] | wt | 109 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.14× (z +9.3) | — |
| [[C32 (line)]] | wt | 69.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +12.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.52× (z +12.2) | — |
| [[CFPAC-1 (line)]] | alt | 82.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.71× (z +11.3) | — |
| [[HepG2_C3A (line)]] | wt | 98.7 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.51× (z +11.7) | — |
| [[NCI-H1573 (line)]] | alt | 49.3 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +9.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 85.4 | 3 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.46× (z +12.9) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 4.34× (z +12.1) | — |
| [[NCI-H2347 (line)]] | alt | 98.2 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.47× (z +12.3) | — |
| [[Panc 03.27 (line)]] | alt | 273 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.02× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.429× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 145 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +9.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.06× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.425× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 63.5 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[H4 (line)]] | wt | 82.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +9.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.39× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 120 | 2 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.50× (z +9.0) ⚠ unreliable plate only | — |
| [[MIA PaCa-2 (line)]] | alt | 186 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.66× (z +11.2) | [[Adagrasib (drug)]] 0.05 µM 0.616× (z -19.1) ⚠ position not correctable |
| [[NCI-H23 (line)]] | alt | 89.1 | 2 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.37× (z +9.0) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 2.33× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 141 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.04× (z +10.0) ⚠ cell-cycle shift, explains ~58% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 160 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +10.8) | — |
| [[SW48 (line)]] | wt | 217 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.50× (z +10.2) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[A-427 (line)]] | wt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.36× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 104 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +11.1) | — |
| [[LOX-IMVI (line)]] | wt | 93.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.03× (z +8.5) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[LS 180 (line)]] | wt | 142 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 72.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[RKO (line)]] | wt | 212 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.558× (z -10.5) ⚠ cell-cycle shift, explains <1% of this change |
| [[SNU-423 (line)]] | alt | 103 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.41× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 83.3 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.42× (z +8.6) ⚠ unreliable plate only | — |
| [[AN3 CA (line)]] | alt | 154 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 144 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 88.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 172 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 115 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 161 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 123 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9472), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*39 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTL]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[KPNA4]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[ACOT7]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[MAPKAPK2]] | +0.63 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[KLF13]] | +0.63 | +0.64 / +0.63 | both halves | 7e-06 | pathway: Differentiation of T cells |
| [[LRP8]] | +0.63 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[HNRNPAB]] | +0.62 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[ACTN1]] | +0.62 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ARPC5L]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[UTP4]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[PLXNA1]] | +0.61 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[NIPA2]] | +0.60 | +0.58 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*61 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX2]] | -0.70 | -0.71 / -0.67 | both halves | 7e-06 |  |
| [[MBIP]] | -0.68 | -0.61 / -0.67 | both halves | 7e-06 | pathway: Chromatin modifying enzymes |
| [[ZNF292]] | -0.67 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[NDUFA5]] | -0.65 | -0.70 / -0.57 | both halves | 1e-05 |  |
| [[THAP8]] | -0.65 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[ANAPC16]] | -0.64 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[ZNF14]] | -0.64 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[FPGT]] | -0.63 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[KBTBD3]] | -0.63 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[DNAJC27]] | -0.63 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[CIR1]] | -0.62 | -0.69 / -0.58 | both halves | 7e-06 |  |
| [[PPIL4]] | -0.62 | -0.62 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNC4]] | B | KCNC4 activity raises GATAD2A's level | lines that do not express KCNC4 (6) vs lines expressing it (44) | 1.24× lower at baseline in the lines without KCNC4 | 0.048 | ⚠ within organs, on part of the lines; also absent: CRTAP, FKBP7, SACS; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **-** arm (projection on the module's main direction -0.526). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (6.1, -24.0); signed map (-11.3, 41.0). **Vector** length 128, 42.9% of its response variance represented; |z| ≥ 3 in 1,368 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.6 | +11.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.0 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.2 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.6 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.5 | +0.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.7 | +2.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.3 | +2.3 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | +3.2 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +1.8 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -5.9 | -5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.2 | -3.8 |
|  | [[NG25 (drug)]] 5 µM |  | -5.0 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -0.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | -5.0 | -3.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.4 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.2 | -3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.0 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | GATA zinc finger domain containing 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:19,385,826-19,508,932 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p66alpha |
| Gene groups (HGNC) | GATA zinc finger domain containing; NuRD complex subunits; MicroRNA protein coding host genes |
| Reactome | 31 pathways, smallest: Transcriptional regulation of brown and beige adipocyte differentiation; Transcriptional regulation of brown and beige adipocyte differentiation by EBF2; ERCC6 (CSB) and EHMT2 (G9a) positively regulate rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YP4](https://www.uniprot.org/uniprotkb/Q86YP4) (Transcriptional repressor p66-alpha):

> Transcriptional repressor. Acts as a component of the histone deacetylase NuRD complex which participates in the remodeling of chromatin. Enhances MBD2-mediated repression. Efficient repression requires the presence of GATAD2B.

**Summary**, from NCBI Gene [54815](https://www.ncbi.nlm.nih.gov/gene/54815):

> Enables protein-macromolecule adaptor activity. Involved in chromatin remodeling and negative regulation of DNA-templated transcription. Located in nucleoplasm. Part of NuRD complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29989) · Entrez [54815](https://www.ncbi.nlm.nih.gov/gene/54815) · UniProt [Q86YP4](https://www.uniprot.org/uniprotkb/Q86YP4) · Ensembl [ENSG00000167491](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167491)

## Data

Gene col 9472: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9472); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9472, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9472]; `tensor/DDL_lfc|DDL_z.npy` [9472]; `embed/gene_vectors.npy` [9472]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9472 or target_col == 9472). Every well: [[GATAD2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GATAD2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
