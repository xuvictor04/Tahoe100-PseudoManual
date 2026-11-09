---
symbol: "ATG5"
type: "gene"
col: 650
ensembl_id: "ENSG00000057663"
name: "autophagy related 5"
location: "6q21"
module: 199
arm: "+"
pooled_cpm: 109.76
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/199"]
generated_by: "tahoemap"
---

# ATG5

*autophagy related 5* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.94× (z +14.7, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.650× (z -12.9, q 1e-35, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAFAH1B2]] (+0.72, fdr 7e-06), [[GTF2E2]] (+0.65, fdr 2e-05), [[CTNNBL1]] (+0.64, fdr 6e-05); moves opposite to [[GALNT7-DT]] (-0.62, fdr 1e-04), [[THAP2]] (-0.61, fdr 5e-05), [[KDM6B]] (-0.61, fdr 1e-05).
> It is in [[Module 199]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 650.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.94×** | +14.7 | 0e+00 | 47/49 (SW480, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.46×** | +9.6 | 1e-19 | 42/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.38×** | +6.7 | 3e-09 | 40/48 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.30×** | +5.6 | 3e-06 | 31/48 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.25×** | +4.4 | 0.001 | 25/48 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.23×** | +4.3 | 0.001 | 25/48 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.22×** | +4.3 | 0.002 | 24/48 (A-427, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.002 | 23/48 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.005 | 23/48 (A-427, PANC-1, …) | rises with dose |  |
| [[Tadalafil (drug)]] 5 µM |  | 1.16× | +3.0 | 0.15 | 11/48 (A-172, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 650.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.650×** | -12.9 | 1e-35 | 43/49 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.545×** | -12.9 | 1e-35 | 46/49 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.541×** | -12.5 | 1e-33 | 37/44 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.572×** | -11.0 | 7e-26 | 39/45 (A-427, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.782×** | -7.4 | 2e-11 | 28/48 (LoVo, SNU-423, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.750×** | -5.9 | 4e-07 | 29/48 (LoVo, PANC-1, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.779×** | -5.1 | 2e-05 | 31/50 (NCI-H2030, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.792×** | -5.0 | 5e-05 | 31/48 (LoVo, HS-578T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.793×** | -4.7 | 1e-04 | 30/47 (SW1417, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.834× | -3.9 | 0.006 | 22/48 (NCI-H2347, A498, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | 0.836× | -3.8 | 0.007 | 22/48 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.713×** | -3.6 | 0.013 | 17/38 (HEC-1-A, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.849× | -3.3 | 0.034 | 19/49 (A549, AsPC-1, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.855× | -3.3 | 0.034 | 12/48 (Hs 766T, HEC-1-A, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.779×** | -3.0 | 0.092 | 17/48 (HepG2/C3A, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 650. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 132 | 0 | 7 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.306× (z -15.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -10.0) |
| [[PANC-1 (line)]] | alt | 171 | 3 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.87× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.424× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -13.5) |
| [[SW1417 (line)]] | alt | 144 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.91× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -10.0) |
| [[SW480 (line)]] | alt | 115 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.32× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.449× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.644× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 120 | 3 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.11× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 104 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.70× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -13.3) |
| [[HOP62 (line)]] | alt | 81.6 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.00× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -10.4) |
| [[HS-578T (line)]] | alt | 111 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 111 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.50× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 191 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -12.4) |
| [[SNU-423 (line)]] | alt | 116 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.97× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -13.3) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -11.7) |
| [[A-427 (line)]] | wt | 120 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.27× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.0809× (z -32.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 97.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -14.5) |
| [[KATO III (line)]] | alt | 152 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.47× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -12.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 159 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.39× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -15.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 86.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.421× (z -10.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 87.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -10.2) |
| [[RKO (line)]] | wt | 112 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.72× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -14.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 93.0 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.62× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -11.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 121 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.10× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.0927× (z -22.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 83.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.610× (z -9.2) |
| [[AN3 CA (line)]] | alt | 178 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -11.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 78.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.98× (z +9.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.385× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 107 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.01× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -13.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 103 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 102 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.36× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.419× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 130 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.57× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -15.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 61.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.374× (z -10.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -13.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 97.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0990× (z -13.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 68.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.8× (z +10.6) | — |
| [[HCT15 (line)]] | alt | 87.2 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0859× (z -11.7) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 84.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.00× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.402× (z -10.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 74.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 90.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.62× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.426× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 101 | 0 | 1 | — | [[Ligustrazine (drug)]] 0.05 µM 0.0693× (z -10.0) |
| [[SW48 (line)]] | wt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -10.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 84.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 70.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 78.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 88.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 650), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAFAH1B2]] | +0.72 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[GTF2E2]] | +0.65 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[CTNNBL1]] | +0.64 | +0.71 / +0.39 | both halves | 6e-05 |  |
| [[SDHB]] | +0.64 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[STRAP]] | +0.63 | +0.74 / +0.41 | both halves | 4e-05 |  |
| [[TMEM161B]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[POMGNT2]] | +0.62 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[NAPG]] | +0.61 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[TAF5L]] | +0.61 | +0.71 / +0.27 | both halves | 3e-04 |  |
| [[FBXW2]] | +0.60 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[VTA1]] | +0.60 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[LMTK2]] | +0.60 | +0.56 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNT7-DT]] | -0.62 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[THAP2]] | -0.61 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[KDM6B]] | -0.61 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[ZC3H6]] | -0.60 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[KRBOX5]] | -0.59 | -0.65 / -0.36 | both halves | 1e-04 |  |
| [[ENO3]] | -0.59 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[AKT1S1]] | -0.58 | -0.62 / -0.29 | both halves | 2e-04 |  |
| [[NOTCH2NLB]] | -0.58 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[ERF]] | -0.58 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[MEPCE]] | -0.58 | -0.61 / -0.32 | both halves | 1e-04 |  |
| [[NEK8]] | -0.58 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[ZNF638]] | -0.57 | -0.59 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ATG5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers ATG5's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 199]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.758). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.0, 11.6); signed map (-40.5, -9.0). **Vector** length 97.9, 27.5% of its response variance represented; |z| ≥ 3 in 1,001 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.5 | +5.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.7 | +6.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +14.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.8 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +3.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.0 | +0.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.0 | -0.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -10.1 | -7.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -7.8 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -6.7 | -3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -12.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -4.2 | -5.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -1.8 |
|  | [[Pentamidine (isethionate) (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | autophagy related 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:106,045,423-106,325,791 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ASP, APG5, hAPG5; previously APG5L |
| Gene groups (HGNC) | Autophagy related; Atypical E3 ubiquitin ligases |
| Reactome | 9 pathways, smallest: Receptor Mediated Mitophagy; PINK1-PRKN Mediated Mitophagy; Negative regulators of DDX58/IFIH1 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1Y0](https://www.uniprot.org/uniprotkb/Q9H1Y0) (Autophagy protein 5):

> Involved in autophagic vesicle formation. Conjugation with ATG12, through a ubiquitin-like conjugating system involving ATG7 as an E1-like activating enzyme and ATG10 as an E2-like conjugating enzyme, is essential for its function. The ATG12-ATG5 conjugate acts as an E3-like enzyme which is required for lipidation of ATG8 family proteins and their association to the vesicle membranes. Involved in mitochondrial quality control after oxidative damage, and in subsequent cellular longevity. Plays a …

**Summary**, from NCBI Gene [9474](https://www.ncbi.nlm.nih.gov/gene/9474):

> The protein encoded by this gene, in combination with autophagy protein 12, functions as an E1-like activating enzyme in a ubiquitin-like conjugating system. The encoded protein is involved in several cellular processes, including autophagic vesicle formation, mitochondrial quality control after oxidative damage, negative regulation of the innate antiviral immune response, lymphocyte development and proliferation, MHC II antigen presentation, adipocyte differentiation, and apoptosis. Several …

**Accessions** — [HGNC:589](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:589) · Entrez [9474](https://www.ncbi.nlm.nih.gov/gene/9474) · UniProt [Q9H1Y0](https://www.uniprot.org/uniprotkb/Q9H1Y0) · Ensembl [ENSG00000057663](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000057663)

## Data

Gene col 650: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 650); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 650, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 650]; `tensor/DDL_lfc|DDL_z.npy` [650]; `embed/gene_vectors.npy` [650]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 650 or target_col == 650). Every well: [[ATG5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATG5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
