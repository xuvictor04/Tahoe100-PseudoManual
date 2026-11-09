---
symbol: "WDR17"
type: "gene"
col: 7447
ensembl_id: "ENSG00000150627"
name: "WD repeat domain 17"
location: "4q34.2"
module: 82
arm: "+"
pooled_cpm: 9.55
n_lines_expressing: 34
n_dd_up: 47
n_dd_down: 8
n_dd_up_clean: 36
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# WDR17

*WD repeat domain 17* — 4q34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 15.1× (z +36.0, q 0e+00, up in 30 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.775× (z -4.8, q 9e-04, down in 9 of 30 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A12]] (+0.61, fdr 1e-05), [[FRRS1]] (+0.59, fdr 2e-04), [[LRCH2]] (+0.59, fdr 1e-05); moves opposite to [[TRPV1]] (-0.55, fdr 3e-04), [[ERVK13-1]] (-0.52, fdr 8e-04, ⚠ one half only (not replicated)), [[LRP2BP-AS1]] (-0.52, fdr 3e-05), [[EOLA2-DT]] (-0.52, fdr 1e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CCDC85A]] → it (grade B ⚠); 6 go from it, the strongest it → [[SMIM10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7447.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **15.1×** | +36.0 | 0e+00 | 30/30 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **13.8×** | +34.8 | 0e+00 | 30/30 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **10.9×** | +31.6 | 0e+00 | 30/30 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **5.11×** | +30.6 | 0e+00 | 30/30 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **5.96×** | +23.6 | 0e+00 | 30/30 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.98×** | +18.3 | 0e+00 | 29/30 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.69×** | +13.1 | 4e-37 | 26/30 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **8.24×** | +12.6 | 2e-34 | 29/30 (A498, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +12.5 | 3e-34 | 21/30 (A-427, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.96×** | +8.6 | 7e-16 | 17/30 (NCI-H2347, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.88×** | +8.0 | 5e-14 | 14/25 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.49×** | +7.5 | 3e-12 | 14/29 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.74×** | +7.3 | 1e-11 | 19/31 (NCI-H2030, J82, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.64×** | +6.5 | 3e-09 | 18/30 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.41×** | +6.4 | 5e-09 | 15/30 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +5.7 | 3e-07 | 15/30 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.78×** | +5.4 | 2e-06 | 13/30 (J82, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.50×** | +5.3 | 3e-06 | 11/30 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.50×** | +5.3 | 3e-06 | 12/30 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7447.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.775×** | -4.8 | 9e-04 | 9/30 (NCI-H1792, NCI-H2030, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.734×** | -4.1 | 0.011 | 11/30 (SW 900, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -3.7 | 0.029 | 6/31 (A549, NCI-H23, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.748×** | -3.7 | 0.029 | 10/30 (A-427, NCI-H1792, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.771×** | -3.5 | 0.053 | 8/30 (SW 900, C32, …) | rises with dose | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.774×** | -3.4 | 0.053 | 6/30 (SHP-77, SK-MEL-2, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.699×** | -3.4 | 0.053 | 11/30 (SK-MEL-2, RPMI-7951, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.570×** | -3.4 | 0.054 | 4/28 (NCI-H1792, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -3.1 | 0.11 | 4/32 (LoVo, H4, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.788× | -3.1 | 0.13 | 13/30 (HS-578T, hTERT-HPNE, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7447. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 6.44 | 8 | 0 | [[Tucidinostat (drug)]] 5 µM 12.4× (z +14.7) | — |
| [[HEC-1-A (line)]] | alt | 27.0 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 7.79× (z +14.3) | [[Bortezomib (drug)]] 5 µM 0.0252× (z -11.6) ⚠ toxic |
| [[SW480 (line)]] | alt | 4.45 | 6 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 8.77× (z +13.6) | [[Digitoxin (drug)]] 5 µM 0.0528× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 12.2 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 14.2× (z +16.6) | — |
| [[HS-578T (line)]] | alt | 9.69 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 14.0× (z +12.2) | [[Pimozide (drug)]] 0.05 µM 0.157× (z -8.6) |
| [[A-172 (line)]] | wt | 3.27 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 53.0× (z +11.7) | [[Lucanthone (drug)]] 5 µM 0.0475× (z -8.7) |
| [[A549 (line)]] | wt | 16.3 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 9.21× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 4.89 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 38.9× (z +13.7) | — |
| [[J82 (line)]] | alt | 9.30 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 16.3× (z +12.5) | — |
| [[LoVo (line)]] | wt | 3.11 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 11.1× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 24.2 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.54× (z +12.0) | — |
| [[NCI-H460 (line)]] | wt | 10.3 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 19.3× (z +15.6) | — |
| [[PANC-1 (line)]] | alt | 4.99 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 24.7× (z +15.2) | — |
| [[CFPAC-1 (line)]] | alt | 7.25 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 22.3× (z +13.4) | — |
| [[NCI-H2030 (line)]] | alt | 25.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.94× (z +11.5) | — |
| [[A-427 (line)]] | wt | 43.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +14.6) | — |
| [[H4 (line)]] | wt | 14.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 13.6× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 11.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 13.9× (z +12.3) | — |
| [[NCI-H1792 (line)]] | alt | 12.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 16.1× (z +12.5) | — |
| [[NCI-H23 (line)]] | alt | 23.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.65× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 4.18 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 22.7× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 54.1 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.88× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[SK-MEL-2 (line)]] | alt | 9.18 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 5.27× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 7.21 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 18.6× (z +10.1) | — |
| [[C-33 A (line)]] | alt | 17.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.09× (z +9.3) | — |
| [[C32 (line)]] | wt | 5.22 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 20.5× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 4.47 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 30.7× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 9.11× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 23.2 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0541× (z -9.3) |
| [[AN3 CA (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.908 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.789 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.987 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.771 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.839 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.995 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.997 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7447), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A12]] | +0.61 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[FRRS1]] | +0.59 | +0.31 / +0.63 | both halves | 2e-04 |  |
| [[LRCH2]] | +0.59 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[BCHE]] | +0.58 | +0.36 / +0.61 | both halves | 1e-04 |  |
| [[ELOVL4]] | +0.58 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[PDGFD]] | +0.57 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[SOGA3]] | +0.56 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[TMEM108]] | +0.56 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[PTPN13]] | +0.56 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[GPM6A]] | +0.56 | +0.60 / +0.65 | both halves | 7e-06 | STRING 442 |
| [[PRKAR2B]] | +0.55 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ASXL3]] | +0.55 | +0.40 / +0.57 | both halves | 5e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRPV1]] | -0.55 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[ERVK13-1]] | -0.52 | -0.19 / -0.51 | ⚠ one half (not replicated) | 8e-04 |  |
| [[LRP2BP-AS1]] | -0.52 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[EOLA2-DT]] | -0.52 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[PIPOX]] | -0.51 | -0.20 / -0.54 | ⚠ one half (not replicated) | 8e-04 |  |
| [[PDK1-AS1]] | -0.49 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[UBAP1L]] | -0.49 | -0.11 / -0.47 | ⚠ not reproduced | 0.002 |  |
| [[MUC20-OT1]] | -0.49 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[DNHD1]] | -0.49 | -0.18 / -0.41 | ⚠ not reproduced | 9e-04 |  |
| [[LINC02798]] | -0.49 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[QRICH2]] | -0.48 | -0.11 / -0.50 | ⚠ not reproduced | 0.002 |  |
| [[FAM120B]] | -0.48 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[MEF2B]] | -0.48 | -0.21 / -0.40 | both halves | 7e-04 |  |
| [[TMEM11-DT]] | -0.47 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[LINC02936]] | -0.47 | -0.26 / -0.39 | both halves | 4e-04 |  |
| [[NPHP3-ACAD11]] | -0.47 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[NPLOC4]] | -0.46 | -0.29 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC85A]] | B | CCDC85A activity raises WDR17's level | lines that do not express CCDC85A (19) vs lines expressing it (31) | 2.41× lower at baseline in the lines without CCDC85A | 0.062 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, SERPINB7, KRT86; maybe low, not absent |
| [[VWDE]] | B | VWDE activity raises WDR17's level | lines that do not express VWDE (22) vs lines expressing it (28) | 2.48× lower at baseline in the lines without VWDE | 0.068 | ⚠ within organs, on part of the lines; also absent: RBM11, L3MBTL4, RPS6KA6 |
| [[SOGA3]] | C | SOGA3 activity raises WDR17's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 3.31× lower at baseline in the lines without SOGA3 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1; co-absent with the target |
| [[SFMBT2]] | C | SFMBT2 activity raises WDR17's level | lines that do not express SFMBT2 (19) vs lines expressing it (31) | 3.73× lower at baseline in the lines without SFMBT2 | 0.058 | ⚠ within organs, on part of the lines; also absent: ANKRD6, LONRF2, GHR; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMIM10]] | B | WDR17 activity raises SMIM10's level | lines that do not express WDR17 (16) vs lines expressing it (34) | 2.09× lower at baseline in the lines without WDR17 | 0.059 | ⚠ within organs, on part of the lines; also absent: WIPF1, AFAP1L1, SGCE |
| [[STK33]] | B | WDR17 activity raises STK33's level | lines that do not express WDR17 (16) vs lines expressing it (34) | 1.91× lower at baseline in the lines without WDR17 | 0.061 | ⚠ within organs, on part of the lines; also absent: WIPF1, AFAP1L1, SGCE |
| [[ERVK13-1]] | B | WDR17 activity lowers ERVK13-1's level | lines that do not express WDR17 (16) vs lines expressing it (34) | 1.33× higher at baseline in the lines without WDR17 | 0.091 | ⚠ within organs, on part of the lines; also absent: WIPF1, AFAP1L1, SGCE |
| [[MAP9]] | C | WDR17 activity raises MAP9's level | lines that do not express WDR17 (16) vs lines expressing it (34) | 7.61× lower at baseline in the lines without WDR17 | 0.016 | ⚠ within organs, on part of the lines; also absent: WIPF1, AFAP1L1, SGCE; co-absent with the target |
| [[SOGA3]] | C | WDR17 activity raises SOGA3's level | lines that do not express WDR17 (16) vs lines expressing it (34) | 4.76× lower at baseline in the lines without WDR17 | 0.075 | ⚠ within organs, on part of the lines; also absent: WIPF1, AFAP1L1, SGCE; co-absent with the target |
| [[ZNF385B]] | C | WDR17 activity raises ZNF385B's level | lines that do not express WDR17 (16) vs lines expressing it (34) | 1.99× lower at baseline in the lines without WDR17 | 0.091 | ⚠ within organs, on part of the lines; also absent: WIPF1, AFAP1L1, SGCE; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.407). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.3, 30.3); signed map (34.6, 32.1). **Vector** length 71.0, 16.3% of its response variance represented; |z| ≥ 3 in 839 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.4 | +30.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.9 | +18.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | +4.8 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +4.6 | +5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +23.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +7.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +12.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +5.2 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -3.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.2 | -4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.0 | -3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -3.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q34.2 — chr4:176,065,841-176,182,818 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q8IZU2](https://www.uniprot.org/uniprotkb/Q8IZU2) carries no function annotation.

**Summary**, from NCBI Gene [116966](https://www.ncbi.nlm.nih.gov/gene/116966):

> This gene encodes a WD repeat-containing protein. It is abundantly expressed in retina and testis, and is thought to be a candidate gene for retinal disease. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:16661](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16661) · Entrez [116966](https://www.ncbi.nlm.nih.gov/gene/116966) · UniProt [Q8IZU2](https://www.uniprot.org/uniprotkb/Q8IZU2) · Ensembl [ENSG00000150627](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150627)

## Data

Gene col 7447: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7447); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7447, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7447]; `tensor/DDL_lfc|DDL_z.npy` [7447]; `embed/gene_vectors.npy` [7447]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7447 or target_col == 7447). Every well: [[WDR17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
