---
drug: "Lidocaine (hydrochloride)"
type: "drug"
salt_base: "Lidocaine"
targets: "MAP2K1, MAPK1, NFKB1"
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 239
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Lidocaine (hydrochloride)

*unclear (unclear) · targets: MAP2K1, MAPK1, NFKB1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 239 / 44 / 21; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.25 / 0.20.
> Flags by dose: low cells (technical?) / - / -.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:E6 | 231 / 8 | — | -1.82 | -1.4/-0.8/-0.1 | low cells (technical?) |
| 0.5 µM | [[Plate 05]]:E6 | 32 / 12 | — | -0.52 | -1.3/-1.1/-1.3 | — |
| 5 µM | [[Plate 14]]:E6 | 10 / 11 | 0.591 | -0.54 | +1.5/+1.0/+0.8 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (231 genes, none with an alert; 12 shown): [[PGBD4]] 1.59× (z +5.9, 5/21 lines), [[SULT4A1]] 2.10× (z +5.7, 0/9 lines), [[H3C6]] 1.77× (z +5.3, 5/17 lines), [[RAD9B]] 1.62× (z +4.8, 2/15 lines), [[TMSB15B]] 1.68× (z +4.8, 3/14 lines), [[HERC2P10]] 1.52× (z +4.6, 1/11 lines), [[LINC01551]] 1.91× (z +4.6, 0/8 lines), [[ENSG00000264660]] 2.17× (z +4.6, 0/6 lines), [[ENSG00000260958]] 2.02× (z +4.5, 1/6 lines), [[TSPYL5]] 1.97× (z +4.5, 0/8 lines), [[ENSG00000254261]] 1.97× (z +4.5, 0/4 lines), [[ENSG00000248993]] 1.57× (z +4.4, 1/13 lines)

**0.5 µM** (32 genes, none with an alert; 12 shown): [[TLCD4-RWDD3]] 1.56× (z +4.7, 3/24 lines), [[ENSG00000288721]] 1.50× (z +4.4, 7/38 lines), [[ARL17A]] 1.28× (z +3.9, 6/42 lines), [[ENSG00000286058]] 1.56× (z +3.7, 6/15 lines), [[SEPTIN7P13]] 1.47× (z +3.7, 11/40 lines), [[RIMBP2]] 1.33× (z +3.7, 2/14 lines), [[ENSG00000267740]] 1.44× (z +3.6, 3/34 lines), [[DOCK7-DT]] 1.36× (z +3.5, 5/32 lines), [[RALY-AS1]] 1.42× (z +3.5, 1/29 lines), [[ZNF558]] 1.26× (z +3.5, 9/43 lines), [[GTF3C2-AS2]] 1.34× (z +3.5, 8/38 lines), [[SETD4]] 1.22× (z +3.4, 10/45 lines)

**5 µM** (10 genes, none with an alert): [[FKBP5]] 1.33× (z +5.1, 16/42 lines), [[ENSG00000257553]] 1.43× (z +4.0, 13/43 lines), [[ENSG00000234915]] 1.33× (z +4.0, 6/44 lines), [[CALCRL]] 1.32× (z +3.8, 0/27 lines), [[ENSG00000270571]] 1.35× (z +3.2, 5/41 lines), [[ANKRD7]] 1.20× (z +3.2, 4/34 lines), [[APPBP2-DT]] 1.30× (z +3.1, 2/39 lines), [[DAW1]] 1.35× (z +3.0, 0/13 lines), [[SH2D4B]] 1.25× (z +2.9, 1/37 lines), [[ENSG00000282440]] 1.31× (z +2.8, 3/24 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (8 genes, none with an alert): [[ICA1L]] 0.759× (z -5.1, 15/42 lines), [[KMT2E-AS1]] 0.666× (z -3.9, 12/35 lines), [[MYORG]] 0.713× (z -3.8, 10/25 lines), [[ENSG00000170846]] 0.725× (z -3.7, 12/37 lines), [[FGFR2]] 0.721× (z -3.5, 0/4 lines), [[C19orf48]] 0.827× (z -3.4, 9/44 lines), [[NAMPTP1]] 0.697× (z -3.4, 9/31 lines), [[INCENP]] 0.815× (z -2.9, 14/45 lines)

**0.5 µM** (12 genes, none with an alert): [[ABITRAM]] 0.790× (z -4.3, 13/45 lines), [[SLC39A6]] 0.809× (z -4.1, 21/48 lines), [[ENSG00000267168]] 0.632× (z -3.7, 13/31 lines), [[ARMCX1]] 0.683× (z -3.7, 4/20 lines), [[DPH1]] 0.800× (z -3.4, 14/46 lines), [[KPNB1]] 0.832× (z -3.2, 24/48 lines), [[TSPAN6]] 0.761× (z -3.2, 11/38 lines), [[RPN2]] 0.832× (z -3.2, 21/48 lines), [[CHAC1]] 0.694× (z -3.1, 7/25 lines), [[ENPP4]] 0.827× (z -3.1, 4/29 lines), [[CCNDBP1]] 0.821× (z -2.8, 9/45 lines), [[ST3GAL5]] 0.808× (z -2.8, 2/37 lines)

**5 µM** (11 genes, none with an alert): [[ASS1]] 0.759× (z -5.6, 22/34 lines), [[ARRDC3]] 0.758× (z -4.8, 41/48 lines), [[BCL2L2]] 0.810× (z -4.5, 19/48 lines), [[DERL2]] 0.823× (z -4.2, 18/48 lines), [[CDC26]] 0.814× (z -3.9, 16/47 lines), [[GPRC5B]] 0.766× (z -3.8, 9/20 lines), [[ENSG00000291107]] 0.776× (z -3.6, 3/38 lines), [[EFCAB3P1]] 0.771× (z -3.5, 15/44 lines), [[CDIPT]] 0.822× (z -3.3, 12/48 lines), [[ATOSB]] 0.825× (z -3.3, 10/43 lines), [[H1-4]] 0.730× (z -3.2, 31/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 194]] (+2.9), [[Module 004]] (+2.1) | [[Module 179]] (-2.2), [[Module 207]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[NCI-H2030 (line)]] (-4.0), [[A498 (line)]] (-3.4), [[SW 900 (line)]] (-3.3), [[SNU-423 (line)]] (-3.3) | [[AN3 CA (line)]] (1.99), [[SNU-1 (line)]] (1.97), [[CHP-212 (line)]] (1.76), [[Hs 766T (line)]] (1.53) · weakest: [[SW480 (line)]] (0.0670), [[NCI-H2347 (line)]] (0.332), [[A-427 (line)]] (0.349) |
| 0.5 µM | — | [[CHP-212 (line)]] (1.80), [[SW 1271 (line)]] (1.65), [[SW 1088 (line)]] (1.42), [[HCT15 (line)]] (1.22) · weakest: [[SNU-1 (line)]] (0.0594), [[MIA PaCa-2 (line)]] (0.258), [[CFPAC-1 (line)]] (0.303) |
| 5 µM | — | [[SW 1271 (line)]] (1.79), [[SW 1088 (line)]] (1.76), [[AN3 CA (line)]] (1.50), [[NCI-H661 (line)]] (1.45) · weakest: [[HT-29 (line)]] (0.166), [[RPMI-7951 (line)]] (0.311), [[KATO III (line)]] (0.442) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 5 next most similar without an alert.*

- [[Vismodegib (drug)]] (+0.71, Sonic inhibitor, ⚠ only 5 significant genes); [[Talc (drug)]] (+0.69, unclear, ⚠ only 7 significant genes); [[Ataluren (drug)]] (+0.67, unclear, ⚠ only 7 significant genes); [[Benztropine (mesylate) (drug)]] (+0.63, unclear); [[Orlistat (drug)]] (+0.61, unclear); [[Rimonabant (Hydrochloride) (drug)]] (+0.60, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Vitamin K4 (drug)]] (+0.60, unclear); [[Imiquimod (hydrochloride) (drug)]] (+0.59, unclear, ⚠ vector dose flagged: toxic); [[Valdecoxib (drug)]] (+0.59, Cyclooxygenase inhibitor); [[Cysteamine (hydrochloride) (drug)]] (+0.57, unclear); [[Pioglitazone (drug)]] (+0.56, unclear); [[Imiquimod (maleate) (drug)]] (+0.51, unclear); [[Saquinavir (drug)]] (+0.51, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[CCL5]] | 0.05 µM | B | CCL5 activity lowers the cells' numbers under Lidocaine (hydrochloride) 0.05 µM (makes them more sensitive) | lines that do not express CCL5 (22) vs lines expressing it (26) | the lines without CCL5: 1.37× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: SRGN, FLI1, KCNMA1 |
| [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] | 0.05 µM | C | ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 activity lowers the cells' numbers under Lidocaine (hydrochloride) 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.64× the cells of the other lines | 0.053 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| [[ENSG00000255031]] | 0.05 µM | C | ENSG00000255031 activity lowers the cells' numbers under Lidocaine (hydrochloride) 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000255031 (3) vs lines expressing it (45) | the lines without ENSG00000255031: 1.62× the cells of the other lines | 0.060 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: GLMP, TCIRG1, MT1X; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Lidocaine (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 618, 619, 620
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
