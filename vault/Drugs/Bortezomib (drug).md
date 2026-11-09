---
drug: "Bortezomib"
type: "drug"
salt_base: "Bortezomib"
targets: "PSMB5"
moa_fine: "Proteasome inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 5863
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Bortezomib

*Proteasome inhibitor (inhibitor/antagonist) · targets: PSMB5 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 5863 / 1691 / 3848; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.86 / 0.80.
> Flags by dose: cell-cycle shift / noisy plate (z scaled) / toxic; cell-cycle shift; noisy plate (z scaled). ⚠ 0.05 µM: cell-cycle shift; 5 µM: toxic; cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:F1 | 2,917 / 2,946 | — | -0.61 | -3.8/-6.6/+15.8 | ⚠ cell-cycle shift |
| 0.5 µM | [[Plate 02]]:F1 | 1,069 / 622 | — | -0.18 | -0.5/-2.3/+6.5 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:F1 | 2,350 / 1,498 | — | -1.37 | -0.9/-4.2/+5.8 | ⚠ toxic; cell-cycle shift · noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2917 genes, 543 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[BAG3]] 9.56× (z +38.0, 48/48 lines; cell-cycle shift (explains ~0% here)), [[DNAJB1]] 11.3× (z +30.7, 48/48 lines; cell-cycle shift (explains ~0% here)), [[HIBCH]] 3.04× (z +29.3, 48/48 lines; cell-cycle shift (explains ~14% here)), [[HSPA1B]] 29.2× (z +28.4, 48/48 lines; cell-cycle shift (explains ~0% here)), [[CAMK2G]] 3.38× (z +27.9, 48/48 lines; cell-cycle shift (explains ~0% here)), [[DYNC1I1]] 10.3× (z +27.7, 29/31 lines; cell-cycle shift (explains ~3% here)), [[DNAJA4]] 6.83× (z +26.1, 25/25 lines; cell-cycle shift (explains ~0% here)), [[TMEM161A]] 4.16× (z +25.0, 41/43 lines; cell-cycle shift (explains ~0% here)), [[UFD1]] 3.84× (z +24.9, 48/48 lines; cell-cycle shift (explains ~0% here)), [[PSMD1]] 3.53× (z +24.8, 48/48 lines; cell-cycle shift (explains ~0% here)), [[PSMD12]] 2.84× (z +24.8, 48/48 lines; cell-cycle shift (explains ~0% here)), [[HSPA1A]] 51.3× (z +24.8, 35/35 lines; cell-cycle shift (explains ~0% here))

**0.5 µM** (1069 genes, none with an alert; 12 shown): [[BAG3]] 6.28× (z +23.4, 48/49 lines), [[DNAJA4]] 6.14× (z +18.6, 25/25 lines), [[HSPA1B]] 17.9× (z +18.3, 48/49 lines), [[SORBS1]] 3.07× (z +15.2, 37/43 lines), [[CAMK2G]] 2.27× (z +14.9, 45/49 lines), [[HSPH1]] 7.43× (z +14.8, 48/49 lines), [[HIBCH]] 2.04× (z +14.2, 45/49 lines), [[ABHD3]] 3.09× (z +13.9, 48/49 lines), [[UFD1]] 2.65× (z +13.6, 45/48 lines), [[OSBPL1A]] 1.98× (z +13.1, 34/47 lines), [[HSPA1A]] 26.1× (z +12.8, 35/35 lines), [[NAA25]] 2.17× (z +12.6, 46/49 lines)

**5 µM** (2350 genes, 2,350 with an alert ⚠; the drug-dose carries ⚠ toxic; cell-cycle shift; 12 shown): [[BAG3]] ⚠ 10.1× (z +21.5, 45/45 lines; toxic; cell-cycle shift (explains ~0% here)), [[DNAJA4]] ⚠ 14.7× (z +20.2, 22/22 lines; toxic; cell-cycle shift (explains ~0% here)), [[HSPA1B]] ⚠ 34.2× (z +16.5, 39/39 lines; toxic; cell-cycle shift (explains ~0% here)), [[HSPA4]] ⚠ 4.70× (z +15.7, 45/45 lines; toxic; cell-cycle shift (explains ~0% here)), [[SERPINH1]] ⚠ 9.28× (z +15.6, 41/42 lines; toxic; cell-cycle shift (explains ~0% here)), [[SORBS1]] ⚠ 4.74× (z +15.5, 32/36 lines; toxic; cell-cycle shift (explains ~3% here)), [[HIBCH]] ⚠ 2.96× (z +15.4, 43/45 lines; toxic; cell-cycle shift (explains ~17% here)), [[HSPH1]] ⚠ 15.8× (z +15.0, 44/44 lines; toxic; cell-cycle shift (explains ~0% here)), [[DNAJB1]] ⚠ 12.0× (z +14.8, 45/45 lines; toxic; cell-cycle shift (explains ~0% here)), [[HSPA1A]] ⚠ 57.9× (z +14.1, 31/31 lines; toxic; cell-cycle shift (explains ~0% here)), [[HSPA4L]] ⚠ 4.75× (z +13.6, 40/41 lines; toxic; cell-cycle shift (explains ~0% here)), [[LARP4]] ⚠ 2.97× (z +13.4, 43/45 lines; toxic; cell-cycle shift (explains ~1% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2946 genes, 557 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[AXL]] 0.342× (z -15.8, 32/34 lines; cell-cycle shift (explains ~18% here)), [[SCLT1]] 0.445× (z -15.3, 46/48 lines; cell-cycle shift (explains ~19% here)), [[ZC3H6]] 0.520× (z -13.6, 43/48 lines; cell-cycle shift (explains ~0% here)), [[RIN2]] 0.391× (z -13.3, 35/39 lines; cell-cycle shift (explains ~0% here)), [[TXNIP]] 0.345× (z -13.1, 36/37 lines; cell-cycle shift (explains ~22% here)), [[TRERF1]] 0.476× (z -12.8, 39/42 lines; cell-cycle shift (explains ~0% here)), [[H6PD]] 0.442× (z -12.7, 42/48 lines; cell-cycle shift (explains ~0% here)), [[ZNF33A]] 0.632× (z -12.5, 44/48 lines; cell-cycle shift (explains ~0% here)), [[GPD2]] 0.569× (z -12.4, 40/46 lines; cell-cycle shift (explains ~0% here)), [[TPCN1]] 0.563× (z -12.3, 35/48 lines; cell-cycle shift (explains ~0% here)), [[ZSWIM5]] 0.520× (z -12.2, 40/43 lines; cell-cycle shift (explains ~0% here)), [[ETV1]] 0.335× (z -12.0, 36/37 lines; cell-cycle shift (explains ~7% here))

**0.5 µM** (622 genes, none with an alert; 12 shown): [[ARL6IP6]] 0.617× (z -5.4, 35/48 lines), [[TMBIM4]] 0.692× (z -5.1, 27/48 lines), [[SCLT1]] 0.699× (z -5.1, 33/49 lines), [[AXL]] 0.684× (z -5.1, 25/35 lines), [[C6orf89]] 0.763× (z -5.0, 20/48 lines), [[NHLRC2]] 0.732× (z -5.0, 26/49 lines), [[SEC22C]] 0.742× (z -5.0, 16/48 lines), [[H6PD]] 0.658× (z -4.9, 26/48 lines), [[FAM114A2]] 0.714× (z -4.8, 15/48 lines), [[NT5E]] 0.574× (z -4.8, 28/35 lines), [[FAM220A]] 0.659× (z -4.7, 7/48 lines), [[CHML]] 0.706× (z -4.7, 22/49 lines)

**5 µM** (1498 genes, 1,498 with an alert ⚠; the drug-dose carries ⚠ toxic; cell-cycle shift; 12 shown): [[TNRC6C]] ⚠ 0.378× (z -12.9, 40/45 lines; toxic; cell-cycle shift (explains ~0% here)), [[AXL]] ⚠ 0.318× (z -11.2, 27/31 lines; toxic; cell-cycle shift (explains ~22% here)), [[H6PD]] ⚠ 0.293× (z -10.6, 34/43 lines; toxic; cell-cycle shift (explains ~0% here)), [[KIF4A]] ⚠ 0.326× (z -10.2, 38/44 lines; toxic; cell-cycle shift, explains ~39% of this change), [[TXNIP]] ⚠ 0.232× (z -10.0, 32/35 lines; toxic; cell-cycle shift (explains ~22% here)), [[MMUT]] ⚠ 0.400× (z -9.4, 36/44 lines; toxic; cell-cycle shift (explains ~0% here)), [[SCLT1]] ⚠ 0.418× (z -9.1, 37/45 lines; toxic; cell-cycle shift (explains ~18% here)), [[BIRC3]] ⚠ 0.370× (z -8.8, 38/40 lines; toxic; cell-cycle shift (explains ~20% here)), [[TMBIM4]] ⚠ 0.423× (z -8.8, 35/43 lines; toxic; cell-cycle shift (explains ~0% here)), [[ZNF395]] ⚠ 0.375× (z -8.6, 36/43 lines; toxic; cell-cycle shift (explains ~11% here)), [[LINC01572]] ⚠ 0.340× (z -8.4, 41/43 lines; toxic; cell-cycle shift (explains ~0% here)), [[SUN2]] ⚠ 0.465× (z -8.3, 31/44 lines; toxic; cell-cycle shift (explains ~19% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 060]] (+17.3), [[Module 072]] (+12.0), [[Module 064]] (+10.8) | [[Module 006]] (-6.6), [[Module 095]] (-5.5), [[Module 170]] (-4.9) |
| 0.5 µM | [[Module 060]] (+8.1), [[Module 072]] (+4.9), [[Module 064]] (+3.6) | [[Module 170]] (-2.9), [[Module 016]] (-2.7), [[Module 148]] (-2.6) |
| 5 µM | [[Module 060]] (+12.3), [[Module 135]] (+5.5), [[Module 072]] (+4.9) | [[Module 170]] (-4.8), [[Module 095]] (-4.2), [[Module 088]] (-3.5) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[SK-MEL-2 (line)]] (-6.0), [[PANC-1 (line)]] (-4.1), [[RPMI-7951 (line)]] (-3.8), [[CHP-212 (line)]] (-3.5), [[C32 (line)]] (-3.3) | [[H4 (line)]] (1.41), [[HT-29 (line)]] (1.33), [[COLO 205 (line)]] (1.29), [[MIA PaCa-2 (line)]] (1.19) · weakest: [[C-33 A (line)]] (0.656), [[NCI-H661 (line)]] (0.658), [[SHP-77 (line)]] (0.744) |
| 0.5 µM | [[H4 (line)]] (-3.2) | [[MIA PaCa-2 (line)]] (1.28), [[HOP62 (line)]] (1.26), [[C32 (line)]] (1.20), [[CFPAC-1 (line)]] (1.19) · weakest: [[NCI-H2122 (line)]] (0.516), [[AN3 CA (line)]] (0.543), [[SHP-77 (line)]] (0.628) |
| 5 µM | [[NCI-H1792 (line)]] (-8.5), [[RPMI-7951 (line)]] (-6.2), [[H4 (line)]] (-5.8), [[J82 (line)]] (-5.3), [[HS-578T (line)]] (-5.1) | [[SNU-423 (line)]] (1.14), [[CFPAC-1 (line)]] (1.13), [[H4 (line)]] (1.10), [[Panc 03.27 (line)]] (1.10) · weakest: [[SHP-77 (line)]] (0.704), [[AN3 CA (line)]] (0.818), [[RKO (line)]] (0.821) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Ixazomib citrate (drug)]] (+0.95, Proteasome inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Infigratinib (drug)]] (+0.40, Other TK inhibitor); [[Auranofin (drug)]] (+0.34, unclear); [[Hydroxyfasudil (drug)]] (+0.33, unclear); [[Macitentan (drug)]] (+0.30, unclear, ⚠ only 5 significant genes); [[Neratinib (maleate) (drug)]] (+0.30, EGFR/ERBB inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Clotrimazole (drug)]] (+0.29, unclear); [[Vinblastine (sulfate) (drug)]] (+0.28, Microtubule inhibitor); [[Belumosudil (mesylate) (drug)]] (+0.26, unclear); [[Lactate (calcium) (drug)]] (+0.26, unclear); [[Neratinib (drug)]] (+0.25, EGFR/ERBB inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 23 arrows, 23 of them with an alert ⚠; grade A 0, B 10, C 13. Shown: the 15 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[DOCK4]] | 0.05 µM | B | DOCK4 activity lowers the cells' numbers under Bortezomib 0.05 µM (makes them more sensitive) | lines that do not express DOCK4 (14) vs lines expressing it (34) | the lines without DOCK4: 1.33× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: STC2 |
| [[GNG11]] | 0.05 µM | B | GNG11 activity lowers the cells' numbers under Bortezomib 0.05 µM (makes them more sensitive) | lines that do not express GNG11 (21) vs lines expressing it (27) | the lines without GNG11: 1.34× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN |
| [[SNAP25]] | 0.05 µM | B | SNAP25 activity lowers the cells' numbers under Bortezomib 0.05 µM (makes them more sensitive) | lines that do not express SNAP25 (26) vs lines expressing it (22) | the lines without SNAP25: 1.30× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: EYA4, SPOCK1, DPYSL3 |
| [[SIPA1L2]] | 0.05 µM | B | SIPA1L2 activity lowers the cells' numbers under Bortezomib 0.05 µM (makes them more sensitive) | lines that do not express SIPA1L2 (10) vs lines expressing it (38) | the lines without SIPA1L2: 1.31× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ZNF594-DT, LINC02036, MGC4859; maybe low, not absent |
| [[FRMD4A]] | 0.05 µM | B | FRMD4A activity lowers the cells' numbers under Bortezomib 0.05 µM (makes them more sensitive) | lines that do not express FRMD4A (24) vs lines expressing it (24) | the lines without FRMD4A: 1.30× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[SMIM10]] | 0.05 µM | B | SMIM10 activity lowers the cells' numbers under Bortezomib 0.05 µM (makes them more sensitive) | lines that do not express SMIM10 (24) vs lines expressing it (24) | the lines without SMIM10: 1.23× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[BARX2]] | 0.5 µM | B | BARX2 activity raises the cells' numbers under Bortezomib 0.5 µM (protects the cells) | lines that do not express BARX2 (29) vs lines expressing it (19) | the lines without BARX2: 0.82× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |
| [[CA8]] | 0.05 µM | B | CA8 activity lowers the cells' numbers under Bortezomib 0.05 µM (makes them more sensitive) | lines that do not express CA8 (27) vs lines expressing it (21) | the lines without CA8: 1.22× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[TRIM9]] | 0.05 µM | B | TRIM9 activity lowers the cells' numbers under Bortezomib 0.05 µM (makes them more sensitive) | lines that do not express TRIM9 (16) vs lines expressing it (32) | the lines without TRIM9: 1.31× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1 |
| [[ENSG00000253642]] | 0.5 µM | B | ENSG00000253642 activity lowers the cells' numbers under Bortezomib 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000253642 (39) vs lines expressing it (9) | the lines without ENSG00000253642: 1.28× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ADGRG7, ENSG00000287211, ENSG00000287474 |
| [[SPART-AS1]] | 5 µM | C | SPART-AS1 activity lowers the cells' numbers under Bortezomib 5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.78× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[FIGN]] | 5 µM | C | FIGN activity lowers the cells' numbers under Bortezomib 5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.69× the cells of the other lines | 0.009 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[ENSG00000286964]] | 5 µM | C | ENSG00000286964 activity lowers the cells' numbers under Bortezomib 5 µM (makes them more sensitive) | lines that do not express ENSG00000286964 (10) vs lines expressing it (38) | the lines without ENSG00000286964: 1.78× the cells of the other lines | 0.021 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SIX1, C2orf74, SYDE1 |
| [[SETD7]] | 0.5 µM | C | SETD7 activity raises the cells' numbers under Bortezomib 0.5 µM (protects the cells) | lines that do not express SETD7 (3) vs lines expressing it (45) | the lines without SETD7: 0.73× the cells of the other lines | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |
| [[ENSG00000214265]], [[SNHG14]], [[SNRPN]] | 5 µM | C | ENSG00000214265, SNHG14, SNRPN activity lowers the cells' numbers under Bortezomib 5 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.69× the cells of the other lines | 0.024 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 493 arrows, 493 of them with an alert ⚠; grade A 0, B 493, C 0. Shown: the 15 strongest; 478 more arrows (478 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[PSMB5]] | [[BTG2]] | moves it that way too | B | PSMB5 activity raises BTG2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[EMSY-DT]] | moves it that way too | B | PSMB5 activity raises EMSY-DT's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[FAM200B]] | moves it that way too | B | PSMB5 activity raises FAM200B's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[GNAQ]] | moves it that way too | B | PSMB5 activity lowers GNAQ's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[GPR37]] | moves it that way too | B | PSMB5 activity raises GPR37's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[ISYNA1]] | moves it that way too | B | PSMB5 activity raises ISYNA1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[MYRIP]] | moves it that way too | B | PSMB5 activity raises MYRIP's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[NPTXR]] | moves it that way too | B | PSMB5 activity raises NPTXR's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[NT5C2]] | moves it that way too | B | PSMB5 activity lowers NT5C2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[PPIL2]] | moves it that way too | B | PSMB5 activity lowers PPIL2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[RFLNA]] | moves it that way too | B | PSMB5 activity raises RFLNA's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[RUFY2]] | moves it that way too | B | PSMB5 activity lowers RUFY2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[TRMT2B]] | moves it that way too | B | PSMB5 activity lowers TRMT2B's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[VARS2]] | moves it that way too | B | PSMB5 activity raises VARS2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | [[WWP1]] | moves it that way too | B | PSMB5 activity lowers WWP1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Bortezomib"
- `tables/drugdoses.parquet` — dd in 206, 207, 208
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
