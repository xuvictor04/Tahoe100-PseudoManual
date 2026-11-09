---
symbol: "ZNF252P"
type: "gene"
col: 12303
ensembl_id: "ENSG00000196922"
name: "zinc finger protein 252, pseudogene"
location: "8q24.3"
module: 7
arm: "+"
pooled_cpm: 11.0
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ZNF252P

*zinc finger protein 252, pseudogene* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.69× (z +5.3, q 6e-05, up in 14 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.45× (z +3.9, q 0.024, up in 21 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.300× (z -12.6, q 8e-34, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF252P-1]] (+0.88, fdr 7e-06, ⚠ same locus), [[RIMOC1]] (+0.71, fdr 7e-06), [[AASDHPPT]] (+0.71, fdr 7e-06), [[MTHFSD]] (+0.70, fdr 7e-06); moves opposite to [[STK32C]] (-0.62, fdr 1e-05), [[AZIN2]] (-0.60, fdr 4e-05), [[PTMAP2]] (-0.59, fdr 1e-05, ⚠ PTMAP2 in the vector space only through flagged drug-doses), [[UQCRH]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF613]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12303.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +5.3 | 6e-05 | 14/22 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.024 | 21/47 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +3.7 | 0.044 | 11/33 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +3.5 | 0.044 | 17/46 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.044 | 13/47 (A-427, HEC-1-A, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.26×** | +3.5 | 0.044 | 10/48 (NCI-H23, RKO, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 1.35× | +3.2 | 0.12 | 10/47 (PANC-1, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.34× | +3.1 | 0.13 | 10/46 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12303.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.300×** | -12.6 | 8e-34 | 44/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.308×** | -12.4 | 9e-33 | 38/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.409×** | -9.4 | 1e-18 | 37/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.432×** | -8.8 | 2e-16 | 35/45 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.483×** | -7.6 | 3e-12 | 30/47 (RPMI-7951, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.520×** | -6.6 | 4e-09 | 29/39 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.594×** | -5.5 | 4e-06 | 23/46 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.609×** | -5.2 | 1e-05 | 24/45 (SW480, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.426×** | -4.7 | 2e-04 | 23/35 (A-172, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.641×** | -4.6 | 3e-04 | 24/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.699×** | -3.5 | 0.020 | 15/45 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12303. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0738× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.103× (z -15.2) |
| [[SW480 (line)]] | alt | 11.0 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.133× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 7.72 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0735× (z -15.0) |
| [[BT-474 (line)]] | alt | 17.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -9.1) |
| [[C32 (line)]] | wt | 10.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0673× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0842× (z -9.9) |
| [[COLO 205 (line)]] | alt | 14.2 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0397× (z -13.5) |
| [[LoVo (line)]] | wt | 11.1 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.140× (z -11.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 7.06 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.127× (z -8.6) |
| [[SHP-77 (line)]] | alt | 27.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.243× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 7.83 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -8.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -8.6) |
| [[HT-29 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -9.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 6.48 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0872× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 17.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 2.86 | 0 | 1 | — | [[vincristine (drug)]] 0.05 µM 0.0526× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.150× (z -9.6) ⚠ toxic |
| [[RKO (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -9.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 12.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0537× (z -11.8) |
| [[SNU-423 (line)]] | alt | 7.88 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0865× (z -9.6) |
| [[SW 900 (line)]] | alt | 8.07 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.05 µM 0.0586× (z -9.8) |
| [[A-172 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12303), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF252P-1]] | +0.88 | +0.90 / +0.82 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[RIMOC1]] | +0.71 | +0.77 / +0.58 | both halves | 7e-06 |  |
| [[AASDHPPT]] | +0.71 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[MTHFSD]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[COQ5]] | +0.69 | +0.79 / +0.45 | both halves | 3e-05 |  |
| [[ZNF623]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[ZFP41]] | +0.67 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[PSME3IP1]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[TRMT13]] | +0.67 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[MRRF]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ZNF543]] | +0.66 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[PEX1]] | +0.65 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[TMEM128]] | +0.65 | +0.69 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK32C]] | -0.62 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[AZIN2]] | -0.60 | -0.43 / -0.62 | both halves | 4e-05 |  |
| [[PTMAP2]] ⚠ | -0.59 | -0.55 / -0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UQCRH]] | -0.59 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[PDE8A]] | -0.58 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[SLC25A5]] | -0.58 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[SLC29A4]] | -0.57 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[PEDS1]] | -0.57 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[SLC37A3]] | -0.57 | -0.62 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF613]] | B | ZNF613 activity raises ZNF252P's level | lines that do not express ZNF613 (7) vs lines expressing it (43) | 1.33× lower at baseline in the lines without ZNF613 | 0.047 | ⚠ within organs, on part of the lines; also absent: ZNF850, ENSG00000283201, ZNF571 |
| [[PSMB5]] | B | PSMB5 activity raises ZNF252P's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF607]] | B | ZNF607 activity raises ZNF252P's level | lines that do not express ZNF607 (7) vs lines expressing it (43) | 1.34× lower at baseline in the lines without ZNF607 | 0.091 | ⚠ within organs, on part of the lines; also absent: ZNF675, ZNF571, ZFP30 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.536). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-20.0, 6.9); signed map (7.4, -28.4). **Vector** length 64.3, 10.9% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +0.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.4 | +1.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -2.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.8 | -7.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.7 | -12.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -5.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +1.9 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 252, pseudogene |
| Locus type | pseudogene |
| Location | 8q24.3 — chr8:144,976,190-144,999,723 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously ZNF252 |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:13046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13046) · Entrez [286101](https://www.ncbi.nlm.nih.gov/gene/286101) · Ensembl [ENSG00000196922](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196922)

## Data

Gene col 12303: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12303); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12303, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12303]; `tensor/DDL_lfc|DDL_z.npy` [12303]; `embed/gene_vectors.npy` [12303]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12303 or target_col == 12303). Every well: [[ZNF252P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF252P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
