---
symbol: "FAHD2A"
type: "gene"
col: 3616
ensembl_id: "ENSG00000115042"
name: "fumarylacetoacetate hydrolase domain containing 2A"
location: "2q11.1"
module: 15
arm: "+"
pooled_cpm: 8.98
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# FAHD2A

*fumarylacetoacetate hydrolase domain containing 2A* — 2q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +13.8, q 1e-40, up in 34 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.389× (z -8.4, q 3e-14, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C8orf76]] (+0.72, fdr 1e-05), [[MFSD8]] (+0.68, fdr 7e-06), [[TAF11]] (+0.63, fdr 1e-05); moves opposite to [[HES1]] (-0.56, fdr 2e-05), [[NR4A1]] (-0.53, fdr 3e-05), [[SRSF3]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01139]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3616.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +13.8 | 1e-40 | 34/45 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +9.9 | 8e-21 | 26/38 (SW1417, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +7.8 | 1e-12 | 27/47 (SW 900, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +7.1 | 2e-10 | 22/44 (HEC-1-A, HS-578T, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.8 | 9e-10 | 21/46 (HS-578T, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +6.4 | 1e-08 | 18/47 (AsPC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +5.9 | 3e-07 | 20/47 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.24×** | +5.2 | 1e-05 | 15/48 (A498, C32, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +4.5 | 4e-04 | 12/43 (LS 180, C-33 A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.9 | 0.004 | 11/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.005 | 4/48 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +3.9 | 0.005 | 6/48 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.25×** | +3.7 | 0.009 | 9/47 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.023 | 5/47 (C32, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.039 | 8/47 (SW 900, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.053 | 4/45 (NCI-H1792, SHP-77, …) | inconsistent across doses |  |
| [[Fulvestrant (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.067 | 7/47 (A498, SW480, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +3.0 | 0.087 | 3/48 (SNU-423, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3616.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.389×** | -8.4 | 3e-14 | 26/47 (NCI-H23, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.433×** | -7.4 | 3e-11 | 21/43 (SK-MEL-2, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.662×** | -6.6 | 6e-09 | 18/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.793×** | -3.8 | 0.020 | 11/46 (PANC-1, A549, …) | rises with dose | composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM |  | **0.805×** | -3.5 | 0.053 | 5/47 (NCI-H460, SHP-77, …) | inconsistent across doses |  |
| [[crizotinib (drug)]] 5 µM |  | **0.813×** | -3.4 | 0.064 | 3/47 (NCI-H1573, HT-29, …) | top dose only |  |
| [[Darolutamide (drug)]] 0.05 µM |  | **0.826×** | -3.3 | 0.090 | 5/47 (SW1417, SW 900, …) | inconsistent across doses | position effect removed |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.828×** | -3.2 | 0.092 | 7/48 (NCI-H661, SHP-77, …) | inconsistent across doses |  |
| [[Rucaparib (phosphate) (drug)]] 5 µM |  | 0.828× | -3.1 | 0.11 | 0/48 | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | 0.835× | -3.1 | 0.11 | 11/43 (C-33 A, AN3 CA, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.882× | -3.0 | 0.11 | 14/47 (NCI-H460, A-427, …) | top dose only | composition shift |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 0.882× | -3.0 | 0.11 | 4/48 (SHP-77, SW48, …) | inconsistent across doses |  |
| [[Verapamil (drug)]] 5 µM |  | 0.833× | -3.0 | 0.12 | 5/47 (HT-29, J82, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3616. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.65 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 9.89 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0912× (z -8.5) ⚠ toxic |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0790× (z -10.6) |
| [[KATO III (line)]] | alt | 6.31 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0756× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 26.8 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0547× (z -11.4) |
| [[RKO (line)]] | wt | 9.19 | 0 | 1 | — | [[PH-797804 (drug)]] 0.5 µM 0.0656× (z -8.8) |
| [[A-172 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3616), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C8orf76]] | +0.72 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[MFSD8]] | +0.68 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[TAF11]] | +0.63 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[NUP133]] | +0.63 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[FAM219B]] | +0.62 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[CAPN10-DT]] | +0.61 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[URM1]] | +0.60 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[WDR20]] | +0.60 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[STARD7-AS1]] | +0.60 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[TRAPPC13]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[MIR762HG]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[ZFYVE27]] | +0.59 | +0.49 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HES1]] | -0.56 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[NR4A1]] | -0.53 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SRSF3]] | -0.51 | -0.33 / -0.61 | both halves | 1e-04 |  |
| [[ASXL1]] | -0.51 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[SMARCA5]] | -0.51 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[AIG1]] | -0.50 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[EZR]] | -0.50 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[FOS]] | -0.50 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[ROCK2]] | -0.49 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[TBL1XR1]] | -0.49 | -0.35 / -0.64 | both halves | 1e-04 |  |
| [[KLF2]] | -0.49 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[JUNB]] | -0.49 | -0.32 / -0.55 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01139]] | B | LINC01139 activity raises FAHD2A's level | lines that do not express LINC01139 (24) vs lines expressing it (26) | 1.23× lower at baseline in the lines without LINC01139 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000260289, NTRK3, CTNNA2 |
| [[TOP2A]] | B | TOP2A activity lowers FAHD2A's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.2, 22.9); signed map (-0.1, 0.5). **Vector** length 53.6, 6.78% of its response variance represented; |z| ≥ 3 in 836 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +13.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +9.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +7.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +2.3 | +5.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.0 | -0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.2 | -0.1 |
|  | [[Carbamazepine (drug)]] 0.5 µM |  | +1.1 | +2.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.1 | +2.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.5 | -8.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -2.6 | -3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -6.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Artemether (drug)]] 0.05 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | fumarylacetoacetate hydrolase domain containing 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.1 — chr2:95,402,708-95,416,616 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-105 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GK7](https://www.uniprot.org/uniprotkb/Q96GK7) (Oxaloacetate tautomerase FAHD2A, mitochondrial):

> Tautomerase that converts enol-oxaloacetate, a strong inhibitor of succinate dehydrogenase, to the physiological keto form of oxaloacetate. It is thereby required to maximize aerobic respiration efficiency by preventing succinate dehydrogenase inhibition.

**Summary**, from NCBI Gene [51011](https://www.ncbi.nlm.nih.gov/gene/51011):

> Enables oxaloacetate tautomerase activity. Involved in oxaloacetate metabolic process. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24252](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24252) · Entrez [51011](https://www.ncbi.nlm.nih.gov/gene/51011) · UniProt [Q96GK7](https://www.uniprot.org/uniprotkb/Q96GK7) · Ensembl [ENSG00000115042](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115042)

## Data

Gene col 3616: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3616); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3616, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3616]; `tensor/DDL_lfc|DDL_z.npy` [3616]; `embed/gene_vectors.npy` [3616]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3616 or target_col == 3616). Every well: [[FAHD2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAHD2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
