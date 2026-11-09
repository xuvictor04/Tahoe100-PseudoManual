---
symbol: "C3orf52"
type: "gene"
col: 3562
ensembl_id: "ENSG00000114529"
name: "chromosome 3 open reading frame 52"
location: "3q13.2"
module: 81
arm: "+"
pooled_cpm: 63.64
n_lines_expressing: 44
n_dd_up: 30
n_dd_down: 35
n_dd_up_clean: 25
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 25
direction_downstream: 6
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# C3orf52

*chromosome 3 open reading frame 52* — 3q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 2.22× (z +9.0, q 2e-16, up in 35 of 42 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 2.17× (z +8.7, q 7e-16, up in 39 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.461× (z -12.3, q 3e-32, down in 38 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBILA]] (+0.76, fdr 7e-06, ⚠ read-through risk), [[PKIA]] (+0.68, fdr 7e-06), [[CD44]] (+0.68, fdr 7e-06), [[HBEGF]] (+0.66, fdr 7e-06); moves opposite to [[RPRD2]] (-0.62, fdr 7e-06), [[LSM14A]] (-0.58, fdr 1e-05), [[SAFB]] (-0.58, fdr 2e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[C6orf141]] → it (grade B ⚠); 6 go from it, the strongest it → [[NABP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3562.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.22×** | +9.0 | 2e-16 | 35/42 (SW 900, A498, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.17×** | +8.7 | 7e-16 | 39/42 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **2.03×** | +8.0 | 3e-13 | 38/42 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +7.9 | 4e-13 | 36/41 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.90×** | +7.2 | 6e-11 | 33/42 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.87×** | +7.0 | 2e-10 | 36/42 (SW480, HCT15, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.77×** | +6.4 | 1e-08 | 33/42 (BT-474, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.74×** | +6.0 | 1e-07 | 33/41 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.43×** | +5.7 | 8e-07 | 28/43 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.62×** | +5.4 | 3e-06 | 27/41 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +4.7 | 1e-04 | 24/42 (SW1417, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.49×** | +4.5 | 3e-04 | 24/42 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +4.4 | 4e-04 | 25/42 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +4.3 | 8e-04 | 25/41 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.45×** | +4.2 | 9e-04 | 24/42 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.47×** | +4.2 | 1e-03 | 22/41 (RPMI-7951, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.002 | 25/41 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.40×** | +3.8 | 0.005 | 21/41 (RPMI-7951, H4, …) | rises with dose | low cells (technical?) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.59×** | +3.7 | 0.006 | 23/42 (SW 900, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.96×** | +3.5 | 0.012 | 19/42 (SW48, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3562.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.461×** | -12.3 | 3e-32 | 38/43 (RKO, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.584×** | -6.1 | 3e-07 | 32/42 (HOP62, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.328×** | -5.8 | 1e-06 | 34/42 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.603×** | -5.7 | 2e-06 | 28/43 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.608×** | -5.4 | 7e-06 | 24/36 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.637×** | -5.1 | 3e-05 | 27/42 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.729×** | -5.0 | 4e-05 | 27/42 (HOP62, H4, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.636×** | -4.9 | 6e-05 | 24/41 (LoVo, SW48, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.665×** | -4.6 | 3e-04 | 29/42 (SNU-423, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.712×** | -4.5 | 3e-04 | 25/42 (SW48, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.710×** | -4.5 | 4e-04 | 24/42 (RKO, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.675×** | -4.4 | 4e-04 | 23/42 (A549, HOP62, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.662×** | -4.4 | 5e-04 | 29/42 (SW48, SK-MEL-2, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.682×** | -4.3 | 6e-04 | 26/42 (HOP62, H4, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **0.764×** | -4.3 | 6e-04 | 27/42 (SK-MEL-2, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.764×** | -4.2 | 0.001 | 26/43 (SW48, CFPAC-1, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.696×** | -4.1 | 0.001 | 25/42 (HOP62, NCI-H1573, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3562. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 106 | 0 | 13 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.183× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 104 | 5 (2 ⚠) | 1 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.93× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -9.2) |
| [[RKO (line)]] | wt | 72.6 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 106 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.78× (z +10.1) ⚠ toxic | — |
| [[NCI-H23 (line)]] | alt | 29.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 32.7 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.87× (z +9.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.05× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 57.0 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.240× (z -13.4) |
| [[SW48 (line)]] | wt | 114 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -10.2) |
| [[A-172 (line)]] | wt | 85.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -8.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 92.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -11.3) |
| [[BT-474 (line)]] | alt | 100 | 1 | 0 | [[Digitoxin (drug)]] 0.5 µM 3.43× (z +8.8) | — |
| [[H4 (line)]] | wt | 64.3 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.158× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 37.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -9.7) |
| [[Hs 766T (line)]] | wt | 68.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -9.8) |
| [[HS-578T (line)]] | alt | 103 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -10.5) |
| [[HT-29 (line)]] | alt | 106 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -11.6) |
| [[hTERT-HPNE (line)]] | wt | 76.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 62.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.591× (z -10.5) ⚠ position not correctable |
| [[NCI-H1792 (line)]] | alt | 100.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 137 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 75.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -10.7) |
| [[PANC-1 (line)]] | alt | 40.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -10.5) |
| [[SNU-423 (line)]] | alt | 47.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -10.7) |
| [[SW 900 (line)]] | alt | 30.7 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.34× (z +9.0) ⚠ unreliable plate only | — |
| [[SW480 (line)]] | alt | 30.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.06× (z +8.5) | — |
| [[A-427 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.09 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.42 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.6 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 96.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 48.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3562), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBILA]] | +0.76 | +0.66 / +0.80 | both halves | 7e-06 | ⚠ **readthrough risk**: TBILA lies 2.4 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[PKIA]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[CD44]] | +0.68 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[HBEGF]] | +0.66 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[CREB5]] | +0.64 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[NRIP3]] | +0.64 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[MIR222HG]] | +0.63 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[SEMA7A]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 | same gene group |
| [[MMP1]] | +0.63 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[PNP]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[KHDRBS3]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PTHLH]] | +0.61 | +0.56 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPRD2]] | -0.62 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[LSM14A]] | -0.58 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[SAFB]] | -0.58 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[TNRC6B]] | -0.55 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[CEP57]] | -0.55 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[CLPX]] | -0.55 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[YY1AP1]] | -0.54 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[YY1]] | -0.53 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[RCOR3]] | -0.53 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[PHC3]] | -0.52 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[PEX13]] | -0.52 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[TNRC6A]] | -0.52 | -0.46 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 22, C 3. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C6orf141]] | B | C6orf141 activity raises C3orf52's level | lines that do not express C6orf141 (21) vs lines expressing it (29) | 2.22× lower at baseline in the lines without C6orf141 | 0.003 | ⚠ within organs, on part of the lines; also absent: ADAM8, ENSG00000251584, SAMD12-AS1 |
| [[MAST4]] | B | MAST4 activity raises C3orf52's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without MAST4 | 0.007 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[F3]] | B | F3 activity raises C3orf52's level | lines that do not express F3 (24) vs lines expressing it (26) | 2.08× lower at baseline in the lines without F3 | 0.016 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[S100A16]] | B | S100A16 activity raises C3orf52's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 3.07× lower at baseline in the lines without S100A16 | 0.024 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[CXCL8]] | B | CXCL8 activity raises C3orf52's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 1.84× lower at baseline in the lines without CXCL8 | 0.027 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[LINC00707]] | B | LINC00707 activity raises C3orf52's level | lines that do not express LINC00707 (26) vs lines expressing it (24) | 1.70× lower at baseline in the lines without LINC00707 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000285845, ENSG00000285743, LINP1 |
| [[CD44]] | B | CD44 activity raises C3orf52's level | lines that do not express CD44 (15) vs lines expressing it (35) | 2.29× lower at baseline in the lines without CD44 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[FAM107B]] | B | FAM107B activity raises C3orf52's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.12× lower at baseline in the lines without FAM107B | 0.036 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[LINC01589]] | B | LINC01589 activity raises C3orf52's level | lines that do not express LINC01589 (23) vs lines expressing it (27) | 1.81× lower at baseline in the lines without LINC01589 | 0.042 | ⚠ within organs, on part of the lines; also absent: HNF1B, ENSG00000279806, GOLT1A |
| [[KRT15]] | B | KRT15 activity raises C3orf52's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.38× lower at baseline in the lines without KRT15 | 0.042 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[DUSP10]] | B | DUSP10 activity raises C3orf52's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 1.82× lower at baseline in the lines without DUSP10 | 0.053 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[CFAP20DC]] | B | CFAP20DC activity raises C3orf52's level | lines that do not express CFAP20DC (16) vs lines expressing it (34) | 1.81× lower at baseline in the lines without CFAP20DC | 0.060 | ⚠ within organs, on part of the lines; also absent: RGS17, CHST11, WDR17 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NABP1]] | B | C3orf52 activity raises NABP1's level | lines that do not express C3orf52 (6) vs lines expressing it (44) | 3.04× lower at baseline in the lines without C3orf52 | 0.081 | ⚠ within organs, on part of the lines; also absent: HTATIP2, TBILA, ISG20; maybe low, not absent; its own permutation p |
| [[CLPX]] | B | C3orf52 activity lowers CLPX's level | lines that do not express C3orf52 (6) vs lines expressing it (44) | 1.57× higher at baseline in the lines without C3orf52 | 0.088 | ⚠ within organs, on part of the lines; also absent: HTATIP2, TBILA, ISG20; maybe low, not absent |
| [[CDCP1]] | B | C3orf52 activity raises CDCP1's level | lines that do not express C3orf52 (6) vs lines expressing it (44) | 5.54× lower at baseline in the lines without C3orf52 | 0.092 | ⚠ within organs, on part of the lines; also absent: HTATIP2, TBILA, ISG20; maybe low, not absent |
| [[CFAP20DC]] | B | C3orf52 activity raises CFAP20DC's level | lines that do not express C3orf52 (6) vs lines expressing it (44) | 4.57× lower at baseline in the lines without C3orf52 | 0.098 | ⚠ within organs, on part of the lines; also absent: HTATIP2, TBILA, ISG20; maybe low, not absent |
| [[HRH1]] | C | C3orf52 activity raises HRH1's level | lines that do not express C3orf52 (6) vs lines expressing it (44) | 5.46× lower at baseline in the lines without C3orf52 | 0.081 | ⚠ within organs, on part of the lines; also absent: HTATIP2, TBILA, ISG20; maybe low, not absent; co-absent with the target |
| [[TBILA]] | C | C3orf52 activity raises TBILA's level | lines that do not express C3orf52 (6) vs lines expressing it (44) | 2.48× lower at baseline in the lines without C3orf52 | 0.081 | ⚠ within organs, on part of the lines; also absent: HTATIP2, TBILA, ISG20; maybe low, not absent; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.4, 0.7); signed map (3.8, 46.3). **Vector** length 131, 46.6% of its response variance represented; |z| ≥ 3 in 1,495 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +7.2 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.9 | +1.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +6.6 | +8.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.4 | +6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.1 | +7.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.9 | +5.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.7 | +4.0 |
| fall | [[NG25 (drug)]] 5 µM |  | -5.8 | -5.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -5.8 | -5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.2 | -6.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.6 | -2.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.6 | -4.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.5 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 3 open reading frame 52 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.2 — chr3:112,086,335-112,131,004 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23186, TTMP |
| Gene groups (HGNC) | MicroRNA protein coding host genes; SEA domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5BVD1](https://www.uniprot.org/uniprotkb/Q5BVD1) (TPA-induced transmembrane protein):

> Has a role in LIPH-mediated synthesis of 2-acyl lysophosphatidic acid (LPA). LPA is a bioactive lipid mediator involved in different biological processes, and necessary to promote hair formation and growth.

**Summary**, from NCBI Gene [79669](https://www.ncbi.nlm.nih.gov/gene/79669):

> Located in plasma membrane. Implicated in hypotrichosis 15. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26255](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26255) · Entrez [79669](https://www.ncbi.nlm.nih.gov/gene/79669) · UniProt [Q5BVD1](https://www.uniprot.org/uniprotkb/Q5BVD1) · Ensembl [ENSG00000114529](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114529)

## Data

Gene col 3562: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3562); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3562, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3562]; `tensor/DDL_lfc|DDL_z.npy` [3562]; `embed/gene_vectors.npy` [3562]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3562 or target_col == 3562). Every well: [[C3orf52 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C3orf52.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
