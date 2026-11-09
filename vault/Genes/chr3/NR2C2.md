---
symbol: "NR2C2"
type: "gene"
col: 10824
ensembl_id: "ENSG00000177463"
name: "nuclear receptor subfamily 2 group C member 2"
location: "3p25.1"
module: 15
arm: "+"
pooled_cpm: 104.19
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 22
n_dd_up_clean: 6
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# NR2C2

*nuclear receptor subfamily 2 group C member 2* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.34× (z +7.8, q 3e-12, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.545× (z -23.2, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAF4]] (+0.69, fdr 7e-06), [[PRDM10]] (+0.67, fdr 2e-05), [[LEMD3]] (+0.63, fdr 1e-05); moves opposite to [[NUDT12]] (-0.59, fdr 1e-05), [[NDUFA5]] (-0.57, fdr 1e-05), [[ALAS1]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PPP1R3C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10824.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +7.8 | 3e-12 | 32/48 (SNU-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +7.2 | 2e-10 | 31/48 (SNU-1, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +6.9 | 1e-09 | 31/48 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +5.8 | 1e-06 | 26/48 (NCI-H460, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +5.7 | 1e-06 | 26/47 (RPMI-7951, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.39×** | +4.7 | 3e-04 | 25/49 (LoVo, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.3 | 0.001 | 15/48 (NCI-H23, H4, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.16× | +3.7 | 0.013 | 17/47 (HOP62, LoVo, …) | rises with dose |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.13× | +3.4 | 0.042 | 7/48 (RKO, CFPAC-1, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.4 | 0.042 | 20/50 (SW480, C32, …) | rises with dose |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.13× | +3.2 | 0.078 | 7/48 (HS-578T, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10824.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.545×** | -23.2 | 0e+00 | 43/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.427×** | -23.0 | 0e+00 | 47/48 (AsPC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.469×** | -20.4 | 0e+00 | 47/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.477×** | -20.0 | 0e+00 | 47/48 (NCI-H23, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.570×** | -14.6 | 0e+00 | 35/44 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.576×** | -14.3 | 2e-44 | 37/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.540×** | -14.1 | 3e-43 | 41/49 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.596×** | -14.0 | 2e-42 | 42/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.706×** | -9.4 | 5e-19 | 39/48 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.712×** | -9.2 | 3e-18 | 36/48 (HT-29, SNU-423, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.717×** | -9.0 | 1e-17 | 34/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.803×** | -8.4 | 2e-15 | 31/48 (A-427, CHP-212, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.717×** | -8.3 | 5e-15 | 33/45 (J82, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.762×** | -7.1 | 7e-11 | 29/47 (NCI-H2030, SW1417, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.744×** | -6.8 | 5e-10 | 27/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.819×** | -5.4 | 2e-06 | 25/48 (COLO 205, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.696×** | -5.1 | 1e-05 | 26/47 (HCT15, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.838× | -4.8 | 5e-05 | 22/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.720×** | -4.6 | 9e-05 | 22/48 (KATO III, SW1417, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10824. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 118 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -35.6) |
| [[SW480 (line)]] | alt | 117 | 0 | 11 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.402× (z -16.9) |
| [[HEC-1-A (line)]] | alt | 148 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -29.0) |
| [[HOP62 (line)]] | alt | 131 | 1 (1 ⚠) | 8 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.01× (z +9.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -22.0) |
| [[NCI-H23 (line)]] | alt | 152 | 0 | 9 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.303× (z -17.9) |
| [[A-427 (line)]] | wt | 122 | 0 | 8 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.361× (z -14.0) |
| [[HS-578T (line)]] | alt | 104 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -25.2) |
| [[J82 (line)]] | alt | 151 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.508× (z -14.2) |
| [[LOX-IMVI (line)]] | wt | 150 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -19.6) |
| [[Panc 03.27 (line)]] | alt | 95.3 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -13.4) |
| [[PANC-1 (line)]] | alt | 113 | 1 | 7 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.474× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 153 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0919× (z -31.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.457× (z -15.3) |
| [[SW1417 (line)]] | alt | 119 | 1 (1 ⚠) | 7 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.460× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 90.7 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.338× (z -14.4) |
| [[NCI-H1573 (line)]] | alt | 137 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -16.4) |
| [[NCI-H1792 (line)]] | alt | 108 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -18.1) |
| [[SNU-423 (line)]] | alt | 90.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -19.5) |
| [[HT-29 (line)]] | alt | 93.6 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.381× (z -12.0) |
| [[RKO (line)]] | wt | 103 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -14.9) |
| [[SNU-1 (line)]] | wt | 95.7 | 3 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.180× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.345× (z -10.0) |
| [[A498 (line)]] | wt | 59.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -21.5) |
| [[NCI-H2030 (line)]] | alt | 110 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -15.1) |
| [[A549 (line)]] | wt | 112 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.488× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 101 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.221× (z -19.9) |
| [[BT-474 (line)]] | alt | 79.5 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.233× (z -14.2) |
| [[HepG2_C3A (line)]] | wt | 112 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.297× (z -12.6) |
| [[hTERT-HPNE (line)]] | wt | 89.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -16.7) |
| [[LoVo (line)]] | wt | 102 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -12.6) |
| [[NCI-H2347 (line)]] | alt | 92.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 83.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.566× (z -13.1) |
| [[SW 900 (line)]] | alt | 85.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.410× (z -10.7) |
| [[C-33 A (line)]] | alt | 119 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.383× (z -10.4) |
| [[SHP-77 (line)]] | alt | 93.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.368× (z -11.5) |
| [[SW48 (line)]] | wt | 94.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -13.7) |
| [[LS 180 (line)]] | wt | 89.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -11.0) |
| [[C32 (line)]] | wt | 74.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -10.1) |
| [[CHP-212 (line)]] | wt | 68.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.229× (z -11.9) |
| [[COLO 205 (line)]] | alt | 79.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +9.4) | — |
| [[KATO III (line)]] | alt | 81.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.474× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW 1271 (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0957× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[AN3 CA (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 83.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 76.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10824), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF4]] | +0.69 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[PRDM10]] | +0.67 | +0.76 / +0.48 | both halves | 2e-05 |  |
| [[LEMD3]] | +0.63 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[SFMBT1]] | +0.62 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[KIAA2026]] | +0.62 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[MCM9]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ARHGEF11]] | +0.61 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[GATD1-DT]] | +0.61 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[KIAA0232]] | +0.60 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[ZNF718]] | +0.60 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[FANCC]] | +0.59 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[ARIH2]] | +0.59 | +0.64 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT12]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[NDUFA5]] | -0.57 | -0.70 / -0.57 | both halves | 1e-05 |  |
| [[ALAS1]] | -0.57 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[TTC5]] | -0.56 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[DDX1]] | -0.56 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[BBS5]] | -0.55 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[CREB3]] | -0.54 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[MRPS31P4]] | -0.53 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[NOCT]] | -0.53 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[PPP1R3C]] | -0.52 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[RIOK2]] | -0.52 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[ZNF205]] | -0.52 | -0.56 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R3C]] | B | PPP1R3C activity lowers NR2C2's level | lines that do not express PPP1R3C (22) vs lines expressing it (28) | 1.13× higher at baseline in the lines without PPP1R3C | 0.062 | ⚠ within organs, on part of the lines; also absent: CDH2, SSTR2, IDO1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.455). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-9.8, 19.6); signed map (6.3, -1.7). **Vector** length 106, 31.8% of its response variance represented; |z| ≥ 3 in 1,266 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.9 | +0.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +8.6 | +1.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.4 | +3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.7 | +6.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.9 | +7.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.8 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | -0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.8 | +4.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | -0.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.3 | -23.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.7 | -14.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -14.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.0 | -8.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.8 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -4.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.4 | -0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -4.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.2 | -4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor subfamily 2 group C member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:14,947,583-15,053,600 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAK1, TR2R1, hTAK1; previously TR4 |
| Gene groups (HGNC) | Nuclear receptor subfamily 2 group C |
| Reactome | 7 pathways, smallest: Interaction of NuRD complexes with transcription factors; NuRD complex assembly; Nuclear Receptor transcription pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P49116](https://www.uniprot.org/uniprotkb/P49116) (Nuclear receptor subfamily 2 group C member 2):

> Orphan nuclear receptor that can act as a repressor or activator of transcription. An important repressor of nuclear receptor signaling pathways such as retinoic acid receptor, retinoid X, vitamin D3 receptor, thyroid hormone receptor and estrogen receptor pathways. May regulate gene expression during the late phase of spermatogenesis. Together with NR2C1, forms the core of the DRED (direct repeat erythroid-definitive) complex that represses embryonic and fetal globin transcription including …

**Summary**, from NCBI Gene [7182](https://www.ncbi.nlm.nih.gov/gene/7182):

> This gene encodes a protein that belongs to the nuclear hormone receptor family. Members of this family act as ligand-activated transcription factors and function in many biological processes such as development, cellular differentiation and homeostasis. The activated receptor/ligand complex is translocated to the nucleus where it binds to hormone response elements of target genes. The protein encoded by this gene plays a role in protecting cells from oxidative stress and damage induced by …

**Accessions** — [HGNC:7972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7972) · Entrez [7182](https://www.ncbi.nlm.nih.gov/gene/7182) · UniProt [P49116](https://www.uniprot.org/uniprotkb/P49116) · Ensembl [ENSG00000177463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177463)

## Data

Gene col 10824: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10824); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10824, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10824]; `tensor/DDL_lfc|DDL_z.npy` [10824]; `embed/gene_vectors.npy` [10824]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10824 or target_col == 10824). Every well: [[NR2C2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR2C2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
