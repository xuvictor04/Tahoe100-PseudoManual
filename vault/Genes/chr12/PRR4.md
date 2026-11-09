---
symbol: "PRR4"
type: "gene"
col: 3202
ensembl_id: "ENSG00000111215"
name: "proline rich 4"
location: "12p13.2"
module: 26
arm: "+"
pooled_cpm: 4.39
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# PRR4

*proline rich 4* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.34× (z +7.8, q 2e-12, up in 2 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.71× (z +4.9, q 1e-04, up in 12 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.371× (z -9.5, q 1e-18, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRH1]] (+0.88, fdr 7e-06, ⚠ read-through risk), [[SEMA6A-AS1]] (+0.71, fdr 7e-06), [[SLC26A7]] (+0.68, fdr 1e-05), [[FSIP2-AS1]] (+0.67, fdr 1e-05); moves opposite to [[IDH2]] (-0.57, fdr 2e-05), [[IFI27L1]] (-0.56, fdr 2e-05), [[SDHAP4]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[FSIP2-AS1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PRH1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3202.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +7.8 | 2e-12 | 2/3 (C32, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +5.5 | 1e-05 | 8/20 (C32, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.71×** | +4.9 | 1e-04 | 12/46 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.44× | +3.2 | 0.16 | 4/10 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.41× | +3.2 | 0.17 | 7/44 (NCI-H1792, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3202.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.371×** | -9.5 | 1e-18 | 37/47 (SW480, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.416×** | -8.4 | 1e-14 | 28/46 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -8.3 | 2e-14 | 23/39 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.423×** | -8.3 | 2e-14 | 32/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.496×** | -6.5 | 1e-08 | 26/45 (H4, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.522×** | -6.2 | 4e-08 | 23/47 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.543×** | -5.6 | 1e-06 | 17/23 (NCI-H23, NCI-H1573, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.603×** | -4.7 | 2e-04 | 17/37 (hTERT-HPNE, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.410×** | -4.5 | 5e-04 | 16/42 (NCI-H23, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.639×** | -4.3 | 1e-03 | 13/45 (BT-474, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.497×** | -3.5 | 0.023 | 9/42 (A-427, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3202. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 8.42 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0634× (z -10.7) |
| [[A-427 (line)]] | wt | 4.30 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0427× (z -11.7) |
| [[H4 (line)]] | wt | 8.36 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0524× (z -9.5) |
| [[LoVo (line)]] | wt | 6.75 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 7.41 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.128× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.122× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 4.11 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.104× (z -11.3) |
| [[A-172 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3202), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRH1]] | +0.88 | +0.86 / +0.85 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of PRH1 on the same strand (can correlate by spillover, not regulation) |
| [[SEMA6A-AS1]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[SLC26A7]] | +0.68 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[FSIP2-AS1]] | +0.67 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.66 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[TIAM2]] | +0.65 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[ATRX]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[LINC01505]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[CXCL13]] | +0.64 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[SLCO1B1]] | +0.62 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[BPTF]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[COMMD10]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[COLQ]] | +0.61 | +0.65 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDH2]] | -0.57 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[IFI27L1]] | -0.56 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[SDHAP4]] | -0.55 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[MINK1]] | -0.53 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[RAP1A]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[ARPC1A]] | -0.52 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[CERS5]] | -0.51 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[POMGNT2]] | -0.51 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[POGLUT2]] | -0.51 | -0.41 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises PRR4's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without FSIP2-AS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[PMFBP1]] | B | PMFBP1 activity raises PRR4's level | lines that do not express PMFBP1 (8) vs lines expressing it (42) | 1.90× lower at baseline in the lines without PMFBP1 | 0.032 | ⚠ within organs, on part of the lines; also absent: GALNT16, FSIP2-AS1, ENSG00000237356; maybe low, not absent |
| [[LINC01505]] | B | LINC01505 activity raises PRR4's level | lines that do not express LINC01505 (5) vs lines expressing it (45) | 1.87× lower at baseline in the lines without LINC01505 | 0.061 | ⚠ within organs, on part of the lines; also absent: EID2, CENPP, ENSG00000223727; maybe low, not absent |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity strengthens PRR4's drug response | lines that do not express FSIP2-AS1 (6) vs lines expressing it (41) | the lines without FSIP2-AS1 respond 0.49× as strongly (z diff +1.69); strongest at Idarubicin (hydrochloride) 5 µM: 0.86x vs 0.49x (z diff +3.4) | 0.062 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CXCL13]] | B | CXCL13 activity raises PRR4's level | lines that do not express CXCL13 (8) vs lines expressing it (42) | 1.71× lower at baseline in the lines without CXCL13 | 0.077 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises PRR4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC02516]] | B | LINC02516 activity raises PRR4's level | lines that do not express LINC02516 (19) vs lines expressing it (31) | 1.41× lower at baseline in the lines without LINC02516 | 0.091 | ⚠ within organs, on part of the lines; also absent: ADAM23, TEK, SPOCK3 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRH1]] | C | PRR4's natural level strengthens PRH1's drug response | PRR4's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.63; direction not clear | 0.032 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (14.0, 15.4); signed map (22.3, 2.5). **Vector** length 61.7, 8.75% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +3.4 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -0.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +2.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | -3.8 | -5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -8.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.1 | -9.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.7 | -4.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.2 | -8.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -0.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Aprepitant (drug)]] 0.05 µM |  | -1.3 | -1.6 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | proline rich 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:10,845,849-10,849,475 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LPRP; previously PROL4 |
| Matched by | ensembl_id |

UniProt [Q16378](https://www.uniprot.org/uniprotkb/Q16378) carries no function annotation.

**Summary**, from NCBI Gene [11272](https://www.ncbi.nlm.nih.gov/gene/11272):

> This gene encodes a member of the proline-rich protein family that lacks a conserved repetitive domain. This protein may play a role in protective functions in the eye. Alternative splicing result in multiple transcript variants. Read-through transcription also exists between this gene and the upstream PRH1 (proline-rich protein HaeIII subfamily 1) gene. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:18020](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18020) · Entrez [11272](https://www.ncbi.nlm.nih.gov/gene/11272) · UniProt [Q16378](https://www.uniprot.org/uniprotkb/Q16378) · Ensembl [ENSG00000111215](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111215)

## Data

Gene col 3202: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3202); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3202, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3202]; `tensor/DDL_lfc|DDL_z.npy` [3202]; `embed/gene_vectors.npy` [3202]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3202 or target_col == 3202). Every well: [[PRR4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRR4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
