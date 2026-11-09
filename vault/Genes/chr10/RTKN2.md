---
symbol: "RTKN2"
type: "gene"
col: 11232
ensembl_id: "ENSG00000182010"
name: "rhotekin 2"
location: "10q21.2"
module: 67
arm: "+"
pooled_cpm: 33.05
n_lines_expressing: 43
n_dd_up: 14
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# RTKN2

*rhotekin 2* — 10q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.89× (z +18.7, q 0e+00, up in 21 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.19× (z +4.5, q 5e-04, up in 12 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.709× (z -8.9, q 3e-16, down in 24 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SKA1]] (+0.66, fdr 7e-06), [[CENPK]] (+0.62, fdr 1e-05), [[PBK]] (+0.61, fdr 1e-05); moves opposite to [[TADA2B]] (-0.57, fdr 1e-05), [[CDC37L1]] (-0.53, fdr 2e-05), [[ZNF7]] (-0.53, fdr 2e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF726]] → it (grade B ⚠); 4 go from it, the strongest it → [[ELOA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11232.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +18.7 | 0e+00 | 21/29 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.77×** | +18.6 | 0e+00 | 30/35 (HOP62, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.42×** | +14.9 | 0e+00 | 27/32 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.56×** | +7.8 | 7e-13 | 23/36 (NCI-H1573, SW1417, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +7.6 | 4e-12 | 22/40 (HS-578T, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.38×** | +5.9 | 4e-07 | 18/41 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.34×** | +5.3 | 1e-05 | 16/40 (NCI-H2030, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.5 | 5e-04 | 12/41 (J82, NCI-H2347, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.57×** | +4.3 | 0.001 | 13/39 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.001 | 14/40 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.55×** | +4.2 | 0.001 | 12/38 (NCI-H460, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.22×** | +3.7 | 0.011 | 13/40 (HT-29, NCI-H23, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.014 | 7/39 (PANC-1, hTERT-HPNE, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.016 | 13/41 (KATO III, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.017 | 5/36 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Methotrexate (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.055 | 6/40 (LS 180, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11232.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -8.9 | 3e-16 | 24/39 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.728×** | -8.2 | 5e-14 | 22/41 (Panc 03.27, LS 180, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.668×** | -7.4 | 2e-11 | 22/40 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.566×** | -5.5 | 7e-06 | 20/41 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.569×** | -5.4 | 7e-06 | 18/37 (LS 180, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.757×** | -5.1 | 3e-05 | 17/40 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.745×** | -5.1 | 3e-05 | 20/39 (PANC-1, KATO III, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 5 µM |  | **0.621×** | -4.6 | 3e-04 | 15/37 (KATO III, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.780×** | -4.4 | 7e-04 | 17/38 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.789×** | -4.4 | 7e-04 | 16/39 (LS 180, HCT15, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.823×** | -3.6 | 0.017 | 16/39 (CFPAC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.765×** | -3.5 | 0.021 | 8/41 (SW480, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.828×** | -3.5 | 0.021 | 14/40 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.832×** | -3.2 | 0.054 | 6/41 (SW480, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11232. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 145 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -22.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -21.1) |
| [[LS 180 (line)]] | wt | 80.6 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -13.5) |
| [[Panc 03.27 (line)]] | alt | 121 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -18.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -14.9) |
| [[A498 (line)]] | wt | 14.4 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.27× (z +11.8) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.350× (z -9.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[LoVo (line)]] | wt | 55.3 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.06× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -13.4) |
| [[PANC-1 (line)]] | alt | 75.4 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -13.2) |
| [[C32 (line)]] | wt | 13.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 12.6× (z +11.3) ⚠ toxic; transcription drop | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0938× (z -10.2) |
| [[HOP62 (line)]] | alt | 12.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.7× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 22.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.52× (z +9.7) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 17.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 12.6× (z +9.3) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 0.05 µM 0.0857× (z -8.7) |
| [[SW 900 (line)]] | alt | 34.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.89× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW480 (line)]] | alt | 44.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +11.4) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 24.8 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.23× (z +9.3) ⚠ toxic; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2030 (line)]] | alt | 27.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.224× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0934× (z -11.4) |
| [[SW1417 (line)]] | alt | 93.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -8.9) |
| [[A-427 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.85 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.56 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.09 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.38 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11232), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKA1]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[CENPK]] | +0.62 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[PBK]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[CENPI]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[CIT]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[NCAPG2]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ANLN]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 | same gene group |
| [[PCLAF]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SKA3]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[NEIL3]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[NCAPH]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[PARPBP]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TADA2B]] | -0.57 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[CDC37L1]] | -0.53 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ZNF7]] | -0.53 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[OXLD1]] | -0.53 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[BLOC1S4]] | -0.52 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[SCAND1]] | -0.51 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[RDH14]] | -0.51 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[RPP38]] | -0.51 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[TSSC4]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[FAM32A]] | -0.50 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[TBCC]] | -0.49 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[ZNF593]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF726]] | B | ZNF726 activity raises RTKN2's level | lines that do not express ZNF726 (20) vs lines expressing it (30) | 1.53× lower at baseline in the lines without ZNF726 | 0.028 | ⚠ within organs, on part of the lines; also absent: SUSD5, RNF150, BVES |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELOA]] | B | RTKN2 activity raises ELOA's level | lines that do not express RTKN2 (7) vs lines expressing it (43) | 1.28× lower at baseline in the lines without RTKN2 | 0.047 | ⚠ within organs, on part of the lines; also absent: RUNDC3B, TENT5C, ENSG00000291112 |
| [[ZNF726]] | B | RTKN2 activity raises ZNF726's level | lines that do not express RTKN2 (7) vs lines expressing it (43) | 2.85× lower at baseline in the lines without RTKN2 | 0.079 | ⚠ within organs, on part of the lines; also absent: RUNDC3B, TENT5C, ENSG00000291112 |
| [[ZNF7]] | B | RTKN2 activity lowers ZNF7's level | lines that do not express RTKN2 (7) vs lines expressing it (43) | 1.30× higher at baseline in the lines without RTKN2 | 0.084 | ⚠ within organs, on part of the lines; also absent: RUNDC3B, TENT5C, ENSG00000291112 |
| [[CEP152]] | B | RTKN2 activity raises CEP152's level | lines that do not express RTKN2 (7) vs lines expressing it (43) | 1.28× lower at baseline in the lines without RTKN2 | 0.098 | ⚠ within organs, on part of the lines; also absent: RUNDC3B, TENT5C, ENSG00000291112 |

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.541). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-34.9, -52.3); signed map (-45.2, -41.7). **Vector** length 104, 24.2% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +6.5 | +18.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +18.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +14.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +7.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +3.7 | +7.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +4.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -8.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.9 | -8.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -4.1 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -5.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.3 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | rhotekin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.2 — chr10:62,183,035-62,268,844 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Em:AC024597.2, bA531F24.1, FLJ39352; previously PLEKHK1 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZC4](https://www.uniprot.org/uniprotkb/Q8IZC4) (Rhotekin-2):

> May play an important role in lymphopoiesis.

**Summary**, from NCBI Gene [219790](https://www.ncbi.nlm.nih.gov/gene/219790):

> Involved in adaptive immune response and intracellular signal transduction. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19364](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19364) · Entrez [219790](https://www.ncbi.nlm.nih.gov/gene/219790) · UniProt [Q8IZC4](https://www.uniprot.org/uniprotkb/Q8IZC4) · Ensembl [ENSG00000182010](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182010)

## Data

Gene col 11232: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11232); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11232, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11232]; `tensor/DDL_lfc|DDL_z.npy` [11232]; `embed/gene_vectors.npy` [11232]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11232 or target_col == 11232). Every well: [[RTKN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTKN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
