---
symbol: "FARP1"
type: "gene"
col: 7656
ensembl_id: "ENSG00000152767"
name: "FERM, ARH/RhoGEF and pleckstrin domain protein 1"
location: "13q32.2"
module: 59
arm: "-"
pooled_cpm: 122.3
n_lines_expressing: 45
n_dd_up: 2
n_dd_down: 16
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# FARP1

*FERM, ARH/RhoGEF and pleckstrin domain protein 1* — 13q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Demeclocycline (drug)]] 5 µM: 1.14× (z +3.7, q 0.059, up in 7 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Clobetasol propionate (drug)]] 0.05 µM in 2 lines (NCI-H1573 4.06×, hTERT-HPNE 3.60×); [[Clobetasol propionate (drug)]] 0.5 µM in 2 lines (NCI-H1573 3.92×, hTERT-HPNE 3.18×); [[Dexamethasone (drug)]] 0.5 µM in 2 lines (NCI-H1573 3.91×, hTERT-HPNE 3.14×).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.573× (z -15.4, q 0e+00, down in 33 of 43 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.568× (z -11.0, q 7e-26, down in 32 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK39]] (+0.67, fdr 7e-06), [[TTL]] (+0.65, fdr 7e-06), [[DOCK1]] (+0.62, fdr 7e-06); moves opposite to [[CIR1]] (-0.59, fdr 1e-05), [[DBP]] (-0.58, fdr 7e-06), [[AFTPH]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[VAV2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7656.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Clobetasol propionate (drug)]] 0.05 µM in 2 lines (NCI-H1573 4.06×, hTERT-HPNE 3.60×); [[Clobetasol propionate (drug)]] 0.5 µM in 2 lines (NCI-H1573 3.92×, hTERT-HPNE 3.18×); [[Dexamethasone (drug)]] 0.5 µM in 2 lines (NCI-H1573 3.91×, hTERT-HPNE 3.14×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Demeclocycline (drug)]] 5 µM |  | 1.14× | +3.7 | 0.059 | 7/43 (NCI-H2347, hTERT-HPNE, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.059 | 22/42 (SW48, H4, …) | two highest doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +3.6 | 0.059 | 18/38 (SK-MEL-2, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.18× | +3.1 | 0.28 | 14/43 (A-172, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7656.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.573×** | -15.4 | 0e+00 | 33/43 (A-172, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.568×** | -11.0 | 7e-26 | 32/43 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.570×** | -10.6 | 9e-24 | 34/43 (A-172, C32, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.408×** | -9.2 | 8e-18 | 38/44 (RKO, J82, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.438×** | -8.4 | 4e-15 | 36/43 (LoVo, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.680×** | -7.5 | 4e-12 | 26/43 (NCI-H23, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.737×** | -6.0 | 2e-07 | 29/43 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.760×** | -5.4 | 6e-06 | 25/43 (J82, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **0.761×** | -5.3 | 6e-06 | 23/43 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.796×** | -4.3 | 0.001 | 24/42 (J82, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.813×** | -4.0 | 0.003 | 24/43 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.819×** | -3.9 | 0.004 | 20/43 (J82, A549, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.819×** | -3.8 | 0.007 | 20/42 (J82, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.829×** | -3.7 | 0.010 | 19/43 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.714×** | -3.4 | 0.022 | 15/35 (Panc 03.27, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.840× | -3.4 | 0.023 | 19/44 (HOP62, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.858× | -3.0 | 0.084 | 17/43 (A-172, C32, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7656. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 117 | 14 | 4 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 4.06× (z +12.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -18.9) |
| [[J82 (line)]] | alt | 401 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -21.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.394× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 141 | 11 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 3.60× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 102 | 8 | 1 (1 ⚠) | [[Budesonide (drug)]] 5 µM 2.39× (z +10.1) | [[Harringtonine (drug)]] 5 µM 0.408× (z -10.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 90.9 | 3 | 4 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 2.33× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -21.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.337× (z -12.7) |
| [[A-172 (line)]] | wt | 228 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -25.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -18.2) |
| [[C32 (line)]] | wt | 160 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -21.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.238× (z -16.5) |
| [[NCI-H23 (line)]] | alt | 54.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -15.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.367× (z -9.2) |
| [[PANC-1 (line)]] | alt | 103 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -19.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.430× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 87.0 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.69× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -11.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.424× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 185 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.408× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.505× (z -8.8) |
| [[LoVo (line)]] | wt | 125 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -10.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 31.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.99× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 191 | 0 | 3 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0785× (z -16.7) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.251× (z -9.1) |
| [[SW48 (line)]] | wt | 134 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -15.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.357× (z -9.0) |
| [[A498 (line)]] | wt | 93.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.16× (z +8.9) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -12.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[AN3 CA (line)]] | alt | 230 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -14.2) |
| [[HS-578T (line)]] | alt | 68.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -15.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.374× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 60.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -12.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -11.8) |
| [[SW480 (line)]] | alt | 242 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.489× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.563× (z -8.6) |
| [[A-427 (line)]] | wt | 109 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.221× (z -19.8) |
| [[BT-474 (line)]] | alt | 262 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -10.2) |
| [[C-33 A (line)]] | alt | 80.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.370× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HepG2_C3A (line)]] | wt | 468 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -10.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HT-29 (line)]] | alt | 236 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.396× (z -9.0) ⚠ toxic |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.113× (z -8.8) |
| [[RKO (line)]] | wt | 152 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.139× (z -11.2) |
| [[SNU-423 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -8.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW 1088 (line)]] | alt | 105 | 0 | 1 | — | [[Nafamostat (mesylate) (drug)]] 0.05 µM 0.0764× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.7 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 144 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.1 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.9 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 76.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7656), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK39]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[TTL]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[DOCK1]] | +0.62 | +0.63 / +0.58 | both halves | 7e-06 | pathway: RAC1 GTPase cycle |
| [[RAP1GDS1]] | +0.62 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[TMTC4]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[ACOT7]] | +0.58 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[MAN2A1]] | +0.57 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[LDLRAD3]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 | same gene group |
| [[GMPS]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[TBC1D1]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[ZNF731P]] | +0.57 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[CMTM4]] | +0.56 | +0.53 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIR1]] | -0.59 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[DBP]] | -0.58 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[AFTPH]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 | same gene group |
| [[ZNF230]] | -0.54 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[ZNF226]] | -0.54 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[GOLPH3L]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[NFKBIL1]] | -0.53 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[YJU2B]] | -0.53 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[KBTBD7]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[BTN3A1]] | -0.53 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[THAP6]] | -0.53 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[LRRC27]] | -0.53 | -0.46 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VAV2]] | B | FARP1 activity raises VAV2's level | lines that do not express FARP1 (5) vs lines expressing it (45) | 2.09× lower at baseline in the lines without FARP1 | 0.027 | ⚠ within organs, on part of the lines; also absent: C5AR1, SPECC1, IGSF3 |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **-** arm (projection on the module's main direction -0.561). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-5.0, -35.0); signed map (-19.0, -49.3). **Vector** length 109, 29.4% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | +1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +3.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.1 | +1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.1 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.8 | +2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.7 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +2.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.8 | -9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -11.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.2 | -10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.7 | -15.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -8.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.4 | -2.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.1 | -0.7 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | FERM, ARH/RhoGEF and pleckstrin domain protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.2 — chr13:98,142,562-98,455,176 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDEP, PLEKHC2, MGC87400, PPP1R75, GLCC1 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Protein phosphatase 1 regulatory subunits; Dbl family Rho GEFs; FERM domain containing; MicroRNA protein coding host genes |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY, MITOTIC_SPINDLE |
| Reactome | 7 pathways, smallest: RHOF GTPase cycle; RHOA GTPase cycle; CDC42 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4F1](https://www.uniprot.org/uniprotkb/Q9Y4F1) (FERM, ARHGEF and pleckstrin domain-containing protein 1):

> Functions as a guanine nucleotide exchange factor for RAC1. May play a role in semaphorin signaling. Plays a role in the assembly and disassembly of dendritic filopodia, the formation of dendritic spines, regulation of dendrite length and ultimately the formation of synapses (By similarity).

**Summary**, from NCBI Gene [10160](https://www.ncbi.nlm.nih.gov/gene/10160):

> This gene encodes a protein containing a FERM (4.2, exrin, radixin, moesin) domain, a Dbl homology domain, and two pleckstrin homology domains. These domains are found in guanine nucleotide exchange factors and proteins that link the cytoskeleton to the cell membrane. The encoded protein functions in neurons to promote dendritic growth. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2013]

**Accessions** — [HGNC:3591](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3591) · Entrez [10160](https://www.ncbi.nlm.nih.gov/gene/10160) · UniProt [Q9Y4F1](https://www.uniprot.org/uniprotkb/Q9Y4F1) · Ensembl [ENSG00000152767](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152767)

## Data

Gene col 7656: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7656); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7656, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7656]; `tensor/DDL_lfc|DDL_z.npy` [7656]; `embed/gene_vectors.npy` [7656]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7656 or target_col == 7656). Every well: [[FARP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FARP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
