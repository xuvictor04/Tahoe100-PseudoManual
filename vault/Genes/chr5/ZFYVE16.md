---
symbol: "ZFYVE16"
type: "gene"
col: 461
ensembl_id: "ENSG00000039319"
name: "zinc finger FYVE-type containing 16"
location: "5q14.1"
module: 57
arm: "-"
pooled_cpm: 127.02
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# ZFYVE16

*zinc finger FYVE-type containing 16* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.49× (z +13.4, q 4e-38, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.503× (z -7.6, q 2e-11, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSRNP2]] (+0.56, fdr 2e-05), [[RO60]] (+0.56, fdr 1e-05), [[KRBOX5]] (+0.55, fdr 4e-05); moves opposite to [[KCNK15-AS1]] (-0.55, fdr 7e-05), [[SDHB]] (-0.53, fdr 7e-05), [[FOXJ3]] (-0.53, fdr 4e-05).
> It sits in the **-** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 461.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +13.4 | 4e-38 | 37/48 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.67×** | +10.9 | 3e-25 | 42/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +9.1 | 1e-17 | 29/49 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +6.3 | 5e-08 | 26/48 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.9 | 4e-07 | 30/48 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.24×** | +5.1 | 2e-05 | 28/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.21×** | +4.5 | 6e-04 | 21/48 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.2 | 0.002 | 19/48 (SNU-423, RKO, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.6 | 0.022 | 20/50 (LS 180, NCI-H23, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.028 | 19/48 (HEC-1-A, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.4 | 0.037 | 17/48 (SNU-423, HepG2/C3A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.15× | +3.3 | 0.048 | 17/48 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.10× | +3.3 | 0.048 | 9/48 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.09× | +3.0 | 0.11 | 6/48 (HS-578T, A549, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 461.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.503×** | -7.6 | 2e-11 | 37/49 (NCI-H23, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.727×** | -6.1 | 3e-07 | 30/45 (C-33 A, A-427, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -5.9 | 9e-07 | 0/50 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.809×** | -5.1 | 5e-05 | 26/48 (SW480, C-33 A, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.875× | -4.5 | 7e-04 | 15/48 (NCI-H1792, RPMI-7951, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.810×** | -4.5 | 7e-04 | 22/44 (C-33 A, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | 0.834× | -4.3 | 0.001 | 23/49 (SW 900, AsPC-1, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.676×** | -4.3 | 0.001 | 26/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.831×** | -4.0 | 0.005 | 24/47 (SHP-77, SW 900, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | 0.869× | -3.4 | 0.043 | 19/48 (SW 900, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.873× | -3.2 | 0.060 | 12/48 (AN3 CA, SNU-423, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.881× | -3.0 | 0.12 | 13/48 (A549, NCI-H23, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 461. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 117 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.6) | [[Lonafarnib (drug)]] 5 µM 0.129× (z -12.1) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 146 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +21.3) | — |
| [[NCI-H2347 (line)]] | alt | 116 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +19.5) | — |
| [[SW480 (line)]] | alt | 148 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +18.0) | — |
| [[A-427 (line)]] | wt | 191 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 1.76× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.447× (z -10.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 131 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +18.2) | — |
| [[C-33 A (line)]] | alt | 185 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 67.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 90.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +12.3) | — |
| [[HT-29 (line)]] | alt | 93.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +17.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 158 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +12.0) | — |
| [[NCI-H23 (line)]] | alt | 118 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.148× (z -12.4) |
| [[RKO (line)]] | wt | 117 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.9) | — |
| [[SW 1088 (line)]] | alt | 156 | 0 | 2 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0903× (z -10.5) |
| [[A-172 (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.476× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 116 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +13.3) | — |
| [[COLO 205 (line)]] | alt | 83.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +15.0) | — |
| [[H4 (line)]] | wt | 91.5 | 1 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.69× (z +9.3) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[Hs 766T (line)]] | wt | 80.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.6) | — |
| [[KATO III (line)]] | alt | 67.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.0) | — |
| [[LoVo (line)]] | wt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 106 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.53× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 156 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 160 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.303× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-1 (line)]] | wt | 113 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.3) | — |
| [[SNU-423 (line)]] | alt | 181 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.37× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 235 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW1417 (line)]] | alt | 85.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +15.3) | — |
| [[A498 (line)]] | wt | 94.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 227 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 245 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 127 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 126 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 98.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 83.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 91.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 461), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSRNP2]] | +0.56 | +0.46 / +0.47 | both halves | 2e-05 | same gene group |
| [[RO60]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[KRBOX5]] | +0.55 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[ERCC6L2]] | +0.53 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[NDUFA6]] | +0.53 | +0.58 / +0.38 | both halves | 7e-05 |  |
| [[USP11]] | +0.52 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[CREM]] | +0.52 | +0.58 / +0.31 | both halves | 2e-04 |  |
| [[N4BP2]] | +0.52 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[CYP20A1]] | +0.51 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[WSB2]] | +0.51 | +0.37 / +0.40 | both halves | 8e-05 |  |
| [[BAZ2B]] | +0.51 | +0.50 / +0.36 | both halves | 9e-05 |  |
| [[GYG1]] | +0.51 | +0.47 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNK15-AS1]] | -0.55 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[SDHB]] | -0.53 | -0.53 / -0.37 | both halves | 7e-05 |  |
| [[FOXJ3]] | -0.53 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[TMEM185A]] | -0.52 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[TMEM182]] | -0.51 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[EXOSC5]] | -0.50 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[USPL1]] | -0.50 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[CGREF1]] | -0.49 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[SKP2]] | -0.49 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[ELP1]] | -0.49 | -0.47 / -0.24 | both halves | 4e-04 |  |
| [[THRA]] | -0.49 | -0.41 / -0.37 | both halves | 9e-05 |  |
| [[NUS1]] | -0.49 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **-** arm (projection on the module's main direction -0.478). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-8.4, 0.5); signed map (20.7, -19.9). **Vector** length 112, 31.0% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.0 | +10.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +5.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +9.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +13.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +0.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.1 | -0.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.1 | +0.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -8.8 | -7.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.7 | -4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.2 | -4.5 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.7 | -2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger FYVE-type containing 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:80,408,013-80,483,379 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0305, PPP1R69 |
| Gene groups (HGNC) | Zinc fingers FYVE-type; Protein phosphatase 1 regulatory subunits |
| Reactome | 2 pathways, smallest: Signaling by BMP; Signaling by TGFB family members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z3T8](https://www.uniprot.org/uniprotkb/Q7Z3T8) (Zinc finger FYVE domain-containing protein 16):

> May be involved in regulating membrane trafficking in the endosomal pathway. Overexpression induces endosome aggregation. Required to target TOM1 to endosomes.

**Summary**, from NCBI Gene [9765](https://www.ncbi.nlm.nih.gov/gene/9765):

> This gene encodes an endosomal protein that belongs to the FYVE zinc finger family of proteins. The encoded protein is thought to regulate membrane trafficking in the endosome. This protein functions as a scaffold protein in the transforming growth factor-beta signaling pathway and is involved in positive and negative feedback regulation of the bone morphogenetic protein signaling pathway. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:20756](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20756) · Entrez [9765](https://www.ncbi.nlm.nih.gov/gene/9765) · UniProt [Q7Z3T8](https://www.uniprot.org/uniprotkb/Q7Z3T8) · Ensembl [ENSG00000039319](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000039319)

## Data

Gene col 461: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 461); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 461, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 461]; `tensor/DDL_lfc|DDL_z.npy` [461]; `embed/gene_vectors.npy` [461]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 461 or target_col == 461). Every well: [[ZFYVE16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFYVE16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
