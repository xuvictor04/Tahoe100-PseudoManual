---
drug: "Fenofibrate"
type: "drug"
salt_base: "Fenofibrate"
targets: "CYP2C19, CYP2B6, CYP2C9, CYP2C8, CYP3A4, PPARA"
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 131
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Fenofibrate

*unclear (unclear) · targets: CYP2C19, CYP2B6, CYP2C9, CYP2C8, CYP3A4, PPARA · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 131 / 0 / 2; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.52 / 0.47.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:C5 | 6 / 125 | — | +0.82 | -0.8/-1.4/-1.3 | — |
| 0.5 µM | [[Plate 08]]:C5 | 0 / 0 | — | -0.22 | -0.8/-1.1/-0.5 | — |
| 5 µM | [[Plate 09]]:C5 | 1 / 1 | — | -0.08 | -0.5/-0.4/-0.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (6 genes, none with an alert): [[CAPRIN1]] 1.24× (z +3.2, 32/48 lines), [[ENSG00000291003]] 1.34× (z +3.2, 1/46 lines), [[KAT7]] 1.26× (z +3.0, 13/48 lines), [[PANK3]] 1.21× (z +2.9, 15/48 lines), [[RAB23]] 1.20× (z +2.8, 1/45 lines), [[FARSB]] 1.24× (z +2.8, 5/48 lines)

**5 µM** (1 gene, none with an alert): [[SLC25A20]] 1.30× (z +3.1, 2/40 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (125 genes, none with an alert; 12 shown): [[NTRK3]] 0.497× (z -4.7, 4/13 lines), [[FSTL5]] 0.690× (z -4.7, 0/13 lines), [[LGALS4]] 0.589× (z -4.4, 1/9 lines), [[ZNF667-AS1]] 0.578× (z -4.4, 0/13 lines), [[NPNT]] 0.695× (z -4.3, 0/15 lines), [[PTPRN]] 0.567× (z -4.3, 1/16 lines), [[KMO]] 0.527× (z -4.2, 4/26 lines), [[KCNE3]] 0.443× (z -4.1, 2/11 lines), [[DDX43]] 0.639× (z -4.1, 1/14 lines), [[EPGN]] 0.525× (z -4.1, 2/7 lines), [[SPTSSB]] 0.493× (z -4.0, 0/11 lines), [[DDIT4L]] 0.469× (z -4.0, 1/15 lines)

**5 µM** (1 gene, none with an alert): [[TRPC4]] 0.744× (z -3.3, 2/16 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 025]] (+2.5), [[Module 020]] (+2.4), [[Module 029]] (+2.3) | [[Module 059]] (-2.6), [[Module 024]] (-2.5), [[Module 048]] (-2.3) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[AN3 CA (line)]] (1.60), [[HCT15 (line)]] (1.36), [[RKO (line)]] (1.27), [[SNU-1 (line)]] (1.27) · weakest: [[NCI-H2347 (line)]] (0.648), [[SW 1088 (line)]] (0.733), [[hTERT-HPNE (line)]] (0.744) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Erlotinib (drug)]] (+0.95, EGFR/ERBB inhibitor); [[Lucanthone (drug)]] (+0.90, unclear); [[Benproperine (phosphate) (drug)]] (+0.90, unclear); [[Rutin (trihydrate) (drug)]] (+0.82, unclear); [[MK-8353 (drug)]] (+0.80, Other MAPK inhibitor); [[Tucatinib (drug)]] (+0.79, EGFR/ERBB inhibitor); [[Paclitaxel (drug)]] (+0.78, Microtubule inhibitor, ⚠ only 3 significant genes); [[Anethole trithione (drug)]] (+0.77, unclear); [[Encorafenib (drug)]] (+0.75, RAF inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 15 arrows, 15 of them with an alert ⚠; grade A 0, B 9, C 6.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[FMNL1-DT]] | 0.05 µM | B | FMNL1-DT activity lowers the cells' numbers under Fenofibrate 0.05 µM (makes them more sensitive) | lines that do not express FMNL1-DT (23) vs lines expressing it (25) | the lines without FMNL1-DT: 1.29× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent |
| [[NLGN4X]] | 0.05 µM | B | NLGN4X activity raises the cells' numbers under Fenofibrate 0.05 µM (protects the cells) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 0.94× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| [[KLRC4-KLRK1]], [[KLRK1]] | 0.05 µM | B | KLRC4-KLRK1, KLRK1 activity raises the cells' numbers under Fenofibrate 0.05 µM (protects the cells) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 0.81× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| [[ENSG00000225751]] | 0.05 µM | B | ENSG00000225751 activity lowers the cells' numbers under Fenofibrate 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000225751 (14) vs lines expressing it (34) | the lines without ENSG00000225751: 1.26× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: SLFN5, MMRN2, MGLL |
| [[ANKRD33B]] | 0.05 µM | B | ANKRD33B activity lowers the cells' numbers under Fenofibrate 0.05 µM (makes them more sensitive) | lines that do not express ANKRD33B (15) vs lines expressing it (33) | the lines without ANKRD33B: 1.30× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |
| [[KLRC3]] | 0.05 µM | B | KLRC3 activity raises the cells' numbers under Fenofibrate 0.05 µM (protects the cells) | lines that do not express KLRC3 (27) vs lines expressing it (21) | the lines without KLRC3: 0.83× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| [[SLFN5]] | 0.05 µM | B | SLFN5 activity lowers the cells' numbers under Fenofibrate 0.05 µM (makes them more sensitive) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 1.30× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[GLIS3]] | 0.05 µM | B | GLIS3 activity lowers the cells' numbers under Fenofibrate 0.05 µM (makes them more sensitive) | lines that do not express GLIS3 (21) vs lines expressing it (27) | the lines without GLIS3: 1.26× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO |
| [[GJC1]] | 0.05 µM | B | GJC1 activity lowers the cells' numbers under Fenofibrate 0.05 µM (makes them more sensitive) | lines that do not express GJC1 (13) vs lines expressing it (35) | the lines without GJC1: 1.30× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB |
| [[C2orf74]] | 0.05 µM | C | C2orf74 activity lowers the cells' numbers under Fenofibrate 0.05 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.29× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[FIGN]] | 0.05 µM | C | FIGN activity lowers the cells' numbers under Fenofibrate 0.05 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.25× the cells of the other lines | 0.012 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[SPART-AS1]] | 0.05 µM | C | SPART-AS1 activity lowers the cells' numbers under Fenofibrate 0.05 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.22× the cells of the other lines | 0.031 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[NR3C1]] | 0.05 µM | C | NR3C1 activity lowers the cells' numbers under Fenofibrate 0.05 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.28× the cells of the other lines | 0.038 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[ENSG00000214265]], [[SNHG14]], [[SNRPN]] | 0.05 µM | C | ENSG00000214265, SNHG14, SNRPN activity lowers the cells' numbers under Fenofibrate 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.21× the cells of the other lines | 0.079 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| [[RNF150]] | 0.05 µM | C | RNF150 activity lowers the cells' numbers under Fenofibrate 0.05 µM (makes them more sensitive) | lines that do not express RNF150 (16) vs lines expressing it (32) | the lines without RNF150: 1.21× the cells of the other lines | 0.091 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SNRPN, BVES, MPDZ |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Fenofibrate"
- `tables/drugdoses.parquet` — dd in 441, 442, 443
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
