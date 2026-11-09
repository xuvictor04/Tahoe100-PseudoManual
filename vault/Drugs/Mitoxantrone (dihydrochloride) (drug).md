---
drug: "Mitoxantrone (dihydrochloride)"
type: "drug"
salt_base: "Mitoxantrone"
targets: "TOP2A, TOP2B, PRKCA"
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 4951
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Mitoxantrone (dihydrochloride)

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · targets: TOP2A, TOP2B, PRKCA · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 21 / 512 / 4951; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.57 / 0.56.
> Flags by dose: - / cell-cycle shift / -. ⚠ 0.5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:E8 | 19 / 2 | — | -0.68 | +1.0/-0.7/-0.5 | — |
| 0.5 µM | [[Plate 05]]:E8 | 359 / 153 | — | -0.19 | +1.3/-4.5/-1.1 | ⚠ cell-cycle shift |
| 5 µM | [[Plate 14]]:E8 | 3,807 / 1,144 | 0.714 | -0.56 | +5.8/-0.5/+2.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (19 genes, none with an alert; 12 shown): [[NTN1]] 1.27× (z +4.2, 8/30 lines), [[CYFIP2]] 1.26× (z +4.1, 13/37 lines), [[ENSG00000269237]] 1.33× (z +3.9, 5/39 lines), [[GRIN2C]] 1.61× (z +3.8, 11/30 lines), [[ACER2]] 1.31× (z +3.7, 10/46 lines), [[ZMAT3]] 1.25× (z +3.7, 17/42 lines), [[TMED6]] 1.38× (z +3.4, 2/41 lines), [[ZNF385C]] 1.34× (z +3.4, 1/36 lines), [[PID1]] 1.25× (z +3.2, 3/26 lines), [[S1PR3]] 1.37× (z +3.1, 5/26 lines), [[FAS]] 1.22× (z +3.1, 10/40 lines), [[FDXR]] 1.36× (z +3.0, 11/38 lines)

**0.5 µM** (359 genes, 235 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 14 shown): [[DYRK3]] 1.87× (z +8.7, 33/41 lines; cell-cycle shift (explains ~7% here)), [[H2BC5]] 2.00× (z +7.8, 35/47 lines; cell-cycle shift (explains ~0% here)), [[RAB30-DT]] 1.86× (z +7.7, 45/48 lines; cell-cycle shift (explains ~6% here)), [[H2BC6]] 2.07× (z +7.6, 31/43 lines; cell-cycle shift (explains ~0% here)), [[ZMAT3]] 1.55× (z +7.4, 22/42 lines; cell-cycle shift (explains ~15% here)), [[MDM2]] 1.39× (z +7.0, 31/49 lines; cell-cycle shift (explains ~14% here)), [[DHRS12]] 1.72× (z +6.8, 24/46 lines; cell-cycle shift (explains ~7% here)), [[LINC00880]] 2.46× (z +6.5, 20/38 lines; cell-cycle shift (explains ~7% here)), [[ENSG00000286319]] 1.93× (z +6.5, 21/42 lines; cell-cycle shift (explains ~9% here)), [[NTN1]] ⚠ 1.43× (z +6.3, 12/30 lines; cell-cycle shift, explains ~30% of this change), [[PTCHD4]] 1.82× (z +6.2, 13/15 lines; cell-cycle shift (explains ~3% here)), [[FBF1]] ⚠ 1.53× (z +6.2, 22/45 lines; cell-cycle shift, explains ~31% of this change), [[PLA2G4C]] 1.49× (z +6.0, 19/44 lines; cell-cycle shift (explains ~2% here)), [[ENSG00000273507]] 1.81× (z +6.0, 16/43 lines; cell-cycle shift (explains ~16% here))

**5 µM** (3807 genes, none with an alert; 12 shown): [[MMADHC-DT]] 4.19× (z +25.1, 41/46 lines), [[ADAMTS17]] 2.93× (z +22.2, 27/32 lines), [[ARRDC3-AS1]] 3.29× (z +20.9, 44/48 lines), [[BHLHE40-AS1]] 2.43× (z +20.5, 36/47 lines), [[LINC01829]] 3.36× (z +20.0, 38/45 lines), [[ENSG00000229021]] 3.63× (z +20.0, 40/46 lines), [[H2BC6]] 3.72× (z +19.3, 38/48 lines), [[ENSG00000289156]] 3.28× (z +19.1, 35/45 lines), [[LINC00880]] 6.21× (z +18.7, 35/41 lines), [[STPG4]] 3.40× (z +18.6, 38/46 lines), [[DPF3]] 2.75× (z +18.5, 28/34 lines), [[SIAH2-AS1]] 4.16× (z +17.9, 27/44 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[CDCA3]] 0.729× (z -3.2, 14/43 lines), [[DHRS2]] 0.632× (z -3.2, 10/32 lines)

**0.5 µM** (153 genes, 119 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 24 shown): [[PIF1]] ⚠ 0.519× (z -8.2, 25/45 lines; cell-cycle shift, explains ~50% of this change), [[KIF20A]] ⚠ 0.509× (z -7.4, 25/46 lines; cell-cycle shift, explains ~57% of this change), [[PLK1]] ⚠ 0.591× (z -6.9, 30/46 lines; cell-cycle shift, explains ~63% of this change), [[CENPE]] ⚠ 0.674× (z -6.8, 30/49 lines; cell-cycle shift, explains ~79% of this change), [[GPSM2]] ⚠ 0.719× (z -6.8, 25/48 lines; cell-cycle shift, explains ~52% of this change), [[CCNF]] ⚠ 0.661× (z -6.8, 26/47 lines; cell-cycle shift, explains ~60% of this change), [[CENPA]] ⚠ 0.749× (z -6.6, 25/48 lines; cell-cycle shift, explains ~46% of this change), [[KIF2C]] ⚠ 0.631× (z -6.4, 31/46 lines; cell-cycle shift, explains ~57% of this change), [[DEPDC1B]] ⚠ 0.726× (z -6.2, 21/48 lines; cell-cycle shift, explains ~38% of this change), [[AURKA]] ⚠ 0.634× (z -6.2, 23/48 lines; cell-cycle shift, explains ~71% of this change), [[TROAP]] ⚠ 0.662× (z -6.0, 23/46 lines; cell-cycle shift, explains ~49% of this change), [[FAM83D]] ⚠ 0.658× (z -6.0, 25/48 lines; cell-cycle shift, explains ~49% of this change), [[FLNB]] 0.800× (z -4.5, 25/46 lines; cell-cycle shift (explains ~6% here)), [[KLHL13]] 0.746× (z -4.4, 6/24 lines; cell-cycle shift (explains ~0% here)), [[EEF2K]] 0.831× (z -4.3, 18/48 lines; cell-cycle shift (explains ~0% here)), [[CAMKK1]] 0.703× (z -4.2, 17/43 lines; cell-cycle shift (explains ~4% here)), [[ABCC4]] 0.810× (z -3.9, 17/46 lines; cell-cycle shift (explains ~0% here)), [[KIF21B]] 0.682× (z -3.8, 10/34 lines; cell-cycle shift (explains ~0% here)), [[GFPT1]] 0.817× (z -3.8, 24/49 lines; cell-cycle shift (explains ~1% here)), [[HERPUD1]] 0.695× (z -3.7, 34/49 lines; cell-cycle shift (explains ~9% here)), [[PEMT]] 0.804× (z -3.7, 13/46 lines; cell-cycle shift (explains ~0% here)), [[VSIG10L]] 0.702× (z -3.6, 11/36 lines; cell-cycle shift (explains ~0% here)), [[LINC01950]] 0.720× (z -3.6, 13/33 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000228793]] 0.728× (z -3.5, 8/40 lines; cell-cycle shift (explains ~20% here))

**5 µM** (1144 genes, none with an alert; 12 shown): [[TPD52]] 0.614× (z -14.4, 45/46 lines), [[PPA2]] 0.703× (z -13.6, 43/48 lines), [[DOCK6]] 0.587× (z -13.6, 46/48 lines), [[ZNF652]] 0.697× (z -13.2, 40/48 lines), [[RHPN2]] 0.656× (z -12.6, 34/44 lines), [[NBN]] 0.670× (z -12.6, 37/48 lines), [[CHD1L]] 0.604× (z -12.5, 44/48 lines), [[GALNT11]] 0.641× (z -12.4, 37/46 lines), [[FAM114A1]] 0.659× (z -12.3, 42/46 lines), [[BBS5]] 0.560× (z -12.3, 30/42 lines), [[KIF13A]] 0.709× (z -12.2, 37/47 lines), [[RBAK-RBAKDN]] 0.710× (z -12.2, 42/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 194]] (+3.9), [[Module 170]] (+3.5), [[Module 062]] (+2.9) | [[Module 022]] (-2.4), [[Module 085]] (-2.1) |
| 5 µM | [[Module 026]] (+10.0), [[Module 194]] (+9.9), [[Module 095]] (+8.1) | [[Module 085]] (-9.1), [[Module 030]] (-6.3), [[Module 077]] (-6.2) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[NCI-H2030 (line)]] (-3.2) | [[SNU-1 (line)]] (3.10), [[A549 (line)]] (1.93), [[SW48 (line)]] (1.86), [[LOX-IMVI (line)]] (1.85) · weakest: [[NCI-H661 (line)]] (-0.0821), [[Hs 766T (line)]] (0.128), [[SW1417 (line)]] (0.160) |
| 0.5 µM | [[CHP-212 (line)]] (-4.2), [[NCI-H2030 (line)]] (-3.3) | [[A-172 (line)]] (2.20), [[SNU-1 (line)]] (2.02), [[A549 (line)]] (2.00), [[H4 (line)]] (1.76) · weakest: [[NCI-H23 (line)]] (0.298), [[AsPC-1 (line)]] (0.339), [[KATO III (line)]] (0.419) |
| 5 µM | [[A-427 (line)]] (-8.3), [[A-172 (line)]] (-6.1), [[SNU-1 (line)]] (-5.9), [[HOP62 (line)]] (-4.6), [[LOX-IMVI (line)]] (-4.3) | [[HOP62 (line)]] (1.77), [[A-172 (line)]] (1.75), [[SNU-1 (line)]] (1.54), [[HS-578T (line)]] (1.37) · weakest: [[SHP-77 (line)]] (0.327), [[NCI-H23 (line)]] (0.450), [[NCI-H1573 (line)]] (0.466) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Doxorubicin (hydrochloride) (drug)]] (+0.71, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] (+0.70, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] (+0.68, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Nafamostat (mesylate) (drug)]] (+0.65, unclear, ⚠ only 3 significant genes); [[Meloxicam (drug)]] (+0.63, Cyclooxygenase inhibitor); [[Abiraterone acetate (drug)]] (+0.62, unclear); [[Brimonidine (drug)]] (+0.60, Adrenoceptor agonist); [[Demeclocycline (drug)]] (+0.58, unclear); [[Esmolol (hydrochloride) (drug)]] (+0.58, unclear); [[Vitamin K4 (drug)]] (+0.55, unclear); [[Benztropine (mesylate) (drug)]] (+0.54, unclear); [[Filgotinib (drug)]] (+0.52, JAK/STAT inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 22 arrows, 22 of them with an alert ⚠; grade A 0, B 12, C 10. Shown: the 15 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000256982]] | 5 µM | B | ENSG00000256982 activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 5 µM (protects the cells) | lines that do not express ENSG00000256982 (18) vs lines expressing it (30) | the lines without ENSG00000256982: 0.74× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ADAM28, LYPD3 |
| [[LINC00482]] | 5 µM | B | LINC00482 activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 5 µM (protects the cells) | lines that do not express LINC00482 (8) vs lines expressing it (40) | the lines without LINC00482: 0.79× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SOX13, SEPTIN9-DT |
| [[ENSG00000260710]] | 0.5 µM | B | ENSG00000260710 activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 0.5 µM (protects the cells) | lines that do not express ENSG00000260710 (19) vs lines expressing it (29) | the lines without ENSG00000260710: 0.80× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: LAD1, TRIM29, NOS3; maybe low, not absent |
| [[C11orf52]] | 5 µM | B | C11orf52 activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 5 µM (protects the cells) | lines that do not express C11orf52 (23) vs lines expressing it (25) | the lines without C11orf52: 0.75× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[CLDN10-AS1]] | 5 µM | B | CLDN10-AS1 activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 5 µM (protects the cells) | lines that do not express CLDN10-AS1 (31) vs lines expressing it (17) | the lines without CLDN10-AS1: 0.74× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ADGRD1, AMBP, NPSR1-AS1 |
| [[AGMAT]] | 5 µM | B | AGMAT activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 5 µM (protects the cells) | lines that do not express AGMAT (11) vs lines expressing it (37) | the lines without AGMAT: 0.71× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ETV7, LYPD5, TNK1; maybe low, not absent |
| [[TBC1D8]] | 5 µM | B | TBC1D8 activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 5 µM (protects the cells) | lines that do not express TBC1D8 (6) vs lines expressing it (42) | the lines without TBC1D8: 0.71× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[MGC32805]] | 5 µM | B | MGC32805 activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 5 µM (protects the cells) | lines that do not express MGC32805 (32) vs lines expressing it (16) | the lines without MGC32805: 0.74× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: CEACAM5, ST18, PRR15L; maybe low, not absent |
| [[TMEM45B]] | 5 µM | B | TMEM45B activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 5 µM (protects the cells) | lines that do not express TMEM45B (32) vs lines expressing it (16) | the lines without TMEM45B: 0.76× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[ENSG00000287003]] | 5 µM | B | ENSG00000287003 activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 5 µM (protects the cells) | lines that do not express ENSG00000287003 (20) vs lines expressing it (28) | the lines without ENSG00000287003: 0.77× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: TMEM154, ALOX5, RASSF6 |
| [[FAT4]] | 0.5 µM | B | FAT4 activity lowers the cells' numbers under Mitoxantrone (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express FAT4 (20) vs lines expressing it (28) | the lines without FAT4: 1.21× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11 |
| [[NCALD]] | 5 µM | B | NCALD activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 5 µM (protects the cells) | lines that do not express NCALD (18) vs lines expressing it (30) | the lines without NCALD: 0.76× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[VRK2]] | 0.5 µM | C | VRK2 activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 0.5 µM (protects the cells) | lines that do not express VRK2 (4) vs lines expressing it (44) | the lines without VRK2: 0.64× the cells of the other lines | 0.002 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PTER, ZC3HAV1L, OSR2 |
| [[STX1A]] | 5 µM | C | STX1A activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 5 µM (protects the cells) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 0.47× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| [[PYGB]] | 5 µM | C | PYGB activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 5 µM (protects the cells) | lines that do not express PYGB (3) vs lines expressing it (45) | the lines without PYGB: 0.57× the cells of the other lines | 0.013 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 4,295 arrows, 4,295 of them with an alert ⚠; grade A 0, B 4,295, C 0. Shown: the 15 strongest; 4,280 more arrows (4,280 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[TOP2A]] | [[G2E3]] | moves it that way too | B | TOP2A activity raises G2E3's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.5% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[RABL2B]] | moves it that way too | B | TOP2A activity lowers RABL2B's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.8% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[RASSF8-AS1]] | moves it that way too | B | TOP2A activity lowers RASSF8-AS1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.8% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ENSG00000285667]] | moves it that way too | B | TOP2A activity lowers ENSG00000285667's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.1% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[LRRIQ3]] | moves it that way too | B | TOP2A activity lowers LRRIQ3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.1% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[BAX]] | moves it that way too | B | TOP2A activity lowers BAX's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[CIBAR1-DT]] | moves it that way too | B | TOP2A activity lowers CIBAR1-DT's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ENSG00000287400]] | moves it that way too | B | TOP2A activity lowers ENSG00000287400's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[MIDEAS]] | moves it that way too | B | TOP2A activity raises MIDEAS's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[TARID]] | moves it that way too | B | TOP2A activity lowers TARID's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ZNF665]] | moves it that way too | B | TOP2A activity lowers ZNF665's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[AK1]] | moves it that way too | B | TOP2A activity lowers AK1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[CAMKK1]] | moves it that way too | B | TOP2A activity raises CAMKK1's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ENSG00000228566]] | moves it that way too | B | TOP2A activity lowers ENSG00000228566's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[FCGBP]] | moves it that way too | B | TOP2A activity lowers FCGBP's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Mitoxantrone (dihydrochloride)"
- `tables/drugdoses.parquet` — dd in 690, 691, 692
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
