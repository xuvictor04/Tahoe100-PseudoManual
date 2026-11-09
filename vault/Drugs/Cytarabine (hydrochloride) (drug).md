---
drug: "Cytarabine (hydrochloride)"
type: "drug"
salt_base: "Cytarabine"
targets: ""
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 366
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Cytarabine (hydrochloride)

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 107 / 242 / 366; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.56 / 0.38.
> Flags by dose: - / cell-cycle shift / cell-cycle shift. ⚠ 0.5 µM: cell-cycle shift; 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:F10 | 51 / 56 | — | +0.50 | +3.8/-2.9/-0.4 | — |
| 0.5 µM | [[Plate 08]]:F10 | 144 / 98 | — | -0.08 | +4.2/-4.5/-0.9 | ⚠ cell-cycle shift |
| 5 µM | [[Plate 09]]:F10 | 211 / 155 | — | -0.03 | +6.1/-2.7/+1.7 | ⚠ cell-cycle shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (51 genes, none with an alert; 12 shown): [[ZGRF1]] 1.30× (z +5.0, 16/48 lines), [[ATAD5]] 1.33× (z +4.7, 24/48 lines), [[ATAD2]] 1.30× (z +4.6, 21/47 lines), [[BRIP1]] 1.42× (z +4.4, 26/47 lines), [[DNA2]] 1.29× (z +4.3, 12/47 lines), [[LIG1]] 1.30× (z +4.3, 20/47 lines), [[MIR924HG]] 1.44× (z +4.2, 22/40 lines), [[CCDC15]] 1.29× (z +4.1, 9/46 lines), [[WDHD1]] 1.25× (z +4.1, 18/48 lines), [[CCNE2]] 1.42× (z +4.1, 14/46 lines), [[EXO1]] 1.41× (z +4.1, 19/45 lines), [[HROB]] 1.28× (z +3.8, 3/46 lines)

**0.5 µM** (144 genes, 129 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 24 shown): [[CCNE2]] ⚠ 1.83× (z +7.6, 26/47 lines; cell-cycle shift, explains ~61% of this change), [[E2F7]] ⚠ 1.43× (z +6.6, 25/43 lines; cell-cycle shift, explains ~41% of this change), [[ZGRF1]] ⚠ 1.36× (z +6.3, 21/48 lines; cell-cycle shift, explains ~39% of this change), [[MCM8]] ⚠ 1.44× (z +6.0, 29/48 lines; cell-cycle shift, explains ~81% of this change), [[DNA2]] ⚠ 1.37× (z +5.8, 25/47 lines; cell-cycle shift, explains ~83% of this change), [[BRIP1]] ⚠ 1.52× (z +5.7, 33/47 lines; cell-cycle shift, explains ~59% of this change), [[POLA2]] ⚠ 1.38× (z +5.7, 19/47 lines; cell-cycle shift, explains ~74% of this change), [[CCDC14]] ⚠ 1.25× (z +5.7, 29/48 lines; cell-cycle shift, explains ~45% of this change), [[WDHD1]] ⚠ 1.33× (z +5.6, 20/48 lines; cell-cycle shift, explains ~80% of this change), [[FANCI]] ⚠ 1.39× (z +5.5, 30/48 lines; cell-cycle shift, explains ~47% of this change), [[MIR924HG]] ⚠ 1.53× (z +5.3, 29/40 lines; cell-cycle shift, explains ~57% of this change), [[ATAD5]] ⚠ 1.34× (z +5.2, 26/48 lines; cell-cycle shift, explains ~75% of this change), [[DAPK2]] 1.42× (z +5.1, 13/37 lines; cell-cycle shift (explains ~23% here)), [[DIAPH3]] 1.23× (z +4.4, 24/45 lines; cell-cycle shift (explains ~0% here)), [[MAST4]] 1.26× (z +4.3, 17/37 lines; cell-cycle shift (explains ~0% here)), [[C1QTNF1]] 1.32× (z +3.6, 6/27 lines; cell-cycle shift (explains ~11% here)), [[LINC01629]] 1.72× (z +3.5, 6/17 lines; cell-cycle shift (explains ~19% here)), [[SLCO2A1]] 1.44× (z +3.3, 4/30 lines; cell-cycle shift (explains ~1% here)), [[NANOS3]] 1.49× (z +3.3, 6/41 lines; cell-cycle shift (explains ~5% here)), [[ZC3H12C]] 1.24× (z +3.1, 17/41 lines; cell-cycle shift (explains ~7% here)), [[MR1]] 1.34× (z +3.0, 6/41 lines; cell-cycle shift (explains ~17% here)), [[PLXNC1]] 1.29× (z +3.0, 4/45 lines; cell-cycle shift (explains ~10% here)), [[SMC1B]] 1.45× (z +3.0, 1/37 lines; cell-cycle shift (explains ~20% here)), [[PLA2G4C]] 1.21× (z +2.9, 8/45 lines; cell-cycle shift (explains ~0% here))

**5 µM** (211 genes, 168 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 24 shown): [[CCNE2]] ⚠ 1.83× (z +7.3, 28/44 lines; cell-cycle shift, explains ~77% of this change), [[E2F7]] ⚠ 1.43× (z +6.4, 24/43 lines; cell-cycle shift, explains ~57% of this change), [[HELLS]] ⚠ 1.49× (z +6.0, 34/48 lines; cell-cycle shift, would explain all of this change), [[POLA2]] ⚠ 1.42× (z +6.0, 25/47 lines; cell-cycle shift, explains ~87% of this change), [[GINS4]] ⚠ 1.58× (z +6.0, 23/46 lines; cell-cycle shift, explains ~84% of this change), [[DNA2]] ⚠ 1.40× (z +5.9, 25/47 lines; cell-cycle shift, explains ~95% of this change), [[NTN1]] ⚠ 1.40× (z +5.7, 17/30 lines; cell-cycle shift, explains ~47% of this change), [[FBF1]] ⚠ 1.50× (z +5.6, 17/46 lines; cell-cycle shift, explains ~66% of this change), [[WDHD1]] ⚠ 1.34× (z +5.6, 22/48 lines; cell-cycle shift, would explain all of this change), [[MCM10]] ⚠ 1.66× (z +5.6, 25/42 lines; cell-cycle shift, would explain all of this change), [[FAM111B]] ⚠ 1.95× (z +5.5, 24/36 lines; cell-cycle shift, explains ~97% of this change), [[WDR76]] ⚠ 1.48× (z +5.5, 19/45 lines; cell-cycle shift, would explain all of this change), [[ACTA2]] 1.61× (z +4.9, 14/36 lines; cell-cycle shift (explains ~19% here)), [[ENKUR]] 1.57× (z +4.6, 18/27 lines; cell-cycle shift (explains ~6% here)), [[PTCHD4]] 1.59× (z +4.6, 11/15 lines; cell-cycle shift (explains ~7% here)), [[EDA2R]] 1.57× (z +4.6, 7/18 lines; cell-cycle shift (explains ~0% here)), [[DRAM1]] 1.30× (z +4.2, 18/42 lines; cell-cycle shift (explains ~0% here)), [[CDKN1A]] 1.34× (z +4.2, 22/45 lines; cell-cycle shift (explains ~0% here)), [[PRRG4]] 1.38× (z +4.0, 10/30 lines; cell-cycle shift (explains ~0% here)), [[APOBEC3A]] 1.58× (z +4.0, 10/38 lines; cell-cycle shift (explains ~0% here)), [[ANKRA2]] 1.28× (z +3.9, 18/48 lines; cell-cycle shift (explains ~0% here)), [[FAS]] 1.30× (z +3.9, 15/39 lines; cell-cycle shift (explains ~15% here)), [[TRAF1]] 1.39× (z +3.7, 15/35 lines; cell-cycle shift (explains ~0% here)), [[BLOC1S2]] 1.35× (z +3.7, 18/47 lines; cell-cycle shift (explains ~13% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (56 genes, none with an alert; 12 shown): [[PIF1]] 0.469× (z -8.8, 31/46 lines), [[CENPA]] 0.720× (z -7.0, 27/47 lines), [[CCNF]] 0.650× (z -6.5, 28/47 lines), [[TROAP]] 0.630× (z -6.2, 23/47 lines), [[CENPE]] 0.700× (z -5.7, 36/48 lines), [[KIF20A]] 0.581× (z -5.5, 26/46 lines), [[PLK1]] 0.638× (z -5.4, 21/47 lines), [[GAS2L3]] 0.729× (z -5.1, 27/48 lines), [[CCNB1]] 0.655× (z -4.9, 29/47 lines), [[ASPM]] 0.693× (z -4.8, 31/47 lines), [[AURKA]] 0.692× (z -4.7, 26/48 lines), [[FAM72B]] 0.580× (z -4.6, 10/34 lines)

**0.5 µM** (98 genes, 87 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 23 shown): [[PIF1]] ⚠ 0.340× (z -13.5, 40/46 lines; cell-cycle shift, explains ~38% of this change), [[CCNF]] ⚠ 0.565× (z -9.3, 36/47 lines; cell-cycle shift, explains ~48% of this change), [[CENPE]] ⚠ 0.607× (z -8.7, 42/48 lines; cell-cycle shift, explains ~70% of this change), [[KIF20A]] ⚠ 0.461× (z -8.5, 38/46 lines; cell-cycle shift, explains ~57% of this change), [[PLK1]] ⚠ 0.538× (z -8.1, 36/47 lines; cell-cycle shift, explains ~65% of this change), [[CCNB1]] ⚠ 0.562× (z -7.2, 37/47 lines; cell-cycle shift, explains ~69% of this change), [[CENPA]] ⚠ 0.733× (z -7.1, 24/47 lines; cell-cycle shift, explains ~51% of this change), [[FAM83D]] ⚠ 0.619× (z -6.9, 27/47 lines; cell-cycle shift, explains ~42% of this change), [[TROAP]] ⚠ 0.632× (z -6.7, 28/47 lines; cell-cycle shift, explains ~47% of this change), [[CDC20]] ⚠ 0.507× (z -6.4, 38/44 lines; cell-cycle shift, explains ~55% of this change), [[ASPM]] ⚠ 0.635× (z -6.3, 34/47 lines; cell-cycle shift, explains ~84% of this change), [[DEPDC1]] ⚠ 0.599× (z -6.3, 35/46 lines; cell-cycle shift, explains ~98% of this change), [[H1-3]] 0.470× (z -5.0, 28/35 lines; cell-cycle shift (explains ~22% here)), [[H2BC17]] 0.400× (z -4.7, 23/45 lines; cell-cycle shift (explains ~20% here)), [[H2BC18]] 0.533× (z -4.5, 22/43 lines; cell-cycle shift (explains ~16% here)), [[ENSG00000253100]] 0.621× (z -4.5, 10/34 lines; cell-cycle shift (explains ~0% here)), [[H3C12]] 0.609× (z -4.4, 13/47 lines; cell-cycle shift (explains ~12% here)), [[RBM15-AS1]] 0.722× (z -3.7, 4/44 lines; cell-cycle shift (explains ~0% here)), [[H2AX]] 0.645× (z -3.6, 17/47 lines; cell-cycle shift (explains ~9% here)), [[H2AC12]] 0.541× (z -3.6, 18/43 lines; cell-cycle shift (explains ~24% here)), [[MXD3]] 0.755× (z -3.5, 8/47 lines; cell-cycle shift (explains ~7% here)), [[H2BC8]] 0.521× (z -3.4, 12/34 lines; cell-cycle shift (explains ~16% here)), [[H2BC12]] 0.579× (z -3.3, 16/44 lines; cell-cycle shift (explains ~21% here))

**5 µM** (155 genes, 102 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 23 shown): [[PIF1]] ⚠ 0.344× (z -12.9, 36/45 lines; cell-cycle shift, explains ~33% of this change), [[PLK1]] ⚠ 0.535× (z -7.9, 29/46 lines; cell-cycle shift, explains ~55% of this change), [[CENPA]] ⚠ 0.711× (z -7.5, 29/47 lines; cell-cycle shift, explains ~39% of this change), [[CCNF]] ⚠ 0.631× (z -7.2, 25/47 lines; cell-cycle shift, explains ~43% of this change), [[GPSM2]] ⚠ 0.703× (z -7.0, 31/48 lines; cell-cycle shift, explains ~47% of this change), [[ENSG00000253100]] 0.467× (z -6.9, 20/34 lines; cell-cycle shift (explains ~0% here)), [[KIF20A]] ⚠ 0.534× (z -6.6, 31/46 lines; cell-cycle shift, explains ~57% of this change), [[CENPE]] ⚠ 0.683× (z -6.3, 37/48 lines; cell-cycle shift, explains ~71% of this change), [[CCNB1]] ⚠ 0.593× (z -6.3, 33/47 lines; cell-cycle shift, explains ~58% of this change), [[AURKA]] ⚠ 0.621× (z -6.3, 37/48 lines; cell-cycle shift, explains ~62% of this change), [[ENSG00000258101]] ⚠ 0.558× (z -6.3, 18/41 lines; cell-cycle shift, explains ~34% of this change), [[TROAP]] ⚠ 0.649× (z -6.1, 21/47 lines; cell-cycle shift, explains ~36% of this change), [[H1-5]] 0.378× (z -5.2, 25/35 lines; cell-cycle shift (explains ~9% here)), [[FRAS1]] 0.810× (z -4.4, 7/26 lines; cell-cycle shift (explains ~0% here)), [[H2BC18]] 0.536× (z -4.3, 20/42 lines; cell-cycle shift (explains ~9% here)), [[H1-3]] 0.519× (z -4.2, 21/35 lines; cell-cycle shift (explains ~11% here)), [[H2BC8]] 0.429× (z -4.2, 19/32 lines; cell-cycle shift (explains ~5% here)), [[ERFL]] 0.616× (z -4.1, 6/39 lines; cell-cycle shift (explains ~10% here)), [[PTCH1]] 0.763× (z -4.0, 16/45 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000286221]] 0.743× (z -4.0, 9/43 lines; cell-cycle shift (explains ~0% here)), [[H4C5]] 0.498× (z -4.0, 19/43 lines; cell-cycle shift (explains ~21% here)), [[ENSG00000255094]] 0.622× (z -3.9, 13/42 lines; cell-cycle shift (explains ~14% here)), [[LINC00672]] 0.679× (z -3.9, 11/41 lines; cell-cycle shift (explains ~13% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 006]] (+2.4), [[Module 091]] (+2.0) | [[Module 022]] (-2.5) |
| 5 µM | [[Module 006]] (+2.5), [[Module 062]] (+2.2), [[Module 068]] (+2.1) | [[Module 179]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[A-427 (line)]] (1.55), [[SW48 (line)]] (1.54), [[NCI-H1573 (line)]] (1.52), [[NCI-H460 (line)]] (1.45) · weakest: [[SW 1088 (line)]] (-0.271), [[hTERT-HPNE (line)]] (0.428), [[NCI-H661 (line)]] (0.459) |
| 0.5 µM | [[HOP62 (line)]] (-3.6), [[A549 (line)]] (-3.4), [[H4 (line)]] (-3.3) | [[H4 (line)]] (1.52), [[NCI-H460 (line)]] (1.51), [[A549 (line)]] (1.50), [[C32 (line)]] (1.34) · weakest: [[SW 1088 (line)]] (0.285), [[NCI-H661 (line)]] (0.461), [[NCI-H2347 (line)]] (0.585) |
| 5 µM | — | [[NCI-H460 (line)]] (1.42), [[C32 (line)]] (1.37), [[SNU-423 (line)]] (1.33), [[A549 (line)]] (1.26) · weakest: [[AsPC-1 (line)]] (0.565), [[SW 1088 (line)]] (0.640), [[NCI-H1792 (line)]] (0.650) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Cytarabine (drug)]] (+0.68, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Amsacrine (drug)]] (+0.60, DNA synthesis/repair inhibitor); [[Irinotecan (drug)]] (+0.59, DNA synthesis/repair inhibitor); [[Plicamycin (drug)]] (+0.46, unclear, ⚠ only 3 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Irinotecan (hydrochloride) (drug)]] (+0.45, DNA synthesis/repair inhibitor); [[Gemcitabine (drug)]] (+0.44, DNA synthesis/repair inhibitor); [[Methotrexate (drug)]] (+0.36, DNA synthesis/repair inhibitor); [[Trifluridine (drug)]] (+0.35, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Silodosin (drug)]] (+0.31, unclear); [[Arbutin (drug)]] (+0.30, unclear); [[Pimitespib (drug)]] (+0.28, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 15 arrows, 15 of them with an alert ⚠; grade A 0, B 8, C 7.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[FAAH2]] | 0.5 µM | B | FAAH2 activity raises the cells' numbers under Cytarabine (hydrochloride) 0.5 µM (protects the cells) | lines that do not express FAAH2 (26) vs lines expressing it (22) | the lines without FAAH2: 0.75× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[MYH14]] | 0.5 µM | B | MYH14 activity raises the cells' numbers under Cytarabine (hydrochloride) 0.5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.75× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[BNC2]] | 0.5 µM | B | BNC2 activity lowers the cells' numbers under Cytarabine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express BNC2 (21) vs lines expressing it (27) | the lines without BNC2: 1.29× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[KCNH8]] | 0.5 µM | B | KCNH8 activity raises the cells' numbers under Cytarabine (hydrochloride) 0.5 µM (protects the cells) | lines that do not express KCNH8 (32) vs lines expressing it (16) | the lines without KCNH8: 0.83× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22 |
| [[HTRA3]] | 0.5 µM | B | HTRA3 activity lowers the cells' numbers under Cytarabine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express HTRA3 (31) vs lines expressing it (17) | the lines without HTRA3: 1.30× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[ENSG00000260710]] | 0.5 µM | B | ENSG00000260710 activity raises the cells' numbers under Cytarabine (hydrochloride) 0.5 µM (protects the cells) | lines that do not express ENSG00000260710 (19) vs lines expressing it (29) | the lines without ENSG00000260710: 0.81× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: LAD1, TRIM29, NOS3; maybe low, not absent |
| [[TMEM45B]] | 0.5 µM | B | TMEM45B activity raises the cells' numbers under Cytarabine (hydrochloride) 0.5 µM (protects the cells) | lines that do not express TMEM45B (32) vs lines expressing it (16) | the lines without TMEM45B: 0.79× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[MTUS1]] | 0.5 µM | B | MTUS1 activity raises the cells' numbers under Cytarabine (hydrochloride) 0.5 µM (protects the cells) | lines that do not express MTUS1 (17) vs lines expressing it (31) | the lines without MTUS1: 0.81× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[FIGN]] | 0.5 µM | C | FIGN activity lowers the cells' numbers under Cytarabine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.25× the cells of the other lines | 0.013 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[SPART-AS1]] | 0.5 µM | C | SPART-AS1 activity lowers the cells' numbers under Cytarabine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.24× the cells of the other lines | 0.018 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[NR3C1]] | 0.5 µM | C | NR3C1 activity lowers the cells' numbers under Cytarabine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.30× the cells of the other lines | 0.023 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[C2orf74]] | 0.5 µM | C | C2orf74 activity lowers the cells' numbers under Cytarabine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.24× the cells of the other lines | 0.031 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[SCAMP5]] | 0.5 µM | C | SCAMP5 activity raises the cells' numbers under Cytarabine (hydrochloride) 0.5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.71× the cells of the other lines | 0.085 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| [[PWWP2B]] | 0.5 µM | C | PWWP2B activity raises the cells' numbers under Cytarabine (hydrochloride) 0.5 µM (protects the cells) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 0.70× the cells of the other lines | 0.091 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| [[KLHL9]] | 0.5 µM | C | KLHL9 activity raises the cells' numbers under Cytarabine (hydrochloride) 0.5 µM (protects the cells) | lines that do not express KLHL9 (3) vs lines expressing it (45) | the lines without KLHL9: 0.71× the cells of the other lines | 0.095 | ⚠ few lines (3 vs 47); across organs; also absent: MTAP, TMEM117, CFL1P1-1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Cytarabine (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 305, 306, 307
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
