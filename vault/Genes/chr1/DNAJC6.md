---
symbol: "DNAJC6"
type: "gene"
col: 3818
ensembl_id: "ENSG00000116675"
name: "DnaJ heat shock protein family (Hsp40) member C6"
location: "1p31.3"
module: 38
arm: "+"
pooled_cpm: 47.2
n_lines_expressing: 47
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# DNAJC6

*DnaJ heat shock protein family (Hsp40) member C6* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.60× (z +16.9, q 0e+00, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.478× (z -12.5, q 5e-33, down in 21 of 37 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SHP-77 0.165×, PANC-1 0.174×, A-427 0.169×, C-33 A 0.124×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (C-33 A 0.0406×, RPMI-7951 0.130×, NCI-H23 0.169×, RKO 0.221×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.200×; ⚠ cell-cycle shift, explains ~0% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (C32 0.174×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (BT-474 0.209×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HEC-1-A 0.542×).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC03016]] (+0.55, fdr 3e-05), [[CDKL1]] (+0.53, fdr 1e-04), [[PCOLCE2]] (+0.51, fdr 2e-04); moves opposite to [[ALDH6A1]] (-0.54, fdr 3e-05), [[PXMP4]] (-0.48, fdr 3e-04), [[UBAC1]] (-0.48, fdr 5e-04).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CABYR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3818.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.60×** | +16.9 | 0e+00 | 38/45 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +16.0 | 0e+00 | 34/45 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.20×** | +13.9 | 1e-41 | 38/45 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.10×** | +13.1 | 5e-37 | 35/45 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +13.0 | 1e-36 | 31/45 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +12.6 | 1e-34 | 40/45 (PANC-1, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +9.7 | 3e-20 | 34/45 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +9.0 | 1e-17 | 40/45 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +8.0 | 7e-14 | 27/45 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.63×** | +7.5 | 4e-12 | 34/44 (CFPAC-1, HOP62, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.0 | 1e-10 | 26/44 (C32, LS 180, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.30×** | +6.6 | 3e-09 | 26/45 (CFPAC-1, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.94×** | +5.8 | 3e-07 | 27/45 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.41×** | +5.8 | 3e-07 | 27/44 (CFPAC-1, hTERT-HPNE, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.30×** | +4.4 | 4e-04 | 19/45 (C32, LS 180, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.002 | 22/45 (HOP62, RKO, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.58×** | +4.0 | 0.002 | 15/45 (C32, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.007 | 16/45 (SK-MEL-2, HS-578T, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.023 | 17/45 (C32, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3818.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SHP-77 0.165×, PANC-1 0.174×, A-427 0.169×, C-33 A 0.124×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (C-33 A 0.0406×, RPMI-7951 0.130×, NCI-H23 0.169×, RKO 0.221×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.200×; ⚠ cell-cycle shift, explains ~0% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (C32 0.174×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (BT-474 0.209×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HEC-1-A 0.542×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.478×** | -12.5 | 5e-33 | 21/37 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.552×** | -9.1 | 3e-17 | 30/43 (C-33 A, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.602×** | -8.6 | 1e-15 | 28/44 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **0.723×** | -5.7 | 2e-06 | 24/43 (H4, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.757×** | -4.9 | 1e-04 | 24/44 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.784×** | -4.0 | 0.007 | 22/42 (RPMI-7951, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.647×** | -3.8 | 0.013 | 19/43 (NCI-H2347, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3818. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 35.1 | 4 | 6 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 3.81× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.174× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 68.8 | 3 | 6 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +11.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.356× (z -11.8) ⚠ toxic |
| [[J82 (line)]] | alt | 38.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.23× (z +24.3) | — |
| [[H4 (line)]] | wt | 183 | 2 (2 ⚠) | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.11× (z +11.9) ⚠ cell-cycle shift, explains ~94% of this change | [[Dinaciclib (drug)]] 5 µM 0.184× (z -13.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 22.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +13.4) | — |
| [[AsPC-1 (line)]] | alt | 12.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +12.9) | — |
| [[HEC-1-A (line)]] | alt | 54.2 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.89× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.374× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.542× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 32.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +12.8) | — |
| [[RPMI-7951 (line)]] | alt | 70.4 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -13.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 29.6 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +8.5) | [[Canagliflozin (drug)]] 0.05 µM 0.174× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 19.6 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +11.9) | — |
| [[HS-578T (line)]] | alt | 60.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 18.2 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.08× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 21.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +12.4) | — |
| [[Panc 03.27 (line)]] | alt | 25.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +12.7) | — |
| [[SW 900 (line)]] | alt | 48.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -10.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 79.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.468× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 25.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.43× (z +9.0) | — |
| [[A-427 (line)]] | wt | 64.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -16.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 60.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -9.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 29.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +14.1) | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.209× (z -9.2) |
| [[C-33 A (line)]] | alt | 110 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0406× (z -21.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 38.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 58.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -12.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 37.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +15.2) | — |
| [[HCT15 (line)]] | alt | 41.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -9.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 47.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +10.9) | — |
| [[KATO III (line)]] | alt | 48.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 25.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.71× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 39.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +12.0) | — |
| [[RKO (line)]] | wt | 55.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -10.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -20.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 28.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.02× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 65.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +8.5) | — |
| [[A549 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.85 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.32 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3818), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC03016]] | +0.55 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[CDKL1]] | +0.53 | +0.62 / +0.32 | both halves | 1e-04 |  |
| [[PCOLCE2]] | +0.51 | +0.32 / +0.45 | both halves | 2e-04 |  |
| [[CABYR]] | +0.51 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[THSD1]] | +0.48 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[NIPAL1]] | +0.47 | +0.44 / +0.32 | both halves | 1e-04 |  |
| [[NABP1]] | +0.46 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[KIF21A]] | +0.46 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[SLCO5A1]] | +0.46 | +0.53 / +0.34 | both halves | 1e-04 |  |
| [[LINC01619]] | +0.46 | +0.43 / +0.30 | both halves | 2e-04 |  |
| [[HDX]] | +0.45 | +0.52 / +0.24 | both halves | 4e-04 |  |
| [[LRIF1]] | +0.45 | +0.46 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH6A1]] | -0.54 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[PXMP4]] | -0.48 | -0.33 / -0.27 | both halves | 3e-04 |  |
| [[UBAC1]] | -0.48 | -0.54 / -0.24 | both halves | 5e-04 |  |
| [[ATF6B]] | -0.47 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[HDGFL2]] | -0.47 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[DDX42]] | -0.47 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[RMDN3]] | -0.46 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[VPS26B]] | -0.46 | -0.44 / -0.19 | ⚠ not reproduced | 9e-04 |  |
| [[NDUFV1]] | -0.45 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[BAG4]] | -0.45 | -0.55 / -0.22 | both halves | 6e-04 |  |
| [[BACE1]] | -0.45 | -0.09 / -0.30 | ⚠ not reproduced | 0.003 |  |
| [[ADD1]] | -0.44 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[RAB40B]] | -0.43 | -0.53 / -0.27 | both halves | 3e-04 |  |
| [[TTLL5]] | -0.42 | -0.38 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CABYR]] | B | CABYR activity raises DNAJC6's level | lines that do not express CABYR (6) vs lines expressing it (44) | 2.09× lower at baseline in the lines without CABYR | 0.012 | ⚠ within organs, on part of the lines; also absent: SUGCT, GABBR1, CLTCL1; maybe low, not absent |
| [[KLHL29]] | B | KLHL29 activity raises DNAJC6's level | lines that do not express KLHL29 (7) vs lines expressing it (43) | 2.33× lower at baseline in the lines without KLHL29 | 0.033 | ⚠ within organs, on part of the lines; also absent: PCNX2, ENSG00000229983, ENSG00000271204; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.282). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.7, -23.4); signed map (16.7, 5.0). **Vector** length 69.5, 14.1% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +12.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +8.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.8 | +7.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | +3.6 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +3.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.4 | -8.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.1 | +13.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.0 | +16.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.7 | +13.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Pentamidine (isethionate) (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.3 | -1.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:65,248,219-65,415,871 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0473, PARK19 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins; C2 tensin-type domain containing |
| Reactome | 6 pathways, smallest: Lysosome Vesicle Biogenesis; Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding |
| Matched by | ensembl_id |

**Function**, from UniProt [O75061](https://www.uniprot.org/uniprotkb/O75061) (Auxilin):

> May act as a protein phosphatase and/or a lipid phosphatase. Co-chaperone that recruits HSPA8/HSC70 to clathrin-coated vesicles (CCVs) and promotes the ATP-dependent dissociation of clathrin from CCVs and participates in clathrin-mediated endocytosis of synaptic vesicles and their recycling and also in intracellular trafficking. Firstly, binds tightly to the clathrin cages, at a ratio of one DNAJC6 per clathrin triskelion. The HSPA8:ATP complex then binds to the clathrin-auxilin cage, initially …

**Summary**, from NCBI Gene [9829](https://www.ncbi.nlm.nih.gov/gene/9829):

> DNAJC6 belongs to the evolutionarily conserved DNAJ/HSP40 family of proteins, which regulate molecular chaperone activity by stimulating ATPase activity. DNAJ proteins may have up to 3 distinct domains: a conserved 70-amino acid J domain, usually at the N terminus, a glycine/phenylalanine (G/F)-rich region, and a cysteine-rich domain containing 4 motifs resembling a zinc finger domain (Ohtsuka and Hata, 2000 [PubMed 11147971]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:15469](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15469) · Entrez [9829](https://www.ncbi.nlm.nih.gov/gene/9829) · UniProt [O75061](https://www.uniprot.org/uniprotkb/O75061) · Ensembl [ENSG00000116675](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116675)

## Data

Gene col 3818: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3818); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3818, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3818]; `tensor/DDL_lfc|DDL_z.npy` [3818]; `embed/gene_vectors.npy` [3818]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3818 or target_col == 3818). Every well: [[DNAJC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
