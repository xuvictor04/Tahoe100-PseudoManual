---
symbol: "NTF3"
type: "gene"
col: 11711
ensembl_id: "ENSG00000185652"
name: "neurotrophin 3"
location: "12p13.31"
module: 13
arm: "+"
pooled_cpm: 4.96
n_lines_expressing: 24
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 14
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# NTF3

*neurotrophin 3* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.44× (z +12.3, q 5e-32, up in 12 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.574× (z -5.4, q 3e-05, down in 9 of 22 measured lines) ⚠ cell-cycle shift, explains ~29% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (RPMI-7951 0.0587×, A-172 0.0834×, NCI-H1573 0.0700×, SNU-423 0.108×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RPMI-7951 0.122×, NCI-H1573 0.150×); [[Dinaciclib (drug)]] 5 µM in 2 lines (HS-578T 0.0543×, RPMI-7951 0.121×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.0945×, NCI-H1573 0.154×); [[Harringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.221×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAM7-AS1]] (+0.60, fdr 1e-05), [[NDNF]] (+0.58, fdr 2e-05), [[OR9Q1]] (+0.58, fdr 1e-05); moves opposite to [[HECTD1]] (-0.42, fdr 7e-05), [[PYGB]] (-0.41, fdr 9e-05), [[VPS50]] (-0.41, fdr 2e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[LINC01605]] → it (grade B ⚠); 14 go from it, the strongest it → [[WSCD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11711.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.44×** | +12.3 | 5e-32 | 12/21 (A549, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.97×** | +10.2 | 4e-22 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.74×** | +9.8 | 2e-20 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +9.1 | 1e-17 | 7/19 (H4, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.91×** | +6.3 | 3e-08 | 11/19 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +5.3 | 1e-05 | 2/20 (H4, SNU-423) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +4.8 | 1e-04 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.7 | 2e-04 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +3.3 | 0.057 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Silodosin (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.069 | 3/17 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.075 | 3/18 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.076 | 5/21 (SW480, NCI-H23, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11711.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (RPMI-7951 0.0587×, A-172 0.0834×, NCI-H1573 0.0700×, SNU-423 0.108×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RPMI-7951 0.122×, NCI-H1573 0.150×); [[Dinaciclib (drug)]] 5 µM in 2 lines (HS-578T 0.0543×, RPMI-7951 0.121×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.0945×, NCI-H1573 0.154×); [[Harringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.221×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.574×** | -5.4 | 3e-05 | 9/22 (NCI-H1573, RPMI-7951, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.718× | -3.2 | 0.34 | 3/20 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | 0.547× | -3.1 | 0.39 | 3/20 (LS 180, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11711. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 68.9 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -16.8) |
| [[NCI-H1573 (line)]] | alt | 30.8 | 0 | 7 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0288× (z -16.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.150× (z -12.6) |
| [[HS-578T (line)]] | alt | 18.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0543× (z -14.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 17.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0650× (z -14.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 23.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -12.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 13.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0834× (z -12.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 5.29 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.129× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.718 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.958 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.773 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.942 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.485 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.927 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.703 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.581 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.955 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.715 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.805 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.955 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.676 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11711), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM7-AS1]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[NDNF]] | +0.58 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[OR9Q1]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[GRIK4]] | +0.58 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[ICAM5]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[LINC01411]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[SYNDIG1]] | +0.54 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[GSDME]] | +0.53 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[CYP26B1]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[CRTAC1]] | +0.53 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[SYT7]] | +0.50 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[SLC24A3]] | +0.50 | +0.59 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HECTD1]] | -0.42 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[PYGB]] | -0.41 | -0.41 / -0.37 | both halves | 9e-05 |  |
| [[VPS50]] | -0.41 | -0.32 / -0.40 | both halves | 2e-04 | pathway: HALLMARK_KRAS_SIGNALING_DN |
| [[DIP2B]] | -0.41 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[CEP20]] | -0.40 | -0.44 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 1, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01605]] | B | LINC01605 activity raises NTF3's level | lines that do not express LINC01605 (27) vs lines expressing it (23) | 1.82× lower at baseline in the lines without LINC01605 | 0.077 | ⚠ within organs, on part of the lines; also absent: LINC00460, LINC01133, PTPRR |
| [[SYNDIG1]] | C | SYNDIG1 activity raises NTF3's level | lines that do not express SYNDIG1 (32) vs lines expressing it (18) | 3.73× lower at baseline in the lines without SYNDIG1 | 0.012 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1; co-absent with the target |
| [[FRMPD4]] | C | FRMPD4 activity raises NTF3's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 3.43× lower at baseline in the lines without FRMPD4 | 0.013 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3; co-absent with the target |
| [[ABI3BP]] | C | ABI3BP activity raises NTF3's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 3.51× lower at baseline in the lines without ABI3BP | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; co-absent with the target |
| [[OR9Q1]] | C | OR9Q1 activity raises NTF3's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 3.15× lower at baseline in the lines without OR9Q1 | 0.032 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises NTF3's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 4.55× lower at baseline in the lines without APCDD1L | 0.034 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[LINC01905]] | C | LINC01905 activity raises NTF3's level | lines that do not express LINC01905 (35) vs lines expressing it (15) | 3.15× lower at baseline in the lines without LINC01905 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000267327, ENSG00000267284, SLC25A24P1; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises NTF3's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 4.24× lower at baseline in the lines without LINC01411 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[ADAM7-AS1]] | C | ADAM7-AS1 activity raises NTF3's level | lines that do not express ADAM7-AS1 (23) vs lines expressing it (27) | 2.46× lower at baseline in the lines without ADAM7-AS1 | 0.064 | ⚠ within organs, on part of the lines; also absent: SETBP1, KCNMA1, STC1; maybe low, not absent; co-absent with the target |
| [[MME]] | C | MME activity raises NTF3's level | lines that do not express MME (30) vs lines expressing it (20) | 3.71× lower at baseline in the lines without MME | 0.067 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC; co-absent with the target |
| [[STAC]] | C | STAC activity raises NTF3's level | lines that do not express STAC (25) vs lines expressing it (25) | 2.49× lower at baseline in the lines without STAC | 0.083 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 4, C 10. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WSCD1]] | B | NTF3 activity raises WSCD1's level | lines that do not express NTF3 (26) vs lines expressing it (24) | 1.54× lower at baseline in the lines without NTF3 | 0.044 | ⚠ within organs, on part of the lines; also absent: COL4A1, MME, HS3ST3A1 |
| [[HMGN2P46]] | B | NTF3 activity raises HMGN2P46's level | lines that do not express NTF3 (26) vs lines expressing it (24) | 2.98× lower at baseline in the lines without NTF3 | 0.048 | ⚠ within organs, on part of the lines; also absent: COL4A1, MME, HS3ST3A1 |
| [[LRIG1]] | B | NTF3 activity raises LRIG1's level | lines that do not express NTF3 (26) vs lines expressing it (24) | 1.95× lower at baseline in the lines without NTF3 | 0.069 | ⚠ within organs, on part of the lines; also absent: COL4A1, MME, HS3ST3A1 |
| [[LINC01119]] | B | NTF3 activity raises LINC01119's level | lines that do not express NTF3 (26) vs lines expressing it (24) | 1.94× lower at baseline in the lines without NTF3 | 0.073 | ⚠ within organs, on part of the lines; also absent: COL4A1, MME, HS3ST3A1 |
| [[GDNF-AS1]] | C | NTF3 activity raises GDNF-AS1's level | lines that do not express NTF3 (26) vs lines expressing it (24) | 2.15× lower at baseline in the lines without NTF3 | 0.022 | ⚠ within organs, on part of the lines; also absent: COL4A1, MME, HS3ST3A1; co-absent with the target |
| [[ADAM7-AS1]] | C | NTF3 activity raises ADAM7-AS1's level | lines that do not express NTF3 (26) vs lines expressing it (24) | 3.02× lower at baseline in the lines without NTF3 | 0.025 | ⚠ within organs, on part of the lines; also absent: COL4A1, MME, HS3ST3A1; co-absent with the target |
| [[CA12]] | C | NTF3 activity raises CA12's level | lines that do not express NTF3 (26) vs lines expressing it (24) | 3.62× lower at baseline in the lines without NTF3 | 0.038 | ⚠ within organs, on part of the lines; also absent: COL4A1, MME, HS3ST3A1; co-absent with the target |
| [[MME]] | C | NTF3 activity raises MME's level | lines that do not express NTF3 (26) vs lines expressing it (24) | 5.74× lower at baseline in the lines without NTF3 | 0.049 | ⚠ within organs, on part of the lines; also absent: COL4A1, MME, HS3ST3A1; co-absent with the target |
| [[LINC01411]] | C | NTF3 activity raises LINC01411's level | lines that do not express NTF3 (26) vs lines expressing it (24) | 4.01× lower at baseline in the lines without NTF3 | 0.053 | ⚠ within organs, on part of the lines; also absent: COL4A1, MME, HS3ST3A1; co-absent with the target |
| [[OR9Q1]] | C | NTF3 activity raises OR9Q1's level | lines that do not express NTF3 (26) vs lines expressing it (24) | 2.93× lower at baseline in the lines without NTF3 | 0.055 | ⚠ within organs, on part of the lines; also absent: COL4A1, MME, HS3ST3A1; co-absent with the target |
| [[OR4F15]] | C | NTF3 activity raises OR4F15's level | lines that do not express NTF3 (26) vs lines expressing it (24) | 1.73× lower at baseline in the lines without NTF3 | 0.057 | ⚠ within organs, on part of the lines; also absent: COL4A1, MME, HS3ST3A1; co-absent with the target |
| [[FRMPD4]] | C | NTF3 activity raises FRMPD4's level | lines that do not express NTF3 (26) vs lines expressing it (24) | 3.53× lower at baseline in the lines without NTF3 | 0.060 | ⚠ within organs, on part of the lines; also absent: COL4A1, MME, HS3ST3A1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.480). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.8, 19.5); signed map (29.6, 45.1). **Vector** length 43.7, 8.80% of its response variance represented; |z| ≥ 3 in 521 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +12.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | -1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +3.2 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | neurotrophin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:5,432,108-5,521,536 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NGF2 |
| Gene groups (HGNC) | Neurotrophins |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 14 pathways, smallest: Activated NTRK3 signals through PLCG1; Activated NTRK3 signals through PI3K; Activated NTRK3 signals through RAS |
| Matched by | ensembl_id |

**Function**, from UniProt [P20783](https://www.uniprot.org/uniprotkb/P20783) (Neurotrophin-3):

> Seems to promote the survival of visceral and proprioceptive sensory neurons.

**Summary**, from NCBI Gene [4908](https://www.ncbi.nlm.nih.gov/gene/4908):

> The protein encoded by this gene is a member of the neurotrophin family, that controls survival and differentiation of mammalian neurons. This protein is closely related to both nerve growth factor and brain-derived neurotrophic factor. It may be involved in the maintenance of the adult nervous system, and may affect development of neurons in the embryo when it is expressed in human placenta. NTF3-deficient mice generated by gene targeting display severe movement defects of the limbs. The …

**Accessions** — [HGNC:8023](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8023) · Entrez [4908](https://www.ncbi.nlm.nih.gov/gene/4908) · UniProt [P20783](https://www.uniprot.org/uniprotkb/P20783) · Ensembl [ENSG00000185652](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185652)

## Data

Gene col 11711: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11711); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11711, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11711]; `tensor/DDL_lfc|DDL_z.npy` [11711]; `embed/gene_vectors.npy` [11711]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11711 or target_col == 11711). Every well: [[NTF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NTF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
