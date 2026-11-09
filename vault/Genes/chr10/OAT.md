---
symbol: "OAT"
type: "gene"
col: 775
ensembl_id: "ENSG00000065154"
name: "ornithine aminotransferase"
location: "10q26.13"
module: 42
arm: "+"
pooled_cpm: 40.21
n_lines_expressing: 48
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# OAT

*ornithine aminotransferase* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.30× (z +16.6, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.05 µM: 0.667× (z -5.3, q 8e-05, down in 25 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Finasteride (drug)]] 0.05 µM in 1 line (NCI-H661 0.0448×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.245×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (A-172 0.281×); [[ULK-101 (drug)]] 5 µM in 1 line (SHP-77 0.0856×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIAA1191]] (+0.66, fdr 7e-06), [[DDB1]] (+0.65, fdr 7e-06), [[NDEL1]] (+0.65, fdr 9e-06); moves opposite to [[JPX]] (-0.60, fdr 1e-05), [[DDX52]] (-0.56, fdr 3e-05), [[IWS1]] (-0.56, fdr 3e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SNAI1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 775.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +16.6 | 0e+00 | 45/46 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.51×** | +12.9 | 7e-36 | 43/46 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +10.6 | 1e-23 | 36/46 (NCI-H1792, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.18×** | +9.9 | 8e-21 | 42/46 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.99×** | +9.7 | 5e-20 | 35/44 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.87×** | +8.5 | 2e-15 | 30/37 (SHP-77, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.81×** | +8.3 | 7e-15 | 34/45 (SW480, HT-29, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +7.0 | 2e-10 | 8/46 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +6.2 | 3e-08 | 31/46 (SW480, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.47×** | +5.2 | 1e-05 | 23/45 (SHP-77, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.32×** | +3.9 | 0.005 | 23/46 (NCI-H460, KATO III, …) | inconsistent across doses | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.33×** | +3.8 | 0.006 | 22/46 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.009 | 19/45 (HT-29, SW48, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.30×** | +3.4 | 0.027 | 18/39 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.58×** | +3.4 | 0.030 | 15/44 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.058 | 20/46 (MIA PaCa-2, COLO 205, …) | top dose only |  |
| [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.061 | 9/46 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 775.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Finasteride (drug)]] 0.05 µM in 1 line (NCI-H661 0.0448×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H23 0.245×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (A-172 0.281×); [[ULK-101 (drug)]] 5 µM in 1 line (SHP-77 0.0856×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.05 µM |  | **0.667×** | -5.3 | 8e-05 | 25/45 (A-172, AN3 CA, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.768×** | -3.6 | 0.088 | 22/46 (A498, A-172, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.782× | -3.5 | 0.10 | 20/45 (NCI-H2030, H4, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.788× | -3.3 | 0.11 | 16/46 (A-172, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 0.789× | -3.2 | 0.16 | 12/45 (SK-MEL-2, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 775. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 17.5 | 7 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +12.4) | — |
| [[KATO III (line)]] | alt | 33.6 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +17.8) | — |
| [[NCI-H460 (line)]] | wt | 27.2 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.24× (z +13.6) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +13.2) | — |
| [[HT-29 (line)]] | alt | 20.7 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +13.8) | — |
| [[SW480 (line)]] | alt | 46.8 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +15.5) | — |
| [[PANC-1 (line)]] | alt | 45.4 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.9) | — |
| [[LoVo (line)]] | wt | 41.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 15.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.94× (z +12.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 45.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 21.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +16.4) | — |
| [[NCI-H23 (line)]] | alt | 30.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.14× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[A-427 (line)]] | wt | 36.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.10× (z +9.5) | — |
| [[C32 (line)]] | wt | 52.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +14.2) | — |
| [[CFPAC-1 (line)]] | alt | 53.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 57.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 28.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 31.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +16.6) | — |
| [[Panc 03.27 (line)]] | alt | 37.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +10.5) | [[Allantoin (drug)]] 0.5 µM 0.270× (z -8.5) |
| [[SHP-77 (line)]] | alt | 36.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.51× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[ULK-101 (drug)]] 5 µM 0.0856× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 49.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.32× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.08× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 64.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.20× (z +9.5) | — |
| [[A-172 (line)]] | wt | 30.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.281× (z -9.6) |
| [[A549 (line)]] | wt | 28.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +11.9) | — |
| [[C-33 A (line)]] | alt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[COLO 205 (line)]] | alt | 34.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 21.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +12.5) | — |
| [[HepG2_C3A (line)]] | wt | 52.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +8.6) | — |
| [[NCI-H661 (line)]] | alt | 55.8 | 0 | 1 | — | [[Finasteride (drug)]] 0.05 µM 0.0448× (z -11.5) |
| [[RKO (line)]] | wt | 41.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 55.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.2) | — |
| [[A498 (line)]] | wt | 64.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.90 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 775), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1191]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[DDB1]] | +0.65 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[NDEL1]] | +0.65 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[KLHL15]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[WDR47]] | +0.63 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[VAMP1]] | +0.62 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[LGMN]] | +0.61 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[ACADSB]] | +0.58 | +0.47 / +0.60 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[COPB1]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 | STRING 456 |
| [[ARF1]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[SAR1A]] | +0.56 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[HDLBP]] | +0.56 | +0.58 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JPX]] | -0.60 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[DDX52]] | -0.56 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[IWS1]] | -0.56 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[GGA3]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[OBI1]] | -0.53 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[ERCC4]] | -0.53 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[PPP6R2]] | -0.52 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[AP4E1]] | -0.52 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[CIAPIN1]] | -0.52 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[CCDC137]] | -0.52 | -0.33 / -0.63 | both halves | 1e-04 |  |
| [[RRS1]] | -0.52 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[LTV1]] | -0.51 | -0.39 / -0.54 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNAI1]] | B | SNAI1 activity raises OAT's level | lines that do not express SNAI1 (8) vs lines expressing it (42) | 2.20× lower at baseline in the lines without SNAI1 | 0.095 | ⚠ within organs, on part of the lines; also absent: TNFSF9; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.542). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.2, -27.4); signed map (1.8, 16.7). **Vector** length 103, 27.9% of its response variance represented; |z| ≥ 3 in 886 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +4.3 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +3.9 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +16.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.5 | +6.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | +2.2 | +3.1 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | +2.0 | +2.2 |
|  | [[Demeclocycline (drug)]] 0.05 µM |  | +1.9 | +2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.9 | +3.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.1 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.5 | -5.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.4 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | ornithine aminotransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:124,397,303-124,418,976 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HOGA |
| Gene groups (HGNC) | Transaminases |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 2 pathways, smallest: Glutamate and glutamine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P04181](https://www.uniprot.org/uniprotkb/P04181) (Ornithine aminotransferase, mitochondrial):

> Catalyzes the reversible interconversion of L-ornithine and 2-oxoglutarate to L-glutamate semialdehyde and L-glutamate.

**Summary**, from NCBI Gene [4942](https://www.ncbi.nlm.nih.gov/gene/4942):

> This gene encodes the mitochondrial enzyme ornithine aminotransferase, which is a key enzyme in the pathway that converts arginine and ornithine into the major excitatory and inhibitory neurotransmitters glutamate and GABA. Mutations that result in a deficiency of this enzyme cause the autosomal recessive eye disease Gyrate Atrophy. Alternatively spliced transcript variants encoding different isoforms have been described. Related pseudogenes have been defined on the X chromosome. [provided by …

**Accessions** — [HGNC:8091](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8091) · Entrez [4942](https://www.ncbi.nlm.nih.gov/gene/4942) · UniProt [P04181](https://www.uniprot.org/uniprotkb/P04181) · Ensembl [ENSG00000065154](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065154)

## Data

Gene col 775: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 775); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 775, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 775]; `tensor/DDL_lfc|DDL_z.npy` [775]; `embed/gene_vectors.npy` [775]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 775 or target_col == 775). Every well: [[OAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
