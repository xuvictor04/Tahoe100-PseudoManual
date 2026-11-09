---
symbol: "PCSK5"
type: "gene"
col: 1779
ensembl_id: "ENSG00000099139"
name: "proprotein convertase subtilisin/kexin type 5"
location: "9q21.13"
module: 8
arm: "+"
pooled_cpm: 112.75
n_lines_expressing: 26
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PCSK5

*proprotein convertase subtilisin/kexin type 5* — 9q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.22× (z +24.7, q 0e+00, up in 19 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.821× (z -4.3, q 0.009, down in 19 of 24 measured lines) ⚠ transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 0.251×, SW1417 0.262×, KATO III 0.278×, NCI-H1792 0.220×, …; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A549 0.437×, SW1417 0.467×, COLO 205 0.461×); [[Docetaxel (drug)]] 0.05 µM in 2 lines (KATO III 0.250×, HT-29 0.317×; ⚠ transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (KATO III 0.360×, SW1417 0.378×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A549 0.372×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SORBS1]] (+0.57, fdr 1e-05), [[MAN1A1]] (+0.56, fdr 1e-05), [[CEMIP2]] (+0.53, fdr 3e-05); moves opposite to [[LINC01535]] (-0.44, fdr 1e-04), [[BCL7C]] (-0.44, fdr 7e-05), [[CDC23]] (-0.42, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FRMD4B]] → it (grade B ⚠); 4 go from it, the strongest it → [[NRG4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1779.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.22×** | +24.7 | 0e+00 | 19/24 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.96×** | +20.8 | 0e+00 | 20/24 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +18.7 | 0e+00 | 13/25 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.82×** | +13.1 | 4e-37 | 19/25 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +12.0 | 3e-31 | 14/24 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.69×** | +11.3 | 7e-28 | 16/23 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +9.6 | 5e-20 | 13/24 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +8.8 | 6e-17 | 10/26 (LoVo, H4, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +6.9 | 3e-10 | 13/24 (HT-29, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.37×** | +6.8 | 5e-10 | 7/24 (LoVo, HCT15, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.55×** | +6.8 | 5e-10 | 11/25 (LoVo, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +6.7 | 8e-10 | 10/24 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.31×** | +5.7 | 4e-07 | 12/24 (H4, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.29×** | +5.6 | 8e-07 | 6/24 (LoVo, SW 900, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.29×** | +5.6 | 8e-07 | 8/24 (LoVo, SW 900, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +5.3 | 5e-06 | 9/25 (RKO, LS 180, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.47×** | +4.4 | 3e-04 | 9/24 (A498, RKO, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.46×** | +4.4 | 4e-04 | 15/24 (COLO 205, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 4e-04 | 6/23 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.7 | 0.007 | 10/24 (HT-29, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1779.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 0.251×, SW1417 0.262×, KATO III 0.278×, NCI-H1792 0.220×, …; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A549 0.437×, SW1417 0.467×, COLO 205 0.461×); [[Docetaxel (drug)]] 0.05 µM in 2 lines (KATO III 0.250×, HT-29 0.317×; ⚠ transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (KATO III 0.360×, SW1417 0.378×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A549 0.372×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.821×** | -4.3 | 0.009 | 19/24 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | 0.865× | -3.2 | 0.25 | 7/24 (HCT15, SNU-1, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.860× | -3.2 | 0.25 | 3/24 (KATO III, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.866× | -3.0 | 0.25 | 16/23 (SW480, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.871× | -3.0 | 0.25 | 11/24 (A549, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1779. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 147 | 7 (2 ⚠) | 1 | [[Peretinoin (drug)]] 5 µM 4.49× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.6) |
| [[LoVo (line)]] | wt | 123 | 8 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +21.4) | — |
| [[SW480 (line)]] | alt | 268 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 236 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +24.4) | — |
| [[KATO III (line)]] | alt | 403 | 0 | 6 (4 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.250× (z -14.0) ⚠ transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.360× (z -10.3) |
| [[SW1417 (line)]] | alt | 448 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -11.4) |
| [[HT-29 (line)]] | alt | 139 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.86× (z +12.3) | [[Docetaxel (drug)]] 0.05 µM 0.317× (z -10.5) ⚠ transcription drop |
| [[A549 (line)]] | wt | 365 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -12.3) |
| [[NCI-H1792 (line)]] | alt | 142 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 132 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 46.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +18.9) | — |
| [[AsPC-1 (line)]] | alt | 321 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +16.3) | [[Dinaciclib (drug)]] 0.05 µM 0.428× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[CFPAC-1 (line)]] | alt | 140 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 38.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 449 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 134 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.20× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 55.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +10.4) | — |
| [[RKO (line)]] | wt | 137 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +14.1) | — |
| [[SNU-1 (line)]] | wt | 125 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +9.5) | — |
| [[A-172 (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.4 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 27.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 14.2 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.31 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 25.5 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.98 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 20.1 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 8.39 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 98.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.40 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.71 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 54.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1779), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SORBS1]] | +0.57 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[MAN1A1]] | +0.56 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[CEMIP2]] | +0.53 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[RASEF]] | +0.50 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[HHLA2]] | +0.48 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[CDHR2]] | +0.46 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[MAGI3]] | +0.45 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[CASK]] | +0.45 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[STYK1]] | +0.45 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[MACC1]] | +0.44 | +0.43 / +0.38 | both halves | 6e-05 |  |
| [[ARL15]] | +0.44 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[LARGE1]] | +0.44 | +0.44 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01535]] | -0.44 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[BCL7C]] | -0.44 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[CDC23]] | -0.42 | -0.32 / -0.48 | both halves | 1e-04 |  |
| [[VCPKMT]] | -0.41 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[CROCCP2]] | -0.41 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[ZNF70]] | -0.41 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[STEEP1]] | -0.40 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[CPSF1]] | -0.39 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[TBC1D13]] | -0.39 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[RMDN3]] | -0.39 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[ZNF529]] | -0.38 | -0.29 / -0.45 | both halves | 3e-04 |  |
| [[ZNF283]] | -0.38 | -0.25 / -0.42 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMD4B]] | B | FRMD4B activity raises PCSK5's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 3.12× lower at baseline in the lines without FRMD4B | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[FRK]] | B | FRK activity raises PCSK5's level | lines that do not express FRK (22) vs lines expressing it (28) | 2.76× lower at baseline in the lines without FRK | 0.035 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[HHLA2]] | C | HHLA2 activity raises PCSK5's level | lines that do not express HHLA2 (38) vs lines expressing it (12) | 7.61× lower at baseline in the lines without HHLA2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, TM4SF4, MUC13; co-absent with the target |
| [[RASSF6]] | C | RASSF6 activity raises PCSK5's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 4.27× lower at baseline in the lines without RASSF6 | 0.003 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6; co-absent with the target |
| [[POF1B]] | C | POF1B activity raises PCSK5's level | lines that do not express POF1B (34) vs lines expressing it (16) | 4.29× lower at baseline in the lines without POF1B | 0.005 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRG4]] | B | PCSK5 activity raises NRG4's level | lines that do not express PCSK5 (24) vs lines expressing it (26) | 1.71× lower at baseline in the lines without PCSK5 | 0.073 | ⚠ within organs, on part of the lines; also absent: ALOX5, PIK3AP1, HOXA9 |
| [[SPATA6L]] | B | PCSK5 activity raises SPATA6L's level | lines that do not express PCSK5 (24) vs lines expressing it (26) | 2.38× lower at baseline in the lines without PCSK5 | 0.088 | ⚠ within organs, on part of the lines; also absent: ALOX5, PIK3AP1, HOXA9 |
| [[RASSF6]] | C | PCSK5 activity raises RASSF6's level | lines that do not express PCSK5 (24) vs lines expressing it (26) | 3.99× lower at baseline in the lines without PCSK5 | 0.007 | ⚠ within organs, on part of the lines; also absent: ALOX5, PIK3AP1, HOXA9; co-absent with the target |
| [[HHLA2]] | C | PCSK5 activity raises HHLA2's level | lines that do not express PCSK5 (24) vs lines expressing it (26) | 2.27× lower at baseline in the lines without PCSK5 | 0.035 | ⚠ within organs, on part of the lines; also absent: ALOX5, PIK3AP1, HOXA9; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.370). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.9, 44.1); signed map (54.8, 12.6). **Vector** length 83.9, 22.8% of its response variance represented; |z| ≥ 3 in 777 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +20.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +13.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.3 | +9.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.9 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +24.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +3.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +6.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +4.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.6 | +5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -2.5 | -3.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.4 | +5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | proprotein convertase subtilisin/kexin type 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.13 — chr9:75,890,644-76,362,975 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PC5, PC6, SPC6 |
| Gene groups (HGNC) | Proprotein convertase subtilisin/kexin family |
| Reactome | 8 pathways, smallest: Expression and Processing of Neurotrophins; NGF processing; Assembly of active LPL and LIPC lipase complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92824](https://www.uniprot.org/uniprotkb/Q92824) (Proprotein convertase subtilisin/kexin type 5):

> Serine endoprotease that processes various proproteins by cleavage at paired basic amino acids, recognizing the RXXX[KR]R consensus motif. Likely functions in the constitutive and regulated secretory pathways. Plays an essential role in pregnancy establishment by proteolytic activation of a number of important factors such as BMP2, CALD1 and alpha-integrins.

**Summary**, from NCBI Gene [5125](https://www.ncbi.nlm.nih.gov/gene/5125):

> This gene encodes a member of the subtilisin-like proprotein convertase family, which includes proteases that process protein and peptide precursors trafficking through regulated or constitutive branches of the secretory pathway. The encoded protein undergoes an initial autocatalytic processing event in the ER to generate a heterodimer which exits the ER. It then sorts to the trans-Golgi network where a second autocatalytic event takes place and the catalytic activity is acquired. This encoded …

**Accessions** — [HGNC:8747](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8747) · Entrez [5125](https://www.ncbi.nlm.nih.gov/gene/5125) · UniProt [Q92824](https://www.uniprot.org/uniprotkb/Q92824) · Ensembl [ENSG00000099139](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099139)

## Data

Gene col 1779: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1779); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1779, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1779]; `tensor/DDL_lfc|DDL_z.npy` [1779]; `embed/gene_vectors.npy` [1779]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1779 or target_col == 1779). Every well: [[PCSK5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCSK5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
