---
symbol: "ING4"
type: "gene"
col: 3252
ensembl_id: "ENSG00000111653"
name: "inhibitor of growth family member 4"
location: "12p13.31"
module: 41
arm: "+"
pooled_cpm: 18.5
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 27
n_dd_up_clean: 11
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# ING4

*inhibitor of growth family member 4* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.15× (z +7.5, q 5e-11, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.316× (z -21.5, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.469× (z -13.6, q 7e-40, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ISY1]] (+0.71, fdr 7e-06), [[SYF2]] (+0.70, fdr 7e-06), [[ZNF394]] (+0.69, fdr 1e-05); moves opposite to [[IDH3A]] (-0.57, fdr 1e-05), [[CEP83]] (-0.57, fdr 3e-05), [[RBBP8]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3252.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.15×** | +7.5 | 5e-11 | 27/48 (NCI-H23, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.24×** | +5.6 | 5e-06 | 23/48 (NCI-H2030, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +5.6 | 5e-06 | 20/47 (NCI-H2030, A498, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.31×** | +5.1 | 6e-05 | 15/46 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.31×** | +4.7 | 3e-04 | 16/47 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.58×** | +4.5 | 7e-04 | 18/44 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.26×** | +4.3 | 0.001 | 13/46 (A-172, KATO III, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.26×** | +4.3 | 0.001 | 14/47 (H4, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.17× | +4.2 | 0.002 | 10/48 (PANC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.011 | 10/48 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.23×** | +3.7 | 0.011 | 3/47 (A-427, NCI-H2347, …) | inconsistent across doses |  |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.7 | 0.011 | 11/48 (BT-474, A-172, …) | all doses, flat |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.7 | 0.011 | 6/48 (A-427, KATO III, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.011 | 11/48 (J82, KATO III, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.31×** | +3.6 | 0.012 | 9/45 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.017 | 6/47 (HOP62, KATO III, …) | all doses, stronger at high dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.025 | 3/47 (NCI-H1792, SW48, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.028 | 11/47 (Panc 03.27, SW 900, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.030 | 5/48 (H4, HOP62, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.041 | 4/48 (Panc 03.27, HOP62, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3252.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.316×** | -21.5 | 0e+00 | 47/48 (SW480, A549, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.560×** | -15.3 | 0e+00 | 32/47 (COLO 205, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.469×** | -13.6 | 7e-40 | 37/47 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.522×** | -12.1 | 9e-32 | 34/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.577×** | -10.3 | 1e-22 | 33/47 (COLO 205, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.577×** | -10.3 | 1e-22 | 31/46 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.360×** | -10.0 | 2e-21 | 39/46 (A-427, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.610×** | -8.9 | 6e-17 | 29/44 (H4, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.623×** | -8.8 | 6e-17 | 31/48 (NCI-H1792, A-172, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.429×** | -8.3 | 9e-15 | 30/45 (A-427, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.444×** | -7.9 | 1e-13 | 29/47 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.659×** | -7.8 | 3e-13 | 32/47 (LOX-IMVI, SK-MEL-2, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.458×** | -7.6 | 1e-12 | 26/46 (HOP62, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.668×** | -7.5 | 2e-12 | 28/48 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.674×** | -7.0 | 1e-10 | 27/47 (SW 900, A498, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.496×** | -6.8 | 3e-10 | 25/46 (A-427, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.622×** | -6.3 | 8e-09 | 26/48 (Panc 03.27, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.708×** | -4.6 | 1e-04 | 13/48 (A-427, MIA PaCa-2, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.847× | -4.4 | 3e-04 | 15/48 (NCI-H460, A-427, …) | top dose only |  |
| [[Volasertib (drug)]] 0.5 µM |  | **0.730×** | -4.2 | 7e-04 | 11/48 (NCI-H460, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.664×** | -4.0 | 0.002 | 10/48 (AN3 CA, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.756×** | -3.7 | 0.004 | 11/48 (KATO III, SW480, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3252. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 36.5 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.256× (z -11.4) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.358× (z -8.6) |
| [[PANC-1 (line)]] | alt | 14.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -13.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.237× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.220× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 23.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0896× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 19.6 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.169× (z -12.1) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.195× (z -10.8) |
| [[KATO III (line)]] | alt | 26.3 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.179× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[NCI-H1792 (line)]] | alt | 15.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -10.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.217× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 39.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 24.5 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.251× (z -12.9) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -10.8) |
| [[A498 (line)]] | wt | 13.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -10.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[COLO 205 (line)]] | alt | 19.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0723× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[H4 (line)]] | wt | 27.5 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.130× (z -10.1) ⚠ cell-cycle shift, explains ~65% of this change |
| [[HepG2_C3A (line)]] | wt | 11.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0719× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Pimozide (drug)]] 0.05 µM 0.125× (z -8.5) |
| [[HOP62 (line)]] | alt | 21.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.283× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[MIA PaCa-2 (line)]] | alt | 22.9 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.217× (z -10.0) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.228× (z -9.3) |
| [[SW 900 (line)]] | alt | 23.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -11.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.305× (z -8.6) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -11.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HCT15 (line)]] | alt | 24.7 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.128× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.341× (z -8.7) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.211× (z -9.7) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -8.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1573 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0942× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -8.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 1271 (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -8.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[AN3 CA (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3252), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISY1]] | +0.71 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[SYF2]] | +0.70 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[ZNF394]] | +0.69 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[TBC1D15]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[EPM2AIP1]] | +0.67 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[PIN4]] | +0.67 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[EAPP]] | +0.66 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ASB3]] | +0.66 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[ECT2L]] | +0.64 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[HAVCR2]] | +0.64 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[FAM185BP]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[MED6]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDH3A]] | -0.57 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[CEP83]] | -0.57 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[RBBP8]] | -0.55 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[CYC1]] | -0.55 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[THOP1]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.452). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (0.1, -20.6); signed map (-2.9, -3.2). **Vector** length 93.9, 20.6% of its response variance represented; |z| ≥ 3 in 1,078 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.7 | +7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.5 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +5.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +5.1 | +5.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | +3.8 | +3.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.8 | -21.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.1 | -7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -13.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.0 | -10.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.8 | -8.3 |
|  | [[EX229 (drug)]] 5 µM |  | -4.6 | -7.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.6 | -6.8 |

## What is on record

|  |  |
|---|---|
| Name | inhibitor of growth family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,650,301-6,663,142 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p29ING4, my036 |
| Gene groups (HGNC) | PHD finger proteins; Inhibitor of growth family |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNL4](https://www.uniprot.org/uniprotkb/Q9UNL4) (Inhibitor of growth protein 4):

> Component of HBO1 complexes, which specifically mediate acetylation of histone H3 at 'Lys-14' (H3K14ac), and have reduced activity toward histone H4. Through chromatin acetylation it may function in DNA replication. May inhibit tumor progression by modulating the transcriptional output of signaling pathways which regulate cell proliferation. Can suppress brain tumor angiogenesis through transcriptional repression of RELA/NFKB3 target genes when complexed with RELA. May also specifically …

**Summary**, from NCBI Gene [51147](https://www.ncbi.nlm.nih.gov/gene/51147):

> This gene encodes a tumor suppressor protein that contains a PHD-finger, which is a common motif in proteins involved in chromatin remodeling. This protein can bind TP53 and EP300/p300, a component of the histone acetyl transferase complex, suggesting its involvement in the TP53-dependent regulatory pathway. Multiple alternatively spliced transcript variants have been observed that encode distinct proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19423](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19423) · Entrez [51147](https://www.ncbi.nlm.nih.gov/gene/51147) · UniProt [Q9UNL4](https://www.uniprot.org/uniprotkb/Q9UNL4) · Ensembl [ENSG00000111653](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111653)

## Data

Gene col 3252: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3252); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3252, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3252]; `tensor/DDL_lfc|DDL_z.npy` [3252]; `embed/gene_vectors.npy` [3252]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3252 or target_col == 3252). Every well: [[ING4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ING4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
