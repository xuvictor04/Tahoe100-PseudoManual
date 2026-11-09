---
drug: "Daptomycin"
type: "drug"
salt_base: "Daptomycin"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 1546
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Daptomycin

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 58 / 1373 / 1546; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.67 / 0.81.
> Flags by dose: unreliable plate only / unreliable plate only / unreliable plate only. ⚠ 0.05 µM: unreliable plate only; 0.5 µM: unreliable plate only; 5 µM: unreliable plate only (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 13]]:H1 | 32 / 26 | — | -0.13 | -0.0/+1.2/+0.5 | ⚠ unreliable plate only |
| 0.5 µM | [[Plate 13]]:G1 | 593 / 780 | — | -0.71 | -0.5/+3.3/+2.3 | ⚠ unreliable plate only |
| 5 µM | [[Plate 13]]:F1 | 677 / 869 | — | -0.04 | -1.5/+2.2/+1.6 | ⚠ unreliable plate only |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (32 genes, 32 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[CREB5]] ⚠ 1.45× (z +6.5, 18/33 lines), [[NF2]] ⚠ 1.25× (z +5.2, 19/47 lines), [[ETS1]] ⚠ 1.34× (z +5.0, 20/37 lines), [[SAMD4A]] ⚠ 1.37× (z +4.9, 32/46 lines), [[RANGAP1]] ⚠ 1.21× (z +3.7, 15/47 lines), [[CORO2B]] ⚠ 1.43× (z +3.7, 7/34 lines), [[DUSP8]] ⚠ 1.46× (z +3.7, 17/43 lines), [[MYPN]] ⚠ 1.39× (z +3.6, 4/19 lines), [[SGO2]] ⚠ 1.24× (z +3.5, 18/48 lines), [[IDI2-AS1]] ⚠ 1.45× (z +3.5, 13/47 lines), [[DNAH12]] ⚠ 1.44× (z +3.4, 10/45 lines), [[KRTAP5-AS1]] ⚠ 1.41× (z +3.3, 10/33 lines)

**0.5 µM** (593 genes, 593 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[CREB5]] ⚠ 3.57× (z +22.3, 30/32 lines), [[SAMD4A]] ⚠ 1.94× (z +10.4, 43/45 lines), [[NF2]] ⚠ 1.55× (z +10.3, 36/46 lines), [[MGLL]] ⚠ 1.53× (z +9.9, 25/33 lines), [[CLIP1]] ⚠ 1.35× (z +9.6, 34/47 lines), [[ARHGAP29]] ⚠ 1.52× (z +9.2, 29/37 lines), [[KRTAP5-AS1]] ⚠ 2.56× (z +9.2, 19/30 lines), [[MYO5B]] ⚠ 1.58× (z +9.1, 15/22 lines), [[RAB3B]] ⚠ 1.76× (z +9.1, 19/30 lines), [[NAV3]] ⚠ 1.88× (z +8.9, 24/31 lines), [[CAPN2]] ⚠ 1.44× (z +8.9, 38/47 lines), [[LINC00707]] ⚠ 2.06× (z +8.9, 16/21 lines)

**5 µM** (677 genes, 677 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[CREB5]] ⚠ 4.18× (z +25.1, 33/33 lines), [[SAMD4A]] ⚠ 2.18× (z +12.2, 44/46 lines), [[ARHGAP29]] ⚠ 1.68× (z +11.5, 33/38 lines), [[MYO5B]] ⚠ 1.77× (z +11.3, 19/22 lines), [[DTNA]] ⚠ 2.24× (z +11.2, 24/26 lines), [[MGLL]] ⚠ 1.60× (z +11.0, 29/34 lines), [[CAPN2]] ⚠ 1.56× (z +10.7, 40/48 lines), [[KRTAP5-AS1]] ⚠ 2.93× (z +10.5, 26/33 lines), [[CORO2B]] ⚠ 2.75× (z +10.5, 26/34 lines), [[IGF2BP2]] ⚠ 1.40× (z +10.1, 31/45 lines), [[CLIP1]] ⚠ 1.37× (z +10.1, 34/48 lines), [[CLDN1]] ⚠ 1.72× (z +9.8, 19/25 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (26 genes, 26 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[TUBB]] ⚠ 0.579× (z -7.1, 44/47 lines), [[TUBA1B]] ⚠ 0.488× (z -5.6, 45/47 lines), [[ENSG00000198211]] ⚠ 0.691× (z -4.3, 27/46 lines), [[TUBA1A]] ⚠ 0.690× (z -3.8, 19/38 lines), [[GSTA4]] ⚠ 0.741× (z -3.7, 6/42 lines), [[CDC42EP4]] ⚠ 0.831× (z -3.7, 6/47 lines), [[TUBB4B]] ⚠ 0.626× (z -3.6, 36/48 lines), [[TRERF1]] ⚠ 0.821× (z -3.6, 15/42 lines), [[EFCAB7]] ⚠ 0.823× (z -3.3, 10/47 lines), [[PIK3C2B]] ⚠ 0.818× (z -3.3, 6/44 lines), [[PEX11B]] ⚠ 0.823× (z -3.2, 4/47 lines), [[TUBA1C]] ⚠ 0.770× (z -3.2, 23/48 lines)

**0.5 µM** (780 genes, 780 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[ETV1]] ⚠ 0.524× (z -8.0, 29/36 lines), [[MEF2C]] ⚠ 0.630× (z -7.6, 22/33 lines), [[KLHL32]] ⚠ 0.501× (z -7.6, 16/31 lines), [[TENT5A]] ⚠ 0.652× (z -7.5, 23/36 lines), [[RHOXF1]] ⚠ 0.607× (z -7.5, 35/46 lines), [[HERC5]] ⚠ 0.552× (z -7.5, 26/32 lines), [[HOXA3]] ⚠ 0.694× (z -7.0, 23/37 lines), [[NFIA]] ⚠ 0.697× (z -6.9, 27/37 lines), [[TRERF1]] ⚠ 0.688× (z -6.8, 33/41 lines), [[PIK3C2B]] ⚠ 0.666× (z -6.7, 25/44 lines), [[PCDH7]] ⚠ 0.559× (z -6.5, 22/29 lines), [[PTCH1]] ⚠ 0.656× (z -6.5, 33/45 lines)

**5 µM** (869 genes, 869 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[ETV1]] ⚠ 0.465× (z -9.5, 31/37 lines), [[MEF2C]] ⚠ 0.575× (z -9.1, 25/34 lines), [[HERC5]] ⚠ 0.485× (z -9.1, 27/33 lines), [[GBP4]] ⚠ 0.423× (z -8.1, 24/28 lines), [[INTU]] ⚠ 0.651× (z -7.8, 29/45 lines), [[OASL]] ⚠ 0.433× (z -7.5, 32/38 lines), [[GBP2]] ⚠ 0.607× (z -7.4, 21/35 lines), [[DHRS3]] ⚠ 0.639× (z -7.3, 30/35 lines), [[PLA2G4A]] ⚠ 0.660× (z -7.3, 16/26 lines), [[IFI44]] ⚠ 0.554× (z -7.2, 31/36 lines), [[IFI44L]] ⚠ 0.440× (z -7.2, 25/26 lines), [[RBM43]] ⚠ 0.541× (z -7.1, 31/44 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 184]] (+4.5), [[Module 060]] (+3.5), [[Module 116]] (+3.5) | [[Module 059]] (-3.7), [[Module 065]] (-3.6), [[Module 045]] (-3.3) |
| 5 µM | [[Module 184]] (+5.3), [[Module 116]] (+3.8), [[Module 227]] (+3.7) | [[Module 059]] (-4.0), [[Module 223]] (-3.3), [[Module 032]] (-3.3) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[RKO (line)]] (-3.6) | [[NCI-H460 (line)]] (1.49), [[MIA PaCa-2 (line)]] (1.41), [[SW 1271 (line)]] (1.38), [[Panc 03.27 (line)]] (1.36) · weakest: [[SHP-77 (line)]] (0.246), [[SW48 (line)]] (0.391), [[KATO III (line)]] (0.508) |
| 0.5 µM | [[H4 (line)]] (-7.6), [[NCI-H23 (line)]] (-4.4), [[HOP62 (line)]] (-3.5), [[HS-578T (line)]] (-3.1) | [[H4 (line)]] (1.54), [[HT-29 (line)]] (1.46), [[CFPAC-1 (line)]] (1.45), [[SW 900 (line)]] (1.43) · weakest: [[J82 (line)]] (0.587), [[SHP-77 (line)]] (0.611), [[SW1417 (line)]] (0.614) |
| 5 µM | [[H4 (line)]] (-7.8), [[RPMI-7951 (line)]] (-4.6), [[NCI-H23 (line)]] (-3.2) | [[H4 (line)]] (1.67), [[CHP-212 (line)]] (1.53), [[CFPAC-1 (line)]] (1.48), [[HT-29 (line)]] (1.45) · weakest: [[SW1417 (line)]] (0.506), [[HEC-1-A (line)]] (0.521), [[J82 (line)]] (0.566) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: no trustworthy dose (vector dose flagged: unreliable plate only). Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Peretinoin (drug)]] (+0.90, Retinoic receptor agonist); [[Vinblastine (sulfate) (drug)]] (+0.84, Microtubule inhibitor); [[vincristine (drug)]] (+0.68, Microtubule inhibitor); [[Mebendazole (drug)]] (+0.56, Microtubule inhibitor); [[5-Azacytidine (drug)]] (+0.49, DNA methyltransferase inhibitor); [[Neratinib (drug)]] (+0.47, EGFR/ERBB inhibitor); [[Infigratinib (drug)]] (+0.42, Other TK inhibitor); [[Pitavastatin (Calcium) (drug)]] (+0.41, unclear, ⚠ vector dose flagged: cell-cycle shift); [[BAY1125976 (drug)]] (+0.38, PI3K/AKT inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 26 arrows, 26 of them with an alert ⚠; grade A 0, B 16, C 10. Shown: the 15 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[TCF4]] | 5 µM | B | TCF4 activity lowers the cells' numbers under Daptomycin 5 µM (makes them more sensitive) | lines that do not express TCF4 (25) vs lines expressing it (23) | the lines without TCF4: 1.21× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; cell counts less trustworthy |
| [[PLEKHO1]] | 5 µM | B | PLEKHO1 activity lowers the cells' numbers under Daptomycin 5 µM (makes them more sensitive) | lines that do not express PLEKHO1 (13) vs lines expressing it (35) | the lines without PLEKHO1: 1.21× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent; cell counts less trustworthy |
| [[MYH14]] | 0.5 µM | B | MYH14 activity raises the cells' numbers under Daptomycin 0.5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.74× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2; cell counts less trustworthy |
| [[LEF1-AS1]] | 0.05 µM | B | LEF1-AS1 activity lowers the cells' numbers under Daptomycin 0.05 µM (makes them more sensitive) | lines that do not express LEF1-AS1 (33) vs lines expressing it (15) | the lines without LEF1-AS1: 1.19× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent; cell counts less trustworthy |
| [[LGALS3BP]] | 0.05 µM | B | LGALS3BP activity raises the cells' numbers under Daptomycin 0.05 µM (protects the cells) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 0.81× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6; cell counts less trustworthy |
| [[PAPPA]] | 0.5 µM | B | PAPPA activity lowers the cells' numbers under Daptomycin 0.5 µM (makes them more sensitive) | lines that do not express PAPPA (33) vs lines expressing it (15) | the lines without PAPPA: 1.43× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; cell counts less trustworthy |
| [[TNFRSF11B]] | 5 µM | B | TNFRSF11B activity lowers the cells' numbers under Daptomycin 5 µM (makes them more sensitive) | lines that do not express TNFRSF11B (26) vs lines expressing it (22) | the lines without TNFRSF11B: 1.19× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: WNT5A, IL7R, ADAMTS12; cell counts less trustworthy |
| [[HTRA3]] | 0.5 µM | B | HTRA3 activity lowers the cells' numbers under Daptomycin 0.5 µM (makes them more sensitive) | lines that do not express HTRA3 (31) vs lines expressing it (17) | the lines without HTRA3: 1.37× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN; cell counts less trustworthy |
| [[MSRB3]] | 0.5 µM | B | MSRB3 activity lowers the cells' numbers under Daptomycin 0.5 µM (makes them more sensitive) | lines that do not express MSRB3 (20) vs lines expressing it (28) | the lines without MSRB3: 1.30× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1; cell counts less trustworthy |
| [[CCDC136]] | 5 µM | B | CCDC136 activity lowers the cells' numbers under Daptomycin 5 µM (makes them more sensitive) | lines that do not express CCDC136 (10) vs lines expressing it (38) | the lines without CCDC136: 1.20× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, RECK, ENSG00000267405; maybe low, not absent; cell counts less trustworthy |
| [[EDN1]] | 5 µM | B | EDN1 activity raises the cells' numbers under Daptomycin 5 µM (protects the cells) | lines that do not express EDN1 (27) vs lines expressing it (21) | the lines without EDN1: 0.82× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC; cell counts less trustworthy |
| [[AKT3]] | 5 µM | B | AKT3 activity lowers the cells' numbers under Daptomycin 5 µM (makes them more sensitive) | lines that do not express AKT3 (16) vs lines expressing it (32) | the lines without AKT3: 1.15× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041; cell counts less trustworthy |
| [[SPOCK1]] | 0.5 µM | B | SPOCK1 activity lowers the cells' numbers under Daptomycin 0.5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.40× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; cell counts less trustworthy |
| [[ENSG00000230647]] | 0.5 µM | B | ENSG00000230647 activity lowers the cells' numbers under Daptomycin 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.31× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1; cell counts less trustworthy |
| [[VEPH1]] | 0.5 µM | B | VEPH1 activity lowers the cells' numbers under Daptomycin 0.5 µM (makes them more sensitive) | lines that do not express VEPH1 (26) vs lines expressing it (22) | the lines without VEPH1: 1.35× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC; cell counts less trustworthy |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Daptomycin"
- `tables/drugdoses.parquet` — dd in 326, 327, 328
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
