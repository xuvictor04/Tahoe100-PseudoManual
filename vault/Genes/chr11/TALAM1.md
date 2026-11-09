---
symbol: "TALAM1"
type: "gene"
col: 16441
ensembl_id: "ENSG00000289740"
name: "TALAM1 transcript, MALAT1 antisense RNA"
location: "11q13.1"
module: 16
arm: "-"
pooled_cpm: 1550.91
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# TALAM1

*TALAM1 transcript, MALAT1 antisense RNA* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.19× (z +13.9, q 7e-41, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.50× (z +7.1, q 1e-10, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.872× (z -8.4, q 3e-14, down in 0 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.785× (z -4.2, q 0.007, down in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (Hs 766T 0.858×, CFPAC-1 0.860×; ⚠ position not correctable).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MALAT1]] (+0.88, fdr 7e-06, ⚠ same locus), [[NEAT1]] (+0.66, fdr 7e-06), [[ZBTB47-AS1]] (+0.64, fdr 1e-05), [[TPT1]] (+0.62, fdr 8e-06); moves opposite to [[SUV39H1]] (-0.68, fdr 7e-06), [[GEMIN4]] (-0.62, fdr 1e-05), [[HGH1]] (-0.60, fdr 5e-05).
> It sits in the **-** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16441.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +13.9 | 7e-41 | 48/49 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +12.7 | 2e-34 | 44/44 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +7.7 | 3e-12 | 43/45 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +7.1 | 1e-10 | 46/48 (HT-29, SW480, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +6.7 | 2e-09 | 46/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +5.7 | 1e-06 | 38/48 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.37×** | +5.3 | 7e-06 | 44/49 (AN3 CA, SW 1088, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.9 | 6e-05 | 29/48 (HS-578T, Panc 03.27, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.9 | 6e-05 | 36/50 (HEC-1-A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.5 | 3e-04 | 33/48 (SHP-77, HS-578T, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +4.5 | 3e-04 | 28/48 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +4.5 | 3e-04 | 37/48 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.20×** | +4.5 | 3e-04 | 26/48 (COLO 205, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +4.4 | 4e-04 | 31/48 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.28×** | +4.3 | 6e-04 | 30/48 (HS-578T, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 9e-04 | 32/48 (COLO 205, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.004 | 27/48 (HS-578T, H4, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 1.16× | +3.7 | 0.006 | 7/48 (LOX-IMVI, HT-29, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.013 | 42/49 (HS-578T, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16441.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (Hs 766T 0.858×, CFPAC-1 0.860×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.872× | -8.4 | 3e-14 | 0/50 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.785×** | -4.2 | 0.007 | 39/48 (MIA PaCa-2, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Larotrectinib (drug)]] 5 µM |  | 0.857× | -3.7 | 0.037 | 13/48 (SW1417, HT-29, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.839× | -3.1 | 0.31 | 21/48 (A-427, LOX-IMVI, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16441. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 1,389 | 7 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.03× (z +11.3) | — |
| [[SW480 (line)]] | alt | 1,558 | 7 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.01× (z +11.2) | — |
| [[H4 (line)]] | wt | 1,365 | 6 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.15× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 1,209 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +16.3) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 1,813 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.19× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.87× (z +10.2) | — |
| [[A498 (line)]] | wt | 978 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +14.0) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 1,871 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +13.3) | — |
| [[HT-29 (line)]] | alt | 1,889 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.01× (z +11.7) | — |
| [[KATO III (line)]] | alt | 1,527 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.85× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 1,135 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.06× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 1,454 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +13.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 1,360 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +16.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 1,588 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.1) | — |
| [[LoVo (line)]] | wt | 1,393 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +17.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 1,546 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.87× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 1,538 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.88× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.68× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 1,857 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.62× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 1,450 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.86× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 1,831 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +13.7) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 1,813 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +9.6) | — |
| [[A-172 (line)]] | wt | 1,557 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.82× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 1,490 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.90× (z +10.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 1,266 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +10.0) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 1,766 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.17× (z +11.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 1,425 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.84× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 1,633 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +12.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 1,634 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +12.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 1,638 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 1,793 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.95× (z +10.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 1,455 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +13.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 1,716 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +13.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 1,076 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +13.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 1,051 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +11.2) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 1,428 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.09× (z +10.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 1,498 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.94× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 1,324 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +12.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 2,326 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.0) | — |
| [[CHP-212 (line)]] | wt | 1,651 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 1,264 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +9.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 1,208 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +11.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 1,043 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +10.7) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 1,712 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +13.1) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 1,671 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.04× (z +8.5) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 2,779 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2,040 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2,028 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1,824 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1,983 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1,412 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1,571 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16441), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MALAT1]] | +0.88 | +0.79 / +0.91 | both halves | 7e-06 | same gene group; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[NEAT1]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 | same gene group |
| [[ZBTB47-AS1]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[TPT1]] | +0.62 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[SPTBN1-AS2]] | +0.59 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[AKAP13-AS1]] | +0.58 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[FTL]] | +0.56 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[EOGT-DT]] | +0.56 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[RPS20]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ST13]] | +0.54 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[ZRANB2-AS1]] | +0.54 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[BEST1]] | +0.54 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[SNAP23]] | +0.53 | +0.40 / +0.58 | both halves | 5e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUV39H1]] | -0.68 | -0.62 / -0.71 | both halves | 7e-06 |  |
| [[GEMIN4]] | -0.62 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[HGH1]] | -0.60 | -0.40 / -0.65 | both halves | 5e-05 |  |
| [[ADO]] | -0.60 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[DDX20]] | -0.59 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[PDE12]] | -0.59 | -0.42 / -0.69 | both halves | 4e-05 |  |
| [[HASPIN]] | -0.59 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[RAVER1]] | -0.59 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[CSTF1]] | -0.58 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[CHAMP1]] | -0.58 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[NOL11]] | -0.58 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[DCLRE1B]] | -0.57 | -0.54 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.378). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-55.9, -5.2); signed map (-20.8, 22.4). **Vector** length 128, 41.4% of its response variance represented; |z| ≥ 3 in 1,113 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.9 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.0 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.5 | +7.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.2 | +4.2 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.9 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +4.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.3 | +3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +4.2 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +4.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -8.1 | +0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.3 | -4.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -6.6 | +4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.5 | -1.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.3 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -0.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -3.5 | -1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | TALAM1 transcript, MALAT1 antisense RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q13.1 — chr11:65,499,312-65,507,432 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [109136579](https://www.ncbi.nlm.nih.gov/gene/109136579):

> Predicted to be involved in positive regulation of cell motility. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:54476](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54476) · Entrez [109136579](https://www.ncbi.nlm.nih.gov/gene/109136579) · Ensembl [ENSG00000289740](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000289740)

## Data

Gene col 16441: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16441); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16441, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16441]; `tensor/DDL_lfc|DDL_z.npy` [16441]; `embed/gene_vectors.npy` [16441]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16441 or target_col == 16441). Every well: [[TALAM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TALAM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
