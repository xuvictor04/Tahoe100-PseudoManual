---
symbol: "ARPP19"
type: "gene"
col: 4939
ensembl_id: "ENSG00000128989"
name: "cAMP regulated phosphoprotein 19"
location: "15q21.2"
module: 25
arm: "+"
pooled_cpm: 113.57
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# ARPP19

*cAMP regulated phosphoprotein 19* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.50× (z +19.9, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.48× (z +8.5, q 3e-15, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.726× (z -7.0, q 2e-09, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATL3]] (+0.71, fdr 7e-06), [[MOB1A]] (+0.67, fdr 1e-05), [[NRAS]] (+0.67, fdr 4e-05); moves opposite to [[INAFM1]] (-0.70, fdr 7e-06), [[ING2]] (-0.69, fdr 4e-05), [[NUDT22]] (-0.64, fdr 4e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4939.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +19.9 | 0e+00 | 49/49 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +18.0 | 0e+00 | 43/44 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +14.5 | 1e-45 | 45/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.50×** | +8.8 | 1e-16 | 41/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +8.5 | 3e-15 | 41/48 (NCI-H460, COLO 205, …) | two highest doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.46×** | +8.2 | 2e-14 | 39/48 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.04×** | +8.1 | 5e-14 | 40/49 (LoVo, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +7.5 | 4e-12 | 37/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.39×** | +7.2 | 4e-11 | 34/48 (SW480, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.38×** | +7.0 | 2e-10 | 36/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +6.7 | 1e-09 | 36/47 (COLO 205, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +5.8 | 4e-07 | 36/48 (COLO 205, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +5.5 | 2e-06 | 31/48 (C32, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.58×** | +5.2 | 7e-06 | 26/38 (NCI-H1573, A-172, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.9 | 3e-05 | 23/48 (C32, SK-MEL-2, …) | top dose only | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.17× | +3.5 | 0.016 | 14/48 (CFPAC-1, COLO 205, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.5 | 0.016 | 18/48 (C32, BT-474, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.30×** | +2.9 | 0.084 | 10/48 (CFPAC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4939.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.726×** | -7.0 | 2e-09 | 37/48 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.743×** | -6.5 | 3e-08 | 39/48 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -5.9 | 8e-07 | 0/50 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.770×** | -5.7 | 2e-06 | 34/48 (CFPAC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -3.8 | 0.017 | 19/48 (HEC-1-A, A549, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.899× | -3.3 | 0.088 | 15/49 (LoVo, CHP-212, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.867× | -3.1 | 0.15 | 16/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4939. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 175 | 9 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +15.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.15× (z +9.9) | — |
| [[SW480 (line)]] | alt | 101 | 9 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +21.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 2.83× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 88.5 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +14.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.24× (z +12.5) | — |
| [[C32 (line)]] | wt | 100 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.24× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 114 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.71× (z +11.5) | — |
| [[KATO III (line)]] | alt | 125 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +12.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 93.5 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.88× (z +18.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 113 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +12.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 98.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +12.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 174 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +17.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 87.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +14.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 71.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.89× (z +13.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 72.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +12.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 120 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +14.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 86.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +12.0) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 101 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.14× (z +14.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 80.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +11.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 112 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +15.6) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.78× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 162 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.590× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 130 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.97× (z +14.0) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 107 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +19.3) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 78.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +13.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 149 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 137 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +11.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 111 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.32× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 120 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +14.4) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 122 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +11.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 131 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +16.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 90.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 108 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.23× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 131 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 2.83× (z +9.3) | — |
| [[A-427 (line)]] | wt | 82.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.85× (z +10.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 78.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +9.7) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 127 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.31× (z +8.7) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 153 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 141 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +10.6) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 117 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.43× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 197 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.33× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 82.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +13.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.17× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 139 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +9.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 122 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 107 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 95.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4939), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATL3]] | +0.71 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[MOB1A]] | +0.67 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[NRAS]] | +0.67 | +0.41 / +0.78 | both halves | 4e-05 |  |
| [[SGCB]] | +0.67 | +0.38 / +0.72 | both halves | 6e-05 |  |
| [[UHMK1]] | +0.67 | +0.44 / +0.74 | both halves | 3e-05 |  |
| [[FUCA2]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[YWHAQ]] | +0.66 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[MMGT1]] | +0.65 | +0.50 / +0.76 | both halves | 1e-05 |  |
| [[DHFR]] | +0.64 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[SZRD1]] | +0.64 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[UBQLN1]] | +0.64 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[UBE2V1]] | +0.63 | +0.49 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 8 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INAFM1]] | -0.70 | -0.60 / -0.70 | both halves | 7e-06 |  |
| [[ING2]] | -0.69 | -0.41 / -0.73 | both halves | 4e-05 |  |
| [[NUDT22]] | -0.64 | -0.25 / -0.70 | both halves | 4e-04 |  |
| [[GCAT]] | -0.64 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[TMEM258]] | -0.62 | -0.42 / -0.68 | both halves | 4e-05 |  |
| [[METTL23]] | -0.61 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[KRTCAP2]] | -0.60 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[PMM1]] | -0.59 | -0.31 / -0.63 | both halves | 2e-04 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[SMIM26]] ⚠ | -0.58 | -0.43 / -0.59 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ING1]] | -0.58 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[NKAP]] | -0.58 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[MRPL36]] | -0.58 | -0.22 / -0.64 | both halves | 6e-04 |  |
| [[SNHG9]] | -0.58 | -0.52 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ARPP19's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.742). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.8, -20.4); signed map (-17.9, -38.0). **Vector** length 84.6, 22.2% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.6 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +14.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +18.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +19.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +6.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.9 | +0.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.9 | -0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +8.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +5.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | -3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -0.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.2 | -1.0 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -1.8 | +1.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.8 | +1.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | cAMP regulated phosphoprotein 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:52,547,045-52,569,883 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARPP-19, ARPP-16, ARPP16, ENSAL |
| Hallmark sets | XENOBIOTIC_METABOLISM, GLYCOLYSIS |
| Reactome | 5 pathways, smallest: MASTL Facilitates Mitotic Progression; Mitotic Prophase; M Phase |
| Matched by | ensembl_id |

**Function**, from UniProt [P56211](https://www.uniprot.org/uniprotkb/P56211) (cAMP-regulated phosphoprotein 19):

> Protein phosphatase inhibitor that specifically inhibits protein phosphatase 2A (PP2A). Inhibition of PP2A is enhanced when ARPP19 is phosphorylated. When phosphorylated at Ser-62 during mitosis, specifically interacts with PPP2R2D (PR55-delta) and inhibits its activity, leading to inactivation of PP2A, an essential condition to keep cyclin-B1-CDK1 activity high during M phase. May indirectly enhance GAP-43 expression (By similarity).

**Summary**, from NCBI Gene [10776](https://www.ncbi.nlm.nih.gov/gene/10776):

> The 19-kD cAMP-regulated phosphoprotein plays a role in regulating mitosis by inhibiting protein phosphatase-2A (PP2A; see MIM 176915) (summary by Gharbi-Ayachi et al., 2010 [PubMed 21164014]).[supplied by OMIM, Feb 2011]

**Accessions** — [HGNC:16967](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16967) · Entrez [10776](https://www.ncbi.nlm.nih.gov/gene/10776) · UniProt [P56211](https://www.uniprot.org/uniprotkb/P56211) · Ensembl [ENSG00000128989](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128989)

## Data

Gene col 4939: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4939); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4939, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4939]; `tensor/DDL_lfc|DDL_z.npy` [4939]; `embed/gene_vectors.npy` [4939]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4939 or target_col == 4939). Every well: [[ARPP19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARPP19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
