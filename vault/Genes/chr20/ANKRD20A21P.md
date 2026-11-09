---
symbol: "ANKRD20A21P"
type: "gene"
col: 15885
ensembl_id: "ENSG00000277112"
name: "ankyrin repeat domain 20 family member A21, pseudogene"
location: "20q11.21"
module: 10
arm: "+"
pooled_cpm: 3.37
n_lines_expressing: 20
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 27
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ANKRD20A21P

*ankyrin repeat domain 20 family member A21, pseudogene* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.84× (z +12.3, q 1e-31, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.28× (z +12.1, q 2e-31, up in 6 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.586× (z -3.9, q 0.063, down in 7 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (PANC-1 0.113×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.117×; ⚠ cell-cycle shift, explains ~37% of this change); [[Digitoxin (drug)]] 0.05 µM in 1 line (SW480 0.0310×; ⚠ cell-cycle shift, explains ~50% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (PANC-1 0.147×); [[Bortezomib (drug)]] 0.05 µM in 1 line (PANC-1 0.144×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.166×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD20A11P]] (+0.73, fdr 7e-06), [[DDX59-AS1]] (+0.69, fdr 8e-06), [[LINC01569]] (+0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ANKRD20A11P]] → it (grade C ⚠); 27 go from it, the strongest it → [[SGK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15885.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.84×** | +12.3 | 1e-31 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.28×** | +12.1 | 2e-31 | 6/11 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.98×** | +10.0 | 4e-21 | 1/5 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.65×** | +8.6 | 8e-16 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.08×** | +7.5 | 9e-12 | 6/11 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.73×** | +7.0 | 3e-10 | 2/8 (A-427, A549) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.07×** | +5.2 | 1e-05 | 14/18 (NCI-H2030, A-427, …) | rises with dose | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.60×** | +4.9 | 6e-05 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.42×** | +4.6 | 3e-04 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.87×** | +4.5 | 4e-04 | 1/7 (NCI-H2030) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.38×** | +4.5 | 4e-04 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.04×** | +4.2 | 0.001 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +4.0 | 0.002 | 2/11 (A-427, NCI-H2030) | top dose only | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.75×** | +3.8 | 0.005 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +3.8 | 0.006 | 4/11 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.014 | 3/12 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +3.5 | 0.014 | 2/10 (SW480, NCI-H23) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.62×** | +3.5 | 0.014 | 4/14 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.60×** | +3.4 | 0.019 | 8/14 (SK-MEL-2, A549, …) | rises with dose | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.54×** | +3.1 | 0.050 | 0/7 | inconsistent across doses | low cells (technical?) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.54×** | +3.1 | 0.050 | 1/10 (NCI-H2030) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.063 | 1/16 (A549) | top dose only | low cells (technical?); cell-cycle shift (explains ~16% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15885.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (PANC-1 0.113×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.117×; ⚠ cell-cycle shift, explains ~37% of this change); [[Digitoxin (drug)]] 0.05 µM in 1 line (SW480 0.0310×; ⚠ cell-cycle shift, explains ~50% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (PANC-1 0.147×); [[Bortezomib (drug)]] 0.05 µM in 1 line (PANC-1 0.144×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.166×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.586×** | -3.9 | 0.063 | 7/14 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | 0.627× | -3.4 | 0.22 | 3/14 (SW 900, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15885. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 38.5 | 0 | 8 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.113× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.147× (z -12.3) |
| [[A-427 (line)]] | wt | 9.00 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0683× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 1.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 1.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +8.8) | — |
| [[SW480 (line)]] | alt | 2.93 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0310× (z -13.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 0.349 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.324 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.891 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.518 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.505 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.827 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.523 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.285 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.767 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.813 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.335 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15885), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD20A11P]] | +0.73 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[DDX59-AS1]] | +0.69 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[LINC01569]] | +0.66 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[FAM66C]] | +0.65 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[LINC00466]] | +0.65 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[ZFP2]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[NSMCE1-DT]] | +0.63 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[F8]] | +0.63 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[ARL14EP-DT]] | +0.63 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[TMEM9B-AS1]] | +0.63 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[ABCA17P]] | +0.62 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[LMO7-AS1]] | +0.60 | +0.63 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD20A11P]] | C | ANKRD20A11P activity raises ANKRD20A21P's level | lines that do not express ANKRD20A11P (29) vs lines expressing it (21) | 1.82× lower at baseline in the lines without ANKRD20A11P | 0.013 | ⚠ within organs, on part of the lines; also absent: KCNQ2, RBM11, ANKRD20A21P; co-absent with the target |
| [[KLHL14]] | C | KLHL14 activity raises ANKRD20A21P's level | lines that do not express KLHL14 (37) vs lines expressing it (13) | 1.74× lower at baseline in the lines without KLHL14 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55; co-absent with the target |
| [[LRRC36]] | C | LRRC36 activity raises ANKRD20A21P's level | lines that do not express LRRC36 (16) vs lines expressing it (34) | 1.77× lower at baseline in the lines without LRRC36 | 0.079 | ⚠ within organs, on part of the lines; also absent: DANT2, ANKRD20A21P, MTMR8; maybe low, not absent; co-absent with the target |
| [[MIR4500HG]] | C | MIR4500HG activity raises ANKRD20A21P's level | lines that do not express MIR4500HG (29) vs lines expressing it (21) | 1.63× lower at baseline in the lines without MIR4500HG | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000272046, BMP5, SNCA; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 22, C 5. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SGK2]] | B | ANKRD20A21P activity raises SGK2's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.88× lower at baseline in the lines without ANKRD20A21P | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[LINC03036]] | B | ANKRD20A21P activity raises LINC03036's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.39× lower at baseline in the lines without ANKRD20A21P | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[TMEM9B-AS1]] | B | ANKRD20A21P activity raises TMEM9B-AS1's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.81× lower at baseline in the lines without ANKRD20A21P | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[RNPC3-DT]] | B | ANKRD20A21P activity raises RNPC3-DT's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.39× lower at baseline in the lines without ANKRD20A21P | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[PLS3-AS1]] | B | ANKRD20A21P activity raises PLS3-AS1's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.65× lower at baseline in the lines without ANKRD20A21P | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[TESMIN]] | B | ANKRD20A21P activity raises TESMIN's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 2.06× lower at baseline in the lines without ANKRD20A21P | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[LRRC37A3]] | B | ANKRD20A21P activity raises LRRC37A3's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.38× lower at baseline in the lines without ANKRD20A21P | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[LRRIQ3]] | B | ANKRD20A21P activity raises LRRIQ3's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.52× lower at baseline in the lines without ANKRD20A21P | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[AGBL2]] | B | ANKRD20A21P activity raises AGBL2's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.71× lower at baseline in the lines without ANKRD20A21P | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[GCC2-AS1]] | B | ANKRD20A21P activity raises GCC2-AS1's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 1.33× lower at baseline in the lines without ANKRD20A21P | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[THNSL2]] | B | ANKRD20A21P activity raises THNSL2's level | lines that do not express ANKRD20A21P (30) vs lines expressing it (20) | 2.05× lower at baseline in the lines without ANKRD20A21P | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P |
| [[GCAWKR]] | B | ANKRD20A21P activity strengthens GCAWKR's drug response | lines that do not express ANKRD20A21P (15) vs lines expressing it (11) | the lines without ANKRD20A21P respond 0.58× as strongly (z diff +1.41); strongest at Harringtonine 5 µM: 0.39x vs 0.17x (z diff +3.7) | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.5, 30.4); signed map (36.5, -9.0). **Vector** length 39.7, 10.9% of its response variance represented; |z| ≥ 3 in 359 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +10.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +12.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +7.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.1 | +1.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.1 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -1.9 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -1.6 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.6 | +0.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.4 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.9 | -1.8 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.9 | -1.9 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -0.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 20 family member A21, pseudogene |
| Locus type | pseudogene |
| Location | 20q11.21 — chr20:30,656,033-30,723,855 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52329](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52329) · Entrez [102723552](https://www.ncbi.nlm.nih.gov/gene/102723552) · Ensembl [ENSG00000277112](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000277112)

## Data

Gene col 15885: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15885); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15885, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15885]; `tensor/DDL_lfc|DDL_z.npy` [15885]; `embed/gene_vectors.npy` [15885]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15885 or target_col == 15885). Every well: [[ANKRD20A21P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD20A21P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
