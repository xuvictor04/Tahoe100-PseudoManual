---
drug: "(S)-Crizotinib"
type: "drug"
salt_base: "(S)-Crizotinib"
targets: "NUDT1"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 65
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# (S)-Crizotinib

*unclear (inhibitor/antagonist) · targets: NUDT1 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 35 / 16 / 65; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.13 / 0.08.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:C6 | 0 / 35 | — | +0.92 | +0.7/-0.2/-0.1 | — |
| 0.5 µM | [[Plate 08]]:C6 | 1 / 15 | — | -0.04 | +0.6/-0.0/-0.4 | — |
| 5 µM | [[Plate 09]]:C6 | 59 / 6 | — | +0.13 | -1.2/-1.3/-0.7 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[TMEM45A]] 1.34× (z +3.7, 12/35 lines)

**5 µM** (59 genes, none with an alert; 12 shown): [[SCD]] 1.80× (z +8.0, 43/48 lines), [[FADS2]] 1.59× (z +7.6, 27/47 lines), [[FASN]] 2.11× (z +7.2, 43/46 lines), [[DHCR7]] 1.91× (z +6.4, 31/43 lines), [[HMGCS1]] 1.70× (z +6.2, 34/47 lines), [[ACSS2]] 1.50× (z +6.2, 31/47 lines), [[LDLR]] 1.58× (z +6.1, 38/46 lines), [[DHCR24]] 1.62× (z +6.0, 26/44 lines), [[HMGCR]] 1.54× (z +6.0, 34/48 lines), [[LPIN1]] 1.30× (z +5.7, 23/48 lines), [[IDI1]] 1.56× (z +5.7, 35/47 lines), [[NSDHL]] 1.37× (z +5.6, 19/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (35 genes, none with an alert; 12 shown): [[ERFL]] 0.542× (z -5.3, 12/42 lines), [[ZNF732]] 0.381× (z -4.8, 1/7 lines), [[TOX3]] 0.679× (z -4.3, 0/17 lines), [[WNT7A]] 0.479× (z -4.3, 0/9 lines), [[LINC01917]] 0.556× (z -4.2, 5/25 lines), [[TAFA5]] 0.656× (z -4.2, 1/18 lines), [[FAM95A]] 0.517× (z -4.1, 2/9 lines), [[PPARGC1A]] 0.669× (z -4.0, 1/20 lines), [[ENSG00000259925]] 0.529× (z -3.8, 3/15 lines), [[SSX1]] 0.407× (z -3.8, 0/5 lines), [[PIWIL1]] 0.602× (z -3.7, 1/9 lines), [[BARX1]] 0.484× (z -3.6, 4/16 lines)

**0.5 µM** (15 genes, none with an alert; 12 shown): [[CAPN10-DT]] 0.600× (z -4.4, 8/42 lines), [[MT-ND4L]] 0.595× (z -3.6, 39/48 lines), [[SERAC1]] 0.818× (z -3.5, 7/47 lines), [[HBS1L]] 0.832× (z -3.5, 21/48 lines), [[NAA16]] 0.799× (z -3.5, 13/48 lines), [[CASC3]] 0.756× (z -3.5, 29/48 lines), [[FBXO3]] 0.806× (z -3.4, 11/48 lines), [[MTND2P28]] 0.627× (z -3.3, 11/46 lines), [[PPTC7]] 0.800× (z -3.3, 16/48 lines), [[SRP54-AS1]] 0.753× (z -3.3, 15/48 lines), [[PREPL]] 0.815× (z -3.3, 18/48 lines), [[PRKAB2]] 0.824× (z -3.2, 13/48 lines)

**5 µM** (6 genes, none with an alert): [[ATP2B4]] 0.812× (z -4.3, 18/40 lines), [[IARS2]] 0.831× (z -3.6, 20/48 lines), [[LHX6]] 0.665× (z -3.5, 6/22 lines), [[ZNF692]] 0.818× (z -3.2, 6/47 lines), [[C2orf72]] 0.756× (z -3.0, 2/37 lines), [[INSYN2B]] 0.734× (z -3.0, 0/16 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[Module 168]] (-3.3), [[Module 171]] (-2.8), [[Module 182]] (-2.2) |
| 5 µM | [[Module 086]] (+3.8) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[C-33 A (line)]] (1.72), [[C32 (line)]] (1.58), [[NCI-H2030 (line)]] (1.40), [[NCI-H1792 (line)]] (1.38) · weakest: [[SW 1088 (line)]] (0.300), [[NCI-H460 (line)]] (0.516), [[CFPAC-1 (line)]] (0.646) |
| 0.5 µM | [[HEC-1-A (line)]] (-3.1) | — |
| 5 µM | — | [[A549 (line)]] (1.79), [[HOP62 (line)]] (1.74), [[SNU-423 (line)]] (1.73), [[hTERT-HPNE (line)]] (1.67) · weakest: [[NCI-H661 (line)]] (0.439), [[CHP-212 (line)]] (0.469), [[AN3 CA (line)]] (0.552) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Ivermectin (drug)]] (+0.68, unclear); [[Phenytoin (sodium) (drug)]] (+0.68, unclear, ⚠ only 7 significant genes); [[Cinacalcet (drug)]] (+0.62, unclear, ⚠ only 8 significant genes); [[crizotinib (drug)]] (+0.48, Multi-TK inhibitor); [[Cilostazol (drug)]] (+0.46, unclear); [[Dabrafenib (drug)]] (+0.46, RAF inhibitor); [[Paclitaxel (drug)]] (+0.45, Microtubule inhibitor, ⚠ only 3 significant genes); [[Pentagastrin (drug)]] (+0.45, unclear, ⚠ only 9 significant genes); [[Benproperine (phosphate) (drug)]] (+0.45, unclear); [[Cepharanthine (drug)]] (+0.45, unclear); [[Fenofibrate (drug)]] (+0.43, unclear); [[Fluvoxamine (drug)]] (+0.41, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[FMN2]] | 0.5 µM | B | FMN2 activity raises the cells' numbers under (S)-Crizotinib 0.5 µM (protects the cells) | lines that do not express FMN2 (26) vs lines expressing it (22) | the lines without FMN2: 0.85× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent |
| [[KLRC4-KLRK1]], [[KLRK1]] | 0.05 µM | B | KLRC4-KLRK1, KLRK1 activity raises the cells' numbers under (S)-Crizotinib 0.05 µM (protects the cells) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 0.85× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| [[CDHR2]] | 0.5 µM | B | CDHR2 activity lowers the cells' numbers under (S)-Crizotinib 0.5 µM (makes them more sensitive) | lines that do not express CDHR2 (30) vs lines expressing it (18) | the lines without CDHR2: 1.18× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: VIL1, NPSR1-AS1, EPS8L3; maybe low, not absent |
| [[KLRC3]] | 0.05 µM | B | KLRC3 activity raises the cells' numbers under (S)-Crizotinib 0.05 µM (protects the cells) | lines that do not express KLRC3 (27) vs lines expressing it (21) | the lines without KLRC3: 0.87× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| [[PLEKHO1]] | 0.5 µM | B | PLEKHO1 activity raises the cells' numbers under (S)-Crizotinib 0.5 µM (protects the cells) | lines that do not express PLEKHO1 (13) vs lines expressing it (35) | the lines without PLEKHO1: 0.82× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |
| [[ANKRD22]] | 0.5 µM | B | ANKRD22 activity lowers the cells' numbers under (S)-Crizotinib 0.5 µM (makes them more sensitive) | lines that do not express ANKRD22 (34) vs lines expressing it (14) | the lines without ANKRD22: 1.21× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |
| [[EDN1]] | 0.5 µM | B | EDN1 activity lowers the cells' numbers under (S)-Crizotinib 0.5 µM (makes them more sensitive) | lines that do not express EDN1 (27) vs lines expressing it (21) | the lines without EDN1: 1.15× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[VSTM4]] | 0.05 µM | B | VSTM4 activity lowers the cells' numbers under (S)-Crizotinib 0.05 µM (makes them more sensitive) | lines that do not express VSTM4 (31) vs lines expressing it (17) | the lines without VSTM4: 1.17× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: LINC01411, KIRREL3, CCL2 |
| [[TMEM117]] | 0.05 µM | C | TMEM117 activity raises the cells' numbers under (S)-Crizotinib 0.05 µM (protects the cells) | lines that do not express TMEM117 (3) vs lines expressing it (45) | the lines without TMEM117: 0.74× the cells of the other lines | 0.040 | ⚠ few lines (3 vs 47); across organs; also absent: KLHL9; maybe low, not absent |
| [[ZNF614]] | 0.5 µM | C | ZNF614's natural level raises the cells' numbers under (S)-Crizotinib 0.5 µM (protects the cells) | ZNF614's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.70 | 0.285 over the table, 0.077 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "(S)-Crizotinib"
- `tables/drugdoses.parquet` — dd in 3, 4, 5
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
