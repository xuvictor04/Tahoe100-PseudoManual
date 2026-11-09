---
symbol: "SLC12A9"
type: "gene"
col: 7122
ensembl_id: "ENSG00000146828"
name: "solute carrier family 12 member 9"
location: "7q22.1"
module: 15
arm: "+"
pooled_cpm: 11.56
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 17
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# SLC12A9

*solute carrier family 12 member 9* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.10× (z +26.5, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.549× (z -9.9, q 2e-20, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR20]] (+0.67, fdr 1e-04), [[GATD1-DT]] (+0.65, fdr 1e-05), [[ANKRD16]] (+0.64, fdr 2e-05); moves opposite to [[MOCS2]] (-0.55, fdr 6e-05), [[NEK1]] (-0.54, fdr 3e-04), [[LMCD1]] (-0.53, fdr 1e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HOXC9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7122.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.10×** | +26.5 | 0e+00 | 44/45 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +11.3 | 3e-27 | 32/44 (A498, C32, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +7.5 | 8e-12 | 26/47 (HT-29, A498, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.59×** | +7.4 | 2e-11 | 27/42 (KATO III, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +7.0 | 3e-10 | 24/48 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +5.7 | 1e-06 | 20/47 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +5.4 | 6e-06 | 20/48 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.38×** | +5.3 | 7e-06 | 20/48 (NCI-H1792, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.34×** | +4.8 | 1e-04 | 18/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.21×** | +4.4 | 7e-04 | 15/47 (A-427, LS 180, …) | rises with dose | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +4.4 | 7e-04 | 6/43 (A498, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.30×** | +4.3 | 8e-04 | 8/47 (LS 180, A549, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.5 | 0.019 | 11/48 (LOX-IMVI, NCI-H1792, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.020 | 10/43 (HT-29, A498, …) | inconsistent across doses |  |
| [[Ixazomib (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.024 | 2/43 (A498, A-427) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.029 | 6/47 (HS-578T, NCI-H1573, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.044 | 7/48 (SW480, SK-MEL-2, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.055 | 10/46 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.076 | 4/48 (SK-MEL-2, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7122.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.549×** | -9.9 | 2e-20 | 33/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.602×** | -8.4 | 1e-14 | 26/45 (RKO, PANC-1, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.604×** | -8.0 | 2e-13 | 25/47 (A-427, NCI-H23, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.434×** | -7.2 | 7e-11 | 24/47 (NCI-H23, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.648×** | -7.2 | 9e-11 | 21/45 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.678×** | -6.4 | 1e-08 | 22/48 (A-427, LS 180, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.773×** | -6.0 | 1e-07 | 25/46 (MIA PaCa-2, A-172, …) | two highest doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.707×** | -5.7 | 7e-07 | 19/47 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.709×** | -5.7 | 8e-07 | 19/47 (HOP62, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.573×** | -4.8 | 8e-05 | 14/43 (LoVo, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.744×** | -4.7 | 1e-04 | 12/39 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.755×** | -4.6 | 2e-04 | 16/46 (LS 180, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.755×** | -4.4 | 5e-04 | 11/46 (PANC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.775×** | -4.2 | 1e-03 | 15/47 (AN3 CA, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.776×** | -4.2 | 1e-03 | 14/46 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.855× | -3.7 | 0.008 | 14/48 (KATO III, LS 180, …) | top dose only |  |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.831×** | -3.1 | 0.068 | 3/48 (PANC-1, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7122. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 15.5 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +13.4) | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -14.0) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Pimozide (drug)]] 0.05 µM 0.258× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 10.9 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.228× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[A-427 (line)]] | wt | 11.9 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -10.5) |
| [[A498 (line)]] | wt | 18.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +17.7) | — |
| [[C32 (line)]] | wt | 23.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +15.1) | — |
| [[CFPAC-1 (line)]] | alt | 6.52 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +8.6) | [[Menadione (drug)]] 5 µM 0.120× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 8.22 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +8.5) | [[Digitoxin (drug)]] 0.05 µM 0.0648× (z -14.0) ⚠ cell-cycle shift, explains ~24% of this change |
| [[PANC-1 (line)]] | alt | 13.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +11.3) | [[Digitoxin (drug)]] 5 µM 0.310× (z -9.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +11.6) | — |
| [[BT-474 (line)]] | alt | 14.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +9.9) | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0536× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 9.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 13.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +11.3) | — |
| [[KATO III (line)]] | alt | 16.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +11.8) | — |
| [[LoVo (line)]] | wt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +13.4) | — |
| [[LS 180 (line)]] | wt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -16.9) ⚠ cell-cycle shift, explains ~85% of this change |
| [[NCI-H1792 (line)]] | alt | 6.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 14.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +9.0) | — |
| [[RKO (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -9.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SNU-1 (line)]] | wt | 14.1 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0578× (z -12.0) |
| [[SW48 (line)]] | wt | 16.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +9.0) | — |
| [[SW480 (line)]] | alt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7122), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR20]] | +0.67 | +0.35 / +0.65 | both halves | 1e-04 |  |
| [[GATD1-DT]] | +0.65 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[ANKRD16]] | +0.64 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[MIR762HG]] | +0.63 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[AGAP3]] | +0.61 | +0.40 / +0.73 | both halves | 5e-05 |  |
| [[NUDT2]] | +0.60 | +0.37 / +0.67 | both halves | 8e-05 |  |
| [[SCAMP5]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[SEPTIN1]] | +0.60 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[MFSD8]] | +0.59 | +0.39 / +0.61 | both halves | 6e-05 |  |
| [[TRIM7]] | +0.59 | +0.33 / +0.59 | both halves | 1e-04 |  |
| [[PANK1]] | +0.59 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[SEC24B-AS1]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOCS2]] | -0.55 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[NEK1]] | -0.54 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[LMCD1]] | -0.53 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[MAP9]] | -0.53 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[CSRP1]] | -0.52 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[RPAP3]] | -0.52 | -0.26 / -0.47 | both halves | 4e-04 |  |
| [[CLCN3]] | -0.50 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[ALAS1]] | -0.50 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[LINC00460]] | -0.50 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[LMCD1-AS1]] | -0.50 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[SPTAN1]] | -0.50 | -0.27 / -0.55 | both halves | 3e-04 |  |
| [[MRPL47]] | -0.50 | -0.29 / -0.55 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXC9]] | B | HOXC9 activity raises SLC12A9's level | lines that do not express HOXC9 (10) vs lines expressing it (40) | 1.34× lower at baseline in the lines without HOXC9 | 0.078 | ⚠ within organs, on part of the lines; also absent: HOXC4, LINC01013, SOCS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.692). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-9.1, 21.2); signed map (4.4, 0.5). **Vector** length 63.8, 9.94% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +26.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +11.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +7.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +2.6 | +7.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +5.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | +5.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +2.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.4 | -8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.0 | -8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | -2.8 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.1 | +0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 12 member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,826,820-100,867,010 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CIP1 |
| Gene groups (HGNC) | Solute carrier family 12 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXP2](https://www.uniprot.org/uniprotkb/Q9BXP2) (Solute carrier family 12 member 9):

> May be an inhibitor of SLC12A1. Seems to correspond to a subunit of a multimeric transport system and thus, additional subunits may be required for its function. May play a role in lysosomal ion flux and osmoregulation.

**Summary**, from NCBI Gene [56996](https://www.ncbi.nlm.nih.gov/gene/56996):

> Predicted to enable potassium:chloride symporter activity. Predicted to be involved in several processes, including cell volume homeostasis; chloride ion homeostasis; and potassium ion homeostasis. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17435](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17435) · Entrez [56996](https://www.ncbi.nlm.nih.gov/gene/56996) · UniProt [Q9BXP2](https://www.uniprot.org/uniprotkb/Q9BXP2) · Ensembl [ENSG00000146828](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146828)

## Data

Gene col 7122: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7122); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7122, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7122]; `tensor/DDL_lfc|DDL_z.npy` [7122]; `embed/gene_vectors.npy` [7122]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7122 or target_col == 7122). Every well: [[SLC12A9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC12A9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
