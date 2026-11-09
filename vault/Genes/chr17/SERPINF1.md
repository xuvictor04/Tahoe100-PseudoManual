---
symbol: "SERPINF1"
type: "gene"
col: 5311
ensembl_id: "ENSG00000132386"
name: "serpin family F member 1"
location: "17p13.3"
module: 27
arm: "+"
pooled_cpm: 3.27
n_lines_expressing: 21
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 32
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# SERPINF1

*serpin family F member 1* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.81× (z +10.9, q 5e-25, up in 8 of 12 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HepG2/C3A 0.298×, SHP-77 0.268×; ⚠ cell-cycle shift, would explain all of this change); [[Bortezomib (drug)]] 5 µM in 1 line (SW480 0.0375×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.170×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JAKMIP2-AS1]] (+0.67, fdr 2e-04), [[FGF20]] (+0.65, fdr 4e-05), [[PHYHIPL]] (+0.64, fdr 3e-04); moves opposite to [[MPP3]] (-0.44, fdr 2e-04), [[CLCF1]] (-0.43, fdr 1e-04), [[BICDL1]] (-0.43, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PSD2]] → it (grade B ⚠); 32 go from it, the strongest it → [[FGD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5311.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.81×** | +10.9 | 5e-25 | 8/12 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.11×** | +10.6 | 1e-23 | 5/7 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.03×** | +10.0 | 2e-21 | 3/4 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.98×** | +7.6 | 6e-12 | 5/5 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.31×** | +4.7 | 3e-04 | 2/4 (HepG2/C3A, MIA PaCa-2) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.8 | 0.016 | 2/6 (HepG2/C3A, MIA PaCa-2) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.58×** | +3.4 | 0.052 | 4/11 (HepG2/C3A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.10×** | +3.2 | 0.077 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.10×** | +3.2 | 0.077 | 3/7 (SHP-77, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.079 | 2/15 (MIA PaCa-2, HepG2/C3A) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.079 | 1/17 (HCT15) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.1 | 0.083 | 2/7 (RPMI-7951, MIA PaCa-2) | inconsistent across doses |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 1.50× | +3.0 | 0.11 | 0/10 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5311.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HepG2/C3A 0.298×, SHP-77 0.268×; ⚠ cell-cycle shift, would explain all of this change); [[Bortezomib (drug)]] 5 µM in 1 line (SW480 0.0375×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.170×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Baicalin (drug)]] 5 µM |  | 0.722× | -3.5 | 0.28 | 2/17 (HEC-1-A, Hs 766T) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5311. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 80.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 8.57 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0375× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.782 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.658 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.958 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.594 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.807 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.719 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.669 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.886 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.683 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.806 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.547 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.980 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.640 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.544 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.812 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.648 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.689 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5311), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JAKMIP2-AS1]] | +0.67 | +0.73 / +0.30 | both halves | 2e-04 |  |
| [[FGF20]] | +0.65 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[PHYHIPL]] | +0.64 | +0.64 / +0.28 | both halves | 3e-04 | **novel candidate** |
| [[F10]] | +0.62 | +0.75 / +0.28 | both halves | 3e-04 | STRING 423 |
| [[B3GAT1-DT]] | +0.60 | +0.60 / +0.34 | both halves | 1e-04 |  |
| [[MKX]] | +0.60 | +0.46 / +0.34 | both halves | 1e-04 |  |
| [[RMST]] | +0.60 | +0.71 / +0.22 | both halves | 6e-04 |  |
| [[APCDD1]] | +0.59 | +0.67 / +0.24 | both halves | 5e-04 |  |
| [[NOTUM]] | +0.58 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[SMOC2]] | +0.56 | +0.63 / +0.26 | both halves | 4e-04 |  |
| [[PKHD1]] | +0.56 | +0.61 / +0.26 | both halves | 4e-04 |  |
| [[KRT5]] | +0.55 | +0.57 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP3]] | -0.44 | -0.37 / -0.30 | both halves | 2e-04 |  |
| [[CLCF1]] | -0.43 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[BICDL1]] | -0.43 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[PASD1]] | -0.43 | -0.51 / +0.02 | ⚠ one half (not replicated) | 1.00 |  |
| [[TUBB6]] | -0.42 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[ZNF83]] | -0.42 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[FRMD8]] | -0.41 | -0.33 / -0.28 | both halves | 3e-04 |  |
| [[SETX]] | -0.41 | -0.39 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSD2]] | B | PSD2 activity raises SERPINF1's level | lines that do not express PSD2 (13) vs lines expressing it (37) | 1.97× lower at baseline in the lines without PSD2 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, CACNA1C, SSC5D; maybe low, not absent |
| [[RUNX1T1]] | C | RUNX1T1 activity raises SERPINF1's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 1.94× lower at baseline in the lines without RUNX1T1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[LINC02428]] | C | LINC02428 activity raises SERPINF1's level | lines that do not express LINC02428 (32) vs lines expressing it (18) | 2.22× lower at baseline in the lines without LINC02428 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ENSG00000287598, ENSG00000287474; co-absent with the target |
| [[SLC25A24P1]] | C | SLC25A24P1 activity raises SERPINF1's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 2.09× lower at baseline in the lines without SLC25A24P1 | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2; co-absent with the target |
| [[JAKMIP2-AS1]] | C | JAKMIP2-AS1 activity raises SERPINF1's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 2.35× lower at baseline in the lines without JAKMIP2-AS1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[AXIN2]] | C | AXIN2 activity raises SERPINF1's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 2.12× lower at baseline in the lines without AXIN2 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964; co-absent with the target |
| [[LINC02058]] | C | LINC02058 activity raises SERPINF1's level | lines that do not express LINC02058 (34) vs lines expressing it (16) | 1.36× lower at baseline in the lines without LINC02058 | 0.054 | ⚠ within organs, on part of the lines; also absent: LINC02253, ENSG00000260573, ST18; maybe low, not absent; co-absent with the target |
| [[PHYHIPL]] | C | PHYHIPL activity raises SERPINF1's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 2.82× lower at baseline in the lines without PHYHIPL | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |

### Downstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 12, C 20. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGD3]] | B | SERPINF1 activity raises FGD3's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.57× lower at baseline in the lines without SERPINF1 | 0.007 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[ADGRL3]] | B | SERPINF1 activity raises ADGRL3's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 2.33× lower at baseline in the lines without SERPINF1 | 0.008 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[LINC01980]] | B | SERPINF1 activity raises LINC01980's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.63× lower at baseline in the lines without SERPINF1 | 0.012 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[RHOXF1-AS1]] | B | SERPINF1 activity raises RHOXF1-AS1's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.71× lower at baseline in the lines without SERPINF1 | 0.015 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[SLC7A8]] | B | SERPINF1 activity raises SLC7A8's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.64× lower at baseline in the lines without SERPINF1 | 0.018 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[HS3ST5]] | B | SERPINF1 activity raises HS3ST5's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 2.06× lower at baseline in the lines without SERPINF1 | 0.029 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[LINC01170]] | B | SERPINF1 activity raises LINC01170's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.95× lower at baseline in the lines without SERPINF1 | 0.046 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[CNTNAP2]] | B | SERPINF1 activity raises CNTNAP2's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.57× lower at baseline in the lines without SERPINF1 | 0.060 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[DACH1]] | B | SERPINF1 activity raises DACH1's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.86× lower at baseline in the lines without SERPINF1 | 0.068 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[TNFRSF19]] | B | SERPINF1 activity raises TNFRSF19's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.90× lower at baseline in the lines without SERPINF1 | 0.074 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[PSD2]] | B | SERPINF1 activity raises PSD2's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.39× lower at baseline in the lines without SERPINF1 | 0.088 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[KIF6]] | B | SERPINF1 activity raises KIF6's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.25× lower at baseline in the lines without SERPINF1 | 0.094 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.626). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.8, 42.9); signed map (62.3, 17.4). **Vector** length 19.9, 3.02% of its response variance represented; |z| ≥ 3 in 265 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.7 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.5 | +7.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.0 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.7 | +3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.7 | +1.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.6 | +1.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -1.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.7 | -1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | -0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.6 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.5 | -0.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.5 | +1.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -0.5 | -1.5 |
|  | [[Auranofin (drug)]] 0.5 µM |  | -0.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | serpin family F member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:1,762,029-1,777,565 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EPC-1, PIG35; previously PEDF |
| Gene groups (HGNC) | Serpin peptidase inhibitors |
| Matched by | ensembl_id |

**Function**, from UniProt [P36955](https://www.uniprot.org/uniprotkb/P36955) (Pigment epithelium-derived factor):

> Neurotrophic protein; induces extensive neuronal differentiation in retinoblastoma cells. Potent inhibitor of angiogenesis. As it does not undergo the S (stressed) to R (relaxed) conformational transition characteristic of active serpins, it exhibits no serine protease inhibitory activity.

**Summary**, from NCBI Gene [5176](https://www.ncbi.nlm.nih.gov/gene/5176):

> This gene encodes a member of the serpin family that does not display the serine protease inhibitory activity shown by many of the other serpin proteins. The encoded protein is secreted and strongly inhibits angiogenesis. In addition, this protein is a neurotrophic factor involved in neuronal differentiation in retinoblastoma cells. Mutations in this gene were found in individuals with osteogenesis imperfecta, type VI. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:8824](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8824) · Entrez [5176](https://www.ncbi.nlm.nih.gov/gene/5176) · UniProt [P36955](https://www.uniprot.org/uniprotkb/P36955) · Ensembl [ENSG00000132386](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132386)

## Data

Gene col 5311: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5311); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5311, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5311]; `tensor/DDL_lfc|DDL_z.npy` [5311]; `embed/gene_vectors.npy` [5311]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5311 or target_col == 5311). Every well: [[SERPINF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPINF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
