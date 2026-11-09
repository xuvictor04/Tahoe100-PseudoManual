---
drug: "Loperamide (hydrochloride)"
type: "drug"
salt_base: "Loperamide"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 24
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Loperamide (hydrochloride)

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 8 / 24 / 22; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.03 / 0.38.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:B4 | 7 / 1 | — | -0.29 | -0.7/+0.3/-0.4 | — |
| 0.5 µM | [[Plate 11]]:B4 | 0 / 24 | — | +0.63 | -1.2/-0.8/-0.7 | — |
| 5 µM | [[Plate 12]]:B4 | 2 / 20 | — | -0.14 | -1.1/-0.3/-0.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (7 genes, none with an alert): [[ENSG00000289293]] 1.51× (z +3.9, 11/44 lines), [[SIPA1]] 1.32× (z +3.6, 4/45 lines), [[ENSG00000248837]] 1.45× (z +3.5, 0/11 lines), [[RBPMS2]] 1.35× (z +3.4, 0/28 lines), [[PYGO2]] 1.29× (z +3.2, 10/46 lines), [[AIF1L]] 1.24× (z +3.1, 0/33 lines), [[BARX2]] 1.22× (z +3.0, 0/19 lines)

**5 µM** (2 genes, none with an alert): [[ACVR1C]] 1.27× (z +3.1, 5/43 lines), [[RSAD2]] 1.46× (z +2.9, 8/34 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[HENMT1]] 0.760× (z -2.9, 6/29 lines)

**0.5 µM** (24 genes, none with an alert; 12 shown): [[KMT2B]] 0.753× (z -4.6, 24/48 lines), [[NSMF]] 0.713× (z -4.0, 23/46 lines), [[MT-RNR1]] 0.513× (z -3.9, 48/49 lines), [[SRRM2]] 0.831× (z -3.9, 26/49 lines), [[TCIRG1]] 0.738× (z -3.7, 12/41 lines), [[FOSB]] 0.428× (z -3.7, 38/48 lines), [[TGFB3]] 0.699× (z -3.7, 6/43 lines), [[LRRC45]] 0.634× (z -3.7, 13/43 lines), [[SLC17A9]] 0.694× (z -3.6, 5/21 lines), [[ABCF3]] 0.778× (z -3.6, 12/48 lines), [[ENSG00000288755]] 0.626× (z -3.4, 8/43 lines), [[BAP1]] 0.803× (z -3.4, 13/48 lines)

**5 µM** (20 genes, none with an alert; 12 shown): [[MT-RNR1]] 0.398× (z -5.4, 48/48 lines), [[DHFR]] 0.567× (z -4.7, 44/48 lines), [[KMT2B]] 0.754× (z -4.6, 27/48 lines), [[TNKS1BP1]] 0.720× (z -4.2, 29/48 lines), [[U2AF2]] 0.773× (z -4.0, 30/48 lines), [[ARFRP1]] 0.751× (z -3.7, 16/47 lines), [[NSMF]] 0.744× (z -3.5, 14/45 lines), [[MTND2P28]] 0.614× (z -3.4, 14/46 lines), [[MBD6]] 0.788× (z -3.3, 10/47 lines), [[BCL9L]] 0.820× (z -3.2, 18/45 lines), [[PLXNB3]] 0.599× (z -3.2, 11/36 lines), [[CRAT]] 0.781× (z -3.2, 5/45 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[COLO 205 (line)]] (1.51), [[NCI-H1792 (line)]] (1.47), [[C32 (line)]] (1.45), [[RPMI-7951 (line)]] (1.44) · weakest: [[NCI-H2122 (line)]] (-0.500), [[KATO III (line)]] (0.639), [[SW1417 (line)]] (0.650) |
| 5 µM | — | [[NCI-H661 (line)]] (1.45), [[RKO (line)]] (1.25), [[SNU-423 (line)]] (1.20), [[A-427 (line)]] (1.19) · weakest: [[SW 1088 (line)]] (0.541), [[NCI-H2030 (line)]] (0.734), [[COLO 205 (line)]] (0.737) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 5 next most similar without an alert.*

- [[Bisoprolol (hemifumarate) (drug)]] (+0.71, Adrenoceptor agonist); [[Ivabradine (hydrochloride) (drug)]] (+0.65, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Adenosine (drug)]] (+0.64, unclear, ⚠ only 9 significant genes); [[Fenofibrate (drug)]] (+0.61, unclear); [[Erlotinib (drug)]] (+0.56, EGFR/ERBB inhibitor); [[Ribociclib (drug)]] (+0.52, CDK inhibitor, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only; position not correctable)); [[Vismodegib (drug)]] (+0.52, Sonic inhibitor, ⚠ only 5 significant genes); [[Carbidopa (monohydrate) (drug)]] (+0.51, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only; position not correctable)); [[Doxycycline (monohydrate) (drug)]] (+0.50, unclear); [[Futibatinib (drug)]] (+0.50, Other TK inhibitor); [[Dabrafenib (drug)]] (+0.47, RAF inhibitor); [[Menadione (drug)]] (+0.45, unclear); [[Lidocaine (hydrochloride) (drug)]] (+0.44, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 19 arrows, 19 of them with an alert ⚠; grade A 0, B 17, C 2. Shown: the 15 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[KLRC4-KLRK1]], [[KLRK1]] | 0.5 µM | B | KLRC4-KLRK1, KLRK1 activity raises the cells' numbers under Loperamide (hydrochloride) 0.5 µM (protects the cells) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 0.86× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| [[PTGS2]] | 0.5 µM | B | PTGS2 activity lowers the cells' numbers under Loperamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express PTGS2 (27) vs lines expressing it (21) | the lines without PTGS2: 1.16× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[C12orf75-AS1]] | 0.5 µM | B | C12orf75-AS1 activity lowers the cells' numbers under Loperamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express C12orf75-AS1 (22) vs lines expressing it (26) | the lines without C12orf75-AS1: 1.18× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[FOXC2]] | 0.5 µM | B | FOXC2 activity lowers the cells' numbers under Loperamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express FOXC2 (33) vs lines expressing it (15) | the lines without FOXC2: 1.18× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT |
| [[PRSS23]] | 0.5 µM | B | PRSS23 activity lowers the cells' numbers under Loperamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express PRSS23 (13) vs lines expressing it (35) | the lines without PRSS23: 1.23× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[ENSG00000225751]] | 0.5 µM | B | ENSG00000225751 activity lowers the cells' numbers under Loperamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000225751 (14) vs lines expressing it (34) | the lines without ENSG00000225751: 1.16× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SLFN5, MMRN2, MGLL |
| [[ENSG00000289309]] | 0.5 µM | B | ENSG00000289309 activity raises the cells' numbers under Loperamide (hydrochloride) 0.5 µM (protects the cells) | lines that do not express ENSG00000289309 (39) vs lines expressing it (9) | the lines without ENSG00000289309: 0.87× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[DNAH11]] | 0.5 µM | B | DNAH11 activity lowers the cells' numbers under Loperamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express DNAH11 (23) vs lines expressing it (25) | the lines without DNAH11: 1.15× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| [[KLRC3]] | 0.5 µM | B | KLRC3 activity raises the cells' numbers under Loperamide (hydrochloride) 0.5 µM (protects the cells) | lines that do not express KLRC3 (27) vs lines expressing it (21) | the lines without KLRC3: 0.87× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| [[PLA2G4A]] | 0.5 µM | B | PLA2G4A activity lowers the cells' numbers under Loperamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express PLA2G4A (22) vs lines expressing it (26) | the lines without PLA2G4A: 1.11× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3 |
| [[NLGN4X]] | 0.5 µM | B | NLGN4X activity raises the cells' numbers under Loperamide (hydrochloride) 0.5 µM (protects the cells) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 0.92× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| [[CXCL3]] | 0.5 µM | B | CXCL3 activity lowers the cells' numbers under Loperamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express CXCL3 (14) vs lines expressing it (34) | the lines without CXCL3: 1.18× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[LY6K]] | 0.5 µM | B | LY6K activity lowers the cells' numbers under Loperamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express LY6K (32) vs lines expressing it (16) | the lines without LY6K: 1.17× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, TNIP3 |
| [[CD44]] | 0.5 µM | B | CD44 activity lowers the cells' numbers under Loperamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express CD44 (15) vs lines expressing it (33) | the lines without CD44: 1.18× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[ZNF469]] | 0.5 µM | B | ZNF469 activity lowers the cells' numbers under Loperamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express ZNF469 (20) vs lines expressing it (28) | the lines without ZNF469: 1.20× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: LINC02057, IL6, TMEM158 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Loperamide (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 630, 631, 632
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
