---
symbol: "STPG4"
type: "gene"
col: 14203
ensembl_id: "ENSG00000239605"
name: "sperm-tail PG-rich repeat containing 4"
location: "2p21"
module: 53
arm: "+"
pooled_cpm: 24.8
n_lines_expressing: 48
n_dd_up: 31
n_dd_down: 3
n_dd_up_clean: 27
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# STPG4

*sperm-tail PG-rich repeat containing 4* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 9.10× (z +33.7, q 0e+00, up in 41 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.489× (z -7.3, q 2e-10, down in 31 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (LoVo 0.200×, SW48 0.143×, LS 180 0.218×, KATO III 0.267×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 0.0462×, LoVo 0.0734×, KATO III 0.140×, SW48 0.126×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 3 lines (KATO III 0.237×, H4 0.0667×, NCI-H2030 0.0922×; ⚠ toxic; transcription drop); [[Belinostat (drug)]] 0.5 µM in 2 lines (SW48 0.191×, SW480 0.368×); [[Neratinib (drug)]] 0.5 µM in 1 line (BT-474 0.0470×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (A549 0.0819×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGF18]] (+0.79, fdr 7e-06), [[LINC02955]] (+0.77, fdr 1e-05), [[LINC00880]] (+0.77, fdr 7e-06); moves opposite to [[PSMD9]] (-0.60, fdr 4e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[C21orf91-OT1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14203.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **9.10×** | +33.7 | 0e+00 | 41/43 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.01×** | +24.6 | 0e+00 | 43/45 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **3.40×** | +18.6 | 0e+00 | 38/46 (A-172, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.93×** | +16.5 | 0e+00 | 40/46 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.73×** | +16.1 | 0e+00 | 36/45 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.14×** | +12.3 | 7e-33 | 34/43 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.74×** | +10.9 | 1e-25 | 36/46 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.93×** | +10.0 | 7e-22 | 37/46 (SW480, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.92×** | +10.0 | 1e-21 | 34/46 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **2.29×** | +8.9 | 3e-17 | 41/46 (HEC-1-A, HepG2/C3A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.35×** | +8.9 | 4e-17 | 26/45 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.34×** | +8.8 | 6e-17 | 26/39 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.10×** | +6.6 | 2e-09 | 38/46 (A-172, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.83×** | +6.5 | 4e-09 | 26/45 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.45×** | +5.1 | 2e-05 | 16/29 (SW480, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +4.9 | 3e-05 | 20/46 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +4.9 | 3e-05 | 19/45 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14203.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (LoVo 0.200×, SW48 0.143×, LS 180 0.218×, KATO III 0.267×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 0.0462×, LoVo 0.0734×, KATO III 0.140×, SW48 0.126×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 3 lines (KATO III 0.237×, H4 0.0667×, NCI-H2030 0.0922×; ⚠ toxic; transcription drop); [[Belinostat (drug)]] 0.5 µM in 2 lines (SW48 0.191×, SW480 0.368×); [[Neratinib (drug)]] 0.5 µM in 1 line (BT-474 0.0470×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (A549 0.0819×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.489×** | -7.3 | 2e-10 | 31/44 (SW48, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.706×** | -3.8 | 0.034 | 20/45 (KATO III, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | **0.656×** | -3.7 | 0.034 | 3/46 (NCI-H2030, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 0.738× | -3.3 | 0.15 | 12/46 (hTERT-HPNE, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14203. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 11.6 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +15.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.57 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.5× (z +14.8) | — |
| [[A-172 (line)]] | wt | 17.7 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.2× (z +19.9) | — |
| [[HEC-1-A (line)]] | alt | 26.0 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.28× (z +15.4) | — |
| [[A498 (line)]] | wt | 6.86 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 66.8× (z +23.9) | — |
| [[HOP62 (line)]] | alt | 23.3 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.6× (z +14.2) | — |
| [[J82 (line)]] | alt | 9.54 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +12.9) | — |
| [[LOX-IMVI (line)]] | wt | 38.9 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +23.7) | — |
| [[NCI-H460 (line)]] | wt | 8.02 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.8× (z +16.5) | — |
| [[SNU-423 (line)]] | alt | 11.6 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.2× (z +14.4) | — |
| [[C32 (line)]] | wt | 15.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.4× (z +15.6) | — |
| [[CFPAC-1 (line)]] | alt | 21.9 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.13× (z +18.1) | — |
| [[hTERT-HPNE (line)]] | wt | 23.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.5× (z +13.8) | — |
| [[LoVo (line)]] | wt | 60.8 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.0734× (z -19.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 25.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +13.9) | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.2× (z +15.8) | — |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +15.9) | — |
| [[SW 900 (line)]] | alt | 15.1 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.6× (z +16.6) | — |
| [[SW48 (line)]] | wt | 80.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 0.5 µM 0.191× (z -9.3) |
| [[A549 (line)]] | wt | 8.83 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.84× (z +11.1) | [[Canagliflozin (drug)]] 0.05 µM 0.0819× (z -8.8) |
| [[H4 (line)]] | wt | 25.1 | 2 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 16.1× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.0667× (z -10.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 105 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -14.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 58.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 10.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.58× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 26.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.78× (z +12.4) | [[Digitoxin (drug)]] 5 µM 0.0922× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 10.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +14.9) | — |
| [[PANC-1 (line)]] | alt | 23.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.44× (z +14.5) | — |
| [[RKO (line)]] | wt | 7.94 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.4× (z +12.0) | — |
| [[SW480 (line)]] | alt | 55.0 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.0462× (z -28.1) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 0.5 µM 0.368× (z -9.0) |
| [[A-427 (line)]] | wt | 10.2 | 2 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 16.8× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 40.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +19.6) | — |
| [[BT-474 (line)]] | alt | 9.04 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +11.6) | [[Neratinib (drug)]] 0.5 µM 0.0470× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 18.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.8× (z +16.2) | — |
| [[Hs 766T (line)]] | wt | 8.89 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.85× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 10.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +15.0) | — |
| [[RPMI-7951 (line)]] | alt | 16.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 45.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +12.9) | — |
| [[C-33 A (line)]] | alt | 10.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.18× (z +9.3) | — |
| [[COLO 205 (line)]] | alt | 44.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 37.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.90 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14203), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGF18]] | +0.79 | +0.79 / +0.75 | both halves | 7e-06 |  |
| [[LINC02955]] | +0.77 | +0.79 / +0.57 | both halves | 1e-05 |  |
| [[LINC00880]] | +0.77 | +0.78 / +0.58 | both halves | 7e-06 |  |
| [[MSH4]] | +0.74 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[PPP1R36]] | +0.73 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[LSMEM1]] | +0.72 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[SYT16]] | +0.72 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.70 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.70 | +0.71 / +0.46 | both halves | 2e-05 |  |
| [[NUP210L]] | +0.69 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[GCNA]] | +0.69 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SLC2A9]] | +0.69 | +0.73 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD9]] | -0.60 | -0.57 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C21orf91-OT1]] | B | C21orf91-OT1 activity raises STPG4's level | lines that do not express C21orf91-OT1 (5) vs lines expressing it (45) | 2.39× lower at baseline in the lines without C21orf91-OT1 | 0.039 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |
| [[TSPOAP1]] | B | TSPOAP1 activity raises STPG4's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 1.98× lower at baseline in the lines without TSPOAP1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2 |
| [[TOP2A]] | B | TOP2A activity lowers STPG4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TNNT2]] | B | TNNT2 activity raises STPG4's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.10× lower at baseline in the lines without TNNT2 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[GPRC5D-AS1]] | B | GPRC5D-AS1 activity raises STPG4's level | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (45) | 1.85× lower at baseline in the lines without GPRC5D-AS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |
| [[MROH3P]] | B | MROH3P activity raises STPG4's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 1.95× lower at baseline in the lines without MROH3P | 0.088 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[SLC2A9]] | B | SLC2A9 activity raises STPG4's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 1.88× lower at baseline in the lines without SLC2A9 | 0.095 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.0, -11.3); signed map (20.0, 3.0). **Vector** length 124, 35.3% of its response variance represented; |z| ≥ 3 in 1,170 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.1 | +24.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +33.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +16.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.1 | +18.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +16.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +10.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.7 | +8.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +5.5 | +6.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -8.5 | -7.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -7.2 | -1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.8 | -2.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.5 | -0.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.7 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | sperm-tail PG-rich repeat containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:47,045,538-47,155,308 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40172; previously C2orf61 |
| Reactome | 2 pathways, smallest: Chromatin modifications during the maternal to zygotic transition (MZT); Maternal to zygotic transition (MZT) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N801](https://www.uniprot.org/uniprotkb/Q8N801) (Protein STPG4):

> Maternal factor that plays a role in epigenetic chromatin reprogramming during early development of the zygote. Involved in the regulation of gametic DNA demethylation by inducing the conversion of the modified genomic base 5-methylcytosine (5mC) into 5-hydroxymethylcytosine (5hmC).

**Summary**, from NCBI Gene [285051](https://www.ncbi.nlm.nih.gov/gene/285051):

> Predicted to enable chromatin binding activity and histone binding activity. Predicted to be involved in epigenetic programing of male pronucleus. Predicted to act upstream of or within pyrimidine-containing compound catabolic process. Predicted to be located in cytoplasm and nucleus. Predicted to be active in female pronucleus; germinal vesicle; and male pronucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26850](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26850) · Entrez [285051](https://www.ncbi.nlm.nih.gov/gene/285051) · UniProt [Q8N801](https://www.uniprot.org/uniprotkb/Q8N801) · Ensembl [ENSG00000239605](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239605)

## Data

Gene col 14203: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14203); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14203, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14203]; `tensor/DDL_lfc|DDL_z.npy` [14203]; `embed/gene_vectors.npy` [14203]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14203 or target_col == 14203). Every well: [[STPG4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STPG4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
