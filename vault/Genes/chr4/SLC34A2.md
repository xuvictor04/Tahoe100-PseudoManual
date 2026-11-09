---
symbol: "SLC34A2"
type: "gene"
col: 8099
ensembl_id: "ENSG00000157765"
name: "solute carrier family 34 member 2"
location: "4p15.2"
module: 8
arm: "+"
pooled_cpm: 5.32
n_lines_expressing: 6
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 43
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SLC34A2

*solute carrier family 34 member 2* — 4p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.60× (z +9.1, q 7e-17, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.88× (z +8.2, q 8e-14, up in 0 of 3 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bicalutamide (drug)]] 5 µM in 1 line (NCI-H661 0.260×); [[Panobinostat (drug)]] 5 µM in 1 line (KATO III 0.0287×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC4]] (+0.73, fdr 7e-06), [[PDZK1IP1]] (+0.73, fdr 7e-06), [[SLC15A1]] (+0.69, fdr 7e-06); moves opposite to [[CROCCP3-1]] (-0.46, fdr 4e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MUC4]] → it (grade C ⚠); 43 go from it, the strongest it → [[UNC5CL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8099.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.60×** | +9.1 | 7e-17 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.88×** | +8.2 | 8e-14 | 0/3 | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.20×** | +7.8 | 8e-13 | 1/2 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.11×** | +7.2 | 1e-10 | 1/2 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.67×** | +5.4 | 9e-06 | 0/2 | top dose only | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +4.7 | 3e-04 | 0/3 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.83×** | +4.7 | 3e-04 | 1/3 (KATO III) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.16×** | +4.5 | 5e-04 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.08×** | +4.0 | 0.004 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.08×** | +4.0 | 0.004 | 0/3 | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +3.9 | 0.005 | 1/3 (CFPAC-1) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +3.9 | 0.005 | 1/3 (KATO III) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.55×** | +3.6 | 0.013 | 1/2 (NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +3.5 | 0.020 | 1/3 (NCI-H2347) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **2.16×** | +3.4 | 0.028 | 0/3 | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +3.2 | 0.042 | 0/3 | top dose only |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **2.00×** | +3.0 | 0.077 | 0/3 | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8099.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bicalutamide (drug)]] 5 µM in 1 line (NCI-H661 0.260×); [[Panobinostat (drug)]] 5 µM in 1 line (KATO III 0.0287×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.531× | -3.5 | 0.23 | 1/3 (NCI-H2347) | inconsistent across doses | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.548× | -3.4 | 0.23 | 0/3 | rises with dose |  |
| [[Gallic acid (drug)]] 0.5 µM |  | 0.574× | -3.1 | 0.38 | 0/3 | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8099. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 4.46 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0287× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 1.73 | 0 | 1 | — | [[Bicalutamide (drug)]] 5 µM 0.260× (z -12.6) |
| [[A-172 (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.283 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.307 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.306 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.353 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.312 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.330 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.330 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.289 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.266 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.322 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.300 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.289 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.293 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.284 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.304 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.394 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.281 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8099), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC4]] | +0.73 | +0.73 / +0.66 | both halves | 7e-06 | pathway: Diseases of metabolism |
| [[PDZK1IP1]] | +0.73 | +0.69 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SLC15A1]] | +0.69 | +0.68 / +0.73 | both halves | 7e-06 | pathway: SLC-mediated transmembrane transport |
| [[MMP7]] | +0.68 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[CASP10]] | +0.68 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[HHLA2]] | +0.67 | +0.60 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[MUC16]] | +0.67 | +0.59 / +0.63 | both halves | 7e-06 | pathway: Diseases of metabolism |
| [[SAMD12-AS1]] | +0.65 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[GABRP]] | +0.65 | +0.72 / +0.46 | both halves | 3e-05 | **novel candidate** |
| [[STEAP4]] | +0.65 | +0.41 / +0.68 | both halves | 4e-05 | **novel candidate** |
| [[PRSS51]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[STS]] | +0.64 | +0.57 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP3-1]] | -0.46 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC4]] | C | MUC4 activity raises SLC34A2's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 2.89× lower at baseline in the lines without MUC4 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6; co-absent with the target |
| [[SLC44A4]] | C | SLC44A4 activity raises SLC34A2's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 2.06× lower at baseline in the lines without SLC44A4 | 0.012 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[LCN2]] | C | LCN2 activity raises SLC34A2's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 1.77× lower at baseline in the lines without LCN2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[SFTPA2]] | C | SFTPA2 activity raises SLC34A2's level | lines that do not express SFTPA2 (46) vs lines expressing it (4) | 4.03× lower at baseline in the lines without SFTPA2 | 0.044 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[WFDC2]] | C | WFDC2 activity raises SLC34A2's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 2.19× lower at baseline in the lines without WFDC2 | 0.048 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; co-absent with the target |
| [[CST6]] | C | CST6 activity raises SLC34A2's level | lines that do not express CST6 (42) vs lines expressing it (8) | 2.68× lower at baseline in the lines without CST6 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, PIGR, ENSG00000286546; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises SLC34A2's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 1.88× lower at baseline in the lines without ADGRF1 | 0.064 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[DPP4]] | C | DPP4 activity raises SLC34A2's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 1.38× lower at baseline in the lines without DPP4 | 0.075 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10; co-absent with the target |
| [[STEAP4]] | C | STEAP4 activity raises SLC34A2's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.22× lower at baseline in the lines without STEAP4 | 0.089 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1; co-absent with the target |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 12, C 31. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UNC5CL]] | B | SLC34A2 activity raises UNC5CL's level | lines that do not express SLC34A2 (44) vs lines expressing it (6) | 1.51× lower at baseline in the lines without SLC34A2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, SFTPA2, GABRP |
| [[MUC20]] | B | SLC34A2 activity raises MUC20's level | lines that do not express SLC34A2 (44) vs lines expressing it (6) | 2.71× lower at baseline in the lines without SLC34A2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, SFTPA2, GABRP |
| [[OCLN]] | B | SLC34A2 activity raises OCLN's level | lines that do not express SLC34A2 (44) vs lines expressing it (6) | 4.90× lower at baseline in the lines without SLC34A2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, SFTPA2, GABRP |
| [[BCL2L15]] | B | SLC34A2 activity raises BCL2L15's level | lines that do not express SLC34A2 (44) vs lines expressing it (6) | 1.89× lower at baseline in the lines without SLC34A2 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, SFTPA2, GABRP |
| [[ADGRF4]] | B | SLC34A2 activity raises ADGRF4's level | lines that do not express SLC34A2 (44) vs lines expressing it (6) | 2.36× lower at baseline in the lines without SLC34A2 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, SFTPA2, GABRP |
| [[RAMP1]] | B | SLC34A2 activity raises RAMP1's level | lines that do not express SLC34A2 (44) vs lines expressing it (6) | 1.81× lower at baseline in the lines without SLC34A2 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, SFTPA2, GABRP |
| [[RBM47]] | B | SLC34A2 activity raises RBM47's level | lines that do not express SLC34A2 (44) vs lines expressing it (6) | 5.18× lower at baseline in the lines without SLC34A2 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, SFTPA2, GABRP |
| [[STS]] | B | SLC34A2 activity raises STS's level | lines that do not express SLC34A2 (44) vs lines expressing it (6) | 1.93× lower at baseline in the lines without SLC34A2 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, SFTPA2, GABRP |
| [[SAMD12-AS1]] | B | SLC34A2 activity raises SAMD12-AS1's level | lines that do not express SLC34A2 (44) vs lines expressing it (6) | 3.07× lower at baseline in the lines without SLC34A2 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, SFTPA2, GABRP |
| [[TLR3]] | B | SLC34A2 activity raises TLR3's level | lines that do not express SLC34A2 (44) vs lines expressing it (6) | 1.96× lower at baseline in the lines without SLC34A2 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, SFTPA2, GABRP |
| [[PLCH1]] | B | SLC34A2 activity raises PLCH1's level | lines that do not express SLC34A2 (44) vs lines expressing it (6) | 2.51× lower at baseline in the lines without SLC34A2 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, SFTPA2, GABRP |
| [[APOL1]] | B | SLC34A2 activity raises APOL1's level | lines that do not express SLC34A2 (44) vs lines expressing it (6) | 2.21× lower at baseline in the lines without SLC34A2 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, SFTPA2, GABRP |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.676). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.5, 54.9); signed map (60.8, 1.3). **Vector** length 19.5, 10.3% of its response variance represented; |z| ≥ 3 in 90 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.56 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.8 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.8 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.8 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.8 | +7.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +0.7 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.7 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.7 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.6 | +0.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.6 | +0.0 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -0.7 | -1.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -0.6 | -1.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -0.5 | -1.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -0.5 | +0.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.4 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 34 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.2 — chr4:25,648,011-25,678,748 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NAPI-3B, NaPi-2b, NPTIIb, NaPi2b, NAPI-IIb |
| Gene groups (HGNC) | Solute carrier family 34 |
| Reactome | 9 pathways, smallest: Sodium-coupled phosphate cotransporters; Diseases associated with surfactant metabolism; Surfactant metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O95436](https://www.uniprot.org/uniprotkb/O95436) (Sodium-dependent phosphate transport protein 2B):

> Involved in actively transporting phosphate into cells via Na(+) cotransport.

**Summary**, from NCBI Gene [10568](https://www.ncbi.nlm.nih.gov/gene/10568):

> The protein encoded by this gene is a pH-sensitive sodium-dependent phosphate transporter. Phosphate uptake is increased at lower pH. Defects in this gene are a cause of pulmonary alveolar microlithiasis. Three transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:11020](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11020) · Entrez [10568](https://www.ncbi.nlm.nih.gov/gene/10568) · UniProt [O95436](https://www.uniprot.org/uniprotkb/O95436) · Ensembl [ENSG00000157765](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157765)

## Data

Gene col 8099: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8099); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8099, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8099]; `tensor/DDL_lfc|DDL_z.npy` [8099]; `embed/gene_vectors.npy` [8099]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8099 or target_col == 8099). Every well: [[SLC34A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC34A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
