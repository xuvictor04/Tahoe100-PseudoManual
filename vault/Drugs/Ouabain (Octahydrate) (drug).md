---
drug: "Ouabain (Octahydrate)"
type: "drug"
salt_base: "Ouabain"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 9763
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Ouabain (Octahydrate)

*unclear (unclear) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3491 / 7518 / 9763; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.86 / 0.95.
> Flags by dose: cell-cycle shift / cell-cycle shift / cell-cycle shift; composition shift. ⚠ 0.05 µM: cell-cycle shift; 0.5 µM: cell-cycle shift; 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:H2 | 1,195 / 2,296 | — | +0.70 | +4.1/+5.6/+3.1 | ⚠ cell-cycle shift |
| 0.5 µM | [[Plate 11]]:H2 | 3,140 / 4,378 | — | -0.45 | +6.4/+6.0/+4.0 | ⚠ cell-cycle shift |
| 5 µM | [[Plate 12]]:H2 | 4,039 / 5,724 | — | -0.11 | +8.7/+9.3/+7.8 | ⚠ cell-cycle shift · composition shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1195 genes, 674 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 16 shown): [[DIAPH1]] 1.41× (z +10.1, 35/48 lines; cell-cycle shift (explains ~18% here)), [[PITPNB]] 1.34× (z +8.9, 30/48 lines; cell-cycle shift (explains ~11% here)), [[NIPBL]] ⚠ 1.25× (z +8.9, 31/48 lines; cell-cycle shift, explains ~15% of this change), [[CAB39L]] 1.51× (z +8.7, 35/48 lines; cell-cycle shift (explains ~0% here)), [[ZBTB11]] 1.66× (z +8.5, 44/48 lines; cell-cycle shift (explains ~18% here)), [[KPNA6]] ⚠ 1.33× (z +8.4, 29/48 lines; cell-cycle shift, explains ~27% of this change), [[SBNO1]] ⚠ 1.34× (z +8.4, 37/48 lines; cell-cycle shift, explains ~23% of this change), [[WDR62]] ⚠ 1.78× (z +8.4, 32/46 lines; cell-cycle shift, explains ~40% of this change), [[ASH1L]] 1.25× (z +8.3, 31/48 lines; cell-cycle shift (explains ~0% here)), [[NFKB1]] 1.62× (z +8.3, 43/48 lines; cell-cycle shift (explains ~19% here)), [[B3GALNT2]] 1.46× (z +8.2, 38/48 lines; cell-cycle shift (explains ~11% here)), [[CRY1]] 2.15× (z +8.1, 47/48 lines; cell-cycle shift (explains ~20% here)), [[SIK3]] 1.38× (z +8.1, 37/48 lines; cell-cycle shift (explains ~0% here)), [[MED13]] 1.34× (z +8.0, 37/48 lines; cell-cycle shift (explains ~0% here)), [[PPP4R3A]] 1.35× (z +8.0, 35/48 lines; cell-cycle shift (explains ~11% here)), [[UBE2K]] 1.29× (z +7.9, 29/48 lines; cell-cycle shift (explains ~10% here))

**0.5 µM** (3140 genes, 1,067 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[ASH1L]] 2.00× (z +25.9, 48/48 lines; cell-cycle shift (explains ~0% here)), [[ZFPM2-AS1]] 3.79× (z +24.8, 32/32 lines; cell-cycle shift (explains ~1% here)), [[NIPBL]] 1.86× (z +24.5, 47/48 lines; cell-cycle shift (explains ~2% here)), [[ADNP2]] 2.29× (z +21.6, 44/48 lines; cell-cycle shift (explains ~7% here)), [[MED13]] 2.10× (z +20.3, 48/48 lines; cell-cycle shift (explains ~0% here)), [[DIAPH1]] 1.99× (z +20.1, 46/48 lines; cell-cycle shift (explains ~11% here)), [[KAT6A]] 1.91× (z +19.2, 47/48 lines; cell-cycle shift (explains ~1% here)), [[CAB39L]] 2.47× (z +19.0, 47/48 lines; cell-cycle shift (explains ~0% here)), [[PIP5K1A]] 2.21× (z +18.4, 46/48 lines; cell-cycle shift (explains ~0% here)), [[SFSWAP]] 1.63× (z +18.4, 46/48 lines; cell-cycle shift (explains ~4% here)), [[SPEN]] 1.82× (z +18.3, 47/48 lines; cell-cycle shift (explains ~10% here)), [[B3GALNT2]] 2.32× (z +18.0, 47/47 lines; cell-cycle shift (explains ~9% here))

**5 µM** (4039 genes, 1,393 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[ASH1L]] 2.70× (z +36.9, 48/48 lines; cell-cycle shift (explains ~0% here)), [[NIPBL]] 2.35× (z +33.7, 48/48 lines; cell-cycle shift (explains ~4% here)), [[ZFPM2-AS1]] 6.08× (z +33.5, 32/32 lines; cell-cycle shift (explains ~2% here)), [[ADNP2]] 3.13× (z +29.7, 48/48 lines; cell-cycle shift (explains ~8% here)), [[ARRDC4]] 5.71× (z +27.1, 40/40 lines; cell-cycle shift (explains ~10% here)), [[KAT6A]] 2.47× (z +26.8, 47/48 lines; cell-cycle shift (explains ~1% here)), [[SFSWAP]] 2.03× (z +26.6, 48/48 lines; cell-cycle shift (explains ~4% here)), [[OSBPL8]] 2.58× (z +26.2, 48/48 lines; cell-cycle shift (explains ~11% here)), [[DIAPH1]] 2.41× (z +26.0, 47/48 lines; cell-cycle shift (explains ~13% here)), [[ARMH4]] 2.19× (z +26.0, 45/48 lines; cell-cycle shift (explains ~3% here)), [[CAB39L]] 3.41× (z +25.8, 48/48 lines; cell-cycle shift (explains ~0% here)), [[REL]] 3.23× (z +25.6, 48/48 lines; cell-cycle shift (explains ~10% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2296 genes, 1,329 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[RAD51B]] 0.459× (z -10.0, 44/48 lines; cell-cycle shift (explains ~22% here)), [[PLEKHH2]] 0.630× (z -9.2, 19/34 lines; cell-cycle shift (explains ~18% here)), [[ZNF25]] 0.561× (z -9.1, 33/48 lines; cell-cycle shift (explains ~24% here)), [[WASHC3]] 0.523× (z -8.9, 34/48 lines; cell-cycle shift (explains ~22% here)), [[TRIM9]] 0.550× (z -8.9, 23/32 lines; cell-cycle shift (explains ~1% here)), [[ARHGAP44]] 0.679× (z -8.8, 24/32 lines; cell-cycle shift (explains ~20% here)), [[NR2F2-AS1]] 0.473× (z -8.7, 34/40 lines; cell-cycle shift (explains ~19% here)), [[ACP6]] 0.608× (z -8.7, 29/45 lines; cell-cycle shift (explains ~20% here)), [[ZNF395]] 0.598× (z -8.6, 40/46 lines; cell-cycle shift (explains ~0% here)), [[LINC01473]] 0.554× (z -8.5, 37/48 lines; cell-cycle shift (explains ~24% here)), [[MMP17]] 0.482× (z -8.4, 14/29 lines; cell-cycle shift (explains ~3% here)), [[BTBD8]] 0.470× (z -8.4, 33/46 lines; cell-cycle shift (explains ~22% here))

**0.5 µM** (4378 genes, 1,464 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[ZNF25]] 0.285× (z -19.8, 42/46 lines; cell-cycle shift (explains ~14% here)), [[CCDC7]] 0.252× (z -19.6, 45/46 lines; cell-cycle shift (explains ~15% here)), [[ATG4C]] 0.426× (z -19.0, 43/47 lines; cell-cycle shift (explains ~4% here)), [[PAPSS1]] 0.493× (z -18.9, 46/48 lines; cell-cycle shift (explains ~1% here)), [[FBXO16]] 0.241× (z -18.2, 38/39 lines; cell-cycle shift (explains ~9% here)), [[KIF3A]] 0.488× (z -17.8, 45/48 lines; cell-cycle shift (explains ~1% here)), [[TMEM182]] 0.330× (z -17.7, 45/47 lines; cell-cycle shift (explains ~15% here)), [[SYT17]] 0.315× (z -17.7, 33/34 lines; cell-cycle shift (explains ~18% here)), [[ARHGAP44]] 0.460× (z -17.7, 28/31 lines; cell-cycle shift (explains ~6% here)), [[ACP6]] 0.368× (z -17.6, 39/43 lines; cell-cycle shift (explains ~12% here)), [[CLCN3]] 0.516× (z -17.3, 44/48 lines; cell-cycle shift (explains ~2% here)), [[SLX4IP]] 0.275× (z -17.2, 46/46 lines; cell-cycle shift (explains ~10% here))

**5 µM** (5724 genes, 2,058 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[ATG4C]] 0.269× (z -29.2, 45/47 lines; cell-cycle shift (explains ~5% here)), [[CCDC7]] 0.159× (z -26.1, 46/46 lines; cell-cycle shift (explains ~17% here)), [[SLC1A1]] 0.210× (z -26.1, 37/37 lines; cell-cycle shift (explains ~11% here)), [[FAM114A1]] 0.290× (z -25.9, 45/46 lines; cell-cycle shift (explains ~23% here)), [[EFCAB11]] 0.251× (z -25.6, 48/48 lines; cell-cycle shift (explains ~2% here)), [[TMEM182]] 0.211× (z -24.9, 47/47 lines; cell-cycle shift (explains ~17% here)), [[ACP6]] 0.247× (z -24.6, 45/45 lines; cell-cycle shift (explains ~13% here)), [[CTPS2]] 0.303× (z -24.1, 47/47 lines; cell-cycle shift (explains ~17% here)), [[BABAM2]] 0.271× (z -23.9, 47/48 lines; cell-cycle shift (explains ~24% here)), [[ZNF248]] 0.278× (z -23.8, 48/48 lines; cell-cycle shift (explains ~21% here)), [[GPR180]] 0.287× (z -23.7, 44/46 lines; cell-cycle shift (explains ~3% here)), [[SLC2A10]] 0.124× (z -23.2, 28/30 lines; cell-cycle shift (explains ~16% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 233]] (+3.2), [[Module 214]] (+2.9), [[Module 205]] (+2.8) | [[Module 200]] (-4.7), [[Module 230]] (-3.4), [[Module 052]] (-3.3) |
| 0.5 µM | [[Module 095]] (+8.6), [[Module 194]] (+6.2), [[Module 124]] (+6.0) | [[Module 065]] (-9.0), [[Module 052]] (-8.2), [[Module 200]] (-7.9) |
| 5 µM | [[Module 095]] (+13.3), [[Module 194]] (+9.0), [[Module 233]] (+8.6) | [[Module 052]] (-13.0), [[Module 146]] (-12.8), [[Module 200]] (-11.7) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[C-33 A (line)]] (-3.3), [[LOX-IMVI (line)]] (-3.2) | [[NCI-H460 (line)]] (2.38), [[H4 (line)]] (2.27), [[SW 900 (line)]] (1.74), [[PANC-1 (line)]] (1.69) · weakest: [[HEC-1-A (line)]] (0.159), [[Panc 03.27 (line)]] (0.270), [[NCI-H2347 (line)]] (0.306) |
| 0.5 µM | [[SW 900 (line)]] (-6.7), [[NCI-H460 (line)]] (-6.1), [[LOX-IMVI (line)]] (-5.5), [[H4 (line)]] (-4.9), [[NCI-H23 (line)]] (-3.9) | [[PANC-1 (line)]] (1.48), [[SW480 (line)]] (1.48), [[BT-474 (line)]] (1.45), [[H4 (line)]] (1.42) · weakest: [[A498 (line)]] (0.353), [[SW 1088 (line)]] (0.468), [[HEC-1-A (line)]] (0.555) |
| 5 µM | [[LOX-IMVI (line)]] (-8.1), [[RPMI-7951 (line)]] (-6.0), [[SNU-1 (line)]] (-4.6), [[RKO (line)]] (-4.4), [[SW 900 (line)]] (-4.3) | [[PANC-1 (line)]] (1.41), [[H4 (line)]] (1.38), [[SW480 (line)]] (1.34), [[NCI-H460 (line)]] (1.27) · weakest: [[A498 (line)]] (0.396), [[SK-MEL-2 (line)]] (0.668), [[HEC-1-A (line)]] (0.695) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Digitoxin (drug)]] (+0.82, unclear, ⚠ vector dose flagged: toxic; transcription drop; cell-cycle shift); [[Gefitinib (drug)]] (+0.39, EGFR/ERBB inhibitor); [[RMC-6236 (drug)]] (+0.29, RAS inhibitor); [[Bimiralisib (drug)]] (+0.28, PI3K/AKT inhibitor); [[Fusidic acid (drug)]] (+0.27, unclear); [[AZD-8055 (drug)]] (+0.22, MTOR inhibitor); [[Cobimetinib (drug)]] (+0.22, MEK inhibitor); [[Carbidopa (monohydrate) (drug)]] (+0.22, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only; position not correctable)); [[Encorafenib (drug)]] (+0.22, RAF inhibitor); [[BI-3406 (drug)]] (+0.21, RAS inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 52 arrows, 52 of them with an alert ⚠; grade A 0, B 34, C 18. Shown: the 15 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[KCNMA1]] | 0.5 µM | B | KCNMA1 activity lowers the cells' numbers under Ouabain (Octahydrate) 0.5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.48× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[MAP3K15]] | 0.05 µM | B | MAP3K15 activity lowers the cells' numbers under Ouabain (Octahydrate) 0.05 µM (makes them more sensitive) | lines that do not express MAP3K15 (19) vs lines expressing it (29) | the lines without MAP3K15: 1.21× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| [[PCDH1]] | 5 µM | B | PCDH1 activity raises the cells' numbers under Ouabain (Octahydrate) 5 µM (protects the cells) | lines that do not express PCDH1 (20) vs lines expressing it (28) | the lines without PCDH1: 0.71× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[TCF4]] | 5 µM | B | TCF4 activity lowers the cells' numbers under Ouabain (Octahydrate) 5 µM (makes them more sensitive) | lines that do not express TCF4 (25) vs lines expressing it (23) | the lines without TCF4: 1.36× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1 |
| [[ERBB3]] | 5 µM | B | ERBB3 activity raises the cells' numbers under Ouabain (Octahydrate) 5 µM (protects the cells) | lines that do not express ERBB3 (27) vs lines expressing it (21) | the lines without ERBB3: 0.74× the cells of the other lines | 0.064 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[FLRT2]] | 0.5 µM | B | FLRT2 activity lowers the cells' numbers under Ouabain (Octahydrate) 0.5 µM (makes them more sensitive) | lines that do not express FLRT2 (29) vs lines expressing it (19) | the lines without FLRT2: 1.41× the cells of the other lines | 0.070 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| [[STC1]] | 5 µM | B | STC1 activity lowers the cells' numbers under Ouabain (Octahydrate) 5 µM (makes them more sensitive) | lines that do not express STC1 (24) vs lines expressing it (24) | the lines without STC1: 1.33× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[CDH3]] | 5 µM | B | CDH3 activity raises the cells' numbers under Ouabain (Octahydrate) 5 µM (protects the cells) | lines that do not express CDH3 (26) vs lines expressing it (22) | the lines without CDH3: 0.81× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: CKMT1A, ESRP1, GPR87; maybe low, not absent |
| [[ENSG00000230647]] | 0.5 µM | B | ENSG00000230647 activity lowers the cells' numbers under Ouabain (Octahydrate) 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.34× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[MYH14]] | 0.5 µM | B | MYH14 activity raises the cells' numbers under Ouabain (Octahydrate) 0.5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.72× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[RBP1]] | 0.5 µM | B | RBP1 activity raises the cells' numbers under Ouabain (Octahydrate) 0.5 µM (protects the cells) | lines that do not express RBP1 (37) vs lines expressing it (11) | the lines without RBP1: 0.67× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000232252, ENSG00000260573, LGR5 |
| [[ZNF860]] | 0.5 µM | B | ZNF860 activity raises the cells' numbers under Ouabain (Octahydrate) 0.5 µM (protects the cells) | lines that do not express ZNF860 (16) vs lines expressing it (32) | the lines without ZNF860: 0.73× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[IL15]] | 0.05 µM | B | IL15 activity raises the cells' numbers under Ouabain (Octahydrate) 0.05 µM (protects the cells) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 0.81× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[CD44]] | 0.05 µM | B | CD44 activity raises the cells' numbers under Ouabain (Octahydrate) 0.05 µM (protects the cells) | lines that do not express CD44 (15) vs lines expressing it (33) | the lines without CD44: 0.84× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[SULT2B1]] | 5 µM | B | SULT2B1 activity raises the cells' numbers under Ouabain (Octahydrate) 5 µM (protects the cells) | lines that do not express SULT2B1 (28) vs lines expressing it (20) | the lines without SULT2B1: 0.80× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Ouabain (Octahydrate)"
- `tables/drugdoses.parquet` — dd in 753, 754, 755
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
