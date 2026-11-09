---
symbol: "GRIK4"
type: "gene"
col: 7371
ensembl_id: "ENSG00000149403"
name: "glutamate ionotropic receptor kainate type subunit 4"
location: "11q23.3"
module: 166
arm: "+"
pooled_cpm: 11.05
n_lines_expressing: 35
n_dd_up: 31
n_dd_down: 12
n_dd_up_clean: 29
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 3
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# GRIK4

*glutamate ionotropic receptor kainate type subunit 4* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.52× (z +21.3, q 0e+00, up in 24 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.546× (z -7.3, q 2e-10, down in 20 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNIP1]] (+0.62, fdr 1e-05), [[KMO]] (+0.61, fdr 1e-05), [[CCDC3]] (+0.60, fdr 7e-06); moves opposite to [[WRN]] (-0.51, fdr 2e-05), [[NTAQ1]] (-0.50, fdr 1e-04), [[RPGR]] (-0.50, fdr 5e-05).
> It is in [[Module 166]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[LINC01933]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7371.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.52×** | +21.3 | 0e+00 | 24/30 (Panc 03.27, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.17×** | +19.5 | 0e+00 | 17/27 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.27×** | +13.8 | 3e-41 | 25/33 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.15×** | +9.2 | 7e-18 | 18/32 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.06×** | +8.6 | 9e-16 | 14/33 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.93×** | +7.8 | 5e-13 | 15/33 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +7.8 | 6e-13 | 14/29 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +6.9 | 4e-10 | 12/32 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.71×** | +6.4 | 1e-08 | 11/31 (A549, A-427, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.67×** | +5.9 | 3e-07 | 16/30 (HOP62, HCT15, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.5 | 2e-06 | 12/33 (A498, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +5.3 | 5e-06 | 4/22 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.50×** | +4.8 | 7e-05 | 13/31 (HOP62, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +4.7 | 1e-04 | 12/30 (HepG2/C3A, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +4.3 | 5e-04 | 12/32 (HOP62, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.3 | 7e-04 | 5/26 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7371.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.546×** | -7.3 | 2e-10 | 20/32 (HS-578T, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.591×** | -6.3 | 7e-08 | 19/32 (HOP62, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.601×** | -6.1 | 2e-07 | 21/29 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.614×** | -5.9 | 6e-07 | 18/31 (HOP62, NCI-H1792, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.636×** | -5.5 | 5e-06 | 19/33 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.687×** | -4.4 | 0.001 | 7/31 (A498, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.711×** | -4.1 | 0.003 | 16/33 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.716×** | -3.9 | 0.008 | 10/32 (HOP62, HCT15, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.734×** | -3.7 | 0.012 | 14/30 (CHP-212, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.811×** | -3.6 | 0.017 | 15/32 (Panc 03.27, SNU-423, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.758×** | -3.4 | 0.040 | 10/32 (HOP62, SNU-423, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.761×** | -3.3 | 0.046 | 10/31 (A498, SW 900, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.780× | -3.0 | 0.11 | 12/33 (A498, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7371. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 49.7 | 1 (1 ⚠) | 8 (6 ⚠) | [[Adagrasib (drug)]] 0.05 µM 2.14× (z +13.6) ⚠ position not correctable | [[Dinaciclib (drug)]] 5 µM 0.0902× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.171× (z -9.3) |
| [[PANC-1 (line)]] | alt | 3.79 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 11.7× (z +10.8) | — |
| [[LoVo (line)]] | wt | 34.2 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0950× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.280× (z -9.0) |
| [[SNU-423 (line)]] | alt | 42.6 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0741× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0797× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 4.75 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.79× (z +10.3) | [[Belinostat (drug)]] 0.5 µM 0.0883× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 13.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0365× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 14.1 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.103× (z -9.2) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.120× (z -8.6) |
| [[A-172 (line)]] | wt | 3.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +11.1) | — |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 1 | — | [[Auranofin (drug)]] 0.5 µM 0.0656× (z -9.9) |
| [[HCT15 (line)]] | alt | 7.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.02× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 5.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.7× (z +12.3) | — |
| [[hTERT-HPNE (line)]] | wt | 3.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.1× (z +10.7) | — |
| [[J82 (line)]] | alt | 6.93 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.104× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 7.60 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.70× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 25.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.147× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~12% of this change |
| [[NCI-H2347 (line)]] | alt | 4.77 | 0 | 1 | — | [[Budesonide (drug)]] 5 µM 0.0846× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 10.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.53× (z +12.6) | — |
| [[SHP-77 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0731× (z -11.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 32.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7371), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNIP1]] | +0.62 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[KMO]] | +0.61 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[CCDC3]] | +0.60 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[GRIN2A]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 | pathway: Neuronal System; STRING 690 |
| [[ESR1]] | +0.59 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[ABCA13]] | +0.58 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[FAM13C]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[SYNPO]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[NTF3]] | +0.58 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[CGNL1]] | +0.57 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[RERGL]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[LINC02968]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRN]] | -0.51 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[NTAQ1]] | -0.50 | -0.58 / -0.33 | both halves | 1e-04 |  |
| [[RPGR]] | -0.50 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[WDR5]] | -0.50 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[FAM135A]] | -0.48 | -0.59 / -0.31 | both halves | 2e-04 |  |
| [[SLC38A9]] | -0.47 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[PDS5A]] | -0.47 | -0.57 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GRIK4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NPTXR]] | B | NPTXR activity raises GRIK4's level | lines that do not express NPTXR (11) vs lines expressing it (39) | 2.22× lower at baseline in the lines without NPTXR | 0.051 | ⚠ within organs, on part of the lines; also absent: WNT9A, RAB6B, MAPK8IP2; maybe low, not absent |
| [[IGDCC4]] | B | IGDCC4 activity raises GRIK4's level | lines that do not express IGDCC4 (18) vs lines expressing it (32) | 1.74× lower at baseline in the lines without IGDCC4 | 0.059 | ⚠ within organs, on part of the lines; also absent: C19orf18, ENSG00000176593, LINC02813; maybe low, not absent |
| [[CSF1R]] | B | CSF1R activity raises GRIK4's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 1.71× lower at baseline in the lines without CSF1R | 0.082 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent |
| [[CADM1]] | B | CADM1 activity raises GRIK4's level | lines that do not express CADM1 (18) vs lines expressing it (32) | 2.20× lower at baseline in the lines without CADM1 | 0.0998 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, BEND6, ARNT2 |
| [[BOC]] | C | BOC activity raises GRIK4's level | lines that do not express BOC (21) vs lines expressing it (29) | 2.39× lower at baseline in the lines without BOC | 0.026 | ⚠ within organs, on part of the lines; also absent: VSTM4, PIEZO2, ARNT2; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01933]] | B | GRIK4 activity raises LINC01933's level | lines that do not express GRIK4 (15) vs lines expressing it (35) | 1.43× lower at baseline in the lines without GRIK4 | 0.062 | ⚠ within organs, on part of the lines; also absent: PRKAA2, RADIL, CHN1; maybe low, not absent |
| [[SPTB]] | B | GRIK4 activity raises SPTB's level | lines that do not express GRIK4 (15) vs lines expressing it (35) | 2.02× lower at baseline in the lines without GRIK4 | 0.071 | ⚠ within organs, on part of the lines; also absent: PRKAA2, RADIL, CHN1; maybe low, not absent |
| [[CCDC148]] | B | GRIK4 activity raises CCDC148's level | lines that do not express GRIK4 (15) vs lines expressing it (35) | 1.67× lower at baseline in the lines without GRIK4 | 0.076 | ⚠ within organs, on part of the lines; also absent: PRKAA2, RADIL, CHN1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.502). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.1, 19.3); signed map (40.0, 18.0). **Vector** length 73.8, 15.5% of its response variance represented; |z| ≥ 3 in 958 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.5 | +21.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +13.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change | +6.1 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +5.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +5.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +4.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -6.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.6 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.4 | -7.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -1.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | glutamate ionotropic receptor kainate type subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:120,511,746-120,988,906 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GluK4, KA1; previously GRIK |
| Gene groups (HGNC) | Glutamate ionotropic receptor kainate type subunits |
| Reactome | 6 pathways, smallest: Activation of Ca-permeable Kainate Receptor; Ionotropic activity of kainate receptors; Activation of kainate receptors upon glutamate binding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16099](https://www.uniprot.org/uniprotkb/Q16099) (Glutamate receptor ionotropic, kainate 4):

> Ionotropic glutamate receptor that functions as a cation-permeable ligand-gated ion channel. Cannot form functional channels on its own. Shows channel activity only in heteromeric assembly with GRIK1, GRIK2 and GRIK3 subunits (By similarity).

**Summary**, from NCBI Gene [2900](https://www.ncbi.nlm.nih.gov/gene/2900):

> This gene encodes a protein that belongs to the glutamate-gated ionic channel family. Glutamate functions as the major excitatory neurotransmitter in the central nervous system through activation of ligand-gated ion channels and G protein-coupled membrane receptors. The protein encoded by this gene forms functional heteromeric kainate-preferring ionic channels with the subunits encoded by related gene family members. Alternatively spliced transcript variants encoding different isoforms have …

**Accessions** — [HGNC:4582](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4582) · Entrez [2900](https://www.ncbi.nlm.nih.gov/gene/2900) · UniProt [Q16099](https://www.uniprot.org/uniprotkb/Q16099) · Ensembl [ENSG00000149403](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149403)

## Data

Gene col 7371: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7371); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7371, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7371]; `tensor/DDL_lfc|DDL_z.npy` [7371]; `embed/gene_vectors.npy` [7371]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7371 or target_col == 7371). Every well: [[GRIK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRIK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
