---
symbol: "RRP8"
type: "gene"
col: 5291
ensembl_id: "ENSG00000132275"
name: "ribosomal RNA processing 8"
location: "11p15.4"
module: 11
arm: "+"
pooled_cpm: 15.27
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 2
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# RRP8

*ribosomal RNA processing 8* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.01× (z +28.3, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.779× (z -4.5, q 0.003, down in 13 of 47 measured lines) ⚠ unreliable plate only; position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (BT-474 0.132×, HEC-1-A 0.217×, SNU-423 0.217×, RPMI-7951 0.194×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0978×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (BT-474 0.111×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change); [[Bergenin (drug)]] 0.5 µM in 1 line (HCT15 0.0871×); [[GSK1059615 (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0689×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SW 900 0.108×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAIF1]] (+0.74, fdr 7e-06), [[ZNF689]] (+0.74, fdr 1e-05), [[ARL14EP]] (+0.68, fdr 1e-05); moves opposite to [[HDAC1]] (-0.65, fdr 1e-05), [[ILRUN]] (-0.61, fdr 3e-05), [[SGSM1]] (-0.60, fdr 5e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5291.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.01×** | +28.3 | 0e+00 | 45/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.31×** | +21.8 | 0e+00 | 43/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +21.1 | 0e+00 | 43/45 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.32×** | +14.7 | 0e+00 | 44/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +9.7 | 5e-20 | 31/42 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.70×** | +9.6 | 6e-20 | 31/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.59×** | +8.5 | 2e-15 | 28/48 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +7.4 | 1e-11 | 25/48 (A-427, NCI-H460, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.0 | 1e-10 | 24/46 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +5.9 | 2e-07 | 17/47 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.35×** | +5.5 | 2e-06 | 17/46 (HCT15, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +5.2 | 9e-06 | 17/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +5.0 | 2e-05 | 18/47 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +5.0 | 3e-05 | 18/47 (SW480, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +5.0 | 3e-05 | 17/46 (H4, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +4.7 | 8e-05 | 14/48 (PANC-1, HOP62, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.61×** | +4.6 | 2e-04 | 6/46 (A498, HCT15, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.58×** | +4.4 | 3e-04 | 14/48 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5291.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (BT-474 0.132×, HEC-1-A 0.217×, SNU-423 0.217×, RPMI-7951 0.194×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0978×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (BT-474 0.111×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change); [[Bergenin (drug)]] 0.5 µM in 1 line (HCT15 0.0871×); [[GSK1059615 (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0689×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SW 900 0.108×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.779×** | -4.5 | 0.003 | 13/47 (A-172, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.799×** | -3.9 | 0.024 | 13/27 (BT-474, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.827× | -3.5 | 0.10 | 15/46 (SW480, Panc 03.27, …) | two highest doses |  |
| [[Olanzapine (drug)]] 5 µM |  | 0.879× | -3.3 | 0.13 | 8/48 (PANC-1, J82, …) | top dose only | position effect removed |
| [[Hexylresorcinol (drug)]] 0.5 µM |  | 0.838× | -3.2 | 0.16 | 6/48 (SHP-77, NCI-H2347, …) | inconsistent across doses |  |
| [[Naproxen (drug)]] 0.05 µM |  | 0.831× | -3.1 | 0.17 | 13/45 (A-427, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5291. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 21.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +17.5) | — |
| [[RPMI-7951 (line)]] | alt | 16.4 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0978× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[GSK1059615 (drug)]] 0.5 µM 0.0689× (z -10.4) |
| [[SW480 (line)]] | alt | 25.8 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.25× (z +12.2) | — |
| [[A498 (line)]] | wt | 22.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 11.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +26.0) | — |
| [[SNU-423 (line)]] | alt | 15.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -9.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 16.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 20.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[HEC-1-A (line)]] | alt | 14.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -10.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 12.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 15.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +12.1) | — |
| [[J82 (line)]] | alt | 21.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +11.8) | — |
| [[LoVo (line)]] | wt | 15.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +12.8) | — |
| [[LS 180 (line)]] | wt | 13.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +12.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 6.56 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.53× (z +14.4) | — |
| [[COLO 205 (line)]] | alt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +10.0) | — |
| [[HCT15 (line)]] | alt | 16.9 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0871× (z -11.6) |
| [[Hs 766T (line)]] | wt | 18.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +13.0) | — |
| [[HS-578T (line)]] | alt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 12.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 17.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 8.96 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.154× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 6.87 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.108× (z -8.7) |
| [[SW1417 (line)]] | alt | 26.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.0) | — |
| [[SW48 (line)]] | wt | 14.0 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.102× (z -8.6) |
| [[A-172 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5291), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAIF1]] | +0.74 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[ZNF689]] | +0.74 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[ARL14EP]] | +0.68 | +0.75 / +0.50 | both halves | 1e-05 |  |
| [[PBDC1]] | +0.68 | +0.74 / +0.44 | both halves | 3e-05 |  |
| [[ZNF181]] | +0.67 | +0.77 / +0.30 | both halves | 2e-04 |  |
| [[C1orf131]] | +0.66 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[GORASP1]] | +0.66 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[THAP2]] | +0.66 | +0.72 / +0.32 | both halves | 2e-04 |  |
| [[ZNF764]] | +0.66 | +0.76 / +0.33 | both halves | 1e-04 |  |
| [[C8orf33]] | +0.65 | +0.70 / +0.42 | both halves | 4e-05 | STRING 419 |
| [[ZCCHC3]] | +0.65 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[BTN2A1]] | +0.65 | +0.58 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC1]] | -0.65 | -0.58 / -0.49 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |
| [[ILRUN]] | -0.61 | -0.78 / -0.45 | both halves | 3e-05 |  |
| [[SGSM1]] | -0.60 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[AIF1L]] | -0.58 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[GNB5]] | -0.57 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[STRN]] | -0.56 | -0.69 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[HPSE]] | -0.56 | -0.43 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RRP8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.691). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.2, 6.3); signed map (14.1, -21.6). **Vector** length 62.8, 9.86% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +21.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +21.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +28.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.6 | +14.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.1 | +9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +5.2 |
|  | [[EX229 (drug)]] 5 µM |  | +1.4 | +3.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.4 | +3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +1.4 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.5 | +3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~96% of this change | -4.3 | +3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -3.7 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.1 | -0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | +2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | +0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | +0.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal RNA processing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:6,595,072-6,603,616 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NML; previously KIAA0409 |
| Gene groups (HGNC) | eNoSC complex; Ribosome biogenesis factors; 7BS N1-adenosine RNA methyltransferases; DNA/RNA methyltransferases |
| Hallmark sets | P53_PATHWAY |
| Reactome | 3 pathways, smallest: SIRT1 negatively regulates rRNA expression; Negative epigenetic regulation of rRNA expression; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [O43159](https://www.uniprot.org/uniprotkb/O43159) (Ribosomal RNA-processing protein 8):

> Essential component of the eNoSC (energy-dependent nucleolar silencing) complex, a complex that mediates silencing of rDNA in response to intracellular energy status and acts by recruiting histone-modifying enzymes. The eNoSC complex is able to sense the energy status of cell: upon glucose starvation, elevation of NAD(+)/NADP(+) ratio activates SIRT1, leading to histone H3 deacetylation followed by dimethylation of H3 at 'Lys-9' (H3K9me2) by SUV39H1 and the formation of silent chromatin in the …

**Summary**, from NCBI Gene [23378](https://www.ncbi.nlm.nih.gov/gene/23378):

> Enables RNA binding activity. Involved in several processes, including cellular response to glucose starvation; intrinsic apoptotic signaling pathway by p53 class mediator; and regulation of gene expression. Acts upstream of with a negative effect on regulation of G1 to G0 transition. Located in cytosol; nuclear lumen; and rDNA heterochromatin. Part of chromatin silencing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29030](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29030) · Entrez [23378](https://www.ncbi.nlm.nih.gov/gene/23378) · UniProt [O43159](https://www.uniprot.org/uniprotkb/O43159) · Ensembl [ENSG00000132275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132275)

## Data

Gene col 5291: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5291); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5291, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5291]; `tensor/DDL_lfc|DDL_z.npy` [5291]; `embed/gene_vectors.npy` [5291]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5291 or target_col == 5291). Every well: [[RRP8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRP8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
