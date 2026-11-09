---
drug: "Peretinoin"
type: "drug"
salt_base: "Peretinoin"
targets: "RXRA, RXRB, RXRG"
moa_fine: "Retinoic receptor agonist"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 1459
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Peretinoin

*Retinoic receptor agonist (unclear) · targets: RXRA, RXRB, RXRG · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 227 / 1323 / 1459; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.67 / 0.82.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:H8 | 167 / 60 | — | +0.50 | +0.4/+2.3/+1.7 | — |
| 0.5 µM | [[Plate 08]]:H8 | 614 / 709 | — | -0.39 | -0.4/+2.5/+2.8 | — |
| 5 µM | [[Plate 09]]:H8 | 665 / 794 | — | -0.35 | -1.6/+2.5/+2.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (167 genes, 5 with an alert ⚠; 16 shown): [[MAP7D1]] ⚠ 2.08× (z +12.0, 48/48 lines; position correction uncertain), [[ACOT7]] ⚠ 1.58× (z +9.1, 38/46 lines; position correction uncertain), [[NF2]] ⚠ 1.48× (z +8.6, 33/47 lines; position correction uncertain), [[CPNE1]] 1.44× (z +7.2, 40/48 lines), [[AURKA]] 1.56× (z +5.6, 32/48 lines), [[DAXX]] 1.57× (z +5.4, 40/48 lines), [[RANGAP1]] 1.33× (z +5.3, 24/47 lines), [[HMG20B]] 1.38× (z +5.0, 25/47 lines), [[MSN]] 1.34× (z +4.9, 31/38 lines), [[ARHGAP11A]] 1.37× (z +4.7, 26/47 lines), [[LYAR]] ⚠ 1.48× (z +4.7, 28/47 lines; position correction uncertain), [[DHX16]] 1.35× (z +4.6, 25/47 lines), [[CCNA2]] 1.61× (z +4.6, 28/48 lines), [[CCNB1]] 1.49× (z +4.5, 26/47 lines), [[STK11]] 1.29× (z +4.5, 8/45 lines), [[LRPAP1]] 1.40× (z +4.5, 35/48 lines)

**0.5 µM** (614 genes, 5 with an alert ⚠; 16 shown): [[CREB5]] ⚠ 2.71× (z +17.5, 29/32 lines; position correction uncertain), [[MAP7D1]] ⚠ 2.22× (z +14.2, 47/47 lines; position correction uncertain), [[NF2]] ⚠ 1.79× (z +13.7, 39/46 lines; position correction uncertain), [[ARHGAP29]] 1.55× (z +9.7, 28/37 lines), [[SAMD4A]] 1.80× (z +9.2, 36/45 lines), [[ACOT7]] ⚠ 1.50× (z +8.7, 35/45 lines; position correction uncertain), [[MYEF2]] 1.50× (z +8.2, 22/31 lines), [[CLIP1]] 1.28× (z +8.0, 32/47 lines), [[BACH2]] 1.54× (z +7.9, 24/40 lines), [[MYO5B]] 1.49× (z +7.9, 17/22 lines), [[CLDN1]] 1.54× (z +7.9, 19/25 lines), [[MGLL]] 1.39× (z +7.7, 25/33 lines), [[KRTAP5-AS1]] 2.19× (z +7.6, 18/32 lines), [[RANGAP1]] 1.46× (z +7.6, 34/47 lines), [[DUSP8]] 2.17× (z +7.5, 28/43 lines), [[ENSG00000285845]] 2.12× (z +7.5, 14/17 lines)

**5 µM** (665 genes, 5 with an alert ⚠; 15 shown): [[CREB5]] ⚠ 3.51× (z +21.1, 31/32 lines; position correction uncertain), [[NF2]] ⚠ 1.83× (z +13.7, 39/46 lines; position correction uncertain), [[MAP7D1]] ⚠ 1.93× (z +11.2, 44/47 lines; position correction uncertain), [[CLIP1]] 1.44× (z +11.1, 38/47 lines), [[SAMD4A]] 1.99× (z +10.4, 42/45 lines), [[CORO2B]] 2.78× (z +10.2, 24/34 lines), [[MGLL]] 1.56× (z +10.0, 29/33 lines), [[BACH2]] 1.75× (z +9.9, 29/40 lines), [[ARHGAP29]] 1.57× (z +9.6, 32/37 lines), [[DAAM1]] 1.45× (z +9.3, 37/46 lines), [[CAPN2]] 1.48× (z +9.2, 35/47 lines), [[DTNA]] 1.98× (z +9.2, 21/25 lines), [[CLDN1]] 1.68× (z +9.1, 20/25 lines), [[IGF2BP2]] 1.35× (z +8.7, 31/44 lines), [[NAV3]] 1.87× (z +8.5, 22/31 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (60 genes, 1 with an alert ⚠; 13 shown): [[FNDC3A]] ⚠ 0.800× (z -4.7, 29/48 lines; position correction uncertain), [[TUBB]] 0.681× (z -4.6, 35/47 lines), [[DOP1A]] 0.782× (z -4.5, 20/48 lines), [[LMBRD1]] 0.825× (z -4.1, 15/48 lines), [[ZDHHC20]] 0.824× (z -3.8, 22/48 lines), [[JAKMIP3]] 0.736× (z -3.8, 3/35 lines), [[DMXL2]] 0.748× (z -3.8, 30/45 lines), [[NRG2]] 0.769× (z -3.7, 10/32 lines), [[SSBP2]] 0.790× (z -3.6, 23/44 lines), [[LRP12]] 0.832× (z -3.6, 11/40 lines), [[ZNF615]] 0.791× (z -3.6, 8/39 lines), [[ENSG00000290876]] 0.672× (z -3.5, 8/41 lines), [[ACACB]] 0.745× (z -3.5, 14/46 lines)

**0.5 µM** (709 genes, 1 with an alert ⚠; 12 shown): [[INTU]] 0.661× (z -7.5, 25/45 lines), [[DHRS3]] 0.639× (z -7.3, 26/35 lines), [[MLLT3]] 0.676× (z -7.2, 27/41 lines), [[PTCH1]] 0.631× (z -7.1, 29/45 lines), [[TRERF1]] 0.680× (z -7.0, 35/41 lines), [[TRIM9]] 0.620× (z -7.0, 24/31 lines), [[ROBO1]] 0.724× (z -6.9, 25/34 lines), [[MEIS2]] 0.705× (z -6.9, 35/44 lines), [[MEF2C]] 0.665× (z -6.7, 22/33 lines), [[PHF21A]] 0.719× (z -6.7, 33/47 lines), [[RHOXF1]] 0.641× (z -6.6, 36/46 lines), [[ZSWIM5]] 0.719× (z -6.5, 32/42 lines)

**5 µM** (794 genes, 1 with an alert ⚠; 12 shown): [[NFIA]] 0.635× (z -8.4, 30/37 lines), [[HOXA3]] 0.644× (z -8.1, 26/37 lines), [[MEF2C]] 0.600× (z -8.1, 26/33 lines), [[TNRC6B]] 0.822× (z -8.0, 24/47 lines), [[PTCH1]] 0.584× (z -8.0, 34/45 lines), [[DHRS3]] 0.615× (z -7.6, 28/35 lines), [[ETV1]] 0.530× (z -7.6, 27/36 lines), [[TENT5A]] 0.643× (z -7.4, 23/36 lines), [[HERC5]] 0.542× (z -7.4, 23/32 lines), [[LPCAT3]] 0.673× (z -7.2, 29/47 lines), [[GBP4]] 0.459× (z -7.0, 22/27 lines), [[LNX1]] 0.674× (z -6.9, 11/26 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 060]] (+2.6), [[Module 002]] (+2.5) | — |
| 0.5 µM | [[Module 184]] (+3.3), [[Module 002]] (+3.3), [[Module 060]] (+3.3) | [[Module 200]] (-3.0), [[Module 230]] (-3.0), [[Module 065]] (-2.8) |
| 5 µM | [[Module 184]] (+4.8), [[Module 116]] (+3.7), [[Module 060]] (+3.5) | [[Module 065]] (-3.9), [[Module 205]] (-3.6), [[Module 059]] (-3.5) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[RKO (line)]] (-4.3), [[NCI-H23 (line)]] (-3.3) | [[NCI-H460 (line)]] (1.67), [[SW 900 (line)]] (1.55), [[HT-29 (line)]] (1.41), [[NCI-H1792 (line)]] (1.31) · weakest: [[CHP-212 (line)]] (0.548), [[SW 1088 (line)]] (0.632), [[HepG2_C3A (line)]] (0.633) |
| 0.5 µM | [[H4 (line)]] (-8.4), [[hTERT-HPNE (line)]] (-6.1), [[HS-578T (line)]] (-4.9), [[NCI-H23 (line)]] (-4.5), [[HOP62 (line)]] (-3.7) | [[H4 (line)]] (1.64), [[NCI-H23 (line)]] (1.58), [[MIA PaCa-2 (line)]] (1.42), [[HT-29 (line)]] (1.39) · weakest: [[HepG2_C3A (line)]] (0.466), [[SHP-77 (line)]] (0.486), [[J82 (line)]] (0.595) |
| 5 µM | [[H4 (line)]] (-4.7), [[NCI-H23 (line)]] (-3.4) | [[HT-29 (line)]] (1.62), [[H4 (line)]] (1.44), [[NCI-H1573 (line)]] (1.44), [[CFPAC-1 (line)]] (1.43) · weakest: [[SW1417 (line)]] (0.570), [[HEC-1-A (line)]] (0.591), [[J82 (line)]] (0.593) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Daptomycin (drug)]] (+0.90, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Vinblastine (sulfate) (drug)]] (+0.81, Microtubule inhibitor); [[vincristine (drug)]] (+0.73, Microtubule inhibitor); [[5-Azacytidine (drug)]] (+0.59, DNA methyltransferase inhibitor); [[Mebendazole (drug)]] (+0.57, Microtubule inhibitor); [[Neratinib (drug)]] (+0.42, EGFR/ERBB inhibitor); [[Infigratinib (drug)]] (+0.42, Other TK inhibitor); [[Acetohexamide (drug)]] (+0.40, unclear); [[BAY1125976 (drug)]] (+0.36, PI3K/AKT inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 63 arrows, 63 of them with an alert ⚠; grade A 0, B 49, C 14. Shown: the 15 strongest; 48 more arrows (48 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SPOCK1]] | 0.5 µM | B | SPOCK1 activity lowers the cells' numbers under Peretinoin 0.5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.54× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[BMPER]] | 0.5 µM | B | BMPER activity lowers the cells' numbers under Peretinoin 0.5 µM (makes them more sensitive) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 1.48× the cells of the other lines | 0.030 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[MSRB3]] | 0.5 µM | B | MSRB3 activity lowers the cells' numbers under Peretinoin 0.5 µM (makes them more sensitive) | lines that do not express MSRB3 (20) vs lines expressing it (28) | the lines without MSRB3: 1.42× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[PAPPA]] | 0.5 µM | B | PAPPA activity lowers the cells' numbers under Peretinoin 0.5 µM (makes them more sensitive) | lines that do not express PAPPA (33) vs lines expressing it (15) | the lines without PAPPA: 1.54× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[ENSG00000230647]] | 0.5 µM | B | ENSG00000230647 activity lowers the cells' numbers under Peretinoin 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.43× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[EPCAM]] | 0.5 µM | B | EPCAM activity raises the cells' numbers under Peretinoin 0.5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.69× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[SNAP25]] | 0.5 µM | B | SNAP25 activity lowers the cells' numbers under Peretinoin 0.5 µM (makes them more sensitive) | lines that do not express SNAP25 (26) vs lines expressing it (22) | the lines without SNAP25: 1.40× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3 |
| [[MYH14]] | 0.5 µM | B | MYH14 activity raises the cells' numbers under Peretinoin 0.5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.68× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[ERBB3]] | 0.5 µM | B | ERBB3 activity raises the cells' numbers under Peretinoin 0.5 µM (protects the cells) | lines that do not express ERBB3 (27) vs lines expressing it (21) | the lines without ERBB3: 0.69× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[CNRIP1]] | 0.5 µM | B | CNRIP1 activity lowers the cells' numbers under Peretinoin 0.5 µM (makes them more sensitive) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 1.37× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| [[EDN1]] | 5 µM | B | EDN1 activity raises the cells' numbers under Peretinoin 5 µM (protects the cells) | lines that do not express EDN1 (27) vs lines expressing it (21) | the lines without EDN1: 0.86× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[LGALS3BP]] | 5 µM | B | LGALS3BP activity raises the cells' numbers under Peretinoin 5 µM (protects the cells) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 0.90× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[C19orf33]] | 5 µM | B | C19orf33 activity raises the cells' numbers under Peretinoin 5 µM (protects the cells) | lines that do not express C19orf33 (19) vs lines expressing it (29) | the lines without C19orf33: 0.87× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: KRT80, MISP, AREG |
| [[GJA1]] | 0.5 µM | B | GJA1 activity lowers the cells' numbers under Peretinoin 0.5 µM (makes them more sensitive) | lines that do not express GJA1 (26) vs lines expressing it (22) | the lines without GJA1: 1.39× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |
| [[LEF1-AS1]] | 5 µM | B | LEF1-AS1 activity lowers the cells' numbers under Peretinoin 5 µM (makes them more sensitive) | lines that do not express LEF1-AS1 (33) vs lines expressing it (15) | the lines without LEF1-AS1: 1.21× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Peretinoin"
- `tables/drugdoses.parquet` — dd in 797, 798, 799
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
