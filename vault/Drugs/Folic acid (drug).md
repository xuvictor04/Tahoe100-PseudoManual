---
drug: "Folic acid"
type: "drug"
salt_base: "Folic acid"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 45
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Folic acid

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 0 / 45; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.40 / 0.50.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:H2 | 0 / 0 | — | +0.18 | -0.5/-0.7/-0.7 | — |
| 0.5 µM | [[Plate 05]]:H2 | 0 / 0 | — | +0.89 | +0.9/+0.8/+0.2 | — |
| 5 µM | [[Plate 14]]:H2 | 18 / 27 | 0.843 | -0.23 | -0.1/-0.4/-0.9 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (18 genes, none with an alert; 12 shown): [[DPYSL4]] 1.37× (z +4.1, 8/24 lines), [[ALG10B]] 1.27× (z +3.8, 12/46 lines), [[ENSG00000266953]] 1.41× (z +3.8, 13/47 lines), [[FAM106A]] 1.25× (z +3.7, 2/17 lines), [[SYNGAP1]] 1.21× (z +3.6, 9/48 lines), [[ZXDB]] 1.26× (z +3.6, 8/47 lines), [[POLR2J3]] 1.27× (z +3.5, 7/48 lines), [[ENSG00000272410]] 1.42× (z +3.5, 3/46 lines), [[CELSR3]] 1.32× (z +3.4, 7/46 lines), [[ENPP3]] 1.33× (z +3.3, 0/34 lines), [[CRYZL2P]] 1.26× (z +3.2, 3/34 lines), [[TRDMT1]] 1.20× (z +3.2, 3/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (27 genes, none with an alert; 12 shown): [[THAP1]] 0.770× (z -4.8, 23/48 lines), [[FOXC1]] 0.729× (z -4.4, 28/44 lines), [[SLU7]] 0.829× (z -4.0, 25/48 lines), [[TMEM14C]] 0.774× (z -3.9, 28/48 lines), [[ALDH2]] 0.829× (z -3.9, 12/39 lines), [[HOTAIRM1]] 0.696× (z -3.9, 20/34 lines), [[TPT1]] 0.706× (z -3.8, 48/48 lines), [[AREG]] 0.728× (z -3.7, 17/22 lines), [[EPCAM]] 0.803× (z -3.7, 12/20 lines), [[NIFK]] 0.759× (z -3.7, 29/48 lines), [[DDX27]] 0.820× (z -3.6, 22/48 lines), [[FAM98C]] 0.784× (z -3.6, 12/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 020]] (+2.3), [[Module 179]] (+2.2), [[Module 025]] (+2.1) | [[Module 048]] (-2.6), [[Module 043]] (-2.6), [[Module 131]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Hs 766T (line)]] (1.28), [[SW 1271 (line)]] (1.25), [[HT-29 (line)]] (1.19), [[MIA PaCa-2 (line)]] (1.16) · weakest: [[SW 1088 (line)]] (0.477), [[A-427 (line)]] (0.701), [[HCT15 (line)]] (0.715) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 5 next most similar without an alert.*

- [[Clonidine (hydrochloride) (drug)]] (+0.76, Adrenoceptor agonist, ⚠ only 4 significant genes); [[Adenine (drug)]] (+0.75, unclear); [[Pyridoxine (hydrochloride) (drug)]] (+0.75, unclear); [[Balsalazide (sodium hydrate) (drug)]] (+0.73, JAK/STAT inhibitor, ⚠ only 9 significant genes); [[Temuterkib (drug)]] (+0.69, Other MAPK inhibitor, ⚠ only 3 significant genes); [[Volasertib (drug)]] (+0.67, unclear); [[Trifluridine (drug)]] (+0.62, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Pentagastrin (drug)]] (+0.61, unclear, ⚠ only 9 significant genes); [[MK-8353 (drug)]] (+0.60, Other MAPK inhibitor); [[Fluvoxamine (drug)]] (+0.60, unclear); [[8-Hydroxyquinoline (drug)]] (+0.59, unclear); [[Pentoxifylline (drug)]] (+0.58, unclear); [[Berberine (chloride hydrate) (drug)]] (+0.57, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[NR3C1]] | 5 µM | C | NR3C1 activity lowers the cells' numbers under Folic acid 5 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.13× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[C2orf74]] | 5 µM | C | C2orf74 activity lowers the cells' numbers under Folic acid 5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.12× the cells of the other lines | 0.022 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[ENSG00000286964]] | 5 µM | C | ENSG00000286964 activity lowers the cells' numbers under Folic acid 5 µM (makes them more sensitive) | lines that do not express ENSG00000286964 (10) vs lines expressing it (38) | the lines without ENSG00000286964: 1.12× the cells of the other lines | 0.030 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SIX1, C2orf74, SYDE1 |
| [[FIGN]] | 5 µM | C | FIGN activity lowers the cells' numbers under Folic acid 5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.10× the cells of the other lines | 0.033 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[ENSG00000268163]] | 5 µM | C | ENSG00000268163 activity lowers the cells' numbers under Folic acid 5 µM (makes them more sensitive) | lines that do not express ENSG00000268163 (12) vs lines expressing it (36) | the lines without ENSG00000268163: 1.11× the cells of the other lines | 0.047 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: ZNF772, SNRPN, DNAAF9; maybe low, not absent |
| [[SPAG16]] | 5 µM | C | SPAG16 activity lowers the cells' numbers under Folic acid 5 µM (makes them more sensitive) | lines that do not express SPAG16 (6) vs lines expressing it (42) | the lines without SPAG16: 1.15× the cells of the other lines | 0.049 | ⚠ tissue-confounded; across organs; co-occurs with WNK2, BRCA2; also absent: ZNF140, LUCAT1, GCA |
| [[ENSG00000214265]], [[SNHG14]], [[SNRPN]] | 5 µM | C | ENSG00000214265, SNHG14, SNRPN activity lowers the cells' numbers under Folic acid 5 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.10× the cells of the other lines | 0.049 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| [[PLEKHN1]] | 5 µM | C | PLEKHN1 activity lowers the cells' numbers under Folic acid 5 µM (makes them more sensitive) | lines that do not express PLEKHN1 (3) vs lines expressing it (45) | the lines without PLEKHN1: 1.19× the cells of the other lines | 0.083 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |
| [[PAXIP1-AS2]] | 5 µM | C | PAXIP1-AS2's natural level lowers the cells' numbers under Folic acid 5 µM (makes them more sensitive) | PAXIP1-AS2's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.285 over the table, 0.059 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[FBF1]] | 5 µM | C | FBF1's natural level lowers the cells' numbers under Folic acid 5 µM (makes them more sensitive) | FBF1's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.308 over the table, 0.059 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Folic acid"
- `tables/drugdoses.parquet` — dd in 468, 469, 470
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
