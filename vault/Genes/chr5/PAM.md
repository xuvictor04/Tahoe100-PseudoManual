---
symbol: "PAM"
type: "gene"
col: 7018
ensembl_id: "ENSG00000145730"
name: "peptidylglycine alpha-amidating monooxygenase"
location: "5q21.1"
module: 200
arm: "+"
pooled_cpm: 458.39
n_lines_expressing: 47
n_dd_up: 2
n_dd_down: 25
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/200"]
generated_by: "tahoemap"
---

# PAM

*peptidylglycine alpha-amidating monooxygenase* — 5q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.23× (z +3.8, q 0.076, up in 25 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Daptomycin (drug)]] 5 µM in 2 lines (COLO 205 2.41×, NCI-H1573 1.97×; ⚠ unreliable plate only); [[Vinblastine (sulfate) (drug)]] 5 µM in 2 lines (COLO 205 1.82×, NCI-H1573 1.61×); [[Selinexor (drug)]] 5 µM in 2 lines (A498 1.61×, A-427 1.66×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 1.84×); [[Peretinoin (drug)]] 5 µM in 1 line (COLO 205 2.46×).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.243× (z -26.7, q 0e+00, down in 44 of 45 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOCK7]] (+0.57, fdr 1e-05), [[DST]] (+0.54, fdr 3e-05), [[IMMP2L]] (+0.53, fdr 2e-04); moves opposite to [[MIGA2]] (-0.52, fdr 3e-05), [[LRCH4]] (-0.48, fdr 7e-05), [[PHF1]] (-0.47, fdr 2e-04).
> It is in [[Module 200]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DTNA]] → it (grade B ⚠); 2 go from it, the strongest it → [[CRYBG3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7018.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Daptomycin (drug)]] 5 µM in 2 lines (COLO 205 2.41×, NCI-H1573 1.97×; ⚠ unreliable plate only); [[Vinblastine (sulfate) (drug)]] 5 µM in 2 lines (COLO 205 1.82×, NCI-H1573 1.61×); [[Selinexor (drug)]] 5 µM in 2 lines (A498 1.61×, A-427 1.66×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 1.84×); [[Peretinoin (drug)]] 5 µM in 1 line (COLO 205 2.46×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.076 | 25/44 (A-427, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.076 | 24/46 (COLO 205, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | 1.38× | +3.1 | 0.33 | 25/45 (A-427, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7018.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.243×** | -26.7 | 0e+00 | 44/45 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.260×** | -25.4 | 0e+00 | 44/45 (HepG2/C3A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.419×** | -23.2 | 0e+00 | 41/45 (HEC-1-A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.325×** | -21.2 | 0e+00 | 44/45 (HepG2/C3A, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.523×** | -12.2 | 4e-32 | 36/45 (HEC-1-A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.538×** | -11.2 | 3e-27 | 39/44 (HOP62, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.554×** | -10.7 | 9e-25 | 40/44 (HEC-1-A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.563×** | -10.4 | 1e-23 | 41/45 (HEC-1-A, NCI-H460, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.584×** | -10.1 | 3e-22 | 41/45 (HOP62, SHP-77, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.580×** | -9.9 | 4e-21 | 36/41 (HCT15, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.704×** | -9.4 | 4e-19 | 30/46 (HEC-1-A, NCI-H1792, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **0.591×** | -9.3 | 1e-18 | 38/46 (SNU-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.676×** | -7.4 | 8e-12 | 33/45 (SNU-423, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **0.686×** | -7.1 | 5e-11 | 40/45 (CFPAC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.688×** | -7.1 | 7e-11 | 32/45 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.831×** | -3.2 | 0.033 | 21/44 (SW 1271, C32, …) | all doses, stronger at high dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 0.890× | -2.9 | 0.075 | 10/45 (NCI-H460, LoVo, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.742×** | -2.9 | 0.079 | 21/46 (HepG2/C3A, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.797×** | -2.9 | 0.083 | 22/45 (NCI-H1573, LS 180, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.899× | -2.8 | 0.090 | 2/46 (SNU-1, SW 1088) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7018. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 1,165 | 0 | 21 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -21.7) |
| [[HEC-1-A (line)]] | alt | 491 | 0 | 18 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -41.5) |
| [[HOP62 (line)]] | alt | 625 | 0 | 18 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -32.4) |
| [[SNU-423 (line)]] | alt | 805 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -29.2) |
| [[NCI-H460 (line)]] | wt | 455 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -29.7) |
| [[RPMI-7951 (line)]] | alt | 552 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -21.8) |
| [[CFPAC-1 (line)]] | alt | 549 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -25.6) |
| [[HepG2_C3A (line)]] | wt | 383 | 0 | 12 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.1000× (z -32.6) |
| [[LoVo (line)]] | wt | 499 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.156× (z -27.4) |
| [[NCI-H1573 (line)]] | alt | 391 | 4 (2 ⚠) | 8 (4 ⚠) | [[Daptomycin (drug)]] 5 µM 1.97× (z +9.3) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.61× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -16.6) |
| [[NCI-H1792 (line)]] | alt | 904 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -35.5) |
| [[SK-MEL-2 (line)]] | alt | 629 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -33.2) |
| [[HCT15 (line)]] | alt | 736 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -33.4) |
| [[J82 (line)]] | alt | 415 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -22.0) |
| [[MIA PaCa-2 (line)]] | alt | 521 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -25.7) |
| [[COLO 205 (line)]] | alt | 243 | 6 (2 ⚠) | 4 (1 ⚠) | [[Daptomycin (drug)]] 0.5 µM 2.53× (z +11.9) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 2.46× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.278× (z -16.4) |
| [[SNU-1 (line)]] | wt | 637 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.270× (z -16.0) |
| [[SW480 (line)]] | alt | 820 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -23.7) |
| [[A-427 (line)]] | wt | 412 | 7 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.463× (z -10.4) |
| [[C-33 A (line)]] | alt | 363 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.274× (z -18.7) |
| [[H4 (line)]] | wt | 854 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -18.6) |
| [[SW48 (line)]] | wt | 481 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -18.0) |
| [[AN3 CA (line)]] | alt | 759 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -17.1) |
| [[CHP-212 (line)]] | wt | 472 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.216× (z -14.6) |
| [[HS-578T (line)]] | alt | 458 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -21.7) |
| [[LOX-IMVI (line)]] | wt | 540 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -19.9) |
| [[LS 180 (line)]] | wt | 438 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.286× (z -16.9) |
| [[Panc 03.27 (line)]] | alt | 356 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -24.3) |
| [[hTERT-HPNE (line)]] | wt | 632 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -17.3) |
| [[RKO (line)]] | wt | 526 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -27.1) |
| [[SW 900 (line)]] | alt | 314 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -20.1) |
| [[SW1417 (line)]] | alt | 223 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -23.2) |
| [[A549 (line)]] | wt | 156 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.211× (z -18.4) |
| [[Hs 766T (line)]] | wt | 303 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -22.3) |
| [[HT-29 (line)]] | alt | 382 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.222× (z -20.3) |
| [[A498 (line)]] | wt | 222 | 2 (2 ⚠) | 2 | [[Selinexor (drug)]] 5 µM 1.61× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.485× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 388 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.342× (z -15.1) |
| [[NCI-H2347 (line)]] | alt | 521 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -16.9) |
| [[A-172 (line)]] | wt | 493 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.287× (z -17.8) |
| [[AsPC-1 (line)]] | alt | 384 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.453× (z -11.6) |
| [[PANC-1 (line)]] | alt | 273 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.506× (z -10.9) |
| [[SW 1088 (line)]] | alt | 731 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 198 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -11.8) |
| [[BT-474 (line)]] | alt | 96.5 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 168 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 438 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 535 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 521 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7018), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOCK7]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[DST]] | +0.54 | +0.44 / +0.57 | both halves | 3e-05 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[IMMP2L]] | +0.53 | +0.32 / +0.58 | both halves | 2e-04 |  |
| [[TRIO]] | +0.52 | +0.43 / +0.60 | both halves | 3e-05 | STRING 400 |
| [[FER]] | +0.52 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[TP53BP2]] | +0.47 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[MYO1B]] | +0.47 | +0.36 / +0.53 | both halves | 9e-05 |  |
| [[PSG5]] | +0.47 | +0.43 / +0.34 | both halves | 1e-04 |  |
| [[FAHD1]] | +0.46 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[ZNF337]] | +0.45 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[UGT2B7]] | +0.45 | +0.30 / +0.34 | both halves | 2e-04 |  |
| [[RBM12B]] | +0.45 | +0.37 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIGA2]] | -0.52 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[LRCH4]] | -0.48 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[PHF1]] | -0.47 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[ZNF684]] | -0.47 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[PDXDC2P-NPIPB14P]] | -0.46 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[TTC38]] | -0.45 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[STAG3L5P-1]] | -0.44 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[CCDC9]] | -0.44 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[TYK2]] | -0.44 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[CDK10]] | -0.44 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[GOLPH3]] | -0.43 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[NKTR]] | -0.43 | -0.37 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DTNA]] | B | DTNA activity raises PAM's level | lines that do not express DTNA (22) vs lines expressing it (28) | 1.48× lower at baseline in the lines without DTNA | 0.007 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, MMP16, ENSG00000253553 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRYBG3]] | C | PAM activity raises CRYBG3's level | lines that do not express PAM (3) vs lines expressing it (47) | 5.15× lower at baseline in the lines without PAM | 2e-04 | ⚠ few lines (3 vs 47); across organs; also absent: PARP3, OSBPL3, CRYBG3; maybe low, not absent; co-absent with the target |
| [[GBE1]] | C | PAM activity raises GBE1's level | lines that do not express PAM (3) vs lines expressing it (47) | 4.31× lower at baseline in the lines without PAM | 0.011 | ⚠ few lines (3 vs 47); across organs; also absent: PARP3, OSBPL3, CRYBG3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 200]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.488). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-6.6, -1.8); signed map (11.3, -10.9). **Vector** length 102, 35.9% of its response variance represented; |z| ≥ 3 in 1,526 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.4 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.6 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.6 | +1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.4 | +1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | -2.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.5 | -5.7 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -3.4 | -2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.4 | -10.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.4 | -3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.2 | -25.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | peptidylglycine alpha-amidating monooxygenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q21.1 — chr5:102,753,981-103,029,730 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAL, PHM, PAM-1 |
| Gene groups (HGNC) | Oxygenases; Carbon-nitrogen lyases |
| Hallmark sets | PROTEIN_SECRETION, GLYCOLYSIS, HYPOXIA |
| Matched by | ensembl_id |

**Function**, from UniProt [P19021](https://www.uniprot.org/uniprotkb/P19021) (Peptidyl-glycine alpha-amidating monooxygenase):

> Bifunctional enzyme that catalyzes amidation of the C-terminus of proteins. Alpha-amidation is present at the C-terminus of many endocrine hormones and neuropeptides and is required for their activity. C-terminal amidation also takes place in response to protein fragmentation triggered by oxidative stress, promoting degradation of amidated protein fragments by the proteasome. Alpha-amidation involves two sequential reactions, both of which are catalyzed by separate catalytic domains of the …

**Summary**, from NCBI Gene [5066](https://www.ncbi.nlm.nih.gov/gene/5066):

> This gene encodes a multifunctional protein. The encoded preproprotein is proteolytically processed to generate the mature enzyme. This enzyme includes two domains with distinct catalytic activities, a peptidylglycine alpha-hydroxylating monooxygenase (PHM) domain and a peptidyl-alpha-hydroxyglycine alpha-amidating lyase (PAL) domain. These catalytic domains work sequentially to catalyze the conversion of neuroendocrine peptides to active alpha-amidated products. Alternative splicing results in …

**Accessions** — [HGNC:8596](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8596) · Entrez [5066](https://www.ncbi.nlm.nih.gov/gene/5066) · UniProt [P19021](https://www.uniprot.org/uniprotkb/P19021) · Ensembl [ENSG00000145730](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145730)

## Data

Gene col 7018: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7018); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7018, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7018]; `tensor/DDL_lfc|DDL_z.npy` [7018]; `embed/gene_vectors.npy` [7018]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7018 or target_col == 7018). Every well: [[PAM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
