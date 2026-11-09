---
symbol: "TAF7"
type: "gene"
col: 10971
ensembl_id: "ENSG00000178913"
name: "TATA-box binding protein associated factor 7"
location: "5q31.3"
module: 11
arm: "+"
pooled_cpm: 110.8
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# TAF7

*TATA-box binding protein associated factor 7* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.83× (z +20.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.770× (z -5.1, q 1e-04, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SON]] (+0.72, fdr 1e-05), [[ZNF24]] (+0.71, fdr 1e-05), [[ZNF830]] (+0.68, fdr 7e-06); moves opposite to [[RPA1]] (-0.64, fdr 7e-06), [[ZDHHC8]] (-0.64, fdr 1e-05), [[CEP131]] (-0.63, fdr 4e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10971.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.83×** | +20.1 | 0e+00 | 48/48 (HEC-1-A, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +13.5 | 4e-39 | 45/47 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.55×** | +11.9 | 2e-30 | 38/48 (A549, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.81×** | +11.4 | 5e-28 | 45/48 (BT-474, COLO 205, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +10.4 | 2e-23 | 43/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +9.3 | 2e-18 | 45/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.46×** | +9.1 | 7e-18 | 41/49 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.57×** | +8.7 | 2e-16 | 40/48 (BT-474, COLO 205, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.49×** | +7.7 | 9e-13 | 45/48 (BT-474, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +7.6 | 2e-12 | 40/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.49×** | +7.4 | 5e-12 | 34/48 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.6 | 1e-09 | 28/49 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +4.9 | 5e-05 | 20/48 (SW480, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.8 | 7e-05 | 23/48 (HS-578T, PANC-1, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **1.30×** | +4.7 | 8e-05 | 24/45 (C-33 A, Hs 766T, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.7 | 9e-05 | 33/48 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +4.7 | 9e-05 | 29/48 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.3 | 6e-04 | 26/48 (A498, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.25×** | +4.0 | 0.002 | 25/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Thymol (drug)]] 5 µM |  | 1.16× | +4.0 | 0.002 | 9/48 (CFPAC-1, Panc 03.27, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.003 | 23/48 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.005 | 25/48 (NCI-H2030, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.010 | 18/48 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10971.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.770×** | -5.1 | 1e-04 | 30/48 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.772×** | -5.0 | 1e-04 | 34/48 (COLO 205, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.790×** | -4.6 | 8e-04 | 28/48 (A-172, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.859× | -4.2 | 0.004 | 18/48 (H4, AsPC-1, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.813×** | -3.9 | 0.012 | 27/49 (HepG2/C3A, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.821×** | -3.8 | 0.012 | 26/48 (COLO 205, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 0.837× | -3.3 | 0.060 | 16/48 (C-33 A, A549, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.720×** | -3.3 | 0.060 | 17/49 (H4, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.845× | -3.3 | 0.062 | 16/48 (HOP62, AsPC-1, …) | two highest doses | position effect removed |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.848× | -3.2 | 0.074 | 17/48 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Sildenafil (drug)]] 0.5 µM |  | 0.851× | -3.1 | 0.087 | 11/48 (hTERT-HPNE, HOP62, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.895× | -3.1 | 0.10 | 5/48 (NCI-H661, NCI-H2347, …) | top dose only |  |
| [[Folic acid (drug)]] 5 µM |  | 0.897× | -3.0 | 0.12 | 5/48 (H4, CFPAC-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10971. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 154 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +15.0) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 121 | 8 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.74× (z +13.2) | — |
| [[COLO 205 (line)]] | alt | 138 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +13.9) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.72× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 114 | 7 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.33× (z +18.6) | — |
| [[SW480 (line)]] | alt | 112 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.69× (z +18.7) | — |
| [[A498 (line)]] | wt | 108 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +16.1) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.13× (z +15.9) | — |
| [[BT-474 (line)]] | alt | 82.3 | 6 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.33× (z +16.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 126 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.19× (z +16.2) | — |
| [[NCI-H2030 (line)]] | alt | 139 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +11.5) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.24× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 109 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.16× (z +14.1) | — |
| [[A549 (line)]] | wt | 95.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +16.5) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.83× (z +12.4) | — |
| [[HS-578T (line)]] | alt | 51.8 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.98× (z +12.7) | — |
| [[SW1417 (line)]] | alt | 147 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.77× (z +14.1) | — |
| [[C32 (line)]] | wt | 61.5 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.65× (z +17.9) | — |
| [[HEC-1-A (line)]] | alt | 134 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.07× (z +22.3) | — |
| [[LOX-IMVI (line)]] | wt | 113 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.90× (z +15.5) | — |
| [[Panc 03.27 (line)]] | alt | 80.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.03× (z +12.2) | [[Lonafarnib (drug)]] 5 µM 0.189× (z -9.5) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 181 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.12× (z +18.9) | — |
| [[A-172 (line)]] | wt | 141 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.28× (z +16.3) | — |
| [[Hs 766T (line)]] | wt | 72.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.1) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.89× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 91.9 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.43× (z +17.3) | — |
| [[J82 (line)]] | alt | 95.1 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.35× (z +10.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 2.06× (z +8.8) | — |
| [[KATO III (line)]] | alt | 144 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.62× (z +12.4) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.376× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 114 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.5) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.05× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 65.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 123 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.29× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 62.1 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.67× (z +11.9) | — |
| [[PANC-1 (line)]] | alt | 118 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.05× (z +11.6) | — |
| [[RKO (line)]] | wt | 117 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.73× (z +14.1) | — |
| [[SNU-423 (line)]] | alt | 92.7 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.78× (z +13.2) | — |
| [[A-427 (line)]] | wt | 143 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.86× (z +16.1) | — |
| [[AN3 CA (line)]] | alt | 95.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +8.5) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[CFPAC-1 (line)]] | alt | 95.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.17× (z +9.2) | — |
| [[H4 (line)]] | wt | 148 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.51× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 134 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.62× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 87.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.48× (z +8.7) | — |
| [[LoVo (line)]] | wt | 192 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.74× (z +13.8) | — |
| [[RPMI-7951 (line)]] | alt | 82.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.94× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 64.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.87× (z +12.6) | — |
| [[SNU-1 (line)]] | wt | 68.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.93× (z +10.1) | — |
| [[C-33 A (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 104 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 65.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10971), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SON]] | +0.72 | +0.76 / +0.51 | both halves | 1e-05 |  |
| [[ZNF24]] | +0.71 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[ZNF830]] | +0.68 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ZNF75A]] | +0.66 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ZBTB40]] | +0.65 | +0.65 / +0.41 | both halves | 4e-05 |  |
| [[ZNF189]] | +0.65 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[RBBP6]] | +0.64 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[C14orf119]] | +0.64 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ZC3H11A]] | +0.64 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[FAM200A]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[MED1]] | +0.63 | +0.78 / +0.33 | both halves | 1e-04 | STRING 811 |
| [[GGPS1]] | +0.63 | +0.64 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPA1]] | -0.64 | -0.58 / -0.61 | both halves | 7e-06 | pathway: Regulation of TP53 Activity |
| [[ZDHHC8]] | -0.64 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[CEP131]] | -0.63 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[UBAC1]] | -0.61 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[ANAPC5]] | -0.61 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SETD3]] | -0.60 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[ABHD12]] | -0.59 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[TBCD]] | -0.59 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[CPSF1]] | -0.58 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[MPND]] | -0.57 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[GPD1L]] | -0.57 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[HACE1]] | -0.57 | -0.62 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TAF7's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.578). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-30.0, 12.6); signed map (5.1, -28.0). **Vector** length 122, 38.7% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.0 | +20.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.1 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.2 | +13.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.6 | +2.9 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.2 | -0.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.0 | -5.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.9 | -5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.7 | -1.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.5 | -4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.2 | -4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.7 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.7 | -2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:141,259,884-141,320,784 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAFII55; previously TAF2F |
| Gene groups (HGNC) | General transcription factor IID complex subunits |
| Reactome | 19 pathways, smallest: HIV Transcription Initiation; RNA Polymerase II HIV Promoter Escape; RNA Polymerase II Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15545](https://www.uniprot.org/uniprotkb/Q15545) (Transcription initiation factor TFIID subunit 7):

> The TFIID basal transcription factor complex plays a major role in the initiation of RNA polymerase II (Pol II)-dependent transcription. TFIID recognizes and binds promoters with or without a TATA box via its subunit TBP, a TATA-box-binding protein, and promotes assembly of the pre-initiation complex (PIC). The TFIID complex consists of TBP and TBP-associated factors (TAFs), including TAF1, TAF2, TAF3, TAF4, TAF5, TAF6, TAF7, TAF8, TAF9, TAF10, TAF11, TAF12 and TAF13. TAF7 forms a promoter DNA …

**Summary**, from NCBI Gene [6879](https://www.ncbi.nlm.nih.gov/gene/6879):

> The intronless gene for this transcription coactivator is located between the protocadherin beta and gamma gene clusters on chromosome 5. The protein encoded by this gene is a component of the TFIID protein complex, a complex which binds to the TATA box in class II promoters and recruits RNA polymerase II and other factors. This particular subunit interacts with the largest TFIID subunit, as well as multiple transcription activators. The protein is required for transcription by promoters …

**Accessions** — [HGNC:11541](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11541) · Entrez [6879](https://www.ncbi.nlm.nih.gov/gene/6879) · UniProt [Q15545](https://www.uniprot.org/uniprotkb/Q15545) · Ensembl [ENSG00000178913](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178913)

## Data

Gene col 10971: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10971); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10971, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10971]; `tensor/DDL_lfc|DDL_z.npy` [10971]; `embed/gene_vectors.npy` [10971]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10971 or target_col == 10971). Every well: [[TAF7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
