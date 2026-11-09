---
drug: "Cytarabine"
type: "drug"
salt_base: "Cytarabine"
targets: ""
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 371
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Cytarabine

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 70 / 150 / 371; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.49 / 0.57.
> Flags by dose: - / cell-cycle shift / cell-cycle shift. ⚠ 0.5 µM: cell-cycle shift; 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:B9 | 29 / 41 | — | +0.40 | +2.5/-2.5/-0.9 | — |
| 0.5 µM | [[Plate 08]]:B9 | 77 / 73 | — | +0.73 | +4.7/-3.6/+0.4 | ⚠ cell-cycle shift |
| 5 µM | [[Plate 09]]:B9 | 222 / 149 | — | -0.55 | +3.9/-4.8/-0.6 | ⚠ cell-cycle shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (29 genes, none with an alert; 12 shown): [[ATAD5]] 1.33× (z +4.8, 25/48 lines), [[CCNE2]] 1.50× (z +4.7, 11/46 lines), [[ZGRF1]] 1.25× (z +4.2, 13/48 lines), [[KAT2B]] 1.23× (z +4.0, 10/47 lines), [[HROB]] 1.30× (z +4.0, 9/46 lines), [[ATAD2]] 1.24× (z +3.8, 23/47 lines), [[DSN1]] 1.28× (z +3.8, 13/48 lines), [[FANCI]] 1.28× (z +3.8, 21/48 lines), [[SORBS1]] 1.24× (z +3.8, 6/41 lines), [[PLEKHH2]] 1.21× (z +3.6, 5/34 lines), [[E2F7]] 1.23× (z +3.5, 10/43 lines), [[WDHD1]] 1.21× (z +3.5, 14/48 lines)

**0.5 µM** (77 genes, 75 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 14 shown): [[CCNE2]] ⚠ 1.71× (z +6.7, 22/47 lines; cell-cycle shift, explains ~71% of this change), [[E2F7]] ⚠ 1.36× (z +5.6, 23/43 lines; cell-cycle shift, explains ~52% of this change), [[ZGRF1]] ⚠ 1.28× (z +5.0, 13/48 lines; cell-cycle shift, explains ~55% of this change), [[DNA2]] ⚠ 1.31× (z +5.0, 24/48 lines; cell-cycle shift, explains ~96% of this change), [[BRIP1]] ⚠ 1.44× (z +5.0, 32/47 lines; cell-cycle shift, explains ~71% of this change), [[WDHD1]] ⚠ 1.28× (z +4.9, 19/48 lines; cell-cycle shift, explains ~99% of this change), [[ATAD2]] ⚠ 1.29× (z +4.8, 21/47 lines; cell-cycle shift, explains ~69% of this change), [[WDR76]] ⚠ 1.39× (z +4.8, 12/46 lines; cell-cycle shift, explains ~99% of this change), [[FANCB]] ⚠ 1.28× (z +4.8, 18/48 lines; cell-cycle shift, explains ~97% of this change), [[MCM8]] ⚠ 1.34× (z +4.8, 26/48 lines; cell-cycle shift, would explain all of this change), [[POLA2]] ⚠ 1.31× (z +4.8, 11/48 lines; cell-cycle shift, explains ~92% of this change), [[MIR924HG]] ⚠ 1.46× (z +4.7, 28/40 lines; cell-cycle shift, explains ~66% of this change), [[TMEM40]] 1.56× (z +3.4, 5/24 lines; cell-cycle shift (explains ~0% here)), [[CDKN1A]] 1.25× (z +3.3, 15/45 lines; cell-cycle shift (explains ~0% here))

**5 µM** (222 genes, 174 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 24 shown): [[ZGRF1]] ⚠ 1.42× (z +6.8, 24/48 lines; cell-cycle shift, explains ~33% of this change), [[E2F7]] ⚠ 1.47× (z +6.7, 24/43 lines; cell-cycle shift, explains ~38% of this change), [[NTN1]] ⚠ 1.48× (z +6.7, 18/30 lines; cell-cycle shift, explains ~41% of this change), [[LIG1]] ⚠ 1.44× (z +6.1, 29/48 lines; cell-cycle shift, explains ~41% of this change), [[FANCB]] ⚠ 1.37× (z +6.0, 24/48 lines; cell-cycle shift, explains ~68% of this change), [[CCNE2]] ⚠ 1.64× (z +6.0, 26/44 lines; cell-cycle shift, explains ~76% of this change), [[DNA2]] ⚠ 1.39× (z +5.9, 22/48 lines; cell-cycle shift, explains ~80% of this change), [[BRIP1]] ⚠ 1.56× (z +5.8, 30/47 lines; cell-cycle shift, explains ~57% of this change), [[FANCI]] ⚠ 1.43× (z +5.7, 29/48 lines; cell-cycle shift, explains ~42% of this change), [[HELLS]] ⚠ 1.46× (z +5.6, 30/48 lines; cell-cycle shift, explains ~79% of this change), [[MIR924HG]] ⚠ 1.58× (z +5.5, 29/40 lines; cell-cycle shift, explains ~52% of this change), [[POLA2]] ⚠ 1.37× (z +5.4, 19/46 lines; cell-cycle shift, explains ~75% of this change), [[MAST4]] 1.34× (z +5.2, 22/37 lines; cell-cycle shift (explains ~0% here)), [[TRAF1]] 1.58× (z +5.1, 20/36 lines; cell-cycle shift (explains ~0% here)), [[CDK18]] 1.35× (z +4.7, 15/38 lines; cell-cycle shift (explains ~10% here)), [[PLA2G4C]] 1.37× (z +4.6, 12/44 lines; cell-cycle shift (explains ~0% here)), [[HROB]] 1.33× (z +4.4, 9/46 lines; cell-cycle shift (explains ~12% here)), [[TMEM40]] 1.77× (z +4.2, 7/22 lines; cell-cycle shift (explains ~0% here)), [[BTG2]] 1.49× (z +4.1, 14/39 lines; cell-cycle shift (explains ~17% here)), [[PAG1]] 1.23× (z +4.1, 6/33 lines; cell-cycle shift (explains ~0% here)), [[DIAPH3]] 1.22× (z +4.1, 22/45 lines; cell-cycle shift (explains ~0% here)), [[PINLYP]] 1.78× (z +4.0, 3/18 lines; cell-cycle shift (explains ~14% here)), [[EBF4]] 1.37× (z +4.0, 9/35 lines; cell-cycle shift (explains ~17% here)), [[AEN]] 1.40× (z +3.9, 16/45 lines; cell-cycle shift (explains ~22% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (41 genes, none with an alert; 12 shown): [[PIF1]] 0.544× (z -7.0, 28/46 lines), [[CCNF]] 0.634× (z -6.9, 25/47 lines), [[PLK1]] 0.608× (z -6.0, 27/47 lines), [[CENPA]] 0.774× (z -5.4, 21/47 lines), [[CENPE]] 0.721× (z -5.2, 27/48 lines), [[KIF20A]] 0.605× (z -5.1, 25/46 lines), [[CCNB1]] 0.673× (z -4.6, 24/47 lines), [[TACC3]] 0.767× (z -4.3, 20/48 lines), [[TROAP]] 0.728× (z -4.3, 16/47 lines), [[AURKA]] 0.723× (z -4.1, 24/48 lines), [[ASPM]] 0.738× (z -4.0, 23/47 lines), [[FAM83D]] 0.741× (z -4.0, 13/47 lines)

**0.5 µM** (73 genes, 64 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 21 shown): [[PIF1]] ⚠ 0.452× (z -9.9, 34/47 lines; cell-cycle shift, explains ~46% of this change), [[KIF20A]] ⚠ 0.487× (z -7.9, 41/47 lines; cell-cycle shift, explains ~53% of this change), [[PLK1]] ⚠ 0.549× (z -7.8, 34/48 lines; cell-cycle shift, explains ~59% of this change), [[CCNF]] ⚠ 0.646× (z -7.1, 30/48 lines; cell-cycle shift, explains ~52% of this change), [[CENPE]] ⚠ 0.664× (z -7.1, 39/48 lines; cell-cycle shift, explains ~73% of this change), [[CCNB1]] ⚠ 0.599× (z -6.4, 34/47 lines; cell-cycle shift, explains ~66% of this change), [[TROAP]] ⚠ 0.661× (z -6.0, 20/47 lines; cell-cycle shift, explains ~44% of this change), [[AURKA]] ⚠ 0.645× (z -6.0, 37/48 lines; cell-cycle shift, explains ~73% of this change), [[GPSM2]] ⚠ 0.754× (z -5.8, 28/48 lines; cell-cycle shift, explains ~62% of this change), [[PSRC1]] ⚠ 0.586× (z -5.8, 22/47 lines; cell-cycle shift, explains ~55% of this change), [[ASPM]] ⚠ 0.659× (z -5.8, 35/47 lines; cell-cycle shift, explains ~80% of this change), [[CENPA]] ⚠ 0.782× (z -5.6, 22/48 lines; cell-cycle shift, explains ~56% of this change), [[H2BC18]] 0.500× (z -5.0, 21/43 lines; cell-cycle shift (explains ~12% here)), [[H2BC17]] 0.405× (z -4.6, 25/46 lines; cell-cycle shift (explains ~14% here)), [[H1-3]] 0.506× (z -4.5, 24/36 lines; cell-cycle shift (explains ~18% here)), [[H1-5]] 0.443× (z -4.5, 21/37 lines; cell-cycle shift (explains ~19% here)), [[H3C12]] 0.608× (z -4.4, 15/47 lines; cell-cycle shift (explains ~5% here)), [[H2BC12]] 0.505× (z -4.2, 16/45 lines; cell-cycle shift (explains ~11% here)), [[H2AC12]] 0.518× (z -3.9, 14/44 lines; cell-cycle shift (explains ~14% here)), [[H2BC8]] 0.533× (z -3.3, 12/34 lines; cell-cycle shift (explains ~12% here)), [[ENSG00000253100]] 0.738× (z -2.8, 2/36 lines; cell-cycle shift (explains ~0% here))

**5 µM** (149 genes, 117 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 24 shown): [[PIF1]] ⚠ 0.349× (z -12.7, 34/45 lines; cell-cycle shift, explains ~42% of this change), [[PLK1]] ⚠ 0.395× (z -11.7, 39/46 lines; cell-cycle shift, explains ~47% of this change), [[KIF20A]] ⚠ 0.434× (z -8.8, 41/46 lines; cell-cycle shift, explains ~58% of this change), [[CCNF]] ⚠ 0.585× (z -8.4, 30/47 lines; cell-cycle shift, explains ~56% of this change), [[CENPE]] ⚠ 0.606× (z -8.4, 39/48 lines; cell-cycle shift, explains ~77% of this change), [[AURKA]] ⚠ 0.532× (z -8.3, 45/48 lines; cell-cycle shift, explains ~65% of this change), [[CCNB1]] ⚠ 0.503× (z -8.3, 43/47 lines; cell-cycle shift, explains ~63% of this change), [[ASPM]] ⚠ 0.546× (z -8.2, 44/47 lines; cell-cycle shift, explains ~68% of this change), [[DLGAP5]] ⚠ 0.529× (z -7.5, 43/46 lines; cell-cycle shift, explains ~68% of this change), [[KNSTRN]] ⚠ 0.629× (z -7.2, 29/47 lines; cell-cycle shift, explains ~48% of this change), [[DEPDC1]] ⚠ 0.552× (z -7.0, 38/46 lines; cell-cycle shift, explains ~91% of this change), [[CENPA]] ⚠ 0.727× (z -7.0, 27/48 lines; cell-cycle shift, explains ~54% of this change), [[H1-3]] 0.431× (z -5.4, 22/36 lines; cell-cycle shift (explains ~23% here)), [[H2BC18]] 0.486× (z -5.0, 24/41 lines; cell-cycle shift (explains ~16% here)), [[H2BC17]] 0.395× (z -4.6, 24/40 lines; cell-cycle shift (explains ~22% here)), [[CPSF2]] 0.811× (z -4.5, 17/48 lines; cell-cycle shift (explains ~5% here)), [[TMTC4]] 0.750× (z -4.4, 15/45 lines; cell-cycle shift (explains ~0% here)), [[LINC02987]] 0.740× (z -4.4, 21/43 lines; cell-cycle shift (explains ~11% here)), [[DTD2]] 0.758× (z -4.2, 9/46 lines; cell-cycle shift (explains ~0% here)), [[H2AC12]] 0.484× (z -4.1, 18/36 lines; cell-cycle shift (explains ~24% here)), [[BEND6]] 0.664× (z -3.9, 7/32 lines; cell-cycle shift (explains ~0% here)), [[METTL13]] 0.824× (z -3.9, 10/47 lines; cell-cycle shift (explains ~0% here)), [[PPIL6]] 0.691× (z -3.9, 12/44 lines; cell-cycle shift (explains ~0% here)), [[FZD7]] 0.733× (z -3.7, 16/43 lines; cell-cycle shift (explains ~12% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[Module 022]] (-2.1) |
| 5 µM | [[Module 006]] (+2.2) | [[Module 022]] (-2.8), [[Module 095]] (-2.6), [[Module 060]] (-2.6) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[NCI-H1573 (line)]] (1.83), [[SNU-1 (line)]] (1.80), [[SW48 (line)]] (1.73), [[HCT15 (line)]] (1.70) · weakest: [[COLO 205 (line)]] (0.350), [[SK-MEL-2 (line)]] (0.387), [[KATO III (line)]] (0.580) |
| 0.5 µM | — | [[HCT15 (line)]] (1.58), [[SW48 (line)]] (1.54), [[NCI-H460 (line)]] (1.46), [[SNU-1 (line)]] (1.46) · weakest: [[NCI-H661 (line)]] (0.380), [[NCI-H2347 (line)]] (0.536), [[SW1417 (line)]] (0.621) |
| 5 µM | — | [[NCI-H460 (line)]] (1.40), [[C32 (line)]] (1.34), [[H4 (line)]] (1.30), [[A549 (line)]] (1.25) · weakest: [[KATO III (line)]] (0.619), [[AsPC-1 (line)]] (0.625), [[SW1417 (line)]] (0.692) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Cytarabine (hydrochloride) (drug)]] (+0.68, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Gemcitabine (drug)]] (+0.57, DNA synthesis/repair inhibitor); [[Irinotecan (drug)]] (+0.55, DNA synthesis/repair inhibitor); [[Irinotecan (hydrochloride) (drug)]] (+0.53, DNA synthesis/repair inhibitor); [[Methotrexate (drug)]] (+0.51, DNA synthesis/repair inhibitor); [[SBI-0640756 (drug)]] (+0.47, Protein synthesis inhibitor); [[PF-06260933 (drug)]] (+0.44, Other MAPK inhibitor); [[Hexylresorcinol (drug)]] (+0.42, unclear); [[Fumaric acid (drug)]] (+0.31, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Cytarabine"
- `tables/drugdoses.parquet` — dd in 302, 303, 304
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
