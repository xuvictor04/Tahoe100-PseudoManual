---
symbol: "ASNSP1"
type: "gene"
col: 14544
ensembl_id: "ENSG00000248498"
name: "ASNS pseudogene 1"
location: "8q11.1"
module: 63
arm: "+"
pooled_cpm: 2.68
n_lines_expressing: 15
n_dd_up: 29
n_dd_down: 3
n_dd_up_clean: 18
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 30
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# ASNSP1

*ASNS pseudogene 1* — 8q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.52× (z +9.5, q 1e-18, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +5.6, q 3e-06, up in 1 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.389× (z -6.2, q 4e-07, down in 8 of 11 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MARS1]] (+0.67, fdr 1e-05), [[CARS1]] (+0.66, fdr 1e-05), [[ASNS]] (+0.65, fdr 1e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01446]] → it (grade C ⚠); 30 go from it, the strongest it → [[YARS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14544.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.52×** | +9.5 | 1e-18 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.96×** | +7.1 | 4e-10 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.03×** | +6.7 | 4e-09 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +5.6 | 3e-06 | 1/8 (HS-578T) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **2.19×** | +5.1 | 3e-05 | 3/8 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **2.11×** | +4.9 | 9e-05 | 8/12 (SHP-77, RPMI-7951, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.84×** | +4.9 | 9e-05 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **2.09×** | +4.8 | 1e-04 | 5/10 (SHP-77, RPMI-7951, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.68×** | +4.8 | 1e-04 | 3/12 (PANC-1, HT-29, …) | rises with dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.69×** | +4.5 | 5e-04 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.98×** | +4.3 | 9e-04 | 0/6 | rises with dose | cell-cycle shift (explains ~5% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.40×** | +4.1 | 0.002 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Artesunate (drug)]] 5 µM |  | **1.55×** | +4.1 | 0.002 | 6/12 (SHP-77, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +3.9 | 0.004 | 0/7 | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.79×** | +3.8 | 0.005 | 2/13 (SNU-1, PANC-1) | two highest doses | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.78×** | +3.8 | 0.006 | 3/9 (SHP-77, RPMI-7951, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.21×** | +3.7 | 0.007 | 1/6 (SHP-77) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.007 | 4/11 (SHP-77, RPMI-7951, …) | rises with dose | position effect removed |
| [[Neratinib (drug)]] 5 µM |  | **1.74×** | +3.6 | 0.008 | 4/9 (SHP-77, RPMI-7951, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.58×** | +3.0 | 0.068 | 0/6 | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.58×** | +3.0 | 0.068 | 4/8 (SHP-77, NCI-H661, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.63×** | +3.0 | 0.070 | 0/7 | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14544.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.389×** | -6.2 | 4e-07 | 8/11 (H4, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[crizotinib (drug)]] 5 µM |  | **0.554×** | -3.7 | 0.058 | 1/10 (SNU-423) | top dose only |  |
| [[Quinidine (15% dihydroquinidine) (drug)]] 0.05 µM |  | **0.557×** | -3.5 | 0.076 | 2/10 (CHP-212, PANC-1) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.628× | -3.0 | 0.33 | 4/10 (H4, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14544. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 49.3 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.121× (z -11.3) |
| [[H4 (line)]] | wt | 38.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0469× (z -16.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0141× (z -16.0) |
| [[HS-578T (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0561× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.217 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.258 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.358 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.280 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.808 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.324 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.512 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.284 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.324 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.292 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.249 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.730 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.455 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.783 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.910 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.850 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.433 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14544), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARS1]] | +0.67 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[CARS1]] | +0.66 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[ASNS]] | +0.65 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[ALDH1L2]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[CEBPG]] | +0.62 | +0.43 / +0.69 | both halves | 3e-05 |  |
| [[LINC00662]] | +0.61 | +0.41 / +0.69 | both halves | 4e-05 |  |
| [[PHGDH]] | +0.61 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[PSAT1]] | +0.61 | +0.46 / +0.69 | both halves | 2e-05 |  |
| [[SARS1]] | +0.60 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[SESN2]] | +0.60 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[AARS1]] | +0.60 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[GARS1]] | +0.60 | +0.47 / +0.66 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01446]] | C | LINC01446 activity raises ASNSP1's level | lines that do not express LINC01446 (34) vs lines expressing it (16) | 2.99× lower at baseline in the lines without LINC01446 | 0.058 | ⚠ within organs, on part of the lines; also absent: GABRG2, BAGE2, ENSG00000253363; co-absent with the target |
| [[LINC01266]] | C | LINC01266 activity raises ASNSP1's level | lines that do not express LINC01266 (35) vs lines expressing it (15) | 3.43× lower at baseline in the lines without LINC01266 | 0.089 | ⚠ within organs, on part of the lines; also absent: UNC5D, KHDRBS2, ENSG00000260958; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 26, C 4. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YARS1]] | B | ASNSP1 activity raises YARS1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.46× lower at baseline in the lines without ASNSP1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[CARS1]] | B | ASNSP1 activity raises CARS1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.42× lower at baseline in the lines without ASNSP1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[GARS1]] | B | ASNSP1 activity raises GARS1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.46× lower at baseline in the lines without ASNSP1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[BEND6]] | B | ASNSP1 activity raises BEND6's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 2.12× lower at baseline in the lines without ASNSP1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[IARS1]] | B | ASNSP1 activity raises IARS1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.31× lower at baseline in the lines without ASNSP1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[SESN2]] | B | ASNSP1 activity raises SESN2's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.63× lower at baseline in the lines without ASNSP1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[PSAT1]] | B | ASNSP1 activity raises PSAT1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.86× lower at baseline in the lines without ASNSP1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[XPOT]] | B | ASNSP1 activity raises XPOT's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.35× lower at baseline in the lines without ASNSP1 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[ASNS]] | B | ASNSP1 activity raises ASNS's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.67× lower at baseline in the lines without ASNSP1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[MARS1]] | B | ASNSP1 activity raises MARS1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.45× lower at baseline in the lines without ASNSP1 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[CEBPG]] | B | ASNSP1 activity raises CEBPG's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.34× lower at baseline in the lines without ASNSP1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[CHAC1]] | B | ASNSP1 activity raises CHAC1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.54× lower at baseline in the lines without ASNSP1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.643). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.9, 48.3); signed map (-12.9, 24.6). **Vector** length 29.1, 7.66% of its response variance represented; |z| ≥ 3 in 276 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.55 to 16); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.57 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.57 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.4 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.3 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.1 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.0 | +4.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.0 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.7 | -2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -0.7 | +0.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -0.7 | -1.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.6 | -0.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -0.6 | +0.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -0.6 | +1.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ASNS pseudogene 1 |
| Locus type | pseudogene |
| Location | 8q11.1 — chr8:46,579,213-46,614,523 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously ASNSL1 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:754](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:754) · Entrez [389652](https://www.ncbi.nlm.nih.gov/gene/389652) · Ensembl [ENSG00000248498](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248498)

## Data

Gene col 14544: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14544); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14544, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14544]; `tensor/DDL_lfc|DDL_z.npy` [14544]; `embed/gene_vectors.npy` [14544]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14544 or target_col == 14544). Every well: [[ASNSP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASNSP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
