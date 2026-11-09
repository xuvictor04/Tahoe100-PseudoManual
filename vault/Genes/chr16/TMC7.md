---
symbol: "TMC7"
type: "gene"
col: 9970
ensembl_id: "ENSG00000170537"
name: "transmembrane channel like 7"
location: "16p12.3"
module: 34
arm: "+"
pooled_cpm: 32.32
n_lines_expressing: 47
n_dd_up: 2
n_dd_down: 32
n_dd_up_clean: 2
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 13
direction_downstream: 16
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# TMC7

*transmembrane channel like 7* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.52× (z +6.4, q 5e-08, up in 23 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (NCI-H460 2.73×); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (NCI-H460 2.78×); [[PH-797804 (drug)]] 5 µM in 1 line (NCI-H1573 8.32×).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.659× (z -9.1, q 4e-17, down in 29 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FERMT1]] (+0.72, fdr 7e-06), [[PRSS3]] (+0.71, fdr 7e-06), [[PLEK2]] (+0.67, fdr 7e-06).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[DHRS9]] → it (grade B ⚠); 16 go from it, the strongest it → [[KIAA1671]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9970.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (NCI-H460 2.73×); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (NCI-H460 2.78×); [[PH-797804 (drug)]] 5 µM in 1 line (NCI-H1573 8.32×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.52×** | +6.4 | 5e-08 | 23/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.54×** | +6.4 | 5e-08 | 23/44 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.24× | +3.3 | 0.16 | 12/44 (COLO 205, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.25× | +3.3 | 0.16 | 14/41 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9970.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.659×** | -9.1 | 4e-17 | 29/44 (Hs 766T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.566×** | -8.5 | 7e-15 | 28/43 (KATO III, LS 180, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.723×** | -7.1 | 3e-10 | 27/45 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.686×** | -5.8 | 8e-07 | 24/45 (AsPC-1, Hs 766T, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.708×** | -5.4 | 1e-05 | 15/45 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.711×** | -5.3 | 1e-05 | 22/45 (AsPC-1, Hs 766T, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.786×** | -5.3 | 1e-05 | 22/45 (CFPAC-1, SW1417, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.758×** | -5.0 | 4e-05 | 20/45 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.806×** | -4.7 | 1e-04 | 19/45 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.746×** | -4.4 | 7e-04 | 23/45 (KATO III, Hs 766T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.748×** | -4.3 | 8e-04 | 19/29 (AsPC-1, SW480, …) | rises with dose | composition shift |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.753×** | -4.2 | 0.001 | 18/44 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.747×** | -4.2 | 0.001 | 14/45 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.772×** | -4.0 | 0.002 | 19/44 (AsPC-1, HepG2/C3A, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.806×** | -3.9 | 0.003 | 16/45 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.618×** | -3.9 | 0.004 | 13/41 (KATO III, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **0.783×** | -3.8 | 0.005 | 16/45 (Hs 766T, AsPC-1, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.776×** | -3.7 | 0.006 | 20/44 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.782×** | -3.7 | 0.007 | 10/42 (A-172, Panc 03.27, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.791×** | -3.6 | 0.007 | 18/44 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9970. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 166 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -21.7) |
| [[Hs 766T (line)]] | wt | 138 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -22.5) |
| [[KATO III (line)]] | alt | 92.2 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -19.5) |
| [[HepG2_C3A (line)]] | wt | 114 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 33.0 | 0 | 6 (2 ⚠) | — | [[Cobimetinib (drug)]] 0.5 µM 0.151× (z -10.6) |
| [[LoVo (line)]] | wt | 63.9 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -11.3) |
| [[SW480 (line)]] | alt | 54.4 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -9.7) |
| [[LS 180 (line)]] | wt | 57.1 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -16.3) |
| [[NCI-H1792 (line)]] | alt | 51.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 31.6 | 2 | 1 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.73× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 31.0 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 8.32× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[NCI-H2030 (line)]] | alt | 40.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[SNU-1 (line)]] | wt | 26.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -9.4) |
| [[A-427 (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0939× (z -11.7) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 21.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -8.7) |
| [[PANC-1 (line)]] | alt | 25.5 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.406× (z -11.5) |
| [[SW1417 (line)]] | alt | 32.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -11.0) |
| [[A-172 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.60 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.02 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.63 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9970), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FERMT1]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[PRSS3]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[PLEK2]] | +0.67 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[LAMC2]] | +0.66 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[KPNA2P3]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[DHRS9]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[ANO1]] | +0.66 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[SERPINB5]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[TINAGL1]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[S100A16]] | +0.64 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[DENND2C]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[PLEKHM1P1]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DHRS9]] | B | DHRS9 activity raises TMC7's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 2.85× lower at baseline in the lines without DHRS9 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610 |
| [[CYP3A5]] | B | CYP3A5 activity raises TMC7's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 2.62× lower at baseline in the lines without CYP3A5 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[MAP2K1]] | B | MAP2K1 activity raises TMC7's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.7% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds |
| [[LINC02582]] | B | LINC02582 activity raises TMC7's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 2.73× lower at baseline in the lines without LINC02582 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975 |
| [[PKP1]] | B | PKP1 activity raises TMC7's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 1.94× lower at baseline in the lines without PKP1 | 0.053 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[FA2H]] | B | FA2H activity raises TMC7's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.22× lower at baseline in the lines without FA2H | 0.053 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[TOP2A]] | B | TOP2A activity raises TMC7's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SERPINB5]] | B | SERPINB5 activity raises TMC7's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.36× lower at baseline in the lines without SERPINB5 | 0.062 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[WNT7B]] | B | WNT7B activity raises TMC7's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.70× lower at baseline in the lines without WNT7B | 0.075 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[LAMA3]] | B | LAMA3 activity raises TMC7's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.04× lower at baseline in the lines without LAMA3 | 0.094 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[NGEF]] | B | NGEF activity raises TMC7's level | lines that do not express NGEF (12) vs lines expressing it (38) | 2.01× lower at baseline in the lines without NGEF | 0.096 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TSPAN15, PDGFB |
| [[HAS3]] | B | HAS3 activity raises TMC7's level | lines that do not express HAS3 (18) vs lines expressing it (32) | 2.36× lower at baseline in the lines without HAS3 | 0.099 | ⚠ within organs, on part of the lines; also absent: IQANK1, MLXIPL, CAMSAP3; maybe low, not absent |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 0, C 16. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA1671]] | C | TMC7 activity raises KIAA1671's level | lines that do not express TMC7 (3) vs lines expressing it (47) | 4.16× lower at baseline in the lines without TMC7 | 0.005 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent with the target |
| [[CD58]] | C | TMC7 activity strengthens CD58's drug response | lines that do not express TMC7 (3) vs lines expressing it (46) | the lines without TMC7 respond 0.20× as strongly (z diff +3.45); strongest at Panobinostat 5 µM: 0.97x vs 0.42x (z diff +7.2) | 0.024 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; target measured in part of the lines; artifact flags |
| cells under [[Sonidegib (drug)]] 5 µM | C | [[EZR]], TMC7 activity raises the cells' numbers under Sonidegib 5 µM (protects the cells) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 0.69× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| [[PARD6B]] | C | [[EZR]], TMC7 activity raises PARD6B's level | lines that do not express EZR, TMC7 (3) vs lines expressing them (47) | 4.35× lower at baseline in the lines without EZR, TMC7 | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| cells under [[DTP3 (drug)]] 5 µM | C | [[EZR]], TMC7 activity raises the cells' numbers under DTP3 5 µM (protects the cells) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 0.61× the cells of the other lines | 0.029 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| cells under [[Peretinoin (drug)]] 5 µM | C | [[EZR]], TMC7 activity raises the cells' numbers under Peretinoin 5 µM (protects the cells) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 0.72× the cells of the other lines | 0.035 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| cells under [[Daptomycin (drug)]] 0.5 µM | C | [[EZR]], TMC7 activity raises the cells' numbers under Daptomycin 0.5 µM (protects the cells) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 0.63× the cells of the other lines | 0.036 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; cell counts less trustworthy; co-absent genes |
| cells under [[Docetaxel (Trihydrate) (drug)]] 5 µM | C | [[EZR]], TMC7 activity raises the cells' numbers under Docetaxel (Trihydrate) 5 µM (protects the cells) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 0.70× the cells of the other lines | 0.039 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| cells under [[Pasireotide (acetate) (drug)]] 5 µM | C | [[EZR]], TMC7 activity raises the cells' numbers under Pasireotide (acetate) 5 µM (protects the cells) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 0.81× the cells of the other lines | 0.041 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| cells under [[Artesunate (drug)]] 0.5 µM | C | [[EZR]], TMC7 activity lowers the cells' numbers under Artesunate 0.5 µM (makes them more sensitive) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 1.29× the cells of the other lines | 0.045 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| cells under [[vincristine (drug)]] 5 µM | C | [[EZR]], TMC7 activity raises the cells' numbers under vincristine 5 µM (protects the cells) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 0.53× the cells of the other lines | 0.045 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | [[EZR]], TMC7 activity lowers the cells' numbers under Anethole trithione 0.5 µM (makes them more sensitive) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 1.33× the cells of the other lines | 0.045 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.751). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.2, 54.0); signed map (1.5, 39.6). **Vector** length 116, 31.2% of its response variance represented; |z| ≥ 3 in 1,178 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.0 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | +4.4 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +3.8 | -4.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.4 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | -2.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +1.3 |
| fall | [[Binimetinib (drug)]] 0.5 µM |  | -4.3 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.2 | -4.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.0 | -3.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.9 | -7.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.8 | -5.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -5.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane channel like 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:18,983,934-19,063,942 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21240 |
| Gene groups (HGNC) | Transmembrane channel like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z402](https://www.uniprot.org/uniprotkb/Q7Z402) (Transmembrane channel-like protein 7):

> Acts as an inhibitory modulator of PIEZO2 mechanosensitive channel in dorsal root ganglion (DRG) neurons through physical interactions or interference with the interaction between PIEZO2 and the cytoskeleton.

**Summary**, from NCBI Gene [79905](https://www.ncbi.nlm.nih.gov/gene/79905):

> Predicted to enable ion channel inhibitor activity and mechanosensitive monoatomic ion channel activity. Predicted to be involved in sensory perception of mechanical stimulus. Predicted to be located in plasma membrane. Predicted to be active in neuronal cell body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23000](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23000) · Entrez [79905](https://www.ncbi.nlm.nih.gov/gene/79905) · UniProt [Q7Z402](https://www.uniprot.org/uniprotkb/Q7Z402) · Ensembl [ENSG00000170537](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170537)

## Data

Gene col 9970: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9970); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9970, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9970]; `tensor/DDL_lfc|DDL_z.npy` [9970]; `embed/gene_vectors.npy` [9970]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9970 or target_col == 9970). Every well: [[TMC7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMC7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
