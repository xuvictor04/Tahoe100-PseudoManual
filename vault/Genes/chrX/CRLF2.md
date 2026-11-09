---
symbol: "CRLF2"
type: "gene"
col: 13007
ensembl_id: "ENSG00000205755"
name: "cytokine receptor like factor 2"
location: "Xp22.3 and Yp11.3"
module: 19
arm: "+"
pooled_cpm: 13.32
n_lines_expressing: 15
n_dd_up: 12
n_dd_down: 19
n_dd_up_clean: 8
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 7
direction_downstream: 13
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# CRLF2

*cytokine receptor like factor 2* — Xp22.3 and Yp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.15× (z +8.1, q 2e-13, up in 7 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.412× (z -6.6, q 2e-08, down in 10 of 12 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Clobetasol propionate (drug)]] 5 µM: 0.441× (z -5.5, q 9e-06, down in 9 of 11 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPIND1]] (+0.74, fdr 7e-06), [[GJA1]] (+0.70, fdr 7e-06), [[UNC5D]] (+0.69, fdr 7e-06); moves opposite to [[FGD4]] (-0.51, fdr 2e-05), [[COBLL1]] (-0.50, fdr 3e-05), [[FKBP5]] (-0.49, fdr 2e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 13 go from it, the strongest it → [[LUCAT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13007.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.15×** | +8.1 | 2e-13 | 7/12 (SK-MEL-2, H4, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.85×** | +7.6 | 1e-11 | 1/5 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.78×** | +4.4 | 0.002 | 7/11 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +4.3 | 0.002 | 1/7 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.82×** | +4.2 | 0.004 | 4/11 (NCI-H2030, H4, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.69×** | +4.0 | 0.007 | 0/11 | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.008 | 5/11 (NCI-H460, SW 900, …) | rises with dose | position effect removed |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.63×** | +3.7 | 0.016 | 5/11 (SW 900, SNU-423, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +3.6 | 0.021 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +3.3 | 0.054 | 1/11 (SK-MEL-2) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.05×** | +3.2 | 0.061 | 1/9 (HOP62) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.53×** | +3.2 | 0.063 | 3/11 (A549, SW 900, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13007.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.412×** | -6.6 | 2e-08 | 10/12 (NCI-H460, SNU-423, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.441×** | -5.5 | 9e-06 | 9/11 (SNU-423, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.463×** | -5.3 | 2e-05 | 7/12 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.533×** | -4.7 | 4e-04 | 8/11 (A549, NCI-H2030, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.548×** | -4.5 | 8e-04 | 5/12 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.674×** | -4.1 | 0.004 | 3/11 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.585×** | -4.0 | 0.005 | 8/11 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.598×** | -3.8 | 0.009 | 3/11 (NCI-H460, NCI-H2030, …) | two highest doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.606×** | -3.7 | 0.012 | 9/11 (CFPAC-1, A549, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.586×** | -3.7 | 0.013 | 9/11 (NCI-H2030, A549, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.590×** | -3.6 | 0.020 | 9/12 (A549, SNU-423, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.630×** | -3.4 | 0.028 | 6/11 (H4, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.636×** | -3.4 | 0.034 | 9/11 (A549, SNU-423, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.642×** | -3.3 | 0.039 | 10/11 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.888× | -3.3 | 0.039 | 6/13 (NCI-H2030, A549, …) | inconsistent across doses |  |
| [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | **0.645×** | -3.3 | 0.039 | 0/11 | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.635×** | -3.2 | 0.039 | 8/11 (SNU-423, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13007. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 48.1 | 0 | 14 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0816× (z -19.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Betamethasone dipropionate (drug)]] 5 µM 0.176× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 159 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0873× (z -24.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -9.2) |
| [[A549 (line)]] | wt | 11.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0675× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0873× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 72.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Betamethasone dipropionate (drug)]] 0.05 µM 0.188× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Triamcinolone (drug)]] 0.5 µM 0.147× (z -8.5) |
| [[HOP62 (line)]] | alt | 6.26 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0620× (z -9.7) ⚠ cell-cycle shift, explains ~61% of this change |
| [[A-172 (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.915 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.986 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.30 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13007), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPIND1]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[GJA1]] | +0.70 | +0.65 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[UNC5D]] | +0.69 | +0.60 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SMOC1]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SCUBE1]] | +0.64 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[SGIP1]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[AADACP1]] | +0.61 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[STEAP1B-AS1]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[STC1]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[EYA2]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[SMOX]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[GRAMD1B]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGD4]] | -0.51 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[COBLL1]] | -0.50 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[FKBP5]] | -0.49 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[RIPOR2]] | -0.46 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[KRT7]] | -0.46 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[COPS8]] | -0.46 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[FSTL3]] | -0.45 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[STOM]] | -0.45 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[MAOA]] | -0.45 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[STXBP5]] | -0.45 | -0.47 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers CRLF2's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[SERPIND1]] | B | SERPIND1 activity raises CRLF2's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 1.99× lower at baseline in the lines without SERPIND1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[AADAC]] | C | AADAC activity raises CRLF2's level | lines that do not express AADAC (34) vs lines expressing it (16) | 2.60× lower at baseline in the lines without AADAC | 0.049 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610; co-absent with the target |
| [[NCKAP5-AS2]] | C | NCKAP5-AS2 activity raises CRLF2's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 2.45× lower at baseline in the lines without NCKAP5-AS2 | 0.058 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |
| [[AADACP1]] | C | AADACP1 activity raises CRLF2's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 2.25× lower at baseline in the lines without AADACP1 | 0.076 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1; co-absent with the target |
| [[ESM1]] | C | ESM1 activity raises CRLF2's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 2.27× lower at baseline in the lines without ESM1 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865; co-absent with the target |
| [[IGFBP3]] | C | IGFBP3 activity raises CRLF2's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 2.30× lower at baseline in the lines without IGFBP3 | 0.083 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 6, C 7. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LUCAT1]] | B | CRLF2 activity raises LUCAT1's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 3.44× lower at baseline in the lines without CRLF2 | 0.011 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR |
| [[SMOX]] | B | CRLF2 activity raises SMOX's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 2.76× lower at baseline in the lines without CRLF2 | 0.022 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR |
| [[PLAUR]] | B | CRLF2 activity raises PLAUR's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 2.01× lower at baseline in the lines without CRLF2 | 0.056 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR |
| [[SLC16A4]] | B | CRLF2 activity raises SLC16A4's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 2.10× lower at baseline in the lines without CRLF2 | 0.075 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR |
| [[RBFOX1]] | B | CRLF2 activity raises RBFOX1's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 2.59× lower at baseline in the lines without CRLF2 | 0.077 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR |
| [[CEMIP]] | B | CRLF2 activity raises CEMIP's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 1.90× lower at baseline in the lines without CRLF2 | 0.089 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR |
| [[MAF]] | C | CRLF2 activity raises MAF's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 5.96× lower at baseline in the lines without CRLF2 | 0.003 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR; co-absent with the target |
| [[HMGN2P46]] | C | CRLF2 activity raises HMGN2P46's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 3.97× lower at baseline in the lines without CRLF2 | 0.009 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR; co-absent with the target |
| [[CRTAC1]] | C | CRLF2 activity raises CRTAC1's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 3.94× lower at baseline in the lines without CRLF2 | 0.025 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR; co-absent with the target |
| [[RSPO3]] | C | CRLF2 activity raises RSPO3's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 5.02× lower at baseline in the lines without CRLF2 | 0.033 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR; co-absent with the target |
| [[SLC16A6]] | C | CRLF2 activity raises SLC16A6's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 3.32× lower at baseline in the lines without CRLF2 | 0.033 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR; co-absent with the target |
| [[IGFBP3]] | C | CRLF2 activity raises IGFBP3's level | lines that do not express CRLF2 (35) vs lines expressing it (15) | 4.39× lower at baseline in the lines without CRLF2 | 0.039 | ⚠ within organs, on part of the lines; also absent: PAK3, RSPO3, FENDRR; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.515). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.6, 16.5); signed map (19.6, 53.0). **Vector** length 60.5, 23.7% of its response variance represented; |z| ≥ 3 in 417 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +8.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.4 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +4.0 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.3 | +3.9 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +1.1 | +1.8 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -2.7 | -5.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -4.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.5 | -3.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -2.2 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | cytokine receptor like factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.3 and Yp11.3 — chrX:1,190,490-1,212,723 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CRL2, TSLPR |
| Gene groups (HGNC) | Fibronectin type III domain containing; Pseudoautosomal region 1 |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING |
| Reactome | 3 pathways, smallest: Interleukin-7 signaling; Signaling by Interleukins; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HC73](https://www.uniprot.org/uniprotkb/Q9HC73) (Cytokine receptor-like factor 2):

> Receptor for thymic stromal lymphopoietin (TSLP). Forms a functional complex with TSLP and IL7R which is capable of stimulating cell proliferation through activation of STAT3 and STAT5. Also activates JAK2 (By similarity). Implicated in the development of the hematopoietic system.

**Summary**, from NCBI Gene [64109](https://www.ncbi.nlm.nih.gov/gene/64109):

> This gene encodes a member of the type I cytokine receptor family. The encoded protein is a receptor for thymic stromal lymphopoietin (TSLP). Together with the interleukin 7 receptor (IL7R), the encoded protein and TSLP activate STAT3, STAT5, and JAK2 pathways, which control processes such as cell proliferation and development of the hematopoietic system. Rearrangement of this gene with immunoglobulin heavy chain gene (IGH) on chromosome 14, or with P2Y purinoceptor 8 gene (P2RY8) on the same X …

**Accessions** — [HGNC:14281](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14281) · Entrez [64109](https://www.ncbi.nlm.nih.gov/gene/64109) · UniProt [Q9HC73](https://www.uniprot.org/uniprotkb/Q9HC73) · Ensembl [ENSG00000205755](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205755)

## Data

Gene col 13007: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13007); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13007, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13007]; `tensor/DDL_lfc|DDL_z.npy` [13007]; `embed/gene_vectors.npy` [13007]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13007 or target_col == 13007). Every well: [[CRLF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRLF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
