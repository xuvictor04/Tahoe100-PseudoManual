---
symbol: "TPMT"
type: "gene"
col: 6006
ensembl_id: "ENSG00000137364"
name: "thiopurine S-methyltransferase"
location: "6p22.3"
module: 10
arm: "-"
pooled_cpm: 25.17
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# TPMT

*thiopurine S-methyltransferase* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.22× (z +21.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 0.05 µM: 0.733× (z -5.3, q 7e-05, down in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.317×); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.179×); [[Allantoin (drug)]] 0.5 µM in 1 line (Hs 766T 0.117×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM1B]] (+0.68, fdr 1e-05, ⚠ same locus), [[CDA]] (+0.66, fdr 1e-05), [[F11R]] (+0.64, fdr 2e-05), [[ARPC1A]] (+0.61, fdr 2e-05); moves opposite to [[ZFX]] (-0.61, fdr 2e-05), [[TYSND1]] (-0.58, fdr 3e-05), [[HOXA7]] (-0.57, fdr 7e-05).
> It sits in the **-** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DYNLT3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6006.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.22×** | +21.2 | 0e+00 | 48/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.16×** | +20.8 | 0e+00 | 48/48 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.04×** | +20.1 | 0e+00 | 47/47 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.01×** | +12.2 | 6e-32 | 27/34 (A498, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.85×** | +11.1 | 8e-27 | 43/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.81×** | +10.8 | 4e-25 | 33/41 (A498, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.77×** | +9.5 | 1e-19 | 25/38 (A498, C32, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.65×** | +9.1 | 6e-18 | 36/47 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +7.3 | 2e-11 | 28/48 (HOP62, J82, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.10×** | +7.0 | 1e-10 | 33/48 (J82, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.49×** | +6.9 | 2e-10 | 24/43 (SW1417, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.27×** | +6.1 | 4e-08 | 24/46 (J82, HEC-1-A, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +5.7 | 5e-07 | 23/48 (HEC-1-A, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +5.6 | 1e-06 | 18/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.34×** | +5.3 | 5e-06 | 22/47 (J82, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +4.7 | 7e-05 | 20/48 (LS 180, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +4.5 | 2e-04 | 19/47 (NCI-H2030, SK-MEL-2, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 3e-04 | 6/48 (PANC-1, A549, …) | two highest doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +4.1 | 0.001 | 19/48 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.006 | 9/48 (PANC-1, CFPAC-1, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.23×** | +3.6 | 0.007 | 11/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.20× | +3.1 | 0.032 | 7/47 (LS 180, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6006.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.317×); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.179×); [[Allantoin (drug)]] 0.5 µM in 1 line (Hs 766T 0.117×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | **0.733×** | -5.3 | 7e-05 | 22/47 (SW48, SW480, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.772×** | -4.7 | 8e-04 | 16/48 (LoVo, hTERT-HPNE, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -3.8 | 0.024 | 1/48 (NCI-H1792) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.829× | -3.3 | 0.13 | 15/48 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.709× | -3.2 | 0.13 | 13/45 (KATO III, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.842× | -3.1 | 0.18 | 16/47 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.887× | -3.0 | 0.19 | 8/48 (LOX-IMVI, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6006. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 16.3 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.69× (z +11.0) | — |
| [[J82 (line)]] | alt | 39.8 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.31× (z +13.3) | — |
| [[SW480 (line)]] | alt | 23.9 | 4 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.41× (z +13.3) | — |
| [[HOP62 (line)]] | alt | 19.1 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.54× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 43.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.84× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 21.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.27× (z +10.5) | — |
| [[NCI-H2347 (line)]] | alt | 21.1 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.46× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 13.7 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.64× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 24.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.17× (z +11.9) | — |
| [[RKO (line)]] | wt | 17.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.06× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 24.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.08× (z +11.1) | — |
| [[A498 (line)]] | wt | 28.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[BT-474 (line)]] | alt | 10.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.91× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 23.2 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 4.51× (z +8.8) | [[Canagliflozin (drug)]] 0.05 µM 0.167× (z -9.7) |
| [[HT-29 (line)]] | alt | 22.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.59× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.23× (z +10.5) | — |
| [[A-172 (line)]] | wt | 20.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 24.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.317× (z -12.3) |
| [[AN3 CA (line)]] | alt | 19.8 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.05 µM 0.0492× (z -9.6) |
| [[C-33 A (line)]] | alt | 16.5 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.176× (z -9.0) |
| [[C32 (line)]] | wt | 19.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.117× (z -10.2) |
| [[KATO III (line)]] | alt | 25.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +8.8) | — |
| [[LoVo (line)]] | wt | 55.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -9.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H1792 (line)]] | alt | 23.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.77× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 23.4 | 0 | 1 | — | [[PF-06260933 (drug)]] 5 µM 0.0747× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 24.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW48 (line)]] | wt | 49.2 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.179× (z -10.2) |
| [[A549 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 71.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6006), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM1B]] | +0.68 | +0.54 / +0.70 | both halves | 1e-05 | ⚠ same locus (0.3 kb: neighbours can correlate without regulation) |
| [[CDA]] | +0.66 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[F11R]] | +0.64 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ARPC1A]] | +0.61 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[RGS9]] | +0.57 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[ENTPD4]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[FA2H]] | +0.56 | +0.64 / +0.34 | both halves | 1e-04 |  |
| [[STAM2]] | +0.56 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[LTBP4]] | +0.55 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[STK40]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[SGTB]] | +0.55 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[UBA6]] | +0.54 | +0.51 / +0.28 | both halves | 3e-04 |  |
| [[STARD4]] | +0.53 | +0.47 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFX]] | -0.61 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[TYSND1]] | -0.58 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[HOXA7]] | -0.57 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[ZNF689]] | -0.57 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[ZNF747]] | -0.55 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[LINC00886]] | -0.55 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[SAFB]] | -0.55 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[YTHDF2]] | -0.55 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[AEBP2]] | -0.54 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[MCPH1]] | -0.54 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[DPH6-DT]] | -0.54 | -0.37 / -0.32 | both halves | 1e-04 |  |
| [[PPP4R3A]] | -0.54 | -0.36 / -0.46 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNLT3]] | C | DYNLT3 activity raises TPMT's level | lines that do not express DYNLT3 (4) vs lines expressing it (46) | 1.72× lower at baseline in the lines without DYNLT3 | 0.092 | ⚠ few lines (4 vs 46); across organs; also absent: PLEKHA5, LRRCC1, RGL1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.490). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (11.3, 2.2); signed map (-19.3, 28.5). **Vector** length 92.8, 21.5% of its response variance represented; |z| ≥ 3 in 1,132 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +4.4 | +10.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.0 | +20.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +21.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.2 | +12.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +7.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.6 | +4.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | +1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.4 | -5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.6 | -4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | thiopurine S-methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:18,128,311-18,155,077 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | 7BS small molecule methyltransferases; Small molecule methyltransferases |
| Reactome | 7 pathways, smallest: Methylation; Azathioprine ADME; Metabolic disorders of biological oxidation enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [P51580](https://www.uniprot.org/uniprotkb/P51580) (Thiopurine S-methyltransferase):

> Catalyzes the S-methylation of thiopurine drugs such as 6-mercaptopurine (also called mercaptopurine, 6-MP or its brand name Purinethol) and 6-thioguanine (also called tioguanine or 6-TG) using S-adenosyl-L-methionine as the methyl donor. TPMT activity modulates the cytotoxic effects of thiopurine prodrugs. A natural substrate for this enzyme has yet to be identified.

**Summary**, from NCBI Gene [7172](https://www.ncbi.nlm.nih.gov/gene/7172):

> This gene encodes the enzyme that metabolizes thiopurine drugs via S-adenosyl-L-methionine as the S-methyl donor and S-adenosyl-L-homocysteine as a byproduct. Thiopurine drugs such as 6-mercaptopurine are used as chemotherapeutic agents. Genetic polymorphisms that affect this enzymatic activity are correlated with variations in sensitivity and toxicity to such drugs within individuals, causing thiopurine S-methyltransferase deficiency. Related pseudogenes have been identified on chromosomes 3, …

**Accessions** — [HGNC:12014](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12014) · Entrez [7172](https://www.ncbi.nlm.nih.gov/gene/7172) · UniProt [P51580](https://www.uniprot.org/uniprotkb/P51580) · Ensembl [ENSG00000137364](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137364)

## Data

Gene col 6006: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6006); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6006, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6006]; `tensor/DDL_lfc|DDL_z.npy` [6006]; `embed/gene_vectors.npy` [6006]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6006 or target_col == 6006). Every well: [[TPMT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPMT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
