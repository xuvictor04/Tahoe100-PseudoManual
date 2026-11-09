---
symbol: "RFPL1S"
type: "gene"
col: 13459
ensembl_id: "ENSG00000225465"
name: "RFPL1 antisense RNA 1"
location: "22q12.2"
module: 128
arm: "+"
pooled_cpm: 2.17
n_lines_expressing: 34
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 11
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# RFPL1S

*RFPL1 antisense RNA 1* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.86× (z +20.0, q 0e+00, up in 10 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.553× (z -3.8, q 0.086, down in 10 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 3 lines (NCI-H23 0.0274×, A-427 0.161×, C-33 A 0.149×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H23 0.0623×, C-33 A 0.100×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.261×, C-33 A 0.272×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH23]] (+0.71, fdr 7e-06), [[CACNA1B]] (+0.66, fdr 7e-06), [[LRRC36]] (+0.65, fdr 7e-06).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GPC3]] → it (grade B ⚠); 11 go from it, the strongest it → [[DGCR5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13459.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.86×** | +20.0 | 0e+00 | 10/16 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.08×** | +10.3 | 2e-22 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.16×** | +7.8 | 1e-12 | 1/1 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +6.9 | 6e-10 | 1/5 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.76×** | +6.4 | 2e-08 | 3/10 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.39×** | +6.4 | 2e-08 | 10/27 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.79×** | +6.0 | 1e-07 | 3/25 (SW480, A498, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.27×** | +6.0 | 1e-07 | 7/19 (SW480, NCI-H1792, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +5.4 | 5e-06 | 10/26 (A498, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +5.1 | 2e-05 | 6/14 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.85×** | +4.5 | 3e-04 | 10/28 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +4.2 | 0.001 | 2/19 (SW480, LoVo) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +3.9 | 0.004 | 8/16 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +3.8 | 0.005 | 10/22 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.96×** | +3.5 | 0.016 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +3.3 | 0.038 | 4/13 (HEC-1-A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.81×** | +3.1 | 0.063 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13459.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 3 lines (NCI-H23 0.0274×, A-427 0.161×, C-33 A 0.149×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H23 0.0623×, C-33 A 0.100×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.261×, C-33 A 0.272×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.553×** | -3.8 | 0.086 | 10/22 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 0.736× | -3.2 | 0.30 | 3/30 (C-33 A, A-427, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.660× | -3.1 | 0.30 | 9/28 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.662× | -3.1 | 0.30 | 8/21 (NCI-H23, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13459. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 24.1 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0274× (z -21.7) |
| [[C-33 A (line)]] | alt | 27.6 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.100× (z -11.1) |
| [[A-427 (line)]] | wt | 15.7 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.161× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 2.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.50× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 5.04 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0457× (z -9.0) |
| [[A-172 (line)]] | wt | 0.900 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.988 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.721 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.543 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.556 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.424 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.690 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.452 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.676 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.503 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.682 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.668 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.965 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.827 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.793 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.441 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.649 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.862 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.712 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.578 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13459), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH23]] | +0.71 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[CACNA1B]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[LRRC36]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[DANT1]] | +0.64 | +0.53 / +0.55 | both halves | 1e-05 | same gene group |
| [[LINC00466]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[JPH3]] | +0.64 | +0.59 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[LINC01122]] | +0.62 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[CHST8]] | +0.60 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ABCA17P]] | +0.59 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[TMEM266]] | +0.59 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[CFL1P1-1]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[SYN2]] | +0.58 | +0.57 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPC3]] | B | GPC3 activity raises RFPL1S's level | lines that do not express GPC3 (35) vs lines expressing it (15) | 2.14× lower at baseline in the lines without GPC3 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TF, GCG, APOA2 |
| [[TMEM150C]] | C | TMEM150C activity raises RFPL1S's level | lines that do not express TMEM150C (13) vs lines expressing it (37) | 1.74× lower at baseline in the lines without TMEM150C | 0.057 | ⚠ within organs, on part of the lines; also absent: AP3B2, MED12L, RAB6B; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DGCR5]] | B | RFPL1S activity raises DGCR5's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 2.80× lower at baseline in the lines without RFPL1S | 0.014 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent |
| [[MEGF11]] | B | RFPL1S activity raises MEGF11's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 2.37× lower at baseline in the lines without RFPL1S | 0.058 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent |
| [[MIR1915HG]] | B | RFPL1S activity raises MIR1915HG's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 2.10× lower at baseline in the lines without RFPL1S | 0.059 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent |
| [[ELFN1]] | B | RFPL1S activity raises ELFN1's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 2.51× lower at baseline in the lines without RFPL1S | 0.077 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent |
| [[RASGEF1A]] | B | RFPL1S activity raises RASGEF1A's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 2.05× lower at baseline in the lines without RFPL1S | 0.079 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent |
| [[ANKS1B]] | B | RFPL1S activity raises ANKS1B's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 2.28× lower at baseline in the lines without RFPL1S | 0.085 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent |
| [[KCNQ2]] | B | RFPL1S activity raises KCNQ2's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 2.30× lower at baseline in the lines without RFPL1S | 0.088 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent |
| [[FBXO15]] | B | RFPL1S activity raises FBXO15's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 1.70× lower at baseline in the lines without RFPL1S | 0.090 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent |
| [[SSPOP]] | B | RFPL1S activity raises SSPOP's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 2.01× lower at baseline in the lines without RFPL1S | 0.0995 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent |
| [[NTN1]] | C | RFPL1S activity raises NTN1's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 3.22× lower at baseline in the lines without RFPL1S | 0.054 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent; co-absent with the target |
| [[TMEM150C]] | C | RFPL1S activity raises TMEM150C's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 2.46× lower at baseline in the lines without RFPL1S | 0.056 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.7, 36.9); signed map (25.1, 25.2). **Vector** length 38.0, 6.62% of its response variance represented; |z| ≥ 3 in 578 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +20.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +6.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +1.8 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.6 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.2 | -3.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -2.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | RFPL1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 22q12.2 — chr22:29,436,534-29,478,868 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RFPL1-AS, NCRNA00006; previously RFPL1-AS1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:9978](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9978) · Entrez [10740](https://www.ncbi.nlm.nih.gov/gene/10740) · Ensembl [ENSG00000225465](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225465)

## Data

Gene col 13459: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13459); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13459, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13459]; `tensor/DDL_lfc|DDL_z.npy` [13459]; `embed/gene_vectors.npy` [13459]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13459 or target_col == 13459). Every well: [[RFPL1S — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFPL1S.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
