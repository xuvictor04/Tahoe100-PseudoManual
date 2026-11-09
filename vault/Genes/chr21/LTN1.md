---
symbol: "LTN1"
type: "gene"
col: 12713
ensembl_id: "ENSG00000198862"
name: "listerin E3 ubiquitin protein ligase 1"
location: "21q21.3"
module: 41
arm: "+"
pooled_cpm: 140.14
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# LTN1

*listerin E3 ubiquitin protein ligase 1* — 21q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.24× (z +11.8, q 1e-29, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.705× (z -6.8, q 7e-09, down in 31 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.783× (z -6.7, q 7e-09, down in 29 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UFSP2]] (+0.65, fdr 7e-06), [[UBE4A]] (+0.65, fdr 9e-06), [[MED8]] (+0.63, fdr 8e-05); moves opposite to [[MEMO1]] (-0.58, fdr 2e-05), [[ARGLU1]] (-0.55, fdr 1e-04), [[ANKRD10]] (-0.54, fdr 2e-04).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12713.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.24×** | +11.8 | 1e-29 | 45/49 (COLO 205, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +11.1 | 6e-26 | 37/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +8.7 | 6e-16 | 39/48 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.20×** | +8.0 | 3e-13 | 38/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +7.3 | 3e-11 | 34/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +5.7 | 1e-06 | 39/48 (SW480, A-427, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.31×** | +5.1 | 2e-05 | 31/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.28×** | +4.8 | 1e-04 | 31/48 (SW48, A-427, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +4.4 | 5e-04 | 27/48 (HT-29, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.24×** | +4.2 | 0.001 | 24/48 (PANC-1, HepG2/C3A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.22×** | +3.7 | 0.009 | 24/48 (NCI-H1573, A-427, …) | rises with dose | composition shift |
| [[Terfenadine (drug)]] 5 µM |  | 1.12× | +3.1 | 0.085 | 1/48 (LOX-IMVI) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.11 | 15/48 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12713.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.705×** | -6.8 | 7e-09 | 31/49 (H4, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.783×** | -6.7 | 7e-09 | 29/49 (A498, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.695×** | -6.5 | 2e-08 | 26/45 (A-427, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.731×** | -5.8 | 9e-07 | 27/44 (NCI-H1573, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.663×** | -5.7 | 2e-06 | 40/48 (HCT15, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.815×** | -5.6 | 2e-06 | 29/48 (NCI-H2347, SHP-77, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.760×** | -5.1 | 3e-05 | 30/48 (C32, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.803×** | -4.2 | 0.002 | 32/49 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.800×** | -4.2 | 0.002 | 27/50 (C32, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | 0.837× | -3.4 | 0.034 | 20/48 (HS-578T, SNU-423, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.841× | -3.3 | 0.043 | 20/48 (A-427, PANC-1, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.888× | -3.2 | 0.057 | 13/48 (C32, SW 900, …) | top dose only | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.849× | -3.2 | 0.070 | 17/49 (RKO, A498, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.851× | -3.1 | 0.071 | 15/48 (NCI-H1792, RKO, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.846× | -3.1 | 0.071 | 16/47 (HCT15, C-33 A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12713. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 160 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +20.2) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -13.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 200 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -13.6) |
| [[LS 180 (line)]] | wt | 106 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.343× (z -9.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 171 | 3 | 1 | [[TAK-901 (drug)]] 5 µM 3.24× (z +9.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -9.0) |
| [[A-427 (line)]] | wt | 107 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -15.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 269 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -15.3) |
| [[CFPAC-1 (line)]] | alt | 170 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.430× (z -11.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 139 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.22× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -8.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 82.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 132 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.4) | — |
| [[NCI-H460 (line)]] | wt | 102 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 97.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +12.2) | — |
| [[RKO (line)]] | wt | 116 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.80× (z +10.8) | — |
| [[C-33 A (line)]] | alt | 114 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +8.8) | — |
| [[H4 (line)]] | wt | 226 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -8.9) |
| [[HCT15 (line)]] | alt | 238 | 0 | 2 (1 ⚠) | — | [[Ipatasertib (drug)]] 0.5 µM 0.245× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 90.0 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.60× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 180 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.1) | — |
| [[RPMI-7951 (line)]] | alt | 165 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.09× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 159 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -9.6) |
| [[A549 (line)]] | wt | 91.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.3) | — |
| [[AN3 CA (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -10.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 146 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -11.7) |
| [[HepG2_C3A (line)]] | wt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 137 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.68× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 84.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.9) | — |
| [[hTERT-HPNE (line)]] | wt | 138 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -8.8) |
| [[KATO III (line)]] | alt | 91.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -11.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 234 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.56× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 142 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.4) | — |
| [[SK-MEL-2 (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.460× (z -8.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 81.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.9) | — |
| [[A-172 (line)]] | wt | 179 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 120 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 163 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 134 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12713), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UFSP2]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[UBE4A]] | +0.65 | +0.62 / +0.57 | both halves | 9e-06 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[MED8]] | +0.63 | +0.69 / +0.37 | both halves | 8e-05 |  |
| [[SPTY2D1]] | +0.61 | +0.73 / +0.43 | both halves | 3e-05 |  |
| [[DHX40]] | +0.61 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[RARS1]] | +0.61 | +0.73 / +0.29 | both halves | 3e-04 |  |
| [[COPB1]] | +0.60 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[ZMYM6]] | +0.60 | +0.66 / +0.34 | both halves | 1e-04 |  |
| [[GOLGA5]] | +0.60 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[NELFE]] | +0.59 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[SUCO]] | +0.59 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[KDELR3]] | +0.59 | +0.57 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEMO1]] | -0.58 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[ARGLU1]] | -0.55 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[ANKRD10]] | -0.54 | -0.58 / -0.29 | both halves | 2e-04 |  |
| [[PSPC1]] | -0.53 | -0.60 / -0.28 | both halves | 3e-04 |  |
| [[ARHGEF11]] | -0.52 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[CUEDC1]] | -0.52 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[PRRC2B]] | -0.50 | -0.49 / -0.26 | both halves | 4e-04 |  |
| [[RUFY3]] | -0.50 | -0.51 / -0.24 | both halves | 4e-04 |  |
| [[POU6F1]] | -0.50 | -0.42 / -0.28 | both halves | 3e-04 |  |
| [[ADGRA3]] | -0.50 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[CPNE8]] | -0.49 | -0.37 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises LTN1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (8.2, -35.1); signed map (-52.9, 16.8). **Vector** length 99.7, 31.3% of its response variance represented; |z| ≥ 3 in 1,119 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +4.8 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +4.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +4.3 | +5.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.2 | +5.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.2 | +11.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.2 | +0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.0 | +1.2 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.8 | +3.1 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -5.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -4.6 | +4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | +2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -5.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.6 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | listerin E3 ubiquitin protein ligase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.3 — chr21:28,928,144-28,992,956 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0714, FLJ11053, LISTERIN; previously C21orf98, C21orf10, ZNF294, RNF160 |
| Gene groups (HGNC) | Ring finger proteins; Armadillo like helical domain containing; RING finger E3 ubiquitin protein ligases |
| Reactome | 6 pathways, smallest: Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide; Ribosome-associated quality control; Antigen processing: Ubiquitination & Proteasome degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [O94822](https://www.uniprot.org/uniprotkb/O94822) (E3 ubiquitin-protein ligase listerin):

> E3 ubiquitin-protein ligase component of the ribosome quality control complex (RQC), a ribosome-associated complex that mediates ubiquitination and extraction of incompletely synthesized nascent chains for proteasomal degradation. Within the RQC complex, LTN1 is recruited to stalled 60S ribosomal subunits by NEMF and mediates ubiquitination of stalled nascent chains. Ubiquitination leads to VCP/p97 recruitment for extraction and degradation of the incomplete translation product (By similarity).

**Summary**, from NCBI Gene [26046](https://www.ncbi.nlm.nih.gov/gene/26046):

> Like most RING finger proteins, LTN1 functions as an E3 ubiquitin ligase (Chu et al., 2009 [PubMed 19196968]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:13082](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13082) · Entrez [26046](https://www.ncbi.nlm.nih.gov/gene/26046) · UniProt [O94822](https://www.uniprot.org/uniprotkb/O94822) · Ensembl [ENSG00000198862](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198862)

## Data

Gene col 12713: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12713); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12713, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12713]; `tensor/DDL_lfc|DDL_z.npy` [12713]; `embed/gene_vectors.npy` [12713]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12713 or target_col == 12713). Every well: [[LTN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LTN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
