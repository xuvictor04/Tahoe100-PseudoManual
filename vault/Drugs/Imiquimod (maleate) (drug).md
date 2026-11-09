---
drug: "Imiquimod (maleate)"
type: "drug"
salt_base: "Imiquimod"
targets: "TLR7"
moa_fine: "unclear"
moa_broad: "activator/agonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 24
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Imiquimod (maleate)

*unclear (activator/agonist) · targets: TLR7 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 14 / 24 / 8; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): -0.18 / 0.16.
> Flags by dose: - / low cells (technical?) / -.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:G7 | 12 / 2 | — | -0.45 | +0.6/+0.3/+1.0 | — |
| 0.5 µM | [[Plate 08]]:G7 | 23 / 1 | — | -1.30 | -0.2/-0.9/-0.5 | low cells (technical?) |
| 5 µM | [[Plate 09]]:G7 | 7 / 1 | — | -0.79 | -0.5/+0.3/+0.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (12 genes, none with an alert): [[DSG2]] 1.27× (z +3.6, 29/37 lines), [[C11orf68]] 1.39× (z +3.4, 1/38 lines), [[LRATD2]] 1.24× (z +3.3, 5/31 lines), [[RPL39L]] 1.37× (z +3.3, 6/29 lines), [[SLC2A9]] 1.44× (z +3.2, 7/38 lines), [[ENSG00000291159]] 1.32× (z +3.2, 3/37 lines), [[VPS28]] 1.38× (z +3.2, 9/45 lines), [[TOR3A]] 1.26× (z +2.9, 6/44 lines), [[SLC25A39]] 1.32× (z +2.9, 16/47 lines), [[SLC2A8]] 1.27× (z +2.9, 6/38 lines), [[GINS3]] 1.27× (z +2.9, 1/41 lines), [[PDIK1L]] 1.21× (z +2.9, 3/45 lines)

**0.5 µM** (23 genes, none with an alert; 12 shown): [[PLPP4]] 1.51× (z +3.6, 2/16 lines), [[ESRP2]] 1.39× (z +3.6, 0/22 lines), [[ENSG00000249803]] 1.58× (z +3.6, 0/11 lines), [[NPIPB12]] 1.43× (z +3.5, 3/31 lines), [[ENSG00000269547]] 1.54× (z +3.4, 4/17 lines), [[TBX20]] 1.40× (z +3.4, 0/15 lines), [[ATP7B]] 1.23× (z +3.4, 6/45 lines), [[ANKRD20A9P]] 1.61× (z +3.4, 0/8 lines), [[CNTN4]] 1.34× (z +3.4, 4/41 lines), [[SNN]] 1.38× (z +3.4, 3/40 lines), [[ZNF667]] 1.46× (z +3.4, 0/12 lines), [[C1orf226]] 1.40× (z +3.3, 2/29 lines)

**5 µM** (7 genes, none with an alert): [[EDA2R]] 1.52× (z +4.2, 0/18 lines), [[ZNF439]] 1.30× (z +3.4, 2/25 lines), [[PEX1]] 1.24× (z +3.2, 12/47 lines), [[ARNT2-DT]] 1.57× (z +3.2, 1/13 lines), [[WDR72]] 1.31× (z +3.1, 2/16 lines), [[ENSG00000236924]] 1.26× (z +3.1, 1/29 lines), [[PLEKHS1]] 1.48× (z +3.0, 0/15 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[ISY1-RAB43]] 0.692× (z -3.5, 9/40 lines), [[MTERF3]] 0.805× (z -3.4, 12/47 lines)

**0.5 µM** (1 gene, none with an alert): [[XKR8]] 0.720× (z -3.4, 6/34 lines)

**5 µM** (1 gene, none with an alert): [[THBS3]] 0.771× (z -2.8, 11/43 lines)

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
| 0.05 µM | — | — |
| 0.5 µM | [[HOP62 (line)]] (-4.3) | [[SW48 (line)]] (1.84), [[NCI-H661 (line)]] (1.61), [[AN3 CA (line)]] (1.57), [[AsPC-1 (line)]] (1.41) · weakest: [[A-427 (line)]] (-0.476), [[SHP-77 (line)]] (-0.0529), [[LoVo (line)]] (0.0878) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Ferulic acid (drug)]] (+0.66, Other TK inhibitor); [[Docetaxel (drug)]] (+0.61, Microtubule inhibitor, ⚠ vector dose flagged: transcription drop; cell-cycle shift); [[Lonafarnib (drug)]] (+0.56, RAS inhibitor, ⚠ vector dose flagged: toxic); [[Dinaciclib (drug)]] (+0.55, CDK inhibitor, ⚠ vector dose flagged: toxic; transcription drop; cell-cycle shift); [[Glycyrrhizic acid (drug)]] (+0.53, unclear); [[Lidocaine (hydrochloride) (drug)]] (+0.51, unclear); [[Riluzole hydrochloride (drug)]] (+0.50, unclear); [[Orlistat (drug)]] (+0.50, unclear); [[Bestatin (hydrochloride) (drug)]] (+0.48, unclear); [[Tadalafil (drug)]] (+0.47, unclear); [[Pemetrexed (drug)]] (+0.47, DNA synthesis/repair inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[KCNMA1]] | 0.5 µM | B | KCNMA1 activity lowers the cells' numbers under Imiquimod (maleate) 0.5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.25× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[MYH14]] | 0.5 µM | B | MYH14 activity raises the cells' numbers under Imiquimod (maleate) 0.5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.80× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[PWWP2B]] | 0.5 µM | C | PWWP2B activity raises the cells' numbers under Imiquimod (maleate) 0.5 µM (protects the cells) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 0.60× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| [[RAB11FIP1]] | 0.5 µM | C | RAB11FIP1 activity raises the cells' numbers under Imiquimod (maleate) 0.5 µM (protects the cells) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 0.70× the cells of the other lines | 0.051 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |
| [[FIGN]] | 0.5 µM | C | FIGN activity lowers the cells' numbers under Imiquimod (maleate) 0.5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.19× the cells of the other lines | 0.072 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Imiquimod (maleate)"
- `tables/drugdoses.parquet` — dd in 549, 550, 551
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
