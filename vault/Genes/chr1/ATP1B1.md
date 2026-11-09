---
symbol: "ATP1B1"
type: "gene"
col: 6683
ensembl_id: "ENSG00000143153"
name: "ATPase Na+/K+ transporting subunit beta 1"
location: "1q24.2"
module: 8
arm: "+"
pooled_cpm: 312.26
n_lines_expressing: 42
n_dd_up: 21
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 43
direction_downstream: 62
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ATP1B1

*ATPase Na+/K+ transporting subunit beta 1* — 1q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.87× (z +13.8, q 2e-40, up in 28 of 40 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.46× (z +8.4, q 1e-14, up in 33 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.5 µM: 0.692× (z -5.7, q 5e-06, down in 27 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHR]] (+0.61, fdr 1e-05), [[ATP8B1]] (+0.60, fdr 1e-05), [[GATA6]] (+0.59, fdr 1e-05); moves opposite to [[NUDCD3]] (-0.56, fdr 1e-05), [[DNAJA3]] (-0.54, fdr 3e-05), [[PARVB]] (-0.49, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 43 arrows point to it, the strongest [[ELF3]] → it (grade B ⚠); 62 go from it, the strongest it → [[LMNA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6683.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.87×** | +13.8 | 2e-40 | 28/40 (AsPC-1, C32, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +8.4 | 1e-14 | 33/40 (NCI-H460, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.63×** | +7.7 | 3e-12 | 25/41 (J82, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.60×** | +7.3 | 4e-11 | 31/40 (BT-474, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +7.2 | 5e-11 | 24/41 (J82, SNU-423, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.59×** | +7.2 | 5e-11 | 31/40 (BT-474, SHP-77, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +5.9 | 3e-07 | 33/41 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.44×** | +5.6 | 1e-06 | 26/40 (BT-474, SHP-77, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.45×** | +5.3 | 6e-06 | 22/37 (J82, NCI-H460, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.36×** | +4.8 | 7e-05 | 29/40 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.37×** | +4.7 | 1e-04 | 18/37 (SK-MEL-2, J82, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.34×** | +4.6 | 2e-04 | 23/40 (J82, SK-MEL-2, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.36×** | +4.6 | 2e-04 | 18/42 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +4.5 | 3e-04 | 19/40 (J82, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.34×** | +4.3 | 5e-04 | 21/40 (BT-474, Panc 03.27, …) | top dose only | composition shift |
| [[Arbutin (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.005 | 29/40 (A498, BT-474, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.7 | 0.006 | 13/40 (HOP62, J82, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.011 | 20/40 (H4, SW48, …) | two highest doses |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.014 | 19/41 (SW 900, SW1417, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6683.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.692×** | -5.7 | 5e-06 | 27/40 (A549, BT-474, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.702×** | -5.5 | 9e-06 | 33/40 (BT-474, A549, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.743×** | -4.6 | 6e-04 | 27/40 (A549, BT-474, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.745×** | -4.6 | 6e-04 | 25/40 (A549, NCI-H1573, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.780×** | -3.9 | 0.009 | 25/40 (NCI-H1792, KATO III, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.839× | -3.9 | 0.009 | 15/40 (H4, NCI-H1792, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.803×** | -3.3 | 0.074 | 23/41 (HepG2/C3A, SW 900, …) | top dose only |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.745×** | -3.3 | 0.074 | 16/40 (LOX-IMVI, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.822× | -3.1 | 0.14 | 21/40 (A498, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6683. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 622 | 0 | 13 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -15.4) |
| [[LS 180 (line)]] | wt | 1,501 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -19.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -19.3) |
| [[J82 (line)]] | alt | 127 | 11 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +18.7) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +11.9) | — |
| [[BT-474 (line)]] | alt | 465 | 7 (7 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +19.6) ⚠ cell-cycle shift, explains ~45% of this change | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.319× (z -11.7) |
| [[COLO 205 (line)]] | alt | 656 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.257× (z -13.6) ⚠ cell-cycle shift, explains ~94% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 256 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +17.1) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H460 (line)]] | wt | 161 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +12.0) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.89× (z +11.0) | — |
| [[HepG2_C3A (line)]] | wt | 628 | 0 | 5 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.467× (z -10.1) |
| [[A498 (line)]] | wt | 466 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +17.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.75× (z +10.3) | [[Clobetasol propionate (drug)]] 0.5 µM 0.503× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 224 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +25.1) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 757 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -12.4) |
| [[hTERT-HPNE (line)]] | wt | 83.6 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.11× (z +17.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 1,070 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -9.9) |
| [[HOP62 (line)]] | alt | 125 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +17.4) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 578 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -10.1) ⚠ cell-cycle shift, explains ~45% of this change |
| [[KATO III (line)]] | alt | 610 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -9.0) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.380× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 120 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +12.5) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[C32 (line)]] | wt | 144 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.50× (z +23.5) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[LOX-IMVI (line)]] | wt | 165 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +14.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +10.4) | — |
| [[NCI-H1792 (line)]] | alt | 223 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +19.7) ⚠ cell-cycle shift, explains ~45% of this change | [[Budesonide (drug)]] 5 µM 0.389× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 694 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -10.5) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Budesonide (drug)]] 5 µM 0.505× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 519 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +14.9) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[RPMI-7951 (line)]] | alt | 89.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +12.5) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 208 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.42× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[SNU-423 (line)]] | alt | 112 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +15.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +10.8) | — |
| [[AN3 CA (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +11.2) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[CHP-212 (line)]] | wt | 105 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +11.3) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[LoVo (line)]] | wt | 166 | 1 | 0 | [[Cobimetinib (drug)]] 5 µM 3.72× (z +9.8) | — |
| [[SW 1271 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0648× (z -12.5) ⚠ toxic; cell-cycle shift, explains ~15% of this change |
| [[SW1417 (line)]] | alt | 235 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.0) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[SW48 (line)]] | wt | 112 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +10.0) | — |
| [[SW480 (line)]] | alt | 86.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +15.3) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[A-172 (line)]] | wt | 270 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 57.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 57.1 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 99.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 45.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 447 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 357 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 46.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.0 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 37.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 498 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6683), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHR]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ATP8B1]] | +0.60 | +0.50 / +0.64 | both halves | 1e-05 | pathway: Ion channel transport |
| [[GATA6]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[FRMD4B]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[TOB1]] | +0.58 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ELF3]] | +0.58 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[CA8]] | +0.57 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[MAPRE2]] | +0.57 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ARHGAP42]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[RHBDL2]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[ANKRD22]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[TNFRSF21]] | +0.55 | +0.55 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDCD3]] | -0.56 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[DNAJA3]] | -0.54 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[PARVB]] | -0.49 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[MAPKAPK5]] | -0.49 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[DCTD]] | -0.48 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[TRIM27]] | -0.48 | -0.43 / -0.52 | both halves | 4e-05 |  |
| [[ZNF142]] | -0.48 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[HSF1]] | -0.48 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[ADSL]] | -0.47 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[NPRL3]] | -0.46 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[EEFSEC]] | -0.46 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[INO80E]] | -0.46 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 40, C 3. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3]] | B | ELF3 activity raises ATP1B1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 3.74× lower at baseline in the lines without ELF3 | 9e-05 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[FRMD4B]] | B | FRMD4B activity raises ATP1B1's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 3.72× lower at baseline in the lines without FRMD4B | 4e-04 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[HNF1B]] | B | HNF1B activity raises ATP1B1's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 3.73× lower at baseline in the lines without HNF1B | 6e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[TFF1]] | B | TFF1 activity raises ATP1B1's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 3.75× lower at baseline in the lines without TFF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[ADGRF1]] | B | ADGRF1 activity raises ATP1B1's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.51× lower at baseline in the lines without ADGRF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[GBP2]] | B | GBP2 activity raises ATP1B1's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.85× lower at baseline in the lines without GBP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[GATA6]] | B | GATA6 activity raises ATP1B1's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 2.58× lower at baseline in the lines without GATA6 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[MPZL2]] | B | MPZL2 activity raises ATP1B1's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 2.94× lower at baseline in the lines without MPZL2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[RASEF]] | B | RASEF activity raises ATP1B1's level | lines that do not express RASEF (20) vs lines expressing it (30) | 2.70× lower at baseline in the lines without RASEF | 0.008 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[ATP8B1]] | B | ATP8B1 activity raises ATP1B1's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.67× lower at baseline in the lines without ATP8B1 | 0.008 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[MMP13]] | B | MMP13 activity raises ATP1B1's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.33× lower at baseline in the lines without MMP13 | 0.008 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[NEDD9]] | B | NEDD9 activity raises ATP1B1's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 2.65× lower at baseline in the lines without NEDD9 | 0.008 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |

### Downstream of this gene

*62 arrows, 62 of them with an alert ⚠; grade A 0, B 60, C 2. Shown: the 12 strongest; 50 more arrows (50 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMNA]] | B | ATP1B1 activity raises LMNA's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 2.49× lower at baseline in the lines without ATP1B1 | 8e-04 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[RIN2]] | B | ATP1B1 activity raises RIN2's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 3.61× lower at baseline in the lines without ATP1B1 | 0.004 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[ARHGAP26]] | B | ATP1B1 activity raises ARHGAP26's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 2.69× lower at baseline in the lines without ATP1B1 | 0.004 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[SOX9]] | B | ATP1B1 activity raises SOX9's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 3.25× lower at baseline in the lines without ATP1B1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[ARHGAP42]] | B | ATP1B1 activity raises ARHGAP42's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 3.29× lower at baseline in the lines without ATP1B1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[NEDD9]] | B | ATP1B1 activity raises NEDD9's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 4.91× lower at baseline in the lines without ATP1B1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[PRKCA]] | B | ATP1B1 activity raises PRKCA's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 2.44× lower at baseline in the lines without ATP1B1 | 0.008 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[ELF3]] | B | ATP1B1 activity raises ELF3's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 5.06× lower at baseline in the lines without ATP1B1 | 0.008 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[ATP8B1]] | B | ATP1B1 activity raises ATP8B1's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 2.80× lower at baseline in the lines without ATP1B1 | 0.010 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[MCM3AP]] | B | ATP1B1 activity lowers MCM3AP's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 1.33× higher at baseline in the lines without ATP1B1 | 0.010 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[TNFRSF21]] | B | ATP1B1 activity raises TNFRSF21's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 3.35× lower at baseline in the lines without ATP1B1 | 0.014 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[FRK]] | B | ATP1B1 activity raises FRK's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 4.60× lower at baseline in the lines without ATP1B1 | 0.018 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.545). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.8, 57.8); signed map (50.9, 5.5). **Vector** length 137, 43.3% of its response variance represented; |z| ≥ 3 in 1,495 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.6 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.7 | +5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +7.2 | +13.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.1 | +1.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +4.5 | +7.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.3 | +1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.6 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.4 | +1.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.5 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.4 | -3.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -5.2 | -4.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -5.0 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.9 | -1.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.2 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | ATPase Na+/K+ transporting subunit beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.2 — chr1:169,105,697-169,310,992 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ATP1B |
| Gene groups (HGNC) | ATPase Na+/K+ transporting subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 12 pathways, smallest: Basigin interactions; Ion homeostasis; Ion transport by P-type ATPases |
| Matched by | ensembl_id |

**Function**, from UniProt [P05026](https://www.uniprot.org/uniprotkb/P05026) (Sodium/potassium-transporting ATPase subunit beta-1):

> Non-catalytic subunit of the Na(+)/K(+)-ATPase pump that hydrolyzes ATP to exchange ions across the plasma membrane, exporting 3 Na(+) and importing 2 K(+) per cycle against electrochemical gradients. The beta subunit is important for the folding, stability, and targeting of the Na(+)/K(+)-ATPase pump to the plasma membranes (By similarity). In addition, acts as a homotypic cell adhesion molecule in epithelia cells. Interactions between ATP1B1 on neighboring cells are critical for proper …

**Summary**, from NCBI Gene [481](https://www.ncbi.nlm.nih.gov/gene/481):

> The protein encoded by this gene belongs to the family of Na+/K+ and H+/K+ ATPases beta chain proteins, and to the subfamily of Na+/K+ -ATPases. Na+/K+ -ATPase is an integral membrane protein responsible for establishing and maintaining the electrochemical gradients of Na and K ions across the plasma membrane. These gradients are essential for osmoregulation, for sodium-coupled transport of a variety of organic and inorganic molecules, and for electrical excitability of nerve and muscle. This …

**Accessions** — [HGNC:804](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:804) · Entrez [481](https://www.ncbi.nlm.nih.gov/gene/481) · UniProt [P05026](https://www.uniprot.org/uniprotkb/P05026) · Ensembl [ENSG00000143153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143153)

## Data

Gene col 6683: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6683); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6683, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6683]; `tensor/DDL_lfc|DDL_z.npy` [6683]; `embed/gene_vectors.npy` [6683]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6683 or target_col == 6683). Every well: [[ATP1B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP1B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
