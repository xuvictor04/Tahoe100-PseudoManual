---
symbol: "INTU"
type: "gene"
col: 8852
ensembl_id: "ENSG00000164066"
name: "inturned planar cell polarity protein"
location: "4q28.1"
module: 64
arm: "+"
pooled_cpm: 21.64
n_lines_expressing: 48
n_dd_up: 27
n_dd_down: 20
n_dd_up_clean: 24
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# INTU

*inturned planar cell polarity protein* — 4q28.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.58× (z +11.7, q 5e-29, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.636× (z -11.6, q 3e-28, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFCAB7]] (+0.78, fdr 7e-06), [[TMLHE]] (+0.70, fdr 1e-05), [[DYNC2LI1]] (+0.69, fdr 7e-06); moves opposite to [[KLF13]] (-0.58, fdr 7e-06), [[LINC01128]] (-0.57, fdr 1e-05), [[MAPKAPK2]] (-0.57, fdr 7e-06).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8852.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +11.7 | 5e-29 | 28/46 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.87×** | +10.5 | 2e-23 | 34/46 (HOP62, C32, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +9.9 | 8e-21 | 32/46 (NCI-H2347, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.55×** | +8.0 | 3e-13 | 29/46 (HOP62, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +7.8 | 8e-13 | 25/45 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[NG25 (drug)]] 5 µM |  | **2.17×** | +7.3 | 2e-11 | 29/43 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +6.4 | 1e-08 | 27/46 (HOP62, LS 180, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +6.0 | 1e-07 | 21/46 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +5.8 | 4e-07 | 22/46 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +5.8 | 5e-07 | 24/45 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.33×** | +5.1 | 1e-05 | 17/46 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.8 | 9e-05 | 14/42 (HOP62, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.23×** | +4.5 | 3e-04 | 20/46 (SW480, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +4.5 | 3e-04 | 12/46 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.28×** | +4.5 | 3e-04 | 16/46 (LoVo, A498, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.28×** | +4.3 | 7e-04 | 14/45 (NCI-H23, C32, …) | all doses, stronger at high dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.28×** | +4.2 | 7e-04 | 17/46 (HEC-1-A, C-33 A, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8852.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.636×** | -11.6 | 3e-28 | 37/46 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.670×** | -10.2 | 4e-22 | 32/46 (RPMI-7951, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.574×** | -9.7 | 7e-20 | 31/45 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.728×** | -8.1 | 6e-14 | 33/46 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.651×** | -7.8 | 1e-12 | 29/45 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.661×** | -7.5 | 6e-12 | 25/45 (MIA PaCa-2, CFPAC-1, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.666×** | -7.4 | 2e-11 | 28/45 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.692×** | -6.7 | 2e-09 | 25/45 (SW 900, Panc 03.27, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.495×** | -6.7 | 2e-09 | 25/44 (SW480, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.699×** | -6.5 | 5e-09 | 23/45 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.696×** | -6.3 | 1e-08 | 27/45 (CFPAC-1, Panc 03.27, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.541×** | -5.8 | 3e-07 | 23/44 (HCT15, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.737×** | -5.5 | 1e-06 | 20/45 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.758×** | -5.0 | 2e-05 | 20/45 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.767×** | -4.6 | 2e-04 | 19/45 (HOP62, COLO 205, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.794×** | -4.2 | 9e-04 | 15/45 (LOX-IMVI, HEC-1-A, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **0.651×** | -4.1 | 0.002 | 18/44 (NCI-H1573, CHP-212, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 0.5 µM |  | **0.830×** | -3.4 | 0.020 | 11/46 (J82, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8852. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 20.3 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.272× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.389× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 28.4 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -10.1) |
| [[A-427 (line)]] | wt | 37.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +14.7) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 23.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.261× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 24.8 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.324× (z -10.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -9.9) |
| [[HOP62 (line)]] | alt | 24.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.98× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 10.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 23.7 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0857× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 21.1 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.363× (z -9.3) |
| [[HCT15 (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 30.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.232× (z -12.8) |
| [[HT-29 (line)]] | alt | 21.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 48.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 26.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.6) | — |
| [[RKO (line)]] | wt | 23.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.54× (z +15.1) | — |
| [[RPMI-7951 (line)]] | alt | 28.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -11.4) |
| [[SW 900 (line)]] | alt | 24.1 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.117× (z -12.2) |
| [[SW1417 (line)]] | alt | 7.53 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0710× (z -10.7) |
| [[A-172 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8852), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB7]] | +0.78 | +0.79 / +0.75 | both halves | 7e-06 | pathway: Signaling by Hedgehog |
| [[TMLHE]] | +0.70 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[DYNC2LI1]] | +0.69 | +0.65 / +0.70 | both halves | 7e-06 | STRING 534 |
| [[CLUAP1]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[CEP162]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[CCDC43]] | +0.66 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[TCTN1]] | +0.63 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[BBS1]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[FAM204A]] | +0.63 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[APOOL]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[NPHP1]] | +0.62 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[CUL5]] | +0.62 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF13]] | -0.58 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[LINC01128]] | -0.57 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[MAPKAPK2]] | -0.57 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[KLHL29]] | -0.54 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[TLNRD1]] | -0.53 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[CCNYL1]] | -0.51 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[CCDC168]] | -0.51 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[GATAD2A]] | -0.50 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.50 | -0.37 / -0.55 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers INTU's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.680). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-24.2, 0.4); signed map (-20.4, -20.4). **Vector** length 113, 28.9% of its response variance represented; |z| ≥ 3 in 1,089 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.9 | +8.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.6 | +10.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.4 | +7.8 |
|  | [[NG25 (drug)]] 5 µM |  | +6.2 | +7.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.5 | +9.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +6.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +5.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.6 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.6 | -11.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -10.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.5 | -7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.6 | -8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -6.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.1 | -6.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.7 | -7.5 |

## What is on record

|  |  |
|---|---|
| Name | inturned planar cell polarity protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q28.1 — chr4:127,623,271-127,726,737 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1284, CPLANE4; previously PDZK6, PDZD6 |
| Gene groups (HGNC) | PDZ domain containing; Ciliogenesis and planar polarity effector complex subunits |
| Reactome | 2 pathways, smallest: Hedgehog 'off' state; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULD6](https://www.uniprot.org/uniprotkb/Q9ULD6) (Protein inturned):

> Plays a key role in ciliogenesis and embryonic development. Regulator of cilia formation by controlling the organization of the apical actin cytoskeleton and the positioning of the basal bodies at the apical cell surface, which in turn is essential for the normal orientation of elongating ciliary microtubules. Plays a key role in definition of cell polarity via its role in ciliogenesis but not via conversion extension. Has an indirect effect on hedgehog signaling (By similarity). Proposed to …

**Summary**, from NCBI Gene [27152](https://www.ncbi.nlm.nih.gov/gene/27152):

> Predicted to enable phosphatidylinositol binding activity. Involved in embryonic digit morphogenesis; roof of mouth development; and tongue morphogenesis. Located in ciliary basal body and motile cilium. Implicated in asphyxiating thoracic dystrophy and orofaciodigital syndrome XVII. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29239](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29239) · Entrez [27152](https://www.ncbi.nlm.nih.gov/gene/27152) · UniProt [Q9ULD6](https://www.uniprot.org/uniprotkb/Q9ULD6) · Ensembl [ENSG00000164066](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164066)

## Data

Gene col 8852: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8852); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8852, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8852]; `tensor/DDL_lfc|DDL_z.npy` [8852]; `embed/gene_vectors.npy` [8852]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8852 or target_col == 8852). Every well: [[INTU — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INTU.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
