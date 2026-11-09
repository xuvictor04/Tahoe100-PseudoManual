---
drug: "Dinaciclib"
type: "drug"
salt_base: "Dinaciclib"
targets: "CDK1, CDK2, CDK5, CDK9"
moa_fine: "CDK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 13164
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Dinaciclib

*CDK inhibitor (inhibitor/antagonist) · targets: CDK1, CDK2, CDK5, CDK9 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 11885 / 12822 / 13164; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.92 / 0.96.
> Flags by dose: toxic; transcription drop; cell-cycle shift; composition shift / toxic; transcription drop; cell-cycle shift; composition shift / toxic; transcription drop; cell-cycle shift; composition shift. ⚠ 0.05 µM: toxic; transcription drop; cell-cycle shift; 0.5 µM: toxic; transcription drop; cell-cycle shift; 5 µM: toxic; transcription drop; cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:B3 | 8,497 / 3,388 | — | -2.14 | +11.6/+4.4/+8.1 | ⚠ toxic; transcription drop; cell-cycle shift · composition shift |
| 0.5 µM | [[Plate 08]]:B3 | 8,900 / 3,922 | — | -1.79 | +17.9/+8.8/+11.8 | ⚠ toxic; transcription drop; cell-cycle shift · composition shift |
| 5 µM | [[Plate 09]]:B3 | 9,470 / 3,694 | — | -2.48 | +15.9/+6.9/+7.6 | ⚠ toxic; transcription drop; cell-cycle shift · composition shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (8497 genes, 8,497 with an alert ⚠; the drug-dose carries ⚠ toxic; transcription drop; cell-cycle shift; 12 shown): [[CYB5D2]] ⚠ 13.0× (z +41.9, 32/32 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[ZC3H3]] ⚠ 14.2× (z +33.3, 41/41 lines; toxic; transcription drop; cell-cycle shift (explains ~1% here)), [[SOX2-OT]] ⚠ 9.37× (z +28.2, 33/35 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[BHLHE40-AS1]] ⚠ 6.02× (z +27.1, 26/26 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[NBDY]] ⚠ 3.62× (z +26.9, 38/44 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[BBOX1-AS1]] ⚠ 8.76× (z +26.5, 18/21 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[ENSG00000251131]] ⚠ 59.7× (z +25.4, 2/2 lines; toxic; transcription drop; cell-cycle shift (explains ~1% here)), [[DNAJC27-AS1]] ⚠ 10.9× (z +25.2, 16/17 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[RBBP4]] ⚠ 2.61× (z +25.1, 45/45 lines; toxic; transcription drop; cell-cycle shift (explains ~14% here)), [[PLB1]] ⚠ 10.6× (z +24.6, 8/10 lines; toxic; transcription drop; cell-cycle shift (explains ~10% here)), [[CLASP1-AS1]] ⚠ 54.2× (z +24.1, 9/9 lines; toxic; transcription drop; cell-cycle shift (explains ~6% here)), [[CHMP3]] ⚠ 2.39× (z +23.5, 44/45 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here))

**0.5 µM** (8900 genes, 8,900 with an alert ⚠; the drug-dose carries ⚠ toxic; transcription drop; cell-cycle shift; 12 shown): [[CYB5D2]] ⚠ 22.0× (z +54.6, 37/37 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[ZC3H3]] ⚠ 16.9× (z +39.9, 46/46 lines; toxic; transcription drop; cell-cycle shift (explains ~1% here)), [[NBDY]] ⚠ 4.64× (z +34.8, 48/48 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[BBOX1-AS1]] ⚠ 13.2× (z +34.1, 17/24 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[DNAJC27-AS1]] ⚠ 19.2× (z +33.7, 27/27 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[MRPL42]] ⚠ 3.63× (z +32.6, 45/48 lines; toxic; transcription drop; cell-cycle shift (explains ~15% here)), [[RBBP4]] ⚠ 2.90× (z +32.3, 49/49 lines; toxic; transcription drop; cell-cycle shift (explains ~19% here)), [[ENSG00000251131]] ⚠ 105× (z +31.3, 9/9 lines; toxic; transcription drop; cell-cycle shift (explains ~3% here)), [[CHMP3]] ⚠ 2.87× (z +30.7, 49/49 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[MACROH2A1]] ⚠ 3.10× (z +30.7, 49/49 lines; toxic; transcription drop; cell-cycle shift (explains ~24% here)), [[RYR3]] ⚠ 11.6× (z +30.6, 20/22 lines; toxic; transcription drop; cell-cycle shift (explains ~10% here)), [[CLASP1-AS1]] ⚠ 94.1× (z +29.7, 19/19 lines; toxic; transcription drop; cell-cycle shift (explains ~7% here))

**5 µM** (9470 genes, 9,470 with an alert ⚠; the drug-dose carries ⚠ toxic; transcription drop; cell-cycle shift; 12 shown): [[CYB5D2]] ⚠ 23.9× (z +52.8, 29/29 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[ZC3H3]] ⚠ 17.2× (z +38.6, 37/37 lines; toxic; transcription drop; cell-cycle shift (explains ~1% here)), [[NBDY]] ⚠ 5.08× (z +35.4, 42/42 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[BBOX1-AS1]] ⚠ 13.1× (z +32.7, 13/18 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[DNAJC27-AS1]] ⚠ 18.8× (z +32.2, 13/13 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[RBBP4]] ⚠ 2.89× (z +31.0, 43/44 lines; toxic; transcription drop; cell-cycle shift (explains ~17% here)), [[ENSG00000251131]] ⚠ 122× (z +31.0, 1/1 lines; toxic; transcription drop; cell-cycle shift (explains ~2% here)), [[MUTYH]] ⚠ 7.51× (z +30.5, 12/12 lines; toxic; transcription drop; cell-cycle shift (explains ~4% here)), [[TMEM138]] ⚠ 7.17× (z +30.0, 15/15 lines; toxic; transcription drop; cell-cycle shift (explains ~8% here)), [[SARM1]] ⚠ 8.26× (z +29.7, 29/29 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[MRPL42]] ⚠ 3.30× (z +29.0, 43/43 lines; toxic; transcription drop; cell-cycle shift (explains ~15% here)), [[RYR3]] ⚠ 11.6× (z +28.9, 6/9 lines; toxic; transcription drop; cell-cycle shift (explains ~9% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3388 genes, 3,388 with an alert ⚠; the drug-dose carries ⚠ toxic; transcription drop; cell-cycle shift; 12 shown): [[TTC17]] ⚠ 0.449× (z -26.7, 44/45 lines; toxic; transcription drop; cell-cycle shift (explains ~10% here)), [[LRCH3]] ⚠ 0.382× (z -26.6, 44/45 lines; toxic; transcription drop; cell-cycle shift (explains ~14% here)), [[CEP350]] ⚠ 0.418× (z -26.5, 45/45 lines; toxic; transcription drop; cell-cycle shift (explains ~7% here)), [[FAM193A]] ⚠ 0.363× (z -26.4, 44/45 lines; toxic; transcription drop; cell-cycle shift (explains ~14% here)), [[PIAS1]] ⚠ 0.389× (z -25.9, 41/45 lines; toxic; transcription drop; cell-cycle shift (explains ~3% here)), [[ZNF609]] ⚠ 0.424× (z -25.5, 44/45 lines; toxic; transcription drop; cell-cycle shift (explains ~12% here)), [[PHF20]] ⚠ 0.489× (z -24.3, 40/45 lines; toxic; transcription drop; cell-cycle shift (explains ~3% here)), [[CBFA2T2]] ⚠ 0.326× (z -24.2, 44/45 lines; toxic; transcription drop; cell-cycle shift (explains ~12% here)), [[SYNRG]] ⚠ 0.477× (z -23.6, 41/45 lines; toxic; transcription drop; cell-cycle shift (explains ~6% here)), [[ATXN2]] ⚠ 0.453× (z -23.2, 45/45 lines; toxic; transcription drop; cell-cycle shift (explains ~8% here)), [[AKAP10]] ⚠ 0.353× (z -22.1, 45/45 lines; toxic; transcription drop; cell-cycle shift (explains ~11% here)), [[UBR2]] ⚠ 0.390× (z -21.8, 44/45 lines; toxic; transcription drop; cell-cycle shift (explains ~9% here))

**0.5 µM** (3922 genes, 3,922 with an alert ⚠; the drug-dose carries ⚠ toxic; transcription drop; cell-cycle shift; 12 shown): [[EPC1]] ⚠ 0.296× (z -36.2, 48/49 lines; toxic; transcription drop; cell-cycle shift (explains ~13% here)), [[PIAS1]] ⚠ 0.322× (z -33.6, 49/49 lines; toxic; transcription drop; cell-cycle shift (explains ~4% here)), [[DCP1A]] ⚠ 0.342× (z -32.0, 49/49 lines; toxic; transcription drop; cell-cycle shift (explains ~6% here)), [[ADNP]] ⚠ 0.371× (z -31.6, 48/49 lines; toxic; transcription drop; cell-cycle shift (explains ~13% here)), [[SYNRG]] ⚠ 0.420× (z -29.8, 45/49 lines; toxic; transcription drop; cell-cycle shift (explains ~9% here)), [[AKAP10]] ⚠ 0.279× (z -29.3, 49/49 lines; toxic; transcription drop; cell-cycle shift (explains ~12% here)), [[PDE8A]] ⚠ 0.349× (z -29.0, 49/49 lines; toxic; transcription drop; cell-cycle shift (explains ~17% here)), [[FAM193A]] ⚠ 0.368× (z -28.1, 46/49 lines; toxic; transcription drop; cell-cycle shift (explains ~19% here)), [[RAPGEF6]] ⚠ 0.348× (z -28.0, 49/49 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[LRCH3]] ⚠ 0.395× (z -27.8, 48/49 lines; toxic; transcription drop; cell-cycle shift (explains ~20% here)), [[HEATR5B]] ⚠ 0.332× (z -27.7, 46/49 lines; toxic; transcription drop; cell-cycle shift (explains ~24% here)), [[ATXN2]] ⚠ 0.418× (z -27.6, 49/49 lines; toxic; transcription drop; cell-cycle shift (explains ~10% here))

**5 µM** (3694 genes, 3,694 with an alert ⚠; the drug-dose carries ⚠ toxic; transcription drop; cell-cycle shift; 12 shown): [[DCP1A]] ⚠ 0.273× (z -37.2, 43/44 lines; toxic; transcription drop; cell-cycle shift (explains ~5% here)), [[PIAS1]] ⚠ 0.300× (z -34.4, 44/44 lines; toxic; transcription drop; cell-cycle shift (explains ~3% here)), [[ADNP]] ⚠ 0.346× (z -32.4, 44/44 lines; toxic; transcription drop; cell-cycle shift (explains ~12% here)), [[AKAP10]] ⚠ 0.259× (z -29.8, 44/44 lines; toxic; transcription drop; cell-cycle shift (explains ~11% here)), [[LRCH3]] ⚠ 0.355× (z -29.8, 40/44 lines; toxic; transcription drop; cell-cycle shift (explains ~17% here)), [[RAPGEF6]] ⚠ 0.316× (z -29.4, 43/44 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[PDE8A]] ⚠ 0.330× (z -29.4, 43/44 lines; toxic; transcription drop; cell-cycle shift (explains ~15% here)), [[PPP1R12A]] ⚠ 0.525× (z -28.2, 40/44 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[ZNF292]] ⚠ 0.258× (z -27.5, 44/44 lines; toxic; transcription drop; cell-cycle shift (explains ~16% here)), [[USP42]] ⚠ 0.312× (z -27.5, 38/43 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[CEP350]] ⚠ 0.423× (z -27.3, 44/44 lines; toxic; transcription drop; cell-cycle shift (explains ~7% here)), [[ZNF148]] ⚠ 0.415× (z -27.0, 44/44 lines; toxic; transcription drop; cell-cycle shift (explains ~16% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 025]] (+12.5), [[Module 168]] (+11.1), [[Module 010]] (+11.0) | [[Module 170]] (-12.9), [[Module 054]] (-11.9), [[Module 231]] (-11.8) |
| 0.5 µM | [[Module 025]] (+16.5), [[Module 148]] (+15.2), [[Module 002]] (+14.3) | [[Module 077]] (-16.3), [[Module 170]] (-16.2), [[Module 234]] (-15.0) |
| 5 µM | [[Module 002]] (+16.1), [[Module 025]] (+16.0), [[Module 148]] (+13.3) | [[Module 077]] (-15.0), [[Module 234]] (-14.3), [[Module 170]] (-14.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[RKO (line)]] (-9.8), [[NCI-H23 (line)]] (-8.7), [[SW480 (line)]] (-8.2), [[COLO 205 (line)]] (-7.2), [[A-427 (line)]] (-6.5) | [[RKO (line)]] (1.46), [[SNU-1 (line)]] (1.40), [[C-33 A (line)]] (1.33), [[A-427 (line)]] (1.23) · weakest: [[NCI-H661 (line)]] (0.620), [[BT-474 (line)]] (0.650), [[AsPC-1 (line)]] (0.650) |
| 0.5 µM | [[RKO (line)]] (-14.2), [[NCI-H23 (line)]] (-11.8), [[SK-MEL-2 (line)]] (-10.6), [[SNU-1 (line)]] (-10.1), [[SW480 (line)]] (-9.9) | [[RKO (line)]] (1.43), [[SNU-1 (line)]] (1.40), [[COLO 205 (line)]] (1.31), [[HCT15 (line)]] (1.20) · weakest: [[NCI-H2122 (line)]] (0.434), [[NCI-H661 (line)]] (0.564), [[BT-474 (line)]] (0.591) |
| 5 µM | [[SW480 (line)]] (-10.1), [[RKO (line)]] (-9.5), [[Hs 766T (line)]] (-9.0), [[NCI-H1573 (line)]] (-8.4), [[SK-MEL-2 (line)]] (-7.8) | [[SNU-1 (line)]] (1.44), [[C-33 A (line)]] (1.29), [[NCI-H23 (line)]] (1.23), [[NCI-H1573 (line)]] (1.21) · weakest: [[BT-474 (line)]] (0.632), [[NCI-H2347 (line)]] (0.652), [[NCI-H661 (line)]] (0.686) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: toxic; transcription drop; cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Lonafarnib (drug)]] (+0.71, RAS inhibitor, ⚠ vector dose flagged: toxic); [[Imiquimod (maleate) (drug)]] (+0.55, unclear); [[Orlistat (drug)]] (+0.54, unclear); [[Nafamostat (mesylate) (drug)]] (+0.53, unclear, ⚠ only 3 significant genes); [[AZD2858 (drug)]] (+0.52, GSK3 inhibitor, ⚠ vector dose flagged: toxic); [[Pimozide (drug)]] (+0.51, unclear); [[Ferulic acid (drug)]] (+0.48, Other TK inhibitor); [[Niclosamide (olamine) (drug)]] (+0.47, unclear, ⚠ vector dose flagged: toxic; cell-cycle shift); [[Valdecoxib (drug)]] (+0.46, Cyclooxygenase inhibitor); [[Filgotinib (drug)]] (+0.45, JAK/STAT inhibitor); [[Meloxicam (drug)]] (+0.45, Cyclooxygenase inhibitor); [[Pyridoxine (drug)]] (+0.44, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 28 arrows, 28 of them with an alert ⚠; grade A 0, B 18, C 10. Shown: the 15 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[PCED1B]] | 0.5 µM | B | PCED1B activity raises the cells' numbers under Dinaciclib 0.5 µM (protects the cells) | lines that do not express PCED1B (11) vs lines expressing it (37) | the lines without PCED1B: 0.33× the cells of the other lines | 0.048 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[KCND3]] | 5 µM | B | KCND3 activity lowers the cells' numbers under Dinaciclib 5 µM (makes them more sensitive) | lines that do not express KCND3 (21) vs lines expressing it (27) | the lines without KCND3: 2.05× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |
| [[NFATC2]] | 0.5 µM | B | NFATC2 activity raises the cells' numbers under Dinaciclib 0.5 µM (protects the cells) | lines that do not express NFATC2 (11) vs lines expressing it (37) | the lines without NFATC2: 0.31× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[CTHRC1]] | 5 µM | B | CTHRC1 activity raises the cells' numbers under Dinaciclib 5 µM (protects the cells) | lines that do not express CTHRC1 (26) vs lines expressing it (22) | the lines without CTHRC1: 0.38× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent |
| [[SYNE3]] | 5 µM | B | SYNE3 activity raises the cells' numbers under Dinaciclib 5 µM (protects the cells) | lines that do not express SYNE3 (11) vs lines expressing it (37) | the lines without SYNE3: 0.44× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[KCND3]] | 0.5 µM | B | KCND3 activity lowers the cells' numbers under Dinaciclib 0.5 µM (makes them more sensitive) | lines that do not express KCND3 (21) vs lines expressing it (27) | the lines without KCND3: 2.00× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |
| [[SYNE3]] | 0.5 µM | B | SYNE3 activity raises the cells' numbers under Dinaciclib 0.5 µM (protects the cells) | lines that do not express SYNE3 (11) vs lines expressing it (37) | the lines without SYNE3: 0.42× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DNM3]] | 0.05 µM | B | DNM3 activity raises the cells' numbers under Dinaciclib 0.05 µM (protects the cells) | lines that do not express DNM3 (7) vs lines expressing it (41) | the lines without DNM3: 0.38× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: DENND3, TSC22D3; maybe low, not absent |
| [[NFATC2]] | 0.05 µM | B | NFATC2 activity raises the cells' numbers under Dinaciclib 0.05 µM (protects the cells) | lines that do not express NFATC2 (11) vs lines expressing it (37) | the lines without NFATC2: 0.40× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[SYNE3]] | 0.05 µM | B | SYNE3 activity raises the cells' numbers under Dinaciclib 0.05 µM (protects the cells) | lines that do not express SYNE3 (11) vs lines expressing it (37) | the lines without SYNE3: 0.52× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PCED1B]] | 0.05 µM | B | PCED1B activity raises the cells' numbers under Dinaciclib 0.05 µM (protects the cells) | lines that do not express PCED1B (11) vs lines expressing it (37) | the lines without PCED1B: 0.47× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[RASD1]] | 5 µM | B | RASD1 activity raises the cells' numbers under Dinaciclib 5 µM (protects the cells) | lines that do not express RASD1 (21) vs lines expressing it (27) | the lines without RASD1: 0.50× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: MTSS1, TREM1, APOE |
| [[HOMER2]] | 0.05 µM | B | HOMER2 activity lowers the cells' numbers under Dinaciclib 0.05 µM (makes them more sensitive) | lines that do not express HOMER2 (11) vs lines expressing it (37) | the lines without HOMER2: 1.29× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: ZNF529-AS1, ZNF420, ENSG00000282381; maybe low, not absent |
| [[TESC]] | 5 µM | B | TESC activity lowers the cells' numbers under Dinaciclib 5 µM (makes them more sensitive) | lines that do not express TESC (23) vs lines expressing it (25) | the lines without TESC: 3.13× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: HSH2D, LINC02331, PIK3AP1 |
| [[TRPM2-AS]] | 5 µM | B | TRPM2-AS activity lowers the cells' numbers under Dinaciclib 5 µM (makes them more sensitive) | lines that do not express TRPM2-AS (29) vs lines expressing it (19) | the lines without TRPM2-AS: 2.42× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Dinaciclib"
- `tables/drugdoses.parquet` — dd in 362, 363, 364
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
