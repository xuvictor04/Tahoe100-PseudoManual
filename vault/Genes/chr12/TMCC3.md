---
symbol: "TMCC3"
type: "gene"
col: 651
ensembl_id: "ENSG00000057704"
name: "transmembrane and coiled-coil domain family 3"
location: "12q22"
module: 34
arm: "+"
pooled_cpm: 29.94
n_lines_expressing: 31
n_dd_up: 15
n_dd_down: 36
n_dd_up_clean: 13
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 24
direction_downstream: 35
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# TMCC3

*transmembrane and coiled-coil domain family 3* — 12q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.89× (z +12.1, q 4e-31, up in 16 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.572× (z -10.7, q 5e-24, down in 22 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA7A]] (+0.74, fdr 7e-06), [[PLAUR]] (+0.68, fdr 7e-06), [[PPARD]] (+0.68, fdr 7e-06); moves opposite to [[TNS3]] (-0.51, fdr 3e-05), [[SLC39A8]] (-0.51, fdr 3e-05), [[MGST1]] (-0.49, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[NLRP1]] → it (grade B ⚠); 35 go from it, the strongest it → [[ZNF185]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 651.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.89×** | +12.1 | 4e-31 | 16/29 (BT-474, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.87×** | +8.4 | 9e-15 | 12/29 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +7.0 | 4e-10 | 10/28 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.67×** | +6.9 | 6e-10 | 10/28 (BT-474, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +6.0 | 3e-07 | 7/28 (A498, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.36×** | +5.8 | 4e-07 | 11/30 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.54×** | +5.8 | 4e-07 | 14/28 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +5.0 | 4e-05 | 9/28 (BT-474, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.44×** | +4.9 | 7e-05 | 16/28 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.007 | 14/28 (LOX-IMVI, HOP62, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.012 | 13/28 (LOX-IMVI, H4, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.014 | 11/28 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.031 | 8/27 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.062 | 6/28 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.071 | 7/28 (AsPC-1, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 651.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.572×** | -10.7 | 5e-24 | 22/29 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.556×** | -8.0 | 5e-13 | 20/28 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -7.9 | 5e-13 | 20/30 (CFPAC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.550×** | -7.8 | 1e-12 | 23/28 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.635×** | -6.2 | 8e-08 | 20/28 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.639×** | -5.8 | 5e-07 | 17/25 (RPMI-7951, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -5.7 | 1e-06 | 7/30 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.657×** | -5.5 | 3e-06 | 17/28 (CFPAC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~23% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.758×** | -5.3 | 6e-06 | 14/29 (CFPAC-1, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.485×** | -5.1 | 2e-05 | 15/29 (CFPAC-1, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.774×** | -4.9 | 4e-05 | 13/28 (HOP62, H4, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.686×** | -4.9 | 4e-05 | 21/29 (SNU-423, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.713×** | -4.6 | 2e-04 | 15/28 (HOP62, H4, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.716×** | -4.5 | 2e-04 | 12/28 (H4, HOP62, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.727×** | -4.3 | 5e-04 | 13/28 (HOP62, H4, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.737×** | -4.1 | 0.001 | 13/29 (HOP62, NCI-H2347, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.744×** | -4.0 | 0.002 | 18/28 (H4, LoVo, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.740×** | -3.9 | 0.002 | 12/29 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 651. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 47.5 | 1 | 27 (6 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.89× (z +8.7) | [[Adagrasib (drug)]] 0.05 µM 0.393× (z -21.0) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.242× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 175 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0674× (z -29.3) |
| [[NCI-H1792 (line)]] | alt | 138 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0622× (z -23.0) |
| [[LOX-IMVI (line)]] | wt | 81.1 | 2 | 5 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 4.00× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -19.0) |
| [[SNU-423 (line)]] | alt | 60.7 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -16.9) |
| [[AsPC-1 (line)]] | alt | 228 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -21.5) |
| [[Panc 03.27 (line)]] | alt | 63.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -21.6) |
| [[SW 900 (line)]] | alt | 90.3 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0812× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -14.2) |
| [[LoVo (line)]] | wt | 93.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -15.6) |
| [[H4 (line)]] | wt | 25.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 31.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0827× (z -18.4) |
| [[RPMI-7951 (line)]] | alt | 20.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0804× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.245× (z -10.0) |
| [[A498 (line)]] | wt | 7.53 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.98× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -10.8) |
| [[A549 (line)]] | wt | 8.47 | 0 | 2 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0419× (z -13.5) |
| [[BT-474 (line)]] | alt | 8.38 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 5.45× (z +9.7) | [[Roxadustat (drug)]] 0.05 µM 0.0976× (z -8.7) |
| [[LS 180 (line)]] | wt | 10.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0568× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.237× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 16.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -15.5) |
| [[HEC-1-A (line)]] | alt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -9.7) |
| [[HT-29 (line)]] | alt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -9.5) |
| [[KATO III (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.46 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.31 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.73 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.99 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.72 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.32 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.46 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.70 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 651), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA7A]] | +0.74 | +0.66 / +0.72 | both halves | 7e-06 | same gene group |
| [[PLAUR]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[PPARD]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[PRSS3]] | +0.68 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[PLEK2]] | +0.66 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[RAC2]] | +0.66 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[WNT7B]] | +0.65 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[MAST4]] | +0.64 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[SHANK1]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ADAM8]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ZNF185]] | +0.60 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PDE2A]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNS3]] | -0.51 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[SLC39A8]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[MGST1]] | -0.49 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[NUDT13]] | -0.49 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[USP24]] | -0.49 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[TBC1D5]] | -0.49 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[FOXG1]] | -0.48 | -0.48 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 20, C 4. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NLRP1]] | B | NLRP1 activity raises TMCC3's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 3.33× lower at baseline in the lines without NLRP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12 |
| [[PTPRE]] | B | PTPRE activity raises TMCC3's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 2.80× lower at baseline in the lines without PTPRE | 0.008 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[PLEK2]] | B | PLEK2 activity raises TMCC3's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 3.11× lower at baseline in the lines without PLEK2 | 0.008 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[IRF6]] | B | IRF6 activity raises TMCC3's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 2.03× lower at baseline in the lines without IRF6 | 0.013 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[PRSS3]] | B | PRSS3 activity raises TMCC3's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 1.96× lower at baseline in the lines without PRSS3 | 0.021 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[LAMB3]] | B | LAMB3 activity raises TMCC3's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 2.39× lower at baseline in the lines without LAMB3 | 0.031 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[WNT7B]] | B | WNT7B activity raises TMCC3's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 2.27× lower at baseline in the lines without WNT7B | 0.042 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[RFX8]] | B | RFX8 activity raises TMCC3's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 3.05× lower at baseline in the lines without RFX8 | 0.047 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[RAC2]] | B | RAC2 activity raises TMCC3's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 2.84× lower at baseline in the lines without RAC2 | 0.051 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[CREG2]] | B | CREG2 activity raises TMCC3's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 2.23× lower at baseline in the lines without CREG2 | 0.052 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[CARD11]] | B | CARD11 activity raises TMCC3's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.39× lower at baseline in the lines without CARD11 | 0.055 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[TNFRSF11A]] | B | TNFRSF11A activity raises TMCC3's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 3.45× lower at baseline in the lines without TNFRSF11A | 0.058 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 31, C 4. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF185]] | B | TMCC3 activity raises ZNF185's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 3.68× lower at baseline in the lines without TMCC3 | 0.001 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[PTPRE]] | B | TMCC3 activity raises PTPRE's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 2.76× lower at baseline in the lines without TMCC3 | 0.003 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[FA2H]] | B | TMCC3 activity raises FA2H's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 3.90× lower at baseline in the lines without TMCC3 | 0.003 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[PRSS3]] | B | TMCC3 activity raises PRSS3's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 2.58× lower at baseline in the lines without TMCC3 | 0.004 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[PLEK2]] | B | TMCC3 activity raises PLEK2's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 2.90× lower at baseline in the lines without TMCC3 | 0.006 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[IRF6]] | B | TMCC3 activity raises IRF6's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 2.92× lower at baseline in the lines without TMCC3 | 0.010 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[RAC2]] | B | TMCC3 activity raises RAC2's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 2.91× lower at baseline in the lines without TMCC3 | 0.010 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[PLEKHM1P1]] | B | TMCC3 activity raises PLEKHM1P1's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 1.36× lower at baseline in the lines without TMCC3 | 0.011 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[WNT7B]] | B | TMCC3 activity raises WNT7B's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 2.73× lower at baseline in the lines without TMCC3 | 0.013 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[CREG2]] | B | TMCC3 activity raises CREG2's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 2.31× lower at baseline in the lines without TMCC3 | 0.014 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[DCLK2]] | B | TMCC3 activity lowers DCLK2's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 1.91× higher at baseline in the lines without TMCC3 | 0.016 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[F11R]] | B | TMCC3 activity raises F11R's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 2.42× lower at baseline in the lines without TMCC3 | 0.023 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.5, 0.8); signed map (0.2, 45.9). **Vector** length 109, 30.9% of its response variance represented; |z| ≥ 3 in 1,101 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +12.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +8.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.1 | +6.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +7.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +5.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.6 | +2.5 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.1 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.0 | -4.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.9 | -4.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.9 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane and coiled-coil domain family 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q22 — chr12:94,567,122-94,650,557 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1145 |
| Gene groups (HGNC) | Transmembrane and coiled-coil domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q9ULS5](https://www.uniprot.org/uniprotkb/Q9ULS5) carries no function annotation.

**Summary**, from NCBI Gene [57458](https://www.ncbi.nlm.nih.gov/gene/57458):

> Enables 14-3-3 protein binding activity and identical protein binding activity. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29199](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29199) · Entrez [57458](https://www.ncbi.nlm.nih.gov/gene/57458) · UniProt [Q9ULS5](https://www.uniprot.org/uniprotkb/Q9ULS5) · Ensembl [ENSG00000057704](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000057704)

## Data

Gene col 651: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 651); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 651, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 651]; `tensor/DDL_lfc|DDL_z.npy` [651]; `embed/gene_vectors.npy` [651]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 651 or target_col == 651). Every well: [[TMCC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMCC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
