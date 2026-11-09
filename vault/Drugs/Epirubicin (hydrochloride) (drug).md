---
drug: "Epirubicin (hydrochloride)"
type: "drug"
salt_base: "Epirubicin"
targets: "TOP2A"
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 6752
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Epirubicin (hydrochloride)

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · targets: TOP2A · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 45 / 196 / 6752; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.03 / 0.18.
> Flags by dose: low cells (technical?) / - / cell-cycle shift. ⚠ 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:C12 | 44 / 1 | — | -1.30 | -0.7/+0.9/-0.6 | low cells (technical?) |
| 0.5 µM | [[Plate 08]]:C12 | 107 / 89 | — | -0.36 | +2.2/-1.4/-0.9 | — |
| 5 µM | [[Plate 09]]:C12 | 4,449 / 2,303 | — | +0.24 | +8.7/+1.1/+1.9 | ⚠ cell-cycle shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (44 genes, none with an alert; 12 shown): [[TMPRSS3]] 1.76× (z +4.7, 2/13 lines), [[CTU1]] 1.51× (z +4.3, 3/33 lines), [[HERC2P10]] 1.51× (z +4.2, 2/14 lines), [[CNTNAP3P2]] 1.45× (z +3.9, 2/22 lines), [[KPTN]] 1.48× (z +3.9, 5/31 lines), [[GAS6-AS1]] 1.45× (z +3.8, 7/23 lines), [[ACBD7]] 1.46× (z +3.7, 5/30 lines), [[ARHGEF6]] 1.35× (z +3.7, 2/20 lines), [[GRK2]] 1.28× (z +3.6, 13/44 lines), [[RELL2]] 1.51× (z +3.6, 1/22 lines), [[GDNF-AS1]] 1.55× (z +3.6, 0/8 lines), [[SYT9]] 1.49× (z +3.5, 1/9 lines)

**0.5 µM** (107 genes, 1 with an alert ⚠; 13 shown): [[TMEM132B]] ⚠ 1.98× (z +7.7, 25/40 lines; position correction uncertain), [[TAF3]] 1.26× (z +6.4, 30/48 lines), [[LIG1]] 1.35× (z +5.3, 22/48 lines), [[CASD1]] 1.41× (z +5.2, 31/47 lines), [[FBF1]] 1.43× (z +5.1, 15/46 lines), [[DIAPH3]] 1.26× (z +4.9, 22/45 lines), [[DNA2]] 1.30× (z +4.8, 18/48 lines), [[PRIM2]] 1.36× (z +4.7, 32/48 lines), [[SESN1]] 1.29× (z +4.6, 23/48 lines), [[POLQ]] 1.35× (z +4.5, 23/46 lines), [[ACER2]] 1.37× (z +4.4, 20/46 lines), [[SPAG1]] 1.22× (z +4.4, 10/48 lines), [[DPF3]] 1.40× (z +4.4, 7/34 lines)

**5 µM** (4449 genes, 1,280 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[EPHA4]] 7.69× (z +28.6, 27/31 lines; cell-cycle shift (explains ~10% here)), [[ENSG00000287292]] 15.3× (z +25.9, 30/30 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000289156]] 8.71× (z +23.6, 33/37 lines; cell-cycle shift (explains ~0% here)), [[DPF3]] 6.55× (z +23.5, 24/28 lines; cell-cycle shift (explains ~14% here)), [[ENSG00000286533]] 7.42× (z +23.0, 43/45 lines; cell-cycle shift (explains ~0% here)), [[GSTCD]] 3.16× (z +22.8, 44/48 lines; cell-cycle shift (explains ~23% here)), [[SIAH2-AS1]] 14.5× (z +22.8, 32/33 lines; cell-cycle shift (explains ~0% here)), [[MAP7D2]] 6.56× (z +21.8, 40/43 lines; cell-cycle shift (explains ~6% here)), [[DRC1]] 15.3× (z +21.7, 30/31 lines; cell-cycle shift (explains ~7% here)), [[ANKRD7]] 6.09× (z +21.4, 29/32 lines; cell-cycle shift (explains ~6% here)), [[ADAMTS17]] 4.48× (z +21.1, 28/29 lines; cell-cycle shift (explains ~9% here)), [[C2]] 7.36× (z +21.0, 44/45 lines; cell-cycle shift (explains ~6% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[SDHAF4]] 0.807× (z -3.2, 7/44 lines)

**0.5 µM** (89 genes, none with an alert; 12 shown): [[ENSG00000235609]] 0.742× (z -5.5, 23/40 lines), [[CCNF]] 0.717× (z -5.4, 22/48 lines), [[BCL11A]] 0.690× (z -5.4, 18/28 lines), [[ENSG00000257545]] 0.678× (z -4.8, 8/45 lines), [[NRF1]] 0.778× (z -4.8, 27/48 lines), [[C1QTNF7-AS1]] 0.784× (z -4.7, 19/45 lines), [[PRXL2C]] 0.730× (z -4.6, 16/46 lines), [[PIF1]] 0.690× (z -4.6, 17/46 lines), [[NBN]] 0.812× (z -4.6, 24/48 lines), [[RARG]] 0.747× (z -4.6, 15/44 lines), [[L1CAM]] 0.712× (z -4.5, 14/26 lines), [[STAC]] 0.789× (z -4.4, 11/23 lines)

**5 µM** (2303 genes, 1,032 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 14 shown): [[TOX2]] 0.324× (z -18.8, 27/30 lines; cell-cycle shift (explains ~0% here)), [[ZNF652]] 0.485× (z -18.1, 43/50 lines; cell-cycle shift (explains ~19% here)), [[DCTN4]] 0.503× (z -17.9, 46/50 lines; cell-cycle shift (explains ~10% here)), [[POGZ]] 0.512× (z -17.6, 45/50 lines; cell-cycle shift (explains ~17% here)), [[DHRSX]] ⚠ 0.478× (z -17.3, 42/49 lines; cell-cycle shift, explains ~32% of this change), [[GTF2IRD1]] 0.469× (z -16.9, 43/50 lines; cell-cycle shift (explains ~18% here)), [[KMT5B]] ⚠ 0.572× (z -16.8, 45/50 lines; cell-cycle shift, explains ~31% of this change), [[DANT2]] 0.440× (z -16.7, 36/39 lines; cell-cycle shift (explains ~15% here)), [[TBC1D25]] 0.387× (z -16.7, 40/48 lines; cell-cycle shift (explains ~18% here)), [[SMIM7]] 0.503× (z -16.5, 39/48 lines; cell-cycle shift (explains ~8% here)), [[CCDC12]] 0.494× (z -16.4, 42/49 lines; cell-cycle shift (explains ~3% here)), [[CRTC1]] 0.464× (z -16.1, 43/48 lines; cell-cycle shift (explains ~9% here)), [[CSTPP1]] 0.527× (z -16.0, 40/50 lines; cell-cycle shift (explains ~0% here)), [[TUT4]] 0.603× (z -16.0, 44/49 lines; cell-cycle shift (explains ~16% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 026]] (+11.1), [[Module 148]] (+9.3), [[Module 137]] (+8.8) | [[Module 085]] (-9.9), [[Module 230]] (-8.0), [[Module 146]] (-7.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW48 (line)]] (1.44), [[SW 1271 (line)]] (1.39), [[NCI-H661 (line)]] (1.34), [[RPMI-7951 (line)]] (1.31) · weakest: [[NCI-H2347 (line)]] (0.227), [[HOP62 (line)]] (0.233), [[SW480 (line)]] (0.235) |
| 0.5 µM | [[H4 (line)]] (-4.0) | [[RKO (line)]] (1.60), [[SNU-423 (line)]] (1.51), [[MIA PaCa-2 (line)]] (1.49), [[A-427 (line)]] (1.44) · weakest: [[SHP-77 (line)]] (0.366), [[NCI-H1573 (line)]] (0.455), [[AsPC-1 (line)]] (0.491) |
| 5 µM | [[SK-MEL-2 (line)]] (-13.6), [[NCI-H23 (line)]] (-12.7), [[RKO (line)]] (-11.6), [[SNU-1 (line)]] (-10.8), [[A-427 (line)]] (-10.2) | [[RKO (line)]] (1.63), [[HOP62 (line)]] (1.50), [[MIA PaCa-2 (line)]] (1.46), [[C32 (line)]] (1.46) · weakest: [[NCI-H596 (line)]] (-0.0622), [[NCI-H1573 (line)]] (0.235), [[SHP-77 (line)]] (0.261) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 5 next most similar without an alert.*

- [[Doxorubicin (hydrochloride) (drug)]] (+0.96, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] (+0.81, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] (+0.70, DNA synthesis/repair inhibitor); [[Pimozide (drug)]] (+0.40, unclear); [[Valdecoxib (drug)]] (+0.36, Cyclooxygenase inhibitor); [[Nafamostat (mesylate) (drug)]] (+0.35, unclear, ⚠ only 3 significant genes); [[γ-Oryzanol (drug)]] (+0.35, DNA methyltransferase inhibitor, ⚠ only 1 significant gene); [[Vemurafenib (drug)]] (+0.35, RAF inhibitor, ⚠ only 1 significant gene); [[Orlistat (drug)]] (+0.33, unclear); [[Demeclocycline (drug)]] (+0.29, unclear); [[Meloxicam (drug)]] (+0.27, Cyclooxygenase inhibitor); [[Drospirenone (drug)]] (+0.26, unclear); [[Aliskiren (drug)]] (+0.26, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 24 arrows, 24 of them with an alert ⚠; grade A 0, B 12, C 12. Shown: the 15 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[EPHA1-AS1]] | 5 µM | B | EPHA1-AS1 activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express EPHA1-AS1 (6) vs lines expressing it (42) | the lines without EPHA1-AS1: 0.48× the cells of the other lines | 0.048 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| [[PLOD2]] | 5 µM | B | PLOD2 activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express PLOD2 (15) vs lines expressing it (33) | the lines without PLOD2: 0.54× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[TRPA1]] | 5 µM | B | TRPA1 activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express TRPA1 (31) vs lines expressing it (17) | the lines without TRPA1: 0.59× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B |
| [[AMIGO2]] | 5 µM | B | AMIGO2 activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express AMIGO2 (12) vs lines expressing it (36) | the lines without AMIGO2: 0.46× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[PCED1B]] | 5 µM | B | PCED1B activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express PCED1B (11) vs lines expressing it (37) | the lines without PCED1B: 0.41× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[DOCK10]] | 5 µM | B | DOCK10 activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express DOCK10 (24) vs lines expressing it (24) | the lines without DOCK10: 0.67× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, TRPA1 |
| [[DNM3]] | 5 µM | B | DNM3 activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express DNM3 (7) vs lines expressing it (41) | the lines without DNM3: 0.52× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: DENND3, TSC22D3; maybe low, not absent |
| [[ENSG00000225647]] | 5 µM | B | ENSG00000225647 activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express ENSG00000225647 (10) vs lines expressing it (38) | the lines without ENSG00000225647: 0.56× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: BTBD6, CPA6; maybe low, not absent |
| [[ARID5B]] | 5 µM | B | ARID5B activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express ARID5B (6) vs lines expressing it (42) | the lines without ARID5B: 0.51× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: TNFAIP3, ATXN1, SSUH2 |
| [[TRIM29]] | 0.5 µM | B | TRIM29 activity raises the cells' numbers under Epirubicin (hydrochloride) 0.5 µM (protects the cells) | lines that do not express TRIM29 (28) vs lines expressing it (20) | the lines without TRIM29: 0.87× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[JUP]] | 0.5 µM | B | JUP activity raises the cells' numbers under Epirubicin (hydrochloride) 0.5 µM (protects the cells) | lines that do not express JUP (16) vs lines expressing it (32) | the lines without JUP: 0.87× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[LINC02057]] | 5 µM | B | LINC02057 activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express LINC02057 (25) vs lines expressing it (23) | the lines without LINC02057: 0.53× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[FTH1]] | 5 µM | C | FTH1 activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express FTH1 (4) vs lines expressing it (44) | the lines without FTH1: 0.28× the cells of the other lines | 0.007 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000284716, ZFP36, DDR1; maybe low, not absent |
| [[ENSG00000291174]] | 5 µM | C | ENSG00000291174 activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express ENSG00000291174 (3) vs lines expressing it (45) | the lines without ENSG00000291174: 0.27× the cells of the other lines | 0.015 | ⚠ few lines (3 vs 47); across organs; also absent: ZFP36, IQCN, NEK3 |
| [[SCAMP5]] | 0.5 µM | C | SCAMP5 activity raises the cells' numbers under Epirubicin (hydrochloride) 0.5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.75× the cells of the other lines | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 4,166 arrows, 4,166 of them with an alert ⚠; grade A 0, B 4,166, C 0. Shown: the 15 strongest; 4,151 more arrows (4,151 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[TOP2A]] | [[G2E3]] | moves it that way too | B | TOP2A activity raises G2E3's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.5% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[RABL2B]] | moves it that way too | B | TOP2A activity lowers RABL2B's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.8% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[RASSF8-AS1]] | moves it that way too | B | TOP2A activity lowers RASSF8-AS1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.8% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ENSG00000285667]] | moves it that way too | B | TOP2A activity lowers ENSG00000285667's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.1% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[LRRIQ3]] | moves it that way too | B | TOP2A activity lowers LRRIQ3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.1% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[BAX]] | moves it that way too | B | TOP2A activity lowers BAX's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[CIBAR1-DT]] | moves it that way too | B | TOP2A activity lowers CIBAR1-DT's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ENSG00000287400]] | moves it that way too | B | TOP2A activity lowers ENSG00000287400's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[MIDEAS]] | moves it that way too | B | TOP2A activity raises MIDEAS's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[TARID]] | moves it that way too | B | TOP2A activity lowers TARID's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ZNF665]] | moves it that way too | B | TOP2A activity lowers ZNF665's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[AK1]] | moves it that way too | B | TOP2A activity lowers AK1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[CAMKK1]] | moves it that way too | B | TOP2A activity raises CAMKK1's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ENSG00000228566]] | moves it that way too | B | TOP2A activity lowers ENSG00000228566's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[FCGBP]] | moves it that way too | B | TOP2A activity lowers FCGBP's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Epirubicin (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 415, 416, 417
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
