---
symbol: "INHBA"
type: "gene"
col: 4358
ensembl_id: "ENSG00000122641"
name: "inhibin subunit beta A"
location: "7p14.1"
module: 112
arm: "+"
pooled_cpm: 159.3
n_lines_expressing: 18
n_dd_up: 15
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 26
direction_downstream: 17
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# INHBA

*inhibin subunit beta A* — 7p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.57× (z +8.2, q 1e-13, up in 3 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.59× (z +5.7, q 1e-06, up in 9 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 0.508× (z -5.9, q 2e-06, down in 13 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CXCL8]] (+0.73, fdr 7e-06), [[IL6]] (+0.70, fdr 7e-06), [[PTGS2]] (+0.68, fdr 7e-06); moves opposite to [[CLASP1]] (-0.52, fdr 3e-05), [[MAPK14]] (-0.52, fdr 3e-05), [[CHPT1]] (-0.51, fdr 3e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 17 go from it, the strongest it → [[ACVR1C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4358.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +8.2 | 1e-13 | 3/17 (LOX-IMVI, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.40×** | +7.3 | 6e-11 | 15/16 (NCI-H1573, A498, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.70×** | +6.6 | 1e-08 | 11/16 (BT-474, A498, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.96×** | +5.9 | 7e-07 | 11/16 (Panc 03.27, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +5.8 | 9e-07 | 9/16 (BT-474, NCI-H460, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +5.7 | 1e-06 | 9/16 (BT-474, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.92×** | +5.3 | 1e-05 | 4/15 (SNU-423, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.68×** | +4.5 | 4e-04 | 13/16 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +4.5 | 4e-04 | 10/17 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.55×** | +3.9 | 0.007 | 9/16 (BT-474, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.54×** | +3.8 | 0.008 | 11/16 (NCI-H460, Panc 03.27, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +3.7 | 0.010 | 1/15 (NCI-H1573) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.52×** | +3.7 | 0.010 | 0/16 | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.059 | 10/15 (H4, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.85×** | +3.1 | 0.071 | 7/16 (HS-578T, Panc 03.27, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4358.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.508×** | -5.9 | 2e-06 | 13/16 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.526×** | -5.6 | 7e-06 | 12/16 (NCI-H460, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.576×** | -4.8 | 3e-04 | 6/16 (BT-474, NCI-H1573, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.581×** | -4.3 | 0.002 | 11/15 (SHP-77, NCI-H2030, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.613×** | -4.2 | 0.002 | 10/16 (A498, HS-578T, …) | all doses, flat | position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **0.613×** | -4.2 | 0.002 | 11/16 (SHP-77, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **0.715×** | -4.1 | 0.003 | 11/16 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.608×** | -4.0 | 0.004 | 5/16 (BT-474, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.632×** | -4.0 | 0.004 | 13/16 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.645×** | -3.8 | 0.008 | 12/16 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 5 µM |  | **0.434×** | -3.8 | 0.008 | 11/16 (A498, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Encorafenib (drug)]] 5 µM |  | **0.442×** | -3.7 | 0.010 | 6/16 (NCI-H1573, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.655×** | -3.7 | 0.011 | 11/16 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.664×** | -3.6 | 0.016 | 14/16 (HS-578T, NCI-H460, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.671×** | -3.5 | 0.020 | 14/16 (H4, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.763×** | -3.2 | 0.041 | 3/16 (BT-474, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4358. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 3,369 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -12.4) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.275× (z -9.1) |
| [[HS-578T (line)]] | alt | 680 | 3 (3 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +13.4) ⚠ cell-cycle shift, explains ~68% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -11.9) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Budesonide (drug)]] 5 µM 0.302× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 509 | 1 | 5 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.86× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -17.3) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.312× (z -9.2) |
| [[SHP-77 (line)]] | alt | 703 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -17.5) ⚠ cell-cycle shift, explains ~75% of this change |
| [[A498 (line)]] | wt | 75.0 | 4 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.05× (z +15.6) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 7.23× (z +10.4) | [[Clobetasol propionate (drug)]] 5 µM 0.192× (z -8.6) |
| [[BT-474 (line)]] | alt | 86.2 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +17.0) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 4.63× (z +9.1) | [[Selinexor (drug)]] 5 µM 0.209× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 59.9 | 3 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 12.2× (z +15.8) | [[Selinexor (drug)]] 5 µM 0.366× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 144 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -14.8) ⚠ cell-cycle shift, explains ~75% of this change |
| [[Panc 03.27 (line)]] | alt | 349 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +14.6) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[RPMI-7951 (line)]] | alt | 555 | 2 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 7.10× (z +12.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.60× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -14.9) ⚠ cell-cycle shift, explains ~75% of this change |
| [[SNU-423 (line)]] | alt | 235 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 16.2× (z +14.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[H4 (line)]] | wt | 437 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.155× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -8.5) ⚠ cell-cycle shift, explains ~68% of this change |
| [[A-172 (line)]] | wt | 29.5 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 29.7 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 39.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 17.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.6 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 16.9 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 36.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 26.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 16.7 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 388 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.6 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 20.3 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 37.3 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 135 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 19.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.6 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 20.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 302 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.7 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 16.2 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 18.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.9 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 31.9 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 27.4 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 13.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4358), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXCL8]] | +0.73 | +0.68 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[IL6]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 400 |
| [[PTGS2]] | +0.68 | +0.72 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[FZD8]] | +0.66 | +0.63 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[GREM1]] | +0.65 | +0.57 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 410 |
| [[LINC01060]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[TRAF1]] | +0.64 | +0.63 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[IL1B]] | +0.63 | +0.55 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[MEG3]] | +0.63 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[IER3]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[COL22A1]] | +0.63 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[IL11]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLASP1]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[MAPK14]] | -0.52 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[CHPT1]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 7, C 19. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers INHBA's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[ADAMTSL1]] | B | ADAMTSL1 activity raises INHBA's level | lines that do not express ADAMTSL1 (18) vs lines expressing it (32) | 3.77× lower at baseline in the lines without ADAMTSL1 | 0.064 | ⚠ within organs, on part of the lines; also absent: SHOX2, ACTN2, AK5; maybe low, not absent |
| [[CD274]] | B | CD274 activity raises INHBA's level | lines that do not express CD274 (18) vs lines expressing it (32) | 3.31× lower at baseline in the lines without CD274 | 0.069 | ⚠ within organs, on part of the lines; also absent: GBP5, IL1B, PDCD1LG2 |
| [[GAP43]] | B | GAP43 activity raises INHBA's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 2.51× lower at baseline in the lines without GAP43 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent |
| [[RIMS1]] | B | RIMS1 activity raises INHBA's level | lines that do not express RIMS1 (18) vs lines expressing it (32) | 4.18× lower at baseline in the lines without RIMS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ELOVL4, GLRB, RNF150; maybe low, not absent |
| [[CLDN1]] | B | CLDN1 activity lowers INHBA's level | lines that do not express CLDN1 (23) vs lines expressing it (27) | 2.01× higher at baseline in the lines without CLDN1 | 0.097 | ⚠ within organs, on part of the lines; also absent: EDN1, CRIP1, SHH |
| [[BMPER]] | B | BMPER activity raises INHBA's level | lines that do not express BMPER (21) vs lines expressing it (29) | 3.26× lower at baseline in the lines without BMPER | 0.099 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[CCL3]] | C | CCL3 activity raises INHBA's level | lines that do not express CCL3 (37) vs lines expressing it (13) | 6.76× lower at baseline in the lines without CCL3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1; co-absent with the target |
| [[IL6]] | C | IL6 activity raises INHBA's level | lines that do not express IL6 (32) vs lines expressing it (18) | 6.39× lower at baseline in the lines without IL6 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2; co-absent with the target |
| [[TNFRSF11B]] | C | TNFRSF11B activity raises INHBA's level | lines that do not express TNFRSF11B (26) vs lines expressing it (24) | 4.94× lower at baseline in the lines without TNFRSF11B | 0.008 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12; co-absent with the target |
| [[HGF]] | C | HGF activity raises INHBA's level | lines that do not express HGF (38) vs lines expressing it (12) | 3.68× lower at baseline in the lines without HGF | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; co-absent with the target |
| [[TRPC4]] | C | TRPC4 activity raises INHBA's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 4.78× lower at baseline in the lines without TRPC4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 4, C 13. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACVR1C]] | B | INHBA activity raises ACVR1C's level | lines that do not express INHBA (32) vs lines expressing it (18) | 1.87× lower at baseline in the lines without INHBA | 0.024 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3 |
| [[NR3C1]] | B | INHBA activity raises NR3C1's level | lines that do not express INHBA (32) vs lines expressing it (18) | 3.51× lower at baseline in the lines without INHBA | 0.037 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3 |
| [[BMPER]] | B | INHBA activity raises BMPER's level | lines that do not express INHBA (32) vs lines expressing it (18) | 2.72× lower at baseline in the lines without INHBA | 0.042 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3 |
| [[PPIF]] | B | INHBA activity raises PPIF's level | lines that do not express INHBA (32) vs lines expressing it (18) | 1.42× lower at baseline in the lines without INHBA | 0.095 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3 |
| [[IL6]] | C | INHBA activity raises IL6's level | lines that do not express INHBA (32) vs lines expressing it (18) | 6.38× lower at baseline in the lines without INHBA | 0.022 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3; co-absent with the target |
| [[CXCL8]] | C | INHBA activity raises CXCL8's level | lines that do not express INHBA (32) vs lines expressing it (18) | 4.57× lower at baseline in the lines without INHBA | 0.032 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3; co-absent with the target |
| [[AJAP1]] | C | INHBA activity raises AJAP1's level | lines that do not express INHBA (32) vs lines expressing it (18) | 3.07× lower at baseline in the lines without INHBA | 0.048 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3; co-absent with the target |
| [[PKIA]] | C | INHBA activity raises PKIA's level | lines that do not express INHBA (32) vs lines expressing it (18) | 3.54× lower at baseline in the lines without INHBA | 0.054 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3; co-absent with the target |
| [[CCL3]] | C | INHBA activity raises CCL3's level | lines that do not express INHBA (32) vs lines expressing it (18) | 1.73× lower at baseline in the lines without INHBA | 0.054 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3; co-absent with the target |
| [[COL22A1]] | C | INHBA activity raises COL22A1's level | lines that do not express INHBA (32) vs lines expressing it (18) | 3.40× lower at baseline in the lines without INHBA | 0.055 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3; co-absent with the target |
| [[TNFRSF11B]] | C | INHBA activity raises TNFRSF11B's level | lines that do not express INHBA (32) vs lines expressing it (18) | 1.88× lower at baseline in the lines without INHBA | 0.061 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3; co-absent with the target |
| [[TRPC4]] | C | INHBA activity raises TRPC4's level | lines that do not express INHBA (32) vs lines expressing it (18) | 3.22× lower at baseline in the lines without INHBA | 0.065 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3; co-absent with the target |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.761). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.7, 14.0); signed map (19.3, 50.4). **Vector** length 85.8, 29.4% of its response variance represented; |z| ≥ 3 in 729 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-10 signaling* (reactome, mean cos +0.63 to 5); *Interleukin-4 and Interleukin-13 signaling* (reactome, mean cos +0.60 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.6 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.4 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.8 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.8 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +2.5 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -4.5 | -5.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.0 | -5.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.7 | -3.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.4 | -4.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.4 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | inhibin subunit beta A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.1 — chr7:41,667,168-41,705,834 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Inhibin subunits |
| Hallmark sets | ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, KRAS_SIGNALING_UP, EPITHELIAL_MESENCHYMAL_TRANSITION, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 9 pathways, smallest: Antagonism of Activin by Follistatin; Glycoprotein hormones; TGFBR3 regulates activin signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P08476](https://www.uniprot.org/uniprotkb/P08476) (Inhibin beta A chain):

> Inhibins/activins are involved in regulating a number of diverse functions such as hypothalamic and pituitary hormone secretion, gonadal hormone secretion, germ cell development and maturation, erythroid differentiation, insulin secretion, nerve cell survival, embryonic axial development or bone growth, depending on their subunit composition.; Activin A is a homodimer of INHBA that plays a role in several essential biological processes including embryonic development, stem cell maintenance and …

**Summary**, from NCBI Gene [3624](https://www.ncbi.nlm.nih.gov/gene/3624):

> This gene encodes a member of the TGF-beta (transforming growth factor-beta) superfamily of proteins. The encoded preproprotein is proteolytically processed to generate a subunit of the dimeric activin and inhibin protein complexes. These complexes activate and inhibit, respectively, follicle stimulating hormone secretion from the pituitary gland. The encoded protein also plays a role in eye, tooth and testis development. Elevated expression of this gene may be associated with cancer cachexia …

**Accessions** — [HGNC:6066](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6066) · Entrez [3624](https://www.ncbi.nlm.nih.gov/gene/3624) · UniProt [P08476](https://www.uniprot.org/uniprotkb/P08476) · Ensembl [ENSG00000122641](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122641)

## Data

Gene col 4358: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4358); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4358, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4358]; `tensor/DDL_lfc|DDL_z.npy` [4358]; `embed/gene_vectors.npy` [4358]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4358 or target_col == 4358). Every well: [[INHBA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INHBA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
