---
symbol: "POU3F2"
type: "gene"
col: 11543
ensembl_id: "ENSG00000184486"
name: "POU class 3 homeobox 2"
location: "6q16.1"
module: 27
arm: "+"
pooled_cpm: 2.38
n_lines_expressing: 18
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 10
direction_downstream: 29
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# POU3F2

*POU class 3 homeobox 2* — 6q16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.22× (z +12.2, q 2e-31, up in 5 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.242×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H661 0.157×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP25]] (+0.60, fdr 8e-06), [[POU6F2]] (+0.59, fdr 1e-05), [[HS3ST5]] (+0.59, fdr 1e-05); moves opposite to [[PCYT1A]] (-0.47, fdr 3e-05), [[CHFR]] (-0.44, fdr 6e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 29 go from it, the strongest it → [[KIF6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11543.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.22×** | +12.2 | 2e-31 | 5/9 (LOX-IMVI, J82, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **5.21×** | +9.9 | 1e-20 | 9/13 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.91×** | +9.5 | 3e-19 | 8/12 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.51×** | +8.7 | 6e-16 | 1/3 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.98×** | +8.3 | 1e-14 | 3/9 (SK-MEL-2, J82, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.83×** | +8.0 | 8e-14 | 8/12 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.44×** | +6.8 | 1e-09 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.07×** | +6.1 | 6e-08 | 4/12 (J82, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.97×** | +5.7 | 6e-07 | 2/9 (J82, C32) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.44×** | +5.1 | 2e-05 | 4/7 (C32, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.26×** | +4.9 | 6e-05 | 4/13 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.99×** | +4.7 | 1e-04 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **2.16×** | +4.6 | 2e-04 | 3/8 (SW480, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.68×** | +4.4 | 5e-04 | 3/13 (C32, SHP-77, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **2.11×** | +4.3 | 7e-04 | 4/8 (C32, J82, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +4.0 | 0.002 | 4/8 (J82, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +3.7 | 0.008 | 1/9 (J82) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.78×** | +3.4 | 0.018 | 0/10 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.10×** | +3.2 | 0.045 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.09×** | +3.1 | 0.046 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.68×** | +3.1 | 0.054 | 0/7 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.071 | 3/12 (LOX-IMVI, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11543.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.242×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H661 0.157×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.560× | -3.5 | 0.14 | 5/11 (SK-MEL-2, A-172, …) | two highest doses |  |
| [[Dabrafenib (drug)]] 5 µM |  | 0.331× | -3.5 | 0.14 | 3/13 (SHP-77, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.695× | -3.1 | 0.28 | 3/13 (A498, hTERT-HPNE, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.599× | -3.1 | 0.28 | 0/12 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11543. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H661 (line)]] | alt | 221 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -10.2) |
| [[A-172 (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.821 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.289 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.925 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.341 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.282 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.974 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.257 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.248 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.285 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.760 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.321 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.854 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.641 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.932 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.230 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.310 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11543), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP25]] | +0.60 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[POU6F2]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 | same gene group |
| [[HS3ST5]] | +0.59 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[LINC01876]] | +0.59 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[DACH1]] | +0.57 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[MIR2052HG]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[RMST]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[FAM133A]] | +0.56 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[KCNB2]] | +0.56 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[RUNX1T1]] | +0.56 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[BAMBI]] | +0.54 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[BCL11A]] | +0.54 | +0.44 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCYT1A]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[CHFR]] | -0.44 | -0.39 / -0.45 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers POU3F2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ASCL1]] | C | ASCL1 activity raises POU3F2's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 3.95× lower at baseline in the lines without ASCL1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises POU3F2's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.33× lower at baseline in the lines without RUNX1T1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity raises POU3F2's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 2.74× lower at baseline in the lines without CSMD3 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises POU3F2's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 3.49× lower at baseline in the lines without SRRM4 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[SERPINF1]] | C | SERPINF1 activity raises POU3F2's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.43× lower at baseline in the lines without SERPINF1 | 0.064 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent; co-absent with the target |
| [[MIR2052HG]] | C | MIR2052HG activity raises POU3F2's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 2.28× lower at baseline in the lines without MIR2052HG | 0.068 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent; co-absent with the target |
| [[RMST]] | C | RMST activity raises POU3F2's level | lines that do not express RMST (35) vs lines expressing it (15) | 1.87× lower at baseline in the lines without RMST | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, ENSG00000287923; maybe low, not absent; co-absent with the target |
| [[LINC02050]] | C | LINC02050 activity raises POU3F2's level | lines that do not express LINC02050 (37) vs lines expressing it (13) | 2.38× lower at baseline in the lines without LINC02050 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000286329, ENSG00000242828, PASD1; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises POU3F2's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 2.74× lower at baseline in the lines without GABRG2 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 11, C 18. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF6]] | B | POU3F2 activity raises KIF6's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 1.68× lower at baseline in the lines without POU3F2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC |
| [[FAM13C]] | B | POU3F2 activity raises FAM13C's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 2.30× lower at baseline in the lines without POU3F2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC |
| [[OFCC1]] | B | POU3F2 activity raises OFCC1's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 2.87× lower at baseline in the lines without POU3F2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC |
| [[LINC01980]] | B | POU3F2 activity raises LINC01980's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 1.68× lower at baseline in the lines without POU3F2 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC |
| [[SLAIN1]] | B | POU3F2 activity raises SLAIN1's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 1.50× lower at baseline in the lines without POU3F2 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC |
| [[RAB30]] | B | POU3F2 activity raises RAB30's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 1.37× lower at baseline in the lines without POU3F2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC |
| [[SMOC2]] | B | POU3F2 activity raises SMOC2's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 1.28× lower at baseline in the lines without POU3F2 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC |
| [[LINC02223]] | B | POU3F2 activity raises LINC02223's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 1.55× lower at baseline in the lines without POU3F2 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC |
| [[ARHGAP25]] | B | POU3F2 activity raises ARHGAP25's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 1.40× lower at baseline in the lines without POU3F2 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC |
| [[SLCO6A1]] | B | POU3F2 activity raises SLCO6A1's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 1.76× lower at baseline in the lines without POU3F2 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC |
| [[LINC00649]] | B | POU3F2 activity raises LINC00649's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 1.17× lower at baseline in the lines without POU3F2 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC |
| [[SHISA9]] | C | POU3F2 activity raises SHISA9's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 1.81× lower at baseline in the lines without POU3F2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.4, 41.6); signed map (46.8, 34.3). **Vector** length 25.8, 6.12% of its response variance represented; |z| ≥ 3 in 253 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +2.5 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +12.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +3.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.8 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.8 | +1.7 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -0.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.9 | -2.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -0.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | POU class 3 homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.1 — chr6:98,834,574-98,839,458 (+) |
| Ensembl biotype | protein_coding |
| Also known as | POUF3, BRN2, OCT7; previously OTF7 |
| Gene groups (HGNC) | POU class homeoboxes and pseudogenes |
| Reactome | 6 pathways, smallest: Regulation of MITF-M-dependent genes involved in apoptosis; EGR2 and SOX10-mediated initiation of Schwann cell myelination; Transcriptional and post-translational regulation of MITF-M expression and activity |
| Matched by | ensembl_id |

**Function**, from UniProt [P20265](https://www.uniprot.org/uniprotkb/P20265) (POU domain, class 3, transcription factor 2):

> Transcription factor that plays a key role in neuronal differentiation (By similarity). Binds preferentially to the recognition sequence which consists of two distinct half-sites, ('GCAT') and ('TAAT'), separated by a non-conserved spacer region of 0, 2, or 3 nucleotides (By similarity). Acts as a transcriptional activator when binding cooperatively with SOX4, SOX11, or SOX12 to gene promoters (By similarity). The combination of three transcription factors, ASCL1, POU3F2/BRN2 and MYT1L, is …

**Summary**, from NCBI Gene [5454](https://www.ncbi.nlm.nih.gov/gene/5454):

> This gene encodes a member of the POU-III class of neural transcription factors. The encoded protein is involved in neuronal differentiation and enhances the activation of corticotropin-releasing hormone regulated genes. Overexpression of this protein is associated with an increase in the proliferation of melanoma cells. [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:9215](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9215) · Entrez [5454](https://www.ncbi.nlm.nih.gov/gene/5454) · UniProt [P20265](https://www.uniprot.org/uniprotkb/P20265) · Ensembl [ENSG00000184486](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184486)

## Data

Gene col 11543: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11543); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11543, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11543]; `tensor/DDL_lfc|DDL_z.npy` [11543]; `embed/gene_vectors.npy` [11543]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11543 or target_col == 11543). Every well: [[POU3F2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POU3F2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
