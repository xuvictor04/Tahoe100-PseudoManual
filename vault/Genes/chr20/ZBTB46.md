---
symbol: "ZBTB46"
type: "gene"
col: 5085
ensembl_id: "ENSG00000130584"
name: "zinc finger and BTB domain containing 46"
location: "20q13.33"
module: 160
arm: "+"
pooled_cpm: 26.94
n_lines_expressing: 46
n_dd_up: 21
n_dd_down: 15
n_dd_up_clean: 19
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# ZBTB46

*zinc finger and BTB domain containing 46* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.46× (z +25.2, q 0e+00, up in 33 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.709× (z -9.6, q 4e-19, down in 29 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OLFM2]] (+0.66, fdr 7e-06), [[GPR153]] (+0.65, fdr 7e-06), [[NOL4L]] (+0.62, fdr 1e-05); moves opposite to [[PTCD3]] (-0.61, fdr 7e-06), [[OSGEPL1]] (-0.55, fdr 2e-05), [[ZZZ3]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ELFN1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PIK3CD]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5085.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.46×** | +25.2 | 0e+00 | 33/43 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.12×** | +14.8 | 0e+00 | 35/44 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.03×** | +13.4 | 9e-39 | 30/44 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +11.6 | 9e-29 | 24/44 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.78×** | +11.4 | 4e-28 | 29/44 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +10.4 | 2e-23 | 29/44 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +8.4 | 3e-15 | 30/44 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +7.8 | 6e-13 | 28/44 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +6.8 | 6e-10 | 23/44 (MIA PaCa-2, SW48, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +5.8 | 4e-07 | 18/44 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +5.5 | 2e-06 | 20/43 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +5.2 | 1e-05 | 17/43 (LoVo, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +5.0 | 2e-05 | 17/44 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.30×** | +5.0 | 2e-05 | 17/43 (SW48, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Rapamycin (drug)]] 5 µM |  | 1.18× | +4.7 | 8e-05 | 9/44 (J82, SHP-77, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5085.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.709×** | -9.6 | 4e-19 | 29/44 (SK-MEL-2, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.664×** | -8.1 | 2e-13 | 21/38 (A-172, Panc 03.27, …) | all doses, flat | composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.450×** | -7.9 | 6e-13 | 26/40 (AsPC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.730×** | -6.2 | 7e-08 | 21/44 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.745×** | -5.6 | 3e-06 | 21/42 (SW1417, A-427, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.739×** | -5.4 | 5e-06 | 21/36 (A549, NCI-H2030, …) | all doses, flat | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.596×** | -5.1 | 3e-05 | 18/42 (AsPC-1, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.623×** | -4.7 | 2e-04 | 16/44 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.783×** | -4.6 | 2e-04 | 18/31 (LoVo, BT-474, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.792×** | -4.4 | 5e-04 | 20/42 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.854× | -4.4 | 5e-04 | 12/44 (J82, MIA PaCa-2, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.815×** | -4.0 | 0.003 | 12/43 (NCI-H2030, SW 900, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.814×** | -3.9 | 0.004 | 19/44 (A-172, SW1417, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.674×** | -3.9 | 0.004 | 15/44 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Clotrimazole (drug)]] 5 µM |  | 0.873× | -3.8 | 0.006 | 10/44 (A498, A-172, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.709×** | -3.4 | 0.025 | 15/42 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Silodosin (drug)]] 5 µM |  | 0.841× | -3.3 | 0.033 | 7/42 (HEC-1-A, NCI-H2030, …) | top dose only |  |
| [[venetoclax (drug)]] 0.05 µM |  | 0.835× | -3.3 | 0.033 | 9/44 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.851× | -3.0 | 0.090 | 5/44 (J82, COLO 205, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.804×** | -2.9 | 0.094 | 4/44 (MIA PaCa-2, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | 0.863× | -2.9 | 0.100 | 13/44 (A498, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5085. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.19 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +15.4) | — |
| [[SW1417 (line)]] | alt | 64.3 | 1 | 5 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.91× (z +11.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.263× (z -13.8) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -12.1) |
| [[A549 (line)]] | wt | 20.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 34.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[HT-29 (line)]] | alt | 37.2 | 1 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.90× (z +11.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.171× (z -13.9) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 28.7 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 38.5 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +20.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.471× (z -8.8) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 59.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A498 (line)]] | wt | 23.0 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HepG2_C3A (line)]] | wt | 33.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.40× (z +16.4) | — |
| [[Hs 766T (line)]] | wt | 19.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +13.2) | — |
| [[AsPC-1 (line)]] | alt | 42.0 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.291× (z -9.8) |
| [[HOP62 (line)]] | alt | 39.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +12.9) | [[Adagrasib (drug)]] 0.05 µM 0.600× (z -13.9) ⚠ position not correctable |
| [[HS-578T (line)]] | alt | 29.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[LoVo (line)]] | wt | 23.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[MIA PaCa-2 (line)]] | alt | 30.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.356× (z -8.7) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 46.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RPMI-7951 (line)]] | alt | 22.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +11.8) | [[Selinexor (drug)]] 5 µM 0.150× (z -13.0) |
| [[SNU-423 (line)]] | alt | 9.90 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +16.1) | — |
| [[SW480 (line)]] | alt | 61.7 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.15× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Selinexor (drug)]] 5 µM 0.574× (z -8.8) |
| [[A-427 (line)]] | wt | 38.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -9.8) |
| [[C-33 A (line)]] | alt | 54.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[CFPAC-1 (line)]] | alt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +17.8) | — |
| [[HEC-1-A (line)]] | alt | 12.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 13.6× (z +17.6) | — |
| [[J82 (line)]] | alt | 12.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +14.3) | — |
| [[NCI-H23 (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H2347 (line)]] | alt | 20.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +12.9) | — |
| [[SW 900 (line)]] | alt | 20.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +15.3) | — |
| [[AN3 CA (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.02 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.14 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5085), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OLFM2]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[GPR153]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[NOL4L]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[OSBP2]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[CLIP2]] | +0.61 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[STK10]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[NFATC1]] | +0.57 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[WNT9A]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ABR]] | +0.55 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[SMURF1]] | +0.55 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[CBFA2T3]] | +0.55 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ZBTB7A]] | +0.54 | +0.55 / +0.49 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTCD3]] | -0.61 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[OSGEPL1]] | -0.55 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ZZZ3]] | -0.52 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[IARS2]] | -0.51 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ARMC1]] | -0.51 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[MTREX]] | -0.49 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ELP3]] | -0.48 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[PMS2]] | -0.48 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[WBP11]] | -0.48 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[EIF2B1]] | -0.47 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[ERLIN1]] | -0.47 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[C5orf15]] | -0.46 | -0.47 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELFN1]] | B | ELFN1 activity raises ZBTB46's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.57× lower at baseline in the lines without ELFN1 | 0.023 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[PDGFA]] | B | PDGFA activity raises ZBTB46's level | lines that do not express PDGFA (9) vs lines expressing it (41) | 1.68× lower at baseline in the lines without PDGFA | 0.050 | ⚠ within organs, on part of the lines; also absent: HCN2; maybe low, not absent |
| [[PIK3CD]] | B | PIK3CD activity raises ZBTB46's level | lines that do not express PIK3CD (8) vs lines expressing it (42) | 2.10× lower at baseline in the lines without PIK3CD | 0.055 | ⚠ within organs, on part of the lines; also absent: WNT3, CCDC3, CSRP2; maybe low, not absent |
| [[ELFN1]] | B | ELFN1 activity weakens ZBTB46's drug response | lines that do not express ELFN1 (21) vs lines expressing it (23) | the lines without ELFN1 respond 1.45× as strongly (z diff -0.90); strongest at Panobinostat 0.5 µM: 2.10x vs 1.44x (z diff -2.5) | 0.076 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547; target measured in part of the lines; artifact flags |
| [[CBFA2T3]] | B | CBFA2T3 activity raises ZBTB46's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 1.73× lower at baseline in the lines without CBFA2T3 | 0.089 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[RHBDL3]] | B | RHBDL3 activity raises ZBTB46's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 1.92× lower at baseline in the lines without RHBDL3 | 0.089 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIK3CD]] | C | ZBTB46 activity raises PIK3CD's level | lines that do not express ZBTB46 (4) vs lines expressing it (46) | 3.36× lower at baseline in the lines without ZBTB46 | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WNT3, ENSG00000250264; maybe low, not absent |

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **+** arm (projection on the module's main direction 0.590). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (2.5, 31.1); signed map (-0.1, 34.2). **Vector** length 111, 28.4% of its response variance represented; |z| ≥ 3 in 1,165 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.1 | +14.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +25.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +5.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.5 | +5.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.2 | +4.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.1 | +3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +3.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.4 | -9.6 |
|  | [[NG25 (drug)]] 5 µM |  | -4.7 | -7.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -6.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.4 | -5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -4.2 | -3.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.4 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.2 | -4.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -2.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 46 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,743,668-63,832,038 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13502, RINZF, BZEL; previously ZNF340, BTBD4 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UZ6](https://www.uniprot.org/uniprotkb/Q86UZ6) (Zinc finger and BTB domain-containing protein 46):

> Transcription regulator that mediates differentiation of conventional and non-conventional dendritic cells, and which is involved in tolerance to gut microbiota. Together with RORgammaT (RORC), specifically expressed in type 3 innate lymphoid cells (ILC3s) that are required for tolerance to gut microbiota, to mediate differentiation of peripherally-induced regulatory T-cells (pTreg), which suppress inflammatory responses to commensal microorganisms. Functions as a transcription corepressor for …

**Summary**, from NCBI Gene [140685](https://www.ncbi.nlm.nih.gov/gene/140685):

> Predicted to enable DNA-binding transcription repressor activity, RNA polymerase II-specific; RNA polymerase II transcription regulatory region sequence-specific DNA binding activity; and transcription coregulator activity. Involved in regulation of transcription by RNA polymerase II. Predicted to be located in chromatin. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16094](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16094) · Entrez [140685](https://www.ncbi.nlm.nih.gov/gene/140685) · UniProt [Q86UZ6](https://www.uniprot.org/uniprotkb/Q86UZ6) · Ensembl [ENSG00000130584](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130584)

## Data

Gene col 5085: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5085); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5085, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5085]; `tensor/DDL_lfc|DDL_z.npy` [5085]; `embed/gene_vectors.npy` [5085]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5085 or target_col == 5085). Every well: [[ZBTB46 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB46.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
