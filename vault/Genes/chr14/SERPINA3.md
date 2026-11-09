---
symbol: "SERPINA3"
type: "gene"
col: 12136
ensembl_id: "ENSG00000196136"
name: "serpin family A member 3"
location: "14q32.13"
module: 139
arm: "+"
pooled_cpm: 67.63
n_lines_expressing: 14
n_dd_up: 29
n_dd_down: 9
n_dd_up_clean: 25
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 14
direction_downstream: 12
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# SERPINA3

*serpin family A member 3* — 14q32.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.28× (z +8.5, q 1e-14, up in 8 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.346× (z -7.7, q 5e-12, down in 12 of 12 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFITM2]] (+0.67, fdr 1e-05), [[FGB]] (+0.65, fdr 7e-06), [[SECTM1]] (+0.62, fdr 5e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[SAA2-SAA4]], [[SAA4]] → it (grade B ⚠); 12 go from it, the strongest it → [[LINC02343]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12136.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.28×** | +8.5 | 1e-14 | 8/12 (CFPAC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **2.88×** | +7.7 | 4e-12 | 5/12 (CFPAC-1, PANC-1, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.67×** | +7.1 | 2e-10 | 9/12 (CFPAC-1, SNU-423, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.63×** | +7.1 | 2e-10 | 8/12 (CFPAC-1, PANC-1, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **2.52×** | +6.7 | 2e-09 | 6/12 (CFPAC-1, SNU-423, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **2.23×** | +5.8 | 5e-07 | 5/12 (CFPAC-1, PANC-1, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.18×** | +5.5 | 4e-06 | 6/12 (CFPAC-1, SNU-423, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +5.4 | 4e-06 | 5/14 (CFPAC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.09×** | +5.4 | 5e-06 | 1/12 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **2.04×** | +5.2 | 1e-05 | 7/12 (CFPAC-1, SNU-423, …) | all doses, flat | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **2.03×** | +5.1 | 1e-05 | 6/12 (CFPAC-1, SNU-423, …) | all doses, flat | position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +4.9 | 3e-05 | 6/12 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.62×** | +4.9 | 3e-05 | 6/12 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **2.04×** | +4.8 | 6e-05 | 8/12 (CFPAC-1, PANC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +4.6 | 1e-04 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +4.5 | 2e-04 | 7/12 (CFPAC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.86×** | +4.5 | 2e-04 | 6/12 (CFPAC-1, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12136.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.346×** | -7.7 | 5e-12 | 12/12 (BT-474, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.459×** | -5.7 | 4e-06 | 11/12 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.472×** | -5.5 | 8e-06 | 11/12 (HepG2/C3A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.479×** | -5.4 | 1e-05 | 9/12 (SK-MEL-2, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.595×** | -3.8 | 0.017 | 11/13 (BT-474, SK-MEL-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.386×** | -3.6 | 0.027 | 10/13 (BT-474, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.611×** | -3.6 | 0.027 | 10/12 (HepG2/C3A, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.715×** | -3.5 | 0.039 | 9/12 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.724×** | -3.3 | 0.053 | 9/13 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.746× | -3.0 | 0.14 | 10/12 (BT-474, SK-MEL-2, …) | top dose only | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12136. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 660 | 0 | 13 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.00922× (z -33.1) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.144× (z -14.3) |
| [[CFPAC-1 (line)]] | alt | 45.7 | 11 | 2 | [[Clobetasol propionate (drug)]] 0.05 µM 11.0× (z +11.0) | [[Tofacitinib (drug)]] 5 µM 0.246× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 1,897 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -18.3) |
| [[SK-MEL-2 (line)]] | alt | 640 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0407× (z -31.8) |
| [[MIA PaCa-2 (line)]] | alt | 414 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0918× (z -22.8) |
| [[C32 (line)]] | wt | 264 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -16.2) |
| [[Panc 03.27 (line)]] | alt | 85.6 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0638× (z -15.6) |
| [[KATO III (line)]] | alt | 36.2 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0865× (z -11.9) |
| [[SNU-423 (line)]] | alt | 36.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 17.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -8.8) |
| [[A-172 (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.87 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.35 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.95 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.30 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.60 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.12 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.96 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.87 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.46 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.69 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.08 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.56 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.96 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.62 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.76 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.95 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.43 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.39 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.89 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.64 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.03 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.09 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.16 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.76 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.98 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.91 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.97 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12136), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFITM2]] | +0.67 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[FGB]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 590 |
| [[SECTM1]] | +0.62 | +0.39 / +0.66 | both halves | 5e-05 |  |
| [[SERPINA1]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ESTROGEN_RESPONSE_LATE; STRING 680 |
| [[SLPI]] | +0.59 | +0.45 / +0.58 | both halves | 3e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP; STRING 422 |
| [[BCL6]] | +0.59 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[FGG]] | +0.59 | +0.56 / +0.63 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation; STRING 499 |
| [[SAA4]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 | STRING 481 |
| [[SAA2-SAA4]] | +0.59 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[SAA2]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 | STRING 532 |
| [[IFITM3]] | +0.56 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[CEBPD]] | +0.55 | +0.38 / +0.63 | both halves | 7e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 4, C 10. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAA2-SAA4]], [[SAA4]] | B | SAA2-SAA4, SAA4 activity raises SERPINA3's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 2.33× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.046 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[NR3C1]] | B | NR3C1 activity raises SERPINA3's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[HDAC6]] | B | HDAC6 activity raises SERPINA3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SAA2]] | B | SAA2 activity raises SERPINA3's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 2.32× lower at baseline in the lines without SAA2 | 0.085 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3 |
| [[SERPINA1]] | C | SERPINA1 activity raises SERPINA3's level | lines that do not express SERPINA1 (34) vs lines expressing it (16) | 5.51× lower at baseline in the lines without SERPINA1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SERPINA5, CST6, SERPINA3; co-absent with the target |
| [[LRG1]] | C | LRG1 activity raises SERPINA3's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 3.42× lower at baseline in the lines without LRG1 | 0.018 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM; co-absent with the target |
| [[SERPINA5]] | C | SERPINA5 activity raises SERPINA3's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 5.81× lower at baseline in the lines without SERPINA5 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546; co-absent with the target |
| [[FGB]] | C | FGB activity raises SERPINA3's level | lines that do not express FGB (42) vs lines expressing it (8) | 5.19× lower at baseline in the lines without FGB | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2; co-absent with the target |
| [[B3GNT7]] | C | B3GNT7 activity raises SERPINA3's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 3.60× lower at baseline in the lines without B3GNT7 | 0.053 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2; co-absent with the target |
| [[KRT23]] | C | KRT23 activity raises SERPINA3's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 4.90× lower at baseline in the lines without KRT23 | 0.053 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP; co-absent with the target |
| [[SMIM2-AS1]] | C | SMIM2-AS1 activity raises SERPINA3's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 2.07× lower at baseline in the lines without SMIM2-AS1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent; co-absent with the target |
| [[A2M]] | C | A2M activity raises SERPINA3's level | lines that do not express A2M (42) vs lines expressing it (8) | 6.80× lower at baseline in the lines without A2M | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, TF, LHFPL3-AS1; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 4, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02343]] | B | SERPINA3 activity raises LINC02343's level | lines that do not express SERPINA3 (36) vs lines expressing it (14) | 1.80× lower at baseline in the lines without SERPINA3 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000286546, LINC02099, SERPINA5 |
| [[TRABD2B]] | B | SERPINA3 activity raises TRABD2B's level | lines that do not express SERPINA3 (36) vs lines expressing it (14) | 1.13× lower at baseline in the lines without SERPINA3 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000286546, LINC02099, SERPINA5 |
| [[RNF213]] | B | SERPINA3 activity raises RNF213's level | lines that do not express SERPINA3 (36) vs lines expressing it (14) | 1.36× lower at baseline in the lines without SERPINA3 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000286546, LINC02099, SERPINA5 |
| [[MUC1]] | B | SERPINA3 activity raises MUC1's level | lines that do not express SERPINA3 (36) vs lines expressing it (14) | 2.39× lower at baseline in the lines without SERPINA3 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000286546, LINC02099, SERPINA5 |
| [[SMIM2-AS1]] | C | SERPINA3 activity raises SMIM2-AS1's level | lines that do not express SERPINA3 (36) vs lines expressing it (14) | 1.43× lower at baseline in the lines without SERPINA3 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000286546, LINC02099, SERPINA5; co-absent with the target |
| [[SERPINA1]] | C | SERPINA3 activity raises SERPINA1's level | lines that do not express SERPINA3 (36) vs lines expressing it (14) | 3.41× lower at baseline in the lines without SERPINA3 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000286546, LINC02099, SERPINA5; co-absent with the target |
| [[A2M]] | C | SERPINA3 activity raises A2M's level | lines that do not express SERPINA3 (36) vs lines expressing it (14) | 3.10× lower at baseline in the lines without SERPINA3 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000286546, LINC02099, SERPINA5; co-absent with the target |
| [[SERPINA5]] | C | SERPINA3 activity raises SERPINA5's level | lines that do not express SERPINA3 (36) vs lines expressing it (14) | 3.09× lower at baseline in the lines without SERPINA3 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000286546, LINC02099, SERPINA5; co-absent with the target |
| [[SAMMSON]] | C | SERPINA3 activity raises SAMMSON's level | lines that do not express SERPINA3 (36) vs lines expressing it (14) | 1.94× lower at baseline in the lines without SERPINA3 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000286546, LINC02099, SERPINA5; co-absent with the target |
| [[LRG1]] | C | SERPINA3 activity raises LRG1's level | lines that do not express SERPINA3 (36) vs lines expressing it (14) | 2.27× lower at baseline in the lines without SERPINA3 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000286546, LINC02099, SERPINA5; co-absent with the target |
| [[KRT23]] | C | SERPINA3 activity raises KRT23's level | lines that do not express SERPINA3 (36) vs lines expressing it (14) | 2.07× lower at baseline in the lines without SERPINA3 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000286546, LINC02099, SERPINA5; co-absent with the target |
| [[LEF1-AS1]] | C | SERPINA3 activity raises LEF1-AS1's level | lines that do not express SERPINA3 (36) vs lines expressing it (14) | 1.59× lower at baseline in the lines without SERPINA3 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000286546, LINC02099, SERPINA5; co-absent with the target |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.3, 49.0); signed map (55.5, 24.7). **Vector** length 67.4, 22.3% of its response variance represented; |z| ≥ 3 in 581 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +8.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.8 | +7.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.7 | +7.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.6 | +4.9 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.4 | -3.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | serpin family A member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.13 — chr14:94,612,384-94,624,055 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ACT; previously AACT |
| Gene groups (HGNC) | Serpin peptidase inhibitors |
| Hallmark sets | KRAS_SIGNALING_UP, ESTROGEN_RESPONSE_LATE |
| Reactome | 6 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [P01011](https://www.uniprot.org/uniprotkb/P01011) (Alpha-1-antichymotrypsin):

> Although its physiological function is unclear, it can inhibit neutrophil cathepsin G and mast cell chymase, both of which can convert angiotensin-1 to the active angiotensin-2.

**Summary**, from NCBI Gene [12](https://www.ncbi.nlm.nih.gov/gene/12):

> The protein encoded by this gene is a member of the serpin family of proteins, a group of proteins that inhibit serine proteases. This gene is one in a cluster of serpin genes located on the q arm of chromosome 14. Polymorphisms in this protein appear to be tissue specific and influence protease targeting. Variations in this protein's sequence have been implicated in Alzheimer's disease, and deficiency of this protein has been associated with liver disease. Mutations have been identified in …

**Accessions** — [HGNC:16](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16) · Entrez [12](https://www.ncbi.nlm.nih.gov/gene/12) · UniProt [P01011](https://www.uniprot.org/uniprotkb/P01011) · Ensembl [ENSG00000196136](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196136)

## Data

Gene col 12136: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12136); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12136, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12136]; `tensor/DDL_lfc|DDL_z.npy` [12136]; `embed/gene_vectors.npy` [12136]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12136 or target_col == 12136). Every well: [[SERPINA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPINA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
