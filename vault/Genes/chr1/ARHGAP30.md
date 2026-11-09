---
symbol: "ARHGAP30"
type: "gene"
col: 11825
ensembl_id: "ENSG00000186517"
name: "Rho GTPase activating protein 30"
location: "1q23.3"
module: 8
arm: "+"
pooled_cpm: 6.2
n_lines_expressing: 28
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 50
direction_downstream: 93
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ARHGAP30

*Rho GTPase activating protein 30* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 3.13× (z +10.1, q 5e-21, up in 4 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.93× (z +8.9, q 1e-16, up in 6 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (COLO 205 0.0213×, HT-29 0.0890×, BT-474 0.161×, NCI-H1573 0.184×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (Hs 766T 0.108×, COLO 205 0.162×, HT-29 0.162×); [[Digitoxin (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.108×, BT-474 0.121×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NECTIN4]] (+0.79, fdr 7e-06, ⚠ same locus), [[ADCY4]] (+0.72, fdr 7e-06), [[FAM83E]] (+0.70, fdr 7e-06), [[RINL]] (+0.70, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 50 arrows point to it, the strongest [[SLC28A3]] → it (grade B ⚠); 93 go from it, the strongest it → [[JUP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11825.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.13×** | +10.1 | 5e-21 | 4/9 (NCI-H460, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +9.7 | 5e-20 | 3/11 (NCI-H460, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +8.9 | 1e-16 | 6/24 (NCI-H2030, C32, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.50×** | +8.4 | 8e-15 | 1/6 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.02×** | +6.7 | 2e-09 | 5/25 (A-172, C32, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +5.4 | 6e-06 | 5/15 (NCI-H460, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +5.3 | 8e-06 | 6/25 (LoVo, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.79×** | +5.1 | 2e-05 | 0/6 | top dose only | noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.69×** | +5.0 | 4e-05 | 10/24 (A-172, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.4 | 7e-04 | 8/26 (AsPC-1, HCT15, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.005 | 6/26 (NCI-H460, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.7 | 0.012 | 1/18 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.027 | 5/26 (A549, LoVo, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.58×** | +3.1 | 0.069 | 1/12 (NCI-H2347) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.069 | 3/24 (COLO 205, BT-474, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.0 | 0.085 | 2/24 (NCI-H2347, A549) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.085 | 9/22 (NCI-H460, A-172, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.40×** | +3.0 | 0.090 | 2/17 (LoVo, Hs 766T) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +3.0 | 0.090 | 1/18 (NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11825.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (COLO 205 0.0213×, HT-29 0.0890×, BT-474 0.161×, NCI-H1573 0.184×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (Hs 766T 0.108×, COLO 205 0.162×, HT-29 0.162×); [[Digitoxin (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.108×, BT-474 0.121×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.694× | -3.5 | 0.14 | 10/26 (NCI-H1573, AsPC-1, …) | two highest doses |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | 0.685× | -3.5 | 0.14 | 10/24 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.722× | -3.1 | 0.34 | 10/26 (NCI-H1573, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11825. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 32.5 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -13.0) |
| [[Hs 766T (line)]] | wt | 71.0 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -19.2) |
| [[HT-29 (line)]] | alt | 12.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0890× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 12.6 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -11.9) |
| [[BT-474 (line)]] | alt | 23.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0279× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.161× (z -14.0) |
| [[COLO 205 (line)]] | alt | 34.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0213× (z -29.1) |
| [[LS 180 (line)]] | wt | 9.21 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -10.8) |
| [[LoVo (line)]] | wt | 3.72 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +8.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0732× (z -9.0) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 6.21 | 0 | 2 | — | [[Trametinib (drug)]] 0.05 µM 0.115× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 3.60 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 14.7× (z +8.8) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.981 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.905 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.772 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.846 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.956 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11825), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NECTIN4]] | +0.79 | +0.77 / +0.76 | both halves | 7e-06 | ⚠ same locus (1.0 kb, same strand: neighbours can correlate without regulation) |
| [[ADCY4]] | +0.72 | +0.69 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[FAM83E]] | +0.70 | +0.74 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[RINL]] | +0.70 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[MROH3P]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[ADGRF1]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[CLDN4]] | +0.63 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[SLC28A3]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[ST8SIA6]] | +0.62 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[KPNA7]] | +0.62 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[TMEM45B]] | +0.61 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[KCNK1]] | +0.61 | +0.56 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*50 arrows, 50 of them with an alert ⚠; grade A 0, B 14, C 36. Shown: the 12 strongest; 38 more arrows (38 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC28A3]] | B | SLC28A3 activity raises ARHGAP30's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 2.53× lower at baseline in the lines without SLC28A3 | 0.003 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[BICDL2]] | B | BICDL2 activity raises ARHGAP30's level | lines that do not express BICDL2 (22) vs lines expressing it (28) | 2.15× lower at baseline in the lines without BICDL2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent |
| [[FUT3]] | B | FUT3 activity raises ARHGAP30's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 2.28× lower at baseline in the lines without FUT3 | 0.016 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[NSUN7]] | B | NSUN7 activity weakens ARHGAP30's drug response | lines that do not express NSUN7 (13) vs lines expressing it (13) | (z diff -3.24); strongest at Homoharringtonine 5 µM: 2.25x vs 0.27x (z diff -9.3) | 0.016 | ⚠ within organs, on part of the lines; also absent: NEBL, KIF1A, FRMPD3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises ARHGAP30's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.48× lower at baseline in the lines without ELF3-AS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[JUP]] | B | JUP activity raises ARHGAP30's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.29× lower at baseline in the lines without JUP | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[ADGRF4]] | B | ADGRF4 activity raises ARHGAP30's level | lines that do not express ADGRF4 (23) vs lines expressing it (27) | 2.23× lower at baseline in the lines without ADGRF4 | 0.056 | ⚠ within organs, on part of the lines; also absent: VNN1, PTPRB, PTPRR |
| [[PTPRB]] | B | PTPRB activity raises ARHGAP30's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 2.07× lower at baseline in the lines without PTPRB | 0.059 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[ENKUR]] | B | ENKUR activity raises ARHGAP30's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 1.83× lower at baseline in the lines without ENKUR | 0.071 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[KCNK1]] | B | KCNK1 activity raises ARHGAP30's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 2.26× lower at baseline in the lines without KCNK1 | 0.072 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[BCAS1]] | B | BCAS1 activity raises ARHGAP30's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 2.05× lower at baseline in the lines without BCAS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ |
| [[ATAD3C]] | B | ATAD3C activity raises ARHGAP30's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 2.11× lower at baseline in the lines without ATAD3C | 0.092 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |

### Downstream of this gene

*93 arrows, 93 of them with an alert ⚠; grade A 0, B 51, C 42. Shown: the 12 strongest; 81 more arrows (81 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JUP]] | B | ARHGAP30 activity raises JUP's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 3.45× lower at baseline in the lines without ARHGAP30 | 0.002 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[ELF3-AS1]] | B | ARHGAP30 activity raises ELF3-AS1's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 2.69× lower at baseline in the lines without ARHGAP30 | 0.002 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[ELMO3]] | B | ARHGAP30 activity raises ELMO3's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 2.02× lower at baseline in the lines without ARHGAP30 | 0.006 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[BICDL2]] | B | ARHGAP30 activity raises BICDL2's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 2.66× lower at baseline in the lines without ARHGAP30 | 0.006 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[DSG2-AS1]] | B | ARHGAP30 activity raises DSG2-AS1's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 1.29× lower at baseline in the lines without ARHGAP30 | 0.006 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[MYH14]] | B | ARHGAP30 activity raises MYH14's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 3.17× lower at baseline in the lines without ARHGAP30 | 0.006 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[LINC01504]] | B | ARHGAP30 activity raises LINC01504's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 1.44× lower at baseline in the lines without ARHGAP30 | 0.007 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[KPNA7]] | B | ARHGAP30 activity raises KPNA7's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 2.41× lower at baseline in the lines without ARHGAP30 | 0.008 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[MAL2-AS1]] | B | ARHGAP30 activity raises MAL2-AS1's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 1.29× lower at baseline in the lines without ARHGAP30 | 0.008 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[TMC4]] | B | ARHGAP30 activity raises TMC4's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 2.53× lower at baseline in the lines without ARHGAP30 | 0.013 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[SRMS]] | B | ARHGAP30 activity raises SRMS's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 1.84× lower at baseline in the lines without ARHGAP30 | 0.017 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[PTK6]] | B | ARHGAP30 activity raises PTK6's level | lines that do not express ARHGAP30 (22) vs lines expressing it (28) | 2.52× lower at baseline in the lines without ARHGAP30 | 0.021 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.590). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.1, 56.0); signed map (57.7, 6.5). **Vector** length 69.7, 17.2% of its response variance represented; |z| ≥ 3 in 746 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +8.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +6.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +3.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +5.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +2.4 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -1.8 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -3.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.8 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -2.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 30 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:161,046,946-161,069,970 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00267 |
| Gene groups (HGNC) | Rho GTPase activating proteins |
| Reactome | 7 pathways, smallest: RHOU GTPase cycle; RHOA GTPase cycle; CDC42 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6I6](https://www.uniprot.org/uniprotkb/Q7Z6I6) (Rho GTPase-activating protein 30):

> GTPase-activating protein (GAP) for RAC1 and RHOA, but not for CDC42.

**Summary**, from NCBI Gene [257106](https://www.ncbi.nlm.nih.gov/gene/257106):

> Enables GTPase activator activity. Involved in negative regulation of Rho protein signal transduction. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27414](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27414) · Entrez [257106](https://www.ncbi.nlm.nih.gov/gene/257106) · UniProt [Q7Z6I6](https://www.uniprot.org/uniprotkb/Q7Z6I6) · Ensembl [ENSG00000186517](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186517)

## Data

Gene col 11825: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11825); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11825, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11825]; `tensor/DDL_lfc|DDL_z.npy` [11825]; `embed/gene_vectors.npy` [11825]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11825 or target_col == 11825). Every well: [[ARHGAP30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
