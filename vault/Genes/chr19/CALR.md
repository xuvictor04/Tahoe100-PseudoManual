---
symbol: "CALR"
type: "gene"
col: 11010
ensembl_id: "ENSG00000179218"
name: "calreticulin"
location: "19p13.13"
module: 42
arm: "+"
pooled_cpm: 429.54
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# CALR

*calreticulin* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.63× (z +10.1, q 2e-21, up in 44 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A549 6.64×, A-427 6.19×, C-33 A 4.74×, SNU-423 4.78×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (C-33 A 5.08×, A549 5.49×, SNU-423 4.49×, A-427 4.41×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (HS-578T 3.66×, A-172 3.14×, H4 3.48×; ⚠ cell-cycle shift, explains ~29% of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.682× (z -5.9, q 2e-06, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDIA4]] (+0.88, fdr 7e-06), [[HSP90B1]] (+0.86, fdr 7e-06), [[P4HB]] (+0.79, fdr 7e-06); moves opposite to [[ITPA]] (-0.59, fdr 1e-05), [[TRMT5]] (-0.59, fdr 1e-05), [[RPL7L1]] (-0.59, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AGR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 11 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11010.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (A549 6.64×, A-427 6.19×, C-33 A 4.74×, SNU-423 4.78×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (C-33 A 5.08×, A549 5.49×, SNU-423 4.49×, A-427 4.41×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (HS-578T 3.66×, A-172 3.14×, H4 3.48×; ⚠ cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.63×** | +10.1 | 2e-21 | 44/44 (C-33 A, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.86×** | +10.1 | 2e-21 | 48/49 (A549, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.34×** | +9.2 | 5e-18 | 48/48 (HS-578T, A-172, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.04×** | +7.7 | 2e-12 | 47/48 (SW480, A549, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.92×** | +6.6 | 6e-09 | 43/45 (C-33 A, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.63×** | +5.3 | 1e-05 | 44/48 (A549, AsPC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.51×** | +4.5 | 6e-04 | 43/48 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.3 | 0.001 | 1/50 (HOP62) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.43×** | +3.9 | 0.007 | 35/48 (J82, PANC-1, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.28×** | +3.7 | 0.011 | 27/49 (SNU-423, NCI-H2347, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.39×** | +3.5 | 0.020 | 28/48 (J82, PANC-1, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11010.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.682×** | -5.9 | 2e-06 | 35/48 (KATO III, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.653×** | -4.6 | 1e-03 | 32/48 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | **0.768×** | -4.1 | 0.009 | 40/48 (C32, SNU-423, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.738× | -3.3 | 0.13 | 34/48 (RPMI-7951, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.814× | -3.2 | 0.17 | 28/48 (NCI-H1573, RPMI-7951, …) | top dose only | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.753× | -3.1 | 0.18 | 33/48 (KATO III, RKO, …) | top dose only | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 0.747× | -3.1 | 0.18 | 30/49 (H4, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11010. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 179 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.64× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[KATO III (line)]] | alt | 736 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -18.7) |
| [[HS-578T (line)]] | alt | 1,145 | 4 (4 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 3.66× (z +12.7) ⚠ cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -9.7) |
| [[J82 (line)]] | alt | 689 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.86× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 470 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -13.1) |
| [[SHP-77 (line)]] | alt | 243 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -8.5) |
| [[SNU-423 (line)]] | alt | 536 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-427 (line)]] | wt | 442 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.0) |
| [[C-33 A (line)]] | alt | 214 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.08× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 330 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.63× (z +10.4) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[Panc 03.27 (line)]] | alt | 541 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 253 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.47× (z +10.4) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW480 (line)]] | alt | 194 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A498 (line)]] | wt | 649 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.20× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.431× (z -8.5) |
| [[H4 (line)]] | wt | 865 | 1 (1 ⚠) | 2 | [[Panobinostat (drug)]] 0.5 µM 3.48× (z +11.6) ⚠ cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -15.2) |
| [[HOP62 (line)]] | alt | 438 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 189 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H23 (line)]] | alt | 236 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -8.5) |
| [[A-172 (line)]] | wt | 875 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.14× (z +11.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[AsPC-1 (line)]] | alt | 201 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.44× (z +8.8) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[C32 (line)]] | wt | 469 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.55× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[CFPAC-1 (line)]] | alt | 436 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -12.9) |
| [[hTERT-HPNE (line)]] | wt | 755 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.08× (z +9.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2347 (line)]] | alt | 654 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +10.0) ⚠ cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 293 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[PANC-1 (line)]] | alt | 374 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RPMI-7951 (line)]] | alt | 678 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.69× (z +10.0) ⚠ cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -10.2) |
| [[SNU-1 (line)]] | wt | 312 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -9.6) |
| [[SW48 (line)]] | wt | 290 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[CHP-212 (line)]] | wt | 276 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RKO (line)]] | wt | 470 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -14.0) |
| [[SW1417 (line)]] | alt | 292 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[AN3 CA (line)]] | alt | 403 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 393 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 306 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 354 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 336 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 328 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 372 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 281 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 516 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 429 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 301 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 341 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 654 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 941 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 320 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 488 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11010), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDIA4]] | +0.88 | +0.87 / +0.85 | both halves | 7e-06 | STRING 973 |
| [[HSP90B1]] | +0.86 | +0.86 / +0.81 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MTORC1_SIGNALING; STRING 999 |
| [[P4HB]] | +0.79 | +0.77 / +0.71 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication; STRING 994 |
| [[PDIA6]] | +0.79 | +0.80 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 937 |
| [[HSPA5]] | +0.77 | +0.78 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 995 |
| [[TMED9]] | +0.75 | +0.73 / +0.69 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PDIA3]] | +0.73 | +0.83 / +0.76 | both halves | 7e-06 | pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 999 |
| [[DNAJC3]] | +0.72 | +0.73 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 667 |
| [[OS9]] | +0.72 | +0.77 / +0.59 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 737 |
| [[MANF]] | +0.71 | +0.68 / +0.76 | both halves | 7e-06 | STRING 656 |
| [[NUCB2]] | +0.71 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[LMAN1]] | +0.71 | +0.70 / +0.62 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 792 |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITPA]] | -0.59 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[TRMT5]] | -0.59 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[RPL7L1]] | -0.59 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[ST7L]] | -0.57 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[GPATCH4]] | -0.57 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[GCFC2]] | -0.56 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[DUS4L]] | -0.56 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[ZNF507]] | -0.56 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[MIER3]] | -0.55 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[GABPB1]] | -0.54 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[ZSCAN29]] | -0.54 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[RPP38]] | -0.54 | -0.46 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGR2]] | B | AGR2 activity weakens CALR's drug response | lines that do not express AGR2 (32) vs lines expressing it (18) | the lines without AGR2 respond 1.37× as strongly (z diff -1.36); strongest at Dinaciclib 5 µM: 3.01x vs 2.03x (z diff -2.3) | 0.060 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers CALR's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.787). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.5, -30.9); signed map (-54.4, 7.4). **Vector** length 129, 53.8% of its response variance represented; |z| ≥ 3 in 1,006 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cargo concentration in the ER* (reactome, mean cos +0.56 to 7); *Cotranslational targeting of proteins to the endoplasmic reticulum* (reactome, mean cos +0.53 to 11); *COPII-mediated vesicle transport* (reactome, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +7.7 | +9.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +7.6 | +7.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +5.6 | +5.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.9 | +1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +3.7 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +1.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.4 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +1.3 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.1 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.6 | -4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.9 | -0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.7 | -0.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.6 | -3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.1 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.8 | -3.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.4 | -0.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.0 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | calreticulin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,938,578-12,944,489 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RO, SSA, cC1qR, CRT, FLJ26680, CALR1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Calnexin/calreticulin family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, UNFOLDED_PROTEIN_RESPONSE, MTORC1_SIGNALING |
| Reactome | 24 pathways, smallest: Assembly of Viral Components at the Budding Site; Virus Assembly and Release; Scavenging by Class F Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P27797](https://www.uniprot.org/uniprotkb/P27797) (Calreticulin):

> Calcium-binding chaperone that promotes folding, oligomeric assembly and quality control in the endoplasmic reticulum (ER) via the calreticulin/calnexin cycle. This lectin interacts transiently with almost all of the monoglucosylated glycoproteins that are synthesized in the ER. Interacts with the DNA-binding domain of NR3C1 and mediates its nuclear export. Involved in maternal gene expression regulation. May participate in oocyte maturation via the regulation of calcium homeostasis (By …

**Summary**, from NCBI Gene [811](https://www.ncbi.nlm.nih.gov/gene/811):

> Calreticulin is a highly conserved chaperone protein which resides primarily in the endoplasmic reticulum, and is involved in a variety of cellular processes, among them, cell adhesion. Additionally, it functions in protein folding quality control and calcium homeostasis. Calreticulin is also found in the nucleus, suggesting that it may have a role in transcription regulation. Systemic lupus erythematosus is associated with increased autoantibody titers against calreticulin. Recurrent mutations …

**Accessions** — [HGNC:1455](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1455) · Entrez [811](https://www.ncbi.nlm.nih.gov/gene/811) · UniProt [P27797](https://www.uniprot.org/uniprotkb/P27797) · Ensembl [ENSG00000179218](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179218)

## Data

Gene col 11010: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11010); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11010, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11010]; `tensor/DDL_lfc|DDL_z.npy` [11010]; `embed/gene_vectors.npy` [11010]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11010 or target_col == 11010). Every well: [[CALR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CALR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
