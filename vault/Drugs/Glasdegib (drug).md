---
drug: "Glasdegib"
type: "drug"
salt_base: "Glasdegib"
targets: "SMO"
moa_fine: "Sonic inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 4
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Glasdegib

*Sonic inhibitor (inhibitor/antagonist) · targets: SMO · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 4 / 2 / 1; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.58 / -0.12.
> Flags by dose: unreliable plate only / unreliable plate only / unreliable plate only. ⚠ 0.05 µM: unreliable plate only; 0.5 µM: unreliable plate only; 5 µM: unreliable plate only (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 13]]:H2 | 4 / 0 | — | +0.07 | -0.1/-0.0/-1.3 | ⚠ unreliable plate only |
| 0.5 µM | [[Plate 13]]:G2 | 0 / 2 | — | +0.21 | +0.1/+0.8/-0.9 | ⚠ unreliable plate only |
| 5 µM | [[Plate 13]]:F2 | 0 / 1 | — | -0.03 | -0.5/-1.1/-0.5 | ⚠ unreliable plate only |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, 4 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[DPYSL4]] ⚠ 1.41× (z +3.2, 2/22 lines), [[IFIT2]] ⚠ 1.42× (z +2.9, 7/40 lines), [[TMEM45A]] ⚠ 1.26× (z +2.9, 11/35 lines), [[ENSG00000214803]] ⚠ 1.37× (z +2.8, 1/40 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (2 genes, 2 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[SLC41A3]] ⚠ 0.799× (z -4.0, 3/47 lines), [[PML]] ⚠ 0.818× (z -3.6, 14/47 lines)

**5 µM** (1 gene, 1 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[OIT3]] ⚠ 0.634× (z -3.6, 12/43 lines)

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

⚠ This drug's own vector: only 4 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only). Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar.*

- [[Esmolol (hydrochloride) (drug)]] (+0.80, unclear); [[Apalutamide (drug)]] (+0.78, Androgen receptor antagonist); [[Omeprazole (drug)]] (+0.76, unclear); [[Tirabrutinib (drug)]] (+0.74, Other TK inhibitor); [[Estrone sulfate (potassium) (drug)]] (+0.74, unclear); [[L-Eflornithine (monohydrochloride) (drug)]] (+0.73, unclear); [[Diphenhydramine (drug)]] (+0.72, unclear); [[Brimonidine (drug)]] (+0.69, Adrenoceptor agonist)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 12 arrows, 12 of them with an alert ⚠; grade A 0, B 5, C 7.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[NLGN4X]] | 5 µM | B | NLGN4X activity raises the cells' numbers under Glasdegib 5 µM (protects the cells) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 0.96× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P; cell counts less trustworthy |
| [[KLRC3]] | 5 µM | B | KLRC3 activity raises the cells' numbers under Glasdegib 5 µM (protects the cells) | lines that do not express KLRC3 (27) vs lines expressing it (21) | the lines without KLRC3: 0.89× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4; cell counts less trustworthy |
| [[PTGS2]] | 5 µM | B | PTGS2 activity lowers the cells' numbers under Glasdegib 5 µM (makes them more sensitive) | lines that do not express PTGS2 (27) vs lines expressing it (21) | the lines without PTGS2: 1.17× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4; cell counts less trustworthy |
| [[SLFN5]] | 5 µM | B | SLFN5 activity lowers the cells' numbers under Glasdegib 5 µM (makes them more sensitive) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 1.23× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent; cell counts less trustworthy |
| [[KLRC4-KLRK1]], [[KLRK1]] | 5 µM | B | KLRC4-KLRK1, KLRK1 activity raises the cells' numbers under Glasdegib 5 µM (protects the cells) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 0.87× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; cell counts less trustworthy; co-absent genes |
| [[FIGN]] | 5 µM | C | FIGN activity lowers the cells' numbers under Glasdegib 5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.22× the cells of the other lines | 0.004 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART; cell counts less trustworthy |
| [[C2orf74]] | 5 µM | C | C2orf74 activity lowers the cells' numbers under Glasdegib 5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.23× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1; cell counts less trustworthy |
| [[SPART-AS1]] | 5 µM | C | SPART-AS1 activity lowers the cells' numbers under Glasdegib 5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.19× the cells of the other lines | 0.022 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART; cell counts less trustworthy |
| [[NR3C1]] | 5 µM | C | NR3C1 activity lowers the cells' numbers under Glasdegib 5 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.23× the cells of the other lines | 0.025 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1; cell counts less trustworthy |
| [[ENSG00000286964]] | 5 µM | C | ENSG00000286964 activity lowers the cells' numbers under Glasdegib 5 µM (makes them more sensitive) | lines that do not express ENSG00000286964 (10) vs lines expressing it (38) | the lines without ENSG00000286964: 1.21× the cells of the other lines | 0.037 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SIX1, C2orf74, SYDE1; cell counts less trustworthy |
| [[SIX1]] | 5 µM | C | SIX1 activity lowers the cells' numbers under Glasdegib 5 µM (makes them more sensitive) | lines that do not express SIX1 (8) vs lines expressing it (40) | the lines without SIX1: 1.21× the cells of the other lines | 0.063 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: TIGD7, ENSG00000286964, FERMT2; cell counts less trustworthy |
| [[MAST1]] | 5 µM | C | MAST1's natural level raises the cells' numbers under Glasdegib 5 µM (protects the cells) | MAST1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.70 | 0.271 over the table, 0.052 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Glasdegib"
- `tables/drugdoses.parquet` — dd in 507, 508, 509
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
