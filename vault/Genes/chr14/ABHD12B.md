---
symbol: "ABHD12B"
type: "gene"
col: 5262
ensembl_id: "ENSG00000131969"
name: "abhydrolase domain containing 12B"
location: "14q22.1"
module: 55
arm: "+"
pooled_cpm: 7.37
n_lines_expressing: 46
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 13
direction_downstream: 1
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# ABHD12B

*abhydrolase domain containing 12B* — 14q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.46× (z +9.6, q 2e-19, up in 9 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +4.1, q 0.007, up in 3 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.597× (z -5.6, q 2e-05, down in 13 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPOAP1-AS1]] (+0.58, fdr 3e-05), [[PRSS48]] (+0.55, fdr 4e-05), [[LINC02058]] (+0.55, fdr 3e-05); moves opposite to [[AKAP11]] (-0.42, fdr 8e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[CALB1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TMPRSS2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5262.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.46×** | +9.6 | 2e-19 | 9/14 (SW480, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +9.6 | 2e-19 | 4/5 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.60×** | +9.5 | 6e-19 | 1/7 (A498) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.007 | 3/32 (LOX-IMVI, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +3.9 | 0.009 | 3/28 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.011 | 3/39 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.97×** | +3.8 | 0.011 | 1/5 (SW480) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +3.7 | 0.014 | 1/15 (SW480) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +3.7 | 0.015 | 2/25 (HEC-1-A, C32) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.56×** | +3.4 | 0.039 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.3 | 0.049 | 2/16 (A498, NCI-H23) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.049 | 4/33 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.33× | +3.0 | 0.11 | 4/29 (A498, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5262.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.597×** | -5.6 | 2e-05 | 13/40 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.625×** | -5.1 | 1e-04 | 15/40 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.745×** | -4.5 | 0.001 | 14/32 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.680×** | -4.2 | 0.004 | 13/41 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.686×** | -4.1 | 0.005 | 11/30 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.693×** | -3.8 | 0.013 | 13/36 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Decitabine (drug)]] 5 µM |  | **0.721×** | -3.4 | 0.055 | 10/39 (RPMI-7951, Hs 766T, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.566×** | -3.2 | 0.095 | 5/36 (SW480, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Malotilate (drug)]] 0.5 µM |  | 0.757× | -3.0 | 0.17 | 7/38 (SW 900, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5262. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 36.0 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0984× (z -16.5) |
| [[LoVo (line)]] | wt | 75.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0673× (z -17.7) |
| [[NCI-H23 (line)]] | alt | 4.11 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0809× (z -8.7) |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0912× (z -11.7) |
| [[Hs 766T (line)]] | wt | 3.54 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -8.9) |
| [[LS 180 (line)]] | wt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -11.8) |
| [[A-172 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5262), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPOAP1-AS1]] | +0.58 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[PRSS48]] | +0.55 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[LINC02058]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[LINC01819]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[TFF3]] | +0.52 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[CLRN3]] | +0.52 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[TPRXL]] | +0.52 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[LGR5]] | +0.52 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[CALB1]] | +0.52 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[IL20RA]] | +0.52 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[TFF1]] | +0.52 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[TPTEP1-1]] | +0.51 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP11]] | -0.42 | -0.37 / -0.48 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALB1]] | B | CALB1 activity raises ABHD12B's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 3.63× lower at baseline in the lines without CALB1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588 |
| [[VSNL1]] | B | VSNL1 activity raises ABHD12B's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 2.12× lower at baseline in the lines without VSNL1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[LGR5]] | B | LGR5 activity raises ABHD12B's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 2.47× lower at baseline in the lines without LGR5 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573 |
| [[GRIN2B]] | B | GRIN2B activity raises ABHD12B's level | lines that do not express GRIN2B (40) vs lines expressing it (10) | 2.82× lower at baseline in the lines without GRIN2B | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000237031, ENSG00000248588 |
| [[LINC02582]] | B | LINC02582 activity raises ABHD12B's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 2.04× lower at baseline in the lines without LINC02582 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975 |
| [[CLRN3]] | B | CLRN3 activity raises ABHD12B's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 2.83× lower at baseline in the lines without CLRN3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13 |
| [[MMP28]] | B | MMP28 activity raises ABHD12B's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.29× lower at baseline in the lines without MMP28 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[CEMIP]] | B | CEMIP activity raises ABHD12B's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 1.59× lower at baseline in the lines without CEMIP | 0.070 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[LINC01819]] | B | LINC01819 activity raises ABHD12B's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 1.65× lower at baseline in the lines without LINC01819 | 0.081 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises ABHD12B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TPTEP1-1]] | B | TPTEP1-1 activity raises ABHD12B's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 1.98× lower at baseline in the lines without TPTEP1-1 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975 |
| [[LINC02058]] | B | LINC02058 activity raises ABHD12B's level | lines that do not express LINC02058 (34) vs lines expressing it (16) | 1.92× lower at baseline in the lines without LINC02058 | 0.099 | ⚠ within organs, on part of the lines; also absent: LINC02253, ENSG00000260573, ST18; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMPRSS2]] | C | ABHD12B activity lowers TMPRSS2's level | lines that do not express ABHD12B (4) vs lines expressing it (46) | 3.09× higher at baseline in the lines without ABHD12B | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC00907, DNAH6, ESRRB; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.7, 46.0); signed map (65.5, 12.3). **Vector** length 40.0, 4.30% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +0.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.3 | -4.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -0.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | abhydrolase domain containing 12B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.1 — chr14:50,872,053-50,904,970 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BEM46L3; previously C14orf29 |
| Gene groups (HGNC) | Abhydrolase domain containing |
| Matched by | ensembl_id |

UniProt [Q7Z5M8](https://www.uniprot.org/uniprotkb/Q7Z5M8) carries no function annotation.

**Summary**, from NCBI Gene [145447](https://www.ncbi.nlm.nih.gov/gene/145447):

> Predicted to enable monoacylglycerol lipase activity and phosphatidylcholine lysophospholipase A1 activity. Predicted to be involved in monoacylglycerol catabolic process and phosphatidylserine catabolic process. Predicted to be active in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19837](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19837) · Entrez [145447](https://www.ncbi.nlm.nih.gov/gene/145447) · UniProt [Q7Z5M8](https://www.uniprot.org/uniprotkb/Q7Z5M8) · Ensembl [ENSG00000131969](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131969)

## Data

Gene col 5262: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5262); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5262, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5262]; `tensor/DDL_lfc|DDL_z.npy` [5262]; `embed/gene_vectors.npy` [5262]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5262 or target_col == 5262). Every well: [[ABHD12B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD12B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
