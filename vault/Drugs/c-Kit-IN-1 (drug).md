---
drug: "c-Kit-IN-1"
type: "drug"
salt_base: "c-Kit-IN-1"
targets: "KIT, MET, KDR, PDGFRA, PDGFRB"
moa_fine: "Multi-TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 5673
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# c-Kit-IN-1

*Multi-TK inhibitor (inhibitor/antagonist) · targets: KIT, MET, KDR, PDGFRA, PDGFRB · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 5673 / 81 / 1878; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.48 / 0.29.
> Flags by dose: unreliable plate only / noisy plate (z scaled) / noisy plate (z scaled). ⚠ 0.05 µM: unreliable plate only (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 13]]:A2 | 2,514 / 3,159 | — | +0.03 | +2.7/-3.6/+2.3 | ⚠ unreliable plate only |
| 0.5 µM | [[Plate 02]]:B3 | 32 / 49 | — | +0.18 | -0.1/-0.9/-1.1 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:B3 | 885 / 993 | — | -0.24 | +1.9/-0.9/+1.5 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2514 genes, 2,514 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[CREB5]] ⚠ 2.74× (z +17.6, 30/33 lines), [[POLR3G]] ⚠ 2.78× (z +17.1, 43/45 lines), [[PUM3]] ⚠ 2.11× (z +17.1, 47/47 lines), [[URB1]] ⚠ 2.73× (z +16.8, 48/48 lines), [[ANK2]] ⚠ 3.27× (z +15.9, 29/32 lines), [[DHX37]] ⚠ 2.40× (z +15.8, 45/47 lines), [[UTP20]] ⚠ 2.53× (z +15.7, 47/48 lines), [[FRMD5]] ⚠ 2.31× (z +15.5, 33/38 lines), [[C19orf48]] ⚠ 2.35× (z +15.5, 43/47 lines), [[ZNRF3]] ⚠ 2.18× (z +15.3, 37/46 lines), [[XPO5]] ⚠ 2.04× (z +15.3, 43/47 lines), [[DHX33]] ⚠ 2.01× (z +15.2, 45/47 lines)

**0.5 µM** (32 genes, 1 with an alert ⚠; 12 shown): [[SNX5]] 1.25× (z +3.9, 12/48 lines), [[POLR1B]] 1.34× (z +3.7, 6/48 lines), [[LRPPRC]] 1.35× (z +3.6, 31/48 lines), [[NSUN2]] 1.38× (z +3.5, 22/48 lines), [[MDN1]] 1.24× (z +3.3, 13/48 lines), [[NAA15]] 1.29× (z +3.3, 15/48 lines), [[EZH2]] 1.37× (z +3.3, 14/48 lines), [[UBE2G2]] 1.24× (z +3.2, 8/48 lines), [[EFTUD2]] 1.23× (z +3.2, 8/48 lines), [[C19orf48]] 1.27× (z +3.1, 2/48 lines), [[ZNF34]] 1.44× (z +3.1, 0/47 lines), [[USP38]] 1.41× (z +3.1, 9/48 lines)

**5 µM** (885 genes, 4 with an alert ⚠; 12 shown): [[DHX33]] 2.09× (z +8.4, 31/46 lines), [[DHX37]] 2.42× (z +8.4, 37/45 lines), [[RCAN1]] 2.28× (z +7.9, 28/46 lines), [[PUM3]] 1.93× (z +7.7, 41/47 lines), [[WDR3]] 2.05× (z +7.7, 33/48 lines), [[NOC3L]] 2.23× (z +7.6, 42/48 lines), [[PDCD11]] 2.08× (z +7.4, 40/48 lines), [[TCERG1]] 1.69× (z +7.3, 43/48 lines), [[CREB5]] 2.21× (z +7.2, 22/33 lines), [[C19orf48]] 2.14× (z +7.2, 31/44 lines), [[LTV1]] 2.22× (z +7.2, 40/47 lines), [[NOL10]] 1.60× (z +7.1, 41/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3159 genes, 3,159 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[TNRC6B]] ⚠ 0.310× (z -48.7, 48/48 lines), [[FBXL20]] ⚠ 0.178× (z -39.9, 48/48 lines), [[KLHL24]] ⚠ 0.0862× (z -39.3, 48/48 lines), [[TFDP2]] ⚠ 0.329× (z -34.3, 48/48 lines), [[FBXO25]] ⚠ 0.210× (z -34.2, 44/44 lines), [[YPEL2]] ⚠ 0.150× (z -32.2, 44/44 lines), [[CREBRF]] ⚠ 0.132× (z -31.6, 48/48 lines), [[PDCD4]] ⚠ 0.244× (z -30.9, 48/48 lines), [[RB1CC1]] ⚠ 0.297× (z -29.7, 48/48 lines), [[PLEKHM3]] ⚠ 0.224× (z -29.2, 48/48 lines), [[CCDC28A]] ⚠ 0.162× (z -27.9, 48/48 lines), [[FBXO32]] ⚠ 0.158× (z -26.8, 33/34 lines)

**0.5 µM** (49 genes, 2 with an alert ⚠; 13 shown): [[PDCD4]] 0.757× (z -4.3, 27/48 lines), [[KLHDC2]] 0.753× (z -4.0, 8/48 lines), [[TMEM45B]] 0.618× (z -3.9, 10/16 lines), [[UBALD2]] 0.596× (z -3.8, 24/48 lines), [[ING4]] 0.756× (z -3.7, 11/48 lines), [[CCDC28A]] 0.740× (z -3.7, 12/48 lines), [[GRB7]] 0.633× (z -3.7, 14/23 lines), [[REST]] 0.810× (z -3.7, 18/46 lines), [[GPRC5C]] ⚠ 0.701× (z -3.6, 3/34 lines; position correction uncertain), [[FTH1]] 0.614× (z -3.6, 40/44 lines), [[ENSG00000286329]] 0.565× (z -3.6, 1/11 lines), [[YIPF4]] 0.819× (z -3.5, 14/48 lines), [[MXD4]] 0.658× (z -3.4, 7/48 lines)

**5 µM** (993 genes, 5 with an alert ⚠; 12 shown): [[PDCD4]] 0.281× (z -14.5, 46/48 lines), [[TFDP2]] 0.414× (z -14.2, 45/48 lines), [[KLHL24]] 0.173× (z -14.1, 47/48 lines), [[PLEKHM3]] 0.251× (z -14.1, 45/48 lines), [[FBXL20]] 0.255× (z -13.8, 46/48 lines), [[YPEL2]] 0.224× (z -13.3, 38/44 lines), [[CCDC28A]] 0.245× (z -12.8, 42/48 lines), [[TOM1L2]] 0.395× (z -12.7, 47/48 lines), [[RB1CC1]] 0.372× (z -12.7, 48/48 lines), [[CREBRF]] 0.229× (z -12.0, 48/48 lines), [[JMY]] 0.241× (z -12.0, 46/47 lines), [[HDAC5]] 0.240× (z -11.9, 46/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 005]] (+9.9), [[Module 004]] (+8.6), [[Module 001]] (+8.0) | [[Module 069]] (-13.7), [[Module 076]] (-12.7), [[Module 225]] (-12.4) |
| 0.5 µM | [[Module 020]] (+2.3) | [[Module 059]] (-2.3), [[Module 048]] (-2.1) |
| 5 µM | [[Module 005]] (+4.9), [[Module 001]] (+4.2), [[Module 004]] (+4.0) | [[Module 069]] (-6.2), [[Module 145]] (-5.8), [[Module 187]] (-5.5) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[NCI-H1792 (line)]] (-11.1), [[Hs 766T (line)]] (-10.5), [[SW 900 (line)]] (-6.2), [[Panc 03.27 (line)]] (-5.0), [[A-427 (line)]] (-4.4) | [[MIA PaCa-2 (line)]] (1.52), [[NCI-H460 (line)]] (1.47), [[NCI-H1792 (line)]] (1.40), [[Hs 766T (line)]] (1.32) · weakest: [[NCI-H661 (line)]] (0.666), [[LS 180 (line)]] (0.671), [[BT-474 (line)]] (0.685) |
| 0.5 µM | [[NCI-H661 (line)]] (-4.0), [[LOX-IMVI (line)]] (-3.3) | [[MIA PaCa-2 (line)]] (1.26), [[NCI-H23 (line)]] (1.26), [[SNU-1 (line)]] (1.25), [[H4 (line)]] (1.24) · weakest: [[BT-474 (line)]] (0.763), [[CFPAC-1 (line)]] (0.799), [[Panc 03.27 (line)]] (0.801) |
| 5 µM | [[NCI-H1792 (line)]] (-5.9), [[Hs 766T (line)]] (-5.1), [[RPMI-7951 (line)]] (-4.1), [[BT-474 (line)]] (-3.7), [[SW 900 (line)]] (-3.7) | [[MIA PaCa-2 (line)]] (1.40), [[NCI-H1792 (line)]] (1.39), [[NCI-H460 (line)]] (1.28), [[SW 900 (line)]] (1.27) · weakest: [[NCI-H661 (line)]] (0.658), [[LS 180 (line)]] (0.670), [[C-33 A (line)]] (0.723) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[TAK-733 (drug)]] (+0.96, MEK inhibitor); [[EX229 (drug)]] (+0.94, unclear); [[Abemaciclib (drug)]] (+0.91, CDK inhibitor); [[venetoclax (drug)]] (+0.84, unclear); [[Volasertib (drug)]] (+0.65, unclear); [[Everolimus (drug)]] (+0.64, MTOR inhibitor); [[Sapanisertib (drug)]] (+0.60, MTOR inhibitor); [[Belzutifan (drug)]] (+0.59, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 24 arrows, 24 of them with an alert ⚠; grade A 0, B 10, C 14. Shown: the 15 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[RNF165]] | 5 µM | B | RNF165 activity lowers the cells' numbers under c-Kit-IN-1 5 µM (makes them more sensitive) | lines that do not express RNF165 (21) vs lines expressing it (27) | the lines without RNF165: 1.30× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: TDRP, ZSCAN18, SH3GL3 |
| [[ARHGAP24]] | 5 µM | B | ARHGAP24 activity lowers the cells' numbers under c-Kit-IN-1 5 µM (makes them more sensitive) | lines that do not express ARHGAP24 (17) vs lines expressing it (31) | the lines without ARHGAP24: 1.45× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, GPR176 |
| [[COL12A1]] | 0.05 µM | B | COL12A1 activity lowers the cells' numbers under c-Kit-IN-1 0.05 µM (makes them more sensitive) | lines that do not express COL12A1 (23) vs lines expressing it (25) | the lines without COL12A1: 1.49× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: RFTN1, FMN2, KIAA0408; cell counts less trustworthy |
| [[ENSG00000287023]] | 0.05 µM | B | ENSG00000287023 activity lowers the cells' numbers under c-Kit-IN-1 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000287023 (25) vs lines expressing it (23) | the lines without ENSG00000287023: 1.35× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ADAMTS14, CDH13, ENSG00000248973; cell counts less trustworthy |
| [[ENSG00000258919]] | 0.5 µM | B | ENSG00000258919 activity raises the cells' numbers under c-Kit-IN-1 0.5 µM (protects the cells) | lines that do not express ENSG00000258919 (23) vs lines expressing it (25) | the lines without ENSG00000258919: 0.79× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC02320, ENSG00000266088, DIO3OS |
| [[ADAMTS14]] | 0.05 µM | B | ADAMTS14 activity lowers the cells' numbers under c-Kit-IN-1 0.05 µM (makes them more sensitive) | lines that do not express ADAMTS14 (31) vs lines expressing it (17) | the lines without ADAMTS14: 1.44× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411; cell counts less trustworthy |
| [[NIPAL1]] | 0.5 µM | B | NIPAL1 activity raises the cells' numbers under c-Kit-IN-1 0.5 µM (protects the cells) | lines that do not express NIPAL1 (5) vs lines expressing it (43) | the lines without NIPAL1: 0.79× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| [[AHR]] | 0.5 µM | B | AHR activity raises the cells' numbers under c-Kit-IN-1 0.5 µM (protects the cells) | lines that do not express AHR (7) vs lines expressing it (41) | the lines without AHR: 0.86× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[ENSG00000258394]] | 5 µM | B | ENSG00000258394 activity raises the cells' numbers under c-Kit-IN-1 5 µM (protects the cells) | lines that do not express ENSG00000258394 (17) vs lines expressing it (31) | the lines without ENSG00000258394: 0.87× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: ADGRB3, KCTD16, LINC00960; maybe low, not absent |
| [[SCAT1]] | 0.5 µM | B | SCAT1 activity raises the cells' numbers under c-Kit-IN-1 0.5 µM (protects the cells) | lines that do not express SCAT1 (16) vs lines expressing it (32) | the lines without SCAT1: 0.80× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[SPART-AS1]] | 5 µM | C | SPART-AS1 activity lowers the cells' numbers under c-Kit-IN-1 5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.33× the cells of the other lines | 0.021 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[NR3C1]] | 5 µM | C | NR3C1 activity lowers the cells' numbers under c-Kit-IN-1 5 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.36× the cells of the other lines | 0.025 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[C2orf74]] | 5 µM | C | C2orf74 activity lowers the cells' numbers under c-Kit-IN-1 5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.34× the cells of the other lines | 0.025 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[ENSG00000288755]] | 0.5 µM | C | ENSG00000288755 activity raises the cells' numbers under c-Kit-IN-1 0.5 µM (protects the cells) | lines that do not express ENSG00000288755 (3) vs lines expressing it (45) | the lines without ENSG00000288755: 0.63× the cells of the other lines | 0.026 | ⚠ few lines (3 vs 47); across organs; also absent: SLC25A45; maybe low, not absent |
| [[NR3C1]] | 0.05 µM | C | NR3C1 activity lowers the cells' numbers under c-Kit-IN-1 0.05 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.41× the cells of the other lines | 0.026 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1; cell counts less trustworthy |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| KIT | [[PKD1P6]] | moves it that way too | B | KIT activity lowers PKD1P6's level | compounds that target KIT: 3 of 4 raise it (Pexidartinib, Ponatinib, c-Kit-IN-1) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| KDR | [[PPARD]] | does not move it that way (the class's other compounds do) | B | KDR activity raises PPARD's level | compounds that target KDR: 5 of 8 lower it (Cabozantinib, Ponatinib, Regorafenib, Sulfatinib, Sunitinib) | 62% of the class's compounds vs 6.2% of all compounds | 0.036 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MET]] | [[TNFAIP1]] | moves it that way too | B | MET activity raises TNFAIP1's level | compounds that target MET: 3 of 4 lower it (Cabozantinib, Crizotinib / crizotinib, c-Kit-IN-1) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |
| KDR | [[DNAJB6]] | moves it that way too | B | KDR activity raises DNAJB6's level | compounds that target KDR: 3 of 8 lower it (Cabozantinib, Ponatinib, c-Kit-IN-1) | 38% of the class's compounds vs 1.7% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| KDR | [[DUSP10]] | moves it that way too | B | KDR activity raises DUSP10's level | compounds that target KDR: 4 of 8 lower it (Cabozantinib, Ponatinib, Sunitinib, c-Kit-IN-1) | 50% of the class's compounds vs 4.5% of all compounds | 0.077 | ⚠ off-target possible; 4 compounds; artifact flags |
| KDR | [[PGLS-DT]] | moves it that way too | B | KDR activity lowers PGLS-DT's level | compounds that target KDR: 4 of 8 raise it (Cabozantinib, Ponatinib, Sunitinib, c-Kit-IN-1) | 50% of the class's compounds vs 4.5% of all compounds | 0.077 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PDGFRA]] | [[HES1]] | moves it that way too | B | PDGFRA activity raises HES1's level | compounds that target PDGFRA: 2 of 3 lower it (Ponatinib, c-Kit-IN-1) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[PDGFRA]] | [[PKD1]] | moves it that way too | B | PDGFRA activity lowers PKD1's level | compounds that target PDGFRA: 2 of 3 raise it (Ponatinib, c-Kit-IN-1) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[PDGFRA]] | [[SAA2]] | moves it that way too | B | PDGFRA activity raises SAA2's level | compounds that target PDGFRA: 2 of 3 lower it (Ponatinib, c-Kit-IN-1) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "c-Kit-IN-1"
- `tables/drugdoses.parquet` — dd in 1111, 1112, 1113
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
