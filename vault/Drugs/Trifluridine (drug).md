---
drug: "Trifluridine"
type: "drug"
salt_base: "Trifluridine"
targets: ""
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 216
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Trifluridine

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 216 / 115; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.15 / 0.32.
> Flags by dose: - / cell-cycle shift / cell-cycle shift. ⚠ 0.5 µM: cell-cycle shift; 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:A3 | 0 / 0 | — | +0.15 | -0.1/+0.4/+0.4 | — |
| 0.5 µM | [[Plate 05]]:A3 | 161 / 55 | — | -0.01 | +5.4/+2.9/+1.6 | ⚠ cell-cycle shift |
| 5 µM | [[Plate 14]]:A3 | 110 / 5 | 0.729 | -0.16 | +5.9/+1.6/+0.9 | ⚠ cell-cycle shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (161 genes, 149 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 24 shown): [[BLM]] ⚠ 1.39× (z +5.7, 21/46 lines; cell-cycle shift, explains ~79% of this change), [[DIAPH3]] ⚠ 1.30× (z +5.6, 29/45 lines; cell-cycle shift, explains ~62% of this change), [[CCNE2]] ⚠ 1.54× (z +5.4, 21/45 lines; cell-cycle shift, explains ~64% of this change), [[ZGRF1]] ⚠ 1.28× (z +4.9, 20/48 lines; cell-cycle shift, explains ~71% of this change), [[CSTF1]] ⚠ 1.26× (z +4.9, 16/48 lines; cell-cycle shift, explains ~15% of this change), [[FANCB]] ⚠ 1.28× (z +4.8, 19/48 lines; cell-cycle shift, explains ~93% of this change), [[SKA3]] ⚠ 1.44× (z +4.8, 20/45 lines; cell-cycle shift, explains ~63% of this change), [[MYBL2]] ⚠ 1.57× (z +4.8, 25/44 lines; cell-cycle shift, explains ~69% of this change), [[EXO1]] ⚠ 1.55× (z +4.8, 17/46 lines; cell-cycle shift, explains ~77% of this change), [[SPC25]] ⚠ 1.38× (z +4.7, 15/47 lines; cell-cycle shift, explains ~71% of this change), [[CBX5]] ⚠ 1.33× (z +4.7, 32/48 lines; cell-cycle shift, explains ~28% of this change), [[WDHD1]] ⚠ 1.27× (z +4.7, 21/48 lines; cell-cycle shift, explains ~99% of this change), [[FANCG]] 1.50× (z +4.1, 11/44 lines; cell-cycle shift (explains ~18% here)), [[RHNO1]] 1.49× (z +3.8, 12/45 lines; cell-cycle shift (explains ~23% here)), [[C9orf64]] 1.36× (z +3.7, 11/39 lines; cell-cycle shift (explains ~11% here)), [[HINT3]] 1.22× (z +3.7, 12/48 lines; cell-cycle shift (explains ~0% here)), [[RFX5]] 1.32× (z +3.5, 11/46 lines; cell-cycle shift (explains ~16% here)), [[ZDHHC16]] 1.21× (z +3.4, 6/47 lines; cell-cycle shift (explains ~0% here)), [[SEPTIN5]] 1.41× (z +3.3, 5/32 lines; cell-cycle shift (explains ~0% here)), [[TOR1A]] 1.27× (z +3.1, 8/46 lines; cell-cycle shift (explains ~5% here)), [[DIO2]] 1.36× (z +2.9, 2/33 lines; cell-cycle shift (explains ~0% here)), [[STPG1]] 1.22× (z +2.8, 8/44 lines; cell-cycle shift (explains ~0% here)), [[MAP2]] 1.30× (z +2.8, 13/33 lines; cell-cycle shift (explains ~0% here)), [[SAMD9]] 1.38× (z +2.7, 13/37 lines; cell-cycle shift (explains ~0% here))

**5 µM** (110 genes, 91 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 24 shown): [[FANCB]] ⚠ 1.29× (z +7.1, 29/48 lines; cell-cycle shift, explains ~72% of this change), [[WDHD1]] ⚠ 1.28× (z +7.0, 26/48 lines; cell-cycle shift, explains ~76% of this change), [[ATAD2]] ⚠ 1.29× (z +6.7, 29/47 lines; cell-cycle shift, explains ~74% of this change), [[EXO1]] ⚠ 1.41× (z +6.2, 29/46 lines; cell-cycle shift, explains ~83% of this change), [[RAD51AP1]] ⚠ 1.38× (z +6.1, 29/46 lines; cell-cycle shift, explains ~64% of this change), [[DNA2]] ⚠ 1.26× (z +6.0, 25/48 lines; cell-cycle shift, explains ~67% of this change), [[ZGRF1]] ⚠ 1.23× (z +6.0, 22/48 lines; cell-cycle shift, explains ~63% of this change), [[BLM]] ⚠ 1.27× (z +5.9, 24/46 lines; cell-cycle shift, explains ~88% of this change), [[ATAD5]] ⚠ 1.26× (z +5.9, 24/48 lines; cell-cycle shift, explains ~75% of this change), [[DTL]] ⚠ 1.36× (z +5.9, 29/48 lines; cell-cycle shift, explains ~91% of this change), [[DIAPH3]] ⚠ 1.22× (z +5.8, 25/45 lines; cell-cycle shift, explains ~52% of this change), [[MASTL]] ⚠ 1.25× (z +5.7, 21/48 lines; cell-cycle shift, explains ~43% of this change), [[STYK1]] 1.22× (z +4.8, 9/27 lines; cell-cycle shift (explains ~3% here)), [[RAD9B]] 1.34× (z +4.1, 3/39 lines; cell-cycle shift (explains ~2% here)), [[LINC01629]] 1.56× (z +4.0, 8/17 lines; cell-cycle shift (explains ~2% here)), [[TMEM40]] 1.43× (z +3.9, 7/22 lines; cell-cycle shift (explains ~12% here)), [[ZNF730]] 1.31× (z +3.9, 7/18 lines; cell-cycle shift (explains ~12% here)), [[TP53I3]] 1.28× (z +3.8, 6/44 lines; cell-cycle shift (explains ~0% here)), [[GCKR]] 1.43× (z +3.6, 2/17 lines; cell-cycle shift (explains ~3% here)), [[ENSG00000224738]] 1.22× (z +3.5, 7/45 lines; cell-cycle shift (explains ~0% here)), [[IL1RN]] 1.41× (z +3.5, 4/17 lines; cell-cycle shift (explains ~0% here)), [[TMEM217]] 1.32× (z +3.5, 11/45 lines; cell-cycle shift (explains ~0% here)), [[REG4]] 1.66× (z +3.4, 2/5 lines; cell-cycle shift (explains ~10% here)), [[LAPTM5]] 1.46× (z +3.4, 2/14 lines; cell-cycle shift (explains ~6% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (55 genes, 31 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 19 shown): [[ZNF461]] ⚠ 0.768× (z -4.5, 14/41 lines; cell-cycle shift, explains ~23% of this change), [[ENSG00000235609]] ⚠ 0.799× (z -4.2, 11/40 lines; cell-cycle shift, explains ~67% of this change), [[ENSG00000253100]] 0.642× (z -4.2, 13/34 lines; cell-cycle shift (explains ~9% here)), [[C9orf153]] ⚠ 0.748× (z -4.0, 15/47 lines; cell-cycle shift, explains ~26% of this change), [[LINC02649]] ⚠ 0.750× (z -4.0, 20/45 lines; cell-cycle shift, explains ~51% of this change), [[ENSG00000236255]] 0.734× (z -4.0, 19/48 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000273184]] ⚠ 0.732× (z -3.9, 26/44 lines; cell-cycle shift, explains ~25% of this change), [[SNX31]] 0.629× (z -3.8, 12/43 lines; cell-cycle shift (explains ~0% here)), [[EPIC1]] ⚠ 0.805× (z -3.8, 15/25 lines; cell-cycle shift, explains ~62% of this change), [[CHURC1-FNTB]] ⚠ 0.816× (z -3.7, 10/47 lines; cell-cycle shift, explains ~42% of this change), [[POTEF]] 0.741× (z -3.7, 6/19 lines; cell-cycle shift (explains ~1% here)), [[TMEM230]] 0.822× (z -3.7, 17/48 lines; cell-cycle shift (explains ~0% here)), [[CCDC144NL-AS1]] 0.788× (z -3.5, 0/15 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000288025]] 0.736× (z -3.5, 11/46 lines; cell-cycle shift (explains ~14% here)), [[ENSG00000258964]] 0.700× (z -3.4, 7/44 lines; cell-cycle shift (explains ~18% here)), [[ZSCAN9]] 0.793× (z -3.4, 11/47 lines; cell-cycle shift (explains ~10% here)), [[TAF12]] 0.823× (z -3.4, 12/48 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000254732]] 0.776× (z -3.4, 13/48 lines; cell-cycle shift (explains ~4% here)), [[SLC2A3]] 0.739× (z -3.4, 18/33 lines; cell-cycle shift (explains ~5% here))

**5 µM** (5 genes, 2 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift): [[H2BC12]] 0.647× (z -3.8, 24/43 lines; cell-cycle shift (explains ~0% here)), [[DHRS2]] 0.693× (z -3.6, 14/32 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000288700]] ⚠ 0.792× (z -3.3, 8/42 lines; cell-cycle shift, explains ~24% of this change), [[H2BC18]] 0.726× (z -3.3, 12/41 lines; cell-cycle shift (explains ~0% here)), [[PIF1]] ⚠ 0.831× (z -3.3, 12/47 lines; cell-cycle shift, explains ~24% of this change)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 006]] (+3.2), [[Module 025]] (+2.1) | [[Module 170]] (-3.3), [[Module 043]] (-2.4), [[Module 207]] (-2.4) |
| 5 µM | [[Module 006]] (+2.8) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[SW48 (line)]] (1.68), [[MIA PaCa-2 (line)]] (1.65), [[LS 180 (line)]] (1.53), [[HCT15 (line)]] (1.30) · weakest: [[NCI-H1792 (line)]] (-0.0318), [[AsPC-1 (line)]] (0.283), [[SHP-77 (line)]] (0.414) |
| 5 µM | [[NCI-H23 (line)]] (-3.2) | [[SW48 (line)]] (1.80), [[HT-29 (line)]] (1.78), [[A549 (line)]] (1.56), [[LS 180 (line)]] (1.50) · weakest: [[AsPC-1 (line)]] (0.0568), [[RPMI-7951 (line)]] (0.373), [[NCI-H1792 (line)]] (0.390) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Pyridoxine (hydrochloride) (drug)]] (+0.80, unclear); [[Retinoic acid (drug)]] (+0.75, Retinoic receptor agonist); [[Megestrol (drug)]] (+0.72, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Lumateperone (tosylate) (drug)]] (+0.70, unclear, ⚠ only 9 significant genes); [[Raltitrexed (drug)]] (+0.69, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Temuterkib (drug)]] (+0.66, Other MAPK inhibitor, ⚠ only 3 significant genes); [[Furosemide (drug)]] (+0.66, unclear); [[Adenine (drug)]] (+0.65, unclear); [[Palmatine (chloride) (drug)]] (+0.64, unclear); [[Berbamine (drug)]] (+0.63, unclear); [[Folic acid (drug)]] (+0.62, unclear); [[Busulfan (drug)]] (+0.62, DNA synthesis/repair inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 117 arrows, 117 of them with an alert ⚠; grade A 0, B 115, C 2. Shown: the 15 strongest; 102 more arrows (102 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SLC44A4]] | 5 µM | B | SLC44A4 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express SLC44A4 (37) vs lines expressing it (11) | the lines without SLC44A4: 0.87× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[ENSG00000253671]], [[MTUS1-DT]] | 5 µM | B | ENSG00000253671, MTUS1-DT activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express ENSG00000253671, MTUS1-DT (17) vs lines expressing them (31) | the lines without ENSG00000253671, MTUS1-DT: 0.88× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: MTUS1, ELF3-AS1, ELF3; co-absent genes |
| [[DPP4]] | 5 µM | B | DPP4 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express DPP4 (29) vs lines expressing it (19) | the lines without DPP4: 0.89× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[ENSG00000287003]] | 5 µM | B | ENSG00000287003 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express ENSG00000287003 (20) vs lines expressing it (28) | the lines without ENSG00000287003: 0.90× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: TMEM154, ALOX5, RASSF6 |
| [[TNFSF10]] | 5 µM | B | TNFSF10 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express TNFSF10 (24) vs lines expressing it (24) | the lines without TNFSF10: 0.89× the cells of the other lines | 0.030 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[TSPAN1]] | 5 µM | B | TSPAN1 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express TSPAN1 (26) vs lines expressing it (22) | the lines without TSPAN1: 0.87× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| [[OVOL1]], [[TMPRSS4]] | 5 µM | B | OVOL1, TMPRSS4 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express OVOL1, TMPRSS4 (33) vs lines expressing them (15) | the lines without OVOL1, TMPRSS4: 0.88× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: GRHL2, ST14, TMEM30B; co-absent genes |
| [[ADGRF1]] | 5 µM | B | ADGRF1 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express ADGRF1 (35) vs lines expressing it (13) | the lines without ADGRF1: 0.87× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[TRIM29]] | 5 µM | B | TRIM29 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express TRIM29 (28) vs lines expressing it (20) | the lines without TRIM29: 0.88× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[LNX1]] | 5 µM | B | LNX1 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express LNX1 (20) vs lines expressing it (28) | the lines without LNX1: 0.91× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[LINC03040]] | 5 µM | B | LINC03040 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express LINC03040 (31) vs lines expressing it (17) | the lines without LINC03040: 0.88× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2 |
| [[CEACAM1]] | 5 µM | B | CEACAM1 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express CEACAM1 (27) vs lines expressing it (21) | the lines without CEACAM1: 0.89× the cells of the other lines | 0.041 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[LCN2]] | 5 µM | B | LCN2 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express LCN2 (33) vs lines expressing it (15) | the lines without LCN2: 0.88× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[GRHL2]], [[LINC02967]] | 5 µM | B | GRHL2, LINC02967 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express GRHL2, LINC02967 (34) vs lines expressing them (14) | the lines without GRHL2, LINC02967: 0.88× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent genes |
| [[SPTLC3]] | 0.5 µM | B | SPTLC3 activity raises the cells' numbers under Trifluridine 0.5 µM (protects the cells) | lines that do not express SPTLC3 (16) vs lines expressing it (32) | the lines without SPTLC3: 0.88× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Trifluridine"
- `tables/drugdoses.parquet` — dd in 1048, 1049, 1050
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
