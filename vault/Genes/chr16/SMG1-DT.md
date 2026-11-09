---
symbol: "SMG1-DT"
type: "gene"
col: 15277
ensembl_id: "ENSG00000260352"
name: "SMG1 divergent transcript"
location: "16p12.3"
module: 35
arm: "+"
pooled_cpm: 2.11
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# SMG1-DT

*SMG1 divergent transcript* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.26× (z +16.4, q 0e+00, up in 23 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.452× (z -6.4, q 7e-08, down in 22 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUMO2P17]] (+0.71, fdr 8e-06), [[ATXN7L3-AS1]] (+0.71, fdr 1e-05), [[HEATR4]] (+0.70, fdr 1e-05); moves opposite to [[NBPF3]] (-0.60, fdr 4e-05), [[SDHAF3]] (-0.60, fdr 3e-05), [[ACTR5]] (-0.56, fdr 1e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15277.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.26×** | +16.4 | 0e+00 | 23/25 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.94×** | +11.8 | 7e-30 | 4/4 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.42×** | +9.5 | 5e-19 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.17×** | +9.2 | 3e-18 | 5/8 (PANC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.21×** | +9.0 | 3e-17 | 14/27 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.06×** | +5.4 | 5e-06 | 13/30 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +4.7 | 2e-04 | 2/11 (SW480, NCI-H1573) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.75×** | +4.5 | 6e-04 | 11/37 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.3 | 1e-03 | 6/41 (PANC-1, CFPAC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.71×** | +4.2 | 0.002 | 1/7 (KATO III) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +4.1 | 0.003 | 12/33 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +3.8 | 0.006 | 3/27 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.7 | 0.010 | 1/17 (NCI-H460) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.33×** | +3.1 | 0.066 | 6/40 (NCI-H1573, PANC-1, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.1 | 0.086 | 3/21 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15277.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.452×** | -6.4 | 7e-08 | 22/41 (HT-29, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.472×** | -6.1 | 3e-07 | 21/37 (HT-29, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.522×** | -5.3 | 3e-05 | 15/41 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.345×** | -4.5 | 1e-03 | 13/30 (HT-29, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.691×** | -4.3 | 0.002 | 15/40 (HT-29, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.613×** | -3.7 | 0.024 | 12/38 (HT-29, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.628×** | -3.5 | 0.038 | 8/37 (LS 180, KATO III, …) | inconsistent across doses | position effect removed |
| [[Trimetrexate (drug)]] 5 µM |  | 0.770× | -3.0 | 0.16 | 3/34 (HepG2/C3A, NCI-H1573, …) | top dose only | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.770× | -3.0 | 0.16 | 9/41 (SW 900, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15277. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 7.23 | 0 | 2 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0711× (z -9.7) |
| [[PANC-1 (line)]] | alt | 2.12 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 15.8× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +9.7) | — |
| [[SW480 (line)]] | alt | 2.40 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0734× (z -9.2) |
| [[A-172 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.799 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.884 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.932 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.695 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.882 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.724 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.586 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.544 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.975 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.786 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15277), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUMO2P17]] | +0.71 | +0.62 / +0.57 | both halves | 8e-06 |  |
| [[ATXN7L3-AS1]] | +0.71 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[HEATR4]] | +0.70 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[C1orf54]] | +0.67 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[ZCWPW1]] | +0.67 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[FBXL19-AS1]] | +0.67 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[AP5S1]] | +0.66 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[NEK8]] | +0.66 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[LNCRNA-IUR]] | +0.66 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[MYO16]] | +0.65 | +0.67 / +0.38 | both halves | 7e-05 |  |
| [[MED28-DT]] | +0.65 | +0.53 / +0.51 | both halves | 1e-05 | same gene group |
| [[SRRM2-AS1]] | +0.65 | +0.55 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF3]] | -0.60 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[SDHAF3]] | -0.60 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[ACTR5]] | -0.56 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[ARRB2]] | -0.56 | -0.39 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises SMG1-DT's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises SMG1-DT's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers SMG1-DT's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SEPTIN9-DT]] | B | SEPTIN9-DT activity raises SMG1-DT's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 1.50× lower at baseline in the lines without SEPTIN9-DT | 0.086 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[AXDND1]] | C | AXDND1 activity lowers SMG1-DT's level | lines that do not express AXDND1 (4) vs lines expressing it (46) | 1.81× higher at baseline in the lines without AXDND1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TMCC2, HACE1, P3H4; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | SMG1-DT's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | SMG1-DT's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.59 | 0.491 over the table, 0.079 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.714). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (12.1, 20.8); signed map (26.8, -2.9). **Vector** length 55.9, 9.33% of its response variance represented; |z| ≥ 3 in 840 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +16.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +9.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.3 | -6.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.1 | -5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.1 | -3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -4.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.6 | -6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -4.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Bexarotene (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | SMG1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16p12.3 — chr16:18,926,863-18,937,043 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55394](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55394) · Entrez [107984844](https://www.ncbi.nlm.nih.gov/gene/107984844) · Ensembl [ENSG00000260352](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000260352)

## Data

Gene col 15277: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15277); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15277, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15277]; `tensor/DDL_lfc|DDL_z.npy` [15277]; `embed/gene_vectors.npy` [15277]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15277 or target_col == 15277). Every well: [[SMG1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMG1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
