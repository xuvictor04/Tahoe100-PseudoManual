---
drug: "Digitoxin"
type: "drug"
salt_base: "Digitoxin"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 9759
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Digitoxin

*unclear (unclear) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2869 / 8363 / 9759; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.81 / 0.86.
> Flags by dose: cell-cycle shift / cell-cycle shift / toxic; transcription drop; cell-cycle shift. ⚠ 0.05 µM: cell-cycle shift; 0.5 µM: cell-cycle shift; 5 µM: toxic; transcription drop; cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:B12 | 910 / 1,959 | — | -0.68 | +4.0/+5.2/+0.6 | ⚠ cell-cycle shift |
| 0.5 µM | [[Plate 11]]:B12 | 2,833 / 5,530 | — | +0.13 | +7.1/+6.1/+3.3 | ⚠ cell-cycle shift |
| 5 µM | [[Plate 12]]:B12 | 4,790 / 4,969 | — | -1.51 | +9.6/+8.0/+7.0 | ⚠ toxic; transcription drop; cell-cycle shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (910 genes, 422 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 16 shown): [[DIAPH1]] 1.42× (z +10.4, 32/47 lines; cell-cycle shift (explains ~16% here)), [[CAB39L]] 1.56× (z +9.3, 37/47 lines; cell-cycle shift (explains ~0% here)), [[PAXBP1]] 1.49× (z +9.3, 32/47 lines; cell-cycle shift (explains ~5% here)), [[NDC80]] ⚠ 1.77× (z +8.9, 36/44 lines; cell-cycle shift, explains ~53% of this change), [[WDR62]] ⚠ 1.83× (z +8.9, 37/45 lines; cell-cycle shift, explains ~36% of this change), [[B3GALNT2]] 1.50× (z +8.7, 39/47 lines; cell-cycle shift (explains ~10% here)), [[NUDT3]] 1.37× (z +8.6, 28/47 lines; cell-cycle shift (explains ~0% here)), [[PRDM15]] 1.67× (z +8.6, 34/46 lines; cell-cycle shift (explains ~0% here)), [[BUB1B]] ⚠ 1.74× (z +8.2, 36/45 lines; cell-cycle shift, explains ~45% of this change), [[MED13]] 1.34× (z +8.1, 34/47 lines; cell-cycle shift (explains ~0% here)), [[CEP85]] 1.54× (z +8.1, 31/47 lines; cell-cycle shift (explains ~24% here)), [[CEP152]] ⚠ 1.35× (z +7.9, 32/47 lines; cell-cycle shift, explains ~29% of this change), [[XPO5]] 1.44× (z +7.9, 34/47 lines; cell-cycle shift (explains ~14% here)), [[ASH1L]] 1.23× (z +7.6, 26/47 lines; cell-cycle shift (explains ~0% here)), [[KAT6A]] 1.29× (z +7.5, 31/47 lines; cell-cycle shift (explains ~2% here)), [[ZFPM2-AS1]] 1.49× (z +7.5, 23/31 lines; cell-cycle shift (explains ~5% here))

**0.5 µM** (2833 genes, 968 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[ZFPM2-AS1]] 3.49× (z +23.2, 32/32 lines; cell-cycle shift (explains ~1% here)), [[ASH1L]] 1.82× (z +22.2, 48/48 lines; cell-cycle shift (explains ~0% here)), [[DIAPH1]] 2.13× (z +22.2, 46/48 lines; cell-cycle shift (explains ~11% here)), [[ADNP2]] 2.15× (z +19.9, 46/48 lines; cell-cycle shift (explains ~8% here)), [[MED13]] 2.02× (z +19.3, 48/48 lines; cell-cycle shift (explains ~0% here)), [[B3GALNT2]] 2.45× (z +19.2, 47/48 lines; cell-cycle shift (explains ~9% here)), [[KAT6A]] 1.89× (z +18.9, 48/48 lines; cell-cycle shift (explains ~1% here)), [[NIPBL]] 1.60× (z +18.7, 45/48 lines; cell-cycle shift (explains ~1% here)), [[CAB39L]] 2.42× (z +18.6, 47/48 lines; cell-cycle shift (explains ~0% here)), [[ARMH4]] 1.68× (z +17.3, 45/48 lines; cell-cycle shift (explains ~2% here)), [[CRAMP1]] 2.43× (z +17.2, 47/48 lines; cell-cycle shift (explains ~5% here)), [[ARRDC4]] 2.96× (z +16.9, 37/40 lines; cell-cycle shift (explains ~11% here))

**5 µM** (4790 genes, 4,790 with an alert ⚠; the drug-dose carries ⚠ toxic; transcription drop; cell-cycle shift; 12 shown): [[ASH1L]] ⚠ 2.12× (z +28.0, 48/48 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[ZFPM2-AS1]] ⚠ 4.06× (z +26.1, 32/32 lines; toxic; transcription drop; cell-cycle shift (explains ~2% here)), [[RBM15]] ⚠ 3.54× (z +25.7, 47/47 lines; toxic; transcription drop; cell-cycle shift (explains ~16% here)), [[ADNP2]] ⚠ 2.67× (z +25.6, 47/47 lines; toxic; transcription drop; cell-cycle shift (explains ~9% here)), [[NIPBL]] ⚠ 1.86× (z +24.5, 48/48 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[B3GALNT2]] ⚠ 3.11× (z +24.3, 43/47 lines; toxic; transcription drop; cell-cycle shift (explains ~11% here)), [[DIAPH1]] ⚠ 2.21× (z +23.5, 48/48 lines; toxic; transcription drop; cell-cycle shift (explains ~14% here)), [[CAB39L]] ⚠ 2.94× (z +22.7, 47/47 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[AKAP8L]] ⚠ 2.37× (z +22.4, 48/48 lines; toxic; transcription drop; cell-cycle shift (explains ~15% here)), [[KPNA6]] ⚠ 2.14× (z +22.3, 47/48 lines; toxic; transcription drop; cell-cycle shift (explains ~16% here)), [[PIP5K1A]] ⚠ 2.57× (z +21.9, 48/48 lines; toxic; transcription drop; cell-cycle shift (explains ~0% here)), [[MCTP1]] ⚠ 3.70× (z +21.9, 33/35 lines; toxic; transcription drop; cell-cycle shift (explains ~12% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1959 genes, 669 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 14 shown): [[ARHGAP44]] 0.648× (z -9.9, 20/31 lines; cell-cycle shift (explains ~16% here)), [[MMP17]] 0.439× (z -9.5, 18/24 lines; cell-cycle shift (explains ~3% here)), [[MAPT]] 0.604× (z -9.0, 25/37 lines; cell-cycle shift (explains ~8% here)), [[CALD1]] 0.650× (z -8.8, 28/33 lines; cell-cycle shift (explains ~0% here)), [[PLEKHH2]] 0.648× (z -8.6, 17/33 lines; cell-cycle shift (explains ~17% here)), [[FBXO16]] 0.520× (z -8.2, 26/38 lines; cell-cycle shift (explains ~19% here)), [[ECHDC2]] ⚠ 0.628× (z -8.2, 25/34 lines; cell-cycle shift, explains ~31% of this change), [[SMARCD3]] 0.602× (z -8.1, 25/43 lines; cell-cycle shift (explains ~14% here)), [[VASH1]] 0.416× (z -7.8, 19/30 lines; cell-cycle shift (explains ~10% here)), [[KLHL32]] 0.495× (z -7.7, 18/30 lines; cell-cycle shift (explains ~8% here)), [[SOX2-OT]] 0.566× (z -7.7, 30/45 lines; cell-cycle shift (explains ~10% here)), [[LMBRD1]] ⚠ 0.717× (z -7.7, 29/47 lines; cell-cycle shift, explains ~27% of this change), [[SLC24A1]] 0.559× (z -7.7, 28/47 lines; cell-cycle shift (explains ~19% here)), [[RNF150]] 0.563× (z -7.6, 20/31 lines; cell-cycle shift (explains ~13% here))

**0.5 µM** (5530 genes, 1,554 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[ATG4C]] 0.343× (z -23.8, 44/47 lines; cell-cycle shift (explains ~3% here)), [[ZNF25]] 0.261× (z -21.2, 45/47 lines; cell-cycle shift (explains ~14% here)), [[SLC2A10]] 0.164× (z -20.0, 27/30 lines; cell-cycle shift (explains ~14% here)), [[CCDC7]] 0.245× (z -19.9, 45/46 lines; cell-cycle shift (explains ~16% here)), [[CEP63]] 0.472× (z -19.5, 44/48 lines; cell-cycle shift (explains ~0% here)), [[ARHGAP44]] 0.424× (z -19.5, 29/32 lines; cell-cycle shift (explains ~5% here)), [[ZMYND8]] 0.370× (z -19.4, 46/47 lines; cell-cycle shift (explains ~11% here)), [[RAD51B]] 0.229× (z -19.1, 48/48 lines; cell-cycle shift (explains ~14% here)), [[SDCCAG8]] 0.364× (z -18.8, 48/48 lines; cell-cycle shift (explains ~9% here)), [[GOLGA1]] 0.453× (z -18.8, 47/48 lines; cell-cycle shift (explains ~15% here)), [[CBR4]] 0.413× (z -18.7, 46/48 lines; cell-cycle shift (explains ~9% here)), [[FBXO16]] 0.237× (z -18.4, 38/39 lines; cell-cycle shift (explains ~9% here))

**5 µM** (4969 genes, 4,969 with an alert ⚠; the drug-dose carries ⚠ toxic; transcription drop; cell-cycle shift; 12 shown): [[ATG4C]] ⚠ 0.272× (z -29.0, 39/46 lines; toxic; transcription drop; cell-cycle shift (explains ~3% here)), [[CCDC7]] ⚠ 0.163× (z -25.8, 44/46 lines; toxic; transcription drop; cell-cycle shift (explains ~17% here)), [[SCAMP1]] ⚠ 0.385× (z -25.2, 46/48 lines; toxic; transcription drop; cell-cycle shift (explains ~18% here)), [[FAM114A1]] ⚠ 0.312× (z -24.4, 46/46 lines; toxic; transcription drop; cell-cycle shift, explains ~27% of this change), [[ZNF248]] ⚠ 0.273× (z -24.1, 47/48 lines; toxic; transcription drop; cell-cycle shift (explains ~20% here)), [[ARHGAP44]] ⚠ 0.352× (z -23.8, 29/30 lines; toxic; transcription drop; cell-cycle shift (explains ~5% here)), [[EFCAB11]] ⚠ 0.278× (z -23.7, 48/48 lines; toxic; transcription drop; cell-cycle shift (explains ~1% here)), [[BABAM2]] ⚠ 0.280× (z -23.3, 48/48 lines; toxic; transcription drop; cell-cycle shift (explains ~24% here)), [[LINC02649]] ⚠ 0.192× (z -22.9, 43/45 lines; toxic; transcription drop; cell-cycle shift (explains ~21% here)), [[PPARA]] ⚠ 0.355× (z -22.8, 42/47 lines; toxic; transcription drop; cell-cycle shift (explains ~17% here)), [[TMEM182]] ⚠ 0.247× (z -22.4, 45/46 lines; toxic; transcription drop; cell-cycle shift (explains ~16% here)), [[SMARCAL1]] ⚠ 0.256× (z -22.4, 47/48 lines; toxic; transcription drop; cell-cycle shift (explains ~21% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 194]] (+4.5), [[Module 124]] (+2.9), [[Module 022]] (+2.9) | [[Module 208]] (-3.5), [[Module 059]] (-3.4), [[Module 064]] (-3.2) |
| 0.5 µM | [[Module 095]] (+7.2), [[Module 214]] (+6.2), [[Module 124]] (+5.6) | [[Module 200]] (-9.3), [[Module 146]] (-8.7), [[Module 065]] (-8.4) |
| 5 µM | [[Module 095]] (+11.9), [[Module 068]] (+8.3), [[Module 214]] (+7.8) | [[Module 200]] (-12.5), [[Module 052]] (-12.4), [[Module 230]] (-9.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[HOP62 (line)]] (-6.1), [[NCI-H23 (line)]] (-5.5), [[NCI-H2030 (line)]] (-5.1), [[HS-578T (line)]] (-4.8), [[SNU-423 (line)]] (-4.1) | [[H4 (line)]] (2.11), [[NCI-H460 (line)]] (2.09), [[SW480 (line)]] (1.72), [[PANC-1 (line)]] (1.62) · weakest: [[NCI-H2347 (line)]] (0.418), [[Panc 03.27 (line)]] (0.444), [[AsPC-1 (line)]] (0.452) |
| 0.5 µM | [[KATO III (line)]] (-6.0), [[LOX-IMVI (line)]] (-5.9), [[NCI-H460 (line)]] (-5.5), [[SW 900 (line)]] (-5.2), [[H4 (line)]] (-3.5) | [[PANC-1 (line)]] (1.49), [[SW480 (line)]] (1.49), [[H4 (line)]] (1.47), [[NCI-H23 (line)]] (1.33) · weakest: [[A498 (line)]] (0.499), [[HEC-1-A (line)]] (0.520), [[SW 1088 (line)]] (0.545) |
| 5 µM | [[KATO III (line)]] (-9.3), [[NCI-H460 (line)]] (-6.2), [[Hs 766T (line)]] (-5.5), [[SHP-77 (line)]] (-4.5), [[RKO (line)]] (-4.3) | [[PANC-1 (line)]] (1.38), [[NCI-H460 (line)]] (1.36), [[SW480 (line)]] (1.33), [[HOP62 (line)]] (1.27) · weakest: [[A498 (line)]] (0.471), [[SW 1088 (line)]] (0.528), [[NCI-H2347 (line)]] (0.639) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: toxic; transcription drop; cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Ouabain (Octahydrate) (drug)]] (+0.82, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Elagolix sodium (drug)]] (+0.40, unclear); [[Decitabine (drug)]] (+0.37, DNA methyltransferase inhibitor); [[Bimatoprost (drug)]] (+0.35, unclear); [[Bergenin (drug)]] (+0.33, unclear); [[Sunitinib (drug)]] (+0.32, Multi-TK inhibitor, ⚠ vector dose flagged: toxic); [[Dexmedetomidine (drug)]] (+0.32, Adrenoceptor agonist, ⚠ only 9 significant genes); [[Allantoin (drug)]] (+0.31, unclear); [[Flutamide (drug)]] (+0.31, Androgen receptor antagonist); [[Bicalutamide (drug)]] (+0.30, Androgen receptor antagonist); [[Vitamin K4 (drug)]] (+0.29, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 30 arrows, 30 of them with an alert ⚠; grade A 0, B 18, C 12. Shown: the 15 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MYH14]] | 0.05 µM | B | MYH14 activity raises the cells' numbers under Digitoxin 0.05 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.60× the cells of the other lines | 0.030 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[KCNMA1]] | 0.05 µM | B | KCNMA1 activity lowers the cells' numbers under Digitoxin 0.05 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.64× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[ENSG00000230615]] | 0.05 µM | B | ENSG00000230615 activity lowers the cells' numbers under Digitoxin 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000230615 (25) vs lines expressing it (23) | the lines without ENSG00000230615: 1.66× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: FRMD4A, ENSG00000253891, SRGN; maybe low, not absent |
| [[ENSG00000230647]] | 0.05 µM | B | ENSG00000230647 activity lowers the cells' numbers under Digitoxin 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.51× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[ST6GAL1]] | 5 µM | B | ST6GAL1 activity raises the cells' numbers under Digitoxin 5 µM (protects the cells) | lines that do not express ST6GAL1 (14) vs lines expressing it (34) | the lines without ST6GAL1: 0.77× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent |
| [[DSP]] | 0.5 µM | B | DSP activity raises the cells' numbers under Digitoxin 0.5 µM (protects the cells) | lines that do not express DSP (17) vs lines expressing it (31) | the lines without DSP: 0.83× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, GRB7, SFN; maybe low, not absent |
| [[SRGN]] | 0.05 µM | B | SRGN activity lowers the cells' numbers under Digitoxin 0.05 µM (makes them more sensitive) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 1.78× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| [[EPCAM]] | 0.05 µM | B | EPCAM activity raises the cells' numbers under Digitoxin 0.05 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.65× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[AOX1]] | 0.05 µM | B | AOX1 activity lowers the cells' numbers under Digitoxin 0.05 µM (makes them more sensitive) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 1.51× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[NLGN4X]] | 0.05 µM | B | NLGN4X activity raises the cells' numbers under Digitoxin 0.05 µM (protects the cells) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 0.82× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| [[ERBB3]] | 0.05 µM | B | ERBB3 activity raises the cells' numbers under Digitoxin 0.05 µM (protects the cells) | lines that do not express ERBB3 (27) vs lines expressing it (21) | the lines without ERBB3: 0.65× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[DNAH11]] | 0.05 µM | B | DNAH11 activity lowers the cells' numbers under Digitoxin 0.05 µM (makes them more sensitive) | lines that do not express DNAH11 (23) vs lines expressing it (25) | the lines without DNAH11: 1.46× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| [[KCNMA1]] | 0.5 µM | B | KCNMA1 activity lowers the cells' numbers under Digitoxin 0.5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.24× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[SLFN5]] | 0.05 µM | B | SLFN5 activity lowers the cells' numbers under Digitoxin 0.05 µM (makes them more sensitive) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 1.53× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[AP1M2]] | 5 µM | B | AP1M2 activity raises the cells' numbers under Digitoxin 5 µM (protects the cells) | lines that do not express AP1M2 (24) vs lines expressing it (24) | the lines without AP1M2: 0.80× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Digitoxin"
- `tables/drugdoses.parquet` — dd in 353, 354, 355
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
