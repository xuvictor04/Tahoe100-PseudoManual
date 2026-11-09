---
symbol: "SNHG31"
type: "gene"
col: 13699
ensembl_id: "ENSG00000229267"
name: "small nucleolar RNA host gene 31"
location: "2q35"
module: 26
arm: "+"
pooled_cpm: 21.58
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 27
n_dd_up_clean: 8
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# SNHG31

*small nucleolar RNA host gene 31* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.40× (z +19.4, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.550× (z -6.7, q 1e-08, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKN2-AS1]] (+0.67, fdr 3e-05), [[STARD4-AS1]] (+0.66, fdr 1e-05), [[PNISR-AS1]] (+0.66, fdr 2e-05); moves opposite to [[RSAD1]] (-0.64, fdr 1e-05), [[COMMD2]] (-0.62, fdr 3e-05), [[GTF2H2C]] (-0.62, fdr 1e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13699.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.40×** | +19.4 | 0e+00 | 43/46 (SW1417, SHP-77, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.17×** | +15.4 | 0e+00 | 41/45 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.99×** | +11.8 | 5e-30 | 41/45 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.042 | 15/45 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.050 | 15/47 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.050 | 15/48 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.055 | 19/48 (SW1417, HEC-1-A, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.35×** | +3.4 | 0.056 | 14/47 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.25× | +3.2 | 0.10 | 11/48 (NCI-H1573, C-33 A, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13699.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.550×** | -6.7 | 1e-08 | 30/47 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.670×** | -6.3 | 7e-08 | 33/48 (C32, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.364×** | -5.9 | 6e-07 | 28/48 (SW 900, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.594×** | -5.8 | 7e-07 | 27/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.595×** | -5.8 | 7e-07 | 29/47 (C32, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.560×** | -5.2 | 2e-05 | 24/46 (C32, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.634×** | -5.1 | 3e-05 | 23/48 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.638×** | -4.8 | 9e-05 | 23/40 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.457×** | -4.6 | 3e-04 | 22/43 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.658×** | -4.5 | 4e-04 | 21/46 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.682×** | -4.3 | 1e-03 | 20/46 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.699×** | -4.0 | 0.003 | 24/47 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.704×** | -3.9 | 0.004 | 16/47 (A-427, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.711×** | -3.8 | 0.006 | 22/46 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.718×** | -3.7 | 0.008 | 18/47 (NCI-H1573, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.723×** | -3.6 | 0.010 | 18/47 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13699. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 43.0 | 3 | 4 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.35× (z +12.0) | [[Belinostat (drug)]] 5 µM 0.214× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 27.6 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.06× (z +13.6) | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -9.4) |
| [[PANC-1 (line)]] | alt | 24.0 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 46.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 25.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +11.6) | — |
| [[SW480 (line)]] | alt | 23.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +13.7) | — |
| [[A-172 (line)]] | wt | 29.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 19.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.41× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 10.9 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.91× (z +9.6) | — |
| [[J82 (line)]] | alt | 9.34 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 4.17× (z +10.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +10.2) | — |
| [[KATO III (line)]] | alt | 16.4 | 2 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 6.06× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 13.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 23.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 39.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 22.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +9.3) | [[TAK-901 (drug)]] 5 µM 0.0442× (z -8.7) |
| [[SW1417 (line)]] | alt | 12.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.76× (z +14.2) | — |
| [[A-427 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0913× (z -13.9) ⚠ toxic |
| [[A549 (line)]] | wt | 9.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 7.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.14× (z +10.0) | — |
| [[BT-474 (line)]] | alt | 6.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.6× (z +13.2) | — |
| [[HOP62 (line)]] | alt | 32.1 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.57× (z +13.1) | — |
| [[hTERT-HPNE (line)]] | wt | 8.35 | 0 | 1 | — | [[Diphenhydramine (drug)]] 5 µM 0.0553× (z -9.9) |
| [[LoVo (line)]] | wt | 11.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.51× (z +13.8) | — |
| [[LOX-IMVI (line)]] | wt | 31.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +9.8) | — |
| [[LS 180 (line)]] | wt | 9.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 22.6 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.77× (z +11.6) | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +9.6) | — |
| [[RKO (line)]] | wt | 9.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.79× (z +11.8) | — |
| [[SHP-77 (line)]] | alt | 17.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.42× (z +13.9) | — |
| [[A498 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13699), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKN2-AS1]] | +0.67 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[STARD4-AS1]] | +0.66 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[PNISR-AS1]] | +0.66 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[NUCKS1]] | +0.66 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | +0.66 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[DLEU2]] | +0.63 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[NCOA2]] | +0.62 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[RMI1]] | +0.62 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[CENPL]] | +0.62 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[CFAP418-AS1]] | +0.61 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[CDKN2C]] | +0.61 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[LINC01135]] | +0.60 | +0.53 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSAD1]] | -0.64 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[COMMD2]] | -0.62 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[GTF2H2C]] | -0.62 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[ST6GALNAC6]] | -0.59 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[EIF3M]] | -0.59 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[ANKS6]] | -0.58 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[PACC1]] | -0.58 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[MAST3]] | -0.58 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[ACTR5]] | -0.58 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[GRAMD4]] | -0.57 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[DCAF4]] | -0.56 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[MTG1]] | -0.56 | -0.44 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SNHG31's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LHFPL6]] | B | LHFPL6 activity raises SNHG31's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 2.01× lower at baseline in the lines without LHFPL6 | 0.040 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |
| [[RBKS]] | B | RBKS activity raises SNHG31's level | lines that do not express RBKS (6) vs lines expressing it (44) | 2.30× lower at baseline in the lines without RBKS | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2B]] | B | TOP2B activity lowers SNHG31's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.573). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-42.5, -52.5); signed map (31.2, -22.2). **Vector** length 100, 25.1% of its response variance represented; |z| ≥ 3 in 1,069 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +19.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.0 | +15.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.7 | +3.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.7 | +2.3 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.7 | +3.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.4 | -4.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.3 | -5.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.2 | -6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.1 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.9 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -0.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.8 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 31 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q35 — chr2:214,810,181-214,963,575 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54196](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54196) · Entrez [101928103](https://www.ncbi.nlm.nih.gov/gene/101928103) · Ensembl [ENSG00000229267](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229267)

## Data

Gene col 13699: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13699); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13699, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13699]; `tensor/DDL_lfc|DDL_z.npy` [13699]; `embed/gene_vectors.npy` [13699]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13699 or target_col == 13699). Every well: [[SNHG31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
