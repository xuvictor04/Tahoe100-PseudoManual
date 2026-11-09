---
drug: "Dapagliflozin ((2S)-1,2-propanediol, hydrate)"
type: "drug"
salt_base: "Dapagliflozin"
targets: "SLC5A2"
moa_fine: "Glucose transporter inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 151
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Dapagliflozin ((2S)-1,2-propanediol, hydrate)

*Glucose transporter inhibitor (inhibitor/antagonist) · targets: SLC5A2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 151 / 25 / 5; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): -0.06 / 0.12.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:G6 | 136 / 15 | — | -0.76 | +0.2/+0.8/+0.7 | — |
| 0.5 µM | [[Plate 08]]:G6 | 6 / 19 | — | -0.94 | -1.5/-1.1/-0.8 | — |
| 5 µM | [[Plate 09]]:G6 | 2 / 3 | — | -0.09 | -1.4/-0.3/+0.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (136 genes, none with an alert; 12 shown): [[RPS18]] 1.59× (z +4.7, 39/47 lines), [[PPP1R9A-AS1]] 1.46× (z +4.2, 8/33 lines), [[RORB]] 1.60× (z +4.1, 1/13 lines), [[ZNF667]] 1.68× (z +4.1, 0/10 lines), [[CFL1P1-1]] 1.65× (z +4.0, 2/23 lines), [[ENSG00000287149]] 1.96× (z +4.0, 0/3 lines), [[LINC02223]] 1.80× (z +4.0, 0/7 lines), [[LINC02438]] 1.51× (z +3.9, 0/12 lines), [[ZNF813]] 1.37× (z +3.9, 4/27 lines), [[SLC38A4]] 1.54× (z +3.9, 3/13 lines), [[GPR141]] 1.77× (z +3.8, 0/7 lines), [[ENSG00000235837]] 1.55× (z +3.8, 3/23 lines)

**0.5 µM** (6 genes, none with an alert): [[ATP8A2]] 1.34× (z +3.7, 4/41 lines), [[DPH2]] 1.35× (z +3.0, 1/39 lines), [[ENSG00000290792]] 1.32× (z +3.0, 4/45 lines), [[GAB3]] 1.36× (z +3.0, 2/24 lines), [[ENSG00000279207]] 1.44× (z +2.9, 3/41 lines), [[ENSG00000236924]] 1.23× (z +2.9, 1/37 lines)

**5 µM** (2 genes, none with an alert): [[TIPARP]] 1.35× (z +3.5, 24/47 lines), [[MIR181A1HG]] 1.23× (z +3.0, 18/41 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (15 genes, none with an alert; 12 shown): [[ZNF641]] 0.714× (z -4.0, 9/38 lines), [[ZNF557]] 0.774× (z -3.9, 15/44 lines), [[MYO1C]] 0.828× (z -3.6, 14/47 lines), [[ZBED6]] 0.538× (z -3.6, 15/38 lines), [[PLEKHH2]] 0.825× (z -3.5, 7/31 lines), [[NAA40]] 0.796× (z -3.4, 17/45 lines), [[ABCA2]] 0.743× (z -3.3, 18/42 lines), [[C3orf62]] 0.767× (z -3.3, 7/39 lines), [[IFT140]] 0.813× (z -3.2, 13/47 lines), [[ACSF2]] 0.817× (z -3.1, 11/44 lines), [[PRR14L]] 0.831× (z -3.0, 18/47 lines), [[TNFRSF14]] 0.716× (z -3.0, 8/28 lines)

**0.5 µM** (19 genes, none with an alert; 12 shown): [[MLST8]] 0.625× (z -4.3, 19/46 lines), [[SCD]] 0.762× (z -3.9, 39/47 lines), [[GNAL]] 0.810× (z -3.8, 5/41 lines), [[RARG]] 0.789× (z -3.7, 6/43 lines), [[PUF60]] 0.760× (z -3.6, 15/47 lines), [[PLSCR3]] 0.725× (z -3.4, 14/44 lines), [[PCSK1N]] 0.559× (z -3.3, 11/23 lines), [[GALE]] 0.759× (z -3.2, 13/45 lines), [[ECM1]] 0.751× (z -3.1, 8/26 lines), [[FAM43A]] 0.685× (z -3.1, 6/32 lines), [[PCOLCE]] 0.747× (z -3.1, 10/38 lines), [[RGS19]] 0.718× (z -3.1, 8/40 lines)

**5 µM** (3 genes, none with an alert): [[DNAJA4]] 0.734× (z -4.3, 3/25 lines), [[B3GALT5]] 0.731× (z -3.5, 4/20 lines), [[PGM5P2-1]] 0.771× (z -3.4, 6/34 lines)

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
| 0.05 µM | [[C32 (line)]] (-3.5) | [[SW 1271 (line)]] (1.69), [[CHP-212 (line)]] (1.56), [[AN3 CA (line)]] (1.46), [[HepG2_C3A (line)]] (1.44) · weakest: [[SW480 (line)]] (0.328), [[NCI-H2347 (line)]] (0.438), [[LOX-IMVI (line)]] (0.440) |
| 0.5 µM | [[HOP62 (line)]] (-3.4) | [[SW 1271 (line)]] (1.80), [[SNU-423 (line)]] (1.69), [[MIA PaCa-2 (line)]] (1.66), [[SW48 (line)]] (1.40) · weakest: [[HT-29 (line)]] (0.180), [[HepG2_C3A (line)]] (0.472), [[RPMI-7951 (line)]] (0.515) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Dorzolamide (hydrochloride) (drug)]] (+0.80, unclear); [[Flutamide (drug)]] (+0.79, Androgen receptor antagonist); [[Imiquimod (hydrochloride) (drug)]] (+0.74, unclear, ⚠ vector dose flagged: toxic); [[Elagolix sodium (drug)]] (+0.72, unclear); [[Torkinib (drug)]] (+0.68, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[Bendamustine (drug)]] (+0.67, DNA synthesis/repair inhibitor); [[Clofarabine (drug)]] (+0.67, DNA synthesis/repair inhibitor, ⚠ only 8 significant genes); [[Canagliflozin (hemihydrate) (drug)]] (+0.66, Glucose transporter inhibitor); [[Bicalutamide (drug)]] (+0.65, Androgen receptor antagonist); [[Docetaxel (Trihydrate) (drug)]] (+0.60, Microtubule inhibitor); [[Saquinavir (drug)]] (+0.59, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 15 arrows, 15 of them with an alert ⚠; grade A 0, B 10, C 5.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[BMPER]] | 0.05 µM | B | BMPER activity lowers the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.05 µM (makes them more sensitive) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 1.10× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[NRIR]] | 0.5 µM | B | NRIR activity raises the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.5 µM (protects the cells) | lines that do not express NRIR (14) vs lines expressing it (34) | the lines without NRIR: 0.93× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[ODF3B]] | 0.05 µM | B | ODF3B activity raises the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.05 µM (protects the cells) | lines that do not express ODF3B (13) vs lines expressing it (35) | the lines without ODF3B: 0.86× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[RPP25]] | 0.05 µM | B | RPP25 activity raises the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.05 µM (protects the cells) | lines that do not express RPP25 (14) vs lines expressing it (34) | the lines without RPP25: 0.86× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, ODF3B, EPHA10 |
| [[INPP4B]] | 0.05 µM | B | INPP4B activity raises the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.05 µM (protects the cells) | lines that do not express INPP4B (10) vs lines expressing it (38) | the lines without INPP4B: 0.85× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[MEG3]] | 0.5 µM | B | MEG3 activity lowers the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.5 µM (makes them more sensitive) | lines that do not express MEG3 (35) vs lines expressing it (13) | the lines without MEG3: 1.21× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8 |
| [[HENMT1]] | 0.05 µM | B | HENMT1 activity raises the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.05 µM (protects the cells) | lines that do not express HENMT1 (17) vs lines expressing it (31) | the lines without HENMT1: 0.87× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: SLC16A5, RPP25, ENSG00000267748 |
| [[MIR493HG]] | 0.5 µM | B | MIR493HG activity lowers the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.5 µM (makes them more sensitive) | lines that do not express MIR493HG (36) vs lines expressing it (12) | the lines without MIR493HG: 1.23× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252 |
| [[MTMR7]] | 0.05 µM | B | MTMR7 activity lowers the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.05 µM (makes them more sensitive) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 1.13× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| [[SPOCK1]] | 0.05 µM | B | SPOCK1 activity lowers the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.05 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.06× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[PWWP2B]] | 0.5 µM | C | PWWP2B activity raises the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.5 µM (protects the cells) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 0.68× the cells of the other lines | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| [[FIGN]] | 0.5 µM | C | FIGN activity lowers the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.18× the cells of the other lines | 0.033 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[ENSG00000274213]] | 0.05 µM | C | ENSG00000274213 activity raises the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.05 µM (protects the cells) | lines that do not express ENSG00000274213 (3) vs lines expressing it (45) | the lines without ENSG00000274213: 0.78× the cells of the other lines | 0.070 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF19, ARHGEF28; maybe low, not absent |
| [[SPART-AS1]] | 0.5 µM | C | SPART-AS1 activity lowers the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.16× the cells of the other lines | 0.082 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[LINC02068]] | 0.05 µM | C | LINC02068 activity raises the cells' numbers under Dapagliflozin ((2S)-1,2-propanediol, hydrate) 0.05 µM (protects the cells) | lines that do not express LINC02068 (3) vs lines expressing it (45) | the lines without LINC02068: 0.79× the cells of the other lines | 0.095 | ⚠ few lines (3 vs 47); across organs; also absent: TRIB3; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Dapagliflozin ((2S)-1,2-propanediol, hydrate)"
- `tables/drugdoses.parquet` — dd in 323, 324, 325
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
