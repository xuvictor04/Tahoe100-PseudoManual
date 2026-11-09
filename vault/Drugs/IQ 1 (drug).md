---
drug: "IQ 1"
type: "drug"
salt_base: "IQ 1"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 32
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# IQ 1

*unclear (unclear) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2 / 1 / 32; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.10 / 0.44.
> Flags by dose: - / plate-row cell shift; noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:E11 | 0 / 2 | — | +0.23 | +0.2/-0.1/+0.7 | — |
| 0.5 µM | [[Plate 02]]:E11 | 0 / 1 | — | -0.85 | +0.2/+0.3/+0.4 | plate-row cell shift; noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:E11 | 12 / 20 | — | -0.51 | -2.3/-1.2/-0.6 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (12 genes, none with an alert): [[CSGALNACT1]] 1.71× (z +4.0, 12/23 lines), [[CCDC28A]] 1.43× (z +3.2, 6/45 lines), [[FAM111A-DT]] 1.77× (z +3.1, 0/19 lines), [[BDKRB2]] 1.59× (z +3.0, 2/30 lines), [[DUSP16]] 1.30× (z +3.0, 10/46 lines), [[PID1]] 1.50× (z +3.0, 5/25 lines), [[CFAP43]] 1.82× (z +3.0, 6/32 lines), [[BCAS3]] 1.37× (z +3.0, 15/48 lines), [[ERBB3]] 1.44× (z +2.8, 5/20 lines), [[LAMP3]] 1.58× (z +2.7, 1/26 lines), [[KLHL24]] 1.40× (z +2.7, 15/48 lines), [[GABARAPL1]] 1.41× (z +2.6, 9/43 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[RYR2]] 0.607× (z -4.7, 18/48 lines), [[DANT1]] 0.676× (z -3.2, 2/28 lines)

**0.5 µM** (1 gene, none with an alert): [[SLCO5A1]] 0.508× (z -7.1, 26/40 lines)

**5 µM** (20 genes, none with an alert; 12 shown): [[SLCO5A1]] 0.469× (z -5.8, 18/38 lines), [[SLC20A1]] 0.631× (z -4.2, 22/48 lines), [[LRP8]] 0.548× (z -4.0, 18/43 lines), [[GPAT3]] 0.614× (z -3.8, 15/40 lines), [[LDLR]] 0.639× (z -3.2, 17/46 lines), [[RTN4]] 0.780× (z -3.2, 20/48 lines), [[LPIN1]] 0.770× (z -3.1, 13/48 lines), [[PRAG1]] 0.785× (z -3.0, 4/32 lines), [[MYO19]] 0.783× (z -3.0, 11/48 lines), [[E2F7]] 0.697× (z -3.0, 10/42 lines), [[B4GALT6]] 0.689× (z -3.0, 10/36 lines), [[HOMER1]] 0.634× (z -2.9, 10/47 lines)

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
| 0.5 µM | — | — |
| 5 µM | [[HCT15 (line)]] (-3.2), [[LoVo (line)]] (-3.1) | [[AN3 CA (line)]] (1.58), [[SW 900 (line)]] (1.45), [[RPMI-7951 (line)]] (1.38), [[LoVo (line)]] (1.34) · weakest: [[RKO (line)]] (0.322), [[A-427 (line)]] (0.454), [[A-172 (line)]] (0.480) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Alpelisib (drug)]] (+0.76, PI3K/AKT inhibitor); [[AZD-8055 (drug)]] (+0.76, MTOR inhibitor); [[MK-3903 (drug)]] (+0.63, unclear); [[Bimiralisib (drug)]] (+0.60, PI3K/AKT inhibitor); [[Hydroxyfasudil (drug)]] (+0.58, unclear); [[Temsirolimus (drug)]] (+0.56, MTOR inhibitor); [[XRK3F2 (drug)]] (+0.55, unclear); [[AZD-7648 (drug)]] (+0.55, DNA synthesis/repair inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[CRIP1]] | 5 µM | B | CRIP1 activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express CRIP1 (27) vs lines expressing it (21) | the lines without CRIP1: 0.83× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: SPINT2, POF1B, S100P |
| [[IFNLR1]] | 5 µM | B | IFNLR1 activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express IFNLR1 (18) vs lines expressing it (30) | the lines without IFNLR1: 0.86× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |
| [[HES4]] | 5 µM | C | HES4 activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express HES4 (4) vs lines expressing it (44) | the lines without HES4: 0.71× the cells of the other lines | 0.019 | ⚠ few lines (4 vs 46); across organs; also absent: SLC26A4, ADAMTSL5 |
| [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] | 5 µM | C | ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.69× the cells of the other lines | 0.028 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| [[FZD6]] | 5 µM | C | FZD6 activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express FZD6 (5) vs lines expressing it (43) | the lines without FZD6: 0.73× the cells of the other lines | 0.028 | ⚠ tissue-confounded; across organs; also absent: DOCK5, PMAIP1, ISG20 |
| [[LMNTD2]] | 5 µM | C | LMNTD2 activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express LMNTD2 (3) vs lines expressing it (45) | the lines without LMNTD2: 0.72× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGAP27, MMP25, RBMS2; maybe low, not absent |
| [[PLEKHN1]] | 5 µM | C | PLEKHN1 activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express PLEKHN1 (3) vs lines expressing it (45) | the lines without PLEKHN1: 0.68× the cells of the other lines | 0.036 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |
| [[ANG]], [[RNASE4]] | 5 µM | C | ANG, RNASE4 activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.76× the cells of the other lines | 0.068 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| [[HOXA-AS2]] | 5 µM | C | HOXA-AS2 activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express HOXA-AS2 (3) vs lines expressing it (45) | the lines without HOXA-AS2: 0.73× the cells of the other lines | 0.075 | ⚠ few lines (3 vs 47); across organs; also absent: HFE, COTL1, ACCS; maybe low, not absent |
| [[ISG20]] | 5 µM | C | ISG20 activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 0.76× the cells of the other lines | 0.097 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "IQ 1"
- `tables/drugdoses.parquet` — dd in 537, 538, 539
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
