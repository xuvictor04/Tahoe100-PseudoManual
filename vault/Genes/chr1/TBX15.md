---
symbol: "TBX15"
type: "gene"
col: 1704
ensembl_id: "ENSG00000092607"
name: "T-box transcription factor 15"
location: "1p12"
module: 88
arm: "+"
pooled_cpm: 3.82
n_lines_expressing: 43
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# TBX15

*T-box transcription factor 15* — 1p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.53× (z +11.3, q 5e-27, up in 0 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.71× (z +7.1, q 2e-10, up in 8 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.532× (z -5.9, q 2e-06, down in 17 of 38 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02889]] (+0.60, fdr 4e-05), [[IPCEF1]] (+0.59, fdr 2e-05), [[SVEP1]] (+0.56, fdr 2e-05); moves opposite to [[LPCAT2]] (-0.53, fdr 3e-05), [[TBC1D2B]] (-0.52, fdr 7e-05), [[HEBP1]] (-0.50, fdr 7e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GALNT8]] → it (grade B ⚠); 4 go from it, the strongest it → [[SLC2A9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1704.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.53×** | +11.3 | 5e-27 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.88×** | +9.1 | 2e-17 | 1/7 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +7.7 | 2e-12 | 1/10 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +7.1 | 2e-10 | 8/28 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.62×** | +4.2 | 0.002 | 8/36 (LoVo, A498, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.48×** | +3.7 | 0.024 | 9/32 (NCI-H1792, RPMI-7951, …) | all doses, flat |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +3.5 | 0.035 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.41×** | +3.2 | 0.082 | 3/35 (LS 180, NCI-H2347, …) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.62×** | +3.2 | 0.082 | 1/6 (PANC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.39× | +3.1 | 0.13 | 3/14 (NCI-H460, SHP-77, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1704.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.532×** | -5.9 | 2e-06 | 17/38 (NCI-H1792, SHP-77, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.560×** | -5.4 | 2e-05 | 17/37 (HEC-1-A, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.564×** | -5.4 | 2e-05 | 10/14 (NCI-H1792, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.658×** | -3.9 | 0.010 | 10/39 (NCI-H1792, SHP-77, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.658×** | -3.9 | 0.010 | 16/40 (NCI-H1792, HT-29, …) | top dose only | composition shift |
| [[Flumatinib (mesylate) (drug)]] 0.5 µM |  | **0.679×** | -3.5 | 0.051 | 9/38 (SW1417, Panc 03.27, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.689×** | -3.4 | 0.063 | 13/38 (RPMI-7951, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1704. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 39.1 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0760× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.0879× (z -13.7) |
| [[SHP-77 (line)]] | alt | 36.1 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 3.11 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0501× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 8.50 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0462× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.697 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.824 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.984 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.826 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.870 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.972 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.521 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.815 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1704), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02889]] | +0.60 | +0.58 / +0.43 | both halves | 4e-05 |  |
| [[IPCEF1]] | +0.59 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[SVEP1]] | +0.56 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[LINC02268]] | +0.55 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[ABCA6]] | +0.55 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[LINC01287]] | +0.55 | +0.48 / +0.40 | both halves | 4e-05 |  |
| [[FIZ1]] | +0.54 | +0.54 / +0.38 | both halves | 6e-05 |  |
| [[GALNT8]] | +0.54 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[TG]] | +0.53 | +0.51 / +0.32 | both halves | 1e-04 |  |
| [[BAAT]] | +0.53 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[SNTG1]] | +0.52 | +0.55 / +0.36 | both halves | 1e-04 |  |
| [[ZNF34]] | +0.52 | +0.49 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPCAT2]] | -0.53 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[TBC1D2B]] | -0.52 | -0.46 / -0.37 | both halves | 7e-05 |  |
| [[HEBP1]] | -0.50 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[FAM118A]] | -0.50 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[CBFA2T2]] | -0.50 | -0.43 / -0.43 | both halves | 4e-05 |  |
| [[DHTKD1]] | -0.49 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[ECI2]] | -0.49 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[PRKD3]] | -0.48 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[SCAI]] | -0.48 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[ATP7B]] | -0.48 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[PPP1R2]] | -0.47 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[HSPB11]] | -0.47 | -0.39 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT8]] | B | GALNT8 activity lowers TBX15's level | lines that do not express GALNT8 (6) vs lines expressing it (44) | 2.12× higher at baseline in the lines without GALNT8 | 0.054 | ⚠ within organs, on part of the lines; also absent: PRDM6, NOS1, C1orf21; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises TBX15's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC01287]] | B | LINC01287 activity raises TBX15's level | lines that do not express LINC01287 (39) vs lines expressing it (11) | 2.33× lower at baseline in the lines without LINC01287 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2 |
| [[GARIN1B]] | C | GARIN1B activity lowers TBX15's level | lines that do not express GARIN1B (4) vs lines expressing it (46) | 2.04× higher at baseline in the lines without GARIN1B | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PGGHG, ALPK1; maybe low, not absent |
| [[SAMSN1]] | C | SAMSN1 activity weakens TBX15's drug response | lines that do not express SAMSN1 (4) vs lines expressing it (36) | the lines without SAMSN1 respond 1.58× as strongly (z diff -0.50); strongest at Belinostat 5 µM: 0.14x vs 0.47x (z diff -5.2) | 0.093 | ⚠ within organs, on part of the lines; also absent: SYTL2, GNA14, ENSG00000235609; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC2A9]] | B | TBX15 activity raises SLC2A9's level | lines that do not express TBX15 (7) vs lines expressing it (43) | 2.16× lower at baseline in the lines without TBX15 | 0.049 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NRP1]] | B | TBX15 activity raises NRP1's level | lines that do not express TBX15 (7) vs lines expressing it (43) | 2.05× lower at baseline in the lines without TBX15 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC01191]] | B | TBX15 activity raises LINC01191's level | lines that do not express TBX15 (7) vs lines expressing it (43) | 1.41× lower at baseline in the lines without TBX15 | 0.074 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ARMCX4]] | B | TBX15 activity raises ARMCX4's level | lines that do not express TBX15 (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without TBX15 | 0.092 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.477). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (24.7, 22.1); signed map (26.3, 12.8). **Vector** length 47.6, 6.06% of its response variance represented; |z| ≥ 3 in 1,061 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +9.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | -0.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -1.7 | -5.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.8 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | T-box transcription factor 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p12 — chr1:118,883,046-118,989,556 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TBX14 |
| Gene groups (HGNC) | T-box transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96SF7](https://www.uniprot.org/uniprotkb/Q96SF7) (T-box transcription factor TBX15):

> Probable transcriptional regulator involved in the development of the skeleton of the limb, vertebral column and head. Acts by controlling the number of mesenchymal precursor cells and chondrocytes (By similarity).

**Summary**, from NCBI Gene [6913](https://www.ncbi.nlm.nih.gov/gene/6913):

> This gene belongs to the T-box family of genes, which encode a phylogenetically conserved family of transcription factors that regulate a variety of developmental processes. All these genes contain a common T-box DNA-binding domain. Mutations in this gene are associated with Cousin syndrome.[provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:11594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11594) · Entrez [6913](https://www.ncbi.nlm.nih.gov/gene/6913) · UniProt [Q96SF7](https://www.uniprot.org/uniprotkb/Q96SF7) · Ensembl [ENSG00000092607](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092607)

## Data

Gene col 1704: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1704); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1704, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1704]; `tensor/DDL_lfc|DDL_z.npy` [1704]; `embed/gene_vectors.npy` [1704]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1704 or target_col == 1704). Every well: [[TBX15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBX15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
