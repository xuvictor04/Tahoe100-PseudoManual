---
drug: "Posaconazole"
type: "drug"
salt_base: "Posaconazole"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 70
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Posaconazole

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 11 / 70; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.03 / -0.23.
> Flags by dose: - / - / plate-row cell shift.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:A2 | 1 / 0 | — | +0.05 | +0.1/-0.0/-0.3 | — |
| 0.5 µM | [[Plate 08]]:A2 | 10 / 1 | — | -0.19 | +0.1/+0.8/+1.1 | — |
| 5 µM | [[Plate 09]]:A2 | 54 / 16 | — | +1.15 | -2.2/-1.3/-1.9 | plate-row cell shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[DNAI7]] 1.36× (z +3.0, 5/42 lines)

**0.5 µM** (10 genes, none with an alert): [[PKD1L1-AS1]] 1.61× (z +3.4, 1/11 lines), [[FDPS]] 1.30× (z +3.3, 26/48 lines), [[KCP]] 1.42× (z +3.3, 1/34 lines), [[ALDH1A1]] 1.36× (z +3.3, 0/12 lines), [[UPK1B]] 1.66× (z +3.2, 0/5 lines), [[TRPV4]] 1.42× (z +3.2, 1/18 lines), [[ENSG00000262198]] 1.64× (z +3.2, 0/4 lines), [[LYZ]] 1.51× (z +3.1, 0/8 lines), [[ADAMTS19]] 1.41× (z +2.9, 0/26 lines), [[DAAM2]] 1.45× (z +2.8, 0/13 lines)

**5 µM** (54 genes, none with an alert; 12 shown): [[SCD]] 2.02× (z +9.6, 47/48 lines), [[LPIN1]] 1.47× (z +8.3, 30/48 lines), [[ACSS2]] 1.63× (z +7.4, 33/47 lines), [[FASN]] 2.10× (z +7.1, 38/47 lines), [[DHCR7]] 2.00× (z +6.8, 33/44 lines), [[LDLR]] 1.63× (z +6.5, 37/46 lines), [[IDI1]] 1.66× (z +6.5, 36/48 lines), [[SREBF2]] 1.51× (z +6.5, 43/48 lines), [[HSD17B7]] 1.62× (z +6.4, 17/47 lines), [[LSS]] 1.67× (z +6.3, 36/48 lines), [[DHCR24]] 1.62× (z +6.1, 30/44 lines), [[HMGCS1]] 1.64× (z +5.8, 34/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[OR51B5]] 0.814× (z -3.0, 1/31 lines)

**5 µM** (16 genes, none with an alert; 12 shown): [[TCP1]] 0.783× (z -4.0, 27/48 lines), [[MZT1]] 0.759× (z -3.8, 26/48 lines), [[MCF2]] 0.664× (z -3.7, 5/43 lines), [[PRPF4]] 0.831× (z -3.7, 8/48 lines), [[ENSG00000291075]] 0.755× (z -3.5, 4/45 lines), [[HSPA4]] 0.830× (z -3.5, 19/48 lines), [[MATR3]] 0.827× (z -3.5, 26/48 lines), [[MSL3]] 0.820× (z -3.4, 6/47 lines), [[DNAJC9]] 0.828× (z -3.3, 12/48 lines), [[CDCA7]] 0.773× (z -3.2, 4/41 lines), [[SPCS2]] 0.810× (z -3.1, 22/48 lines), [[WDR76]] 0.805× (z -3.1, 5/46 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 086]] (+4.1) | [[Module 182]] (-2.2) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[MIA PaCa-2 (line)]] (-3.1) | [[HEC-1-A (line)]] (1.83), [[AsPC-1 (line)]] (1.76), [[NCI-H1573 (line)]] (1.55), [[COLO 205 (line)]] (1.48) · weakest: [[NCI-H661 (line)]] (0.325), [[HepG2_C3A (line)]] (0.325), [[SK-MEL-2 (line)]] (0.422) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Daidzin (drug)]] (+0.62, unclear, ⚠ only 3 significant genes); [[Berbamine (dihydrochloride) (drug)]] (+0.53, unclear); [[Tirabrutinib (hydrochloride) (drug)]] (+0.51, Other TK inhibitor); [[Almonertinib (mesylate) (drug)]] (+0.49, EGFR/ERBB inhibitor); [[Sinomenine (drug)]] (+0.46, unclear); [[Fumaric acid (drug)]] (+0.45, unclear); [[Hesperidin (drug)]] (+0.43, unclear); [[Pexidartinib (hydrochloride) (drug)]] (+0.41, Multi-TK inhibitor); [[Entrectinib (drug)]] (+0.40, Other TK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 25 arrows, 25 of them with an alert ⚠; grade A 0, B 12, C 13. Shown: the 15 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[CDH3]] | 5 µM | B | CDH3 activity lowers the cells' numbers under Posaconazole 5 µM (makes them more sensitive) | lines that do not express CDH3 (26) vs lines expressing it (22) | the lines without CDH3: 1.22× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: CKMT1A, ESRP1, GPR87; maybe low, not absent |
| [[BMPER]] | 5 µM | B | BMPER activity raises the cells' numbers under Posaconazole 5 µM (protects the cells) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 0.86× the cells of the other lines | 0.074 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[MSRB3]] | 5 µM | B | MSRB3 activity raises the cells' numbers under Posaconazole 5 µM (protects the cells) | lines that do not express MSRB3 (20) vs lines expressing it (28) | the lines without MSRB3: 0.85× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[GJC1]] | 0.5 µM | B | GJC1 activity raises the cells' numbers under Posaconazole 0.5 µM (protects the cells) | lines that do not express GJC1 (13) vs lines expressing it (35) | the lines without GJC1: 0.83× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB |
| [[FAM13C]] | 5 µM | B | FAM13C activity raises the cells' numbers under Posaconazole 5 µM (protects the cells) | lines that do not express FAM13C (15) vs lines expressing it (33) | the lines without FAM13C: 0.84× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[KLRC4-KLRK1]], [[KLRK1]] | 0.5 µM | B | KLRC4-KLRK1, KLRK1 activity lowers the cells' numbers under Posaconazole 0.5 µM (makes them more sensitive) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 1.15× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| [[ATP2C2]] | 5 µM | B | ATP2C2 activity lowers the cells' numbers under Posaconazole 5 µM (makes them more sensitive) | lines that do not express ATP2C2 (32) vs lines expressing it (16) | the lines without ATP2C2: 1.21× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[EHF]] | 5 µM | B | EHF activity lowers the cells' numbers under Posaconazole 5 µM (makes them more sensitive) | lines that do not express EHF (27) vs lines expressing it (21) | the lines without EHF: 1.17× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[CGAS]] | 0.5 µM | B | CGAS activity raises the cells' numbers under Posaconazole 0.5 µM (protects the cells) | lines that do not express CGAS (17) vs lines expressing it (31) | the lines without CGAS: 0.84× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP |
| [[SLFN5]] | 0.5 µM | B | SLFN5 activity raises the cells' numbers under Posaconazole 0.5 µM (protects the cells) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 0.82× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[BARX2]] | 5 µM | B | BARX2 activity lowers the cells' numbers under Posaconazole 5 µM (makes them more sensitive) | lines that do not express BARX2 (29) vs lines expressing it (19) | the lines without BARX2: 1.17× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[GRHL2]], [[LINC02967]] | 5 µM | B | GRHL2, LINC02967 activity lowers the cells' numbers under Posaconazole 5 µM (makes them more sensitive) | lines that do not express GRHL2, LINC02967 (34) vs lines expressing them (14) | the lines without GRHL2, LINC02967: 1.21× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent genes |
| [[FIGN]] | 0.5 µM | C | FIGN activity raises the cells' numbers under Posaconazole 0.5 µM (protects the cells) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 0.84× the cells of the other lines | 0.019 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[NR3C1]] | 0.5 µM | C | NR3C1 activity raises the cells' numbers under Posaconazole 0.5 µM (protects the cells) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 0.82× the cells of the other lines | 0.022 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[SPAG16]] | 0.5 µM | C | SPAG16 activity raises the cells' numbers under Posaconazole 0.5 µM (protects the cells) | lines that do not express SPAG16 (6) vs lines expressing it (42) | the lines without SPAG16: 0.79× the cells of the other lines | 0.027 | ⚠ tissue-confounded; across organs; co-occurs with WNK2, BRCA2; also absent: ZNF140, LUCAT1, GCA |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Posaconazole"
- `tables/drugdoses.parquet` — dd in 833, 834, 835
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
