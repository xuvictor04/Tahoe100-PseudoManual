---
symbol: "PTX3"
type: "gene"
col: 8748
ensembl_id: "ENSG00000163661"
name: "pentraxin 3"
location: "3q25.32"
module: 14
arm: "+"
pooled_cpm: 16.56
n_lines_expressing: 26
n_dd_up: 38
n_dd_down: 3
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 15
direction_downstream: 6
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# PTX3

*pentraxin 3* — 3q25.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.63× (z +25.6, q 0e+00, up in 23 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.568× (z -4.4, q 0.006, down in 10 of 24 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 0.632× (z -3.7, q 0.043, down in 10 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 5 µM in 1 line (J82 0.211×); [[Selinexor (drug)]] 5 µM in 1 line (J82 0.350×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (H4 0.122×; ⚠ cell-cycle shift, explains ~79% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRGN]] (+0.77, fdr 7e-06), [[SLC1A3]] (+0.65, fdr 7e-06), [[CSF1]] (+0.64, fdr 7e-06); moves opposite to [[SIRLNT]] (-0.51, fdr 3e-05), [[ARHGEF6]] (-0.50, fdr 5e-05), [[TANGO2]] (-0.50, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[ARHGAP40]] → it (grade B ⚠); 6 go from it, the strongest it → [[MT1E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8748.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.63×** | +25.6 | 0e+00 | 23/23 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **8.63×** | +17.4 | 0e+00 | 24/24 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **5.28×** | +14.0 | 4e-42 | 23/23 (A-172, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.26×** | +13.9 | 5e-42 | 22/23 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +12.0 | 4e-31 | 13/21 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **15.3×** | +12.0 | 4e-31 | 24/24 (Panc 03.27, CFPAC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.66×** | +11.6 | 4e-29 | 23/24 (hTERT-HPNE, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **3.91×** | +11.5 | 2e-28 | 22/24 (A-172, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.21×** | +9.8 | 9e-21 | 19/24 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **3.25×** | +9.2 | 3e-18 | 12/18 (SNU-423, SW 900, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **2.84×** | +8.7 | 1e-16 | 11/18 (NCI-H1792, J82, …) | all doses, flat | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.45×** | +7.5 | 3e-12 | 18/23 (J82, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.36×** | +7.2 | 3e-11 | 21/23 (A-172, SW 900, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.43×** | +7.2 | 4e-11 | 16/22 (J82, SNU-423, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **2.33×** | +6.8 | 3e-10 | 19/21 (NCI-H1792, SW 900, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.25×** | +6.5 | 2e-09 | 12/24 (A-172, HS-578T, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.89×** | +5.3 | 3e-06 | 10/24 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.00×** | +4.8 | 4e-05 | 13/24 (Panc 03.27, HOP62, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.49×** | +4.7 | 6e-05 | 12/24 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.76×** | +4.5 | 1e-04 | 15/24 (SNU-423, NCI-H1792, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.4 | 2e-04 | 11/24 (HOP62, A-172, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.66×** | +4.2 | 5e-04 | 10/22 (HS-578T, J82, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8748.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 5 µM in 1 line (J82 0.211×); [[Selinexor (drug)]] 5 µM in 1 line (J82 0.350×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (H4 0.122×; ⚠ cell-cycle shift, explains ~79% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.568×** | -4.4 | 0.006 | 10/24 (A498, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.632×** | -3.7 | 0.043 | 10/22 (J82, Panc 03.27, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.631×** | -3.7 | 0.043 | 12/24 (H4, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.697× | -3.1 | 0.22 | 10/24 (J82, SW 1088, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.501× | -3.1 | 0.22 | 11/23 (A-172, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.746× | -3.0 | 0.22 | 6/24 (A498, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.68 per unit of S-phase module lfc, +0.62 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8748. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 67.1 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +21.7) | — |
| [[hTERT-HPNE (line)]] | wt | 84.7 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.7× (z +22.0) | — |
| [[HOP62 (line)]] | alt | 19.9 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 35.4× (z +24.5) | — |
| [[SNU-423 (line)]] | alt | 49.1 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.5× (z +21.5) | — |
| [[HS-578T (line)]] | alt | 39.7 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +16.8) | — |
| [[J82 (line)]] | alt | 131 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +22.9) | [[Cobimetinib (drug)]] 5 µM 0.211× (z -10.0) |
| [[A498 (line)]] | wt | 44.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +20.6) | — |
| [[CFPAC-1 (line)]] | alt | 22.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.8× (z +24.9) | — |
| [[NCI-H1792 (line)]] | alt | 17.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.72× (z +13.3) | — |
| [[Panc 03.27 (line)]] | alt | 28.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.0× (z +22.1) | — |
| [[PANC-1 (line)]] | alt | 6.29 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.3× (z +20.6) | — |
| [[SW 900 (line)]] | alt | 48.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.78× (z +12.0) | — |
| [[H4 (line)]] | wt | 62.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +11.6) | [[Bortezomib (drug)]] 0.05 µM 0.122× (z -9.8) ⚠ cell-cycle shift, explains ~79% of this change |
| [[NCI-H460 (line)]] | wt | 8.51 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 10.9× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 19.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +12.4) | — |
| [[CHP-212 (line)]] | wt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.26× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.39× (z +11.1) | — |
| [[NCI-H23 (line)]] | alt | 8.87 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.63× (z +9.0) | — |
| [[A-427 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.17 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8748), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGN]] | +0.77 | +0.70 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[SLC1A3]] | +0.65 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[CSF1]] | +0.64 | +0.63 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CSF3]] | +0.63 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[EBI3]] | +0.62 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[FOXC2]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[TNFAIP3]] | +0.61 | +0.53 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[ANKRD33B]] | +0.60 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[CCBE1]] | +0.58 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[BIRC3]] | +0.57 | +0.55 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ADAMTS9]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[CCL20]] | +0.56 | +0.48 / +0.63 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRLNT]] | -0.51 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[ARHGEF6]] | -0.50 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[TANGO2]] | -0.50 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[VSTM4]] | -0.49 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[LINC01705]] | -0.48 | -0.55 / -0.37 | both halves | 7e-05 |  |
| [[TMOD1]] | -0.48 | -0.63 / -0.32 | both halves | 2e-04 |  |
| [[FAM219A]] | -0.48 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[GCKR]] | -0.47 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[PCYT1A]] | -0.47 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ANXA10]] | -0.46 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[SNX21]] | -0.45 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[C9orf24]] | -0.45 | -0.48 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 6, C 9. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP40]] | B | ARHGAP40 activity raises PTX3's level | lines that do not express ARHGAP40 (16) vs lines expressing it (34) | 2.51× lower at baseline in the lines without ARHGAP40 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000282943, ENSG00000225096, ENSG00000239462; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PTX3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FJX1]] | B | FJX1 activity raises PTX3's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 4.63× lower at baseline in the lines without FJX1 | 0.057 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[NKX3-1]] | B | NKX3-1 activity raises PTX3's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 4.10× lower at baseline in the lines without NKX3-1 | 0.075 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises PTX3's level | compounds that target MAP2K1: 2 of 4 lower it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MT1E]] | B | MT1E activity raises PTX3's level | lines that do not express MT1E (22) vs lines expressing it (28) | 1.40× lower at baseline in the lines without MT1E | 0.096 | ⚠ within organs, on part of the lines; also absent: MT1M, ENSG00000291105, ACSL5 |
| [[CCBE1]] | C | CCBE1 activity raises PTX3's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 6.13× lower at baseline in the lines without CCBE1 | 0.006 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1; co-absent with the target |
| [[ANKRD33B]] | C | ANKRD33B activity raises PTX3's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 5.32× lower at baseline in the lines without ANKRD33B | 0.007 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22; co-absent with the target |
| [[FOXC2]] | C | FOXC2 activity raises PTX3's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 3.83× lower at baseline in the lines without FOXC2 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT; co-absent with the target |
| [[TNFAIP6]] | C | TNFAIP6 activity raises PTX3's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 5.75× lower at baseline in the lines without TNFAIP6 | 0.039 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises PTX3's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 6.36× lower at baseline in the lines without LINC01411 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[CXCL5]] | C | CXCL5 activity raises PTX3's level | lines that do not express CXCL5 (35) vs lines expressing it (15) | 2.52× lower at baseline in the lines without CXCL5 | 0.046 | ⚠ within organs, on part of the lines; also absent: ANXA10, IRAK3, TRBC2; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MT1E]] | B | PTX3 activity raises MT1E's level | lines that do not express PTX3 (24) vs lines expressing it (26) | 1.91× lower at baseline in the lines without PTX3 | 0.080 | ⚠ within organs, on part of the lines; also absent: IL7R, RNF182, COL5A1 |
| [[SLC1A3]] | B | PTX3 activity raises SLC1A3's level | lines that do not express PTX3 (24) vs lines expressing it (26) | 2.26× lower at baseline in the lines without PTX3 | 0.081 | ⚠ within organs, on part of the lines; also absent: IL7R, RNF182, COL5A1 |
| [[PCYT1A]] | B | PTX3 activity raises PCYT1A's level | lines that do not express PTX3 (24) vs lines expressing it (26) | 1.35× lower at baseline in the lines without PTX3 | 0.083 | ⚠ within organs, on part of the lines; also absent: IL7R, RNF182, COL5A1 |
| [[ARHGEF6]] | C | PTX3 activity raises ARHGEF6's level | lines that do not express PTX3 (24) vs lines expressing it (26) | 3.58× lower at baseline in the lines without PTX3 | 0.015 | ⚠ within organs, on part of the lines; also absent: IL7R, RNF182, COL5A1; co-absent with the target |
| [[S1PR3]] | C | PTX3 activity raises S1PR3's level | lines that do not express PTX3 (24) vs lines expressing it (26) | 3.29× lower at baseline in the lines without PTX3 | 0.057 | ⚠ within organs, on part of the lines; also absent: IL7R, RNF182, COL5A1; co-absent with the target |
| [[PID1]] | C | PTX3 activity raises PID1's level | lines that do not express PTX3 (24) vs lines expressing it (26) | 4.64× lower at baseline in the lines without PTX3 | 0.074 | ⚠ within organs, on part of the lines; also absent: IL7R, RNF182, COL5A1; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.458). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.8, 9.9); signed map (13.5, 29.1). **Vector** length 94.3, 29.1% of its response variance represented; |z| ≥ 3 in 923 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +11.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +7.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +17.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +25.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.1 | +12.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.9 | +2.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.8 | +6.5 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +2.3 | +1.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.2 | +3.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.6 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -4.6 | -2.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | -4.5 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.1 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | pentraxin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.32 — chr3:157,436,850-157,443,633 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TSG-14; previously TNFAIP5 |
| Gene groups (HGNC) | Long pentraxins; Pattern recognition pentraxins |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P26022](https://www.uniprot.org/uniprotkb/P26022) (Pentraxin-related protein PTX3):

> Plays a role in the regulation of innate resistance to pathogens, inflammatory reactions, possibly clearance of self-components and female fertility.

**Summary**, from NCBI Gene [5806](https://www.ncbi.nlm.nih.gov/gene/5806):

> This gene encodes a member of the pentraxin protein family. The expression of this protein is induced by inflammatory cytokines in response to inflammatory stimuli in several mesenchymal and epithelial cell types, particularly endothelial cells and mononuclear phagocytes. The protein promotes fibrocyte differentiation and is involved in regulating inflammation and complement activation. It also plays a role in angiogenesis and tissue remodeling. The protein serves as a biomarker for several …

**Accessions** — [HGNC:9692](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9692) · Entrez [5806](https://www.ncbi.nlm.nih.gov/gene/5806) · UniProt [P26022](https://www.uniprot.org/uniprotkb/P26022) · Ensembl [ENSG00000163661](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163661)

## Data

Gene col 8748: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8748); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8748, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8748]; `tensor/DDL_lfc|DDL_z.npy` [8748]; `embed/gene_vectors.npy` [8748]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8748 or target_col == 8748). Every well: [[PTX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
