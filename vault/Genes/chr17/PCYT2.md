---
symbol: "PCYT2"
type: "gene"
col: 11736
ensembl_id: "ENSG00000185813"
name: "phosphate cytidylyltransferase 2, ethanolamine"
location: "17q25.3"
module: 86
arm: "+"
pooled_cpm: 5.07
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 8
n_dd_up_clean: 18
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# PCYT2

*phosphate cytidylyltransferase 2, ethanolamine* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.84× (z +13.3, q 1e-37, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.424× (z -8.5, q 9e-15, down in 31 of 44 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHCR7]] (+0.72, fdr 7e-06), [[FASN]] (+0.66, fdr 7e-06), [[MVK]] (+0.65, fdr 1e-05); moves opposite to [[ANKRD42-DT]] (-0.42, fdr 2e-04), [[NKIRAS1]] (-0.41, fdr 6e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[UCP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11736.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.84×** | +13.3 | 1e-37 | 43/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.49×** | +12.4 | 1e-32 | 41/45 (Panc 03.27, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.04×** | +11.0 | 6e-26 | 21/23 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.95×** | +10.1 | 7e-22 | 13/15 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.60×** | +9.4 | 4e-19 | 36/45 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +7.4 | 9e-12 | 12/17 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.60×** | +6.6 | 3e-09 | 27/44 (NCI-H2030, HEC-1-A, …) | top dose only | position effect removed |
| [[Berbamine (drug)]] 5 µM |  | **1.59×** | +6.5 | 7e-09 | 28/45 (NCI-H2030, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +6.2 | 3e-08 | 13/35 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.78×** | +5.7 | 6e-07 | 23/44 (A498, NCI-H2030, …) | top dose only | position effect removed |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.71×** | +5.0 | 3e-05 | 17/45 (A498, HEC-1-A, …) | top dose only | position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.48×** | +3.9 | 0.005 | 10/38 (SW 900, AsPC-1, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.015 | 10/38 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.6 | 0.015 | 5/30 (C32, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.025 | 5/45 (Panc 03.27, SW480, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.035 | 8/40 (J82, NCI-H1792, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +3.2 | 0.037 | 5/46 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.037 | 7/34 (SHP-77, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.039 | 10/40 (A498, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +3.0 | 0.069 | 4/42 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11736.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.424×** | -8.5 | 9e-15 | 31/44 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -4.7 | 9e-04 | 19/36 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.632×** | -4.6 | 9e-04 | 19/44 (LS 180, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.673×** | -3.9 | 0.010 | 14/46 (BT-474, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.675×** | -3.9 | 0.010 | 8/42 (BT-474, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.760×** | -3.9 | 0.011 | 11/45 (LoVo, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.717×** | -3.3 | 0.074 | 12/42 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.721×** | -3.3 | 0.079 | 16/44 (PANC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11736. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.12× (z +8.6) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 9.85 | 0 | 1 | — | [[Selinexor (drug)]] 0.5 µM 0.0678× (z -10.2) |
| [[J82 (line)]] | alt | 8.51 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.25× (z +8.7) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 2.83 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.0447× (z -10.8) |
| [[SW1417 (line)]] | alt | 6.62 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0828× (z -10.2) |
| [[A-427 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11736), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHCR7]] | +0.72 | +0.71 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[FASN]] | +0.66 | +0.81 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[MVK]] | +0.65 | +0.62 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[HMGCS1]] | +0.61 | +0.70 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[LSS]] | +0.59 | +0.60 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[HMGCR]] | +0.59 | +0.65 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[MMAB]] | +0.57 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[LPIN1]] | +0.57 | +0.59 / +0.42 | both halves | 4e-05 | pathway: Glycerophospholipid biosynthesis |
| [[IDI1]] | +0.57 | +0.67 / +0.42 | both halves | 4e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[FDFT1]] | +0.56 | +0.50 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[SNAI3-AS1]] | +0.55 | +0.63 / +0.40 | both halves | 4e-05 |  |
| [[CYP51A1]] | +0.55 | +0.63 / +0.41 | both halves | 4e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD42-DT]] | -0.42 | -0.35 / -0.32 | both halves | 2e-04 |  |
| [[NKIRAS1]] | -0.41 | -0.22 / -0.24 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UCP2]] | B | UCP2 activity raises PCYT2's level | lines that do not express UCP2 (18) vs lines expressing it (32) | 1.32× lower at baseline in the lines without UCP2 | 0.029 | ⚠ within organs, on part of the lines; also absent: WNK2 |
| [[YBX2]] | B | YBX2 activity raises PCYT2's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 1.26× lower at baseline in the lines without YBX2 | 0.051 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[KIF1A]] | B | KIF1A activity raises PCYT2's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 1.11× lower at baseline in the lines without KIF1A | 0.070 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.4, -49.3); signed map (-52.5, 31.4). **Vector** length 72.2, 12.4% of its response variance represented; |z| ≥ 3 in 1,049 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *cholesterol synthesis* (control, mean cos +0.53 to 22); *Cholesterol biosynthesis* (reactome, mean cos +0.54 to 20); *Metabolism of steroids* (reactome, mean cos +0.53 to 25).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +7.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.4 | +3.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +4.4 | +6.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.2 | +5.7 |
|  | [[Berbamine (drug)]] 5 µM |  | +3.0 | +6.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +2.6 |
| fall | [[Tucidinostat (drug)]] 0.5 µM |  | -3.5 | -3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -4.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.1 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | phosphate cytidylyltransferase 2, ethanolamine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,900,958-81,911,432 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ET |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS |
| Reactome | 4 pathways, smallest: Synthesis of PE; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99447](https://www.uniprot.org/uniprotkb/Q99447) (Ethanolamine-phosphate cytidylyltransferase):

> Ethanolamine-phosphate cytidylyltransferase that catalyzes the second step in the synthesis of phosphatidylethanolamine (PE) from ethanolamine via the CDP-ethanolamine pathway. Phosphatidylethanolamine is a dominant inner-leaflet phospholipid in cell membranes, where it plays a role in membrane function by structurally stabilizing membrane-anchored proteins, and participates in important cellular processes such as cell division, cell fusion, blood coagulation, and apoptosis.

**Summary**, from NCBI Gene [5833](https://www.ncbi.nlm.nih.gov/gene/5833):

> This gene encodes an enzyme that catalyzes the formation of CDP-ethanolamine from CTP and phosphoethanolamine in the Kennedy pathway of phospholipid synthesis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:8756](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8756) · Entrez [5833](https://www.ncbi.nlm.nih.gov/gene/5833) · UniProt [Q99447](https://www.uniprot.org/uniprotkb/Q99447) · Ensembl [ENSG00000185813](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185813)

## Data

Gene col 11736: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11736); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11736, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11736]; `tensor/DDL_lfc|DDL_z.npy` [11736]; `embed/gene_vectors.npy` [11736]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11736 or target_col == 11736). Every well: [[PCYT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCYT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
