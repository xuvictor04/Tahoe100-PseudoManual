---
symbol: "GPATCH4"
type: "gene"
col: 8387
ensembl_id: "ENSG00000160818"
name: "G-patch domain containing 4 (gene/pseudogene)"
location: "1q22-q23.1"
module: 1
arm: "+"
pooled_cpm: 27.24
n_lines_expressing: 50
n_dd_up: 41
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# GPATCH4

*G-patch domain containing 4 (gene/pseudogene)* — 1q22-q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.19× (z +14.8, q 0e+00, up in 44 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 5.06× (z +14.7, q 0e+00, up in 47 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.601×; ⚠ position not correctable).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UTP20]] (+0.83, fdr 7e-06), [[COA7]] (+0.80, fdr 7e-06), [[DNAJC11]] (+0.80, fdr 7e-06); moves opposite to [[GMCL1]] (-0.75, fdr 7e-06), [[MOSPD3]] (-0.75, fdr 7e-06), [[ARL3]] (-0.73, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAM169A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8387.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **3.19×** | +14.8 | 0e+00 | 44/47 (NCI-H1792, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **5.06×** | +14.7 | 0e+00 | 47/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.81×** | +14.2 | 2e-43 | 42/46 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **5.13×** | +13.8 | 3e-41 | 45/47 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **4.48×** | +13.6 | 8e-40 | 44/45 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **4.09×** | +11.9 | 1e-30 | 34/36 (SW480, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **3.32×** | +10.9 | 1e-25 | 44/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.62×** | +10.8 | 4e-25 | 38/42 (Panc 03.27, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.05×** | +9.4 | 3e-19 | 44/46 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.53×** | +8.4 | 2e-15 | 44/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **2.67×** | +8.2 | 1e-14 | 42/46 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.29×** | +7.5 | 3e-12 | 41/47 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.67×** | +6.6 | 2e-09 | 35/48 (J82, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.06×** | +6.5 | 3e-09 | 35/46 (NCI-H1573, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.03×** | +6.4 | 5e-09 | 38/47 (HT-29, A-172, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **2.01×** | +5.9 | 1e-07 | 38/47 (NCI-H1792, C32, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +5.3 | 4e-06 | 33/47 (A-172, HEC-1-A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.80×** | +4.9 | 3e-05 | 33/45 (NCI-H460, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **2.71×** | +4.7 | 7e-05 | 35/46 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.67×** | +4.6 | 9e-05 | 33/46 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.64×** | +4.5 | 2e-04 | 33/47 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.68×** | +4.4 | 2e-04 | 23/47 (HT-29, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8387.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.601×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 0.644× | -3.7 | 0.12 | 23/46 (HOP62, LoVo, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.688× | -3.4 | 0.21 | 24/47 (LoVo, RKO, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.58 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8387. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 14.3 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.07× (z +14.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 12.9× (z +12.3) | — |
| [[A498 (line)]] | wt | 30.3 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +13.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.45× (z +12.8) | — |
| [[A549 (line)]] | wt | 19.3 | 6 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 7.86× (z +11.3) | — |
| [[HEC-1-A (line)]] | alt | 20.5 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +10.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.74× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 19.1 | 6 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 9.02× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 17.7 | 6 (3 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 17.4× (z +12.8) | — |
| [[NCI-H460 (line)]] | wt | 35.9 | 6 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 6.57× (z +12.8) | — |
| [[PANC-1 (line)]] | alt | 31.1 | 6 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 5.13× (z +12.6) | — |
| [[A-172 (line)]] | wt | 17.5 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.90× (z +12.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 10.5× (z +11.0) | — |
| [[H4 (line)]] | wt | 14.3 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.35× (z +10.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 18.0× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 14.5 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +11.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 12.8× (z +11.3) | — |
| [[J82 (line)]] | alt | 25.7 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.22× (z +9.9) | — |
| [[C32 (line)]] | wt | 25.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +9.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 6.34× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 16.2 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 11.2× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 11.9 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +10.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 8.98× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 41.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +12.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.91× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 83.6 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.27× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.27× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 19.3 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.54× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.43× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 26.8 | 4 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 9.34× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 9.19 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.47× (z +10.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 9.88× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 14.6 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 15.3× (z +10.6) | — |
| [[SW480 (line)]] | alt | 31.2 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 6.19× (z +13.2) | — |
| [[AsPC-1 (line)]] | alt | 14.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 17.4× (z +12.5) | — |
| [[CFPAC-1 (line)]] | alt | 12.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 10.9× (z +11.0) | — |
| [[COLO 205 (line)]] | alt | 18.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +9.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 11.4× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 11.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 11.8× (z +11.0) | — |
| [[NCI-H2347 (line)]] | alt | 17.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.24× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 94.1 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.25× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 54.6 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 5.07× (z +9.9) | — |
| [[KATO III (line)]] | alt | 23.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 22.0 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 6.33× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 25.6 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 6.72× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.601× (z -8.8) ⚠ position not correctable |
| [[A-427 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 65.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8387), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP20]] | +0.83 | +0.84 / +0.78 | both halves | 7e-06 |  |
| [[COA7]] | +0.80 | +0.83 / +0.76 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.80 | +0.81 / +0.74 | both halves | 7e-06 |  |
| [[MAK16]] | +0.79 | +0.78 / +0.81 | both halves | 7e-06 | STRING 863 |
| [[NIP7]] | +0.78 | +0.81 / +0.76 | both halves | 7e-06 |  |
| [[RRS1]] | +0.78 | +0.81 / +0.83 | both halves | 7e-06 | STRING 656 |
| [[NOP14]] | +0.78 | +0.82 / +0.76 | both halves | 7e-06 | STRING 551 |
| [[RPL7L1]] | +0.78 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[LTV1]] | +0.78 | +0.75 / +0.77 | both halves | 7e-06 | STRING 530 |
| [[DHX37]] | +0.77 | +0.78 / +0.71 | both halves | 7e-06 | STRING 515 |
| [[RRP15]] | +0.76 | +0.80 / +0.79 | both halves | 7e-06 | STRING 546 |
| [[NOC3L]] | +0.76 | +0.79 / +0.78 | both halves | 7e-06 | STRING 568 |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMCL1]] | -0.75 | -0.79 / -0.67 | both halves | 7e-06 |  |
| [[MOSPD3]] | -0.75 | -0.80 / -0.64 | both halves | 7e-06 |  |
| [[ARL3]] | -0.73 | -0.75 / -0.57 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.72 | -0.72 / -0.62 | both halves | 7e-06 |  |
| [[KMT5C]] | -0.70 | -0.74 / -0.59 | both halves | 7e-06 |  |
| [[KDELR1]] | -0.70 | -0.76 / -0.63 | both halves | 7e-06 |  |
| [[LAPTM4A]] | -0.70 | -0.71 / -0.69 | both halves | 7e-06 |  |
| [[GNB2]] | -0.69 | -0.70 / -0.55 | both halves | 1e-05 |  |
| [[ANG]] | -0.69 | -0.69 / -0.63 | both halves | 7e-06 |  |
| [[ADIPOR1]] | -0.69 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[PJA2]] | -0.68 | -0.73 / -0.57 | both halves | 8e-06 |  |
| [[CBFA2T2]] | -0.68 | -0.73 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM169A]] | B | FAM169A activity raises GPATCH4's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 1.29× lower at baseline in the lines without FAM169A | 0.086 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |
| [[LRP1]] | C | LRP1 activity lowers GPATCH4's level | lines that do not express LRP1 (3) vs lines expressing it (47) | 2.07× higher at baseline in the lines without LRP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OAF, TGFBR3, OSBPL3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.850). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.3, -36.1); signed map (1.1, -43.2). **Vector** length 109, 40.9% of its response variance represented; |z| ≥ 3 in 1,294 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.54 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.55 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.56 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +9.3 | +14.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.9 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.6 | +14.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.6 | +8.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +13.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.3 | +5.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.3 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +6.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.8 | +2.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | +1.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +1.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -1.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +0.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.7 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | G-patch domain containing 4 (gene/pseudogene) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22-q23.1 — chr1:156,594,301-156,601,496 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20249, DKFZP434F1735; previously GPATC4 |
| Gene groups (HGNC) | G-patch domain containing |
| Matched by | ensembl_id |

UniProt [Q5T3I0](https://www.uniprot.org/uniprotkb/Q5T3I0) carries no function annotation.

**Summary**, from NCBI Gene [54865](https://www.ncbi.nlm.nih.gov/gene/54865):

> Enables RNA binding activity. Predicted to act upstream of or within hematopoietic progenitor cell differentiation. Predicted to be active in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25982](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25982) · Entrez [54865](https://www.ncbi.nlm.nih.gov/gene/54865) · UniProt [Q5T3I0](https://www.uniprot.org/uniprotkb/Q5T3I0) · Ensembl [ENSG00000160818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160818)

## Data

Gene col 8387: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8387); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8387, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8387]; `tensor/DDL_lfc|DDL_z.npy` [8387]; `embed/gene_vectors.npy` [8387]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8387 or target_col == 8387). Every well: [[GPATCH4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPATCH4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
