---
symbol: "RBP1"
type: "gene"
col: 3524
ensembl_id: "ENSG00000114115"
name: "retinol binding protein 1"
location: "3q23"
module: 73
arm: "+"
pooled_cpm: 16.68
n_lines_expressing: 13
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 13
direction_downstream: 17
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# RBP1

*retinol binding protein 1* — 3q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.44× (z +11.1, q 6e-26, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.51× (z +4.0, q 0.008, up in 0 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HepG2/C3A 0.113×, SW480 0.259×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW480 0.211×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.241×); [[Panobinostat (drug)]] 5 µM in 1 line (HepG2/C3A 0.140×).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFF1]] (+0.65, fdr 9e-06), [[LCK]] (+0.58, fdr 1e-05), [[TFF2]] (+0.57, fdr 3e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 17 go from it, the strongest it → [[OSBPL10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3524.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.44×** | +11.1 | 6e-26 | 3/4 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.86×** | +10.8 | 1e-24 | 6/10 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.57×** | +7.2 | 1e-10 | 5/7 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.31×** | +4.1 | 0.007 | 2/6 (SW480, SW1417) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.008 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +3.9 | 0.010 | 0/10 | top dose only | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.73×** | +3.7 | 0.015 | 3/9 (Panc 03.27, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.5 | 0.031 | 0/10 | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.43×** | +3.3 | 0.058 | 1/10 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.3 | 0.058 | 2/10 (CFPAC-1, SW1417) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.64×** | +3.3 | 0.058 | 3/10 (SW480, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.074 | 2/10 (SW1417, HepG2/C3A) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | 1.56× | +3.0 | 0.11 | 2/10 (SW480, SW1417) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3524.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HepG2/C3A 0.113×, SW480 0.259×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SW480 0.211×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.241×); [[Panobinostat (drug)]] 5 µM in 1 line (HepG2/C3A 0.140×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 5 µM |  | 0.588× | -3.6 | 0.13 | 7/11 (Panc 03.27, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.599× | -3.5 | 0.13 | 9/9 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.630× | -3.1 | 0.31 | 0/10 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3524. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 192 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 62.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 4.47 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.05 µM 0.0546× (z -8.5) |
| [[A-172 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.90 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3524), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFF1]] | +0.65 | +0.57 / +0.67 | both halves | 9e-06 | **novel candidate** |
| [[LCK]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_BILE_ACID_METABOLISM |
| [[TFF2]] | +0.57 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[KLK6]] | +0.54 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[KRTCAP3]] | +0.53 | +0.39 / +0.58 | both halves | 6e-05 |  |
| [[LEMD1]] | +0.52 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[KLK11]] | +0.51 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[KLK10]] | +0.51 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[PADI1]] | +0.49 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[FERMT1]] | +0.48 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[BLACAT1]] | +0.48 | +0.52 / +0.30 | both halves | 2e-04 |  |
| [[INPP5D]] | +0.48 | +0.58 / +0.24 | both halves | 4e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 1, C 12. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RBP1's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LCK]] | C | LCK activity raises RBP1's level | lines that do not express LCK (31) vs lines expressing it (19) | 3.44× lower at baseline in the lines without LCK | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent; co-absent with the target |
| [[PPP2R2B]] | C | PPP2R2B activity raises RBP1's level | lines that do not express PPP2R2B (23) vs lines expressing it (27) | 1.88× lower at baseline in the lines without PPP2R2B | 0.025 | ⚠ within organs, on part of the lines; also absent: SSTR2, COL5A1, MCAM; maybe low, not absent; co-absent with the target |
| [[GPX2]] | C | GPX2 activity raises RBP1's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 3.15× lower at baseline in the lines without GPX2 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31; co-absent with the target |
| [[BMP4]] | C | BMP4 activity raises RBP1's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 2.53× lower at baseline in the lines without BMP4 | 0.041 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises RBP1's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 1.76× lower at baseline in the lines without KCNH7 | 0.047 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[CEACAM1]] | C | CEACAM1 activity raises RBP1's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 2.19× lower at baseline in the lines without CEACAM1 | 0.050 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29; co-absent with the target |
| [[KLK7]] | C | KLK7 activity raises RBP1's level | lines that do not express KLK7 (38) vs lines expressing it (12) | 2.74× lower at baseline in the lines without KLK7 | 0.054 | ⚠ within organs, on part of the lines; also absent: KLK11, KLK6, ONECUT3; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity raises RBP1's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 2.14× lower at baseline in the lines without CSMD3 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[APOA2]] | C | APOA2 activity raises RBP1's level | lines that do not express APOA2 (46) vs lines expressing it (4) | 5.84× lower at baseline in the lines without APOA2 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, AFP, BMP10; co-absent with the target; its own permutation p |
| [[PEG3]] | C | PEG3 activity raises RBP1's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 1.51× lower at baseline in the lines without PEG3 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1; co-absent with the target |
| [[SLC30A10]] | C | SLC30A10 activity raises RBP1's level | lines that do not express SLC30A10 (22) vs lines expressing it (28) | 2.47× lower at baseline in the lines without SLC30A10 | 0.079 | ⚠ within organs, on part of the lines; also absent: PKHD1, LINC00698, LINC02147; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 3, C 14. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSBPL10]] | B | RBP1 activity raises OSBPL10's level | lines that do not express RBP1 (37) vs lines expressing it (13) | 1.95× lower at baseline in the lines without RBP1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ENSG00000260573, LGR5 |
| cells under [[Ouabain (Octahydrate) (drug)]] 0.5 µM | B | RBP1 activity raises the cells' numbers under Ouabain (Octahydrate) 0.5 µM (protects the cells) | lines that do not express RBP1 (37) vs lines expressing it (11) | the lines without RBP1: 0.67× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ENSG00000260573, LGR5 |
| [[BLACAT1]] | B | RBP1 activity raises BLACAT1's level | lines that do not express RBP1 (37) vs lines expressing it (13) | 1.85× lower at baseline in the lines without RBP1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ENSG00000260573, LGR5 |
| [[KCNH8]] | C | RBP1 activity raises KCNH8's level | lines that do not express RBP1 (37) vs lines expressing it (13) | 3.10× lower at baseline in the lines without RBP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ENSG00000260573, LGR5; co-absent with the target |
| [[DSG3]] | C | RBP1 activity raises DSG3's level | lines that do not express RBP1 (37) vs lines expressing it (13) | 3.31× lower at baseline in the lines without RBP1 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ENSG00000260573, LGR5; co-absent with the target |
| [[PIK3AP1]] | C | RBP1 activity raises PIK3AP1's level | lines that do not express RBP1 (37) vs lines expressing it (13) | 2.79× lower at baseline in the lines without RBP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ENSG00000260573, LGR5; co-absent with the target |
| [[INPP5D]] | C | RBP1 activity raises INPP5D's level | lines that do not express RBP1 (37) vs lines expressing it (13) | 3.57× lower at baseline in the lines without RBP1 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ENSG00000260573, LGR5; co-absent with the target |
| [[PCDH17]] | C | RBP1 activity raises PCDH17's level | lines that do not express RBP1 (37) vs lines expressing it (13) | 1.93× lower at baseline in the lines without RBP1 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ENSG00000260573, LGR5; co-absent with the target |
| [[LINC02964]] | C | RBP1 activity raises LINC02964's level | lines that do not express RBP1 (37) vs lines expressing it (13) | 2.32× lower at baseline in the lines without RBP1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ENSG00000260573, LGR5; co-absent with the target |
| [[LCK]] | C | RBP1 activity raises LCK's level | lines that do not express RBP1 (37) vs lines expressing it (13) | 2.31× lower at baseline in the lines without RBP1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ENSG00000260573, LGR5; co-absent with the target |
| [[ANO1]] | C | RBP1 activity raises ANO1's level | lines that do not express RBP1 (37) vs lines expressing it (13) | 2.60× lower at baseline in the lines without RBP1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ENSG00000260573, LGR5; co-absent with the target |
| [[KCNH7]] | C | RBP1 activity raises KCNH7's level | lines that do not express RBP1 (37) vs lines expressing it (13) | 1.77× lower at baseline in the lines without RBP1 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ENSG00000260573, LGR5; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.385). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (14.2, 53.2); signed map (69.1, 9.7). **Vector** length 26.6, 7.63% of its response variance represented; |z| ≥ 3 in 179 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.5 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.5 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.6 | +2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.6 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.6 | +3.3 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.8 | -1.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.7 | -3.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | retinol binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q23 — chr3:139,517,434-139,539,829 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CRABP-I, CRBP1, CRBP, RBPC, CRBPI, CRBP-I, hCRBP1 |
| Gene groups (HGNC) | Fatty acid binding protein family |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 9 pathways, smallest: Diseases associated with visual transduction; Diseases of the neuronal system; Retinoid cycle disease events |
| Matched by | ensembl_id |

**Function**, from UniProt [P09455](https://www.uniprot.org/uniprotkb/P09455) (Retinol-binding protein 1):

> Cytoplasmic retinol-binding protein. Accepts retinol from the transport protein STRA6, and thereby contributes to retinol uptake, storage and retinoid homeostasis.

**Summary**, from NCBI Gene [5947](https://www.ncbi.nlm.nih.gov/gene/5947):

> This gene encodes the carrier protein involved in the transport of retinol (vitamin A alcohol) from the liver storage site to peripheral tissue. Vitamin A is a fat-soluble vitamin necessary for growth, reproduction, differentiation of epithelial tissues, and vision. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2008]

**Accessions** — [HGNC:9919](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9919) · Entrez [5947](https://www.ncbi.nlm.nih.gov/gene/5947) · UniProt [P09455](https://www.uniprot.org/uniprotkb/P09455) · Ensembl [ENSG00000114115](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114115)

## Data

Gene col 3524: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3524); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3524, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3524]; `tensor/DDL_lfc|DDL_z.npy` [3524]; `embed/gene_vectors.npy` [3524]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3524 or target_col == 3524). Every well: [[RBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
