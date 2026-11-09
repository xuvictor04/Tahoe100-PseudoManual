---
drug: "Hydroxyfasudil"
type: "drug"
salt_base: "Hydroxyfasudil"
targets: "ROCK1, ROCK2, PRKACA"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 51
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Hydroxyfasudil

*unclear (inhibitor/antagonist) · targets: ROCK1, ROCK2, PRKACA · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 51 / 11 / 1; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): -0.34 / 0.42.
> Flags by dose: unreliable plate only / noisy plate (z scaled) / noisy plate (z scaled). ⚠ 0.05 µM: unreliable plate only (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 13]]:A6 | 29 / 22 | — | +0.57 | -2.7/-1.9/-2.5 | ⚠ unreliable plate only |
| 0.5 µM | [[Plate 02]]:F2 | 11 / 0 | — | -0.72 | +0.0/+0.3/+1.6 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:F2 | 1 / 0 | — | -0.77 | -0.9/-0.9/-0.3 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (29 genes, 29 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[WASHC2A]] ⚠ 1.24× (z +4.6, 14/48 lines), [[HSPBAP1]] ⚠ 1.33× (z +4.4, 13/47 lines), [[GULP1]] ⚠ 1.22× (z +4.2, 17/44 lines), [[HS1BP3]] ⚠ 1.31× (z +4.0, 8/48 lines), [[HDAC9]] ⚠ 1.23× (z +3.9, 17/39 lines), [[SLC49A4]] ⚠ 1.23× (z +3.8, 15/48 lines), [[ARHGEF28]] ⚠ 1.26× (z +3.7, 20/42 lines), [[SCMH1]] ⚠ 1.21× (z +3.7, 16/48 lines), [[ING4]] ⚠ 1.22× (z +3.7, 6/48 lines), [[VPS13C]] ⚠ 1.22× (z +3.6, 25/48 lines), [[VAC14]] ⚠ 1.20× (z +3.4, 14/48 lines), [[NAV2]] ⚠ 1.22× (z +3.4, 14/31 lines)

**0.5 µM** (11 genes, none with an alert): [[HSPA1A]] 4.71× (z +6.1, 30/35 lines), [[HSPA1B]] 2.43× (z +5.6, 37/48 lines), [[BAG3]] 1.50× (z +5.1, 28/49 lines), [[ENSG00000285565]] 2.87× (z +4.9, 12/41 lines), [[DNAJB1]] 1.91× (z +4.2, 30/49 lines), [[DNAJA4]] 1.44× (z +3.8, 7/25 lines), [[HSPH1]] 1.59× (z +3.4, 28/49 lines), [[DYNC1I1]] 1.41× (z +3.1, 3/31 lines), [[CRYAB]] 3.02× (z +3.0, 1/13 lines), [[MIX23]] 1.34× (z +3.0, 6/48 lines), [[HSP90AA1]] 1.63× (z +2.8, 24/49 lines)

**5 µM** (1 gene, none with an alert): [[ROR2]] 1.35× (z +2.7, 0/18 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (22 genes, 22 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[EHF]] ⚠ 0.795× (z -4.0, 1/21 lines), [[LCK]] ⚠ 0.610× (z -3.5, 1/14 lines), [[SCD]] ⚠ 0.790× (z -3.4, 25/48 lines), [[RNF128]] ⚠ 0.833× (z -3.4, 2/25 lines), [[LINC03040]] ⚠ 0.645× (z -3.3, 3/16 lines), [[FDPS]] ⚠ 0.769× (z -3.3, 23/48 lines), [[POLR3G]] ⚠ 0.824× (z -3.2, 8/45 lines), [[RPN2]] ⚠ 0.830× (z -3.2, 19/48 lines), [[LINC02864]] ⚠ 0.780× (z -3.2, 0/12 lines), [[FDFT1]] ⚠ 0.797× (z -3.2, 18/47 lines), [[P2RY2]] ⚠ 0.701× (z -3.1, 5/21 lines), [[MCM10]] ⚠ 0.763× (z -3.1, 9/43 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 230]] (+2.1) | — |
| 0.5 µM | [[Module 060]] (+2.2) | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[KATO III (line)]] (1.97), [[RPMI-7951 (line)]] (1.68), [[SW 900 (line)]] (1.48), [[Hs 766T (line)]] (1.45) · weakest: [[J82 (line)]] (0.586), [[HT-29 (line)]] (0.610), [[SHP-77 (line)]] (0.610) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Bendamustine (drug)]] (+0.68, DNA synthesis/repair inhibitor); [[AZD2858 (drug)]] (+0.67, GSK3 inhibitor, ⚠ vector dose flagged: toxic); [[XRK3F2 (drug)]] (+0.67, unclear); [[Canagliflozin (hemihydrate) (drug)]] (+0.65, Glucose transporter inhibitor); [[9-ING-41 (drug)]] (+0.62, GSK3 inhibitor); [[Bicalutamide (drug)]] (+0.62, Androgen receptor antagonist); [[olaparib (drug)]] (+0.61, DNA synthesis/repair inhibitor, ⚠ only 3 significant genes); [[BI-78D3 (drug)]] (+0.61, Other MAPK inhibitor); [[AZD-7648 (drug)]] (+0.59, DNA synthesis/repair inhibitor); [[Entrectinib (drug)]] (+0.59, Other TK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[FTH1]] | 5 µM | C | FTH1 activity lowers the cells' numbers under Hydroxyfasudil 5 µM (makes them more sensitive) | lines that do not express FTH1 (4) vs lines expressing it (44) | the lines without FTH1: 1.34× the cells of the other lines | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000284716, ZFP36, DDR1; maybe low, not absent |
| [[DDR1]] | 5 µM | C | DDR1 activity lowers the cells' numbers under Hydroxyfasudil 5 µM (makes them more sensitive) | lines that do not express DDR1 (3) vs lines expressing it (45) | the lines without DDR1: 1.36× the cells of the other lines | 0.023 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD3; also absent: FTH1, LINC00847, IER3; maybe low, not absent |
| [[PLS3]] | 5 µM | C | PLS3 activity lowers the cells' numbers under Hydroxyfasudil 5 µM (makes them more sensitive) | lines that do not express PLS3 (4) vs lines expressing it (44) | the lines without PLS3: 1.28× the cells of the other lines | 0.026 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent |
| [[ENSG00000284716]] | 5 µM | C | ENSG00000284716 activity lowers the cells' numbers under Hydroxyfasudil 5 µM (makes them more sensitive) | lines that do not express ENSG00000284716 (5) vs lines expressing it (43) | the lines without ENSG00000284716: 1.29× the cells of the other lines | 0.036 | ⚠ tissue-confounded; across organs; also absent: FTH1, TMEM184A, ZFP36; maybe low, not absent |
| [[HBEGF]] | 5 µM | C | HBEGF activity lowers the cells' numbers under Hydroxyfasudil 5 µM (makes them more sensitive) | lines that do not express HBEGF (3) vs lines expressing it (45) | the lines without HBEGF: 1.35× the cells of the other lines | 0.037 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, TRAF3IP2; maybe low, not absent |
| [[ZFP36]] | 5 µM | C | ZFP36 activity lowers the cells' numbers under Hydroxyfasudil 5 µM (makes them more sensitive) | lines that do not express ZFP36 (3) vs lines expressing it (45) | the lines without ZFP36: 1.35× the cells of the other lines | 0.039 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: FTH1, CDC42EP1, ENSG00000284716 |
| [[ENSG00000287264]] | 5 µM | C | ENSG00000287264 activity lowers the cells' numbers under Hydroxyfasudil 5 µM (makes them more sensitive) | lines that do not express ENSG00000287264 (3) vs lines expressing it (45) | the lines without ENSG00000287264: 1.30× the cells of the other lines | 0.052 | ⚠ few lines (3 vs 47); across organs; also absent: PLEKHG5, MYH16, PER3; maybe low, not absent |
| [[LTBP3]] | 5 µM | C | LTBP3 activity lowers the cells' numbers under Hydroxyfasudil 5 µM (makes them more sensitive) | lines that do not express LTBP3 (4) vs lines expressing it (44) | the lines without LTBP3: 1.25× the cells of the other lines | 0.071 | ⚠ few lines (4 vs 46); across organs; also absent: DBN1, NUAK1, BLVRA; maybe low, not absent |
| [[RARG]] | 5 µM | C | RARG activity lowers the cells' numbers under Hydroxyfasudil 5 µM (makes them more sensitive) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 1.30× the cells of the other lines | 0.093 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Hydroxyfasudil"
- `tables/drugdoses.parquet` — dd in 531, 532, 533
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
