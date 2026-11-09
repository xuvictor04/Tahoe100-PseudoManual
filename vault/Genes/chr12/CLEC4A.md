---
symbol: "CLEC4A"
type: "gene"
col: 3273
ensembl_id: "ENSG00000111729"
name: "C-type lectin domain family 4 member A"
location: "12p13.31"
module: 37
arm: "+"
pooled_cpm: 6.99
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 16
n_dd_up_clean: 12
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# CLEC4A

*C-type lectin domain family 4 member A* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 3.08× (z +10.4, q 2e-22, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.516× (z -5.8, q 3e-06, down in 10 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 0.564× (z -5.3, q 3e-05, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ECT2L]] (+0.76, fdr 7e-06), [[BNIPL]] (+0.70, fdr 7e-06), [[PPP1R32]] (+0.69, fdr 7e-06); moves opposite to [[RIF1]] (-0.59, fdr 1e-05), [[TCF12]] (-0.58, fdr 3e-05), [[HSPB8]] (-0.58, fdr 1e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF404]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3273.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.08×** | +10.4 | 2e-22 | 41/47 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.02×** | +10.2 | 7e-22 | 42/47 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.99×** | +10.1 | 1e-21 | 42/46 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +7.9 | 5e-13 | 31/41 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.03×** | +6.5 | 7e-09 | 28/46 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.96×** | +6.2 | 5e-08 | 28/45 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +6.1 | 1e-07 | 33/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +6.0 | 1e-07 | 19/44 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.26×** | +5.7 | 8e-07 | 23/45 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +5.2 | 1e-05 | 16/33 (Panc 03.27, AsPC-1, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.60×** | +4.3 | 8e-04 | 18/46 (SW 900, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.2 | 0.001 | 14/35 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +3.9 | 0.005 | 12/47 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.017 | 16/42 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.023 | 10/44 (A549, RKO, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3273.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.516×** | -5.8 | 3e-06 | 10/12 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.545×** | -5.6 | 7e-06 | 23/30 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.564×** | -5.3 | 3e-05 | 21/47 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.618×** | -4.4 | 0.001 | 17/48 (LS 180, NCI-H1573, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.627×** | -4.3 | 0.002 | 20/47 (Hs 766T, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.629×** | -4.3 | 0.002 | 16/46 (A-427, A498, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.647×** | -4.0 | 0.005 | 12/47 (C-33 A, CFPAC-1, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.655×** | -3.9 | 0.007 | 14/46 (Hs 766T, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.655×** | -3.7 | 0.012 | 17/45 (NCI-H1792, COLO 205, …) | top dose only | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.672×** | -3.7 | 0.015 | 17/46 (SW48, RKO, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.681×** | -3.5 | 0.022 | 11/47 (H4, PANC-1, …) | inconsistent across doses |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | **0.701×** | -3.3 | 0.053 | 9/46 (LoVo, NCI-H1573, …) | top dose only | position effect removed |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.708×** | -3.2 | 0.066 | 9/46 (HS-578T, COLO 205, …) | top dose only |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.712×** | -3.1 | 0.072 | 14/47 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.715×** | -3.1 | 0.078 | 15/47 (LoVo, SW 1088, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **0.699×** | -3.0 | 0.083 | 11/46 (A498, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3273. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 17.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0509× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Thymol (drug)]] 0.5 µM 0.190× (z -8.6) |
| [[SW480 (line)]] | alt | 10.3 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.41× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0605× (z -14.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 7.34 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0807× (z -12.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 9.67 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0792× (z -11.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 6.92 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0948× (z -8.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 6.57 | 0 | 1 | — | [[Hexylresorcinol (drug)]] 0.5 µM 0.123× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0939× (z -9.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3273), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECT2L]] | +0.76 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[BNIPL]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[PPP1R32]] | +0.69 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[TMEM161B-DT]] | +0.67 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[HYPK]] | +0.67 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.66 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[TMEM14B]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SDHAP1-1]] | +0.65 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[ADAM20P1]] | +0.64 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[GPR107]] | +0.64 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[LINC00640]] | +0.64 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[ADAM20]] | +0.63 | +0.68 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIF1]] | -0.59 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[TCF12]] | -0.58 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[HSPB8]] | -0.58 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[TASOR]] | -0.58 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[CEP41]] | -0.56 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.56 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[CENPBD1P]] | -0.56 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[RASAL2]] | -0.54 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[ROCK2]] | -0.54 | -0.49 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF404]] | B | ZNF404 activity raises CLEC4A's level | lines that do not express ZNF404 (14) vs lines expressing it (36) | 1.13× lower at baseline in the lines without ZNF404 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: MIR130AHG, RAB34, PYGO1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.3, -20.6); signed map (8.4, 5.7). **Vector** length 74.6, 14.0% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +6.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +5.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.3 | +10.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.2 | +10.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.5 | +2.5 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.3 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.1 | +6.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.7 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | +3.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.6 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | +0.7 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.1 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | C-type lectin domain family 4 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:8,123,617-8,138,607 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DCIR, DDB27, CD367, hDCIR; previously CLECSF6 |
| Gene groups (HGNC) | CD molecules; C-type lectin domain containing; Dectin 2 cluster |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 3 pathways, smallest: Dectin-2 family; C-type lectin receptors (CLRs); Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMR7](https://www.uniprot.org/uniprotkb/Q9UMR7) (C-type lectin domain family 4 member A):

> C-type lectin receptor that binds carbohydrates mannose and fucose but also weakly interacts with N-acetylglucosamine (GlcNAc) in a Ca(2+)-dependent manner. Involved in regulating immune reactivity. Once triggered by antigen, it is internalized by clathrin-dependent endocytosis and delivers its antigenic cargo into the antigen presentation pathway resulting in cross-priming of CD8(+) T cells. This cross-presentation and cross-priming are enhanced by TLR7 and TLR8 agonists with increased …

**Summary**, from NCBI Gene [50856](https://www.ncbi.nlm.nih.gov/gene/50856):

> This gene encodes a member of the C-type lectin/C-type lectin-like domain (CTL/CTLD) superfamily. Members of this family share a common protein fold and have diverse functions, such as cell adhesion, cell-cell signalling, glycoprotein turnover, and roles in inflammation and immune response. The encoded type 2 transmembrane protein may play a role in inflammatory and immune response. Multiple transcript variants encoding distinct isoforms have been identified for this gene. This gene is closely …

**Accessions** — [HGNC:13257](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13257) · Entrez [50856](https://www.ncbi.nlm.nih.gov/gene/50856) · UniProt [Q9UMR7](https://www.uniprot.org/uniprotkb/Q9UMR7) · Ensembl [ENSG00000111729](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111729)

## Data

Gene col 3273: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3273); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3273, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3273]; `tensor/DDL_lfc|DDL_z.npy` [3273]; `embed/gene_vectors.npy` [3273]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3273 or target_col == 3273). Every well: [[CLEC4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLEC4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
