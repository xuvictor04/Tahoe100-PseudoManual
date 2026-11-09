---
symbol: "EEF2"
type: "gene"
col: 9513
ensembl_id: "ENSG00000167658"
name: "eukaryotic translation elongation factor 2"
location: "19p13.3"
module: 43
arm: "+"
pooled_cpm: 626.77
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# EEF2

*eukaryotic translation elongation factor 2* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.31× (z +12.1, q 4e-31, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.68× (z +7.5, q 8e-12, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.594×; ⚠ cell-cycle shift, explains ~41% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL3]] (+0.77, fdr 7e-06), [[RPL4]] (+0.73, fdr 7e-06), [[NPM1]] (+0.72, fdr 7e-06); moves opposite to [[DHRS7B]] (-0.55, fdr 3e-05), [[LRR1]] (-0.54, fdr 4e-05), [[RBX1]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[EEF1G]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9513.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +12.1 | 4e-31 | 49/49 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +9.6 | 3e-19 | 42/44 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +8.1 | 1e-13 | 42/45 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.47×** | +7.9 | 4e-13 | 31/48 (COLO 205, C32, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +7.5 | 8e-12 | 48/48 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +6.3 | 2e-08 | 46/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.53×** | +6.2 | 6e-08 | 46/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +5.8 | 4e-07 | 37/48 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +5.5 | 2e-06 | 41/48 (HT-29, RPMI-7951, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +5.1 | 2e-05 | 44/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +4.9 | 5e-05 | 41/48 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +4.8 | 7e-05 | 37/48 (HT-29, PANC-1, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.4 | 6e-04 | 37/47 (COLO 205, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +4.1 | 0.002 | 41/48 (HT-29, SW 900, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.71×** | +4.0 | 0.002 | 41/45 (LS 180, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +3.9 | 0.003 | 39/48 (HT-29, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.65×** | +3.8 | 0.005 | 44/48 (HT-29, AsPC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.005 | 22/48 (RPMI-7951, AN3 CA, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.4 | 0.023 | 19/49 (CFPAC-1, NCI-H2030, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.036 | 37/48 (HepG2/C3A, HCT15, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.046 | 29/48 (NCI-H2030, CFPAC-1, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.056 | 29/50 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.056 | 28/47 (C32, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.594×; ⚠ cell-cycle shift, explains ~41% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9513. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 432 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +14.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +10.6) | — |
| [[NCI-H460 (line)]] | wt | 793 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +11.5) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 221 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.83× (z +19.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.60× (z +10.0) | — |
| [[KATO III (line)]] | alt | 305 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.16× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 451 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +16.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.11× (z +8.8) | — |
| [[A498 (line)]] | wt | 529 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.19× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 571 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.97× (z +9.6) | — |
| [[LoVo (line)]] | wt | 1,028 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +13.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 509 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +13.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 444 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +12.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.66× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 409 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.20× (z +9.8) | — |
| [[SW480 (line)]] | alt | 736 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.97× (z +9.2) | — |
| [[A549 (line)]] | wt | 636 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +13.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 427 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +16.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.43× (z +12.9) | — |
| [[LS 180 (line)]] | wt | 806 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +12.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 942 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +12.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 461 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.13× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 305 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +14.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.15× (z +11.5) | — |
| [[C-33 A (line)]] | alt | 734 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.594× (z -9.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[H4 (line)]] | wt | 471 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 697 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +11.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 768 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +12.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 472 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +10.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 405 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +10.7) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 776 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.2) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[J82 (line)]] | alt | 331 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.2) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H1573 (line)]] | alt | 367 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +12.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.70× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 636 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[PANC-1 (line)]] | alt | 466 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 984 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +11.2) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 503 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.92× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 331 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.0) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[HS-578T (line)]] | alt | 777 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +9.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 1,187 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 609 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 1,206 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 680 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 823 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 408 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 732 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 955 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 935 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 646 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 465 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 978 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 624 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 570 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1,040 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 461 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 503 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9513), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL3]] | +0.77 | +0.66 / +0.80 | both halves | 7e-06 | same gene group; pathway: Eukaryotic Translation Elongation; STRING 999 |
| [[RPL4]] | +0.73 | +0.64 / +0.79 | both halves | 7e-06 | same gene group; pathway: Eukaryotic Translation Elongation; STRING 999 |
| [[NPM1]] | +0.72 | +0.69 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 538 |
| [[PABPC1]] | +0.70 | +0.65 / +0.71 | both halves | 7e-06 | STRING 775 |
| [[EEF1G]] | +0.70 | +0.62 / +0.73 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 994 |
| [[HNRNPA1]] | +0.65 | +0.52 / +0.65 | both halves | 1e-05 | STRING 777 |
| [[SLC25A6]] | +0.65 | +0.50 / +0.68 | both halves | 1e-05 | STRING 534 |
| [[RPL14]] | +0.65 | +0.57 / +0.66 | both halves | 1e-05 | pathway: Eukaryotic Translation Elongation; STRING 999 |
| [[EEF1A1]] | +0.64 | +0.71 / +0.70 | both halves | 7e-06 | same gene group; pathway: Eukaryotic Translation Elongation; STRING 982 |
| [[EIF3L]] | +0.64 | +0.55 / +0.66 | both halves | 1e-05 | STRING 736 |
| [[SNHG29]] | +0.64 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[PCBP2]] | +0.63 | +0.68 / +0.66 | both halves | 7e-06 | STRING 587 |

## Genes that move opposite

*21 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHRS7B]] | -0.55 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[LRR1]] | -0.54 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[RBX1]] | -0.53 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[MGME1]] | -0.51 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[POLR2K]] | -0.50 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[FEN1]] | -0.48 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[MICOS10]] | -0.48 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[WDR53]] | -0.48 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[ZNF200]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[C2orf42]] | -0.46 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[CNOT9]] | -0.46 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[LSM5]] | -0.46 | -0.34 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EEF1G]] | C | EEF1G's natural level weakens EEF2's drug response | EEF1G's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.04; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[RPS2]] | C | RPS2's natural level weakens EEF2's drug response | RPS2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.20; direction not clear | 0.064 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[EEF1A1P5]] | C | EEF1A1P5's natural level weakens EEF2's drug response | EEF1A1P5's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.48; direction not clear | 0.064 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[EEF1A1]] | C | EEF1A1's natural level weakens EEF2's drug response | EEF1A1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.35; direction not clear | 0.068 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[RPL10A]] | C | RPL10A's natural level weakens EEF2's drug response | RPL10A's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.61, reverse -0.03; direction clear | 0.092 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.371). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-30.2, -25.8); signed map (-22.6, -33.4). **Vector** length 127, 54.3% of its response variance represented; |z| ≥ 3 in 1,196 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Sapanisertib (drug)]] 0.05 µM |  | +6.4 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +3.8 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +4.6 | +2.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +4.2 | +0.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +3.9 | +1.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.9 | +1.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -7.2 | -0.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.8 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.4 | -1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | +0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -1.6 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -3.2 | -1.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -3.2 | -1.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.0 | -1.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation elongation factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:3,976,056-3,985,463 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EEF-2; previously EF2 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes; Translational GTPases |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 11 pathways, smallest: Uptake and function of diphtheria toxin; Synthesis of diphthamide-EEF2; Protein methylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P13639](https://www.uniprot.org/uniprotkb/P13639) (Elongation factor 2):

> Catalyzes the GTP-dependent ribosomal translocation step during translation elongation. During this step, the ribosome changes from the pre-translocational (PRE) to the post-translocational (POST) state as the newly formed A-site-bound peptidyl-tRNA and P-site-bound deacylated tRNA move to the P and E sites, respectively. Catalyzes the coordinated movement of the two tRNA molecules, the mRNA and conformational changes in the ribosome.

**Summary**, from NCBI Gene [1938](https://www.ncbi.nlm.nih.gov/gene/1938):

> This gene encodes a member of the GTP-binding translation elongation factor family. This protein is an essential factor for protein synthesis. It promotes the GTP-dependent translocation of the nascent protein chain from the A-site to the P-site of the ribosome. This protein is completely inactivated by EF-2 kinase phosporylation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3214](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3214) · Entrez [1938](https://www.ncbi.nlm.nih.gov/gene/1938) · UniProt [P13639](https://www.uniprot.org/uniprotkb/P13639) · Ensembl [ENSG00000167658](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167658)

## Data

Gene col 9513: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9513); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9513, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9513]; `tensor/DDL_lfc|DDL_z.npy` [9513]; `embed/gene_vectors.npy` [9513]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9513 or target_col == 9513). Every well: [[EEF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EEF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
