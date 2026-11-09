---
symbol: "CYP2E1"
type: "gene"
col: 5092
ensembl_id: "ENSG00000130649"
name: "cytochrome P450 family 2 subfamily E member 1"
location: "10q26.3"
module: 47
arm: "+"
pooled_cpm: 3.91
n_lines_expressing: 47
n_dd_up: 10
n_dd_down: 18
n_dd_up_clean: 7
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 6
direction_downstream: 4
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# CYP2E1

*cytochrome P450 family 2 subfamily E member 1* — 10q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.88× (z +13.3, q 2e-37, up in 39 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.423× (z -8.4, q 2e-14, down in 28 of 41 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCART1]] (+0.92, fdr 7e-06, ⚠ same locus), [[CPLX1]] (+0.59, fdr 1e-05), [[AHRR]] (+0.59, fdr 1e-05), [[LINC02885]] (+0.58, fdr 2e-05); moves opposite to [[SLC16A14]] (-0.58, fdr 3e-05), [[ATP6V0D1-DT]] (-0.55, fdr 8e-05), [[AKAP7]] (-0.54, fdr 3e-04).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LINC01422]] → it (grade B ⚠); 4 go from it, the strongest it → [[AHRR]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5092.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.88×** | +13.3 | 2e-37 | 39/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.77×** | +10.0 | 6e-21 | 28/41 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.00×** | +9.6 | 2e-19 | 33/42 (LS 180, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.01×** | +6.8 | 1e-09 | 20/40 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +5.6 | 3e-06 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +5.4 | 7e-06 | 11/42 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +5.1 | 3e-05 | 0/6 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +4.7 | 2e-04 | 11/38 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +4.6 | 2e-04 | 13/37 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +4.0 | 0.004 | 1/18 (SW 900) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.37× | +3.1 | 0.11 | 9/32 (AsPC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5092.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.423×** | -8.4 | 2e-14 | 28/41 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.640×** | -6.2 | 2e-07 | 22/43 (HEC-1-A, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.541×** | -5.7 | 3e-06 | 16/39 (CFPAC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.697×** | -5.0 | 9e-05 | 16/43 (SNU-1, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -4.8 | 1e-04 | 16/30 (Panc 03.27, J82, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.618×** | -4.4 | 0.001 | 13/37 (HOP62, CFPAC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.664×** | -4.0 | 0.005 | 18/42 (RPMI-7951, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.650×** | -3.8 | 0.008 | 10/41 (H4, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.682×** | -3.7 | 0.012 | 12/39 (C32, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.684×** | -3.7 | 0.012 | 16/44 (C32, AsPC-1, …) | rises with dose | composition shift |
| [[Radotinib (drug)]] 5 µM |  | **0.772×** | -3.6 | 0.019 | 13/40 (H4, HepG2/C3A, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.704×** | -3.4 | 0.029 | 17/40 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ligustrazine (drug)]] 0.5 µM |  | **0.706×** | -3.4 | 0.030 | 7/42 (NCI-H661, Hs 766T, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 5 µM |  | **0.700×** | -3.2 | 0.059 | 8/40 (hTERT-HPNE, C32, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.725×** | -3.1 | 0.061 | 7/39 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.725×** | -3.1 | 0.061 | 13/39 (HOP62, HepG2/C3A, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.725×** | -3.0 | 0.095 | 6/36 (SNU-423, KATO III, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5092. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 5.04 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0900× (z -9.1) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.232× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 7.43 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0317× (z -13.5) |
| [[J82 (line)]] | alt | 8.29 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0849× (z -9.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 5.10 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0737× (z -10.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 10.1 | 0 | 1 | — | [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.123× (z -9.0) |
| [[SNU-1 (line)]] | wt | 20.3 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.107× (z -9.6) |
| [[SW 900 (line)]] | alt | 6.20 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -8.7) |
| [[SW480 (line)]] | alt | 7.99 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.63× (z +9.7) | — |
| [[A-172 (line)]] | wt | 0.999 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5092), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCART1]] | +0.92 | +0.89 / +0.90 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[CPLX1]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[AHRR]] | +0.59 | +0.64 / +0.51 | both halves | 1e-05 | pathway: Biological oxidations |
| [[LINC02885]] | +0.58 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[MYO15A]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[UCKL1-AS1]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[GSG1L]] | +0.55 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PTCH2]] | +0.55 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[LINC01031]] | +0.54 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[GNB1L]] | +0.53 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[ACOT12]] | +0.53 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[NTRK1]] | +0.53 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[SH2D4B]] | +0.52 | +0.56 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC16A14]] | -0.58 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ATP6V0D1-DT]] | -0.55 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[AKAP7]] | -0.54 | -0.28 / -0.59 | both halves | 3e-04 |  |
| [[ZNF85]] | -0.54 | -0.27 / -0.47 | both halves | 3e-04 |  |
| [[C5orf34]] | -0.54 | -0.25 / -0.49 | both halves | 4e-04 |  |
| [[ZNF442]] | -0.53 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[ZNF700]] | -0.51 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[ZNF138]] | -0.50 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[KLHL42]] | -0.50 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[RWDD3]] | -0.50 | -0.37 / -0.45 | both halves | 9e-05 |  |
| [[ZNF433]] | -0.49 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[TSTD3]] | -0.49 | -0.23 / -0.46 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01422]] | B | LINC01422 activity raises CYP2E1's level | lines that do not express LINC01422 (6) vs lines expressing it (44) | 1.86× lower at baseline in the lines without LINC01422 | 0.040 | ⚠ within organs, on part of the lines; also absent: ESRRB, MIAT, ARHGAP15 |
| [[LINC01250]] | B | LINC01250 activity raises CYP2E1's level | lines that do not express LINC01250 (10) vs lines expressing it (40) | 1.80× lower at baseline in the lines without LINC01250 | 0.040 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CYP2E1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers CYP2E1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC02133]] | C | LINC02133 activity raises CYP2E1's level | lines that do not express LINC02133 (4) vs lines expressing it (46) | 2.36× lower at baseline in the lines without LINC02133 | 0.042 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LYG1, RBM44, TRIM72; maybe low, not absent |
| [[RBM44]] | C | RBM44 activity raises CYP2E1's level | lines that do not express RBM44 (3) vs lines expressing it (47) | 2.36× lower at baseline in the lines without RBM44 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC02133, LYG1, SYCP2L; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AHRR]] | C | CYP2E1, [[SCART1]] activity raises AHRR's level | lines that do not express CYP2E1, SCART1 (3) vs lines expressing them (47) | 3.53× lower at baseline in the lines without CYP2E1, SCART1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AHRR, ARHGAP15, FAT1; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[RBM44]] | C | CYP2E1, [[SCART1]] activity raises RBM44's level | lines that do not express CYP2E1, SCART1 (3) vs lines expressing them (47) | 2.93× lower at baseline in the lines without CYP2E1, SCART1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AHRR, ARHGAP15, FAT1; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[UCKL1-AS1]] | C | CYP2E1, [[SCART1]] activity raises UCKL1-AS1's level | lines that do not express CYP2E1, SCART1 (3) vs lines expressing them (47) | 2.13× lower at baseline in the lines without CYP2E1, SCART1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AHRR, ARHGAP15, FAT1; maybe low, not absent; its own permutation p; co-absent genes |
| [[TPCN2]] | C | CYP2E1, [[SCART1]] activity raises TPCN2's level | lines that do not express CYP2E1, SCART1 (3) vs lines expressing them (47) | 1.85× lower at baseline in the lines without CYP2E1, SCART1 | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AHRR, ARHGAP15, FAT1; maybe low, not absent; co-absent genes |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.535). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.1, -13.5); signed map (17.6, 15.9). **Vector** length 63.3, 9.37% of its response variance represented; |z| ≥ 3 in 1,165 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +9.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +13.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | +1.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.1 | -6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.9 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -3.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -5.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.7 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 2 subfamily E member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.3 — chr10:133,520,406-133,561,220 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CYP2E |
| Gene groups (HGNC) | Cytochrome P450 family 2 |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 11 pathways, smallest: Biosynthesis of maresins; Biosynthesis of DHA-derived SPMs; Xenobiotics |
| Matched by | ensembl_id |

**Function**, from UniProt [P05181](https://www.uniprot.org/uniprotkb/P05181) (Cytochrome P450 2E1):

> A cytochrome P450 monooxygenase involved in the metabolism of fatty acids. Mechanistically, uses molecular oxygen inserting one oxygen atom into a substrate, and reducing the second into a water molecule, with two electrons provided by NADPH via cytochrome P450 reductase (NADPH--hemoprotein reductase). Catalyzes the hydroxylation of carbon-hydrogen bonds. Hydroxylates fatty acids specifically at the omega-1 position displaying the highest catalytic activity for saturated fatty acids. May be …

**Summary**, from NCBI Gene [1571](https://www.ncbi.nlm.nih.gov/gene/1571):

> This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. This protein localizes to the endoplasmic reticulum and is induced by ethanol, the diabetic state, and starvation. The enzyme metabolizes both endogenous substrates, such as ethanol, acetone, and acetal, as well as exogenous substrates including benzene, carbon …

**Accessions** — [HGNC:2631](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2631) · Entrez [1571](https://www.ncbi.nlm.nih.gov/gene/1571) · UniProt [P05181](https://www.uniprot.org/uniprotkb/P05181) · Ensembl [ENSG00000130649](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130649)

## Data

Gene col 5092: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5092); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5092, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5092]; `tensor/DDL_lfc|DDL_z.npy` [5092]; `embed/gene_vectors.npy` [5092]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5092 or target_col == 5092). Every well: [[CYP2E1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP2E1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
