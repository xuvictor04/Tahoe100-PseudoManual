---
symbol: "AGPAT4"
type: "gene"
col: 373
ensembl_id: "ENSG00000026652"
name: "1-acylglycerol-3-phosphate O-acyltransferase 4"
location: "6q26"
module: 34
arm: "+"
pooled_cpm: 68.91
n_lines_expressing: 44
n_dd_up: 8
n_dd_down: 18
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 8
direction_downstream: 3
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# AGPAT4

*1-acylglycerol-3-phosphate O-acyltransferase 4* — 6q26

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.42× (z +8.1, q 3e-13, up in 32 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.475× (z -17.1, q 0e+00, down in 35 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MEG8]] (+0.64, fdr 1e-05), [[IER3]] (+0.63, fdr 1e-05), [[MEG3]] (+0.63, fdr 1e-05); moves opposite to [[SAFB]] (-0.55, fdr 2e-05), [[CHPT1]] (-0.51, fdr 3e-05), [[ZNF362]] (-0.51, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[KCNMA1]] → it (grade B ⚠); 3 go from it, the strongest it → [[BPGM]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 373.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +8.1 | 3e-13 | 32/42 (NCI-H2347, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +6.0 | 8e-07 | 26/42 (RKO, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +5.8 | 2e-06 | 22/42 (C32, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +5.6 | 3e-06 | 21/42 (SW48, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +5.5 | 4e-06 | 22/42 (SW48, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +5.4 | 5e-06 | 23/42 (LS 180, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.32×** | +4.6 | 4e-04 | 19/42 (C32, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.010 | 14/41 (LS 180, LOX-IMVI, …) | two highest doses | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | 1.45× | +3.1 | 0.10 | 12/43 (RKO, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 373.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.475×** | -17.1 | 0e+00 | 35/43 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.576×** | -8.9 | 1e-16 | 27/43 (NCI-H1573, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -7.3 | 5e-11 | 26/42 (hTERT-HPNE, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.636×** | -7.0 | 3e-10 | 18/36 (NCI-H1573, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.673×** | -6.4 | 2e-08 | 28/41 (RPMI-7951, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.694×** | -5.9 | 3e-07 | 22/42 (PANC-1, LoVo, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.706×** | -5.2 | 2e-05 | 23/39 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.743×** | -4.8 | 1e-04 | 22/42 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.570×** | -4.8 | 1e-04 | 22/43 (A549, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.777×** | -4.1 | 0.003 | 21/42 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.838× | -4.0 | 0.003 | 19/42 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.774×** | -4.0 | 0.003 | 18/42 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.786×** | -3.9 | 0.004 | 21/42 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.665×** | -3.4 | 0.022 | 18/42 (HS-578T, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.808×** | -3.4 | 0.022 | 16/42 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.674×** | -3.3 | 0.030 | 14/41 (AsPC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.817×** | -3.3 | 0.037 | 14/42 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 373. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 157 | 1 | 19 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.70× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.0553× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 0.194× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 208 | 3 (1 ⚠) | 12 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +16.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.39× (z +8.9) | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM 0.171× (z -12.0) |
| [[A-172 (line)]] | wt | 143 | 2 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +16.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.76× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -18.5) |
| [[LoVo (line)]] | wt | 80.6 | 2 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +17.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.25× (z +12.2) | [[Ponatinib (drug)]] 5 µM 0.253× (z -9.2) |
| [[PANC-1 (line)]] | alt | 117 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -22.5) |
| [[A498 (line)]] | wt | 95.3 | 3 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.31× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -19.0) |
| [[A549 (line)]] | wt | 98.7 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -18.3) |
| [[SNU-423 (line)]] | alt | 209 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +20.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.90× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.163× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -10.3) |
| [[SW48 (line)]] | wt | 41.7 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.9× (z +21.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 42.8× (z +19.7) | — |
| [[hTERT-HPNE (line)]] | wt | 180 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -14.6) |
| [[SHP-77 (line)]] | alt | 39.9 | 3 | 1 | [[Auranofin (drug)]] 5 µM 3.91× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -8.7) |
| [[A-427 (line)]] | wt | 59.3 | 0 | 3 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -14.3) ⚠ cell-cycle shift, explains ~18% of this change |
| [[C-33 A (line)]] | alt | 63.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 122 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 19.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +15.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.94× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 46.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -17.8) |
| [[RKO (line)]] | wt | 39.9 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.52× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 54.8 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -11.0) |
| [[HS-578T (line)]] | alt | 91.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 51.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -14.7) |
| [[NCI-H596 (line)]] | alt | 69.3 | 1 | 1 | [[Methylthiouracil (drug)]] 0.05 µM 2.67× (z +11.8) | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.341× (z -13.4) |
| [[Panc 03.27 (line)]] | alt | 25.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.43× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 163 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -18.6) |
| [[SW 900 (line)]] | alt | 152 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -8.8) |
| [[AN3 CA (line)]] | alt | 64.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 25.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +14.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 79.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -8.5) |
| [[Hs 766T (line)]] | wt | 52.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -11.7) |
| [[HT-29 (line)]] | alt | 50.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -12.4) |
| [[J82 (line)]] | alt | 49.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +15.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 38.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.42× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 39.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 148 | 0 | 1 | — | [[Eplerenone (drug)]] 0.05 µM 0.0845× (z -9.0) |
| [[BT-474 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.98 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.81 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 97.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 11.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 373), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEG8]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[IER3]] | +0.63 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[MEG3]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[C6orf141]] | +0.61 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[LAMC2]] | +0.60 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ARHGEF4]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[TUBB2A]] | +0.59 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[GEM]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[C3orf52]] | +0.58 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[PKIA]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[WNT7B]] | +0.57 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[RPLP0P2]] | +0.57 | +0.48 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAFB]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[CHPT1]] | -0.51 | -0.50 / -0.46 | both halves | 3e-05 | pathway: Glycerophospholipid biosynthesis |
| [[ZNF362]] | -0.51 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[CIAO2A]] | -0.51 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[CLPX]] | -0.51 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[DERA]] | -0.51 | -0.49 / -0.37 | both halves | 9e-05 |  |
| [[RAF1]] | -0.50 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[RPRD2]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ERBB2]] | -0.49 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[KCTD3]] | -0.48 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[NDUFAF6]] | -0.48 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[PPM1B]] | -0.48 | -0.42 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNMA1]] | B | KCNMA1 activity raises AGPAT4's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 2.57× lower at baseline in the lines without KCNMA1 | 0.036 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[NR3C1]] | B | NR3C1 activity lowers AGPAT4's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[GJA1]] | B | GJA1 activity strengthens AGPAT4's drug response | lines that do not express GJA1 (21) vs lines expressing it (22) | the lines without GJA1 respond 0.86× as strongly (z diff +0.76); strongest at Dinaciclib 0.5 µM: 0.74x vs 0.42x (z diff +4.2) | 0.055 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1; target measured in part of the lines; both ways; artifact flags |
| [[CPA6]] | B | CPA6 activity raises AGPAT4's level | lines that do not express CPA6 (14) vs lines expressing it (36) | 1.80× lower at baseline in the lines without CPA6 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000225647, LINC02223, LINC01579; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers AGPAT4's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[KCNMA1]] | B | KCNMA1 activity strengthens AGPAT4's drug response | lines that do not express KCNMA1 (21) vs lines expressing it (22) | the lines without KCNMA1 respond 0.75× as strongly (z diff +0.90); strongest at Dinaciclib 0.5 µM: 0.77x vs 0.41x (z diff +4.1) | 0.092 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN; target measured in part of the lines; both ways; artifact flags |
| [[MIR493HG]] | B | MIR493HG activity raises AGPAT4's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 2.16× lower at baseline in the lines without MIR493HG | 0.093 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252 |
| [[RAB31]] | B | RAB31 activity raises AGPAT4's level | lines that do not express RAB31 (16) vs lines expressing it (34) | 2.53× lower at baseline in the lines without RAB31 | 0.097 | ⚠ within organs, on part of the lines; also absent: VEGFC, HERC5, NR3C1 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BPGM]] | B | AGPAT4 activity lowers BPGM's level | lines that do not express AGPAT4 (6) vs lines expressing it (44) | 1.07× higher at baseline in the lines without AGPAT4 | 0.056 | ⚠ within organs, on part of the lines; also absent: SSBP2, ENSG00000236230, PTPN13; maybe low, not absent |
| [[LYPD3]] | B | AGPAT4 activity lowers LYPD3's level | lines that do not express AGPAT4 (6) vs lines expressing it (44) | 2.01× higher at baseline in the lines without AGPAT4 | 0.090 | ⚠ within organs, on part of the lines; also absent: SSBP2, ENSG00000236230, PTPN13; maybe low, not absent |
| [[SFR1]] | C | AGPAT4's natural level strengthens SFR1's drug response | AGPAT4's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.71, reverse -0.09; direction not clear | 0.037 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.549). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.3, 0.8); signed map (6.0, 42.0). **Vector** length 119, 32.7% of its response variance represented; |z| ≥ 3 in 1,434 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +8.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +5.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.6 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | -1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +1.9 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.3 | -17.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.5 | -4.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.2 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.1 | -2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -7.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.0 | -1.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.8 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | 1-acylglycerol-3-phosphate O-acyltransferase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q26 — chr6:161,129,967-161,274,061 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LPAAT-delta, dJ473J16.2, LPAAT4, LPLAT4 |
| Gene groups (HGNC) | 1-acylglycerol-3-phosphate O-acyltransferases; Lysophospholipid acyltransferases |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 4 pathways, smallest: Synthesis of PA; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRZ5](https://www.uniprot.org/uniprotkb/Q9NRZ5) (1-acyl-sn-glycerol-3-phosphate acyltransferase delta):

> Converts 1-acyl-sn-glycerol-3-phosphate (lysophosphatidic acid or LPA) into 1,2-diacyl-sn-glycerol-3-phosphate (phosphatidic acid or PA) by incorporating an acyl moiety at the sn-2 position of the glycerol backbone (By similarity). Exhibits high acyl-CoA specificity for polyunsaturated fatty acyl-CoA, especially docosahexaenoyl-CoA (22:6-CoA, DHA-CoA) (By similarity).

**Summary**, from NCBI Gene [56895](https://www.ncbi.nlm.nih.gov/gene/56895):

> This gene encodes a member of the 1-acylglycerol-3-phosphate O-acyltransferase family. This integral membrane protein converts lysophosphatidic acid to phosphatidic acid, the second step in de novo phospholipid biosynthesis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20885](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20885) · Entrez [56895](https://www.ncbi.nlm.nih.gov/gene/56895) · UniProt [Q9NRZ5](https://www.uniprot.org/uniprotkb/Q9NRZ5) · Ensembl [ENSG00000026652](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000026652)

## Data

Gene col 373: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 373); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 373, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 373]; `tensor/DDL_lfc|DDL_z.npy` [373]; `embed/gene_vectors.npy` [373]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 373 or target_col == 373). Every well: [[AGPAT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGPAT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
