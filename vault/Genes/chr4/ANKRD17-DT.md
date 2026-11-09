---
symbol: "ANKRD17-DT"
type: "gene"
col: 14673
ensembl_id: "ENSG00000250220"
name: "ANKRD17 divergent transcript"
location: "4q13.3"
module: 23
arm: "+"
pooled_cpm: 18.05
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 16
n_dd_up_clean: 11
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ANKRD17-DT

*ANKRD17 divergent transcript* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.33× (z +17.6, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.455× (z -8.1, q 2e-13, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHD1-DT]] (+0.89, fdr 7e-06), [[RFX3-DT]] (+0.85, fdr 1e-05), [[DNAI4]] (+0.85, fdr 7e-06); moves opposite to [[NDRG3]] (-0.71, fdr 1e-05), [[WASF3]] (-0.71, fdr 2e-04), [[CAMK2G]] (-0.70, fdr 2e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14673.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.33×** | +17.6 | 0e+00 | 45/46 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.87×** | +10.5 | 3e-23 | 40/45 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +6.8 | 2e-09 | 33/47 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +6.4 | 2e-08 | 32/47 (SHP-77, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +6.4 | 2e-08 | 32/47 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +6.1 | 1e-07 | 31/42 (CFPAC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +5.6 | 2e-06 | 29/45 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +4.4 | 6e-04 | 25/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +4.3 | 0.001 | 19/47 (NCI-H2030, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.43×** | +3.7 | 0.012 | 21/47 (LS 180, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +3.5 | 0.023 | 18/47 (LoVo, NCI-H460, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +3.5 | 0.024 | 20/47 (BT-474, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.26× | +3.0 | 0.10 | 15/48 (SW480, NCI-H23, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14673.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.455×** | -8.1 | 2e-13 | 43/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.464×** | -7.6 | 6e-12 | 30/43 (NCI-H23, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.544×** | -6.3 | 5e-08 | 33/47 (PANC-1, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.333×** | -6.0 | 4e-07 | 36/48 (NCI-H23, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.552×** | -5.8 | 7e-07 | 36/47 (PANC-1, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.379×** | -5.3 | 1e-05 | 28/44 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.639×** | -4.6 | 3e-04 | 27/46 (A-427, HOP62, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.648×** | -4.5 | 5e-04 | 23/45 (PANC-1, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.691×** | -3.8 | 0.008 | 21/48 (NCI-H1792, BT-474, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **0.702×** | -3.7 | 0.014 | 20/45 (HCT15, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.711×** | -3.5 | 0.020 | 19/48 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.717×** | -3.4 | 0.026 | 17/48 (HCT15, SW480, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.797×** | -3.3 | 0.036 | 14/48 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.650×** | -3.2 | 0.058 | 16/47 (SW 1088, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.574×** | -3.0 | 0.099 | 12/46 (RPMI-7951, H4, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14673. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 22.7 | 3 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +13.9) | [[Digitoxin (drug)]] 0.5 µM 0.243× (z -11.5) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.264× (z -10.9) |
| [[PANC-1 (line)]] | alt | 15.5 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +11.5) | [[Ixazomib citrate (drug)]] 0.5 µM 0.158× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 59.7 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.172× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 22.5 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.89× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.265× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 6.50 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +13.9) | [[Nimesulide (drug)]] 5 µM 0.0802× (z -9.9) ⚠ toxic; unreliable plate only |
| [[KATO III (line)]] | alt | 23.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.187× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 14.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +14.1) | [[Digitoxin (drug)]] 5 µM 0.190× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[MIA PaCa-2 (line)]] | alt | 8.56 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.38× (z +12.2) | — |
| [[NCI-H2030 (line)]] | alt | 7.59 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.28× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 20.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +12.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.105× (z -12.9) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 14.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +9.7) | [[Ixazomib citrate (drug)]] 5 µM 0.265× (z -8.6) |
| [[A549 (line)]] | wt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 16.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +11.0) | — |
| [[C32 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.120× (z -10.2) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +10.6) | — |
| [[COLO 205 (line)]] | alt | 18.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 30.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 28.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +13.6) | — |
| [[HOP62 (line)]] | alt | 26.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 15.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 14.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 9.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.49× (z +11.2) | — |
| [[hTERT-HPNE (line)]] | wt | 20.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0708× (z -11.6) ⚠ toxic |
| [[J82 (line)]] | alt | 9.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 16.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 29.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 9.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.39× (z +11.3) | — |
| [[RKO (line)]] | wt | 23.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +12.5) | — |
| [[RPMI-7951 (line)]] | alt | 17.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.84× (z +11.2) | — |
| [[A-172 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14673), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHD1-DT]] | +0.89 | +0.89 / +0.76 | both halves | 7e-06 | same gene group |
| [[RFX3-DT]] | +0.85 | +0.90 / +0.56 | both halves | 1e-05 | same gene group |
| [[DNAI4]] | +0.85 | +0.85 / +0.64 | both halves | 7e-06 |  |
| [[HEXIM2-AS1]] | +0.85 | +0.86 / +0.57 | both halves | 1e-05 |  |
| [[BDNF-AS]] | +0.84 | +0.86 / +0.62 | both halves | 7e-06 |  |
| [[PRANCR]] | +0.82 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[MAD2L1-DT]] | +0.81 | +0.79 / +0.55 | both halves | 1e-05 | same gene group |
| [[LINC01004]] | +0.81 | +0.80 / +0.51 | both halves | 1e-05 |  |
| [[MAILR]] | +0.80 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[CASS4]] | +0.79 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[MFF-DT]] | +0.79 | +0.77 / +0.39 | both halves | 6e-05 | same gene group |
| [[OXA1L-DT]] | +0.79 | +0.79 / +0.53 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG3]] | -0.71 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[WASF3]] | -0.71 | -0.72 / -0.31 | both halves | 2e-04 |  |
| [[CAMK2G]] | -0.70 | -0.68 / -0.32 | both halves | 2e-04 |  |
| [[MAST3]] | -0.68 | -0.59 / -0.26 | both halves | 4e-04 |  |
| [[ARRB2]] | -0.67 | -0.55 / -0.26 | both halves | 4e-04 |  |
| [[MPP1]] | -0.67 | -0.52 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANKRD17-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RNF217-AS1]] | B | RNF217-AS1 activity raises ANKRD17-DT's level | lines that do not express RNF217-AS1 (9) vs lines expressing it (41) | 1.50× lower at baseline in the lines without RNF217-AS1 | 0.064 | ⚠ within organs, on part of the lines; also absent: RNF217, LRP12, CCDC149; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.847). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.4, 17.1); signed map (26.2, -8.3). **Vector** length 109, 30.1% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +17.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.7 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.7 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.1 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +1.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -7.7 | -3.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.8 | -1.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -1.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.5 | -1.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.4 | -4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.7 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -6.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | -3.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ANKRD17 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q13.3 — chr4:73,259,209-73,317,953 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55556](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55556) · Entrez [102724832](https://www.ncbi.nlm.nih.gov/gene/102724832) · Ensembl [ENSG00000250220](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250220)

## Data

Gene col 14673: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14673); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14673, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14673]; `tensor/DDL_lfc|DDL_z.npy` [14673]; `embed/gene_vectors.npy` [14673]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14673 or target_col == 14673). Every well: [[ANKRD17-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD17-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
