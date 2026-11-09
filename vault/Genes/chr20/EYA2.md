---
symbol: "EYA2"
type: "gene"
col: 754
ensembl_id: "ENSG00000064655"
name: "EYA transcriptional coactivator and phosphatase 2"
location: "20q13.12"
module: 19
arm: "+"
pooled_cpm: 39.79
n_lines_expressing: 16
n_dd_up: 15
n_dd_down: 23
n_dd_up_clean: 12
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 11
direction_downstream: 4
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# EYA2

*EYA transcriptional coactivator and phosphatase 2* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.73× (z +13.2, q 4e-37, up in 2 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +11.3, q 2e-27, up in 0 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.609× (z -6.5, q 5e-08, down in 10 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMOC1]] (+0.75, fdr 7e-06), [[NCKAP5-AS2]] (+0.69, fdr 7e-06), [[RSPO3]] (+0.65, fdr 7e-06); moves opposite to [[GLUL]] (-0.44, fdr 5e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[EBF2]] → it (grade B ⚠); 4 go from it, the strongest it → [[SFMBT2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 754.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.73×** | +13.2 | 4e-37 | 2/13 (SW 900, A-427) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +12.6 | 4e-34 | 1/12 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +11.3 | 2e-27 | 0/14 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +8.7 | 4e-16 | 5/14 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.4 | 2e-08 | 0/14 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +6.2 | 5e-08 | 1/12 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +5.5 | 3e-06 | 5/14 (NCI-H460, SW 1088, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.45×** | +4.9 | 8e-05 | 0/13 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +4.8 | 8e-05 | 0/14 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.41×** | +4.4 | 7e-04 | 0/13 | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +4.1 | 0.002 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.011 | 0/14 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.083 | 0/13 | rises with dose | position effect removed |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.086 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.092 | 1/13 (H4) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 754.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.609×** | -6.5 | 5e-08 | 10/14 (NCI-H1573, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.638×** | -5.9 | 1e-06 | 6/13 (NCI-H1573, A498, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.660×** | -5.4 | 1e-05 | 8/13 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **0.664×** | -5.4 | 1e-05 | 11/13 (A549, SHP-77, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.655×** | -5.1 | 3e-05 | 1/14 (SW 900) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.695×** | -4.8 | 2e-04 | 7/14 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.695×** | -4.8 | 2e-04 | 7/13 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.698×** | -4.7 | 2e-04 | 8/13 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.730×** | -4.0 | 0.005 | 10/14 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.724×** | -3.9 | 0.005 | 0/14 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.745×** | -3.8 | 0.006 | 11/14 (SHP-77, KATO III, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.814×** | -3.8 | 0.007 | 5/14 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.754×** | -3.7 | 0.010 | 5/14 (NCI-H1573, H4, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.765×** | -3.5 | 0.018 | 6/13 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.826×** | -3.5 | 0.018 | 0/14 | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.751×** | -3.5 | 0.019 | 7/13 (H4, NCI-H1573, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 754. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 372 | 0 | 24 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0772× (z -28.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.133× (z -15.1) |
| [[NCI-H460 (line)]] | wt | 31.3 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -16.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.242× (z -10.5) |
| [[KATO III (line)]] | alt | 213 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0889× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.309× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 202 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -15.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -12.9) |
| [[SHP-77 (line)]] | alt | 350 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.103× (z -17.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.146× (z -14.7) |
| [[A549 (line)]] | wt | 63.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0866× (z -19.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0674× (z -15.2) |
| [[HOP62 (line)]] | alt | 82.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -9.3) |
| [[A-427 (line)]] | wt | 37.3 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 36.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0998× (z -18.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.161× (z -10.2) |
| [[H4 (line)]] | wt | 12.6 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0713× (z -8.7) |
| [[Hs 766T (line)]] | wt | 32.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -10.9) ⚠ cell-cycle shift, explains ~53% of this change |
| [[PANC-1 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.26 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.70 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.70 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.79 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.34 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.63 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.33 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.76 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.83 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.17 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.74 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.71 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.42 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.49 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.21 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.92 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.18 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.36 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.25 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.88 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.85 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.75 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.39 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.31 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 754), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMOC1]] | +0.75 | +0.67 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[NCKAP5-AS2]] | +0.69 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[RSPO3]] | +0.65 | +0.59 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[GRAMD1B]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[TRPA1]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[CRLF2]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[P3H2-AS1]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[UNC5D]] | +0.59 | +0.40 / +0.68 | both halves | 4e-05 |  |
| [[NCKAP5]] | +0.58 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[CNTN1]] | +0.57 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[GPRIN3]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[LGSN]] | +0.56 | +0.47 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLUL]] | -0.44 | -0.39 / -0.47 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EBF2]] | B | EBF2 activity raises EYA2's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 2.71× lower at baseline in the lines without EBF2 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers EYA2's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[NCKAP5]] | C | NCKAP5 activity raises EYA2's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 2.34× lower at baseline in the lines without NCKAP5 | 0.012 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent; co-absent with the target |
| [[NCKAP5-AS2]] | C | NCKAP5-AS2 activity raises EYA2's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 2.55× lower at baseline in the lines without NCKAP5-AS2 | 0.035 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |
| [[UNC5D]] | C | UNC5D activity raises EYA2's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 2.91× lower at baseline in the lines without UNC5D | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11; co-absent with the target |
| [[COL22A1]] | C | COL22A1 activity raises EYA2's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 2.90× lower at baseline in the lines without COL22A1 | 0.063 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2; co-absent with the target |
| [[INHBA]] | C | INHBA activity raises EYA2's level | lines that do not express INHBA (32) vs lines expressing it (18) | 2.70× lower at baseline in the lines without INHBA | 0.068 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3; co-absent with the target |
| [[NRXN3]] | C | NRXN3 activity raises EYA2's level | lines that do not express NRXN3 (23) vs lines expressing it (27) | 2.14× lower at baseline in the lines without NRXN3 | 0.069 | ⚠ within organs, on part of the lines; also absent: RGS7, FGF13, ENSG00000255983; co-absent with the target |
| [[SMOC1]] | C | SMOC1 activity raises EYA2's level | lines that do not express SMOC1 (34) vs lines expressing it (16) | 3.54× lower at baseline in the lines without SMOC1 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CPLX2, LGSN, CYP24A1; co-absent with the target |
| [[FGF14]] | C | FGF14 activity raises EYA2's level | lines that do not express FGF14 (28) vs lines expressing it (22) | 2.87× lower at baseline in the lines without FGF14 | 0.094 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, PTPRD, KCNT2; co-absent with the target |
| [[SYT13]] | C | SYT13 activity raises EYA2's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 2.60× lower at baseline in the lines without SYT13 | 0.096 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SFMBT2]] | C | EYA2 activity raises SFMBT2's level | lines that do not express EYA2 (34) vs lines expressing it (16) | 3.44× lower at baseline in the lines without EYA2 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL22A1, LGSN, EPGN; co-absent with the target |
| [[SLC35F3]] | C | EYA2 activity raises SLC35F3's level | lines that do not express EYA2 (34) vs lines expressing it (16) | 3.23× lower at baseline in the lines without EYA2 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL22A1, LGSN, EPGN; co-absent with the target |
| [[FGF14]] | C | EYA2 activity raises FGF14's level | lines that do not express EYA2 (34) vs lines expressing it (16) | 3.45× lower at baseline in the lines without EYA2 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL22A1, LGSN, EPGN; co-absent with the target |
| [[SMOC1]] | C | EYA2 activity raises SMOC1's level | lines that do not express EYA2 (34) vs lines expressing it (16) | 4.39× lower at baseline in the lines without EYA2 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL22A1, LGSN, EPGN; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.636). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.9, 33.1); signed map (39.2, 45.6). **Vector** length 70.6, 27.6% of its response variance represented; |z| ≥ 3 in 458 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +8.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.6 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +2.3 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.9 | -5.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.5 | -4.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -5.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -2.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.1 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | EYA transcriptional coactivator and phosphatase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:46,894,624-47,188,844 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EAB1 |
| Gene groups (HGNC) | EYA transcriptional coactivator and phosphatases; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Recruitment and ATM-mediated phosphorylation of repair and signaling proteins at DNA double strand breaks; DNA Double Strand Break Response; DNA Double-Strand Break Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [O00167](https://www.uniprot.org/uniprotkb/O00167) (Protein phosphatase EYA2):

> Functions both as protein phosphatase and as transcriptional coactivator for SIX1, and probably also for SIX2, SIX4 and SIX5. Tyrosine phosphatase that dephosphorylates 'Tyr-142' of histone H2AX (H2AXY142ph) and promotes efficient DNA repair via the recruitment of DNA repair complexes containing MDC1. 'Tyr-142' phosphorylation of histone H2AX plays a central role in DNA repair and acts as a mark that distinguishes between apoptotic and repair responses to genotoxic stress. Its function as …

**Summary**, from NCBI Gene [2139](https://www.ncbi.nlm.nih.gov/gene/2139):

> This gene encodes a member of the eyes absent (EYA) family of proteins. The encoded protein may be post-translationally modified and may play a role in eye development. A similar protein in mice can act as a transcriptional activator. Alternative splicing results in multiple transcript variants, but the full-length natures of all of these variants have not yet been determined. [provided by RefSeq, Jul 2009]

**Accessions** — [HGNC:3520](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3520) · Entrez [2139](https://www.ncbi.nlm.nih.gov/gene/2139) · UniProt [O00167](https://www.uniprot.org/uniprotkb/O00167) · Ensembl [ENSG00000064655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064655)

## Data

Gene col 754: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 754); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 754, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 754]; `tensor/DDL_lfc|DDL_z.npy` [754]; `embed/gene_vectors.npy` [754]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 754 or target_col == 754). Every well: [[EYA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EYA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
