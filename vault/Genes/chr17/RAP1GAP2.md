---
symbol: "RAP1GAP2"
type: "gene"
col: 5306
ensembl_id: "ENSG00000132359"
name: "RAP1 GTPase activating protein 2"
location: "17p13.3"
module: 34
arm: "+"
pooled_cpm: 56.07
n_lines_expressing: 46
n_dd_up: 15
n_dd_down: 23
n_dd_up_clean: 10
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# RAP1GAP2

*RAP1 GTPase activating protein 2* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.87× (z +12.5, q 3e-33, up in 25 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.50× (z +12.0, q 5e-31, up in 31 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.560× (z -17.1, q 0e+00, down in 28 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACOT7]] (+0.66, fdr 7e-06), [[SCEL]] (+0.58, fdr 3e-05), [[EMP1]] (+0.57, fdr 1e-05); moves opposite to [[SYNRG]] (-0.51, fdr 2e-05), [[LRRC27]] (-0.51, fdr 2e-05), [[EMC2]] (-0.50, fdr 5e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[EMP1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GFOD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5306.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +12.5 | 3e-33 | 25/37 (SW 900, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +12.0 | 5e-31 | 27/38 (SW 900, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +12.0 | 5e-31 | 31/44 (SW480, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +10.9 | 1e-25 | 23/41 (SW 900, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +8.2 | 3e-14 | 26/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.40×** | +6.8 | 1e-09 | 25/43 (COLO 205, A-172, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.36×** | +6.5 | 9e-09 | 22/44 (NCI-H460, A-172, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +6.2 | 3e-08 | 19/45 (C32, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.31×** | +5.7 | 9e-07 | 21/43 (NCI-H460, C32, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.31×** | +5.6 | 1e-06 | 22/43 (LS 180, SW48, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.30×** | +5.3 | 6e-06 | 19/43 (SW48, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[vincristine (drug)]] 5 µM |  | **1.50×** | +4.4 | 4e-04 | 15/41 (NCI-H460, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.23×** | +4.3 | 9e-04 | 17/43 (LS 180, C32, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.30×** | +3.9 | 0.005 | 13/43 (C32, NCI-H460, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.006 | 7/41 (SW480, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.19× | +3.7 | 0.008 | 16/43 (C32, LS 180, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.19× | +3.5 | 0.017 | 9/43 (A-427, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.025 | 12/43 (HS-578T, PANC-1, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.17× | +3.2 | 0.040 | 12/44 (AsPC-1, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5306.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.560×** | -17.1 | 0e+00 | 28/43 (A549, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.518×** | -13.8 | 1e-40 | 27/42 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.581×** | -11.4 | 1e-27 | 30/44 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.599×** | -10.3 | 8e-23 | 27/43 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.663×** | -8.3 | 2e-14 | 25/45 (KATO III, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.677×** | -7.9 | 4e-13 | 28/42 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.720×** | -6.9 | 5e-10 | 26/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.796×** | -6.8 | 1e-09 | 20/44 (A-172, Hs 766T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.747×** | -6.1 | 6e-08 | 21/43 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.757×** | -5.8 | 3e-07 | 20/45 (A-172, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.758×** | -5.8 | 3e-07 | 21/44 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.825×** | -5.7 | 6e-07 | 21/44 (AsPC-1, HepG2/C3A, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.639×** | -4.9 | 4e-05 | 14/43 (LoVo, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.643×** | -4.8 | 5e-05 | 19/43 (Hs 766T, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.797×** | -4.8 | 7e-05 | 21/41 (NCI-H2030, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.800×** | -4.7 | 1e-04 | 18/43 (A549, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.691×** | -4.0 | 0.002 | 15/42 (HCT15, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.832×** | -3.9 | 0.004 | 16/44 (CFPAC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.835× | -3.8 | 0.004 | 13/44 (SW 1088, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5306. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 49.1 | 3 | 4 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.04× (z +11.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.235× (z -15.9) |
| [[PANC-1 (line)]] | alt | 45.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -18.7) |
| [[A549 (line)]] | wt | 110 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0806× (z -25.9) |
| [[A-172 (line)]] | wt | 44.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -14.3) |
| [[AsPC-1 (line)]] | alt | 148 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -15.0) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.470× (z -12.8) |
| [[Hs 766T (line)]] | wt | 29.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -11.6) |
| [[J82 (line)]] | alt | 39.7 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.337× (z -10.1) |
| [[KATO III (line)]] | alt | 162 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -17.0) |
| [[LoVo (line)]] | wt | 114 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -13.9) |
| [[NCI-H23 (line)]] | alt | 73.4 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.149× (z -17.5) ⚠ toxic; cell-cycle shift, explains ~80% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.325× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 41.7 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.49× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -11.4) |
| [[A-427 (line)]] | wt | 75.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -15.5) |
| [[C32 (line)]] | wt | 17.3 | 3 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.46× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 86.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -14.1) |
| [[HepG2_C3A (line)]] | wt | 181 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -12.5) ⚠ cell-cycle shift, explains ~6% of this change |
| [[NCI-H2030 (line)]] | alt | 188 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -20.5) |
| [[Panc 03.27 (line)]] | alt | 60.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.85× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -12.8) |
| [[RKO (line)]] | wt | 35.8 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.197× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~11% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.362× (z -10.7) |
| [[SW 900 (line)]] | alt | 26.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.8× (z +14.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 78.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -12.3) |
| [[LS 180 (line)]] | wt | 74.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -15.6) |
| [[MIA PaCa-2 (line)]] | alt | 53.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -11.7) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.321× (z -9.5) |
| [[SW1417 (line)]] | alt | 59.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -10.4) |
| [[BT-474 (line)]] | alt | 48.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -14.3) |
| [[HCT15 (line)]] | alt | 42.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 16.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 23.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.62× (z +9.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 18.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.31× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 158 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -13.7) |
| [[A498 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.0 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.1 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5306), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACOT7]] | +0.66 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[SCEL]] | +0.58 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[EMP1]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ASAP2]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[MAOB]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[CLTB]] | +0.55 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[ITGA6]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[TLN2]] | +0.55 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[DIAPH1]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[MPRIP]] | +0.55 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ANO1]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[ABLIM2]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNRG]] | -0.51 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[LRRC27]] | -0.51 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[EMC2]] | -0.50 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[TTC9C]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[TENT5A]] | -0.49 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[GALK2]] | -0.48 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[PHC3]] | -0.47 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[CEP57]] | -0.47 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[CNPY2]] | -0.47 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[SPATA7]] | -0.46 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[COQ9]] | -0.46 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[MITD1]] | -0.46 | -0.38 / -0.45 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EMP1]] | B | EMP1 activity lowers RAP1GAP2's level | lines that do not express EMP1 (10) vs lines expressing it (40) | 2.01× higher at baseline in the lines without EMP1 | 0.028 | ⚠ within organs, on part of the lines |
| [[CRYBG2]] | B | CRYBG2 activity raises RAP1GAP2's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 2.34× lower at baseline in the lines without CRYBG2 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[BTNL9]] | B | BTNL9 activity raises RAP1GAP2's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 2.11× lower at baseline in the lines without BTNL9 | 0.046 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |
| [[UNC5A]] | B | UNC5A activity raises RAP1GAP2's level | lines that do not express UNC5A (21) vs lines expressing it (29) | 1.86× lower at baseline in the lines without UNC5A | 0.056 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, KCNK5, CGN |
| [[BCL2L1]] | B | BCL2L1 activity strengthens RAP1GAP2's drug response | lines that do not express BCL2L1 (5) vs lines expressing it (40) | the lines without BCL2L1 respond 0.56× as strongly (z diff +1.25); strongest at Homoharringtonine 5 µM: 1.20x vs 0.51x (z diff +7.2) | 0.070 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ABLIM2]] | B | ABLIM2 activity raises RAP1GAP2's level | lines that do not express ABLIM2 (13) vs lines expressing it (37) | 2.09× lower at baseline in the lines without ABLIM2 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CAMSAP3, SLC9A2, MNX1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GFOD1]] | C | RAP1GAP2 activity raises GFOD1's level | lines that do not express RAP1GAP2 (4) vs lines expressing it (46) | 2.54× lower at baseline in the lines without RAP1GAP2 | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LRIF1, IFI30; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.471). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.8, 51.1); signed map (2.8, 36.5). **Vector** length 110, 27.7% of its response variance represented; |z| ≥ 3 in 1,397 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.1 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +11.1 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.9 | +12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +9.3 | +12.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.5 | +8.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.1 | +6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.9 | +6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.3 | +3.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.3 | +4.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.1 | -10.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.9 | -11.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.8 | -6.8 |
|  | [[NG25 (drug)]] 5 µM |  | -3.6 | -4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | -4.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.2 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -3.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.5 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | RAP1 GTPase activating protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:2,755,705-3,037,741 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1039; previously GARNL4 |
| Reactome | 2 pathways, smallest: Rap1 signalling; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q684P5](https://www.uniprot.org/uniprotkb/Q684P5) (Rap1 GTPase-activating protein 2):

> GTPase activator for the nuclear Ras-related regulatory protein RAP-1A (KREV-1), converting it to the putatively inactive GDP-bound state.

**Summary**, from NCBI Gene [23108](https://www.ncbi.nlm.nih.gov/gene/23108):

> This gene encodes a GTPase-activating protein that activates the small guanine-nucleotide-binding protein Rap1 in platelets. The protein interacts with synaptotagmin-like protein 1 and Rab27 and regulates secretion of dense granules from platelets at sites of endothelial damage. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:29176](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29176) · Entrez [23108](https://www.ncbi.nlm.nih.gov/gene/23108) · UniProt [Q684P5](https://www.uniprot.org/uniprotkb/Q684P5) · Ensembl [ENSG00000132359](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132359)

## Data

Gene col 5306: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5306); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5306, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5306]; `tensor/DDL_lfc|DDL_z.npy` [5306]; `embed/gene_vectors.npy` [5306]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5306 or target_col == 5306). Every well: [[RAP1GAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAP1GAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
