---
symbol: "TRIML2"
type: "gene"
col: 10992
ensembl_id: "ENSG00000179046"
name: "tripartite motif family like 2"
location: "4q35.2"
module: 125
arm: "+"
pooled_cpm: 6.37
n_lines_expressing: 20
n_dd_up: 29
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 9
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# TRIML2

*tripartite motif family like 2* — 4q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.90× (z +26.3, q 0e+00, up in 11 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.563× (z -4.9, q 3e-04, down in 8 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 3 lines (NCI-H460 0.143×, LOX-IMVI 0.164×, C-33 A 0.0747×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H460 0.0841×, LOX-IMVI 0.150×); [[Panobinostat (drug)]] 5 µM in 2 lines (NCI-H460 0.0966×, LOX-IMVI 0.166×; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.0760×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C12orf50]] (+0.68, fdr 1e-05), [[FGF2]] (+0.66, fdr 1e-05), [[SLCO2B1]] (+0.66, fdr 1e-05); moves opposite to [[POGLUT2]] (-0.59, fdr 3e-05), [[TAF5L]] (-0.56, fdr 3e-05), [[MTMR12]] (-0.55, fdr 2e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 9 go from it, the strongest it → [[PLA2G4C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10992.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.90×** | +26.3 | 0e+00 | 11/12 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.98×** | +16.5 | 0e+00 | 11/12 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **5.79×** | +13.4 | 2e-38 | 13/15 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.90×** | +12.1 | 2e-31 | 3/5 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.34×** | +10.3 | 1e-22 | 4/8 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.24×** | +9.3 | 2e-18 | 2/6 (NCI-H460, MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.81×** | +8.8 | 1e-16 | 14/16 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.81×** | +8.8 | 1e-16 | 10/16 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.74×** | +8.6 | 6e-16 | 7/13 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +8.0 | 6e-14 | 5/13 (hTERT-HPNE, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +7.4 | 8e-12 | 6/15 (SK-MEL-2, RPMI-7951, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.30×** | +7.1 | 6e-11 | 10/15 (LOX-IMVI, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.10×** | +6.3 | 1e-08 | 9/15 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.95×** | +5.7 | 5e-07 | 10/15 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +5.4 | 2e-06 | 4/6 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.87×** | +5.3 | 4e-06 | 11/14 (LOX-IMVI, MIA PaCa-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.0 | 2e-05 | 5/15 (A549, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.83×** | +4.8 | 4e-05 | 5/14 (H4, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.70×** | +4.5 | 2e-04 | 6/15 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +4.0 | 0.002 | 6/15 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10992.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 3 lines (NCI-H460 0.143×, LOX-IMVI 0.164×, C-33 A 0.0747×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H460 0.0841×, LOX-IMVI 0.150×); [[Panobinostat (drug)]] 5 µM in 2 lines (NCI-H460 0.0966×, LOX-IMVI 0.166×; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.0760×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.563×** | -4.9 | 3e-04 | 8/15 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.563×** | -4.9 | 3e-04 | 10/15 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.678× | -3.3 | 0.13 | 6/16 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Budesonide (drug)]] 5 µM |  | 0.685× | -3.2 | 0.13 | 5/16 (HOP62, H4, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | 0.690× | -3.1 | 0.13 | 3/15 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.900× | -3.1 | 0.13 | 5/18 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.672× | -3.1 | 0.13 | 1/16 (NCI-H661) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.695× | -3.1 | 0.13 | 12/17 (NCI-H460, LOX-IMVI, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.696× | -3.1 | 0.13 | 6/15 (HOP62, H4, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | 0.503× | -3.0 | 0.13 | 5/14 (NCI-H460, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Captopril (drug)]] 0.5 µM |  | 0.700× | -3.0 | 0.13 | 2/15 (A-172, hTERT-HPNE) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10992. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 52.0 | 9 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +18.6) | [[Panobinostat (drug)]] 0.5 µM 0.0841× (z -18.8) |
| [[A549 (line)]] | wt | 25.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.4× (z +23.8) | — |
| [[LOX-IMVI (line)]] | wt | 56.9 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +12.7) | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -12.9) |
| [[C-33 A (line)]] | alt | 14.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0760× (z -12.0) |
| [[HOP62 (line)]] | alt | 12.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +14.0) | — |
| [[A-172 (line)]] | wt | 1.99 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 68.7× (z +13.1) | — |
| [[NCI-H23 (line)]] | alt | 5.81 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +12.3) | [[Proglumide (drug)]] 0.05 µM 0.0506× (z -9.7) |
| [[H4 (line)]] | wt | 33.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.46× (z +9.5) | — |
| [[J82 (line)]] | alt | 2.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.8× (z +11.4) | — |
| [[SNU-423 (line)]] | alt | 1.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 58.1× (z +12.9) | — |
| [[A-427 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.683 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.691 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.710 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.847 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.877 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.856 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.748 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.790 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.891 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.611 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.682 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.821 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.986 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.921 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.658 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.954 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.714 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.913 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.643 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10992), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C12orf50]] | +0.68 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[FGF2]] | +0.66 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[SLCO2B1]] | +0.66 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[CLIC2]] | +0.65 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[KMO]] | +0.63 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[DIO2]] | +0.62 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[CPEB1]] | +0.62 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[LINC02154]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[IL7R]] | +0.62 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[MYPN]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[LINC01828]] | +0.61 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[TMEM52B]] | +0.59 | +0.55 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGLUT2]] | -0.59 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[TAF5L]] | -0.56 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[MTMR12]] | -0.55 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[ELP1]] | -0.54 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[OXNAD1]] | -0.53 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[SMARCD2]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[PRSS23-AS1]] | -0.52 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[PHKA2]] | -0.50 | -0.31 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TRIML2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TENM3-AS1]] | C | TENM3-AS1 activity raises TRIML2's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 2.14× lower at baseline in the lines without TENM3-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLA2G4C]] | B | TRIML2 activity raises PLA2G4C's level | lines that do not express TRIML2 (30) vs lines expressing it (20) | 1.72× lower at baseline in the lines without TRIML2 | 0.023 | ⚠ within organs, on part of the lines; also absent: ZNF471, LINC01010, ENSG00000222032 |
| [[FGF2]] | B | TRIML2 activity raises FGF2's level | lines that do not express TRIML2 (30) vs lines expressing it (20) | 3.61× lower at baseline in the lines without TRIML2 | 0.027 | ⚠ within organs, on part of the lines; also absent: ZNF471, LINC01010, ENSG00000222032 |
| [[SLCO3A1]] | B | TRIML2 activity lowers SLCO3A1's level | lines that do not express TRIML2 (30) vs lines expressing it (20) | 1.64× higher at baseline in the lines without TRIML2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF471, LINC01010, ENSG00000222032 |
| [[KDM4A-AS1]] | B | TRIML2 activity raises KDM4A-AS1's level | lines that do not express TRIML2 (30) vs lines expressing it (20) | 1.37× lower at baseline in the lines without TRIML2 | 0.090 | ⚠ within organs, on part of the lines; also absent: ZNF471, LINC01010, ENSG00000222032 |
| [[LINC02456]] | B | TRIML2 activity raises LINC02456's level | lines that do not express TRIML2 (30) vs lines expressing it (20) | 1.50× lower at baseline in the lines without TRIML2 | 0.093 | ⚠ within organs, on part of the lines; also absent: ZNF471, LINC01010, ENSG00000222032 |
| [[TENM3-AS1]] | C | TRIML2 activity raises TENM3-AS1's level | lines that do not express TRIML2 (30) vs lines expressing it (20) | 2.44× lower at baseline in the lines without TRIML2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ZNF471, LINC01010, ENSG00000222032; co-absent with the target |
| [[LINC02154]] | C | TRIML2 activity raises LINC02154's level | lines that do not express TRIML2 (30) vs lines expressing it (20) | 2.66× lower at baseline in the lines without TRIML2 | 0.049 | ⚠ within organs, on part of the lines; also absent: ZNF471, LINC01010, ENSG00000222032; co-absent with the target |
| [[LINC02241]] | C | TRIML2 activity raises LINC02241's level | lines that do not express TRIML2 (30) vs lines expressing it (20) | 2.11× lower at baseline in the lines without TRIML2 | 0.072 | ⚠ within organs, on part of the lines; also absent: ZNF471, LINC01010, ENSG00000222032; co-absent with the target |
| [[ACTN2]] | C | TRIML2 activity raises ACTN2's level | lines that do not express TRIML2 (30) vs lines expressing it (20) | 3.02× lower at baseline in the lines without TRIML2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF471, LINC01010, ENSG00000222032; co-absent with the target |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.4, 23.0); signed map (40.6, 20.8). **Vector** length 51.9, 14.6% of its response variance represented; |z| ≥ 3 in 511 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +26.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +2.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.2 | -4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.8 | -4.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.6 | -3.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.2 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif family like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.2 — chr4:188,091,272-188,109,603 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25801, SPRYD6 |
| Matched by | ensembl_id |

UniProt [Q8N7C3](https://www.uniprot.org/uniprotkb/Q8N7C3) carries no function annotation.

**Summary**, from NCBI Gene [205860](https://www.ncbi.nlm.nih.gov/gene/205860):

> This gene encodes a member of the tri-partite motif (TRIM) family of proteins. This protein may be regulated by the tumor suppressor p53 and may regulate p53 through the enhancement of p53 SUMOylation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:26378](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26378) · Entrez [205860](https://www.ncbi.nlm.nih.gov/gene/205860) · UniProt [Q8N7C3](https://www.uniprot.org/uniprotkb/Q8N7C3) · Ensembl [ENSG00000179046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179046)

## Data

Gene col 10992: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10992); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10992, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10992]; `tensor/DDL_lfc|DDL_z.npy` [10992]; `embed/gene_vectors.npy` [10992]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10992 or target_col == 10992). Every well: [[TRIML2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIML2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
