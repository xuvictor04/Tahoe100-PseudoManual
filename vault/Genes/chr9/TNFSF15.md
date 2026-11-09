---
symbol: "TNFSF15"
type: "gene"
col: 11201
ensembl_id: "ENSG00000181634"
name: "TNF superfamily member 15"
location: "9q32"
module: 55
arm: "+"
pooled_cpm: 8.26
n_lines_expressing: 19
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 61
direction_downstream: 63
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# TNFSF15

*TNF superfamily member 15* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.03× (z +11.0, q 3e-25, up in 3 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.68× (z +7.3, q 6e-11, up in 5 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.586× (z -5.3, q 4e-05, down in 13 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC12A2]] (+0.69, fdr 8e-06), [[SYK]] (+0.67, fdr 1e-05), [[KCNH8]] (+0.64, fdr 7e-06); moves opposite to [[DNAAF9]] (-0.54, fdr 9e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 61 arrows point to it, the strongest [[POU5F1B]] → it (grade B ⚠); 63 go from it, the strongest it → [[MAPK13]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11201.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +11.0 | 3e-25 | 3/13 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +10.2 | 9e-22 | 3/8 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +7.3 | 6e-11 | 5/17 (NCI-H2347, HCT15, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +7.2 | 6e-11 | 2/10 (NCI-H2347, Panc 03.27) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.64×** | +6.9 | 5e-10 | 9/17 (NCI-H2347, Panc 03.27, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.99×** | +6.8 | 1e-09 | 9/17 (NCI-H2347, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +6.7 | 2e-09 | 6/16 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +5.4 | 4e-06 | 6/15 (NCI-H2347, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +5.0 | 3e-05 | 9/17 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.0 | 0.004 | 1/16 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.007 | 11/17 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.47×** | +3.8 | 0.007 | 8/17 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.019 | 11/17 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Cyclosporin A (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.021 | 7/17 (NCI-H2347, NCI-H1573, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.036 | 3/17 (HT-29, SW1417, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.039 | 7/17 (BT-474, CFPAC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.039 | 7/17 (LoVo, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Sulfatinib (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.047 | 0/17 | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.83×** | +3.1 | 0.047 | 2/16 (LS 180, AsPC-1) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.41×** | +3.1 | 0.048 | 2/17 (KATO III, Panc 03.27) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11201.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.586×** | -5.3 | 4e-05 | 13/17 (SW48, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.592×** | -5.2 | 4e-05 | 15/17 (LS 180, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.610×** | -4.9 | 1e-04 | 10/17 (HCT15, SHP-77, …) | top dose only | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.611×** | -4.9 | 1e-04 | 10/17 (LS 180, HT-29, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.661×** | -4.1 | 0.004 | 7/17 (AsPC-1, Panc 03.27, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.713×** | -3.4 | 0.061 | 10/17 (HT-29, LS 180, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.695×** | -3.4 | 0.061 | 5/17 (HCT15, RKO, …) | all doses, flat | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -3.3 | 0.063 | 1/17 (SW48) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.733× | -3.1 | 0.12 | 9/17 (HCT15, HEC-1-A, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11201. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 50.6 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0576× (z -15.2) |
| [[HT-29 (line)]] | alt | 54.4 | 0 | 6 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0972× (z -11.3) |
| [[COLO 205 (line)]] | alt | 19.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0586× (z -13.8) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0266× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 12.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -12.6) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.136× (z -9.6) |
| [[SW1417 (line)]] | alt | 53.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -9.8) |
| [[SW48 (line)]] | wt | 21.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0102× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 21.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0731× (z -16.1) |
| [[NCI-H2347 (line)]] | alt | 15.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +9.8) | — |
| [[HCT15 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0477× (z -9.0) ⚠ transcription drop; unreliable plate only |
| [[KATO III (line)]] | alt | 7.06 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0544× (z -9.3) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 35.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +9.0) | — |
| [[A-172 (line)]] | wt | 0.971 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.791 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.656 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.584 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.859 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.845 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.769 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.718 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.770 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.669 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.960 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.15 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11201), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC12A2]] | +0.69 | +0.71 / +0.58 | both halves | 8e-06 |  |
| [[SYK]] | +0.67 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[KCNH8]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[ACSL5]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[IL20RA]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[DENND2D]] | +0.64 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[BMP4]] | +0.63 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[MYO7B]] | +0.62 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[EPS8L3]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CFTR]] | +0.62 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[TSPOAP1]] | +0.62 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[KBTBD12]] | +0.61 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF9]] | -0.54 | -0.53 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*61 arrows, 61 of them with an alert ⚠; grade A 0, B 7, C 54. Shown: the 12 strongest; 49 more arrows (49 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POU5F1B]] | B | POU5F1B activity raises TNFSF15's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 3.17× lower at baseline in the lines without POU5F1B | 0.027 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[PCAT1]] | B | PCAT1 activity raises TNFSF15's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 2.99× lower at baseline in the lines without PCAT1 | 0.030 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[KATNAL1]] | B | KATNAL1 activity lowers TNFSF15's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 5.45× higher at baseline in the lines without KATNAL1 | 0.031 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[DNAAF9]] | B | DNAAF9 activity lowers TNFSF15's level | lines that do not express DNAAF9 (12) vs lines expressing it (38) | 5.29× higher at baseline in the lines without DNAAF9 | 0.060 | ⚠ within organs, on part of the lines; also absent: CHST10, ENSG00000268163, RIMKLB; its own permutation p |
| [[MAPK13]] | B | MAPK13 activity raises TNFSF15's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 3.16× lower at baseline in the lines without MAPK13 | 0.065 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises TNFSF15's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GNA14]] | B | GNA14 activity raises TNFSF15's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 2.03× lower at baseline in the lines without GNA14 | 0.074 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[GRHL2]] | C | GRHL2 activity raises TNFSF15's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 7.54× lower at baseline in the lines without GRHL2 | 4e-05 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent with the target |
| [[SYK]] | C | SYK activity raises TNFSF15's level | lines that do not express SYK (30) vs lines expressing it (20) | 6.62× lower at baseline in the lines without SYK | 1e-04 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14; co-absent with the target |
| [[TMEM30B]] | C | TMEM30B activity raises TNFSF15's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 6.90× lower at baseline in the lines without TMEM30B | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; co-absent with the target |
| [[COL17A1]] | C | COL17A1 activity raises TNFSF15's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 5.83× lower at baseline in the lines without COL17A1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1; co-absent with the target |
| [[SPINT1-AS1]] | C | SPINT1-AS1 activity raises TNFSF15's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 5.15× lower at baseline in the lines without SPINT1-AS1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3; co-absent with the target |

### Downstream of this gene

*63 arrows, 63 of them with an alert ⚠; grade A 0, B 19, C 44. Shown: the 12 strongest; 51 more arrows (51 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAPK13]] | B | TNFSF15 activity raises MAPK13's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 4.19× lower at baseline in the lines without TNFSF15 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[DNAAF9]] | B | TNFSF15 activity lowers DNAAF9's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 4.75× higher at baseline in the lines without TNFSF15 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[PCAT1]] | B | TNFSF15 activity raises PCAT1's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 3.13× lower at baseline in the lines without TNFSF15 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[ABHD11]] | B | TNFSF15 activity raises ABHD11's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 3.03× lower at baseline in the lines without TNFSF15 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[TNFRSF21]] | B | TNFSF15 activity raises TNFRSF21's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 4.08× lower at baseline in the lines without TNFSF15 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[RAMP1]] | B | TNFSF15 activity raises RAMP1's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 2.56× lower at baseline in the lines without TNFSF15 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[ZG16B]] | B | TNFSF15 activity raises ZG16B's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 1.97× lower at baseline in the lines without TNFSF15 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[KATNAL1]] | B | TNFSF15 activity lowers KATNAL1's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 2.95× higher at baseline in the lines without TNFSF15 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[POU5F1B]] | B | TNFSF15 activity raises POU5F1B's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 2.45× lower at baseline in the lines without TNFSF15 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[MFSD6]] | B | TNFSF15 activity raises MFSD6's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 2.30× lower at baseline in the lines without TNFSF15 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[NOSTRIN]] | B | TNFSF15 activity raises NOSTRIN's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 2.75× lower at baseline in the lines without TNFSF15 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[FAM228B]] | B | TNFSF15 activity weakens FAM228B's drug response | lines that do not express TNFSF15 (31) vs lines expressing it (18) | the lines without TNFSF15 respond 1.85× as strongly (z diff -2.59); strongest at Homoharringtonine 5 µM: 0.45x vs 0.85x (z diff -4.7) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.9, 48.6); signed map (63.1, 8.1). **Vector** length 65.8, 21.3% of its response variance represented; |z| ≥ 3 in 516 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +7.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +3.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.3 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.5 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -3.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.6 | -4.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.6 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -3.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | TNF superfamily member 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:114,784,652-114,806,039 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TL1, VEGI, TL1A, VEGI192A, MGC129934, MGC129935 |
| Gene groups (HGNC) | Tumor necrosis factor superfamily |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 3 pathways, smallest: TNFs bind their physiological receptors; TNFR2 non-canonical NF-kB pathway; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [O95150](https://www.uniprot.org/uniprotkb/O95150) (Tumor necrosis factor ligand superfamily member 15):

> Cytokine that signals through TNFRSF25 receptor. Functions as a T-cell costimulator, that increases IL-2 responsiveness and secretion of pro-inflammatory cytokines which enhances T-cell activation, proliferation and the survival of activated T-cells. Inhibits vascular endothelial growth and angiogenesis (in vitro). Binds to the decoy receptor TNFRSF6B, blocking the activation normally triggered by TNFSF15 and leading to decreased T-cell activation and reduced inflammation.

**Summary**, from NCBI Gene [9966](https://www.ncbi.nlm.nih.gov/gene/9966):

> The protein encoded by this gene is a cytokine that belongs to the tumor necrosis factor (TNF) ligand family. This protein is abundantly expressed in endothelial cells, but is not expressed in either B or T cells. The expression of this protein is inducible by TNF and IL-1 alpha. This cytokine is a ligand for receptor TNFRSF25 and decoy receptor TNFRSF21/DR6. It can activate NF-kappaB and MAP kinases, and acts as an autocrine factor to induce apoptosis in endothelial cells. This cytokine is …

**Accessions** — [HGNC:11931](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11931) · Entrez [9966](https://www.ncbi.nlm.nih.gov/gene/9966) · UniProt [O95150](https://www.uniprot.org/uniprotkb/O95150) · Ensembl [ENSG00000181634](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181634)

## Data

Gene col 11201: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11201); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11201, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11201]; `tensor/DDL_lfc|DDL_z.npy` [11201]; `embed/gene_vectors.npy` [11201]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11201 or target_col == 11201). Every well: [[TNFSF15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFSF15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
