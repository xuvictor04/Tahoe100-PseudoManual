---
symbol: "NR2F1"
type: "gene"
col: 10643
ensembl_id: "ENSG00000175745"
name: "nuclear receptor subfamily 2 group F member 1"
location: "5q15"
module: 152
arm: "+"
pooled_cpm: 42.18
n_lines_expressing: 42
n_dd_up: 7
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# NR2F1

*nuclear receptor subfamily 2 group F member 1* — 5q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.15× (z +10.2, q 8e-22, up in 28 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.486× (z -6.8, q 6e-09, down in 31 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOX2]] (+0.63, fdr 1e-05), [[ATXN2]] (+0.56, fdr 1e-05), [[TFAP2A]] (+0.55, fdr 1e-05); moves opposite to [[TPD52L2]] (-0.60, fdr 1e-05), [[ZDHHC6]] (-0.58, fdr 1e-05), [[DLST]] (-0.50, fdr 4e-05).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TFAP2C]] → it (grade B ⚠); 4 go from it, the strongest it → [[HOXB-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10643.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +10.2 | 8e-22 | 28/40 (LoVo, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.76×** | +5.3 | 3e-05 | 22/38 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.77×** | +5.1 | 5e-05 | 17/35 (NCI-H2347, PANC-1, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +4.2 | 0.004 | 17/32 (NCI-H2347, LS 180, …) | two highest doses | cell-cycle shift (explains ~25% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.007 | 20/39 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.049 | 19/39 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.27×** | +3.2 | 0.100 | 18/40 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.38× | +3.1 | 0.15 | 14/40 (CFPAC-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10643.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.486×** | -6.8 | 6e-09 | 31/40 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.506×** | -6.4 | 4e-08 | 31/40 (C-33 A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.646×** | -4.1 | 0.007 | 25/39 (RPMI-7951, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.651×** | -4.1 | 0.007 | 23/40 (A-427, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.657×** | -4.0 | 0.008 | 21/39 (MIA PaCa-2, SHP-77, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.643×** | -3.9 | 0.008 | 22/39 (SHP-77, NCI-H460, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.678×** | -3.7 | 0.018 | 21/38 (NCI-H460, CHP-212, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.760×** | -3.7 | 0.018 | 18/40 (A-427, H4, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.692×** | -3.5 | 0.031 | 20/39 (MIA PaCa-2, SW 900, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.496×** | -3.5 | 0.031 | 19/38 (HT-29, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Gallic acid (drug)]] 5 µM |  | **0.774×** | -3.4 | 0.032 | 15/40 (SW 900, NCI-H23, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.778×** | -3.3 | 0.037 | 18/40 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.702×** | -3.3 | 0.037 | 18/39 (A-427, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.790×** | -3.1 | 0.067 | 17/40 (NCI-H460, A-172, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.713×** | -3.0 | 0.095 | 12/39 (CHP-212, SW48, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10643. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 160 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -21.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0907× (z -20.5) |
| [[MIA PaCa-2 (line)]] | alt | 172 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -19.2) |
| [[C-33 A (line)]] | alt | 525 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -21.9) |
| [[A-427 (line)]] | wt | 298 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0977× (z -19.9) |
| [[NCI-H460 (line)]] | wt | 54.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.129× (z -15.5) |
| [[SW 900 (line)]] | alt | 55.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.191× (z -9.9) |
| [[SW480 (line)]] | alt | 25.1 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.202× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 87.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.170× (z -11.4) |
| [[LoVo (line)]] | wt | 15.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.27× (z +14.8) | — |
| [[HCT15 (line)]] | alt | 12.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0811× (z -8.7) |
| [[HOP62 (line)]] | alt | 16.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 27.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 23.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.226× (z -8.7) |
| [[NCI-H661 (line)]] | alt | 369 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -9.9) |
| [[PANC-1 (line)]] | alt | 16.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +9.5) | — |
| [[RKO (line)]] | wt | 16.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +9.7) | — |
| [[A-172 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.64 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 156 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.41 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.18 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.20 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10643), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOX2]] | +0.63 | +0.50 / +0.65 | both halves | 1e-05 | STRING 454 |
| [[ATXN2]] | +0.56 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[TFAP2A]] | +0.55 | +0.49 / +0.55 | both halves | 1e-05 | STRING 596 |
| [[ARID2]] | +0.54 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[YAF2]] | +0.54 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[MEF2C]] | +0.54 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[HOXA6]] | +0.53 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[FOXA2]] | +0.53 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ARID1A]] | +0.53 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[SATB2-AS1]] | +0.53 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[HOXA5]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 | STRING 401 |
| [[LINC00461]] | +0.52 | +0.46 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPD52L2]] | -0.60 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[ZDHHC6]] | -0.58 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[DLST]] | -0.50 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[VAMP3]] | -0.48 | -0.43 / -0.47 | both halves | 4e-05 |  |
| [[DTD1]] | -0.47 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[HARS1]] | -0.47 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[RFT1]] | -0.47 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[WDR55]] | -0.46 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[SIKE1]] | -0.46 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[RNF141]] | -0.45 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[MTG1]] | -0.44 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[CDC16]] | -0.44 | -0.42 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TFAP2C]] | B | TFAP2C activity lowers NR2F1's level | lines that do not express TFAP2C (18) vs lines expressing it (32) | 1.98× higher at baseline in the lines without TFAP2C | 0.063 | ⚠ within organs, on part of the lines; also absent: LYPD1, SETBP1, SAA1 |
| [[PAX6]] | B | PAX6 activity raises NR2F1's level | lines that do not express PAX6 (30) vs lines expressing it (20) | 2.58× lower at baseline in the lines without PAX6 | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC02643, WT1-AS, CHRDL1 |
| [[ZNF827]] | C | ZNF827 activity lowers NR2F1's level | lines that do not express ZNF827 (4) vs lines expressing it (46) | 1.59× higher at baseline in the lines without ZNF827 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYNJ2, ITGA2-AS1, RND3; its own permutation p |
| [[NR2F1-AS1]] | C | NR2F1-AS1 activity raises NR2F1's level | lines that do not express NR2F1-AS1 (8) vs lines expressing it (42) | 4.01× lower at baseline in the lines without NR2F1-AS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: TGFB1, NR2F1, PCDH15; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXB-AS1]] | B | NR2F1 activity raises HOXB-AS1's level | lines that do not express NR2F1 (8) vs lines expressing it (42) | 2.26× lower at baseline in the lines without NR2F1 | 0.046 | ⚠ within organs, on part of the lines; also absent: NR2F1-AS1, PCDH15; maybe low, not absent |
| [[REV3L]] | B | NR2F1 activity raises REV3L's level | lines that do not express NR2F1 (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without NR2F1 | 0.072 | ⚠ within organs, on part of the lines; also absent: NR2F1-AS1, PCDH15; maybe low, not absent |
| [[MEF2C]] | B | NR2F1 activity raises MEF2C's level | lines that do not express NR2F1 (8) vs lines expressing it (42) | 3.77× lower at baseline in the lines without NR2F1 | 0.077 | ⚠ within organs, on part of the lines; also absent: NR2F1-AS1, PCDH15; maybe low, not absent |
| [[NR2F1-AS1]] | C | NR2F1 activity raises NR2F1-AS1's level | lines that do not express NR2F1 (8) vs lines expressing it (42) | 4.79× lower at baseline in the lines without NR2F1 | 0.031 | ⚠ within organs, on part of the lines; also absent: NR2F1-AS1, PCDH15; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.286). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.2, -26.0); signed map (10.6, -3.3). **Vector** length 95.9, 25.6% of its response variance represented; |z| ≥ 3 in 868 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +10.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.7 | +5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.1 | +0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.4 | +1.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | +1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +0.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.9 | +2.1 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.9 | -6.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.9 | -3.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor subfamily 2 group F member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q15 — chr5:93,583,222-93,594,611 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EAR-3, COUP-TFI, TCFCOUP1, SVP44, COUPTF1; previously ERBAL3, TFCOUP1 |
| Gene groups (HGNC) | Nuclear receptor subfamily 2 group F |
| Reactome | 1 pathways, smallest: Nuclear Receptor transcription pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P10589](https://www.uniprot.org/uniprotkb/P10589) (COUP transcription factor 1):

> Coup (chicken ovalbumin upstream promoter) transcription factor binds to the ovalbumin promoter and, in conjunction with another protein (S300-II) stimulates initiation of transcription. Binds to both direct repeats and palindromes of the 5'-AGGTCA-3' motif. Represses transcriptional activity of LHCG.

**Summary**, from NCBI Gene [7025](https://www.ncbi.nlm.nih.gov/gene/7025):

> The protein encoded by this gene is a nuclear hormone receptor and transcriptional regulator. The encoded protein acts as a homodimer and binds to 5'-AGGTCA-3' repeats. Defects in this gene are a cause of Bosch-Boonstra optic atrophy syndrome (BBOAS). [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:7975](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7975) · Entrez [7025](https://www.ncbi.nlm.nih.gov/gene/7025) · UniProt [P10589](https://www.uniprot.org/uniprotkb/P10589) · Ensembl [ENSG00000175745](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175745)

## Data

Gene col 10643: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10643); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10643, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10643]; `tensor/DDL_lfc|DDL_z.npy` [10643]; `embed/gene_vectors.npy` [10643]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10643 or target_col == 10643). Every well: [[NR2F1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR2F1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
