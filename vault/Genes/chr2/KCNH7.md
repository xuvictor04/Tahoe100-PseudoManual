---
symbol: "KCNH7"
type: "gene"
col: 11557
ensembl_id: "ENSG00000184611"
name: "potassium voltage-gated channel subfamily H member 7"
location: "2q24.2"
module: 9
arm: "+"
pooled_cpm: 7.88
n_lines_expressing: 15
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 24
direction_downstream: 41
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# KCNH7

*potassium voltage-gated channel subfamily H member 7* — 2q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.94× (z +21.1, q 0e+00, up in 4 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.282×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRIA2]] (+0.75, fdr 1e-05), [[ASXL3]] (+0.73, fdr 2e-05), [[KHDRBS2]] (+0.73, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 41 go from it, the strongest it → [[NRXN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11557.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.94×** | +21.1 | 0e+00 | 4/6 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.57×** | +13.9 | 3e-41 | 7/10 (A-427, NCI-H23, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **4.42×** | +11.4 | 5e-28 | 5/10 (BT-474, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.72×** | +10.9 | 1e-25 | 3/8 (NCI-H23, BT-474, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.91×** | +8.2 | 2e-14 | 1/4 (J82) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +6.9 | 5e-10 | 0/2 | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +6.7 | 1e-09 | 0/3 | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.25×** | +6.3 | 3e-08 | 8/9 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.01×** | +5.4 | 4e-06 | 7/10 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +4.9 | 4e-05 | 0/5 | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.9 | 4e-05 | 0/10 | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.86×** | +4.8 | 8e-05 | 8/11 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +4.5 | 4e-04 | 1/5 (J82) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +4.2 | 0.001 | 7/10 (NCI-H23, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +3.9 | 0.003 | 2/8 (NCI-H23, J82) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.00×** | +3.8 | 0.005 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +3.7 | 0.007 | 8/11 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.013 | 2/9 (NCI-H1573, SHP-77) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11557.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.282×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.642× | -3.4 | 0.36 | 2/9 (SHP-77, J82) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.667× | -3.1 | 0.51 | 2/9 (SHP-77, BT-474) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11557. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 4.63 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.99× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 2.17 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 13.9× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 3.05 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 18.3× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 282 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 110 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.34 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11557), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRIA2]] | +0.75 | +0.57 / +0.79 | both halves | 1e-05 | pathway: Neuronal System |
| [[ASXL3]] | +0.73 | +0.48 / +0.84 | both halves | 2e-05 | **novel candidate** |
| [[KHDRBS2]] | +0.73 | +0.58 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[CDH10]] | +0.69 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[LINC02197]] | +0.69 | +0.43 / +0.76 | both halves | 3e-05 |  |
| [[NKAIN2]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[NCAM2]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[CDH12]] | +0.67 | +0.63 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[MARCHF1]] | +0.67 | +0.64 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[LRFN2]] | +0.67 | +0.42 / +0.77 | both halves | 4e-05 | pathway: Neuronal System |
| [[ADGRL3]] | +0.66 | +0.55 / +0.79 | both halves | 1e-05 |  |
| [[KCNB2]] | +0.65 | +0.46 / +0.74 | both halves | 3e-05 | same gene group; pathway: Neuronal System; STRING 423 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 1, C 23. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KCNH7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CALCA]] | C | CALCA activity raises KCNH7's level | lines that do not express CALCA (45) vs lines expressing it (5) | 5.12× lower at baseline in the lines without CALCA | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises KCNH7's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.78× lower at baseline in the lines without RIT2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises KCNH7's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 4.06× lower at baseline in the lines without SYT4 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[GTSF1]] | C | GTSF1 activity raises KCNH7's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 3.66× lower at baseline in the lines without GTSF1 | 0.015 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises KCNH7's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 2.73× lower at baseline in the lines without ASCL1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[PRUNE2]] | C | PRUNE2 activity raises KCNH7's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 1.47× lower at baseline in the lines without PRUNE2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY; co-absent with the target |
| [[LINC01320]] | C | LINC01320 activity raises KCNH7's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 2.24× lower at baseline in the lines without LINC01320 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168; co-absent with the target |
| [[MIR3667HG]] | C | MIR3667HG activity raises KCNH7's level | lines that do not express MIR3667HG (38) vs lines expressing it (12) | 1.83× lower at baseline in the lines without MIR3667HG | 0.022 | ⚠ within organs, on part of the lines; also absent: GTSF1, ENSG00000288098, CALCA; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises KCNH7's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 3.06× lower at baseline in the lines without KCNB2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[CGA]] | C | CGA activity raises KCNH7's level | lines that do not express CGA (44) vs lines expressing it (6) | 3.95× lower at baseline in the lines without CGA | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises KCNH7's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 2.57× lower at baseline in the lines without SRRM4 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*41 arrows, 41 of them with an alert ⚠; grade A 0, B 6, C 35. Shown: the 12 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRXN1]] | B | KCNH7 activity raises NRXN1's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 2.71× lower at baseline in the lines without KCNH7 | 0.031 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent |
| [[SEMA6A]] | B | KCNH7 activity raises SEMA6A's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 3.02× lower at baseline in the lines without KCNH7 | 0.069 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent |
| [[RALYL]] | B | KCNH7 activity raises RALYL's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 3.18× lower at baseline in the lines without KCNH7 | 0.084 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent |
| [[KSR2]] | B | KCNH7 activity raises KSR2's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 2.12× lower at baseline in the lines without KCNH7 | 0.093 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent |
| [[HYDIN]] | B | KCNH7 activity raises HYDIN's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 1.84× lower at baseline in the lines without KCNH7 | 0.097 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent |
| [[UNC80]] | B | KCNH7 activity raises UNC80's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 1.83× lower at baseline in the lines without KCNH7 | 0.097 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent |
| [[CTNNA2]] | C | KCNH7 activity raises CTNNA2's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 6.18× lower at baseline in the lines without KCNH7 | 0.001 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[DACH1]] | C | KCNH7 activity raises DACH1's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 4.30× lower at baseline in the lines without KCNH7 | 0.004 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[RERG]] | C | KCNH7 activity raises RERG's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 3.75× lower at baseline in the lines without KCNH7 | 0.005 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[FUT9]] | C | KCNH7 activity raises FUT9's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 4.20× lower at baseline in the lines without KCNH7 | 0.008 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[CHGB]] | C | KCNH7 activity raises CHGB's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 2.83× lower at baseline in the lines without KCNH7 | 0.013 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[SLITRK6]] | C | KCNH7 activity raises SLITRK6's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 3.25× lower at baseline in the lines without KCNH7 | 0.013 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.5, 35.3); signed map (42.6, 35.7). **Vector** length 25.8, 6.84% of its response variance represented; |z| ≥ 3 in 214 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +3.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.8 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -2.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -1.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -3.1 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel subfamily H member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.2 — chr2:162,371,407-162,838,767 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Kv11.3, HERG3, erg3 |
| Gene groups (HGNC) | Potassium voltage-gated channels; PAS domain containing |
| Reactome | 3 pathways, smallest: Voltage gated Potassium channels; Potassium Channels; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NS40](https://www.uniprot.org/uniprotkb/Q9NS40) (Voltage-gated inwardly rectifying potassium channel KCNH7):

> Pore-forming (alpha) subunit of voltage-gated inwardly rectifying potassium channel. Exhibits faster activation and deactivation kinetics and slow inactivation at membrane potentials positive to 240 mV, resulting in the weakest inward rectification.

**Summary**, from NCBI Gene [90134](https://www.ncbi.nlm.nih.gov/gene/90134):

> Voltage-gated potassium (Kv) channels represent the most complex class of voltage-gated ion channels from both functional and structural standpoints. Their diverse functions include regulating neurotransmitter release, heart rate, insulin secretion, neuronal excitability, epithelial electrolyte transport, smooth muscle contraction, and cell volume. This gene encodes a member of the potassium channel, voltage-gated, subfamily H. This member is a pore-forming (alpha) subunit. There are at least …

**Accessions** — [HGNC:18863](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18863) · Entrez [90134](https://www.ncbi.nlm.nih.gov/gene/90134) · UniProt [Q9NS40](https://www.uniprot.org/uniprotkb/Q9NS40) · Ensembl [ENSG00000184611](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184611)

## Data

Gene col 11557: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11557); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11557, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11557]; `tensor/DDL_lfc|DDL_z.npy` [11557]; `embed/gene_vectors.npy` [11557]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11557 or target_col == 11557). Every well: [[KCNH7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNH7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
