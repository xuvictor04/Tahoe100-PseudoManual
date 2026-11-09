---
symbol: "NAA15"
type: "gene"
col: 8879
ensembl_id: "ENSG00000164134"
name: "N-alpha-acetyltransferase 15, NatA auxiliary subunit"
location: "4q31.1"
module: 4
arm: "+"
pooled_cpm: 124.75
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 7
n_dd_up_clean: 28
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# NAA15

*N-alpha-acetyltransferase 15, NatA auxiliary subunit* — 4q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.89× (z +26.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.736× (z -7.8, q 3e-12, down in 29 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCERG1]] (+0.83, fdr 7e-06), [[FARSB]] (+0.78, fdr 7e-06), [[POLR1A]] (+0.78, fdr 7e-06); moves opposite to [[AAMDC]] (-0.78, fdr 7e-06), [[ZFYVE1]] (-0.77, fdr 7e-06), [[TSC22D4]] (-0.74, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CXCR4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8879.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.89×** | +26.8 | 0e+00 | 48/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.84×** | +18.7 | 0e+00 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.83×** | +18.6 | 0e+00 | 47/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **6.50×** | +17.5 | 0e+00 | 48/49 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.53×** | +16.0 | 0e+00 | 47/48 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +14.9 | 0e+00 | 46/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.77×** | +14.6 | 0e+00 | 48/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.18×** | +13.9 | 3e-42 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.17×** | +13.9 | 7e-42 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.94×** | +11.8 | 2e-30 | 45/48 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +11.1 | 6e-27 | 45/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.85×** | +11.0 | 2e-26 | 45/48 (Hs 766T, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.04×** | +9.2 | 1e-18 | 47/48 (NCI-H460, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.63×** | +8.8 | 7e-17 | 42/48 (SW480, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.49×** | +7.1 | 4e-11 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +6.4 | 4e-09 | 38/48 (HT-29, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.96×** | +6.3 | 1e-08 | 41/48 (A498, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +6.2 | 2e-08 | 33/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8879.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.736×** | -7.8 | 3e-12 | 29/49 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.701×** | -4.6 | 0.001 | 33/48 (LoVo, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.778×** | -4.5 | 0.001 | 30/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.785×** | -4.4 | 0.002 | 38/48 (KATO III, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | 0.851× | -4.1 | 0.004 | 24/48 (RKO, A498, …) | top dose only | low cells (technical?) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.739×** | -3.9 | 0.009 | 32/48 (MIA PaCa-2, SW480, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.812×** | -3.8 | 0.014 | 29/48 (KATO III, A-427, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.767×** | -3.4 | 0.044 | 24/47 (Panc 03.27, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.838× | -3.4 | 0.044 | 20/48 (LoVo, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.854× | -3.3 | 0.049 | 17/48 (MIA PaCa-2, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.871× | -3.2 | 0.072 | 11/49 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.834× | -3.2 | 0.072 | 16/47 (SW480, LoVo, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.841× | -3.1 | 0.072 | 16/48 (KATO III, A-172, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.845× | -3.0 | 0.091 | 21/48 (RKO, BT-474, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -3.0 | 0.091 | 23/50 (C-33 A, LOX-IMVI, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.847× | -3.0 | 0.091 | 21/48 (SW 1271, SW 900, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.848× | -3.0 | 0.097 | 18/47 (RKO, LoVo, …) | two highest doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8879. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 134 | 17 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +23.4) | — |
| [[SW480 (line)]] | alt | 98.5 | 16 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +15.3) | — |
| [[PANC-1 (line)]] | alt | 160 | 13 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +27.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 107 | 13 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +21.7) | — |
| [[LoVo (line)]] | wt | 145 | 11 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.34× (z +19.0) | [[Trametinib (drug)]] 5 µM 0.523× (z -9.3) ⚠ cell-cycle shift, explains ~59% of this change |
| [[HOP62 (line)]] | alt | 90.1 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +19.8) | — |
| [[HT-29 (line)]] | alt | 109 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +20.4) | — |
| [[NCI-H1792 (line)]] | alt | 97.9 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +23.7) | — |
| [[A498 (line)]] | wt | 135 | 6 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +21.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -13.7) |
| [[COLO 205 (line)]] | alt | 66.7 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +16.5) | — |
| [[H4 (line)]] | wt | 124 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +16.3) | — |
| [[LS 180 (line)]] | wt | 95.8 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.71× (z +17.9) | — |
| [[SK-MEL-2 (line)]] | alt | 175 | 6 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +18.4) | [[Dinaciclib (drug)]] 0.5 µM 0.459× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -9.0) |
| [[SNU-423 (line)]] | alt | 57.9 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.80× (z +23.6) | — |
| [[SW 900 (line)]] | alt | 87.6 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +16.3) | — |
| [[A549 (line)]] | wt | 111 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +21.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 101 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +15.4) | — |
| [[Hs 766T (line)]] | wt | 81.6 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +14.0) | — |
| [[KATO III (line)]] | alt | 107 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.57× (z +15.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 117 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +13.1) | — |
| [[NCI-H23 (line)]] | alt | 113 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -8.8) |
| [[A-172 (line)]] | wt | 83.4 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +21.7) | — |
| [[C32 (line)]] | wt | 82.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +16.5) | — |
| [[NCI-H2030 (line)]] | alt | 158 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +12.5) | — |
| [[NCI-H2347 (line)]] | alt | 154 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +18.3) | — |
| [[Panc 03.27 (line)]] | alt | 97.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +14.1) | — |
| [[RKO (line)]] | wt | 242 | 3 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 5.08× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -16.4) |
| [[BT-474 (line)]] | alt | 169 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 72.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +19.4) | — |
| [[HS-578T (line)]] | alt | 97.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +18.5) | — |
| [[J82 (line)]] | alt | 133 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +19.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.619× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 121 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.9) | — |
| [[RPMI-7951 (line)]] | alt | 127 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +16.7) | — |
| [[SW1417 (line)]] | alt | 110 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +12.6) | — |
| [[HCT15 (line)]] | alt | 127 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +15.0) | — |
| [[HEC-1-A (line)]] | alt | 142 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +14.4) | — |
| [[HepG2_C3A (line)]] | wt | 110 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +12.3) | — |
| [[hTERT-HPNE (line)]] | wt | 97.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +15.9) | — |
| [[A-427 (line)]] | wt | 201 | 2 | 1 | [[PH-797804 (drug)]] 5 µM 4.93× (z +10.6) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.541× (z -11.1) |
| [[C-33 A (line)]] | alt | 259 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -9.8) |
| [[SNU-1 (line)]] | wt | 216 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +13.1) | — |
| [[SW48 (line)]] | wt | 196 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.79× (z +10.7) | — |
| [[SHP-77 (line)]] | alt | 123 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.09× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 233 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 204 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 93.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8879), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCERG1]] | +0.83 | +0.80 / +0.84 | both halves | 7e-06 |  |
| [[FARSB]] | +0.78 | +0.74 / +0.82 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.78 | +0.75 / +0.78 | both halves | 7e-06 |  |
| [[ABCE1]] | +0.77 | +0.74 / +0.83 | both halves | 7e-06 | STRING 602 |
| [[DDX10]] | +0.77 | +0.67 / +0.80 | both halves | 7e-06 |  |
| [[RUVBL1]] | +0.76 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[ATIC]] | +0.76 | +0.67 / +0.81 | both halves | 7e-06 |  |
| [[CTPS1]] | +0.75 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[NAA25]] | +0.75 | +0.76 / +0.73 | both halves | 7e-06 | same gene group; STRING 993 |
| [[LTV1]] | +0.75 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[PNO1]] | +0.74 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[PUM3]] | +0.74 | +0.68 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AAMDC]] | -0.78 | -0.75 / -0.76 | both halves | 7e-06 |  |
| [[ZFYVE1]] | -0.77 | -0.75 / -0.75 | both halves | 7e-06 |  |
| [[TSC22D4]] | -0.74 | -0.68 / -0.76 | both halves | 7e-06 |  |
| [[NARF]] | -0.70 | -0.67 / -0.69 | both halves | 7e-06 |  |
| [[RSRP1]] | -0.69 | -0.62 / -0.73 | both halves | 7e-06 |  |
| [[TCP11L2]] | -0.68 | -0.71 / -0.63 | both halves | 7e-06 |  |
| [[CCS]] | -0.68 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[LMBR1L]] | -0.67 | -0.57 / -0.75 | both halves | 1e-05 |  |
| [[CERT1]] | -0.67 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[TMEM59]] | -0.66 | -0.61 / -0.66 | both halves | 7e-06 |  |
| [[FAM117A]] | -0.66 | -0.57 / -0.61 | both halves | 8e-06 |  |
| [[TESK2]] | -0.65 | -0.58 / -0.63 | both halves | 8e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCR4]] | B | CXCR4 activity lowers NAA15's level | lines that do not express CXCR4 (22) vs lines expressing it (28) | 1.28× higher at baseline in the lines without CXCR4 | 0.026 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, LMO2 |
| [[ANG]] | C | ANG activity lowers NAA15's level | lines that do not express ANG (4) vs lines expressing it (46) | 1.56× higher at baseline in the lines without ANG | 0.054 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.860). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-12.3, -35.9); signed map (-6.4, -47.2). **Vector** length 104, 44.6% of its response variance represented; |z| ≥ 3 in 1,738 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.54 to 21); *tRNA Aminoacylation* (reactome, mean cos +0.52 to 7); *tRNA processing in the nucleus* (reactome, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.1 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +7.4 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.4 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.9 | +0.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.3 | +6.3 |
|  | [[EX229 (drug)]] 5 µM |  | +5.2 | +5.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.1 | +4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.6 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +6.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -7.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.8 | +18.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.0 | +0.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.7 | -4.6 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -2.5 | -1.5 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -2.4 | -0.1 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | N-alpha-acetyltransferase 15, NatA auxiliary subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.1 — chr4:139,301,446-139,420,033 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TBDN100, NATH, FLJ13340; previously NARG1 |
| Gene groups (HGNC) | N-alpha-acetyltransferase subunits; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXJ9](https://www.uniprot.org/uniprotkb/Q9BXJ9) (N-alpha-acetyltransferase 15, NatA auxiliary subunit):

> Auxillary subunit of N-terminal acetyltransferase complexes which display alpha (N-terminal) acetyltransferase (NAT) activity. The NAT activity may be important for vascular, hematopoietic and neuronal growth and development. Required to control retinal neovascularization in adult ocular endothelial cells. In complex with XRCC6 and XRCC5 (Ku80), up-regulates transcription from the osteocalcin promoter.

**Summary**, from NCBI Gene [80155](https://www.ncbi.nlm.nih.gov/gene/80155):

> N-alpha-acetylation is among the most common post-translational protein modifications in eukaryotic cells. This process involves the transfer of an acetyl group from acetyl-coenzyme A to the alpha-amino group on a nascent polypeptide and is essential for normal cell function. This gene encodes the auxillary subunit of the N-terminal acetyltransferase A (NatA) complex. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:30782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30782) · Entrez [80155](https://www.ncbi.nlm.nih.gov/gene/80155) · UniProt [Q9BXJ9](https://www.uniprot.org/uniprotkb/Q9BXJ9) · Ensembl [ENSG00000164134](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164134)

## Data

Gene col 8879: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8879); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8879, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8879]; `tensor/DDL_lfc|DDL_z.npy` [8879]; `embed/gene_vectors.npy` [8879]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8879 or target_col == 8879). Every well: [[NAA15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAA15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
