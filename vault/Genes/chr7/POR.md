---
symbol: "POR"
type: "gene"
col: 4846
ensembl_id: "ENSG00000127948"
name: "cytochrome p450 oxidoreductase"
location: "7q11.23"
module: 93
arm: "+"
pooled_cpm: 71.42
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 3
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# POR

*cytochrome p450 oxidoreductase* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.94× (z +21.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.927× (z -4.1, q 0.022, down in 0 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.639× (z -3.7, q 0.038, down in 24 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.198×, Panc 03.27 0.277×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (LS 180 0.343×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (A498 0.598×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM53C]] (+0.76, fdr 7e-06), [[SLC9A1]] (+0.72, fdr 7e-06), [[GTF2B]] (+0.69, fdr 7e-06); moves opposite to [[NHLRC2]] (-0.61, fdr 7e-05), [[MTPAP]] (-0.54, fdr 1e-04), [[FAM174A-DT]] (-0.52, fdr 1e-04).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4846.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.94×** | +21.9 | 0e+00 | 48/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +19.8 | 0e+00 | 45/49 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.13×** | +18.2 | 0e+00 | 48/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.82×** | +16.5 | 0e+00 | 48/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +12.3 | 7e-33 | 37/48 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +10.1 | 5e-22 | 42/48 (KATO III, A498, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +8.6 | 5e-16 | 41/48 (LoVo, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.65×** | +7.7 | 1e-12 | 35/47 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +7.3 | 2e-11 | 38/48 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.46×** | +5.9 | 3e-07 | 28/48 (NCI-H460, H4, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +5.6 | 9e-07 | 34/48 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.43×** | +5.5 | 1e-06 | 28/50 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.5 | 2e-06 | 26/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +5.3 | 4e-06 | 36/48 (KATO III, LoVo, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.39×** | +5.3 | 5e-06 | 30/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +4.4 | 4e-04 | 27/49 (KATO III, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.65×** | +4.2 | 9e-04 | 26/49 (AsPC-1, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.65×** | +4.2 | 9e-04 | 29/48 (Panc 03.27, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.006 | 21/49 (NCI-H460, KATO III, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4846.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.198×, Panc 03.27 0.277×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (LS 180 0.343×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (A498 0.598×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -4.1 | 0.022 | 0/49 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.768×** | -3.9 | 0.030 | 22/44 (RKO, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.639×** | -3.7 | 0.038 | 24/49 (NCI-H1792, AN3 CA, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.796×** | -3.5 | 0.069 | 23/47 (NCI-H1792, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4846. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 44.9 | 8 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +20.4) | — |
| [[A498 (line)]] | wt | 155 | 5 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +20.0) | [[Vinblastine (sulfate) (drug)]] 5 µM 0.598× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 89.0 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +19.8) | — |
| [[LoVo (line)]] | wt | 88.5 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +17.3) | — |
| [[PANC-1 (line)]] | alt | 48.2 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.06× (z +19.0) | — |
| [[HT-29 (line)]] | alt | 75.3 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +15.9) | — |
| [[J82 (line)]] | alt | 53.7 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +14.8) | — |
| [[KATO III (line)]] | alt | 113 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 5.01× (z +18.0) | — |
| [[Panc 03.27 (line)]] | alt | 82.4 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.48× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -10.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 151 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 3.85× (z +14.6) | — |
| [[SW480 (line)]] | alt | 69.1 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 6.24× (z +17.7) | — |
| [[A-172 (line)]] | wt | 53.0 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +14.2) | — |
| [[CFPAC-1 (line)]] | alt | 79.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +17.0) | — |
| [[HOP62 (line)]] | alt | 43.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +15.0) | — |
| [[SK-MEL-2 (line)]] | alt | 58.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.89× (z +14.6) | — |
| [[SNU-423 (line)]] | alt | 54.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.12× (z +11.8) | — |
| [[A549 (line)]] | wt | 45.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.63× (z +17.0) | — |
| [[HEC-1-A (line)]] | alt | 77.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +15.3) | — |
| [[Hs 766T (line)]] | wt | 36.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.44× (z +13.9) | — |
| [[HS-578T (line)]] | alt | 42.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.20× (z +12.0) | — |
| [[LOX-IMVI (line)]] | wt | 36.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.69× (z +12.7) | — |
| [[LS 180 (line)]] | wt | 80.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.02× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.343× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 82.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +20.3) | — |
| [[NCI-H23 (line)]] | alt | 37.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +16.3) | — |
| [[RKO (line)]] | wt | 51.0 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +13.6) | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -12.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 67.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.47× (z +10.4) | — |
| [[A-427 (line)]] | wt | 62.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.72× (z +13.3) | — |
| [[C-33 A (line)]] | alt | 61.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +10.1) | — |
| [[H4 (line)]] | wt | 42.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.34× (z +11.2) | — |
| [[HCT15 (line)]] | alt | 86.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 57.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 111 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.38× (z +12.8) | — |
| [[NCI-H2030 (line)]] | alt | 49.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.45× (z +12.1) | — |
| [[RPMI-7951 (line)]] | alt | 43.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.02× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 32.1 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.11× (z +10.2) | — |
| [[SW48 (line)]] | wt | 64.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +10.7) | — |
| [[C32 (line)]] | wt | 113 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +11.4) | — |
| [[hTERT-HPNE (line)]] | wt | 44.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +11.4) | — |
| [[NCI-H2347 (line)]] | alt | 74.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.76× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 85.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +11.8) | — |
| [[HepG2_C3A (line)]] | wt | 211 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.91× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 36.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4846), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM53C]] | +0.76 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[SLC9A1]] | +0.72 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[GTF2B]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[LRRC23]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[LGMN]] | +0.64 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[CNNM4]] | +0.62 | +0.57 / +0.64 | both halves | 1e-05 | same gene group |
| [[IFRD1]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[DHDH]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 | same gene group |
| [[LPIN2]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[SPSB1]] | +0.59 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[SPSB2]] | +0.59 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[NOSIP]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHLRC2]] | -0.61 | -0.38 / -0.58 | both halves | 7e-05 |  |
| [[MTPAP]] | -0.54 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[FAM174A-DT]] | -0.52 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[SLC25A24]] | -0.51 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[B3GALT9]] | -0.51 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[MSL2]] | -0.49 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[CEP41]] | -0.49 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[ZNF839]] | -0.49 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[EXOSC10]] | -0.49 | -0.32 / -0.55 | both halves | 1e-04 |  |
| [[MRRF]] | -0.49 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[ATAD1]] | -0.48 | -0.29 / -0.53 | both halves | 3e-04 |  |
| [[PIGK]] | -0.48 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers POR's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.747). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.4, -26.1); signed map (3.1, 17.0). **Vector** length 105, 31.0% of its response variance represented; |z| ≥ 3 in 1,205 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +10.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.0 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +4.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +3.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +3.2 | +1.6 |
|  | [[Auranofin (drug)]] 0.5 µM |  | +2.9 | +3.2 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.4 | -3.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.9 | -3.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.8 | -3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.9 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.3 | -1.1 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -2.7 | -2.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome p450 oxidoreductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:75,899,200-75,986,855 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CYPOR, FLJ26468 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Small nucleolar RNA protein coding host genes; Flavoproteins; Oxidoreductases |
| Hallmark sets | XENOBIOTIC_METABOLISM, ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Cytochrome P450 - arranged by substrate type; Phase I - Functionalization of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [P16435](https://www.uniprot.org/uniprotkb/P16435) (NADPH--cytochrome P450 reductase):

> This enzyme is required for electron transfer from NADP to cytochrome P450 in microsomes. It can also provide electron transfer to heme oxygenase and cytochrome B5.

**Summary**, from NCBI Gene [5447](https://www.ncbi.nlm.nih.gov/gene/5447):

> This gene encodes an endoplasmic reticulum membrane oxidoreductase that is essential for multiple metabolic processes, including reactions catalyzed by cytochrome P450 proteins for metabolism of steroid hormones, drugs and xenobiotics. The encoded protein has a flavin adenine dinucleotide (FAD)-binding domain and a flavodoxin-like domain which bind two cofactors, FAD and FMN, that allow it to donate electrons directly from NADPH to all microsomal P450 enzymes. Mutations in this gene cause a …

**Accessions** — [HGNC:9208](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9208) · Entrez [5447](https://www.ncbi.nlm.nih.gov/gene/5447) · UniProt [P16435](https://www.uniprot.org/uniprotkb/P16435) · Ensembl [ENSG00000127948](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127948)

## Data

Gene col 4846: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4846); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4846, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4846]; `tensor/DDL_lfc|DDL_z.npy` [4846]; `embed/gene_vectors.npy` [4846]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4846 or target_col == 4846). Every well: [[POR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
