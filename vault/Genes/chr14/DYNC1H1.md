---
symbol: "DYNC1H1"
type: "gene"
col: 12341
ensembl_id: "ENSG00000197102"
name: "dynein cytoplasmic 1 heavy chain 1"
location: "14q32.31"
module: 25
arm: "+"
pooled_cpm: 393.46
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# DYNC1H1

*dynein cytoplasmic 1 heavy chain 1* — 14q32.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 1.56× (z +8.4, q 2e-14, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.607× (z -9.1, q 6e-17, down in 42 of 47 measured lines) ⚠ toxic.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H460 0.369×, HOP62 0.499×, J82 0.529×, A-427 0.509×, …; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H460 0.423×, NCI-H2030 0.550×, NCI-H1792 0.638×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.485×, HEC-1-A 0.542×; ⚠ cell-cycle shift, explains ~0% of this change); [[Capmatinib (drug)]] 5 µM in 1 line (CHP-212 0.0382×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HUWE1]] (+0.70, fdr 7e-06), [[SPTBN1]] (+0.69, fdr 7e-06), [[STIP1]] (+0.68, fdr 7e-06); moves opposite to [[SNHG9]] (-0.65, fdr 1e-05), [[SELENOH]] (-0.64, fdr 1e-05), [[ZNF816-ZNF321P]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MYO5A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12341.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +8.4 | 2e-14 | 45/48 (COLO 205, SW480, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +7.9 | 8e-13 | 41/48 (COLO 205, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +7.6 | 7e-12 | 45/48 (SW480, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +7.2 | 9e-11 | 31/44 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +6.6 | 4e-09 | 35/49 (A498, COLO 205, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.9 | 1e-04 | 29/48 (SW1417, COLO 205, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +4.5 | 7e-04 | 26/48 (BT-474, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.20× | +3.3 | 0.059 | 24/48 (HT-29, AsPC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.12 | 23/48 (hTERT-HPNE, PANC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.0 | 0.12 | 0/50 | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | 1.18× | +3.0 | 0.12 | 22/50 (LS 180, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12341.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 5 lines (NCI-H460 0.369×, HOP62 0.499×, J82 0.529×, A-427 0.509×, …; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H460 0.423×, NCI-H2030 0.550×, NCI-H1792 0.638×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.485×, HEC-1-A 0.542×; ⚠ cell-cycle shift, explains ~0% of this change); [[Capmatinib (drug)]] 5 µM in 1 line (CHP-212 0.0382×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.607×** | -9.1 | 6e-17 | 42/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.843× | -3.2 | 0.19 | 21/48 (HepG2/C3A, BT-474, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.845× | -3.2 | 0.19 | 19/48 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 0.792× | -3.2 | 0.19 | 30/48 (SW1417, NCI-H2030, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.893× | -3.1 | 0.19 | 16/49 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.798× | -3.1 | 0.19 | 27/49 (BT-474, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.852× | -3.0 | 0.19 | 20/48 (H4, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12341. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 368 | 4 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.11× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.624× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 122 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.12× (z +13.2) | — |
| [[SW480 (line)]] | alt | 348 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.26× (z +13.0) | — |
| [[A498 (line)]] | wt | 206 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +18.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HEC-1-A (line)]] | alt | 372 | 2 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.80× (z +10.3) | [[Harringtonine (drug)]] 5 µM 0.542× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 249 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.26× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 208 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.94× (z +10.5) | — |
| [[PANC-1 (line)]] | alt | 279 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.86× (z +9.3) | — |
| [[A549 (line)]] | wt | 499 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 1.97× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 399 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.499× (z -10.2) ⚠ toxic |
| [[HS-578T (line)]] | alt | 289 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.91× (z +8.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 628 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.81× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.531× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 462 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.66× (z +11.5) | — |
| [[NCI-H2030 (line)]] | alt | 965 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 782 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 284 | 2 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.05× (z +9.1) | — |
| [[A-172 (line)]] | wt | 327 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.551× (z -8.6) ⚠ toxic |
| [[A-427 (line)]] | wt | 370 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.509× (z -9.6) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 174 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.74× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 408 | 0 | 1 | — | [[Capmatinib (drug)]] 5 µM 0.0382× (z -16.6) |
| [[H4 (line)]] | wt | 353 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.450× (z -8.9) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 407 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.11× (z +9.8) | — |
| [[J82 (line)]] | alt | 411 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.529× (z -9.6) ⚠ toxic |
| [[LoVo (line)]] | wt | 292 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 509 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.517× (z -8.7) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 489 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 389 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.218× (z -12.4) ⚠ toxic |
| [[RKO (line)]] | wt | 376 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.479× (z -9.5) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 341 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.06× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 439 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.485× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 371 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.469× (z -9.0) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 361 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.90× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 300 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.73× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 430 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 322 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 471 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 439 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 436 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 240 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 207 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 369 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 300 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 321 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 369 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 374 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 286 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 370 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 480 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 357 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 609 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12341), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HUWE1]] | +0.70 | +0.62 / +0.75 | both halves | 7e-06 | STRING 602 |
| [[SPTBN1]] | +0.69 | +0.58 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[STIP1]] | +0.68 | +0.61 / +0.70 | both halves | 7e-06 | pathway: HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand |
| [[FLII]] | +0.67 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[SPTAN1]] | +0.66 | +0.49 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 562 |
| [[EIF4H]] | +0.65 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[DST]] | +0.64 | +0.55 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 549 |
| [[FKBP4]] | +0.64 | +0.68 / +0.64 | both halves | 7e-06 | pathway: HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; STRING 429 |
| [[LIN7C]] | +0.63 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[GPN1]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[AP2M1]] | +0.62 | +0.58 / +0.58 | both halves | 8e-06 | pathway: MHC class II antigen presentation |
| [[STX16]] | +0.62 | +0.54 / +0.68 | both halves | 1e-05 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |

## Genes that move opposite

*25 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG9]] | -0.65 | -0.51 / -0.70 | both halves | 1e-05 |  |
| [[SELENOH]] | -0.64 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[ZNF816-ZNF321P]] | -0.61 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[MINCR]] | -0.60 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[POLR1H]] | -0.58 | -0.37 / -0.64 | both halves | 8e-05 |  |
| [[NCBP2AS2]] | -0.58 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[MRPL23]] | -0.57 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[SNHG19]] | -0.57 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[NR1H3]] | -0.57 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[TMEM258]] | -0.57 | -0.44 / -0.60 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation |
| [[TMEM216]] | -0.56 | -0.49 / -0.63 | both halves | 1e-05 | pathway: Anchoring of the basal body to the plasma membrane |
| [[TERF2IP]] | -0.56 | -0.39 / -0.60 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO5A]] | B | MYO5A activity raises DYNC1H1's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 1.68× lower at baseline in the lines without MYO5A | 0.022 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |
| [[ZNF816-ZNF321P]] | B | ZNF816-ZNF321P activity lowers DYNC1H1's level | lines that do not express ZNF816-ZNF321P (6) vs lines expressing it (44) | 1.37× higher at baseline in the lines without ZNF816-ZNF321P | 0.044 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF816, ZNF468, ZNF701 |
| [[PSMB5]] | B | PSMB5 activity lowers DYNC1H1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DSG2]] | B | DSG2 activity lowers DYNC1H1's level | lines that do not express DSG2 (11) vs lines expressing it (39) | 1.29× higher at baseline in the lines without DSG2 | 0.084 | ⚠ within organs, on part of the lines; also absent: KITLG, COBLL1, ETS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.614). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-33.7, -19.4); signed map (-19.4, -35.8). **Vector** length 154, 53.6% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.5 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.1 | +7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.7 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +6.6 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +5.4 | +2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.3 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +4.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +3.4 | +2.7 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | +3.1 | +1.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.6 | -9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | -3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.4 | -2.4 |
|  | [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.6 | -3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.5 | -2.5 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -4.2 | -3.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.8 | -3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.8 | -2.2 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | dynein cytoplasmic 1 heavy chain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.31 — chr14:101,964,573-102,056,443 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Dnchc1, HL-3, p22, DHC1, CMT2O; previously DNECL, DNCL, DNCH1 |
| Gene groups (HGNC) | Dynein 1 complex subunits; Dynein heavy chains |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 56 pathways, smallest: Aggrephagy; COPI-independent Golgi-to-ER retrograde traffic; HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14204](https://www.uniprot.org/uniprotkb/Q14204) (Cytoplasmic dynein 1 heavy chain 1):

> Cytoplasmic dynein 1 acts as a motor for the intracellular retrograde motility of vesicles and organelles along microtubules. Dynein has ATPase activity; the force-producing power stroke is thought to occur on release of ADP. Plays a role in mitotic spindle assembly and metaphase plate congression.

**Summary**, from NCBI Gene [1778](https://www.ncbi.nlm.nih.gov/gene/1778):

> Dyneins are a group of microtubule-activated ATPases that function as molecular motors. They are divided into two subgroups of axonemal and cytoplasmic dyneins. The cytoplasmic dyneins function in intracellular motility, including retrograde axonal transport, protein sorting, organelle movement, and spindle dynamics. Molecules of conventional cytoplasmic dynein are comprised of 2 heavy chain polypeptides and a number of intermediate and light chains.This gene encodes a member of the cytoplasmic …

**Accessions** — [HGNC:2961](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2961) · Entrez [1778](https://www.ncbi.nlm.nih.gov/gene/1778) · UniProt [Q14204](https://www.uniprot.org/uniprotkb/Q14204) · Ensembl [ENSG00000197102](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197102)

## Data

Gene col 12341: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12341); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12341, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12341]; `tensor/DDL_lfc|DDL_z.npy` [12341]; `embed/gene_vectors.npy` [12341]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12341 or target_col == 12341). Every well: [[DYNC1H1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYNC1H1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
