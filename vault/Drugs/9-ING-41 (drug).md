---
drug: "9-ING-41"
type: "drug"
salt_base: "9-ING-41"
targets: "GSK3B"
moa_fine: "GSK3 inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 662
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# 9-ING-41

*GSK3 inhibitor (inhibitor/antagonist) · targets: GSK3B · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 7 / 662 / 2; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): -0.35 / -0.66.
> Flags by dose: - / low cells (technical?); plate-row cell shift; noisy plate (z scaled) / plate-row cell shift; noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:D9 | 6 / 1 | — | +0.36 | -1.2/-0.6/-0.7 | — |
| 0.5 µM | [[Plate 02]]:D9 | 518 / 144 | — | -1.16 | +0.1/+1.1/+2.7 | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:D9 | 1 / 1 | — | +1.48 | -0.5/+0.2/-1.5 | plate-row cell shift; noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (6 genes, none with an alert): [[HNRNPK-AS1]] 1.47× (z +3.7, 6/44 lines), [[C3orf52]] 1.38× (z +3.4, 21/42 lines), [[BACH2]] 1.21× (z +3.3, 5/41 lines), [[NAV3]] 1.28× (z +3.3, 9/32 lines), [[CLIP4]] 1.21× (z +2.9, 5/36 lines), [[PLCL1]] 1.31× (z +2.7, 0/43 lines)

**0.5 µM** (518 genes, none with an alert; 12 shown): [[DHPS]] 1.75× (z +5.3, 32/47 lines), [[RER1]] 1.44× (z +5.3, 25/48 lines), [[SPINT2]] 1.55× (z +5.2, 21/24 lines), [[TSPAN3]] 1.53× (z +5.2, 34/48 lines), [[HNRNPH1]] 1.76× (z +5.1, 47/48 lines), [[POLR2F]] 1.79× (z +5.1, 32/48 lines), [[MTPN]] 1.40× (z +4.9, 40/48 lines), [[ADIPOR1]] 1.57× (z +4.8, 40/48 lines), [[DDR1]] 1.55× (z +4.7, 19/43 lines), [[FHOD1]] 1.73× (z +4.7, 20/44 lines), [[DYNLRB1]] 1.62× (z +4.6, 42/48 lines), [[UPP1]] 1.87× (z +4.6, 33/39 lines)

**5 µM** (1 gene, none with an alert): [[ZFPM2-AS1]] 1.41× (z +2.9, 8/33 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[SLC16A14]] 0.762× (z -3.0, 1/31 lines)

**0.5 µM** (144 genes, none with an alert; 12 shown): [[ZNF584]] 0.621× (z -5.4, 17/44 lines), [[ZNG1E]] 0.675× (z -4.9, 13/44 lines), [[SETD2]] 0.815× (z -4.7, 28/48 lines), [[ENSG00000285043]] 0.541× (z -4.4, 12/38 lines), [[ZNF286A]] 0.753× (z -4.3, 14/46 lines), [[C1orf112]] 0.696× (z -4.2, 16/47 lines), [[LINC00888]] 0.516× (z -4.2, 10/21 lines), [[ZNF527]] 0.622× (z -4.1, 12/39 lines), [[GRB2]] 0.787× (z -4.1, 24/48 lines), [[ICE1]] 0.802× (z -4.1, 23/48 lines), [[FN3K]] 0.672× (z -4.1, 16/43 lines), [[TIGD1]] 0.591× (z -4.0, 13/41 lines)

**5 µM** (1 gene, none with an alert): [[SGPP2]] 0.680× (z -3.3, 0/16 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 002]] (+2.8), [[Module 059]] (+2.7), [[Module 024]] (+2.4) | [[Module 020]] (-2.3), [[Module 018]] (-2.0) |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[HCT15 (line)]] (-3.9) | [[SW 1271 (line)]] (1.16), [[LOX-IMVI (line)]] (1.06), [[CHP-212 (line)]] (1.06), [[LS 180 (line)]] (1.05) · weakest: [[SHP-77 (line)]] (0.801), [[NCI-H23 (line)]] (0.817), [[BT-474 (line)]] (0.824) |
| 5 µM | [[KATO III (line)]] (-3.3) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[XRK3F2 (drug)]] (+0.87, unclear); [[LY-2584702 (tosylate salt) (drug)]] (+0.83, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[Nimesulide (drug)]] (+0.81, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[Thymol (drug)]] (+0.79, unclear); [[BI-78D3 (drug)]] (+0.78, Other MAPK inhibitor); [[Celecoxib (drug)]] (+0.76, Cyclooxygenase inhibitor); [[Canagliflozin (hemihydrate) (drug)]] (+0.76, Glucose transporter inhibitor); [[Ipatasertib (drug)]] (+0.76, PI3K/AKT inhibitor); [[Canagliflozin (drug)]] (+0.75, Glucose transporter inhibitor); [[Lenalidomide (hemihydrate) (drug)]] (+0.69, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 34 arrows, 34 of them with an alert ⚠; grade A 0, B 24, C 10. Shown: the 15 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[DMKN]] | 5 µM | B | DMKN activity lowers the cells' numbers under 9-ING-41 5 µM (makes them more sensitive) | lines that do not express DMKN (24) vs lines expressing it (24) | the lines without DMKN: 1.18× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: SPINT1, BSPRY, SMPDL3B |
| [[HOOK1]] | 5 µM | B | HOOK1 activity lowers the cells' numbers under 9-ING-41 5 µM (makes them more sensitive) | lines that do not express HOOK1 (22) vs lines expressing it (26) | the lines without HOOK1: 1.16× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1 |
| [[SIRLNT]] | 5 µM | B | SIRLNT activity raises the cells' numbers under 9-ING-41 5 µM (protects the cells) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 0.82× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[TRPM2-AS]] | 0.5 µM | B | TRPM2-AS activity lowers the cells' numbers under 9-ING-41 0.5 µM (makes them more sensitive) | lines that do not express TRPM2-AS (29) vs lines expressing it (19) | the lines without TRPM2-AS: 1.22× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1 |
| [[ENSG00000230647]] | 0.05 µM | B | ENSG00000230647 activity raises the cells' numbers under 9-ING-41 0.05 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.82× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[PLCE1]] | 5 µM | B | PLCE1 activity raises the cells' numbers under 9-ING-41 5 µM (protects the cells) | lines that do not express PLCE1 (16) vs lines expressing it (32) | the lines without PLCE1: 0.89× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: SLC46A3; maybe low, not absent |
| [[BMPER]] | 5 µM | B | BMPER activity raises the cells' numbers under 9-ING-41 5 µM (protects the cells) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 0.85× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[LOXL2]] | 0.5 µM | B | LOXL2 activity raises the cells' numbers under 9-ING-41 0.5 µM (protects the cells) | lines that do not express LOXL2 (18) vs lines expressing it (30) | the lines without LOXL2: 0.80× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1 |
| [[TMC6]] | 5 µM | B | TMC6 activity lowers the cells' numbers under 9-ING-41 5 µM (makes them more sensitive) | lines that do not express TMC6 (12) vs lines expressing it (36) | the lines without TMC6: 1.18× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[AOX1]] | 0.05 µM | B | AOX1 activity raises the cells' numbers under 9-ING-41 0.05 µM (protects the cells) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 0.86× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[SYTL1]] | 5 µM | B | SYTL1 activity lowers the cells' numbers under 9-ING-41 5 µM (makes them more sensitive) | lines that do not express SYTL1 (15) vs lines expressing it (33) | the lines without SYTL1: 1.21× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[CKMT1B]] | 0.05 µM | B | CKMT1B activity lowers the cells' numbers under 9-ING-41 0.05 µM (makes them more sensitive) | lines that do not express CKMT1B (28) vs lines expressing it (20) | the lines without CKMT1B: 1.17× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| [[EPPK1]] | 5 µM | B | EPPK1 activity lowers the cells' numbers under 9-ING-41 5 µM (makes them more sensitive) | lines that do not express EPPK1 (25) vs lines expressing it (23) | the lines without EPPK1: 1.17× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[MGAT4A]] | 5 µM | B | MGAT4A activity lowers the cells' numbers under 9-ING-41 5 µM (makes them more sensitive) | lines that do not express MGAT4A (11) vs lines expressing it (37) | the lines without MGAT4A: 1.23× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, ZNF860, EPHA2 |
| [[LINC01583]] | 5 µM | B | LINC01583 activity raises the cells' numbers under 9-ING-41 5 µM (protects the cells) | lines that do not express LINC01583 (28) vs lines expressing it (20) | the lines without LINC01583: 0.83× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: INSYN2B, ADAM12, ZEB2 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "9-ING-41"
- `tables/drugdoses.parquet` — dd in 21, 22, 23
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
