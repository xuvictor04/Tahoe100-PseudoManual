---
symbol: "CTSE"
type: "gene"
col: 12150
ensembl_id: "ENSG00000196188"
name: "cathepsin E"
location: "1q32.1"
module: 73
arm: "+"
pooled_cpm: 3.01
n_lines_expressing: 8
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 14
direction_downstream: 30
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# CTSE

*cathepsin E* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 9.61× (z +10.7, q 7e-24, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.89× (z +9.4, q 9e-19, up in 0 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LS 180 0.0562×, KATO III 0.181×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (KATO III 0.129×; ⚠ cell-cycle shift, explains ~31% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[REG4]] (+0.86, fdr 7e-06), [[TPTEP1-1]] (+0.75, fdr 8e-06), [[MUC2]] (+0.74, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[MUC2]] → it (grade C ⚠); 30 go from it, the strongest it → [[VILL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12150.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.61×** | +10.7 | 7e-24 | 1/1 (KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **8.67×** | +10.6 | 8e-24 | 2/2 (KATO III, LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.89×** | +9.4 | 9e-19 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.80×** | +9.3 | 3e-18 | 2/6 (Panc 03.27, HEC-1-A) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.41×** | +8.4 | 4e-15 | 1/2 (KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **3.34×** | +5.9 | 3e-07 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.02×** | +4.9 | 9e-05 | 0/7 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.61×** | +4.7 | 2e-04 | 0/5 | top dose only | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.61×** | +4.5 | 4e-04 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **5.24×** | +4.2 | 0.001 | 1/1 (LoVo) | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.44×** | +4.2 | 0.001 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.31×** | +4.1 | 0.002 | 0/4 | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.71×** | +3.7 | 0.009 | 4/7 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +3.6 | 0.015 | 0/4 | top dose only | cell-cycle shift (explains ~16% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.62×** | +3.3 | 0.032 | 0/6 | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +3.3 | 0.038 | 0/5 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.94×** | +3.2 | 0.040 | 0/5 | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.02×** | +3.1 | 0.050 | 0/4 | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.85×** | +2.9 | 0.094 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12150.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LS 180 0.0562×, KATO III 0.181×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (KATO III 0.129×; ⚠ cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[XRK3F2 (drug)]] 5 µM |  | 0.303× | -3.1 | 0.38 | 2/6 (Panc 03.27, LoVo) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.527× | -3.1 | 0.38 | 0/7 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12150. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 103 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -11.0) |
| [[LS 180 (line)]] | wt | 8.98 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0562× (z -15.2) |
| [[A-172 (line)]] | wt | 0.229 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.185 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.197 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.175 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.210 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.165 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.186 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.583 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.211 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.174 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.291 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.200 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.179 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.217 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.169 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.179 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.150 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.183 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.153 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.171 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[NCI-H23 (line)]] | alt | 0.175 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.313 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.180 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.165 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.172 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.179 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.171 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.834 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.257 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.182 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.202 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.166 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12150), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REG4]] | +0.86 | +0.86 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[TPTEP1-1]] | +0.75 | +0.79 / +0.58 | both halves | 8e-06 |  |
| [[MUC2]] | +0.74 | +0.72 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[KLK10]] | +0.72 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[SPON1]] | +0.72 | +0.64 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[GPA33]] | +0.72 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[LINC01819]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[FAM3D]] | +0.71 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[TFF2]] | +0.70 | +0.69 / +0.66 | both halves | 7e-06 | STRING 421 |
| [[DSG4]] | +0.69 | +0.75 / +0.43 | both halves | 3e-05 |  |
| [[PPP1R1B]] | +0.69 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[NPSR1]] | +0.69 | +0.71 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 0, C 14. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC2]] | C | MUC2 activity raises CTSE's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 1.94× lower at baseline in the lines without MUC2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; co-absent with the target |
| [[MUC6]] | C | MUC6 activity raises CTSE's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 1.44× lower at baseline in the lines without MUC6 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[CFTR]] | C | CFTR activity raises CTSE's level | lines that do not express CFTR (39) vs lines expressing it (11) | 2.75× lower at baseline in the lines without CFTR | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent; co-absent with the target |
| [[LINC02474]] | C | LINC02474 activity raises CTSE's level | lines that do not express LINC02474 (40) vs lines expressing it (10) | 2.89× lower at baseline in the lines without LINC02474 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC4, SFTPA2, ENSG00000230975; co-absent with the target |
| [[XACT]] | C | XACT activity raises CTSE's level | lines that do not express XACT (30) vs lines expressing it (20) | 1.53× lower at baseline in the lines without XACT | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438; co-absent with the target |
| [[SPON1]] | C | SPON1 activity raises CTSE's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 1.59× lower at baseline in the lines without SPON1 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A; co-absent with the target |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises CTSE's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 2.33× lower at baseline in the lines without ST6GALNAC1 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |
| [[DSG4]] | C | DSG4 activity raises CTSE's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 2.01× lower at baseline in the lines without DSG4 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031; co-absent with the target |
| [[UGT1A1]] | C | UGT1A1 activity raises CTSE's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 2.12× lower at baseline in the lines without UGT1A1 | 0.086 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; co-absent with the target |
| [[FAM3D]] | C | FAM3D activity raises CTSE's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 1.70× lower at baseline in the lines without FAM3D | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent; co-absent with the target |
| [[PADI1]] | C | PADI1 activity raises CTSE's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 1.38× lower at baseline in the lines without PADI1 | 0.089 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3; co-absent with the target |
| [[CADPS]] | C | CADPS activity raises CTSE's level | lines that do not express CADPS (39) vs lines expressing it (11) | 1.35× lower at baseline in the lines without CADPS | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, TYR; co-absent with the target |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 7, C 23. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VILL]] | B | CTSE activity raises VILL's level | lines that do not express CTSE (42) vs lines expressing it (8) | 3.19× lower at baseline in the lines without CTSE | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, REG4, CFTR |
| [[ADAP1]] | B | CTSE activity raises ADAP1's level | lines that do not express CTSE (42) vs lines expressing it (8) | 2.71× lower at baseline in the lines without CTSE | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, REG4, CFTR |
| [[TMEM229B]] | B | CTSE activity raises TMEM229B's level | lines that do not express CTSE (42) vs lines expressing it (8) | 2.19× lower at baseline in the lines without CTSE | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, REG4, CFTR |
| [[HTR1D]] | B | CTSE activity raises HTR1D's level | lines that do not express CTSE (42) vs lines expressing it (8) | 1.71× lower at baseline in the lines without CTSE | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, REG4, CFTR |
| [[SEPTIN9-DT]] | B | CTSE activity raises SEPTIN9-DT's level | lines that do not express CTSE (42) vs lines expressing it (8) | 2.24× lower at baseline in the lines without CTSE | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, REG4, CFTR |
| [[KRT18]] | B | CTSE activity raises KRT18's level | lines that do not express CTSE (42) vs lines expressing it (8) | 3.74× lower at baseline in the lines without CTSE | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, REG4, CFTR |
| [[NOSTRIN]] | B | CTSE activity raises NOSTRIN's level | lines that do not express CTSE (42) vs lines expressing it (8) | 3.50× lower at baseline in the lines without CTSE | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, REG4, CFTR |
| [[CFTR]] | C | CTSE activity raises CFTR's level | lines that do not express CTSE (42) vs lines expressing it (8) | 6.18× lower at baseline in the lines without CTSE | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, REG4, CFTR; co-absent with the target |
| [[MUC2]] | C | CTSE activity raises MUC2's level | lines that do not express CTSE (42) vs lines expressing it (8) | 4.02× lower at baseline in the lines without CTSE | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, REG4, CFTR; co-absent with the target |
| [[HEPH]] | C | CTSE activity raises HEPH's level | lines that do not express CTSE (42) vs lines expressing it (8) | 5.77× lower at baseline in the lines without CTSE | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, REG4, CFTR; co-absent with the target |
| [[IL1R2]] | C | CTSE activity raises IL1R2's level | lines that do not express CTSE (42) vs lines expressing it (8) | 3.02× lower at baseline in the lines without CTSE | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, REG4, CFTR; co-absent with the target |
| [[FAM3D]] | C | CTSE activity raises FAM3D's level | lines that do not express CTSE (42) vs lines expressing it (8) | 3.32× lower at baseline in the lines without CTSE | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, REG4, CFTR; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.820). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.1, 50.0); signed map (66.6, 9.1). **Vector** length 26.9, 11.3% of its response variance represented; |z| ≥ 3 in 149 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.6 | +8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.4 | +0.4 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +0.4 | +0.7 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +0.4 | +0.5 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.8 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.7 | +0.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.6 | -2.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.6 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | cathepsin E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:206,008,535-206,023,909 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cathepsins; Peptidase family A1 |
| Hallmark sets | COAGULATION, HEME_METABOLISM |
| Reactome | 5 pathways, smallest: Processing of antigen in germinal center B cells; MHC class II antigen presentation; Affinity selection of immunoglobulins |
| Matched by | ensembl_id |

**Function**, from UniProt [P14091](https://www.uniprot.org/uniprotkb/P14091) (Cathepsin E):

> May have a role in immune function. Probably involved in the processing of antigenic peptides during MHC class II-mediated antigen presentation. May play a role in activation-induced lymphocyte depletion in the thymus, and in neuronal degeneration and glial cell activation in the brain.

**Summary**, from NCBI Gene [1510](https://www.ncbi.nlm.nih.gov/gene/1510):

> This gene encodes a member of the A1 family of peptidases. Alternative splicing of this gene results in multiple transcript variants. At least one of these variants encodes a preproprotein that is proteolytically processed to generate the mature enzyme. This enzyme, an aspartic endopeptidase, may be involved in antigen processing and the maturation of secretory proteins. Elevated expression of this gene has been observed in neurodegeneration. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:2530](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2530) · Entrez [1510](https://www.ncbi.nlm.nih.gov/gene/1510) · UniProt [P14091](https://www.uniprot.org/uniprotkb/P14091) · Ensembl [ENSG00000196188](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196188)

## Data

Gene col 12150: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12150); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12150, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12150]; `tensor/DDL_lfc|DDL_z.npy` [12150]; `embed/gene_vectors.npy` [12150]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12150 or target_col == 12150). Every well: [[CTSE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTSE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
