---
symbol: "ST6GAL2"
type: "gene"
col: 6841
ensembl_id: "ENSG00000144057"
name: "ST6 beta-galactoside alpha-2,6-sialyltransferase 2"
location: "2q12.3"
module: 92
arm: "+"
pooled_cpm: 10.64
n_lines_expressing: 11
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 15
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# ST6GAL2

*ST6 beta-galactoside alpha-2,6-sialyltransferase 2* — 2q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.17× (z +10.3, q 6e-22, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.72× (z +5.7, q 2e-06, up in 6 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LoVo 0.192×, A549 0.133×, NCI-H1573 0.168×, SW 900 0.155×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A549 0.0972×, NCI-H1573 0.182×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (A549 0.133×, NCI-H1573 0.135×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LoVo 0.218×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMOC1]] (+0.58, fdr 1e-05), [[NR2E3]] (+0.57, fdr 1e-05), [[XDH]] (+0.56, fdr 2e-05); moves opposite to [[ALDH2]] (-0.41, fdr 1e-04).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LINC02582]] → it (grade C ⚠); 15 go from it, the strongest it → [[CEMIP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6841.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.17×** | +10.3 | 6e-22 | 2/5 (NCI-H1573, CHP-212) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.83×** | +10.0 | 3e-21 | 2/9 (RPMI-7951, CHP-212) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.51×** | +8.7 | 8e-16 | 2/7 (CHP-212, SHP-77) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +5.7 | 2e-06 | 6/9 (HEC-1-A, RPMI-7951, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.99×** | +5.1 | 3e-05 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +4.9 | 9e-05 | 1/9 (RPMI-7951) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +4.3 | 0.002 | 0/9 | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.09×** | +3.9 | 0.006 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.64×** | +3.7 | 0.013 | 2/9 (LoVo, RPMI-7951) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.3 | 0.055 | 1/9 (BT-474) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.1 | 0.086 | 1/8 (CHP-212) | top dose only | cell-cycle shift (explains ~21% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6841.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LoVo 0.192×, A549 0.133×, NCI-H1573 0.168×, SW 900 0.155×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A549 0.0972×, NCI-H1573 0.182×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (A549 0.133×, NCI-H1573 0.135×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LoVo 0.218×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (drug)]] 0.05 µM |  | 0.629× | -3.2 | 0.27 | 0/9 | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | 0.647× | -3.1 | 0.27 | 5/9 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.659× | -3.1 | 0.27 | 0/9 | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.640× | -3.1 | 0.27 | 0/9 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6841. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 111 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 29.3 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -11.2) |
| [[A549 (line)]] | wt | 180 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0972× (z -14.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -12.8) |
| [[CHP-212 (line)]] | wt | 43.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0613× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[SW 900 (line)]] | alt | 25.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -9.8) |
| [[A-172 (line)]] | wt | 0.903 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.850 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.683 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.885 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.973 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.896 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.916 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.659 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.913 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.824 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.937 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.872 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.846 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.965 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.845 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.776 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6841), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMOC1]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[NR2E3]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[XDH]] | +0.56 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[GPR141]] | +0.56 | +0.59 / +0.40 | both halves | 4e-05 | **novel candidate** |
| [[LAMA3]] | +0.55 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[TARID]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ABCC3]] | +0.53 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[CYP24A1]] | +0.52 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[CEMIP]] | +0.52 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[DUSP4]] | +0.52 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[COL4A3]] | +0.51 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[IL33]] | +0.51 | +0.42 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH2]] | -0.41 | -0.34 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02582]] | C | LINC02582 activity raises ST6GAL2's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 3.15× lower at baseline in the lines without LINC02582 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |
| [[XACT]] | C | XACT activity raises ST6GAL2's level | lines that do not express XACT (30) vs lines expressing it (20) | 2.12× lower at baseline in the lines without XACT | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438; co-absent with the target |
| [[COL4A4]] | C | COL4A4 activity raises ST6GAL2's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 2.06× lower at baseline in the lines without COL4A4 | 0.061 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A; co-absent with the target |
| [[TNS4]] | C | TNS4 activity raises ST6GAL2's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 1.70× lower at baseline in the lines without TNS4 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6; co-absent with the target |
| [[GPRIN3]] | C | GPRIN3 activity raises ST6GAL2's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 2.99× lower at baseline in the lines without GPRIN3 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031; co-absent with the target |
| [[IL33]] | C | IL33 activity raises ST6GAL2's level | lines that do not express IL33 (35) vs lines expressing it (15) | 1.95× lower at baseline in the lines without IL33 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01133, MUC2, LINC01411; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 9, C 6. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEMIP]] | B | ST6GAL2 activity raises CEMIP's level | lines that do not express ST6GAL2 (39) vs lines expressing it (11) | 3.43× lower at baseline in the lines without ST6GAL2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC01456, MUC6 |
| [[ABHD17C]] | B | ST6GAL2 activity raises ABHD17C's level | lines that do not express ST6GAL2 (39) vs lines expressing it (11) | 2.64× lower at baseline in the lines without ST6GAL2 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC01456, MUC6 |
| [[ABCC3]] | B | ST6GAL2 activity raises ABCC3's level | lines that do not express ST6GAL2 (39) vs lines expressing it (11) | 2.95× lower at baseline in the lines without ST6GAL2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC01456, MUC6 |
| [[PKP2]] | B | ST6GAL2 activity raises PKP2's level | lines that do not express ST6GAL2 (39) vs lines expressing it (11) | 1.61× lower at baseline in the lines without ST6GAL2 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC01456, MUC6 |
| [[GTF2IP7]] | B | ST6GAL2 activity raises GTF2IP7's level | lines that do not express ST6GAL2 (39) vs lines expressing it (11) | 1.66× lower at baseline in the lines without ST6GAL2 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC01456, MUC6 |
| [[LAMA3]] | B | ST6GAL2 activity raises LAMA3's level | lines that do not express ST6GAL2 (39) vs lines expressing it (11) | 1.74× lower at baseline in the lines without ST6GAL2 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC01456, MUC6 |
| [[DUSP4]] | B | ST6GAL2 activity raises DUSP4's level | lines that do not express ST6GAL2 (39) vs lines expressing it (11) | 2.20× lower at baseline in the lines without ST6GAL2 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC01456, MUC6 |
| [[NOSTRIN]] | B | ST6GAL2 activity raises NOSTRIN's level | lines that do not express ST6GAL2 (39) vs lines expressing it (11) | 1.63× lower at baseline in the lines without ST6GAL2 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC01456, MUC6 |
| [[SIPA1L2]] | B | ST6GAL2 activity raises SIPA1L2's level | lines that do not express ST6GAL2 (39) vs lines expressing it (11) | 2.21× lower at baseline in the lines without ST6GAL2 | 0.0998 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC01456, MUC6 |
| [[LINC01456]] | C | ST6GAL2 activity raises LINC01456's level | lines that do not express ST6GAL2 (39) vs lines expressing it (11) | 5.01× lower at baseline in the lines without ST6GAL2 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC01456, MUC6; co-absent with the target |
| [[XACT]] | C | ST6GAL2 activity raises XACT's level | lines that do not express ST6GAL2 (39) vs lines expressing it (11) | 2.75× lower at baseline in the lines without ST6GAL2 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC01456, MUC6; co-absent with the target |
| [[LINC02582]] | C | ST6GAL2 activity raises LINC02582's level | lines that do not express ST6GAL2 (39) vs lines expressing it (11) | 2.41× lower at baseline in the lines without ST6GAL2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC01456, MUC6; co-absent with the target |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.378). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.8, 46.0); signed map (37.4, 49.5). **Vector** length 39.0, 13.8% of its response variance represented; |z| ≥ 3 in 272 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.0 | +0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +0.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +0.8 | +1.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.5 | -3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -2.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.1 | -1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ST6 beta-galactoside alpha-2,6-sialyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q12.3 — chr2:106,801,600-106,887,108 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1877, St6GalII; previously SIAT2 |
| Gene groups (HGNC) | Sialyltransferases |
| Reactome | 4 pathways, smallest: Sialic acid metabolism; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JF0](https://www.uniprot.org/uniprotkb/Q96JF0) (Beta-galactoside alpha-2,6-sialyltransferase 2):

> Transfers sialic acid from the donor of substrate CMP-sialic acid to galactose containing acceptor substrates. Has alpha-2,6-sialyltransferase activity toward oligosaccharides that have the Gal-beta-1,4-GlcNAc sequence at the non-reducing end of their carbohydrate groups, but it has weak or no activities toward glycoproteins and glycolipids.

**Summary**, from NCBI Gene [84620](https://www.ncbi.nlm.nih.gov/gene/84620):

> This locus encodes a sialyltransferase. The encoded type II transmembrane protein catalyzes the transfer of sialic acid from CMP to an oligosaccharide substrate. Polymorphisms at this locus may be associated with variations in risperidone response in schizophrenic patients. Alternatively spliced transcript variants have been described. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:10861](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10861) · Entrez [84620](https://www.ncbi.nlm.nih.gov/gene/84620) · UniProt [Q96JF0](https://www.uniprot.org/uniprotkb/Q96JF0) · Ensembl [ENSG00000144057](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144057)

## Data

Gene col 6841: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6841); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6841, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6841]; `tensor/DDL_lfc|DDL_z.npy` [6841]; `embed/gene_vectors.npy` [6841]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6841 or target_col == 6841). Every well: [[ST6GAL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST6GAL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
