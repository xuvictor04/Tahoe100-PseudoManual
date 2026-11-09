---
symbol: "SCN2A"
type: "gene"
col: 5877
ensembl_id: "ENSG00000136531"
name: "sodium voltage-gated channel alpha subunit 2"
location: "2q24.3"
module: 9
arm: "+"
pooled_cpm: 3.45
n_lines_expressing: 24
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 4
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SCN2A

*sodium voltage-gated channel alpha subunit 2* — 2q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.37× (z +19.0, q 0e+00, up in 5 of 12 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.0631×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H23 0.133×; ⚠ cell-cycle shift, explains ~27% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.263×); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H23 0.185×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH10]] (+0.69, fdr 7e-06), [[LINC02211]] (+0.68, fdr 7e-06), [[EPHA5-AS1]] (+0.67, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[SCN3A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5877.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.37×** | +19.0 | 0e+00 | 5/12 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.58×** | +11.7 | 5e-29 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.12×** | +10.5 | 2e-23 | 2/5 (NCI-H460, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.46×** | +9.9 | 6e-21 | 2/7 (AsPC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.18×** | +8.8 | 1e-16 | 10/18 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.06×** | +8.2 | 3e-14 | 3/14 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.63×** | +7.7 | 1e-12 | 8/17 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.66×** | +5.7 | 1e-06 | 8/18 (NCI-H23, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.64×** | +5.5 | 2e-06 | 3/18 (A498, C32, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +5.1 | 2e-05 | 1/11 (A498) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +4.5 | 3e-04 | 3/8 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.73×** | +4.4 | 6e-04 | 10/18 (AsPC-1, hTERT-HPNE, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +4.3 | 8e-04 | 4/15 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.66×** | +4.0 | 0.002 | 5/15 (AsPC-1, C32, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.54×** | +4.0 | 0.002 | 5/16 (NCI-H23, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.48×** | +3.9 | 0.003 | 4/17 (AsPC-1, SHP-77, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +3.8 | 0.006 | 4/12 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.63×** | +3.7 | 0.006 | 5/13 (NCI-H23, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5877.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.0631×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H23 0.133×; ⚠ cell-cycle shift, explains ~27% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.263×); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H23 0.185×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Levobupivacaine (hydrochloride) (drug)]] 0.05 µM |  | 0.625× | -3.5 | 0.22 | 0/16 | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.660× | -3.3 | 0.22 | 7/14 (LOX-IMVI, A-172, …) | two highest doses |  |
| [[Dabrafenib (drug)]] 0.05 µM |  | 0.658× | -3.2 | 0.22 | 2/17 (HepG2/C3A, AsPC-1) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.674× | -3.2 | 0.22 | 5/13 (NCI-H23, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5877. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 39.2 | 0 | 7 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0631× (z -15.6) |
| [[A-172 (line)]] | wt | 1.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.6× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 28.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.84× (z +12.3) | — |
| [[A-427 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.821 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.643 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.972 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.899 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.693 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.595 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.650 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.516 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.918 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.661 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.471 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5877), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH10]] | +0.69 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[LINC02211]] | +0.68 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[EPHA5-AS1]] | +0.67 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[FGF14]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 | pathway: Cardiac conduction; STRING 771 |
| [[MAPK10]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[CDH8]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[KCNH5]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CDH12]] | +0.62 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[KCND2]] | +0.62 | +0.60 / +0.50 | both halves | 1e-05 | pathway: Cardiac conduction; STRING 607 |
| [[LINC01122]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[RALYL]] | +0.61 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[FAT3]] | +0.61 | +0.55 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SCN2A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RALYL]] | B | RALYL activity raises SCN2A's level | lines that do not express RALYL (17) vs lines expressing it (33) | 1.85× lower at baseline in the lines without RALYL | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |
| [[CDH10]] | C | CDH10 activity raises SCN2A's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 2.57× lower at baseline in the lines without CDH10 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[MTMR7]] | C | MTMR7 activity raises SCN2A's level | lines that do not express MTMR7 (16) vs lines expressing it (34) | 2.05× lower at baseline in the lines without MTMR7 | 0.047 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent; co-absent with the target |
| [[CDH18]] | C | CDH18 activity raises SCN2A's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 2.07× lower at baseline in the lines without CDH18 | 0.064 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises SCN2A's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 1.85× lower at baseline in the lines without KCNH7 | 0.098 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[CDH12]] | C | CDH12 activity raises SCN2A's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 1.80× lower at baseline in the lines without CDH12 | 0.0995 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCN3A]] | C | SCN2A activity raises SCN3A's level | lines that do not express SCN2A (26) vs lines expressing it (24) | 2.57× lower at baseline in the lines without SCN2A | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTPRN, ENSG00000286251, EDA2R; maybe low, not absent; co-absent with the target |
| [[DMD]] | C | SCN2A activity raises DMD's level | lines that do not express SCN2A (26) vs lines expressing it (24) | 3.72× lower at baseline in the lines without SCN2A | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTPRN, ENSG00000286251, EDA2R; maybe low, not absent; co-absent with the target |
| [[PTCHD4]] | C | SCN2A activity raises PTCHD4's level | lines that do not express SCN2A (26) vs lines expressing it (24) | 4.34× lower at baseline in the lines without SCN2A | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTPRN, ENSG00000286251, EDA2R; maybe low, not absent; co-absent with the target |
| [[CDH10]] | C | SCN2A activity raises CDH10's level | lines that do not express SCN2A (26) vs lines expressing it (24) | 3.53× lower at baseline in the lines without SCN2A | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTPRN, ENSG00000286251, EDA2R; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.1, 32.2); signed map (40.9, 33.5). **Vector** length 34.8, 7.07% of its response variance represented; |z| ≥ 3 in 448 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +19.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +0.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.1 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -0.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | sodium voltage-gated channel alpha subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.3 — chr2:165,194,993-165,392,310 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Nav1.2, HBSCII, HBSCI; previously SCN2A1, SCN2A2 |
| Gene groups (HGNC) | Sodium voltage-gated channel alpha subunits |
| Reactome | 10 pathways, smallest: Sensory perception of sweet, bitter, and umami (glutamate) taste; Sensory perception of taste; Interaction between L1 and Ankyrins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99250](https://www.uniprot.org/uniprotkb/Q99250) (Sodium channel protein type 2 subunit alpha):

> Mediates the voltage-dependent sodium ion permeability of excitable membranes. Assuming opened or closed conformations in response to the voltage difference across the membrane, the protein forms a sodium-selective channel through which Na(+) ions may pass in accordance with their electrochemical gradient. Implicated in the regulation of hippocampal replay occurring within sharp wave ripples (SPW-R) important for memory (By similarity).

**Summary**, from NCBI Gene [6326](https://www.ncbi.nlm.nih.gov/gene/6326):

> Voltage-gated sodium channels are transmembrane glycoprotein complexes composed of a large alpha subunit with four repeat domains, each of which is composed of six membrane-spanning segments, and one or more regulatory beta subunits. Voltage-gated sodium channels function in the generation and propagation of action potentials in neurons and muscle. This gene encodes one member of the sodium channel alpha subunit gene family. Allelic variants of this gene are associated with seizure disorders …

**Accessions** — [HGNC:10588](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10588) · Entrez [6326](https://www.ncbi.nlm.nih.gov/gene/6326) · UniProt [Q99250](https://www.uniprot.org/uniprotkb/Q99250) · Ensembl [ENSG00000136531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136531)

## Data

Gene col 5877: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5877); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5877, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5877]; `tensor/DDL_lfc|DDL_z.npy` [5877]; `embed/gene_vectors.npy` [5877]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5877 or target_col == 5877). Every well: [[SCN2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCN2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
