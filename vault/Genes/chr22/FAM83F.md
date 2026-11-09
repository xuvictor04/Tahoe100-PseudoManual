---
symbol: "FAM83F"
type: "gene"
col: 5452
ensembl_id: "ENSG00000133477"
name: "scaffolding CK1 anchoring protein F"
location: "22q13.1"
module: 55
arm: "+"
pooled_cpm: 8.23
n_lines_expressing: 18
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 44
direction_downstream: 37
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# FAM83F

*scaffolding CK1 anchoring protein F* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.52× (z +9.9, q 2e-20, up in 0 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.75× (z +4.4, q 0.001, up in 0 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.579× (z -5.9, q 2e-06, down in 12 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (RKO 0.147×, LoVo 0.292×, LS 180 0.321×, COLO 205 0.230×, …; ⚠ cell-cycle shift, explains ~29% of this change); [[Harringtonine (drug)]] 5 µM in 4 lines (LoVo 0.319×, SW480 0.310×, LS 180 0.294×, RKO 0.242×); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (RKO 0.142×, LoVo 0.348×, LS 180 0.307×); [[Meloxicam (drug)]] 0.5 µM in 1 line (A-427 0.0414×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALDH1L1]] (+0.70, fdr 1e-05), [[LINC03040]] (+0.68, fdr 1e-05), [[USH1C]] (+0.68, fdr 7e-06); moves opposite to [[DNAAF9]] (-0.47, fdr 4e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 44 arrows point to it, the strongest [[ZNF503-AS1]] → it (grade B ⚠); 37 go from it, the strongest it → [[MCF2L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5452.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.52×** | +9.9 | 2e-20 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.40×** | +9.7 | 5e-20 | 2/12 (COLO 205, SW48) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +6.4 | 3e-08 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +4.5 | 9e-04 | 1/15 (CFPAC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.75×** | +4.4 | 0.001 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.004 | 1/14 (NCI-H1573) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.42×** | +3.9 | 0.009 | 3/16 (SW480, LS 180, …) | two highest doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.8 | 0.012 | 2/13 (LS 180, LoVo) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +3.7 | 0.014 | 1/12 (LoVo) | top dose only | noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.030 | 0/16 | inconsistent across doses |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.030 | 3/15 (LS 180, SHP-77, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.4 | 0.038 | 0/14 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.52×** | +3.3 | 0.041 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.047 | 4/15 (LS 180, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5452.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (RKO 0.147×, LoVo 0.292×, LS 180 0.321×, COLO 205 0.230×, …; ⚠ cell-cycle shift, explains ~29% of this change); [[Harringtonine (drug)]] 5 µM in 4 lines (LoVo 0.319×, SW480 0.310×, LS 180 0.294×, RKO 0.242×); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (RKO 0.142×, LoVo 0.348×, LS 180 0.307×); [[Meloxicam (drug)]] 0.5 µM in 1 line (A-427 0.0414×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.579×** | -5.9 | 2e-06 | 12/15 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.672×** | -4.5 | 0.002 | 5/16 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.792×** | -3.7 | 0.036 | 12/14 (RKO, LoVo, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.726×** | -3.6 | 0.043 | 8/16 (SW48, SHP-77, …) | inconsistent across doses |  |
| [[Malotilate (drug)]] 0.5 µM |  | 0.749× | -3.3 | 0.11 | 2/16 (KATO III, LS 180) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.751× | -3.2 | 0.11 | 9/14 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.756× | -3.2 | 0.13 | 2/16 (Panc 03.27, KATO III) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.761× | -3.1 | 0.15 | 10/16 (SHP-77, LoVo, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5452. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 24.9 | 0 | 5 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0576× (z -17.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -12.4) |
| [[LoVo (line)]] | wt | 47.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -14.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.319× (z -9.4) |
| [[LS 180 (line)]] | wt | 43.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -12.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.307× (z -8.9) |
| [[COLO 205 (line)]] | alt | 34.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 27.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0578× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 31.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -10.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.310× (z -9.2) |
| [[A-427 (line)]] | wt | 3.46 | 0 | 1 | — | [[Meloxicam (drug)]] 0.5 µM 0.0414× (z -10.5) |
| [[HCT15 (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -9.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 6.89 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0607× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0820× (z -15.7) ⚠ toxic |
| [[A-172 (line)]] | wt | 0.924 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.574 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.933 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.737 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.743 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.965 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.948 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.571 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.598 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.738 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.772 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.876 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 17.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5452), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH1L1]] | +0.70 | +0.57 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[LINC03040]] | +0.68 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[USH1C]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[SLC5A1]] | +0.64 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[MYO7B]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ABO]] | +0.64 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[RIMBP2]] | +0.63 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[ESRP1]] | +0.63 | +0.52 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[TMEM125]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[EPS8L3]] | +0.62 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[INPP5D]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[LINC02253]] | +0.61 | +0.57 / +0.62 | both halves | 9e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF9]] | -0.47 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 1, C 43. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF503-AS1]] | B | ZNF503-AS1 activity raises FAM83F's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 2.12× lower at baseline in the lines without ZNF503-AS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[TMEM45B]] | C | TMEM45B activity raises FAM83F's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 6.08× lower at baseline in the lines without TMEM45B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881; co-absent with the target |
| [[ILDR2]] | C | ILDR2 activity raises FAM83F's level | lines that do not express ILDR2 (31) vs lines expressing it (19) | 3.78× lower at baseline in the lines without ILDR2 | 0.003 | ⚠ within organs, on part of the lines; also absent: NKD1, ENSG00000265554, PADI1; co-absent with the target |
| [[ADGRG5]] | C | ADGRG5 activity raises FAM83F's level | lines that do not express ADGRG5 (35) vs lines expressing it (15) | 4.65× lower at baseline in the lines without ADGRG5 | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC01559, RNF183, GPA33; maybe low, not absent; co-absent with the target |
| [[LINC03040]] | C | LINC03040 activity raises FAM83F's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 4.23× lower at baseline in the lines without LINC03040 | 0.005 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2; co-absent with the target |
| [[SLC5A1]] | C | SLC5A1 activity raises FAM83F's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 7.12× lower at baseline in the lines without SLC5A1 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125; co-absent with the target |
| [[GTSF1]] | C | GTSF1 activity raises FAM83F's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 1.33× lower at baseline in the lines without GTSF1 | 0.006 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[NKD1]] | C | NKD1 activity raises FAM83F's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 4.31× lower at baseline in the lines without NKD1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981; co-absent with the target |
| [[TMEM132D]] | C | TMEM132D activity raises FAM83F's level | lines that do not express TMEM132D (29) vs lines expressing it (21) | 2.45× lower at baseline in the lines without TMEM132D | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000271955, ENSG00000287211, GABRG2; maybe low, not absent; co-absent with the target |
| [[LINC02253]] | C | LINC02253 activity raises FAM83F's level | lines that do not express LINC02253 (35) vs lines expressing it (15) | 4.77× lower at baseline in the lines without LINC02253 | 0.007 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02058, ENSG00000289349; co-absent with the target |
| [[LINC01814]] | C | LINC01814 activity raises FAM83F's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 4.38× lower at baseline in the lines without LINC01814 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3; co-absent with the target |
| [[ESRP1]] | C | ESRP1 activity raises FAM83F's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 5.15× lower at baseline in the lines without ESRP1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7; co-absent with the target |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 6, C 31. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCF2L]] | B | FAM83F activity raises MCF2L's level | lines that do not express FAM83F (32) vs lines expressing it (18) | 3.18× lower at baseline in the lines without FAM83F | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TRIM15, TMEM45B |
| [[FKBP9P1]] | B | FAM83F activity raises FKBP9P1's level | lines that do not express FAM83F (32) vs lines expressing it (18) | 1.84× lower at baseline in the lines without FAM83F | 0.016 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TRIM15, TMEM45B |
| [[ARHGEF16]] | B | FAM83F activity raises ARHGEF16's level | lines that do not express FAM83F (32) vs lines expressing it (18) | 2.91× lower at baseline in the lines without FAM83F | 0.031 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TRIM15, TMEM45B |
| [[MROH7]] | B | FAM83F activity raises MROH7's level | lines that do not express FAM83F (32) vs lines expressing it (18) | 2.78× lower at baseline in the lines without FAM83F | 0.032 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TRIM15, TMEM45B |
| [[ZFAND1]] | B | FAM83F activity raises ZFAND1's level | lines that do not express FAM83F (32) vs lines expressing it (18) | 1.81× lower at baseline in the lines without FAM83F | 0.037 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TRIM15, TMEM45B |
| [[SYTL1]] | B | FAM83F activity raises SYTL1's level | lines that do not express FAM83F (32) vs lines expressing it (18) | 2.57× lower at baseline in the lines without FAM83F | 0.090 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TRIM15, TMEM45B |
| [[FAAH2]] | C | FAM83F activity raises FAAH2's level | lines that do not express FAM83F (32) vs lines expressing it (18) | 5.82× lower at baseline in the lines without FAM83F | 0.004 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TRIM15, TMEM45B; co-absent with the target |
| [[TMC4]] | C | FAM83F activity raises TMC4's level | lines that do not express FAM83F (32) vs lines expressing it (18) | 5.10× lower at baseline in the lines without FAM83F | 0.004 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TRIM15, TMEM45B; co-absent with the target |
| [[ESRP1]] | C | FAM83F activity raises ESRP1's level | lines that do not express FAM83F (32) vs lines expressing it (18) | 9.21× lower at baseline in the lines without FAM83F | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TRIM15, TMEM45B; co-absent with the target |
| [[SYK]] | C | FAM83F activity raises SYK's level | lines that do not express FAM83F (32) vs lines expressing it (18) | 7.06× lower at baseline in the lines without FAM83F | 0.009 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TRIM15, TMEM45B; co-absent with the target |
| [[PROM1]] | C | FAM83F activity raises PROM1's level | lines that do not express FAM83F (32) vs lines expressing it (18) | 4.92× lower at baseline in the lines without FAM83F | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TRIM15, TMEM45B; co-absent with the target |
| [[LINC03040]] | C | FAM83F activity raises LINC03040's level | lines that do not express FAM83F (32) vs lines expressing it (18) | 3.34× lower at baseline in the lines without FAM83F | 0.013 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TRIM15, TMEM45B; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.628). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.5, 53.3); signed map (61.6, 9.3). **Vector** length 46.6, 13.6% of its response variance represented; |z| ≥ 3 in 352 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +6.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.7 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +4.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | -0.4 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -1.0 | -3.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -0.9 | -5.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.9 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | scaffolding CK1 anchoring protein F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:39,994,954-40,043,534 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously FAM83F |
| Gene groups (HGNC) | Scaffolding anchor of CK1 domain containing |
| Matched by | ensembl_id |

UniProt [Q8NEG4](https://www.uniprot.org/uniprotkb/Q8NEG4) carries no function annotation.

**Summary**, from NCBI Gene [113828](https://www.ncbi.nlm.nih.gov/gene/113828):

> Predicted to enable protein kinase binding activity. Predicted to be involved in signal transduction. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25148](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25148) · Entrez [113828](https://www.ncbi.nlm.nih.gov/gene/113828) · UniProt [Q8NEG4](https://www.uniprot.org/uniprotkb/Q8NEG4) · Ensembl [ENSG00000133477](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133477)

## Data

Gene col 5452: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5452); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5452, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5452]; `tensor/DDL_lfc|DDL_z.npy` [5452]; `embed/gene_vectors.npy` [5452]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5452 or target_col == 5452). Every well: [[FAM83F — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM83F.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
