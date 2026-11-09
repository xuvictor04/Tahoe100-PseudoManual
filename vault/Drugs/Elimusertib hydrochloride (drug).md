---
drug: "Elimusertib hydrochloride"
type: "drug"
salt_base: "Elimusertib hydrochloride"
targets: "ATR"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 887
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Elimusertib hydrochloride

*unclear (inhibitor/antagonist) · targets: ATR · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 887 / 35 / 427; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.44 / 0.44.
> Flags by dose: - / noisy plate (z scaled) / toxic; noisy plate (z scaled). ⚠ 5 µM: toxic (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:F8 | 500 / 387 | — | -0.32 | -2.4/-1.3/-1.1 | — |
| 0.5 µM | [[Plate 02]]:F8 | 5 / 30 | — | +0.24 | -1.9/-1.6/-0.8 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:F8 | 172 / 255 | — | -1.02 | -2.0/-1.1/+0.3 | ⚠ toxic · noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (500 genes, none with an alert; 12 shown): [[CFB]] 2.66× (z +8.0, 24/27 lines), [[GBP2]] 1.99× (z +7.5, 25/35 lines), [[APOL6]] 1.46× (z +6.4, 25/42 lines), [[KRT80]] 1.66× (z +6.1, 15/26 lines), [[GBP1]] 2.00× (z +5.9, 25/32 lines), [[TLR3]] 2.08× (z +5.8, 14/33 lines), [[PLCH1]] 1.61× (z +5.8, 21/36 lines), [[POT1-AS1]] 1.77× (z +5.7, 20/44 lines), [[OLFML2A]] 1.74× (z +5.7, 14/26 lines), [[JDP2]] 1.51× (z +5.6, 15/33 lines), [[RNF213]] 1.46× (z +5.3, 38/48 lines), [[SYTL2]] 1.54× (z +5.3, 23/41 lines)

**0.5 µM** (5 genes, none with an alert): [[GBP2]] 1.51× (z +3.5, 4/36 lines), [[FBXO16]] 1.42× (z +3.3, 14/39 lines), [[EPB41]] 1.31× (z +3.1, 10/47 lines), [[MIA2]] 1.24× (z +3.1, 11/50 lines), [[AARS1]] 1.30× (z +2.8, 5/50 lines)

**5 µM** (172 genes, 172 with an alert ⚠; the drug-dose carries ⚠ toxic; 12 shown): [[CYP1B1]] ⚠ 4.50× (z +5.1, 15/17 lines), [[GBP2]] ⚠ 2.46× (z +5.0, 20/33 lines), [[AKR1C1]] ⚠ 2.56× (z +4.9, 14/21 lines), [[TRAFD1]] ⚠ 1.62× (z +4.7, 19/43 lines), [[ENSG00000230490]] ⚠ 1.94× (z +4.6, 6/16 lines), [[BMF]] ⚠ 3.87× (z +4.5, 3/16 lines), [[PIR]] ⚠ 1.85× (z +4.5, 15/35 lines), [[MYPN]] ⚠ 2.16× (z +4.4, 11/16 lines), [[NNMT]] ⚠ 2.49× (z +4.4, 10/22 lines), [[HECW2]] ⚠ 1.88× (z +4.3, 9/22 lines), [[CFB]] ⚠ 2.90× (z +4.3, 15/23 lines), [[UGT1A6]] ⚠ 2.15× (z +4.3, 6/12 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (387 genes, none with an alert; 12 shown): [[ETV4]] 0.381× (z -12.2, 34/45 lines), [[SPRY4]] 0.372× (z -12.2, 43/48 lines), [[ETV5]] 0.517× (z -10.7, 42/48 lines), [[SPRY4-AS1]] 0.345× (z -10.4, 41/45 lines), [[ITGA2]] 0.418× (z -10.0, 32/37 lines), [[NT5E]] 0.393× (z -10.0, 30/34 lines), [[ITGB5]] 0.560× (z -9.6, 34/46 lines), [[DUSP6]] 0.303× (z -9.3, 42/44 lines), [[CDCP1]] 0.572× (z -8.7, 27/32 lines), [[MYEOV]] 0.456× (z -8.5, 22/29 lines), [[ELK3]] 0.545× (z -7.9, 33/44 lines), [[SPRED2]] 0.592× (z -7.5, 45/48 lines)

**0.5 µM** (30 genes, none with an alert; 12 shown): [[ELK3]] 0.715× (z -4.0, 22/46 lines), [[ETV4]] 0.677× (z -3.9, 9/45 lines), [[CD59]] 0.735× (z -3.8, 26/43 lines), [[SPRY4]] 0.667× (z -3.7, 20/48 lines), [[CCND1]] 0.691× (z -3.6, 23/43 lines), [[CD44]] 0.774× (z -3.6, 23/35 lines), [[ETV5]] 0.761× (z -3.6, 12/50 lines), [[B4GALT6]] 0.755× (z -3.5, 5/39 lines), [[KIAA0040]] 0.697× (z -3.5, 11/24 lines), [[EGR1]] 0.531× (z -3.5, 36/48 lines), [[NT5E]] 0.678× (z -3.3, 21/36 lines), [[ARHGAP31]] 0.711× (z -3.3, 5/38 lines)

**5 µM** (255 genes, 255 with an alert ⚠; the drug-dose carries ⚠ toxic; 12 shown): [[ETV5]] ⚠ 0.139× (z -14.1, 41/46 lines), [[SPRY4-AS1]] ⚠ 0.193× (z -8.9, 42/42 lines), [[DUSP4]] ⚠ 0.307× (z -8.9, 30/31 lines), [[ZFPM2-AS1]] ⚠ 0.374× (z -8.1, 28/30 lines), [[CCND1]] ⚠ 0.342× (z -7.9, 38/39 lines), [[SPRED1]] ⚠ 0.370× (z -7.9, 44/46 lines), [[MYEOV]] ⚠ 0.289× (z -7.4, 24/28 lines), [[NT5E]] ⚠ 0.250× (z -7.1, 27/32 lines), [[ETV1]] ⚠ 0.239× (z -7.1, 28/34 lines), [[HMGA2]] ⚠ 0.319× (z -7.1, 35/37 lines), [[SPRY4]] ⚠ 0.187× (z -7.1, 40/44 lines), [[ENSG00000260877]] ⚠ 0.261× (z -7.0, 24/31 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 032]] (+2.6), [[Module 146]] (+2.6), [[Module 070]] (+2.5) | [[Module 174]] (-4.7), [[Module 147]] (-3.6), [[Module 092]] (-3.3) |
| 0.5 µM | — | — |
| 5 µM | [[Module 059]] (+2.6), [[Module 117]] (+2.3), [[Module 064]] (+2.3) | [[Module 174]] (-4.0), [[Module 092]] (-3.0), [[Module 193]] (-2.6) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[CHP-212 (line)]] (-5.1), [[NCI-H1792 (line)]] (-3.4) | [[AsPC-1 (line)]] (1.69), [[MIA PaCa-2 (line)]] (1.64), [[SW480 (line)]] (1.49), [[C32 (line)]] (1.46) · weakest: [[NCI-H661 (line)]] (0.367), [[AN3 CA (line)]] (0.471), [[hTERT-HPNE (line)]] (0.537) |
| 0.5 µM | [[SW 1088 (line)]] (-3.3) | [[SW 1088 (line)]] (1.55), [[NCI-H661 (line)]] (1.26), [[CFPAC-1 (line)]] (1.24), [[Hs 766T (line)]] (1.23) · weakest: [[NCI-H596 (line)]] (0.110), [[NCI-H2122 (line)]] (0.130), [[CHP-212 (line)]] (0.590) |
| 5 µM | [[C32 (line)]] (-5.1), [[SK-MEL-2 (line)]] (-3.3) | [[NCI-H1573 (line)]] (1.37), [[AsPC-1 (line)]] (1.31), [[HOP62 (line)]] (1.27), [[C32 (line)]] (1.19) · weakest: [[NCI-H661 (line)]] (0.535), [[C-33 A (line)]] (0.649), [[AN3 CA (line)]] (0.677) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Trametinib (DMSO_TF solvate) (drug)]] (+0.95, MEK inhibitor); [[Binimetinib (drug)]] (+0.95, MEK inhibitor); [[Cobimetinib (drug)]] (+0.92, MEK inhibitor); [[Trametinib (drug)]] (+0.90, MEK inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Capmatinib (drug)]] (+0.83, EGFR/ERBB inhibitor); [[AZD-7648 (drug)]] (+0.79, DNA synthesis/repair inhibitor); [[Perindopril (erbumine) (drug)]] (+0.77, unclear); [[BI-3406 (drug)]] (+0.74, RAS inhibitor); [[Alpelisib (drug)]] (+0.72, PI3K/AKT inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 22 arrows, 22 of them with an alert ⚠; grade A 0, B 13, C 9. Shown: the 15 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[IL15]] | 0.5 µM | B | IL15 activity lowers the cells' numbers under Elimusertib hydrochloride 0.5 µM (makes them more sensitive) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 1.31× the cells of the other lines | 0.041 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[ATP1B1]] | 0.5 µM | B | ATP1B1 activity lowers the cells' numbers under Elimusertib hydrochloride 0.5 µM (makes them more sensitive) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 1.28× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[LGALS3BP]] | 0.5 µM | B | LGALS3BP activity lowers the cells' numbers under Elimusertib hydrochloride 0.5 µM (makes them more sensitive) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 1.35× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[ALDH3B1]] | 0.5 µM | B | ALDH3B1 activity lowers the cells' numbers under Elimusertib hydrochloride 0.5 µM (makes them more sensitive) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 1.25× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[SPTLC3]] | 0.5 µM | B | SPTLC3 activity lowers the cells' numbers under Elimusertib hydrochloride 0.5 µM (makes them more sensitive) | lines that do not express SPTLC3 (16) vs lines expressing it (32) | the lines without SPTLC3: 1.21× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[LINC02315]] | 5 µM | B | LINC02315 activity raises the cells' numbers under Elimusertib hydrochloride 5 µM (protects the cells) | lines that do not express LINC02315 (31) vs lines expressing it (17) | the lines without LINC02315: 0.83× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: GABRG2, COX7B2, SLC25A24P1 |
| [[TGFBR2]] | 0.5 µM | B | TGFBR2 activity lowers the cells' numbers under Elimusertib hydrochloride 0.5 µM (makes them more sensitive) | lines that do not express TGFBR2 (7) vs lines expressing it (41) | the lines without TGFBR2: 1.35× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[IGSF9]] | 0.5 µM | B | IGSF9 activity lowers the cells' numbers under Elimusertib hydrochloride 0.5 µM (makes them more sensitive) | lines that do not express IGSF9 (16) vs lines expressing it (32) | the lines without IGSF9: 1.25× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[HES7]] | 0.5 µM | B | HES7 activity raises the cells' numbers under Elimusertib hydrochloride 0.5 µM (protects the cells) | lines that do not express HES7 (13) vs lines expressing it (35) | the lines without HES7: 0.81× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, ACTN2, ENSG00000281091; maybe low, not absent |
| [[ATXN1]] | 0.5 µM | B | ATXN1 activity lowers the cells' numbers under Elimusertib hydrochloride 0.5 µM (makes them more sensitive) | lines that do not express ATXN1 (6) vs lines expressing it (42) | the lines without ATXN1: 1.37× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[HOXB9]] | 0.5 µM | B | HOXB9 activity raises the cells' numbers under Elimusertib hydrochloride 0.5 µM (protects the cells) | lines that do not express HOXB9 (17) vs lines expressing it (31) | the lines without HOXB9: 0.83× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: LINC02086, HOXB8; maybe low, not absent |
| [[TSC22D3]] | 0.5 µM | B | TSC22D3 activity lowers the cells' numbers under Elimusertib hydrochloride 0.5 µM (makes them more sensitive) | lines that do not express TSC22D3 (11) vs lines expressing it (37) | the lines without TSC22D3: 1.19× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[ENSG00000232884]] | 0.5 µM | B | ENSG00000232884 activity lowers the cells' numbers under Elimusertib hydrochloride 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000232884 (12) vs lines expressing it (36) | the lines without ENSG00000232884: 1.27× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, NRIP1, ATXN1; maybe low, not absent |
| [[OSR2]] | 5 µM | C | OSR2 activity raises the cells' numbers under Elimusertib hydrochloride 5 µM (protects the cells) | lines that do not express OSR2 (5) vs lines expressing it (43) | the lines without OSR2: 0.64× the cells of the other lines | 0.004 | ⚠ tissue-confounded; across organs; also absent: ZC3HAV1L, TACC2, VRK2; maybe low, not absent |
| [[ATAD1]], [[PTEN]] | 5 µM | C | ATAD1, PTEN activity raises the cells' numbers under Elimusertib hydrochloride 5 µM (protects the cells) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 0.61× the cells of the other lines | 0.021 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Elimusertib hydrochloride"
- `tables/drugdoses.parquet` — dd in 404, 405, 406
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
