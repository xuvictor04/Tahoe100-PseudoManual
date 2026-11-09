---
symbol: "ADARB1"
type: "gene"
col: 12391
ensembl_id: "ENSG00000197381"
name: "adenosine deaminase RNA specific B1"
location: "21q22.3"
module: 135
arm: "-"
pooled_cpm: 119.25
n_lines_expressing: 46
n_dd_up: 10
n_dd_down: 18
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# ADARB1

*adenosine deaminase RNA specific B1* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.62× (z +15.6, q 0e+00, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.450× (z -12.9, q 1e-35, down in 39 of 44 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPHP4]] (+0.56, fdr 8e-05), [[SKI]] (+0.56, fdr 4e-05), [[ZFYVE28]] (+0.55, fdr 3e-05); moves opposite to [[CCNT2]] (-0.61, fdr 3e-05), [[RRAGB]] (-0.57, fdr 5e-05), [[AHI1-DT]] (-0.57, fdr 3e-05).
> It sits in the **-** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[SMYD3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12391.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.62×** | +15.6 | 0e+00 | 40/44 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.19×** | +12.8 | 7e-35 | 37/44 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.95×** | +10.9 | 2e-25 | 38/44 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +6.8 | 1e-09 | 24/44 (SW1417, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +5.8 | 6e-07 | 26/44 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +5.3 | 1e-05 | 24/44 (HepG2/C3A, HEC-1-A, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.86×** | +5.3 | 1e-05 | 29/44 (Hs 766T, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +5.2 | 2e-05 | 27/45 (BT-474, HT-29, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +4.7 | 2e-04 | 22/45 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.30×** | +4.1 | 0.003 | 21/44 (A498, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12391.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.450×** | -12.9 | 1e-35 | 39/44 (HT-29, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.472×** | -11.3 | 6e-27 | 36/42 (SNU-1, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.489×** | -11.2 | 1e-26 | 27/40 (LoVo, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.420×** | -7.4 | 3e-11 | 33/45 (HT-29, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.628×** | -7.2 | 5e-11 | 32/43 (J82, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.740×** | -6.9 | 5e-10 | 31/44 (J82, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.665×** | -6.6 | 4e-09 | 31/44 (RKO, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.718×** | -5.4 | 6e-06 | 29/43 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.569×** | -4.8 | 1e-04 | 25/40 (A-427, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.589×** | -4.5 | 4e-04 | 19/34 (A549, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.775×** | -4.1 | 0.002 | 22/44 (A498, HS-578T, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.790×** | -3.8 | 0.007 | 25/44 (BT-474, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.793×** | -3.7 | 0.008 | 23/44 (PANC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.645×** | -3.7 | 0.008 | 21/43 (LS 180, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.791×** | -3.6 | 0.010 | 22/43 (J82, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.802×** | -3.6 | 0.014 | 19/44 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.860× | -3.4 | 0.020 | 13/44 (BT-474, A-172, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.815×** | -3.2 | 0.049 | 17/44 (NCI-H2030, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.733×** | -3.0 | 0.069 | 14/44 (HEC-1-A, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12391. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 500 | 0 | 14 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -21.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.262× (z -19.4) |
| [[HT-29 (line)]] | alt | 324 | 4 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.90× (z +10.1) | [[Auranofin (drug)]] 5 µM 0.108× (z -16.8) |
| [[A498 (line)]] | wt | 49.3 | 6 (3 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.84× (z +18.4) | [[Auranofin (drug)]] 5 µM 0.356× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 354 | 0 | 9 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 313 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.244× (z -12.6) |
| [[SW480 (line)]] | alt | 139 | 3 (2 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +19.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.44× (z +12.0) | [[Auranofin (drug)]] 5 µM 0.305× (z -16.1) |
| [[LoVo (line)]] | wt | 103 | 4 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +16.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.47× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.260× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.344× (z -12.2) |
| [[LS 180 (line)]] | wt | 111 | 4 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 2.66× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.369× (z -8.7) |
| [[BT-474 (line)]] | alt | 283 | 1 | 4 (3 ⚠) | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 3.00× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.169× (z -14.2) |
| [[HepG2_C3A (line)]] | wt | 159 | 2 (1 ⚠) | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.18× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.288× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 68.3 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.03× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.263× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.387× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 225 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.262× (z -12.8) |
| [[RKO (line)]] | wt | 125 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.00× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0948× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.163× (z -8.5) |
| [[C-33 A (line)]] | alt | 145 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.241× (z -13.3) |
| [[Hs 766T (line)]] | wt | 70.1 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.64× (z +12.1) | — |
| [[KATO III (line)]] | alt | 72.6 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.86× (z +14.7) | [[Auranofin (drug)]] 5 µM 0.397× (z -8.6) |
| [[SW1417 (line)]] | alt | 47.6 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.08× (z +10.1) | — |
| [[A-172 (line)]] | wt | 174 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.88× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -10.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 81.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -12.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 43.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.10× (z +11.9) | — |
| [[CHP-212 (line)]] | wt | 321 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -11.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 120 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 34.5 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.35× (z +10.7) | — |
| [[CFPAC-1 (line)]] | alt | 34.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.16× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 49.4 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.72× (z +8.6) | [[Harringtonine (drug)]] 0.5 µM 0.356× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 56.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 84.2 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.62× (z +10.8) | [[Auranofin (drug)]] 5 µM 0.313× (z -13.1) |
| [[SNU-1 (line)]] | wt | 119 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0937× (z -18.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 36.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +10.0) | — |
| [[C32 (line)]] | wt | 42.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0806× (z -18.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 133 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 41.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.05× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 45.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.61× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 33.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.67× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 132 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.289× (z -9.6) |
| [[SW 900 (line)]] | alt | 72.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.258× (z -11.6) |
| [[SW48 (line)]] | wt | 137 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.8 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 25.7 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 190 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.4 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12391), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHP4]] | +0.56 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[SKI]] | +0.56 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[ZFYVE28]] | +0.55 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[AGAP1]] | +0.54 | +0.46 / +0.35 | both halves | 1e-04 |  |
| [[TXNDC17]] | +0.54 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[CD320]] | +0.54 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[KIAA1958]] | +0.53 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[DOCK5]] | +0.53 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[ERRFI1]] | +0.52 | +0.50 / +0.33 | both halves | 1e-04 |  |
| [[FLNB]] | +0.52 | +0.39 / +0.31 | both halves | 2e-04 |  |
| [[ODF2]] | +0.51 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[SMYD3]] | +0.51 | +0.38 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNT2]] | -0.61 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[RRAGB]] | -0.57 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[AHI1-DT]] | -0.57 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ATP6V1H]] | -0.57 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[GPRASP3]] | -0.56 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[C3orf38]] | -0.56 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[HEXA]] | -0.55 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[PLEKHF2]] | -0.55 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[MR1]] | -0.54 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[FMO4]] | -0.53 | -0.37 / -0.48 | both halves | 9e-05 |  |
| [[CLIC2]] | -0.53 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[RAB21]] | -0.53 | -0.44 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMYD3]] | C | ADARB1 activity raises SMYD3's level | lines that do not express ADARB1 (4) vs lines expressing it (46) | 1.88× lower at baseline in the lines without ADARB1 | 0.006 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC16A1-AS1; maybe low, not absent |
| [[AGAP1]] | C | ADARB1 activity strengthens AGAP1's drug response | lines that do not express ADARB1 (4) vs lines expressing it (45) | the lines without ADARB1 respond 0.80× as strongly (z diff +2.06); strongest at Homoharringtonine 5 µM: 0.56x vs 0.28x (z diff +6.6) | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC16A1-AS1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CD320]] | C | ADARB1 activity raises CD320's level | lines that do not express ADARB1 (4) vs lines expressing it (46) | 2.22× lower at baseline in the lines without ADARB1 | 0.072 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC16A1-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **-** arm (projection on the module's main direction -0.475). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-1.7, 17.2); signed map (-20.6, 42.2). **Vector** length 99.7, 25.3% of its response variance represented; |z| ≥ 3 in 1,276 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.8 | +15.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +12.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.8 | +10.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.4 | +5.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +2.8 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +0.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +5.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +0.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.8 | -6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.0 | -12.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.7 | -7.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.5 | -7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.1 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | +0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | adenosine deaminase RNA specific B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:45,073,853-45,226,560 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ADAR2, DRADA2, ADAR2g, DRABA2, RED1, hRED1, ADAR2a-L1, ADAR2a-L2 |
| Gene groups (HGNC) | Adenosine deaminases acting on RNA |
| Reactome | 2 pathways, smallest: mRNA Editing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P78563](https://www.uniprot.org/uniprotkb/P78563) (Double-stranded RNA-specific editase 1):

> Catalyzes the hydrolytic deamination of adenosine to inosine in double-stranded RNA (dsRNA) referred to as A-to-I RNA editing. This may affect gene expression and function in a number of ways that include mRNA translation by changing codons and hence the amino acid sequence of proteins; pre-mRNA splicing by altering splice site recognition sequences; RNA stability by changing sequences involved in nuclease recognition; genetic stability in the case of RNA virus genomes by changing sequences …

**Summary**, from NCBI Gene [104](https://www.ncbi.nlm.nih.gov/gene/104):

> This gene encodes the enzyme responsible for pre-mRNA editing of the glutamate receptor subunit B by site-specific deamination of adenosines. Studies in rat found that this enzyme acted on its own pre-mRNA molecules to convert an AA dinucleotide to an AI dinucleotide which resulted in a new splice site. Alternative splicing of this gene results in several transcript variants, some of which have been characterized by the presence or absence of an ALU cassette insert and a short or long …

**Accessions** — [HGNC:226](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:226) · Entrez [104](https://www.ncbi.nlm.nih.gov/gene/104) · UniProt [P78563](https://www.uniprot.org/uniprotkb/P78563) · Ensembl [ENSG00000197381](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197381)

## Data

Gene col 12391: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12391); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12391, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12391]; `tensor/DDL_lfc|DDL_z.npy` [12391]; `embed/gene_vectors.npy` [12391]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12391 or target_col == 12391). Every well: [[ADARB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADARB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
