---
symbol: "UNC5D"
type: "gene"
col: 8006
ensembl_id: "ENSG00000156687"
name: "unc-5 netrin receptor D"
location: "8p12"
module: 19
arm: "+"
pooled_cpm: 14.41
n_lines_expressing: 14
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 12
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# UNC5D

*unc-5 netrin receptor D* — 8p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.84× (z +12.3, q 4e-32, up in 10 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.110×, NCI-H460 0.119×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.188×); [[Budesonide (drug)]] 0.05 µM in 1 line (NCI-H460 0.145×); [[Triamcinolone (drug)]] 0.5 µM in 1 line (NCI-H460 0.148×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCUBE1]] (+0.74, fdr 7e-06), [[SMOC1]] (+0.73, fdr 1e-05), [[SERPIND1]] (+0.72, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NCKAP5-AS2]] → it (grade C ⚠); 12 go from it, the strongest it → [[SLC16A4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8006.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.84×** | +12.3 | 4e-32 | 10/11 (HS-578T, H4, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.72×** | +11.8 | 8e-30 | 2/10 (HS-578T, SK-MEL-2) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.69×** | +10.5 | 2e-23 | 1/5 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.14×** | +9.6 | 2e-19 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.21×** | +6.6 | 4e-09 | 10/10 (H4, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.73×** | +6.5 | 8e-09 | 5/9 (SHP-77, H4, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.98×** | +5.7 | 9e-07 | 9/11 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.95×** | +5.6 | 2e-06 | 10/10 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +4.3 | 9e-04 | 11/11 (HS-578T, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.68×** | +4.3 | 9e-04 | 10/11 (HS-578T, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.68×** | +4.3 | 9e-04 | 2/10 (SK-MEL-2, HS-578T) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.74×** | +4.3 | 9e-04 | 0/6 | all doses, stronger at high dose | composition shift; position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.72×** | +4.2 | 0.001 | 0/9 | inconsistent across doses | position effect removed |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.64×** | +4.1 | 0.002 | 1/11 (SK-MEL-2) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +3.9 | 0.003 | 0/8 | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.11×** | +3.9 | 0.004 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +3.5 | 0.018 | 2/10 (SNU-423, H4) | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.48×** | +3.3 | 0.032 | 3/9 (HS-578T, SNU-423, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.051 | 2/9 (A549, SHP-77) | inconsistent across doses | position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.44×** | +2.9 | 0.090 | 0/9 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8006.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.110×, NCI-H460 0.119×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.188×); [[Budesonide (drug)]] 0.05 µM in 1 line (NCI-H460 0.145×); [[Triamcinolone (drug)]] 0.5 µM in 1 line (NCI-H460 0.148×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.632× | -3.6 | 0.11 | 2/11 (NCI-H460, CHP-212) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.656× | -3.5 | 0.11 | 4/9 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Encorafenib (drug)]] 5 µM |  | 0.483× | -3.2 | 0.24 | 0/11 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.769× | -3.1 | 0.24 | 3/12 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.775× | -3.1 | 0.25 | 5/10 (NCI-H460, NCI-H1573, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8006. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 198 | 0 | 13 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -12.6) |
| [[HS-578T (line)]] | alt | 5.08 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 13.6× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 73.0 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.35× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.110× (z -11.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 18.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.80× (z +9.6) | — |
| [[A549 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0547× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 10.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 13.1× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 17.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.20× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 8.46 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.37× (z +9.3) | — |
| [[A-172 (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.63 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.93 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8006), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCUBE1]] | +0.74 | +0.63 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SMOC1]] | +0.73 | +0.56 / +0.77 | both halves | 1e-05 | **novel candidate** |
| [[SERPIND1]] | +0.72 | +0.64 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SLITRK4]] | +0.70 | +0.52 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[CNTN1]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 | same gene group |
| [[CRLF2]] | +0.69 | +0.60 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[DOCK4]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[GTF2IP7]] | +0.63 | +0.58 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[UNC13A]] | +0.63 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[NRXN3]] | +0.63 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[NCAM1]] | +0.62 | +0.49 / +0.59 | both halves | 1e-05 | same gene group |
| [[DPP10]] | +0.62 | +0.51 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCKAP5-AS2]] | C | NCKAP5-AS2 activity raises UNC5D's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 2.21× lower at baseline in the lines without NCKAP5-AS2 | 0.043 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises UNC5D's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 3.31× lower at baseline in the lines without DPP10 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[NCKAP5]] | C | NCKAP5 activity raises UNC5D's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 2.12× lower at baseline in the lines without NCKAP5 | 0.067 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 1, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A4]] | B | UNC5D activity raises SLC16A4's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 1.72× lower at baseline in the lines without UNC5D | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11 |
| [[NRXN3]] | C | UNC5D activity raises NRXN3's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 4.45× lower at baseline in the lines without UNC5D | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11; co-absent with the target |
| [[NCKAP5]] | C | UNC5D activity raises NCKAP5's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 3.44× lower at baseline in the lines without UNC5D | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11; co-absent with the target |
| [[PDE4B]] | C | UNC5D activity raises PDE4B's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 4.57× lower at baseline in the lines without UNC5D | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11; co-absent with the target |
| [[CNTN1]] | C | UNC5D activity raises CNTN1's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 3.65× lower at baseline in the lines without UNC5D | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11; co-absent with the target |
| [[KCNK2]] | C | UNC5D activity raises KCNK2's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 2.45× lower at baseline in the lines without UNC5D | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11; co-absent with the target |
| [[NCKAP5-AS2]] | C | UNC5D activity raises NCKAP5-AS2's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 2.04× lower at baseline in the lines without UNC5D | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11; co-absent with the target |
| [[PDE1C]] | C | UNC5D activity raises PDE1C's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 3.37× lower at baseline in the lines without UNC5D | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11; co-absent with the target |
| [[EYA2]] | C | UNC5D activity raises EYA2's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 2.91× lower at baseline in the lines without UNC5D | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11; co-absent with the target |
| [[CDH19]] | C | UNC5D activity raises CDH19's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 2.90× lower at baseline in the lines without UNC5D | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11; co-absent with the target |
| [[TENM1]] | C | UNC5D activity raises TENM1's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 3.77× lower at baseline in the lines without UNC5D | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11; co-absent with the target |
| [[PDE7B]] | C | UNC5D activity raises PDE7B's level | lines that do not express UNC5D (36) vs lines expressing it (14) | 2.46× lower at baseline in the lines without UNC5D | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01266, KCNH5, NAA11; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.3, 33.1); signed map (39.7, 46.3). **Vector** length 45.6, 15.8% of its response variance represented; |z| ≥ 3 in 296 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +3.8 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +1.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +1.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -3.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.5 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | unc-5 netrin receptor D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p12 — chr8:35,235,475-35,796,550 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1777, Unc5h4 |
| Gene groups (HGNC) | I-set domain containing; Ig-like cell adhesion molecule family; ZU5 domain containing |
| Reactome | 4 pathways, smallest: Netrin mediated repulsion signals; Netrin-1 signaling; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UXZ4](https://www.uniprot.org/uniprotkb/Q6UXZ4) (Netrin receptor UNC5D):

> Receptor for the netrin NTN4 that promotes neuronal cell survival (By similarity). Plays a role in cell-cell adhesion and cell guidance. Receptor for netrin involved in cell migration. Plays a role in axon guidance by mediating axon repulsion of neuronal growth cones in the developing nervous system upon ligand binding (By similarity). May play a role in apoptosis in response to DNA damage. It also acts as a dependence receptor required for apoptosis induction when not associated with netrin …

**Summary**, from NCBI Gene [137970](https://www.ncbi.nlm.nih.gov/gene/137970):

> Predicted to enable netrin receptor activity. Involved in cell-cell adhesion. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18634](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18634) · Entrez [137970](https://www.ncbi.nlm.nih.gov/gene/137970) · UniProt [Q6UXZ4](https://www.uniprot.org/uniprotkb/Q6UXZ4) · Ensembl [ENSG00000156687](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156687)

## Data

Gene col 8006: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8006); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8006, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8006]; `tensor/DDL_lfc|DDL_z.npy` [8006]; `embed/gene_vectors.npy` [8006]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8006 or target_col == 8006). Every well: [[UNC5D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UNC5D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
