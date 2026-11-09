---
symbol: "AP3S1"
type: "gene"
col: 10872
ensembl_id: "ENSG00000177879"
name: "adaptor related protein complex 3 subunit sigma 1"
location: "5q22.3-q23.1"
module: 7
arm: "-"
pooled_cpm: 144.1
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# AP3S1

*adaptor related protein complex 3 subunit sigma 1* — 5q22.3-q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.58× (z +7.9, q 2e-12, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.725× (z -5.5, q 2e-05, down in 34 of 48 measured lines) ⚠ transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.816× (z -4.7, q 3e-04, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAP30-DT]] (+0.64, fdr 1e-05), [[HERC3]] (+0.63, fdr 7e-06), [[ARL3]] (+0.60, fdr 4e-05); moves opposite to [[PATZ1]] (-0.61, fdr 2e-05), [[PSMD7]] (-0.60, fdr 1e-05), [[TOE1]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLAG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10872.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +7.9 | 2e-12 | 37/48 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +5.8 | 2e-06 | 30/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.87×** | +5.6 | 3e-06 | 27/37 (NCI-H1573, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +4.6 | 7e-04 | 26/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 0.004 | 29/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.24×** | +3.5 | 0.052 | 21/45 (A549, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | 1.20× | +3.1 | 0.16 | 19/49 (C-33 A, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10872.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.725×** | -5.5 | 2e-05 | 34/48 (HOP62, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.744×** | -4.9 | 3e-04 | 27/44 (CFPAC-1, KATO III, …) | top dose only | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.816×** | -4.7 | 3e-04 | 25/48 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.753×** | -4.7 | 3e-04 | 27/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.763×** | -4.7 | 4e-04 | 27/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.770×** | -4.5 | 6e-04 | 30/48 (NCI-H1573, hTERT-HPNE, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.831×** | -4.1 | 0.004 | 23/48 (HS-578T, Panc 03.27, …) | all doses, flat | composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **0.800×** | -3.9 | 0.008 | 26/48 (NCI-H1792, A-172, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.802×** | -3.8 | 0.008 | 29/48 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.798×** | -3.7 | 0.010 | 22/48 (C32, LS 180, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.821×** | -3.4 | 0.033 | 19/49 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **0.816×** | -3.4 | 0.033 | 24/47 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.863× | -3.4 | 0.033 | 17/48 (CFPAC-1, SK-MEL-2, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.826×** | -3.3 | 0.038 | 24/48 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.829×** | -3.2 | 0.046 | 21/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.830×** | -3.2 | 0.047 | 23/48 (A-172, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10872. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 434 | 8 (4 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +25.6) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.65× (z +19.5) | [[Panobinostat (drug)]] 5 µM 0.301× (z -15.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 218 | 8 (4 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +25.7) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.83× (z +15.3) | [[Homoharringtonine (drug)]] 0.05 µM 0.364× (z -11.9) |
| [[SW480 (line)]] | alt | 143 | 10 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.46× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 151 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -15.6) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.433× (z -9.8) |
| [[A-427 (line)]] | wt | 224 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +18.6) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.25× (z +10.3) | — |
| [[C32 (line)]] | wt | 157 | 1 | 3 (3 ⚠) | [[Ponatinib (drug)]] 5 µM 2.26× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -16.8) ⚠ cell-cycle shift, explains ~4% of this change |
| [[NCI-H2030 (line)]] | alt | 68.1 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +12.7) | — |
| [[NCI-H2347 (line)]] | alt | 211 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -14.8) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.493× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 90.3 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +10.5) | — |
| [[PANC-1 (line)]] | alt | 93.3 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +16.9) | — |
| [[HEC-1-A (line)]] | alt | 275 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -11.6) ⚠ cell-cycle shift, explains ~4% of this change |
| [[HS-578T (line)]] | alt | 205 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -18.4) ⚠ cell-cycle shift, explains ~4% of this change |
| [[LOX-IMVI (line)]] | wt | 159 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -17.0) ⚠ cell-cycle shift, explains ~4% of this change |
| [[Panc 03.27 (line)]] | alt | 143 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -17.4) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.441× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 143 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -12.0) ⚠ cell-cycle shift, explains ~4% of this change |
| [[SW48 (line)]] | wt | 121 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +11.4) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +9.8) | — |
| [[A-172 (line)]] | wt | 169 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.317× (z -12.9) |
| [[A498 (line)]] | wt | 105 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.4) ⚠ cell-cycle shift, explains ~4% of this change | — |
| [[A549 (line)]] | wt | 121 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.41× (z +14.1) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 89.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +15.9) ⚠ cell-cycle shift, explains ~4% of this change | — |
| [[H4 (line)]] | wt | 233 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 83.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -12.5) ⚠ cell-cycle shift, explains ~4% of this change |
| [[hTERT-HPNE (line)]] | wt | 149 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -9.9) ⚠ cell-cycle shift, explains ~4% of this change |
| [[J82 (line)]] | alt | 99.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -11.3) ⚠ cell-cycle shift, explains ~4% of this change |
| [[KATO III (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.426× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 140 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.7) ⚠ cell-cycle shift, explains ~4% of this change | — |
| [[LS 180 (line)]] | wt | 169 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.59× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1792 (line)]] | alt | 244 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -10.3) ⚠ cell-cycle shift, explains ~4% of this change |
| [[SW1417 (line)]] | alt | 122 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 143 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 94.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 153 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 83.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 73.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10872), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAP30-DT]] | +0.64 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[HERC3]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[ARL3]] | +0.60 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[GMCL1]] | +0.60 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[ZBTB47-AS1]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ESYT2]] | +0.60 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[SRP54-AS1]] | +0.59 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[MINDY2]] | +0.59 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[RAP1A]] | +0.59 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[PLAG1]] | +0.58 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[ZDHHC9]] | +0.58 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[SEPTIN2]] | +0.58 | +0.66 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATZ1]] | -0.61 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[PSMD7]] | -0.60 | -0.59 / -0.55 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[TOE1]] | -0.60 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[DNAJB12]] | -0.60 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[DNAJC11]] | -0.60 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[NUP62]] | -0.60 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[RTL6]] | -0.60 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[MED1]] | -0.58 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[ZSCAN29]] | -0.58 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[ZNF629]] | -0.58 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[MCRS1]] | -0.58 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[GPATCH4]] | -0.57 | -0.64 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAG1]] | B | PLAG1 activity raises AP3S1's level | lines that do not express PLAG1 (9) vs lines expressing it (41) | 1.38× lower at baseline in the lines without PLAG1 | 0.097 | ⚠ within organs, on part of the lines; also absent: FCGRT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **-** arm (projection on the module's main direction -0.529). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.0, 9.2); signed map (-34.9, 17.9). **Vector** length 116, 35.6% of its response variance represented; |z| ≥ 3 in 1,142 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +3.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.4 | +0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.6 | -0.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.5 | +1.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +2.5 | +0.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.4 | -0.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.4 | +1.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.4 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.5 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.3 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.3 | -2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.1 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.7 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 3 subunit sigma 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.3-q23.1 — chr5:115,841,592-115,914,081 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CLAPS3 |
| Gene groups (HGNC) | Adaptor related protein complex 3 |
| Hallmark sets | PROTEIN_SECRETION, MYC_TARGETS_V1 |
| Reactome | 4 pathways, smallest: Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92572](https://www.uniprot.org/uniprotkb/Q92572) (AP-3 complex subunit sigma-1):

> Part of the AP-3 complex, an adaptor-related complex which is not clathrin-associated. The complex is associated with the Golgi region as well as more peripheral structures. It facilitates the budding of vesicles from the Golgi membrane and may be directly involved in trafficking to lysosomes. In concert with the BLOC-1 complex, AP-3 is required to target cargos into vesicles assembled at cell bodies for delivery into neurites and nerve terminals.

**Summary**, from NCBI Gene [1176](https://www.ncbi.nlm.nih.gov/gene/1176):

> This gene encodes a subunit of the AP3 adaptor complex. This complex functions in the formation of subcellular vesicles budded from the Golgi body. Several related pseudogenes of this gene have been found. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:2013](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2013) · Entrez [1176](https://www.ncbi.nlm.nih.gov/gene/1176) · UniProt [Q92572](https://www.uniprot.org/uniprotkb/Q92572) · Ensembl [ENSG00000177879](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177879)

## Data

Gene col 10872: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10872); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10872, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10872]; `tensor/DDL_lfc|DDL_z.npy` [10872]; `embed/gene_vectors.npy` [10872]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10872 or target_col == 10872). Every well: [[AP3S1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP3S1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
