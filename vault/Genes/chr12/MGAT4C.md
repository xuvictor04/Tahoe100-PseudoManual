---
symbol: "MGAT4C"
type: "gene"
col: 11234
ensembl_id: "ENSG00000182050"
name: "MGAT4 family member C"
location: "12q21.31-q21.32"
module: 108
arm: "+"
pooled_cpm: 31.09
n_lines_expressing: 15
n_dd_up: 32
n_dd_down: 3
n_dd_up_clean: 25
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 10
direction_downstream: 17
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# MGAT4C

*MGAT4 family member C* — 12q21.31-q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.46× (z +25.2, q 0e+00, up in 6 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.905× (z -4.2, q 0.014, down in 1 of 13 measured lines) ⚠ position not correctable. The strongest without an alert is [[Pyridoxine (hydrochloride) (drug)]] 5 µM: 0.797× (z -3.9, q 0.030, down in 6 of 13 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNH5]] (+0.72, fdr 7e-06), [[CDH10]] (+0.69, fdr 7e-06), [[LINC02484]] (+0.69, fdr 1e-05).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 17 go from it, the strongest it → [[LINC01414]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11234.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.46×** | +25.2 | 0e+00 | 6/12 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.95×** | +12.9 | 2e-35 | 5/13 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.52×** | +11.0 | 8e-26 | 2/12 (RPMI-7951, KATO III) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +8.2 | 2e-14 | 8/13 (hTERT-HPNE, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +6.6 | 4e-09 | 4/13 (A-427, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +6.1 | 1e-07 | 0/10 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +5.9 | 2e-07 | 1/9 (BT-474) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.9 | 2e-07 | 0/13 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +5.5 | 2e-06 | 0/12 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +5.0 | 3e-05 | 6/13 (SK-MEL-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.54×** | +4.9 | 4e-05 | 0/13 | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.53×** | +4.9 | 5e-05 | 7/13 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.40×** | +4.9 | 5e-05 | 9/13 (NCI-H1573, SHP-77, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.2 | 0.001 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.004 | 7/13 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.007 | 7/13 (SHP-77, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.009 | 4/13 (hTERT-HPNE, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.009 | 0/13 | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.011 | 2/13 (SK-MEL-2, HEC-1-A) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.38×** | +3.5 | 0.013 | 2/12 (hTERT-HPNE, HEC-1-A) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11234.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -4.2 | 0.014 | 1/13 (NCI-H661) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.797×** | -3.9 | 0.030 | 6/13 (NCI-H23, KATO III, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.753×** | -3.4 | 0.091 | 7/13 (BT-474, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.753×** | -3.4 | 0.091 | 3/13 (NCI-H661, KATO III, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.768× | -3.2 | 0.16 | 3/13 (NCI-H1573, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11234. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 246 | 0 | 8 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0590× (z -18.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 123 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0826× (z -14.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0572× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 43.7 | 2 | 2 (2 ⚠) | [[Cepharanthine (drug)]] 5 µM 3.99× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -9.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 623 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -12.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 8.52 | 1 | 1 | [[Auranofin (drug)]] 5 µM 9.95× (z +8.9) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.104× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 11.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0412× (z -12.4) ⚠ cell-cycle shift, explains ~5% of this change |
| [[A-172 (line)]] | wt | 4.43 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.60 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.40 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.28 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.57 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.90 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.60 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.95 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.37 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.83 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.62 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.94 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.11 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.21 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.54 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11234), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNH5]] | +0.72 | +0.63 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[CDH10]] | +0.69 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[LINC02484]] | +0.69 | +0.56 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[MIR2052HG]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[VAV3]] | +0.66 | +0.68 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[SLITRK6]] | +0.65 | +0.53 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[NETO1]] | +0.65 | +0.50 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[LINC00993]] | +0.65 | +0.54 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[FGF14]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[LGSN]] | +0.64 | +0.56 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[LINC01456]] | +0.62 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[ZIC1]] | +0.62 | +0.60 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MGAT4C's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GABRA2]] | B | GABRA2 activity raises MGAT4C's level | lines that do not express GABRA2 (24) vs lines expressing it (26) | 2.12× lower at baseline in the lines without GABRA2 | 0.064 | ⚠ within organs, on part of the lines; also absent: LINC02253, ASXL3, ENSG00000257883; maybe low, not absent |
| [[FUT9]] | C | FUT9 activity raises MGAT4C's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 4.72× lower at baseline in the lines without FUT9 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[NETO1]] | C | NETO1 activity raises MGAT4C's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 8.00× lower at baseline in the lines without NETO1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises MGAT4C's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 3.34× lower at baseline in the lines without KCNH7 | 0.025 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[MIR2052HG]] | C | MIR2052HG activity raises MGAT4C's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 3.30× lower at baseline in the lines without MIR2052HG | 0.027 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent; co-absent with the target |
| [[ERBB4]] | C | ERBB4 activity raises MGAT4C's level | lines that do not express ERBB4 (33) vs lines expressing it (17) | 3.41× lower at baseline in the lines without ERBB4 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, NETO1, CDH10; co-absent with the target |
| [[LINC02616]] | C | LINC02616 activity raises MGAT4C's level | lines that do not express LINC02616 (37) vs lines expressing it (13) | 3.50× lower at baseline in the lines without LINC02616 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, ENSG00000287474, FCRLA; co-absent with the target |
| [[LINC01456]] | C | LINC01456 activity raises MGAT4C's level | lines that do not express LINC01456 (42) vs lines expressing it (8) | 4.03× lower at baseline in the lines without LINC01456 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, S100A8; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises MGAT4C's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 3.57× lower at baseline in the lines without KCNH5 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 2, C 15. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01414]] | B | MGAT4C activity raises LINC01414's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 1.89× lower at baseline in the lines without MGAT4C | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385 |
| [[AGBL4]] | B | MGAT4C activity raises AGBL4's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 2.95× lower at baseline in the lines without MGAT4C | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385 |
| [[FMN2]] | C | MGAT4C activity raises FMN2's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 2.81× lower at baseline in the lines without MGAT4C | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |
| [[GABRA3]] | C | MGAT4C activity raises GABRA3's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 3.77× lower at baseline in the lines without MGAT4C | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |
| [[MAGEA3-DT]] | C | MGAT4C activity raises MAGEA3-DT's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 5.28× lower at baseline in the lines without MGAT4C | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |
| [[ROBO2]] | C | MGAT4C activity raises ROBO2's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 3.15× lower at baseline in the lines without MGAT4C | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |
| [[FSTL5]] | C | MGAT4C activity raises FSTL5's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 4.55× lower at baseline in the lines without MGAT4C | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |
| [[RIMS2]] | C | MGAT4C activity raises RIMS2's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 4.29× lower at baseline in the lines without MGAT4C | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |
| [[MIR2052HG]] | C | MGAT4C activity raises MIR2052HG's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 3.91× lower at baseline in the lines without MGAT4C | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |
| [[SLITRK6]] | C | MGAT4C activity raises SLITRK6's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 2.30× lower at baseline in the lines without MGAT4C | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |
| [[FUT9]] | C | MGAT4C activity raises FUT9's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 2.65× lower at baseline in the lines without MGAT4C | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |
| [[OR3A2]] | C | MGAT4C activity raises OR3A2's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 2.26× lower at baseline in the lines without MGAT4C | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.1, 33.3); signed map (40.2, 36.4). **Vector** length 49.8, 16.5% of its response variance represented; |z| ≥ 3 in 376 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +25.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +6.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.3 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +4.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +3.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -1.8 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.4 | -1.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | MGAT4 family member C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.31-q21.32 — chr12:85,955,666-86,838,904 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HGNT-IV-H |
| Gene groups (HGNC) | Mannosyl-glycoprotein N-acetylglucosaminyltransferases |
| Reactome | 10 pathways, smallest: N-Glycan antennae elongation; N-glycan antennae elongation in the medial/trans-Golgi; Maturation of spike protein_9694548 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBM8](https://www.uniprot.org/uniprotkb/Q9UBM8) (Alpha-1,3-mannosyl-glycoprotein 4-beta-N-acetylglucosaminyltransferase C):

> Glycosyltransferase that participates in the transfer of N-acetylglucosamine (GlcNAc) to the core mannose residues of N-linked glycans. Catalyzes the formation of the GlcNAcbeta1-4 branch on the GlcNAcbeta1-2Manalpha1-3 arm of the core structure of N-linked glycans. Essential for the production of tri- and tetra-antennary N-linked sugar chains (By similarity). Does not catalyze the transfer of GlcNAc to the Manalpha1-6 arm to form GlcNAcBeta1-4Manalpha1-6 linkage ('GnT-VI' activity).

**Summary**, from NCBI Gene [25834](https://www.ncbi.nlm.nih.gov/gene/25834):

> Predicted to enable acetylglucosaminyltransferase activity. Predicted to be involved in protein N-linked glycosylation. Predicted to be located in Golgi membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30871](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30871) · Entrez [25834](https://www.ncbi.nlm.nih.gov/gene/25834) · UniProt [Q9UBM8](https://www.uniprot.org/uniprotkb/Q9UBM8) · Ensembl [ENSG00000182050](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182050)

## Data

Gene col 11234: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11234); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11234, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11234]; `tensor/DDL_lfc|DDL_z.npy` [11234]; `embed/gene_vectors.npy` [11234]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11234 or target_col == 11234). Every well: [[MGAT4C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MGAT4C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
