---
symbol: "GNB4"
type: "gene"
col: 3555
ensembl_id: "ENSG00000114450"
name: "G protein subunit beta 4"
location: "3q26.33"
module: 55
arm: "+"
pooled_cpm: 71.6
n_lines_expressing: 32
n_dd_up: 4
n_dd_down: 26
n_dd_up_clean: 2
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 10
direction_downstream: 5
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# GNB4

*G protein subunit beta 4* — 3q26.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.24× (z +4.4, q 0.007, up in 14 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.28× (z +3.7, q 0.031, up in 14 of 29 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1792 2.77×, Panc 03.27 2.84×; ⚠ toxic; transcription drop); [[Triamcinolone (drug)]] 5 µM in 2 lines (LOX-IMVI 1.76×, A-172 1.52×); [[Triamcinolone (drug)]] 0.5 µM in 2 lines (LOX-IMVI 2.17×, A-172 1.98×); [[Budesonide (drug)]] 0.05 µM in 1 line (LOX-IMVI 2.10×).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.221× (z -44.5, q 0e+00, down in 30 of 30 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRPX]] (+0.54, fdr 2e-05), [[ADAMTS2]] (+0.53, fdr 4e-05), [[DENND2A]] (+0.51, fdr 4e-05); moves opposite to [[HSD17B2]] (-0.54, fdr 5e-05), [[IL20RA]] (-0.52, fdr 8e-04, ⚠ one half only (not replicated)), [[TNFRSF14-AS1]] (-0.51, fdr 2e-04), [[TMC4]] (-0.48, fdr 3e-04).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[STK31]] → it (grade B ⚠); 5 go from it, the strongest it → [[TRAM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3555.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1792 2.77×, Panc 03.27 2.84×; ⚠ toxic; transcription drop); [[Triamcinolone (drug)]] 5 µM in 2 lines (LOX-IMVI 1.76×, A-172 1.52×); [[Triamcinolone (drug)]] 0.5 µM in 2 lines (LOX-IMVI 2.17×, A-172 1.98×); [[Budesonide (drug)]] 0.05 µM in 1 line (LOX-IMVI 2.10×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +4.4 | 0.007 | 14/27 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.22×** | +4.1 | 0.011 | 14/31 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.8 | 0.025 | 0/31 | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.031 | 14/29 (SHP-77, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.070 | 10/30 (NCI-H1792, HOP62, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.070 | 9/30 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.10 | 10/30 (HS-578T, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3555.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.221×** | -44.5 | 0e+00 | 30/30 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.381×** | -20.2 | 0e+00 | 30/30 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.398×** | -19.2 | 0e+00 | 28/30 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.414×** | -17.7 | 0e+00 | 26/30 (SK-MEL-2, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.452×** | -16.6 | 0e+00 | 29/30 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.504×** | -14.3 | 2e-44 | 18/30 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.245×** | -13.3 | 1e-38 | 29/31 (SK-MEL-2, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.584×** | -11.2 | 2e-27 | 24/30 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.579×** | -10.8 | 3e-25 | 24/30 (A-172, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.348×** | -10.0 | 8e-22 | 24/30 (SW 900, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.657×** | -8.7 | 1e-16 | 26/30 (NCI-H2347, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.660×** | -8.7 | 2e-16 | 22/30 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.673×** | -8.3 | 6e-15 | 21/30 (A-172, H4, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.764×** | -7.9 | 9e-14 | 21/30 (NCI-H2347, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.696×** | -7.5 | 2e-12 | 23/30 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.704×** | -7.3 | 8e-12 | 23/30 (A-172, H4, …) | two highest doses | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3555. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 196 | 7 | 11 (2 ⚠) | [[Triamcinolone (drug)]] 5 µM 1.76× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -28.8) |
| [[SK-MEL-2 (line)]] | alt | 241 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -38.8) |
| [[A-172 (line)]] | wt | 386 | 2 | 11 (1 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 1.98× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -40.1) |
| [[HOP62 (line)]] | alt | 104 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -34.9) |
| [[NCI-H460 (line)]] | wt | 69.3 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.286× (z -16.2) |
| [[HS-578T (line)]] | alt | 193 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -41.5) |
| [[H4 (line)]] | wt | 142 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -27.0) |
| [[NCI-H1792 (line)]] | alt | 86.5 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -25.8) |
| [[A549 (line)]] | wt | 57.3 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -23.6) |
| [[J82 (line)]] | alt | 219 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -38.4) |
| [[A-427 (line)]] | wt | 220 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -28.3) |
| [[hTERT-HPNE (line)]] | wt | 151 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -26.7) |
| [[PANC-1 (line)]] | alt | 65.3 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -29.7) |
| [[RPMI-7951 (line)]] | alt | 170 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -38.1) |
| [[A498 (line)]] | wt | 62.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -23.0) |
| [[NCI-H23 (line)]] | alt | 56.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -23.5) |
| [[NCI-H2347 (line)]] | alt | 118 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -20.7) |
| [[SNU-423 (line)]] | alt | 47.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0938× (z -26.0) |
| [[SW 1088 (line)]] | alt | 109 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.0403× (z -12.5) |
| [[SW 900 (line)]] | alt | 36.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -17.2) |
| [[C-33 A (line)]] | alt | 121 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -12.8) |
| [[C32 (line)]] | wt | 62.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -12.1) |
| [[CFPAC-1 (line)]] | alt | 37.1 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.44× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.5) |
| [[CHP-212 (line)]] | wt | 110 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 50.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -13.4) |
| [[SHP-77 (line)]] | alt | 58.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -9.2) |
| [[BT-474 (line)]] | alt | 29.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 58.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -24.8) |
| [[AN3 CA (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.11 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.12 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.39 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.10 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.89 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.71 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.74 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.66 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.06 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.46 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.70 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.36 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.23 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.65 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3555), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRPX]] | +0.54 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[ADAMTS2]] | +0.53 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[DENND2A]] | +0.51 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[LINC01615]] | +0.50 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[CNRIP1]] | +0.49 | +0.60 / +0.32 | both halves | 2e-04 |  |
| [[RNF144A]] | +0.48 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[ITGA4]] | +0.44 | +0.47 / +0.36 | both halves | 1e-04 |  |
| [[CPQ]] | +0.44 | +0.49 / +0.44 | both halves | 3e-05 | pathway: HALLMARK_COMPLEMENT |
| [[LOX]] | +0.44 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[CHROMR]] | +0.43 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[AFAP1L1]] | +0.43 | +0.52 / +0.35 | both halves | 1e-04 |  |
| [[WIPF1]] | +0.43 | +0.57 / +0.37 | both halves | 8e-05 | pathway: Leishmania infection |

## Genes that move opposite

*62 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSD17B2]] | -0.54 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[IL20RA]] | -0.52 | -0.58 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[TNFRSF14-AS1]] | -0.51 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[TMC4]] | -0.48 | -0.53 / -0.28 | both halves | 3e-04 |  |
| [[C9orf152]] | -0.47 | -0.46 / -0.25 | both halves | 4e-04 |  |
| [[ABO]] | -0.46 | -0.57 / -0.21 | both halves | 6e-04 |  |
| [[MUC2]] | -0.46 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[EPS8L3]] | -0.46 | -0.53 / -0.26 | both halves | 4e-04 |  |
| [[SPINT1-AS1]] | -0.46 | -0.50 / -0.25 | both halves | 4e-04 |  |
| [[GPR35]] | -0.45 | -0.48 / -0.26 | both halves | 3e-04 | pathway: GPCR ligand binding |
| [[ZMIZ1-AS1]] | -0.45 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[ARHGEF34P]] | -0.44 | -0.44 / -0.24 | both halves | 5e-04 |  |
| [[FGD5]] | -0.44 | -0.48 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STK31]] | B | STK31 activity raises GNB4's level | lines that do not express STK31 (6) vs lines expressing it (44) | 2.89× lower at baseline in the lines without STK31 | 0.026 | ⚠ within organs, on part of the lines; also absent: HPSE, LTBP4, STRIP2; maybe low, not absent |
| [[KATNAL1]] | B | KATNAL1 activity raises GNB4's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 5.50× lower at baseline in the lines without KATNAL1 | 0.054 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[GPR35]] | B | GPR35 activity lowers GNB4's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 5.42× higher at baseline in the lines without GPR35 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[DMTN]] | B | DMTN activity lowers GNB4's level | lines that do not express DMTN (14) vs lines expressing it (36) | 4.08× higher at baseline in the lines without DMTN | 0.089 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[BVES]] | C | BVES activity raises GNB4's level | lines that do not express BVES (19) vs lines expressing it (31) | 11.50× lower at baseline in the lines without BVES | 5e-04 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2; co-absent with the target |
| [[SLC8A1]] | C | SLC8A1 activity raises GNB4's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 6.31× lower at baseline in the lines without SLC8A1 | 0.008 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3; co-absent with the target |
| [[PRR16]] | C | PRR16 activity raises GNB4's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 9.19× lower at baseline in the lines without PRR16 | 0.018 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2; co-absent with the target |
| [[WIPF1]] | C | WIPF1 activity raises GNB4's level | lines that do not express WIPF1 (16) vs lines expressing it (34) | 10.43× lower at baseline in the lines without WIPF1 | 0.026 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, GNB4, POPDC3; co-absent with the target |
| [[ADAMTS2]] | C | ADAMTS2 activity raises GNB4's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 4.99× lower at baseline in the lines without ADAMTS2 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1; co-absent with the target |
| [[LINC01615]] | C | LINC01615 activity raises GNB4's level | lines that do not express LINC01615 (36) vs lines expressing it (14) | 5.41× lower at baseline in the lines without LINC01615 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRAM2]] | B | GNB4 activity raises TRAM2's level | lines that do not express GNB4 (18) vs lines expressing it (32) | 2.11× lower at baseline in the lines without GNB4 | 0.040 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES, BVES-AS1 |
| [[KATNAL1]] | B | GNB4 activity raises KATNAL1's level | lines that do not express GNB4 (18) vs lines expressing it (32) | 2.67× lower at baseline in the lines without GNB4 | 0.099 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES, BVES-AS1 |
| [[WIPF1]] | C | GNB4 activity raises WIPF1's level | lines that do not express GNB4 (18) vs lines expressing it (32) | 8.27× lower at baseline in the lines without GNB4 | 0.004 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES, BVES-AS1; co-absent with the target |
| [[BVES]] | C | GNB4 activity raises BVES's level | lines that do not express GNB4 (18) vs lines expressing it (32) | 4.88× lower at baseline in the lines without GNB4 | 0.008 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES, BVES-AS1; co-absent with the target |
| [[SLC8A1]] | C | GNB4 activity raises SLC8A1's level | lines that do not express GNB4 (18) vs lines expressing it (32) | 5.39× lower at baseline in the lines without GNB4 | 0.076 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES, BVES-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction -0.447). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (54.2, 24.3); signed map (26.9, 46.5). **Vector** length 97.7, 27.0% of its response variance represented; |z| ≥ 3 in 1,009 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +4.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.4 | +2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.1 | +3.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.0 | +1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +3.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.6 | -17.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.5 | -13.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.6 | -4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.5 | -10.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.4 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -8.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -10.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit beta 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.33 — chr3:179,396,088-179,451,476 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | WD repeat domain containing; G protein subunits beta |
| Hallmark sets | COMPLEMENT |
| Reactome | 66 pathways, smallest: G beta:gamma signalling through BTK; Prostacyclin signalling through prostacyclin receptor; G beta:gamma signalling through PLC beta |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAV0](https://www.uniprot.org/uniprotkb/Q9HAV0) (Guanine nucleotide-binding protein subunit beta-4):

> Guanine nucleotide-binding proteins (G proteins) are involved as a modulator or transducer in various transmembrane signaling systems. The beta and gamma chains are required for the GTPase activity, for replacement of GDP by GTP, and for G protein-effector interaction.

**Summary**, from NCBI Gene [59345](https://www.ncbi.nlm.nih.gov/gene/59345):

> Heterotrimeric guanine nucleotide-binding proteins (G proteins), which integrate signals between receptors and effector proteins, are composed of an alpha, a beta, and a gamma subunit. These subunits are encoded by families of related genes. This gene encodes a beta subunit. Beta subunits are important regulators of alpha subunits, as well as of certain signal transduction receptors and effectors. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20731](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20731) · Entrez [59345](https://www.ncbi.nlm.nih.gov/gene/59345) · UniProt [Q9HAV0](https://www.uniprot.org/uniprotkb/Q9HAV0) · Ensembl [ENSG00000114450](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114450)

## Data

Gene col 3555: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3555); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3555, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3555]; `tensor/DDL_lfc|DDL_z.npy` [3555]; `embed/gene_vectors.npy` [3555]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3555 or target_col == 3555). Every well: [[GNB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
