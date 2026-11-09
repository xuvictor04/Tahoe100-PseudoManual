---
symbol: "USP31"
type: "gene"
col: 2363
ensembl_id: "ENSG00000103404"
name: "ubiquitin specific peptidase 31"
location: "16p12.2"
module: 18
arm: "+"
pooled_cpm: 35.32
n_lines_expressing: 47
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 16
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# USP31

*ubiquitin specific peptidase 31* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.58× (z +9.5, q 1e-18, up in 29 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.757× (z -5.8, q 3e-06, down in 24 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-427 0.296×, SW48 0.111×, A-172 0.293×, NCI-H23 0.392×, …; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.173×, A-172 0.168×, NCI-H23 0.341×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change); [[Auranofin (drug)]] 5 µM in 3 lines (SK-MEL-2 0.209×, A-427 0.415×, A-172 0.417×); [[Auranofin (drug)]] 0.5 µM in 1 line (AN3 CA 0.0654×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (SW48 0.157×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LDLRAD3]] (+0.70, fdr 7e-06), [[PINX1]] (+0.69, fdr 7e-06), [[CAD]] (+0.63, fdr 7e-06); moves opposite to [[FAM117A]] (-0.56, fdr 3e-05), [[TESK2]] (-0.55, fdr 3e-05), [[SELENOK]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GNAZ]] → it (grade B ⚠); 16 go from it, the strongest it → [[FSD1L]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2363.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +9.5 | 1e-18 | 29/45 (NCI-H1573, LoVo, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +9.3 | 6e-18 | 36/45 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +7.7 | 3e-12 | 21/45 (SW480, SW 900, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.36×** | +6.4 | 3e-08 | 23/45 (NCI-H1573, LoVo, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.35×** | +6.2 | 5e-08 | 26/44 (HCT15, NCI-H460, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +6.1 | 1e-07 | 18/45 (LOX-IMVI, C32, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.33×** | +6.0 | 2e-07 | 22/45 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.71×** | +5.9 | 3e-07 | 18/45 (NCI-H1573, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.33×** | +5.9 | 3e-07 | 19/45 (Hs 766T, HS-578T, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.32×** | +5.8 | 4e-07 | 22/45 (NCI-H1573, NCI-H460, …) | two highest doses |  |
| [[Budesonide (drug)]] 5 µM |  | **1.29×** | +5.2 | 8e-06 | 19/45 (Hs 766T, HS-578T, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +5.1 | 2e-05 | 18/44 (Hs 766T, H4, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +5.0 | 3e-05 | 13/45 (A549, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.28×** | +4.9 | 4e-05 | 17/44 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.27×** | +4.9 | 4e-05 | 17/44 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +4.7 | 8e-05 | 19/45 (SW480, NCI-H1573, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +4.4 | 3e-04 | 14/45 (NCI-H1573, MIA PaCa-2, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.47×** | +4.2 | 9e-04 | 19/45 (A498, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.22×** | +4.1 | 1e-03 | 15/45 (Hs 766T, HS-578T, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +4.1 | 0.001 | 17/45 (C32, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2363.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-427 0.296×, SW48 0.111×, A-172 0.293×, NCI-H23 0.392×, …; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.173×, A-172 0.168×, NCI-H23 0.341×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change); [[Auranofin (drug)]] 5 µM in 3 lines (SK-MEL-2 0.209×, A-427 0.415×, A-172 0.417×); [[Auranofin (drug)]] 0.5 µM in 1 line (AN3 CA 0.0654×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (SW48 0.157×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.757×** | -5.8 | 3e-06 | 24/45 (SK-MEL-2, A-427, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.876× | -4.0 | 0.021 | 16/44 (HS-578T, NCI-H1573, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.716×** | -3.7 | 0.045 | 16/43 (A498, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.898× | -3.2 | 0.17 | 11/45 (KATO III, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.865× | -3.1 | 0.25 | 12/45 (HEC-1-A, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2363. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 81.6 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +19.9) ⚠ cell-cycle shift, explains ~0% of this change; position correction uncertain · without an alert: [[TAK-901 (drug)]] 5 µM 6.96× (z +12.8) | — |
| [[A-172 (line)]] | wt | 67.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.417× (z -8.6) |
| [[A-427 (line)]] | wt | 49.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.415× (z -8.9) |
| [[C32 (line)]] | wt | 32.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change; position correction uncertain |
| [[NCI-H460 (line)]] | wt | 25.7 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 45.0 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.209× (z -13.6) |
| [[SW48 (line)]] | wt | 35.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.157× (z -9.4) |
| [[KATO III (line)]] | alt | 23.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 55.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.341× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[SNU-1 (line)]] | wt | 37.7 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.103× (z -12.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 36.3 | 0 | 1 | — | [[Auranofin (drug)]] 0.5 µM 0.0654× (z -11.2) |
| [[BT-474 (line)]] | alt | 24.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change; position correction uncertain | — |
| [[HOP62 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 16.2 | 1 | 0 | [[Budesonide (drug)]] 5 µM 5.19× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 26.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change; position correction uncertain |
| [[NCI-H1573 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 47.3 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0916× (z -8.6) |
| [[PANC-1 (line)]] | alt | 60.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.25× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | — |
| [[RKO (line)]] | wt | 40.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 28.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[SNU-423 (line)]] | alt | 40.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change; position correction uncertain | — |
| [[A549 (line)]] | wt | 71.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.71 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.63 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2363), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDLRAD3]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[PINX1]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[CAD]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[CPNE7]] | +0.62 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[URB2]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[TCOF1]] | +0.61 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[UCK2]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PDSS1]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[BOP1]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[LETM1]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[XYLB]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[SDC3]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM117A]] | -0.56 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[TESK2]] | -0.55 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[SELENOK]] | -0.55 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[MXD1]] | -0.55 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[KLC4]] | -0.54 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[STX17-DT]] | -0.53 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[TMF1]] | -0.52 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[CCDC186]] | -0.52 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[DNAJB4]] | -0.52 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[AP1G1]] | -0.51 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[SMIM14]] | -0.51 | -0.41 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAZ]] | B | GNAZ activity raises USP31's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.45× lower at baseline in the lines without GNAZ | 0.001 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[JPH1]] | B | JPH1 activity lowers USP31's level | lines that do not express JPH1 (15) vs lines expressing it (35) | 1.54× higher at baseline in the lines without JPH1 | 0.020 | ⚠ within organs, on part of the lines; also absent: UGT8, CADPS2, PTPRE |
| [[FAM78B]] | B | FAM78B activity raises USP31's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 1.70× lower at baseline in the lines without FAM78B | 0.034 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 0, C 16. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSD1L]] | C | USP31 activity raises FSD1L's level | lines that do not express USP31 (3) vs lines expressing it (47) | 3.49× lower at baseline in the lines without USP31 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |
| [[ADCY3]] | C | [[MTHFD1L]], USP31 activity raises ADCY3's level | lines that do not express MTHFD1L, USP31 (3) vs lines expressing them (47) | 3.19× lower at baseline in the lines without MTHFD1L, USP31 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p; co-absent genes |
| [[FXN]] | C | USP31 activity raises FXN's level | lines that do not express USP31 (3) vs lines expressing it (47) | 2.66× lower at baseline in the lines without USP31 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |
| [[MDN1]] | C | [[MTHFD1L]], USP31 activity raises MDN1's level | lines that do not express MTHFD1L, USP31 (3) vs lines expressing them (47) | 2.58× lower at baseline in the lines without MTHFD1L, USP31 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p; co-absent genes |
| [[CEP83]] | C | USP31 activity raises CEP83's level | lines that do not express USP31 (3) vs lines expressing it (47) | 2.44× lower at baseline in the lines without USP31 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |
| [[RCL1]] | C | USP31 activity raises RCL1's level | lines that do not express USP31 (3) vs lines expressing it (47) | 2.27× lower at baseline in the lines without USP31 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |
| [[NUP93]] | C | USP31 activity raises NUP93's level | lines that do not express USP31 (3) vs lines expressing it (47) | 2.06× lower at baseline in the lines without USP31 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |
| [[LDLRAD3]] | C | [[MTHFD1L]], USP31 activity raises LDLRAD3's level | lines that do not express MTHFD1L, USP31 (3) vs lines expressing them (47) | 3.40× lower at baseline in the lines without MTHFD1L, USP31 | 0.061 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; co-absent genes |
| [[TCFL5]] | C | USP31 activity raises TCFL5's level | lines that do not express USP31 (3) vs lines expressing it (47) | 2.16× lower at baseline in the lines without USP31 | 0.070 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent |
| [[PUS7]] | C | [[MTHFD1L]], USP31 activity raises PUS7's level | lines that do not express MTHFD1L, USP31 (3) vs lines expressing them (47) | 2.89× lower at baseline in the lines without MTHFD1L, USP31 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p; co-absent genes |
| [[DNAJB4]] | C | USP31 activity raises DNAJB4's level | lines that do not express USP31 (3) vs lines expressing it (47) | 2.64× lower at baseline in the lines without USP31 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |
| [[CMSS1]] | C | [[MTHFD1L]], USP31 activity raises CMSS1's level | lines that do not express MTHFD1L, USP31 (3) vs lines expressing them (47) | 2.53× lower at baseline in the lines without MTHFD1L, USP31 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p; co-absent genes |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-13.2, -37.6); signed map (-3.5, -54.4). **Vector** length 115, 29.0% of its response variance represented; |z| ≥ 3 in 1,150 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.2 | +9.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.9 | +6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.8 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.4 | +5.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.4 | +4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +4.7 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.8 | +5.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.2 | -5.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | -4.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.2 | -3.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -3.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.2 — chr16:23,061,406-23,149,452 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1203 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q70CQ4](https://www.uniprot.org/uniprotkb/Q70CQ4) (Ubiquitin carboxyl-terminal hydrolase 31):

> Deubiquitinase that recognizes and hydrolyzes the peptide bond at the C-terminal Gly of ubiquitin. May play a role in the regulation of NF-kappa-B signaling pathway by deubiquitinating TRAF2.; (Microbial infection) Plays a positive role in foot-and-mouth disease and classical swine fever viral infection. Mechanistically, associates with internal ribosomal entry site (IRES) element within the 5'-untranslated region of viral genomes to promote translation of the virus-encoded polyprotein.

**Summary**, from NCBI Gene [57478](https://www.ncbi.nlm.nih.gov/gene/57478):

> Enables cysteine-type deubiquitinase activity. Predicted to be involved in protein deubiquitination and proteolysis. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20060](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20060) · Entrez [57478](https://www.ncbi.nlm.nih.gov/gene/57478) · UniProt [Q70CQ4](https://www.uniprot.org/uniprotkb/Q70CQ4) · Ensembl [ENSG00000103404](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103404)

## Data

Gene col 2363: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2363); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2363, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2363]; `tensor/DDL_lfc|DDL_z.npy` [2363]; `embed/gene_vectors.npy` [2363]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2363 or target_col == 2363). Every well: [[USP31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
