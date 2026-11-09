---
symbol: "PPP1R14B-AS1"
type: "gene"
col: 15012
ensembl_id: "ENSG00000256940"
name: "PPP1R14B antisense RNA 1"
location: "11q13.1"
module: 101
arm: "+"
pooled_cpm: 3.21
n_lines_expressing: 47
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 15
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# PPP1R14B-AS1

*PPP1R14B antisense RNA 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.38× (z +8.4, q 3e-14, up in 20 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.76× (z +4.5, q 0.001, up in 16 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.303× (z -6.8, q 7e-09, down in 28 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM131B-AS2]] (+0.69, fdr 1e-05), [[PHLDA2]] (+0.69, fdr 7e-06), [[LETM2]] (+0.63, fdr 5e-05); moves opposite to [[HSD17B4]] (-0.62, fdr 1e-05), [[NDRG3]] (-0.60, fdr 2e-05), [[OPA1]] (-0.59, fdr 3e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[S100A6]] → it (grade B ⚠); 15 go from it, the strongest it → cells under [[Glycyrrhizic acid (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15012.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.38×** | +8.4 | 3e-14 | 20/23 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.98×** | +7.5 | 1e-11 | 2/3 (HS-578T, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +4.5 | 0.001 | 16/33 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.64×** | +4.0 | 0.010 | 12/40 (SW480, Hs 766T, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +3.6 | 0.028 | 3/6 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.89×** | +3.6 | 0.028 | 16/40 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +3.5 | 0.040 | 7/19 (BT-474, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +3.4 | 0.041 | 12/42 (LoVo, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.82×** | +3.4 | 0.041 | 14/40 (KATO III, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[vincristine (drug)]] 0.5 µM |  | 2.48× | +3.1 | 0.12 | 6/29 (MIA PaCa-2, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | 1.71× | +3.0 | 0.12 | 6/20 (NCI-H2030, SW1417, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15012.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.303×** | -6.8 | 7e-09 | 28/41 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.352×** | -5.9 | 9e-07 | 27/39 (KATO III, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.452×** | -4.5 | 0.001 | 22/40 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.456×** | -4.5 | 0.001 | 22/39 (A549, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.240×** | -4.2 | 0.003 | 24/36 (SW480, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.540×** | -3.5 | 0.044 | 16/41 (HS-578T, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.545×** | -3.4 | 0.045 | 18/40 (NCI-H1573, A549, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.318×** | -3.4 | 0.045 | 12/37 (J82, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.518×** | -3.4 | 0.045 | 14/42 (KATO III, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.669×** | -3.1 | 0.094 | 13/40 (SK-MEL-2, A498, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.578×** | -3.1 | 0.095 | 13/40 (NCI-H23, KATO III, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.682×** | -3.1 | 0.099 | 11/40 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15012. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 4.25 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0483× (z -8.9) |
| [[A549 (line)]] | wt | 4.71 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0302× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 3.54 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0393× (z -9.3) |
| [[KATO III (line)]] | alt | 7.81 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0634× (z -9.6) |
| [[A-172 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.921 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.738 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.825 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.956 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15012), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM131B-AS2]] | +0.69 | +0.52 / +0.71 | both halves | 1e-05 | same gene group |
| [[PHLDA2]] | +0.69 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[LETM2]] | +0.63 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[HOMER1]] | +0.63 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[KCTD11]] | +0.62 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[LUCAT1]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[S100A11]] | +0.61 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[C14orf119]] | +0.60 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[ITGA2-AS1]] | +0.60 | +0.49 / +0.60 | both halves | 1e-05 | same gene group |
| [[S100A13]] | +0.59 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[C2orf92]] | +0.59 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[CLCF1]] | +0.59 | +0.46 / +0.67 | both halves | 2e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSD17B4]] | -0.62 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[NDRG3]] | -0.60 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[OPA1]] | -0.59 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[SOAT1]] | -0.59 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[CCDC6]] | -0.59 | -0.46 / -0.66 | both halves | 2e-05 |  |
| [[EHMT2]] | -0.58 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[KAT7]] | -0.57 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[SUDS3]] | -0.56 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[NUDT21]] | -0.56 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[DFFB]] | -0.55 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[HNRNPA1]] | -0.55 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[SSRP1]] | -0.54 | -0.34 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100A6]] | B | S100A6 activity raises PPP1R14B-AS1's level | lines that do not express S100A6 (5) vs lines expressing it (45) | 1.88× lower at baseline in the lines without S100A6 | 0.089 | ⚠ within organs, on part of the lines; also absent: GPRC5D-AS1, HLA-H, PRRG1; maybe low, not absent; its own permutation p |
| [[PLEKHN1]] | C | PLEKHN1 activity raises PPP1R14B-AS1's level | lines that do not express PLEKHN1 (3) vs lines expressing it (47) | 2.16× lower at baseline in the lines without PLEKHN1 | 0.094 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 0, C 15. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Glycyrrhizic acid (drug)]] 0.05 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], PPP1R14B-AS1 activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.50× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], PPP1R14B-AS1 activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.45× the cells of the other lines | 0.022 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[SBI-0640756 (drug)]] 5 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], PPP1R14B-AS1 activity lowers the cells' numbers under SBI-0640756 5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.48× the cells of the other lines | 0.023 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], PPP1R14B-AS1 activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.42× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[IQ 1 (drug)]] 5 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], PPP1R14B-AS1 activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.69× the cells of the other lines | 0.028 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Cyclosporin A (drug)]] 0.05 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], PPP1R14B-AS1 activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.66× the cells of the other lines | 0.033 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], PPP1R14B-AS1 activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.75× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Lidocaine (hydrochloride) (drug)]] 0.05 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], PPP1R14B-AS1 activity lowers the cells' numbers under Lidocaine (hydrochloride) 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.64× the cells of the other lines | 0.053 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Tolcapone (drug)]] 5 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], PPP1R14B-AS1 activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.77× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Naproxen (drug)]] 5 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], PPP1R14B-AS1 activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.77× the cells of the other lines | 0.066 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], PPP1R14B-AS1 activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.22× the cells of the other lines | 0.070 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Salicylic acid (drug)]] 5 µM | C | [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], PPP1R14B-AS1 activity lowers the cells' numbers under Salicylic acid 5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.21× the cells of the other lines | 0.080 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.709). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.6, -4.1); signed map (1.0, 32.0). **Vector** length 54.4, 9.78% of its response variance represented; |z| ≥ 3 in 727 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +4.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +1.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.3 | +3.1 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.2 | +1.9 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.8 | -3.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | PPP1R14B antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q13.1 — chr11:64,245,838-64,248,221 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54233](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54233) · Entrez [105369340](https://www.ncbi.nlm.nih.gov/gene/105369340) · Ensembl [ENSG00000256940](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000256940)

## Data

Gene col 15012: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15012); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15012, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15012]; `tensor/DDL_lfc|DDL_z.npy` [15012]; `embed/gene_vectors.npy` [15012]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15012 or target_col == 15012). Every well: [[PPP1R14B-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R14B-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
