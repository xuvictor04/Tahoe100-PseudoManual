---
drug: "Ropivacaine (hydrochloride monohydrate)"
type: "drug"
salt_base: "Ropivacaine"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 67
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Ropivacaine (hydrochloride monohydrate)

*unclear (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 22 / 67 / 37; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.32 / 0.33.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:B12 | 19 / 3 | — | -0.04 | +0.8/-0.3/-0.0 | — |
| 0.5 µM | [[Plate 05]]:B12 | 50 / 17 | — | -0.91 | +1.3/-0.3/+0.3 | — |
| 5 µM | [[Plate 14]]:B12 | 20 / 17 | 0.875 | +0.00 | +1.8/+0.7/+0.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (19 genes, none with an alert; 12 shown): [[ARHGAP22]] 1.35× (z +4.1, 17/27 lines), [[MANCR]] 1.40× (z +3.7, 8/28 lines), [[SH3TC2]] 1.44× (z +3.5, 7/27 lines), [[PDE2A]] 1.46× (z +3.5, 9/42 lines), [[ENSG00000255872]] 1.29× (z +3.5, 17/46 lines), [[LINC02320]] 1.45× (z +3.4, 8/29 lines), [[SYNE3]] 1.26× (z +3.4, 4/37 lines), [[ANO1]] 1.31× (z +3.3, 5/18 lines), [[A3GALT2]] 1.54× (z +3.3, 2/36 lines), [[SOWAHC]] 1.26× (z +3.3, 9/46 lines), [[TMEM255B]] 1.38× (z +3.2, 5/28 lines), [[ENSG00000285906]] 1.22× (z +3.1, 3/39 lines)

**0.5 µM** (50 genes, none with an alert; 12 shown): [[TMEM255B]] 1.59× (z +4.5, 13/27 lines), [[ZNF485]] 1.53× (z +4.5, 5/22 lines), [[ENSG00000270055]] 1.61× (z +4.5, 5/18 lines), [[OTUB2]] 1.43× (z +4.4, 9/36 lines), [[PPIEL-1]] 1.56× (z +4.2, 9/39 lines), [[CCDC13]] 1.56× (z +4.2, 4/23 lines), [[DTX3]] 1.43× (z +4.1, 6/28 lines), [[SLC25A36]] 1.23× (z +4.1, 25/48 lines), [[KBTBD11]] 1.38× (z +3.8, 5/28 lines), [[TP73]] 1.36× (z +3.8, 3/27 lines), [[BMP8A]] 1.48× (z +3.7, 6/28 lines), [[HAGLR]] 1.42× (z +3.7, 1/17 lines)

**5 µM** (20 genes, none with an alert; 12 shown): [[PDE2A]] 1.48× (z +5.1, 23/43 lines), [[ADAMTSL4-AS2]] 1.43× (z +4.5, 20/46 lines), [[SH3TC2]] 1.39× (z +4.5, 16/28 lines), [[ARHGAP22]] 1.25× (z +4.3, 17/27 lines), [[RAC2]] 1.31× (z +4.2, 10/29 lines), [[MANCR]] 1.30× (z +4.1, 13/28 lines), [[RAPGEF3]] 1.31× (z +3.8, 5/40 lines), [[ENSG00000255872]] 1.22× (z +3.8, 20/46 lines), [[AZU1]] 1.46× (z +3.6, 2/40 lines), [[LINC02320]] 1.32× (z +3.5, 10/29 lines), [[ENSG00000249240]] 1.27× (z +3.5, 13/48 lines), [[KIAA0040]] 1.20× (z +3.5, 3/24 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, 1 with an alert ⚠): [[SPRY2]] ⚠ 0.728× (z -4.8, 17/46 lines; position correction uncertain), [[ENSG00000255639]] 0.707× (z -3.6, 5/44 lines), [[DRAM1]] 0.820× (z -3.3, 13/42 lines)

**0.5 µM** (17 genes, 1 with an alert ⚠; 13 shown): [[SPRY2]] ⚠ 0.669× (z -6.2, 25/44 lines; position correction uncertain), [[IBA57]] 0.823× (z -4.0, 15/45 lines), [[DRAM1]] 0.792× (z -3.9, 15/41 lines), [[TBX18]] 0.749× (z -3.8, 8/20 lines), [[LINC02951]] 0.716× (z -3.6, 7/29 lines), [[HAUS3]] 0.825× (z -3.6, 16/45 lines), [[KPNB1]] 0.819× (z -3.5, 30/48 lines), [[SLC39A7]] 0.790× (z -3.5, 20/48 lines), [[ENSG00000226965]] 0.792× (z -3.4, 12/36 lines), [[COL3A1]] 0.716× (z -3.3, 2/13 lines), [[TLCD2]] 0.770× (z -3.3, 11/46 lines), [[EPHA6]] 0.806× (z -3.2, 4/19 lines), [[EBLN2]] 0.757× (z -3.2, 15/39 lines)

**5 µM** (17 genes, 1 with an alert ⚠; 13 shown): [[SPRY2]] ⚠ 0.736× (z -6.6, 27/46 lines; position correction uncertain), [[AJUBA]] 0.793× (z -4.2, 14/46 lines), [[SYT9-AS1]] 0.722× (z -4.2, 10/36 lines), [[FIGN]] 0.827× (z -4.0, 11/32 lines), [[HOXA-AS2]] 0.747× (z -4.0, 8/41 lines), [[KCTD16]] 0.813× (z -3.8, 4/30 lines), [[HOXC4]] 0.746× (z -3.6, 11/34 lines), [[LINC00278]] 0.716× (z -3.6, 7/16 lines), [[ATOH8]] 0.672× (z -3.6, 7/21 lines), [[ABCC6]] 0.793× (z -3.4, 5/36 lines), [[FAM167A]] 0.785× (z -3.4, 3/30 lines), [[F8]] 0.809× (z -3.3, 10/45 lines), [[ENSG00000284956]] 0.823× (z -3.3, 9/37 lines)

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
| 0.05 µM | — | [[HCT15 (line)]] (1.56), [[NCI-H661 (line)]] (1.47), [[hTERT-HPNE (line)]] (1.31), [[C32 (line)]] (1.18) · weakest: [[SW 1088 (line)]] (0.121), [[Hs 766T (line)]] (0.176), [[A-172 (line)]] (0.408) |
| 0.5 µM | — | [[SW 1271 (line)]] (1.83), [[NCI-H661 (line)]] (1.61), [[SW 1088 (line)]] (1.54), [[HCT15 (line)]] (1.50) · weakest: [[LoVo (line)]] (0.163), [[LOX-IMVI (line)]] (0.170), [[A-172 (line)]] (0.329) |
| 5 µM | — | [[SK-MEL-2 (line)]] (1.47), [[NCI-H1573 (line)]] (1.21), [[LOX-IMVI (line)]] (1.19), [[HS-578T (line)]] (1.16) · weakest: [[SNU-1 (line)]] (0.502), [[SW 1088 (line)]] (0.645), [[SW 1271 (line)]] (0.797) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[LY-2584702 (tosylate salt) (drug)]] (+0.56, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[Bestatin (drug)]] (+0.52, unclear, ⚠ only 3 significant genes); [[Pemetrexed (drug)]] (+0.52, DNA synthesis/repair inhibitor); [[Lenalidomide (hemihydrate) (drug)]] (+0.51, unclear); [[Erythromycin (drug)]] (+0.48, unclear); [[Tubulin inhibitor 6 (drug)]] (+0.47, Microtubule inhibitor, ⚠ only 2 significant genes); [[vincristine (drug)]] (+0.47, Microtubule inhibitor); [[Ipatasertib (drug)]] (+0.46, PI3K/AKT inhibitor); [[Canagliflozin (drug)]] (+0.46, Glucose transporter inhibitor); [[Naproxen (drug)]] (+0.46, Cyclooxygenase inhibitor); [[Monocrotaline (drug)]] (+0.45, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 18 arrows, 18 of them with an alert ⚠; grade A 0, B 5, C 13. Shown: the 15 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[CACNB4]] | 5 µM | B | CACNB4 activity raises the cells' numbers under Ropivacaine (hydrochloride monohydrate) 5 µM (protects the cells) | lines that do not express CACNB4 (8) vs lines expressing it (40) | the lines without CACNB4: 0.88× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: HECTD2, RHBDL3, CERCAM; maybe low, not absent |
| [[PDLIM1]] | 0.5 µM | B | PDLIM1 activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express PDLIM1 (11) vs lines expressing it (37) | the lines without PDLIM1: 1.23× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[CACNB4]] | 0.5 µM | B | CACNB4 activity raises the cells' numbers under Ropivacaine (hydrochloride monohydrate) 0.5 µM (protects the cells) | lines that do not express CACNB4 (8) vs lines expressing it (40) | the lines without CACNB4: 0.87× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: HECTD2, RHBDL3, CERCAM; maybe low, not absent |
| [[KCNK6]] | 0.5 µM | B | KCNK6 activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express KCNK6 (12) vs lines expressing it (36) | the lines without KCNK6: 1.23× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[IFIT2]] | 0.5 µM | B | IFIT2 activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express IFIT2 (8) vs lines expressing it (40) | the lines without IFIT2: 1.28× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[RILP]] | 5 µM | C | RILP activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 5 µM (makes them more sensitive) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 1.25× the cells of the other lines | 0.026 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] | 0.5 µM | C | ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.42× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| [[RILP]] | 0.5 µM | C | RILP activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 1.42× the cells of the other lines | 0.028 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| [[LINC02068]] | 5 µM | C | LINC02068 activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 5 µM (makes them more sensitive) | lines that do not express LINC02068 (3) vs lines expressing it (45) | the lines without LINC02068: 1.25× the cells of the other lines | 0.037 | ⚠ few lines (3 vs 47); across organs; also absent: TRIB3; maybe low, not absent |
| [[ENSG00000285458]] | 0.5 µM | C | ENSG00000285458 activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000285458 (5) vs lines expressing it (43) | the lines without ENSG00000285458: 1.30× the cells of the other lines | 0.045 | ⚠ tissue-confounded; across organs; also absent: TBILA, GCA, RILP; maybe low, not absent |
| [[DDR1]] | 0.5 µM | C | DDR1 activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express DDR1 (3) vs lines expressing it (45) | the lines without DDR1: 1.37× the cells of the other lines | 0.049 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD3; also absent: FTH1, LINC00847, IER3; maybe low, not absent |
| [[HBEGF]] | 0.5 µM | C | HBEGF activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express HBEGF (3) vs lines expressing it (45) | the lines without HBEGF: 1.35× the cells of the other lines | 0.056 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, TRAF3IP2; maybe low, not absent |
| [[DPP7]] | 5 µM | C | DPP7 activity raises the cells' numbers under Ropivacaine (hydrochloride monohydrate) 5 µM (protects the cells) | lines that do not express DPP7 (3) vs lines expressing it (45) | the lines without DPP7: 0.82× the cells of the other lines | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: FAM89A, GALNT7, KLF2; maybe low, not absent |
| [[MAP3K5]] | 5 µM | C | MAP3K5 activity raises the cells' numbers under Ropivacaine (hydrochloride monohydrate) 5 µM (protects the cells) | lines that do not express MAP3K5 (3) vs lines expressing it (45) | the lines without MAP3K5: 0.82× the cells of the other lines | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: PFKP, GALNT7, C3orf52 |
| [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] | 5 µM | C | ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.22× the cells of the other lines | 0.070 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Ropivacaine (hydrochloride monohydrate)"
- `tables/drugdoses.parquet` — dd in 908, 909, 910
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
