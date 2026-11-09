---
symbol: "FABP5"
type: "gene"
col: 8989
ensembl_id: "ENSG00000164687"
name: "fatty acid binding protein 5"
location: "8q21.13"
module: 4
arm: "+"
pooled_cpm: 5.69
n_lines_expressing: 45
n_dd_up: 33
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# FABP5

*fatty acid binding protein 5* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.67× (z +15.7, q 0e+00, up in 21 of 21 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.03× (z +9.1, q 2e-17, up in 32 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.778× (z -7.9, q 2e-12, down in 25 of 42 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.154×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (RKO 0.0745×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.237×; ⚠ cell-cycle shift, explains ~43% of this change); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0696×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR3G]] (+0.69, fdr 7e-06), [[CHRNA5]] (+0.64, fdr 1e-05), [[TIMM8A]] (+0.59, fdr 1e-05); moves opposite to [[LRRC27]] (-0.54, fdr 3e-05), [[TERF2IP]] (-0.54, fdr 5e-05), [[N4BP2L2]] (-0.53, fdr 5e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PLAAT1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 18 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8989.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **5.67×** | +15.7 | 0e+00 | 21/21 (NCI-H1792, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **4.99×** | +14.0 | 6e-42 | 11/11 (NCI-H1792, A498, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.03×** | +9.1 | 2e-17 | 32/39 (NCI-H2347, NCI-H460, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.79×** | +8.6 | 2e-15 | 14/14 (A498, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **2.46×** | +8.1 | 5e-14 | 24/39 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **2.39×** | +7.9 | 4e-13 | 23/38 (SW480, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.97×** | +6.1 | 8e-08 | 20/39 (NCI-H460, SW1417, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **2.01×** | +6.1 | 1e-07 | 14/24 (LOX-IMVI, NCI-H2347, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.90×** | +5.8 | 5e-07 | 21/39 (NCI-H1792, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.89×** | +5.5 | 2e-06 | 15/29 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.49×** | +5.1 | 2e-05 | 15/33 (A549, NCI-H2347, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.74×** | +5.0 | 3e-05 | 14/38 (HT-29, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +4.6 | 2e-04 | 16/37 (HT-29, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +4.5 | 3e-04 | 10/35 (NCI-H2347, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.52×** | +4.4 | 5e-04 | 8/18 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +3.9 | 0.004 | 12/39 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.004 | 11/39 (J82, NCI-H2347, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.021 | 9/35 (NCI-H1573, NCI-H1792, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.96×** | +3.2 | 0.038 | 6/30 (CFPAC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.058 | 2/38 (RKO, SW480) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.87×** | +3.0 | 0.069 | 6/35 (CFPAC-1, NCI-H460, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.069 | 6/38 (NCI-H460, C-33 A, …) | two highest doses | position effect removed |
| [[NG25 (drug)]] 0.05 µM |  | **1.41×** | +2.9 | 0.069 | 2/38 (MIA PaCa-2, A-427) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.38×** | +2.9 | 0.073 | 6/39 (LS 180, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.38×** | +2.8 | 0.092 | 5/39 (SHP-77, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.36×** | +2.8 | 0.093 | 6/33 (A498, PANC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8989.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.154×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (RKO 0.0745×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.237×; ⚠ cell-cycle shift, explains ~43% of this change); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0696×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.778×** | -7.9 | 2e-12 | 25/42 (NCI-H2030, RPMI-7951, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.05 µM |  | 0.671× | -3.4 | 0.12 | 8/38 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | 0.680× | -3.4 | 0.12 | 8/39 (hTERT-HPNE, RKO, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.668× | -3.3 | 0.12 | 12/42 (SHP-77, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.679× | -3.3 | 0.12 | 6/39 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.687× | -3.2 | 0.12 | 11/36 (MIA PaCa-2, A498, …) | inconsistent across doses | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.715× | -3.0 | 0.19 | 9/39 (NCI-H2347, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.77 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8989. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.25 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.39× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.3× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SHP-77 (line)]] | alt | 26.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -11.7) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 5.40 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.8× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1573 (line)]] | alt | 3.45 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0696× (z -8.5) |
| [[RKO (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0745× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 6.42 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.26× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 0.862 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.899 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.821 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.14 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8989), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR3G]] | +0.69 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CHRNA5]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[TIMM8A]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[GLO1]] | +0.58 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[PPAT]] | +0.57 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[TEX15]] | +0.56 | +0.37 / +0.58 | both halves | 8e-05 |  |
| [[HPSE]] | +0.56 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[BOP1]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[NME1]] | +0.55 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[GLB1L2]] | +0.54 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[GNPNAT1]] | +0.54 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[NEIL2]] | +0.53 | +0.52 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC27]] | -0.54 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[TERF2IP]] | -0.54 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[N4BP2L2]] | -0.53 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[UPF2]] | -0.52 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[RFX1]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[CREBRF]] | -0.52 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[CHKB]] | -0.51 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[CPT1B]] | -0.51 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[SYNRG]] | -0.50 | -0.43 / -0.45 | both halves | 4e-05 |  |
| [[RBM5]] | -0.50 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[BRAP]] | -0.50 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[ENTPD3-AS1]] | -0.49 | -0.46 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAAT1]] | B | PLAAT1 activity raises FABP5's level | lines that do not express PLAAT1 (20) vs lines expressing it (30) | 1.52× lower at baseline in the lines without PLAAT1 | 0.033 | ⚠ within organs, on part of the lines; also absent: SDK1, PDGFD, SNCA |
| [[ONECUT2]] | B | ONECUT2 activity raises FABP5's level | lines that do not express ONECUT2 (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without ONECUT2 | 0.034 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers FABP5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GALNT12]] | B | GALNT12 activity lowers FABP5's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 1.13× higher at baseline in the lines without GALNT12 | 0.084 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.457). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-8.5, -40.4); signed map (-8.9, -56.3). **Vector** length 58.3, 10.4% of its response variance represented; |z| ≥ 3 in 759 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +4.9 | +15.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +4.7 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +4.2 | +8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +3.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.6 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +3.9 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -7.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -1.6 | -3.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | +0.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.1 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.6 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | fatty acid binding protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.13 — chr8:81,280,536-81,284,777 (+) |
| Ensembl biotype | protein_coding |
| Also known as | E-FABP, PA-FABP, KFABP |
| Gene groups (HGNC) | Fatty acid binding protein family |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, ESTROGEN_RESPONSE_LATE |
| Reactome | 7 pathways, smallest: Triglyceride catabolism; Triglyceride metabolism; Signaling by Retinoic Acid |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01469](https://www.uniprot.org/uniprotkb/Q01469) (Fatty acid-binding protein 5):

> Intracellular carrier for long-chain fatty acids and related active lipids, such as endocannabinoids, that regulate the metabolism and actions of the ligands they bind. In addition to the cytosolic transport, selectively delivers specific fatty acids from the cytosol to the nucleus, wherein they activate nuclear receptors. Delivers retinoic acid to the nuclear receptor peroxisome proliferator-activated receptor delta; which promotes proliferation and survival. May also serve as a synaptic …

**Summary**, from NCBI Gene [2171](https://www.ncbi.nlm.nih.gov/gene/2171):

> This gene encodes the fatty acid binding protein found in epidermal cells, and was first identified as being upregulated in psoriasis tissue. Fatty acid binding proteins are a family of small, highly conserved, cytoplasmic proteins that bind long-chain fatty acids and other hydrophobic ligands. FABPs may play roles in fatty acid uptake, transport, and metabolism. Polymorphisms in this gene are associated with type 2 diabetes. The human genome contains many pseudogenes similar to this …

**Accessions** — [HGNC:3560](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3560) · Entrez [2171](https://www.ncbi.nlm.nih.gov/gene/2171) · UniProt [Q01469](https://www.uniprot.org/uniprotkb/Q01469) · Ensembl [ENSG00000164687](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164687)

## Data

Gene col 8989: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8989); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8989, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8989]; `tensor/DDL_lfc|DDL_z.npy` [8989]; `embed/gene_vectors.npy` [8989]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8989 or target_col == 8989). Every well: [[FABP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FABP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
