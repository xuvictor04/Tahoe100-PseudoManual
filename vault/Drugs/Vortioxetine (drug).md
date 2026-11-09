---
drug: "Vortioxetine"
type: "drug"
salt_base: "Vortioxetine"
targets: "SLC6A4, HTR3A, HTR7"
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 37
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Vortioxetine

*unclear (unclear) · targets: SLC6A4, HTR3A, HTR7 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 20 / 37; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.47 / -0.01.
> Flags by dose: - / - / toxic. ⚠ 5 µM: toxic (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:B8 | 2 / 1 | — | +0.01 | -0.4/+0.1/+0.5 | — |
| 0.5 µM | [[Plate 11]]:B8 | 6 / 14 | — | +0.55 | -2.5/-1.0/-1.6 | — |
| 5 µM | [[Plate 12]]:B8 | 35 / 2 | — | -1.29 | -1.3/-0.5/+0.9 | ⚠ toxic |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[ENSG00000230021]] 1.28× (z +3.0, 17/48 lines), [[RBPMS2]] 1.30× (z +3.0, 0/33 lines)

**0.5 µM** (6 genes, none with an alert): [[PIGC]] 1.31× (z +3.7, 13/48 lines), [[NADK2]] 1.24× (z +3.6, 12/48 lines), [[ZNF550]] 1.27× (z +3.3, 4/42 lines), [[BDH1]] 1.23× (z +3.3, 5/36 lines), [[APTR]] 1.24× (z +3.2, 10/48 lines), [[PCTP]] 1.22× (z +3.1, 3/47 lines)

**5 µM** (35 genes, 35 with an alert ⚠; the drug-dose carries ⚠ toxic; 12 shown): [[ACKR3]] ⚠ 1.77× (z +4.3, 2/14 lines), [[ANOS2P]] ⚠ 1.72× (z +4.1, 0/11 lines), [[MEOX2]] ⚠ 1.80× (z +4.0, 1/7 lines), [[ENSG00000241168]] ⚠ 1.76× (z +3.6, 0/3 lines), [[PCSK2]] ⚠ 1.73× (z +3.6, 0/11 lines), [[MVK]] ⚠ 1.30× (z +3.6, 10/45 lines), [[CXCL10]] ⚠ 2.11× (z +3.6, 4/16 lines), [[LINC02967]] ⚠ 1.81× (z +3.5, 0/12 lines), [[TTC22]] ⚠ 1.61× (z +3.5, 0/15 lines), [[HBG2]] ⚠ 1.47× (z +3.4, 0/17 lines), [[AK4P3]] ⚠ 1.43× (z +3.4, 0/11 lines), [[SOD3]] ⚠ 1.98× (z +3.3, 0/9 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ENSG00000258378]] 0.683× (z -3.2, 11/44 lines)

**0.5 µM** (14 genes, none with an alert; 12 shown): [[FOSB]] 0.425× (z -3.8, 38/47 lines), [[KIF9]] 0.608× (z -3.6, 22/47 lines), [[DDX5]] 0.802× (z -3.6, 30/48 lines), [[SMCO2]] 0.683× (z -3.5, 3/36 lines), [[SNAI1]] 0.662× (z -3.5, 4/37 lines), [[HVCN1]] 0.680× (z -3.5, 11/42 lines), [[ANXA1]] 0.713× (z -3.4, 24/39 lines), [[MROH3P]] 0.663× (z -3.4, 2/19 lines), [[MIR493HG]] 0.518× (z -3.3, 1/11 lines), [[LINC01029]] 0.558× (z -3.3, 0/6 lines), [[MMP2]] 0.749× (z -3.1, 0/14 lines), [[IL6]] 0.639× (z -3.0, 1/16 lines)

**5 µM** (2 genes, 2 with an alert ⚠; the drug-dose carries ⚠ toxic): [[WNK2]] ⚠ 0.823× (z -3.2, 5/31 lines), [[BEND3]] ⚠ 0.770× (z -3.1, 9/44 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 170]] (+2.6) | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[SW 900 (line)]] (1.56), [[NCI-H2030 (line)]] (1.53), [[C32 (line)]] (1.47), [[HepG2_C3A (line)]] (1.47) · weakest: [[SNU-1 (line)]] (0.324), [[H4 (line)]] (0.330), [[BT-474 (line)]] (0.419) |
| 5 µM | — | [[HepG2_C3A (line)]] (1.85), [[SW 1271 (line)]] (1.78), [[AN3 CA (line)]] (1.65), [[NCI-H661 (line)]] (1.59) · weakest: [[LoVo (line)]] (0.0330), [[HT-29 (line)]] (0.162), [[SW1417 (line)]] (0.236) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: toxic. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Fingolimod (hydrochloride) (drug)]] (+0.69, unclear, ⚠ vector dose flagged: toxic); [[Almonertinib (hydrochloride) (drug)]] (+0.69, EGFR/ERBB inhibitor); [[olaparib (drug)]] (+0.62, DNA synthesis/repair inhibitor, ⚠ only 3 significant genes); [[Terfenadine (drug)]] (+0.57, unclear); [[Fluvoxamine (maleate) (drug)]] (+0.56, unclear); [[Imiquimod (hydrochloride) (drug)]] (+0.55, unclear, ⚠ vector dose flagged: toxic); [[Minodronic acid (drug)]] (+0.55, unclear); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] (+0.53, Glucose transporter inhibitor); [[Canagliflozin (hemihydrate) (drug)]] (+0.52, Glucose transporter inhibitor); [[Saquinavir (drug)]] (+0.52, unclear); [[Methylprednisolone succinate (drug)]] (+0.52, Glucocorticoid receptor agonist)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 28 arrows, 28 of them with an alert ⚠; grade A 0, B 17, C 11. Shown: the 15 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[AOX1]] | 5 µM | B | AOX1 activity lowers the cells' numbers under Vortioxetine 5 µM (makes them more sensitive) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 1.24× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[ENSG00000225751]] | 0.5 µM | B | ENSG00000225751 activity lowers the cells' numbers under Vortioxetine 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000225751 (14) vs lines expressing it (34) | the lines without ENSG00000225751: 1.20× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: SLFN5, MMRN2, MGLL |
| [[SLFN5]] | 0.5 µM | B | SLFN5 activity lowers the cells' numbers under Vortioxetine 0.5 µM (makes them more sensitive) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 1.24× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[C12orf75-AS1]] | 0.5 µM | B | C12orf75-AS1 activity lowers the cells' numbers under Vortioxetine 0.5 µM (makes them more sensitive) | lines that do not express C12orf75-AS1 (22) vs lines expressing it (26) | the lines without C12orf75-AS1: 1.21× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[NLGN4X]] | 0.5 µM | B | NLGN4X activity raises the cells' numbers under Vortioxetine 0.5 µM (protects the cells) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 0.90× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| [[FAAH2]] | 5 µM | B | FAAH2 activity raises the cells' numbers under Vortioxetine 5 µM (protects the cells) | lines that do not express FAAH2 (26) vs lines expressing it (22) | the lines without FAAH2: 0.82× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[PTGS2]] | 0.5 µM | B | PTGS2 activity lowers the cells' numbers under Vortioxetine 0.5 µM (makes them more sensitive) | lines that do not express PTGS2 (27) vs lines expressing it (21) | the lines without PTGS2: 1.20× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[SIRLNT]] | 0.5 µM | B | SIRLNT activity lowers the cells' numbers under Vortioxetine 0.5 µM (makes them more sensitive) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 1.23× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[DNAH11]] | 0.5 µM | B | DNAH11 activity lowers the cells' numbers under Vortioxetine 0.5 µM (makes them more sensitive) | lines that do not express DNAH11 (23) vs lines expressing it (25) | the lines without DNAH11: 1.20× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| [[HS6ST3]] | 5 µM | B | HS6ST3 activity lowers the cells' numbers under Vortioxetine 5 µM (makes them more sensitive) | lines that do not express HS6ST3 (19) vs lines expressing it (29) | the lines without HS6ST3: 1.17× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, NPTX1; maybe low, not absent |
| [[FOXA1]] | 5 µM | B | FOXA1 activity raises the cells' numbers under Vortioxetine 5 µM (protects the cells) | lines that do not express FOXA1 (22) vs lines expressing it (26) | the lines without FOXA1: 0.84× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: MYO5C, SPINT1, COBL |
| [[ENSG00000286329]] | 0.5 µM | B | ENSG00000286329 activity raises the cells' numbers under Vortioxetine 0.5 µM (protects the cells) | lines that do not express ENSG00000286329 (37) vs lines expressing it (11) | the lines without ENSG00000286329: 0.86× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC02050, ENSG00000242828, PASD1 |
| [[CXCL3]] | 0.5 µM | B | CXCL3 activity lowers the cells' numbers under Vortioxetine 0.5 µM (makes them more sensitive) | lines that do not express CXCL3 (14) vs lines expressing it (34) | the lines without CXCL3: 1.21× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[SERPINB7]] | 0.5 µM | B | SERPINB7 activity lowers the cells' numbers under Vortioxetine 0.5 µM (makes them more sensitive) | lines that do not express SERPINB7 (24) vs lines expressing it (24) | the lines without SERPINB7: 1.22× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7 |
| [[SPOCK1]] | 5 µM | B | SPOCK1 activity lowers the cells' numbers under Vortioxetine 5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.25× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Vortioxetine"
- `tables/drugdoses.parquet` — dd in 1102, 1103, 1104
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
