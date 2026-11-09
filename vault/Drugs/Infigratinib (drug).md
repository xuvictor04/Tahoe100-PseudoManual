---
drug: "Infigratinib"
type: "drug"
salt_base: "Infigratinib"
targets: "FGFR1, FGFR2, FGFR3, FGFR4"
moa_fine: "Other TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 281
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Infigratinib

*Other TK inhibitor (inhibitor/antagonist) · targets: FGFR1, FGFR2, FGFR3, FGFR4 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 81 / 1 / 281; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.38 / 0.28.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:A1 | 31 / 50 | — | +0.13 | +1.8/+1.6/+1.9 | — |
| 0.5 µM | [[Plate 02]]:A1 | 0 / 1 | — | +0.27 | +0.0/-0.2/-0.5 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:A1 | 227 / 54 | — | +0.45 | -2.5/-0.4/+0.6 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (31 genes, none with an alert; 12 shown): [[SAAL1]] 1.28× (z +4.0, 13/48 lines), [[TOP1MT]] 1.24× (z +4.0, 4/47 lines), [[CTSZ]] 1.23× (z +3.8, 7/40 lines), [[HNRNPA3]] 1.24× (z +3.8, 26/48 lines), [[PPIA]] 1.30× (z +3.5, 25/48 lines), [[USP11]] 1.28× (z +3.5, 19/48 lines), [[SUSD5]] 1.45× (z +3.5, 1/23 lines), [[BABAM1]] 1.31× (z +3.5, 9/48 lines), [[EDARADD]] 1.28× (z +3.4, 1/22 lines), [[MARVELD1]] 1.45× (z +3.4, 1/43 lines), [[SLC4A2]] 1.28× (z +3.4, 15/48 lines), [[DNTTIP1]] 1.27× (z +3.4, 11/48 lines)

**5 µM** (227 genes, none with an alert; 12 shown): [[BAG3]] 3.93× (z +12.8, 47/48 lines), [[DNAJA4]] 4.58× (z +11.4, 25/25 lines), [[HMOX1]] 6.84× (z +9.5, 29/37 lines), [[HSPH1]] 5.12× (z +8.9, 47/48 lines), [[HSPA1B]] 6.63× (z +8.8, 45/46 lines), [[HSPA4L]] 2.63× (z +8.4, 41/45 lines), [[HSPA1A]] 10.7× (z +8.3, 34/35 lines), [[DNAJB4]] 2.79× (z +8.1, 38/45 lines), [[DNAJB1]] 3.16× (z +6.8, 46/48 lines), [[STIP1]] 2.23× (z +6.6, 42/48 lines), [[HIBCH]] 1.58× (z +6.5, 32/48 lines), [[ABHD3]] 2.04× (z +6.5, 42/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (50 genes, none with an alert; 12 shown): [[EOGT]] 0.721× (z -4.5, 14/47 lines), [[HCLS1]] 0.557× (z -4.2, 16/44 lines), [[ENSG00000260060]] 0.552× (z -4.1, 14/44 lines), [[LINC02955]] 0.686× (z -4.0, 7/46 lines), [[CDKL1]] 0.796× (z -4.0, 15/48 lines), [[COG6]] 0.756× (z -4.0, 29/48 lines), [[ENSG00000273507]] 0.678× (z -3.8, 12/44 lines), [[C9orf153]] 0.751× (z -3.7, 11/47 lines), [[APRG1]] 0.681× (z -3.7, 27/48 lines), [[ENSG00000288000]] 0.637× (z -3.7, 30/48 lines), [[ENSG00000275740]] 0.752× (z -3.6, 12/46 lines), [[ENSG00000257759]] 0.748× (z -3.6, 18/47 lines)

**0.5 µM** (1 gene, none with an alert): [[MT-CO1]] 0.659× (z -3.5, 44/49 lines)

**5 µM** (54 genes, none with an alert; 12 shown): [[GDAP1]] 0.508× (z -4.7, 18/39 lines), [[KIF3A]] 0.732× (z -4.0, 16/48 lines), [[USP18]] 0.467× (z -3.8, 21/41 lines), [[PBRM1]] 0.794× (z -3.7, 13/48 lines), [[TXNIP]] 0.578× (z -3.7, 24/37 lines), [[UNK]] 0.739× (z -3.7, 11/48 lines), [[RFC3]] 0.714× (z -3.5, 9/47 lines), [[SARS2]] 0.608× (z -3.5, 9/43 lines), [[ASH2L]] 0.745× (z -3.4, 5/47 lines), [[PNPT1]] 0.663× (z -3.3, 19/47 lines), [[FAM120C]] 0.725× (z -3.3, 7/46 lines), [[SSH2]] 0.791× (z -3.2, 12/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 179]] (-2.4) |
| 0.5 µM | — | — |
| 5 µM | [[Module 060]] (+4.1), [[Module 135]] (+2.0) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[RPMI-7951 (line)]] (-3.1) | [[MIA PaCa-2 (line)]] (1.58), [[SW 1088 (line)]] (1.38), [[NCI-H1573 (line)]] (1.37), [[hTERT-HPNE (line)]] (1.25) · weakest: [[NCI-H661 (line)]] (0.402), [[AN3 CA (line)]] (0.523), [[NCI-H2347 (line)]] (0.626) |
| 0.5 µM | — | — |
| 5 µM | [[SK-MEL-2 (line)]] (-5.8), [[NCI-H1792 (line)]] (-4.7), [[SNU-1 (line)]] (-4.5), [[H4 (line)]] (-4.3), [[CHP-212 (line)]] (-4.0) | [[AsPC-1 (line)]] (1.39), [[HOP62 (line)]] (1.39), [[BT-474 (line)]] (1.38), [[CHP-212 (line)]] (1.23) · weakest: [[SW 1088 (line)]] (0.424), [[SHP-77 (line)]] (0.696), [[A-427 (line)]] (0.697) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Auranofin (drug)]] (+0.59, unclear); [[Daptomycin (drug)]] (+0.42, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Peretinoin (drug)]] (+0.42, Retinoic receptor agonist); [[Bortezomib (drug)]] (+0.40, Proteasome inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Vinblastine (sulfate) (drug)]] (+0.39, Microtubule inhibitor); [[Neratinib (drug)]] (+0.37, EGFR/ERBB inhibitor); [[APTO-253 (drug)]] (+0.37, unclear, ⚠ only 4 significant genes); [[Neratinib (maleate) (drug)]] (+0.35, EGFR/ERBB inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[BAY1125976 (drug)]] (+0.33, PI3K/AKT inhibitor); [[5-Azacytidine (drug)]] (+0.31, DNA methyltransferase inhibitor); [[Temsirolimus (drug)]] (+0.30, MTOR inhibitor); [[Rapamycin (drug)]] (+0.30, MTOR inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 55 arrows, 55 of them with an alert ⚠; grade A 0, B 39, C 16. Shown: the 15 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[LGALS3BP]] | 0.5 µM | B | LGALS3BP activity raises the cells' numbers under Infigratinib 0.5 µM (protects the cells) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 0.77× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[IL15]] | 0.5 µM | B | IL15 activity raises the cells' numbers under Infigratinib 0.5 µM (protects the cells) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 0.79× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[ATP1B1]] | 0.5 µM | B | ATP1B1 activity raises the cells' numbers under Infigratinib 0.5 µM (protects the cells) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 0.81× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[ALDH3B1]] | 0.5 µM | B | ALDH3B1 activity raises the cells' numbers under Infigratinib 0.5 µM (protects the cells) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 0.82× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[ENSG00000251537]] | 0.5 µM | B | ENSG00000251537 activity raises the cells' numbers under Infigratinib 0.5 µM (protects the cells) | lines that do not express ENSG00000251537 (9) vs lines expressing it (39) | the lines without ENSG00000251537: 0.85× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: FBXW10B, PCED1B, NHS; maybe low, not absent |
| [[MSRB3-AS1]] | 0.05 µM | B | MSRB3-AS1 activity raises the cells' numbers under Infigratinib 0.05 µM (protects the cells) | lines that do not express MSRB3-AS1 (42) vs lines expressing it (6) | the lines without MSRB3-AS1: 0.74× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2 |
| [[ENSG00000258919]] | 0.5 µM | B | ENSG00000258919 activity raises the cells' numbers under Infigratinib 0.5 µM (protects the cells) | lines that do not express ENSG00000258919 (23) vs lines expressing it (25) | the lines without ENSG00000258919: 0.85× the cells of the other lines | 0.059 | ⚠ within organs, on part of the lines; also absent: LINC02320, ENSG00000266088, DIO3OS |
| [[BMP2]] | 0.5 µM | B | BMP2 activity raises the cells' numbers under Infigratinib 0.5 µM (protects the cells) | lines that do not express BMP2 (20) vs lines expressing it (28) | the lines without BMP2: 0.86× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[DUSP10]] | 0.5 µM | B | DUSP10 activity raises the cells' numbers under Infigratinib 0.5 µM (protects the cells) | lines that do not express DUSP10 (11) vs lines expressing it (37) | the lines without DUSP10: 0.86× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[SPTLC3]] | 0.5 µM | B | SPTLC3 activity raises the cells' numbers under Infigratinib 0.5 µM (protects the cells) | lines that do not express SPTLC3 (16) vs lines expressing it (32) | the lines without SPTLC3: 0.87× the cells of the other lines | 0.070 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[NMRAL2P-1]] | 0.5 µM | B | NMRAL2P-1 activity raises the cells' numbers under Infigratinib 0.5 µM (protects the cells) | lines that do not express NMRAL2P-1 (18) vs lines expressing it (30) | the lines without NMRAL2P-1: 0.87× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[LINC02320]] | 0.5 µM | B | LINC02320 activity raises the cells' numbers under Infigratinib 0.5 µM (protects the cells) | lines that do not express LINC02320 (19) vs lines expressing it (29) | the lines without LINC02320: 0.84× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[ENSG00000275993]] | 0.05 µM | B | ENSG00000275993 activity lowers the cells' numbers under Infigratinib 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000275993 (7) vs lines expressing it (41) | the lines without ENSG00000275993: 1.24× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: GAL3ST1, LINC00571; maybe low, not absent |
| [[MLPH]] | 0.5 µM | B | MLPH activity raises the cells' numbers under Infigratinib 0.5 µM (protects the cells) | lines that do not express MLPH (13) vs lines expressing it (35) | the lines without MLPH: 0.84× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[IFIT2]] | 5 µM | B | IFIT2 activity raises the cells' numbers under Infigratinib 5 µM (protects the cells) | lines that do not express IFIT2 (8) vs lines expressing it (40) | the lines without IFIT2: 0.78× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Infigratinib"
- `tables/drugdoses.parquet` — dd in 555, 556, 557
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
