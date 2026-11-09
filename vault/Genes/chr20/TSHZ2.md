---
symbol: "TSHZ2"
type: "gene"
col: 11287
ensembl_id: "ENSG00000182463"
name: "teashirt zinc finger homeobox 2"
location: "20q13.2"
module: 9
arm: "+"
pooled_cpm: 53.07
n_lines_expressing: 21
n_dd_up: 21
n_dd_down: 11
n_dd_up_clean: 18
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 27
direction_downstream: 38
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# TSHZ2

*teashirt zinc finger homeobox 2* — 20q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.82× (z +19.4, q 0e+00, up in 13 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.683× (z -5.0, q 3e-04, down in 12 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC4A4]] (+0.65, fdr 7e-06), [[PKHD1]] (+0.64, fdr 1e-05), [[MIR4500HG]] (+0.61, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[LINC01091]] → it (grade B ⚠); 38 go from it, the strongest it → [[LINC01091]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11287.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.82×** | +19.4 | 0e+00 | 13/19 (BT-474, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.15×** | +15.2 | 0e+00 | 9/19 (BT-474, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.80×** | +13.1 | 1e-36 | 8/16 (H4, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.72×** | +12.2 | 4e-32 | 6/16 (BT-474, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +12.0 | 3e-31 | 4/19 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.90×** | +12.0 | 3e-31 | 7/19 (BT-474, SW1417, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.25×** | +10.7 | 9e-25 | 14/19 (SW1417, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +6.1 | 8e-08 | 14/19 (NCI-H1573, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +4.9 | 8e-05 | 5/19 (NCI-H1573, BT-474, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.5 | 4e-04 | 10/19 (HepG2/C3A, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +4.3 | 8e-04 | 3/19 (BT-474, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 0.001 | 11/19 (CFPAC-1, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.004 | 2/19 (HT-29, BT-474) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.004 | 2/19 (BT-474, HT-29) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.007 | 4/19 (HT-29, NCI-H1573, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.031 | 1/20 (HepG2/C3A) | rises with dose | position effect removed |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.039 | 4/19 (CFPAC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.044 | 12/18 (CFPAC-1, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11287.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.683×** | -5.0 | 3e-04 | 12/19 (COLO 205, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.717×** | -4.4 | 0.003 | 13/19 (KATO III, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.737×** | -4.0 | 0.010 | 3/18 (KATO III, NCI-H2030, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **0.818×** | -3.8 | 0.023 | 6/19 (KATO III, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.821×** | -3.7 | 0.026 | 9/19 (NCI-H1573, COLO 205, …) | top dose only | low cells (technical?) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.778×** | -3.3 | 0.078 | 5/19 (NCI-H2030, HepG2/C3A, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.781×** | -3.3 | 0.078 | 9/19 (NCI-H1573, CHP-212, …) | two highest doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | **0.781×** | -3.3 | 0.078 | 3/19 (CFPAC-1, HT-29, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.784×** | -3.2 | 0.081 | 8/19 (KATO III, NCI-H1573, …) | top dose only |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.774×** | -3.1 | 0.092 | 1/19 (HT-29) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.636×** | -3.1 | 0.092 | 9/19 (KATO III, AN3 CA, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11287. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 317 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0274× (z -27.4) |
| [[AN3 CA (line)]] | alt | 969 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0483× (z -28.1) |
| [[SHP-77 (line)]] | alt | 423 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -12.5) |
| [[SW480 (line)]] | alt | 67.3 | 0 | 7 (6 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.216× (z -10.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -9.3) |
| [[BT-474 (line)]] | alt | 19.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 8.68× (z +13.0) | — |
| [[SW1417 (line)]] | alt | 44.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.49× (z +12.3) | — |
| [[A498 (line)]] | wt | 475 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -10.3) |
| [[H4 (line)]] | wt | 42.4 | 0 | 1 | — | [[Peretinoin (drug)]] 0.5 µM 0.176× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 15.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.08× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 14.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.39× (z +11.7) | — |
| [[NCI-H1573 (line)]] | alt | 46.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.72× (z +9.8) | — |
| [[A-172 (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.29 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.48 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.80 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.5 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 82.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.82 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.94 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.02 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.58 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.44 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.29 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.75 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.63 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.79 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.42 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.29 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.36 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.50 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.88 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.71 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.48 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.81 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.05 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.53 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.92 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.48 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11287), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC4A4]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[PKHD1]] | +0.64 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[MIR4500HG]] | +0.61 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[AGMO]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[SNTG1]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[LINC01091]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[RUNX1T1]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[FGF13]] | +0.56 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[RMST]] | +0.56 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[STXBP5L]] | +0.56 | +0.37 / +0.59 | both halves | 7e-05 |  |
| [[WDR72]] | +0.55 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[PPARGC1A]] | +0.54 | +0.45 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 5, C 22. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01091]] | B | LINC01091 activity raises TSHZ2's level | lines that do not express LINC01091 (16) vs lines expressing it (34) | 2.17× lower at baseline in the lines without LINC01091 | 0.033 | ⚠ within organs, on part of the lines; also absent: TOX3, BCAS1; maybe low, not absent |
| [[PRKG1]] | B | PRKG1 activity raises TSHZ2's level | lines that do not express PRKG1 (23) vs lines expressing it (27) | 2.70× lower at baseline in the lines without PRKG1 | 0.039 | ⚠ within organs, on part of the lines; also absent: NTNG1, CAMK4, DSCAM; maybe low, not absent |
| [[SPATA6L]] | B | SPATA6L activity raises TSHZ2's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 1.90× lower at baseline in the lines without SPATA6L | 0.042 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[NCALD]] | B | NCALD activity raises TSHZ2's level | lines that do not express NCALD (18) vs lines expressing it (32) | 2.61× lower at baseline in the lines without NCALD | 0.076 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers TSHZ2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[PKHD1]] | C | PKHD1 activity raises TSHZ2's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 2.89× lower at baseline in the lines without PKHD1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent; co-absent with the target |
| [[FGF13]] | C | FGF13 activity raises TSHZ2's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 2.60× lower at baseline in the lines without FGF13 | 0.003 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11; co-absent with the target |
| [[PROX1-AS1]] | C | PROX1-AS1 activity raises TSHZ2's level | lines that do not express PROX1-AS1 (29) vs lines expressing it (21) | 3.25× lower at baseline in the lines without PROX1-AS1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises TSHZ2's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 7.44× lower at baseline in the lines without RUNX1T1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[PROX1]] | C | PROX1 activity raises TSHZ2's level | lines that do not express PROX1 (30) vs lines expressing it (20) | 2.47× lower at baseline in the lines without PROX1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964; co-absent with the target |
| [[PPARGC1A]] | C | PPARGC1A activity raises TSHZ2's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 2.26× lower at baseline in the lines without PPARGC1A | 0.010 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2; co-absent with the target |
| [[ST18]] | C | ST18 activity raises TSHZ2's level | lines that do not express ST18 (39) vs lines expressing it (11) | 5.30× lower at baseline in the lines without ST18 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 12, C 26. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01091]] | B | TSHZ2 activity raises LINC01091's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 2.96× lower at baseline in the lines without TSHZ2 | 0.001 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5 |
| [[LINC02466]] | B | TSHZ2 activity raises LINC02466's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 1.65× lower at baseline in the lines without TSHZ2 | 0.027 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5 |
| [[FHDC1]] | B | TSHZ2 activity raises FHDC1's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 1.69× lower at baseline in the lines without TSHZ2 | 0.034 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5 |
| [[FHDC1]] | B | TSHZ2 activity weakens FHDC1's drug response | lines that do not express TSHZ2 (27) vs lines expressing it (19) | the lines without TSHZ2 respond 1.34× as strongly (z diff -0.44); strongest at Panobinostat 0.5 µM: 1.76x vs 0.97x (z diff -2.4) | 0.034 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5; target measured in part of the lines; artifact flags |
| [[RAB17]] | B | TSHZ2 activity raises RAB17's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 1.80× lower at baseline in the lines without TSHZ2 | 0.038 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5 |
| [[NCKAP5]] | B | TSHZ2 activity raises NCKAP5's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 2.37× lower at baseline in the lines without TSHZ2 | 0.041 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5 |
| [[NCALD]] | B | TSHZ2 activity raises NCALD's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 2.25× lower at baseline in the lines without TSHZ2 | 0.046 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5 |
| [[AKR1C3]] | B | TSHZ2 activity raises AKR1C3's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 2.33× lower at baseline in the lines without TSHZ2 | 0.063 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5 |
| [[SPATA6L]] | B | TSHZ2 activity raises SPATA6L's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 1.93× lower at baseline in the lines without TSHZ2 | 0.067 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5 |
| [[MAN1A1]] | B | TSHZ2 activity raises MAN1A1's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 2.19× lower at baseline in the lines without TSHZ2 | 0.079 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5 |
| [[LINC02223]] | B | TSHZ2 activity raises LINC02223's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 1.66× lower at baseline in the lines without TSHZ2 | 0.087 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5 |
| [[SOX5]] | B | TSHZ2 activity raises SOX5's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 2.20× lower at baseline in the lines without TSHZ2 | 0.097 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5 |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.566). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.4, 42.8); signed map (48.5, 31.8). **Vector** length 66.5, 19.8% of its response variance represented; |z| ≥ 3 in 531 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.8 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.6 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.2 | +12.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +19.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +12.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.2 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.2 | -3.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -4.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -3.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | teashirt zinc finger homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.2 — chr20:52,972,358-53,495,330 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZABC2, OVC10-2, TSH2; previously C20orf17, ZNF218 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; ZF class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRE2](https://www.uniprot.org/uniprotkb/Q9NRE2) (Teashirt homolog 2):

> Probable transcriptional regulator involved in developmental processes. May act as a transcriptional repressor (Potential).

**Summary**, from NCBI Gene [128553](https://www.ncbi.nlm.nih.gov/gene/128553):

> This gene is a member of the teashirt C2H2-type zinc-finger protein family of transcription factors. This gene encodes a protein with five C2H2-type zinc fingers, a homeobox DNA-binding domain and a coiled-coil domain. This nuclear protein is predicted to act as a transcriptional repressor. This gene is thought to play a role in the development and progression of breast and other types of cancer. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided …

**Accessions** — [HGNC:13010](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13010) · Entrez [128553](https://www.ncbi.nlm.nih.gov/gene/128553) · UniProt [Q9NRE2](https://www.uniprot.org/uniprotkb/Q9NRE2) · Ensembl [ENSG00000182463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182463)

## Data

Gene col 11287: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11287); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11287, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11287]; `tensor/DDL_lfc|DDL_z.npy` [11287]; `embed/gene_vectors.npy` [11287]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11287 or target_col == 11287). Every well: [[TSHZ2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSHZ2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
