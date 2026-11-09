---
symbol: "STK38L"
type: "gene"
col: 13062
ensembl_id: "ENSG00000211455"
name: "serine/threonine kinase 38 like"
location: "12p11.23"
module: 111
arm: "+"
pooled_cpm: 79.04
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# STK38L

*serine/threonine kinase 38 like* — 12p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.64× (z +15.7, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.590× (z -8.6, q 5e-15, down in 33 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 0.827× (z -4.4, q 0.002, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 9 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (SW 1271 0.0667×, CHP-212 0.0854×, PANC-1 0.393×, NCI-H460 0.416×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.181×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 0.325×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.304×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1271 0.0693×); [[Radotinib (drug)]] 5 µM in 1 line (AsPC-1 0.454×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PALLD]] (+0.57, fdr 1e-05), [[OSBPL11]] (+0.56, fdr 1e-05), [[PDLIM5]] (+0.53, fdr 6e-05); moves opposite to [[AGAP3]] (-0.54, fdr 1e-05), [[EEF2K]] (-0.53, fdr 1e-05), [[FNTB]] (-0.51, fdr 1e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13062.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.64×** | +15.7 | 0e+00 | 44/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.61×** | +15.6 | 0e+00 | 44/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +12.9 | 6e-36 | 35/48 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.14×** | +12.4 | 5e-33 | 44/48 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +9.4 | 6e-19 | 39/48 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +8.0 | 2e-13 | 41/48 (SW1417, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +7.8 | 4e-13 | 34/48 (MIA PaCa-2, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +5.8 | 4e-07 | 30/49 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.85×** | +5.2 | 1e-05 | 32/49 (A-172, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +5.2 | 1e-05 | 29/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +5.2 | 1e-05 | 29/48 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +4.6 | 2e-04 | 29/48 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.25×** | +3.7 | 0.011 | 22/48 (CFPAC-1, SW 900, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.24×** | +3.5 | 0.020 | 21/48 (A-172, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13062.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 9 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (SW 1271 0.0667×, CHP-212 0.0854×, PANC-1 0.393×, NCI-H460 0.416×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.181×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 0.325×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.304×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1271 0.0693×); [[Radotinib (drug)]] 5 µM in 1 line (AsPC-1 0.454×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -8.6 | 5e-15 | 33/48 (SW 1271, CHP-212, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.679×** | -6.1 | 4e-07 | 31/47 (Panc 03.27, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.827×** | -4.4 | 0.002 | 20/48 (AsPC-1, CHP-212, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **0.796×** | -3.7 | 0.028 | 24/48 (NCI-H460, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | **0.801×** | -3.6 | 0.034 | 22/49 (RKO, PANC-1, …) | inconsistent across doses | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.740×** | -3.5 | 0.044 | 19/48 (SHP-77, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.814× | -3.2 | 0.10 | 18/49 (PANC-1, NCI-H2122, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 0.775× | -3.2 | 0.11 | 19/45 (SW 900, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13062. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 65.6 | 2 | 6 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.42× (z +10.0) | [[Digitoxin (drug)]] 0.5 µM 0.325× (z -12.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 216 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +14.2) | [[Digitoxin (drug)]] 5 µM 0.545× (z -8.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 44.5 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 5.18× (z +13.7) | — |
| [[A-172 (line)]] | wt | 44.0 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.84× (z +12.6) | — |
| [[AsPC-1 (line)]] | alt | 73.2 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.78× (z +11.2) | [[Radotinib (drug)]] 5 µM 0.454× (z -9.6) |
| [[SW 900 (line)]] | alt | 115 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.41× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -9.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 58.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +14.7) | — |
| [[A-427 (line)]] | wt | 46.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.1) | — |
| [[CFPAC-1 (line)]] | alt | 29.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +16.8) | — |
| [[HEC-1-A (line)]] | alt | 37.3 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.40× (z +11.9) | — |
| [[J82 (line)]] | alt | 29.1 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.27× (z +11.9) | — |
| [[NCI-H23 (line)]] | alt | 103 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +13.5) | — |
| [[A498 (line)]] | wt | 49.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.57× (z +13.1) | — |
| [[C32 (line)]] | wt | 45.7 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 3.45× (z +9.7) | [[Monocrotaline (drug)]] 0.05 µM 0.218× (z -9.1) |
| [[HOP62 (line)]] | alt | 68.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +10.2) | — |
| [[LoVo (line)]] | wt | 104 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.42× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 49.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.45× (z +11.6) | — |
| [[PANC-1 (line)]] | alt | 72.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.48× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.393× (z -10.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 63.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.39× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 55.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 57.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 101 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.5) | — |
| [[KATO III (line)]] | alt | 70.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.62× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 250 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -14.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.304× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 69.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.335× (z -9.8) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 131 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0667× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0693× (z -10.0) |
| [[SW48 (line)]] | wt | 56.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.49× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.260× (z -9.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 85.1 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.114× (z -9.7) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 210 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0854× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 68.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 91.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.3) | — |
| [[A549 (line)]] | wt | 80.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 97.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 104 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 80.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 99.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13062), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PALLD]] | +0.57 | +0.55 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[OSBPL11]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[PDLIM5]] | +0.53 | +0.39 / +0.50 | both halves | 6e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[ZFYVE16]] | +0.48 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[TFPI]] | +0.48 | +0.46 / +0.37 | both halves | 9e-05 |  |
| [[VCL]] | +0.48 | +0.41 / +0.49 | both halves | 4e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[CLTB]] | +0.47 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[STK17A]] | +0.47 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[TTPAL]] | +0.47 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[BMP2]] | +0.47 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[INO80C]] | +0.46 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[GLIPR1]] | +0.46 | +0.47 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGAP3]] | -0.54 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[EEF2K]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[FNTB]] | -0.51 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[SLC16A4-AS1]] | -0.51 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[NDC1]] | -0.49 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[LINC00159]] | -0.49 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[POM121C]] | -0.48 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[ACP6]] | -0.46 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[GOT1-DT]] | -0.46 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[DIDO1]] | -0.45 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[NUP153]] | -0.45 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[TTC9C]] | -0.44 | -0.40 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.366). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.7, 28.0); signed map (-5.9, 39.0). **Vector** length 106, 30.9% of its response variance represented; |z| ≥ 3 in 1,225 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.9 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.7 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.2 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.3 | +0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.5 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.8 | -4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +2.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | -8.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.2 | -0.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.1 | -2.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 38 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.23 — chr12:27,243,968-27,325,959 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0965, NDR2 |
| Gene groups (HGNC) | Serine/threonine kinase 38 family |
| Hallmark sets | MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2H1](https://www.uniprot.org/uniprotkb/Q9Y2H1) (Serine/threonine-protein kinase 38-like):

> Involved in the regulation of structural processes in differentiating and mature neuronal cells.

**Summary**, from NCBI Gene [23012](https://www.ncbi.nlm.nih.gov/gene/23012):

> Enables ATP binding activity; magnesium ion binding activity; and protein serine/threonine kinase activity. Involved in intracellular signal transduction and negative regulation of autophagy. Acts upstream of or within protein phosphorylation. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17848](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17848) · Entrez [23012](https://www.ncbi.nlm.nih.gov/gene/23012) · UniProt [Q9Y2H1](https://www.uniprot.org/uniprotkb/Q9Y2H1) · Ensembl [ENSG00000211455](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000211455)

## Data

Gene col 13062: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13062); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13062, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13062]; `tensor/DDL_lfc|DDL_z.npy` [13062]; `embed/gene_vectors.npy` [13062]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13062 or target_col == 13062). Every well: [[STK38L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK38L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
