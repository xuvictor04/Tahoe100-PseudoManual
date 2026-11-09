---
symbol: "MYCBP2"
type: "gene"
col: 88
ensembl_id: "ENSG00000005810"
name: "MYC binding protein 2"
location: "13q22.3"
module: 216
arm: "+"
pooled_cpm: 210.06
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/216"]
generated_by: "tahoemap"
---

# MYCBP2

*MYC binding protein 2* — 13q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.34× (z +10.7, q 5e-24, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.686× (z -9.4, q 4e-18, down in 32 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (LoVo 0.360×, A498 0.423×, RKO 0.395×, NCI-H460 0.485×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (LOX-IMVI 0.286×, A498 0.389×, SW480 0.414×, LoVo 0.418×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (LOX-IMVI 0.322×, HEC-1-A 0.455×, A498 0.451×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (LoVo 0.484×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMCHD1]] (+0.55, fdr 9e-05), [[STK3]] (+0.55, fdr 5e-05), [[GPHN]] (+0.55, fdr 7e-06); moves opposite to [[HNRNPD-DT]] (-0.55, fdr 1e-04), [[RNF139-DT]] (-0.53, fdr 2e-05), [[LINC00674]] (-0.52, fdr 1e-05).
> It is in [[Module 216]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 88.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +10.7 | 5e-24 | 29/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.47×** | +9.9 | 1e-20 | 43/48 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +9.8 | 1e-20 | 35/48 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.41×** | +8.9 | 9e-17 | 40/48 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.32×** | +7.2 | 8e-11 | 33/48 (CFPAC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +6.8 | 8e-10 | 29/48 (MIA PaCa-2, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +6.3 | 3e-08 | 35/48 (SNU-423, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +5.8 | 4e-07 | 20/48 (SW1417, Hs 766T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.25×** | +5.8 | 4e-07 | 27/48 (NCI-H2347, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +5.0 | 3e-05 | 25/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.22×** | +4.8 | 7e-05 | 23/48 (PANC-1, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +4.8 | 9e-05 | 27/47 (Hs 766T, NCI-H2347, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +4.7 | 1e-04 | 33/49 (LS 180, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~10% of this change | 1.19× | +4.3 | 9e-04 | 21/47 (COLO 205, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.8 | 0.005 | 9/48 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.15× | +3.4 | 0.021 | 8/48 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.085 | 18/48 (HOP62, NCI-H23, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 88.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (LoVo 0.360×, A498 0.423×, RKO 0.395×, NCI-H460 0.485×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (LOX-IMVI 0.286×, A498 0.389×, SW480 0.414×, LoVo 0.418×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (LOX-IMVI 0.322×, HEC-1-A 0.455×, A498 0.451×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (LoVo 0.484×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.686×** | -9.4 | 4e-18 | 32/44 (LOX-IMVI, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.698×** | -9.0 | 9e-17 | 39/47 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.692×** | -8.8 | 3e-16 | 30/45 (LOX-IMVI, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.737×** | -7.9 | 4e-13 | 31/49 (LoVo, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.673×** | -5.3 | 1e-05 | 21/38 (HS-578T, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.892× | -4.2 | 0.002 | 11/49 (Panc 03.27, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.851× | -4.2 | 0.002 | 20/48 (LoVo, Panc 03.27, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | 0.856× | -4.0 | 0.004 | 15/48 (PANC-1, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.876× | -3.4 | 0.036 | 12/48 (AN3 CA, SW48, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.881× | -3.3 | 0.057 | 12/48 (C-33 A, SW 1088, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.884× | -3.2 | 0.066 | 10/48 (LS 180, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 88. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 461 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.50× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.414× (z -16.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 119 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +13.8) | — |
| [[PANC-1 (line)]] | alt | 154 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +23.8) | — |
| [[A498 (line)]] | wt | 311 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.389× (z -16.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 87.2 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.43× (z +10.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 245 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.455× (z -15.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 223 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.420× (z -12.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 227 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.484× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 362 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -18.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 149 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.11× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 159 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +16.2) | — |
| [[NCI-H460 (line)]] | wt | 221 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.485× (z -13.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 345 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -14.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 224 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +18.9) | — |
| [[Panc 03.27 (line)]] | alt | 329 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.524× (z -10.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 259 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 142 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +14.5) | — |
| [[AsPC-1 (line)]] | alt | 97.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.1) | — |
| [[COLO 205 (line)]] | alt | 389 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.452× (z -10.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 117 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 142 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 1.79× (z +8.6) | [[Lonafarnib (drug)]] 5 µM 0.184× (z -13.2) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 202 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.06× (z +9.3) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 5 µM 0.488× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 255 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.540× (z -11.0) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 142 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.80× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.653× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 152 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.427× (z -12.5) ⚠ toxic |
| [[A-172 (line)]] | wt | 161 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -12.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 155 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 126 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.4) | — |
| [[C32 (line)]] | wt | 223 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.532× (z -8.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 172 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.451× (z -8.6) ⚠ toxic |
| [[HCT15 (line)]] | alt | 213 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.01× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 254 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 132 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +12.0) | — |
| [[SNU-1 (line)]] | wt | 271 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.5) | — |
| [[SNU-423 (line)]] | alt | 153 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.94× (z +9.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW 900 (line)]] | alt | 157 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.00× (z +8.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[AN3 CA (line)]] | alt | 234 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 242 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 163 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 301 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 173 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 270 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 88), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMCHD1]] | +0.55 | +0.36 / +0.61 | both halves | 9e-05 |  |
| [[STK3]] | +0.55 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[GPHN]] | +0.55 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[HSD17B10]] ⚠ | +0.54 | +0.55 / +0.46 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ROCK2]] | +0.54 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[USP25]] | +0.51 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[PRH1]] | +0.51 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[VPS13B]] | +0.51 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[XRN2]] | +0.51 | +0.29 / +0.58 | both halves | 2e-04 |  |
| [[VPS13C]] | +0.50 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[EIF4G3]] | +0.50 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[FAF1]] | +0.50 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[DDX10]] | +0.49 | +0.51 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPD-DT]] | -0.55 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[RNF139-DT]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[LINC00674]] | -0.52 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[C1orf52]] | -0.52 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[LINC02210-CRHR1]] | -0.52 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[ABCC11]] | -0.51 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[SDHAP4-1]] | -0.51 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[LINC01772]] | -0.51 | -0.24 / -0.61 | both halves | 4e-04 |  |
| [[ZNF418]] | -0.51 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[UBOX5]] | -0.50 | -0.47 / -0.52 | both halves | 2e-05 | same gene group |
| [[CAPN1-AS1]] | -0.50 | -0.31 / -0.62 | both halves | 2e-04 |  |
| [[CCNY-AS1]] | -0.49 | -0.35 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 216]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.606). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.1, 16.2); signed map (10.8, -8.9). **Vector** length 112, 34.4% of its response variance represented; |z| ≥ 3 in 1,224 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.5 | +6.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.1 | +9.8 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | +3.1 | +2.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.9 | +2.2 |
|  | [[Busulfan (drug)]] 5 µM |  | +2.8 | +2.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.7 | -9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -8.6 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.6 | -8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.6 | -4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -6.9 | -1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.2 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -4.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.3 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | MYC binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q22.3 — chr13:77,042,474-77,327,094 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAM, KIAA0916, FLJ10106, PHR1 |
| Gene groups (HGNC) | Ring finger proteins; Atypical E3 ubiquitin ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [O75592](https://www.uniprot.org/uniprotkb/O75592) (E3 ubiquitin-protein ligase MYCBP2):

> Atypical E3 ubiquitin-protein ligase which specifically mediates ubiquitination of threonine and serine residues on target proteins, instead of ubiquitinating lysine residues. Shows esterification activity towards both threonine and serine, with a preference for threonine, and acts via two essential catalytic cysteine residues that relay ubiquitin to its substrate via thioester intermediates. Interacts with the E2 enzymes UBE2D1, UBE2D3, UBE2E1 and UBE2L3. Plays a key role in neural …

**Summary**, from NCBI Gene [23077](https://www.ncbi.nlm.nih.gov/gene/23077):

> This gene encodes an E3 ubiquitin-protein ligase and member of the PHR (Phr1/MYCBP2, highwire and RPM-1) family of proteins. The encoded protein plays a role in axon guidance and synapse formation in the developing nervous system. In mammalian cells, this protein regulates the cAMP and mTOR signaling pathways, and may additionally regulate autophagy. Reduced expression of this gene has been observed in acute lymphoblastic leukemia patients and a mutation in this gene has been identified in …

**Accessions** — [HGNC:23386](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23386) · Entrez [23077](https://www.ncbi.nlm.nih.gov/gene/23077) · UniProt [O75592](https://www.uniprot.org/uniprotkb/O75592) · Ensembl [ENSG00000005810](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005810)

## Data

Gene col 88: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 88); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 88, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 88]; `tensor/DDL_lfc|DDL_z.npy` [88]; `embed/gene_vectors.npy` [88]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 88 or target_col == 88). Every well: [[MYCBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYCBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
