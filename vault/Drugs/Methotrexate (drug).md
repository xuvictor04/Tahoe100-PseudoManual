---
drug: "Methotrexate"
type: "drug"
salt_base: "Methotrexate"
targets: "DHFR"
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 15
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Methotrexate

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · targets: DHFR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 9 / 15 / 10; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.02 / 0.32.
> Flags by dose: low cells (technical?) / - / -.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:G6 | 9 / 0 | — | -1.02 | -0.6/-0.9/-0.5 | low cells (technical?) |
| 0.5 µM | [[Plate 11]]:G6 | 9 / 6 | — | +0.25 | +2.3/+0.8/-0.3 | — |
| 5 µM | [[Plate 12]]:G6 | 7 / 3 | — | +0.42 | +2.7/-0.1/-0.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (9 genes, none with an alert): [[LINC01030]] 1.48× (z +3.6, 3/32 lines), [[ZNF439]] 1.29× (z +3.4, 3/26 lines), [[ENSG00000273014]] 1.39× (z +3.4, 2/35 lines), [[OLFM2]] 1.24× (z +3.4, 2/32 lines), [[CASC20]] 1.49× (z +3.2, 0/12 lines), [[DNAH2]] 1.34× (z +3.1, 2/28 lines), [[FAAP100]] 1.31× (z +3.1, 2/44 lines), [[ENSG00000286536]] 1.37× (z +3.1, 2/33 lines), [[ATP8A2]] 1.24× (z +2.8, 2/40 lines)

**0.5 µM** (9 genes, none with an alert): [[ZGRF1]] 1.22× (z +4.1, 10/48 lines), [[ATG16L2]] 1.26× (z +3.9, 17/48 lines), [[BLM]] 1.24× (z +3.7, 7/46 lines), [[RPS18]] 1.35× (z +3.3, 25/48 lines), [[PLB1]] 1.33× (z +3.2, 2/39 lines), [[TM4SF1-AS1]] 1.37× (z +3.1, 2/33 lines), [[MND1]] 1.20× (z +3.1, 4/47 lines), [[FGFR3]] 1.34× (z +2.9, 1/36 lines), [[ENSG00000289084]] 1.23× (z +2.8, 1/42 lines)

**5 µM** (7 genes, none with an alert): [[NCAPG2]] 1.25× (z +3.9, 20/48 lines), [[BRIP1]] 1.29× (z +3.4, 20/47 lines), [[EXO1]] 1.28× (z +3.2, 7/46 lines), [[ZNF695]] 1.25× (z +3.1, 3/38 lines), [[CDC45]] 1.26× (z +2.9, 3/45 lines), [[MELK]] 1.20× (z +2.9, 8/45 lines), [[DTL]] 1.22× (z +2.8, 7/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (6 genes, none with an alert): [[LINC00665]] 0.716× (z -4.3, 9/32 lines), [[SBDSP1-1]] 0.673× (z -3.7, 6/43 lines), [[ENSG00000111780]] 0.773× (z -3.6, 9/47 lines), [[TROAP]] 0.802× (z -3.2, 6/47 lines), [[ADM2]] 0.715× (z -3.1, 7/33 lines), [[ERICH2-DT]] 0.773× (z -3.0, 3/36 lines)

**5 µM** (3 genes, none with an alert): [[MIR3667HG]] 0.699× (z -3.7, 0/10 lines), [[MT-CO1]] 0.746× (z -3.4, 45/48 lines), [[UGDH-AS1]] 0.798× (z -3.4, 2/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Ornidazole (drug)]] (+0.62, unclear, ⚠ only 1 significant gene; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Hesperidin (drug)]] (+0.57, unclear); [[ETC-206 (drug)]] (+0.55, Protein synthesis inhibitor, ⚠ only 0 significant genes); [[SBI-0640756 (drug)]] (+0.55, Protein synthesis inhibitor); [[Minodronic acid (drug)]] (+0.52, unclear); [[Cytarabine (drug)]] (+0.51, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Malotilate (drug)]] (+0.51, unclear); [[PF-06260933 (drug)]] (+0.50, Other MAPK inhibitor); [[Allopurinol (drug)]] (+0.50, unclear); [[Silodosin (drug)]] (+0.48, unclear); [[Tazarotene (drug)]] (+0.47, Retinoic receptor agonist)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Methotrexate"
- `tables/drugdoses.parquet` — dd in 672, 673, 674
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
