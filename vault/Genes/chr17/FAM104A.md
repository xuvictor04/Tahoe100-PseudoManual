---
symbol: "FAM104A"
type: "gene"
col: 5428
ensembl_id: "ENSG00000133193"
name: "VCP nuclear cofactor family member 1"
location: "17q25.1"
module: 30
arm: "+"
pooled_cpm: 33.96
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# FAM104A

*VCP nuclear cofactor family member 1* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.13× (z +15.9, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.498× (z -18.0, q 0e+00, down in 29 of 38 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (NCI-H460 0.253×, SHP-77 0.191×, H4 0.112×, LOX-IMVI 0.242×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (KATO III 0.0887×, NCI-H23 0.188×, HEC-1-A 0.275×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (Hs 766T 0.232×, NCI-H2347 0.395×, SW480 0.464×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POMGNT2]] (+0.70, fdr 1e-05), [[JKAMP]] (+0.69, fdr 8e-06), [[ASB7]] (+0.67, fdr 1e-05); moves opposite to [[PSMD6-AS1]] (-0.68, fdr 1e-05), [[ST7L]] (-0.67, fdr 1e-05), [[TIA1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PLEKHF1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5428.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.13×** | +15.9 | 0e+00 | 45/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.56×** | +13.1 | 9e-37 | 36/48 (SW480, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +12.7 | 8e-35 | 39/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +10.7 | 9e-25 | 33/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +10.7 | 9e-25 | 37/48 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +8.5 | 2e-15 | 32/48 (SW480, A498, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +8.1 | 5e-14 | 28/47 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +7.9 | 2e-13 | 28/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +7.3 | 2e-11 | 26/48 (A498, C32, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +7.1 | 8e-11 | 23/48 (PANC-1, A498, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +6.8 | 7e-10 | 26/48 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.14× | +4.8 | 9e-05 | 12/48 (CFPAC-1, NCI-H1573, …) | top dose only | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.002 | 5/48 (HOP62, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.16× | +4.0 | 0.002 | 19/46 (SW48, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.7 | 0.008 | 12/48 (HOP62, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.15× | +3.5 | 0.017 | 13/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.021 | 12/47 (NCI-H2347, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.12× | +2.9 | 0.095 | 3/48 (SK-MEL-2, J82, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5428.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (NCI-H460 0.253×, SHP-77 0.191×, H4 0.112×, LOX-IMVI 0.242×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (KATO III 0.0887×, NCI-H23 0.188×, HEC-1-A 0.275×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (Hs 766T 0.232×, NCI-H2347 0.395×, SW480 0.464×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.498×** | -18.0 | 0e+00 | 29/38 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.544×** | -16.3 | 0e+00 | 34/44 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.660×** | -10.3 | 1e-22 | 26/42 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.906× | -3.8 | 0.021 | 18/47 (NCI-H23, A-172, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.866× | -3.7 | 0.023 | 16/48 (A-172, hTERT-HPNE, …) | top dose only | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | 0.874× | -3.5 | 0.043 | 7/47 (AN3 CA, NCI-H2347, …) | top dose only | position effect removed |
| [[Thymol (drug)]] 5 µM |  | 0.919× | -3.2 | 0.096 | 6/48 (MIA PaCa-2, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5428. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 40.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -11.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 42.4 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.83× (z +11.0) | — |
| [[KATO III (line)]] | alt | 40.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0887× (z -23.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 41.0 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.36× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.464× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 32.0 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.24× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -10.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LOX-IMVI (line)]] | wt | 40.9 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.37× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 36.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 26.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +9.0) ⚠ cell-cycle shift, explains ~39% of this change | [[Dinaciclib (drug)]] 5 µM 0.253× (z -15.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 47.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -12.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -18.0) ⚠ cell-cycle shift, explains ~73% of this change |
| [[A498 (line)]] | wt | 38.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.03× (z +10.8) | — |
| [[A549 (line)]] | wt | 38.9 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +9.3) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[BT-474 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -10.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -10.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -9.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 45.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -8.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[H4 (line)]] | wt | 41.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -14.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -13.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 38.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -10.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 24.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -11.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -8.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -9.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -11.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.358× (z -8.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 46.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -15.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 53.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -10.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -8.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5428), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POMGNT2]] | +0.70 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[JKAMP]] | +0.69 | +0.72 / +0.57 | both halves | 8e-06 |  |
| [[ASB7]] | +0.67 | +0.69 / +0.57 | both halves | 1e-05 | STRING 718 |
| [[PDCD10]] | +0.67 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[MMS19]] | +0.66 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[CNOT8]] | +0.66 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[MED17]] | +0.66 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[MFSD9]] | +0.66 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[CGRRF1]] | +0.65 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[GRB2]] | +0.65 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[MYPOP]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[RNF121]] | +0.64 | +0.70 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD6-AS1]] | -0.68 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[ST7L]] | -0.67 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[TIA1]] | -0.63 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[NPIPB5]] | -0.63 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[NPIPB4]] | -0.61 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[PIEZO1]] | -0.60 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[CPSF2]] | -0.59 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[CACNA2D1]] | -0.59 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[FKRP]] | -0.59 | -0.59 / -0.32 | both halves | 2e-04 |  |
| [[DCAF8]] | -0.59 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[WARS2-AS1]] | -0.58 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[SDCBP2-AS1]] | -0.58 | -0.50 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHF1]] | B | PLEKHF1 activity raises FAM104A's level | lines that do not express PLEKHF1 (5) vs lines expressing it (45) | 1.35× lower at baseline in the lines without PLEKHF1 | 0.039 | ⚠ within organs, on part of the lines; also absent: E2F1, MCM10, DAGLA; maybe low, not absent |
| [[ZNF71]] | B | ZNF71 activity raises FAM104A's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 1.24× lower at baseline in the lines without ZNF71 | 0.044 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28 |
| [[RGS14]] | C | RGS14's natural level strengthens FAM104A's drug response | RGS14's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.20; direction not clear | 0.078 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.663). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-1.5, -11.6); signed map (-34.3, -7.4). **Vector** length 82.9, 15.9% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +15.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +13.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.9 | +8.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.3 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +7.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +8.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +4.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.5 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -6.7 | -3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.5 | -16.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -18.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -4.8 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.7 | -10.3 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -3.5 |
|  | [[Acetohexamide (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | VCP nuclear cofactor family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:73,207,353-73,236,753 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14775; previously FAM104A |
| Matched by | ensembl_id |

UniProt [Q969W3](https://www.uniprot.org/uniprotkb/Q969W3) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25918](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25918) · Entrez [84923](https://www.ncbi.nlm.nih.gov/gene/84923) · UniProt [Q969W3](https://www.uniprot.org/uniprotkb/Q969W3) · Ensembl [ENSG00000133193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133193)

## Data

Gene col 5428: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5428); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5428, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5428]; `tensor/DDL_lfc|DDL_z.npy` [5428]; `embed/gene_vectors.npy` [5428]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5428 or target_col == 5428). Every well: [[FAM104A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM104A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
