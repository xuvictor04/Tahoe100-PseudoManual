---
symbol: "ARFIP1"
type: "gene"
col: 8882
ensembl_id: "ENSG00000164144"
name: "ARF interacting protein 1"
location: "4q31.3"
module: 12
arm: "+"
pooled_cpm: 100.97
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# ARFIP1

*ARF interacting protein 1* — 4q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.16× (z +9.1, q 7e-17, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.527× (z -15.7, q 0e+00, down in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.754× (z -9.8, q 1e-20, down in 33 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 0.162×, HCT15 0.154×, LoVo 0.248×, SHP-77 0.149×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A-427 0.208×, SW 900 0.223×, LoVo 0.335×, NCI-H1573 0.349×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A498 0.543×, SW 900 0.500×, A549 0.569×, NCI-H2347 0.615×); [[Auranofin (drug)]] 5 µM in 2 lines (A-172 0.413×, C32 0.406×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SW 1271 0.0843×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA8]] (+0.69, fdr 7e-06), [[MBD5]] (+0.59, fdr 9e-06), [[VTA1]] (+0.59, fdr 2e-05); moves opposite to [[B3GALNT2]] (-0.50, fdr 8e-05), [[PRDM11]] (-0.48, fdr 1e-04), [[ATN1]] (-0.46, fdr 9e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8882.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.16×** | +9.1 | 7e-17 | 41/49 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +7.5 | 1e-11 | 27/48 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +7.1 | 3e-10 | 29/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +6.9 | 1e-09 | 30/48 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.55×** | +5.2 | 3e-05 | 28/48 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.22×** | +5.0 | 7e-05 | 24/49 (PANC-1, SW1417, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.11× | +3.8 | 0.013 | 15/48 (SW1417, KATO III, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.16× | +3.7 | 0.013 | 17/48 (PANC-1, KATO III, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.6 | 0.020 | 7/48 (SNU-1, LOX-IMVI, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.041 | 13/49 (SK-MEL-2, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.0 | 0.13 | 14/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8882.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 0.162×, HCT15 0.154×, LoVo 0.248×, SHP-77 0.149×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A-427 0.208×, SW 900 0.223×, LoVo 0.335×, NCI-H1573 0.349×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A498 0.543×, SW 900 0.500×, A549 0.569×, NCI-H2347 0.615×); [[Auranofin (drug)]] 5 µM in 2 lines (A-172 0.413×, C32 0.406×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SW 1271 0.0843×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.527×** | -15.7 | 0e+00 | 44/49 (A-427, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.513×** | -15.6 | 0e+00 | 42/44 (KATO III, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.484×** | -11.0 | 6e-26 | 38/45 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.754×** | -9.8 | 1e-20 | 33/49 (A498, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.766×** | -6.6 | 6e-09 | 35/48 (HS-578T, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **0.774×** | -6.0 | 2e-07 | 28/47 (AsPC-1, NCI-H1573, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.780×** | -5.8 | 5e-07 | 29/47 (COLO 205, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.800×** | -5.5 | 3e-06 | 27/48 (COLO 205, H4, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.835× | -4.4 | 6e-04 | 22/48 (A-172, C32, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.868× | -3.5 | 0.027 | 12/47 (A-172, CFPAC-1, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.790×** | -3.4 | 0.035 | 15/47 (Hs 766T, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.876× | -3.2 | 0.055 | 18/48 (J82, AsPC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.874× | -3.1 | 0.073 | 20/50 (A-172, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8882. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 88.9 | 1 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.76× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -15.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 84.8 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 1.94× (z +8.6) | [[Auranofin (drug)]] 5 µM 0.413× (z -11.6) |
| [[LoVo (line)]] | wt | 115 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -20.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 123 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.96× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.496× (z -10.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 139 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -12.3) |
| [[COLO 205 (line)]] | alt | 186 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -13.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 123 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -10.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 124 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -24.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 158 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -16.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 147 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -11.2) |
| [[A-427 (line)]] | wt | 85.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -19.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 122 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.406× (z -10.3) |
| [[HOP62 (line)]] | alt | 103 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.474× (z -10.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 89.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -10.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 145 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -17.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 74.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.542× (z -9.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 129 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -10.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 77.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -10.0) |
| [[AN3 CA (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -15.5) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -11.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 82.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.394× (z -9.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 92.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -17.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 147 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.394× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HCT15 (line)]] | alt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -20.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.433× (z -12.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -10.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 61.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.456× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.453× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 94.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.615× (z -9.4) |
| [[RKO (line)]] | wt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -13.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 63.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -18.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -15.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 93.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -10.2) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0715× (z -11.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 102 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0843× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 79.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 90.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 88.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8882), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA8]] | +0.69 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[MBD5]] | +0.59 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[VTA1]] | +0.59 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[UBR1]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[DAD1]] | +0.55 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[PIBF1]] | +0.54 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[MAGEF1]] | +0.54 | +0.37 / +0.49 | both halves | 9e-05 |  |
| [[RARS1]] | +0.53 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[UBE4A]] | +0.52 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[CSTPP1]] | +0.52 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[NDUFB3]] | +0.52 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[POLR3A]] | +0.52 | +0.52 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GALNT2]] | -0.50 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[PRDM11]] | -0.48 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[ATN1]] | -0.46 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[UBE2Q2]] | -0.45 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[UBQLN4]] | -0.44 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[PGM5P2-1]] | -0.44 | -0.29 / -0.38 | both halves | 2e-04 |  |
| [[ANKRD10]] | -0.44 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[MAN2A2]] | -0.44 | -0.40 / -0.29 | both halves | 3e-04 |  |
| [[TBKBP1]] | -0.43 | -0.43 / -0.29 | both halves | 2e-04 |  |
| [[PHF2]] | -0.43 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[RUSC1-AS1]] | -0.43 | -0.36 / -0.28 | both halves | 3e-04 |  |
| [[CROCC]] | -0.43 | -0.36 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ARFIP1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.380). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.2, -6.9); signed map (-8.1, -6.7). **Vector** length 84.7, 20.3% of its response variance represented; |z| ≥ 3 in 898 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.4 | +9.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +5.0 | +3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +0.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +3.8 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | -0.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.2 | +1.0 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.1 | -2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.6 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.1 | -11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -15.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Neratinib (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | ARF interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.3 — chr4:152,779,937-152,918,463 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSU52521 |
| Gene groups (HGNC) | AH domain containing |
| Hallmark sets | PROTEIN_SECRETION |
| Matched by | ensembl_id |

**Function**, from UniProt [P53367](https://www.uniprot.org/uniprotkb/P53367) (Arfaptin-1):

> Plays a role in controlling biogenesis of secretory granules at the trans-Golgi network. Mechanistically, binds ARF-GTP at the neck of a growing secretory granule precursor and forms a protective scaffold. Once the granule precursor has been completely loaded, active PRKD1 phosphorylates ARFIP1 and releases it from ARFs. In turn, ARFs induce fission. Through this mechanism, ensures proper secretory granule formation at the Golgi of pancreatic beta cells.

**Summary**, from NCBI Gene [27236](https://www.ncbi.nlm.nih.gov/gene/27236):

> Enables phosphatidylinositol-4-phosphate binding activity. Involved in negative regulation of retrograde transport, endosome to Golgi. Acts upstream of or within intracellular protein transport and regulation of protein secretion. Located in Golgi membrane; cytosol; and trans-Golgi network membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21496](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21496) · Entrez [27236](https://www.ncbi.nlm.nih.gov/gene/27236) · UniProt [P53367](https://www.uniprot.org/uniprotkb/P53367) · Ensembl [ENSG00000164144](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164144)

## Data

Gene col 8882: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8882); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8882, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8882]; `tensor/DDL_lfc|DDL_z.npy` [8882]; `embed/gene_vectors.npy` [8882]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8882 or target_col == 8882). Every well: [[ARFIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARFIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
