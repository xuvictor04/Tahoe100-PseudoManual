---
symbol: "RHPN1"
type: "gene"
col: 8132
ensembl_id: "ENSG00000158106"
name: "rhophilin Rho GTPase binding protein 1"
location: "8q24.3"
module: 2
arm: "+"
pooled_cpm: 4.48
n_lines_expressing: 43
n_dd_up: 16
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# RHPN1

*rhophilin Rho GTPase binding protein 1* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.21× (z +12.6, q 1e-33, up in 40 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.491× (z -6.2, q 3e-07, down in 17 of 31 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHTF18]] (+0.75, fdr 7e-06), [[KCTD17]] (+0.73, fdr 3e-05), [[TCIRG1]] (+0.69, fdr 3e-05); moves opposite to [[YARS2]] (-0.65, fdr 3e-05), [[AP5M1]] (-0.64, fdr 6e-05), [[METTL6]] (-0.61, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FGFR4]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PLPPR2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8132.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.21×** | +12.6 | 1e-33 | 40/40 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.45×** | +10.9 | 5e-25 | 37/40 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.87×** | +9.2 | 5e-18 | 37/40 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.94×** | +5.8 | 8e-07 | 9/19 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.94×** | +5.6 | 3e-06 | 3/6 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.83×** | +5.3 | 1e-05 | 19/40 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.77×** | +5.0 | 4e-05 | 18/34 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.82×** | +3.7 | 0.013 | 6/21 (PANC-1, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +3.6 | 0.017 | 4/14 (SW480, NCI-H2347, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.20×** | +3.6 | 0.017 | 5/36 (NCI-H23, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.76×** | +3.5 | 0.021 | 11/33 (NCI-H1573, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +3.4 | 0.037 | 8/27 (SW 900, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.49×** | +3.2 | 0.055 | 4/9 (SW480, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.48×** | +3.2 | 0.055 | 3/31 (HEC-1-A, BT-474, …) | inconsistent across doses | position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.63×** | +3.1 | 0.081 | 9/36 (A498, BT-474, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Trimetrexate (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.081 | 7/37 (LS 180, HEC-1-A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8132.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.491×** | -6.2 | 3e-07 | 17/31 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.343×** | -4.9 | 2e-04 | 20/37 (Panc 03.27, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.859× | -4.9 | 2e-04 | 14/41 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.415×** | -4.0 | 0.008 | 18/30 (RKO, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.728×** | -3.9 | 0.010 | 14/30 (MIA PaCa-2, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.736×** | -3.8 | 0.015 | 13/38 (SK-MEL-2, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.686×** | -3.3 | 0.082 | 11/38 (PANC-1, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | 0.701× | -3.1 | 0.13 | 9/38 (C32, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8132. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 6.30 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.87× (z +10.0) | — |
| [[A549 (line)]] | wt | 4.30 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 7.35 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 8.84 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 9.10 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0968× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.817 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.535 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.935 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8132), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHTF18]] | +0.75 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[KCTD17]] | +0.73 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[TCIRG1]] | +0.69 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[CEP131]] | +0.68 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[MATCAP1]] | +0.68 | +0.63 / +0.35 | both halves | 1e-04 |  |
| [[PLA2G4B]] | +0.66 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[BAIAP3]] | +0.65 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[SH3GLB2]] | +0.65 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[MAPK11]] | +0.64 | +0.62 / +0.50 | both halves | 1e-05 | pathway: RHO GTPase Effectors |
| [[SAPCD1]] | +0.63 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[FAM118A]] | +0.62 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[SLC26A6]] | +0.61 | +0.51 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YARS2]] | -0.65 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[AP5M1]] | -0.64 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[METTL6]] | -0.61 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[C3orf38]] | -0.60 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[MFF-DT]] | -0.60 | -0.37 / -0.32 | both halves | 1e-04 |  |
| [[ERCC6L2-AS1]] | -0.59 | -0.37 / -0.28 | both halves | 3e-04 |  |
| [[DNAJB14]] | -0.58 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[CASS4]] | -0.58 | -0.41 / -0.25 | both halves | 4e-04 |  |
| [[TTC33]] | -0.58 | -0.50 / -0.22 | both halves | 6e-04 |  |
| [[ATE1OSP]] | -0.58 | -0.38 / -0.24 | both halves | 5e-04 |  |
| [[THAP2]] | -0.58 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[MAIP1]] | -0.57 | -0.44 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGFR4]] | B | FGFR4 activity raises RHPN1's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 2.25× lower at baseline in the lines without FGFR4 | 0.015 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent |
| [[MLXIPL]] | B | MLXIPL activity raises RHPN1's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 2.37× lower at baseline in the lines without MLXIPL | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent |
| [[ENTPD2]] | B | ENTPD2 activity raises RHPN1's level | lines that do not express ENTPD2 (22) vs lines expressing it (28) | 2.00× lower at baseline in the lines without ENTPD2 | 0.063 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ESRP2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLPPR2]] | B | RHPN1 activity lowers PLPPR2's level | lines that do not express RHPN1 (7) vs lines expressing it (43) | 2.11× higher at baseline in the lines without RHPN1 | 0.084 | ⚠ within organs, on part of the lines; also absent: RHOF, LRRC8B, MBP; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (9.9, -4.5); signed map (-31.0, 1.0). **Vector** length 61.7, 10.7% of its response variance represented; |z| ≥ 3 in 800 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.4 | +12.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.0 | +10.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.6 | +9.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +3.4 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.6 | +3.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.3 | +3.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +3.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +1.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.8 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -6.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.4 | -1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | rhophilin Rho GTPase binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,368,876-143,384,221 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1929, RHPN, ODF5 |
| Gene groups (HGNC) | PDZ domain containing |
| Reactome | 6 pathways, smallest: RHO GTPases Activate Rhotekin and Rhophilins; RHOA GTPase cycle; RHO GTPase Effectors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCX5](https://www.uniprot.org/uniprotkb/Q8TCX5) (Rhophilin-1):

> Has no enzymatic activity. May serve as a target for Rho, and interact with some cytoskeletal component upon Rho binding or relay a Rho signal to other molecules.

**Summary**, from NCBI Gene [114822](https://www.ncbi.nlm.nih.gov/gene/114822):

> Predicted to be involved in negative regulation of stress fiber assembly. Predicted to act upstream of or within several processes, including focal adhesion assembly; glomerular filtration; and renal albumin absorption. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19973](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19973) · Entrez [114822](https://www.ncbi.nlm.nih.gov/gene/114822) · UniProt [Q8TCX5](https://www.uniprot.org/uniprotkb/Q8TCX5) · Ensembl [ENSG00000158106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158106)

## Data

Gene col 8132: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8132); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8132, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8132]; `tensor/DDL_lfc|DDL_z.npy` [8132]; `embed/gene_vectors.npy` [8132]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8132 or target_col == 8132). Every well: [[RHPN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHPN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
