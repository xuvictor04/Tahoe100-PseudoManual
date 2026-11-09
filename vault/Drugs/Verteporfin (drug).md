---
drug: "Verteporfin"
type: "drug"
salt_base: "Verteporfin"
targets: "YAP1"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 1167
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Verteporfin

*unclear (inhibitor/antagonist) · targets: YAP1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 27 / 82 / 1167; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.40 / 0.38.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:E9 | 24 / 3 | — | +0.07 | +0.2/+0.3/+0.3 | — |
| 0.5 µM | [[Plate 08]]:E9 | 81 / 1 | — | -0.30 | +0.1/+0.5/+0.4 | — |
| 5 µM | [[Plate 09]]:E9 | 546 / 621 | — | -0.57 | -0.8/-0.3/-0.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (24 genes, none with an alert; 12 shown): [[TMEM184A]] 1.40× (z +3.9, 4/35 lines), [[LINC02405]] 1.34× (z +3.8, 0/20 lines), [[ROR2]] 1.25× (z +3.7, 0/22 lines), [[ENSG00000230021]] 1.34× (z +3.6, 21/48 lines), [[EHF]] 1.24× (z +3.6, 0/21 lines), [[CCDC26]] 1.33× (z +3.5, 0/42 lines), [[COL24A1]] 1.42× (z +3.4, 2/34 lines), [[AFAP1-AS1]] 1.29× (z +3.4, 0/15 lines), [[ENSG00000286797]] 1.50× (z +3.4, 1/12 lines), [[P4HB]] 1.30× (z +3.4, 34/48 lines), [[FOXG1]] 1.67× (z +3.3, 0/10 lines), [[ERICH2-DT]] 1.35× (z +3.2, 0/36 lines)

**0.5 µM** (81 genes, none with an alert; 12 shown): [[UTY]] 1.44× (z +6.2, 0/18 lines), [[TXLNGY]] 1.59× (z +6.0, 0/17 lines), [[MAL2]] 1.36× (z +5.6, 0/18 lines), [[PRKY]] 1.44× (z +5.1, 0/17 lines), [[GALNT13]] 1.37× (z +5.0, 0/18 lines), [[FAM83B]] 1.28× (z +4.9, 0/18 lines), [[ESRP1]] 1.43× (z +4.7, 0/18 lines), [[MME]] 1.39× (z +4.6, 0/19 lines), [[GNGT1]] 1.31× (z +4.5, 0/19 lines), [[SYK]] 1.38× (z +4.5, 0/18 lines), [[KCNMA1]] 1.25× (z +4.3, 0/23 lines), [[POTEF]] 1.42× (z +4.3, 0/19 lines)

**5 µM** (546 genes, none with an alert; 12 shown): [[ENSG00000259827]] 8.25× (z +11.0, 33/34 lines), [[MT-TV]] 3.31× (z +7.4, 31/36 lines), [[MT-TL1]] 3.20× (z +7.2, 40/43 lines), [[KIF5C]] 1.52× (z +6.4, 27/47 lines), [[KCNMA1]] 1.41× (z +6.4, 1/23 lines), [[DLEU2]] 1.24× (z +5.9, 30/49 lines), [[ZFPM2]] 1.43× (z +5.9, 6/32 lines), [[CCBE1]] 1.41× (z +5.8, 0/19 lines), [[H2AC6]] 1.67× (z +5.7, 34/48 lines), [[ENSG00000228933]] 1.45× (z +5.5, 4/22 lines), [[PDE8A]] 1.23× (z +5.5, 27/49 lines), [[TXLNGY]] 1.55× (z +5.5, 1/17 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[ATP6V0A2]] 0.821× (z -3.5, 14/47 lines), [[BRME1]] 0.688× (z -3.2, 6/32 lines), [[KIF24]] 0.824× (z -2.8, 6/46 lines)

**0.5 µM** (1 gene, none with an alert): [[PCDHB2]] 0.690× (z -3.1, 6/24 lines)

**5 µM** (621 genes, none with an alert; 12 shown): [[PSAP]] 0.574× (z -11.3, 44/49 lines), [[GPC1]] 0.453× (z -10.4, 35/45 lines), [[LGALS3BP]] 0.389× (z -9.8, 40/42 lines), [[GANAB]] 0.615× (z -9.5, 43/49 lines), [[CHPF]] 0.482× (z -8.9, 36/46 lines), [[OS9]] 0.672× (z -8.7, 44/49 lines), [[APLP2]] 0.666× (z -8.6, 43/49 lines), [[IGSF8]] 0.452× (z -8.6, 35/44 lines), [[TBL2]] 0.654× (z -8.5, 35/48 lines), [[CTSB]] 0.632× (z -8.4, 37/46 lines), [[LAMP1]] 0.630× (z -8.4, 43/48 lines), [[GRN]] 0.476× (z -8.3, 44/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 065]] (+3.5), [[Module 035]] (+2.5), [[Module 182]] (+2.4) | [[Module 050]] (-3.8), [[Module 002]] (-3.0), [[Module 007]] (-2.4) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[KATO III (line)]] (-3.5) | [[SNU-1 (line)]] (1.76), [[AN3 CA (line)]] (1.56), [[HCT15 (line)]] (1.41), [[SW 1271 (line)]] (1.28) · weakest: [[COLO 205 (line)]] (-0.189), [[HEC-1-A (line)]] (0.194), [[NCI-H1573 (line)]] (0.326) |
| 0.5 µM | — | [[RKO (line)]] (1.52), [[AN3 CA (line)]] (1.34), [[SNU-1 (line)]] (1.33), [[MIA PaCa-2 (line)]] (1.21) · weakest: [[NCI-H2122 (line)]] (0.0290), [[A-427 (line)]] (0.103), [[H4 (line)]] (0.176) |
| 5 µM | [[Hs 766T (line)]] (-4.3), [[HepG2_C3A (line)]] (-4.1) | [[HepG2_C3A (line)]] (1.43), [[hTERT-HPNE (line)]] (1.33), [[SNU-423 (line)]] (1.25), [[HS-578T (line)]] (1.24) · weakest: [[NCI-H2122 (line)]] (0.161), [[NCI-H661 (line)]] (0.464), [[SW 1271 (line)]] (0.683) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 5 next most similar without an alert.*

- [[Fostamatinib (disodium hexahydrate) (drug)]] (+0.70, Other TK inhibitor, ⚠ only 3 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Plicamycin (drug)]] (+0.62, unclear, ⚠ only 3 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Elagolix sodium (drug)]] (+0.60, unclear); [[Bicalutamide (drug)]] (+0.54, Androgen receptor antagonist); [[Imiquimod (hydrochloride) (drug)]] (+0.52, unclear, ⚠ vector dose flagged: toxic); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.48, unclear); [[Ivabradine (hydrochloride) (drug)]] (+0.48, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Rimonabant (Hydrochloride) (drug)]] (+0.48, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] (+0.45, Glucose transporter inhibitor); [[Ciclopirox (drug)]] (+0.44, unclear); [[Decitabine (drug)]] (+0.44, DNA methyltransferase inhibitor); [[Docetaxel (Trihydrate) (drug)]] (+0.43, Microtubule inhibitor); [[Allantoin (drug)]] (+0.43, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[CDH3]] | 5 µM | B | CDH3 activity raises the cells' numbers under Verteporfin 5 µM (protects the cells) | lines that do not express CDH3 (26) vs lines expressing it (22) | the lines without CDH3: 0.79× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: CKMT1A, ESRP1, GPR87; maybe low, not absent |
| [[GUCY1B2]] | 5 µM | B | GUCY1B2 activity raises the cells' numbers under Verteporfin 5 µM (protects the cells) | lines that do not express GUCY1B2 (18) vs lines expressing it (30) | the lines without GUCY1B2: 0.82× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, TNFRSF1B, MAP7; maybe low, not absent |
| [[SULT2B1]] | 5 µM | B | SULT2B1 activity raises the cells' numbers under Verteporfin 5 µM (protects the cells) | lines that do not express SULT2B1 (28) vs lines expressing it (20) | the lines without SULT2B1: 0.77× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[PLEKHG1]] | 5 µM | B | PLEKHG1 activity raises the cells' numbers under Verteporfin 5 µM (protects the cells) | lines that do not express PLEKHG1 (17) vs lines expressing it (31) | the lines without PLEKHG1: 0.78× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[ENSG00000256029]] | 5 µM | C | ENSG00000256029 activity raises the cells' numbers under Verteporfin 5 µM (protects the cells) | lines that do not express ENSG00000256029 (4) vs lines expressing it (44) | the lines without ENSG00000256029: 0.71× the cells of the other lines | 0.045 | ⚠ few lines (4 vs 46); across organs; also absent: ERRFI1, FXYD5, CAV2; maybe low, not absent |
| [[RARG]] | 5 µM | C | RARG activity raises the cells' numbers under Verteporfin 5 µM (protects the cells) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 0.67× the cells of the other lines | 0.057 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |
| [[LIFR]] | 5 µM | C | LIFR activity lowers the cells' numbers under Verteporfin 5 µM (makes them more sensitive) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 1.20× the cells of the other lines | 0.095 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Verteporfin"
- `tables/drugdoses.parquet` — dd in 1081, 1082, 1083
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
