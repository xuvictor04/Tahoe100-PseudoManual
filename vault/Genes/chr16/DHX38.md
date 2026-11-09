---
symbol: "DHX38"
type: "gene"
col: 6451
ensembl_id: "ENSG00000140829"
name: "DEAH-box helicase 38"
location: "16q22.2"
module: 173
arm: "+"
pooled_cpm: 42.61
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 6
n_dd_up_clean: 19
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# DHX38

*DEAH-box helicase 38* — 16q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.81× (z +13.2, q 5e-37, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Carbidopa (monohydrate) (drug)]] 0.05 µM: 0.688× (z -5.9, q 2e-06, down in 40 of 48 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.775× (z -5.7, q 3e-06, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATXN1L]] (+0.69, fdr 7e-06), [[SCAF1]] (+0.68, fdr 1e-05), [[VPS52]] (+0.68, fdr 1e-05); moves opposite to [[PAFAH1B3]] (-0.67, fdr 1e-05), [[ANTKMT]] (-0.62, fdr 7e-05), [[SERAC1]] (-0.59, fdr 3e-05).
> It is in [[Module 173]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6451.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +13.2 | 5e-37 | 46/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +9.3 | 3e-18 | 43/48 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +8.4 | 6e-15 | 40/47 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +7.4 | 2e-11 | 41/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.41×** | +7.3 | 4e-11 | 40/49 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +6.4 | 1e-08 | 40/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.11×** | +6.2 | 5e-08 | 33/48 (LS 180, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +5.8 | 5e-07 | 34/48 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.42×** | +5.6 | 2e-06 | 28/47 (KATO III, NCI-H23, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +5.4 | 5e-06 | 28/48 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +5.0 | 3e-05 | 32/48 (MIA PaCa-2, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.39×** | +4.8 | 7e-05 | 26/47 (LoVo, SW480, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +4.5 | 3e-04 | 27/48 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.2 | 0.001 | 25/48 (SNU-1, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +4.2 | 0.001 | 23/48 (A498, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.002 | 22/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +4.0 | 0.002 | 26/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6451.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.688×** | -5.9 | 2e-06 | 40/48 (HT-29, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.775×** | -5.7 | 3e-06 | 34/48 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.705×** | -5.6 | 5e-06 | 36/48 (HOP62, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.714×** | -5.4 | 1e-05 | 38/48 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.739×** | -4.8 | 2e-04 | 30/48 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.812×** | -3.3 | 0.086 | 19/48 (J82, HEC-1-A, …) | rises with dose |  |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | 0.819× | -3.2 | 0.11 | 14/48 (RKO, NCI-H1792, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.822× | -3.1 | 0.12 | 15/48 (HT-29, Panc 03.27, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | 0.695× | -3.0 | 0.15 | 12/48 (LOX-IMVI, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6451. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 54.6 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.74× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 48.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +17.1) | — |
| [[SNU-1 (line)]] | wt | 43.3 | 0 | 2 (1 ⚠) | — | [[Ipatasertib (drug)]] 0.5 µM 0.0946× (z -11.2) |
| [[A-427 (line)]] | wt | 43.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A498 (line)]] | wt | 57.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.3) | — |
| [[A549 (line)]] | wt | 41.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.1) | — |
| [[C-33 A (line)]] | alt | 40.8 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.220× (z -9.9) |
| [[C32 (line)]] | wt | 36.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +8.9) | — |
| [[CHP-212 (line)]] | wt | 68.7 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0642× (z -14.2) |
| [[COLO 205 (line)]] | alt | 33.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HS-578T (line)]] | alt | 32.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.4) | — |
| [[KATO III (line)]] | alt | 43.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[LoVo (line)]] | wt | 35.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 50.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 33.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 59.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +12.5) | — |
| [[NCI-H23 (line)]] | alt | 41.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H460 (line)]] | wt | 29.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +13.1) | — |
| [[NCI-H661 (line)]] | alt | 34.3 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.05 µM 0.0605× (z -9.2) |
| [[PANC-1 (line)]] | alt | 27.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 53.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 36.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.8) | — |
| [[A-172 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 76.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6451), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN1L]] | +0.69 | +0.60 / +0.59 | both halves | 7e-06 | STRING 459 |
| [[SCAF1]] | +0.68 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[VPS52]] | +0.68 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[PET100]] | +0.65 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ZFHX2-AS1]] | +0.64 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[WDR74]] | +0.63 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[CCDC17]] | +0.62 | +0.53 / +0.39 | both halves | 6e-05 |  |
| [[U2AF2]] | +0.62 | +0.46 / +0.54 | both halves | 3e-05 | pathway: Dengue Virus-Host Interactions; STRING 924 |
| [[YJEFN3]] | +0.62 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[ARFGAP2]] | +0.62 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[FBRS]] | +0.61 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[CACTIN]] | +0.61 | +0.64 / +0.58 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 639 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAFAH1B3]] | -0.67 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[ANTKMT]] | -0.62 | -0.37 / -0.47 | both halves | 7e-05 |  |
| [[SERAC1]] | -0.59 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[TMEM160]] | -0.55 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[ELOB]] | -0.55 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[BTBD3]] | -0.54 | -0.58 / -0.28 | both halves | 3e-04 |  |
| [[ABHD6]] | -0.53 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[LSM2]] | -0.52 | -0.44 / -0.36 | both halves | 9e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[TMEM147]] | -0.51 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[RNF114]] | -0.51 | -0.36 / -0.42 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DHX38's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DHX38's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.701). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-10.2, 6.3); signed map (21.7, -22.7). **Vector** length 94.3, 22.7% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +5.4 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +5.1 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +13.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +4.8 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +2.6 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +4.0 |
|  | [[Arbutin (drug)]] 0.5 µM |  | +2.1 | -0.1 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -5.0 | -5.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -5.7 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -3.9 | -5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -2.8 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -3.3 |
|  | [[vincristine (drug)]] 0.05 µM |  | -2.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | DEAH-box helicase 38 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.2 — chr16:72,093,613-72,112,912 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Prp16, KIAA0224, hPrp16, PRPF16; previously DDX38 |
| Gene groups (HGNC) | DEAH-box helicases |
| Reactome | 10 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA 3'-end processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92620](https://www.uniprot.org/uniprotkb/Q92620) (Pre-mRNA-splicing factor ATP-dependent RNA helicase PRP16):

> Probable ATP-binding RNA helicase (Probable). Involved in pre-mRNA splicing as component of the spliceosome.

**Summary**, from NCBI Gene [9785](https://www.ncbi.nlm.nih.gov/gene/9785):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. The protein encoded …

**Accessions** — [HGNC:17211](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17211) · Entrez [9785](https://www.ncbi.nlm.nih.gov/gene/9785) · UniProt [Q92620](https://www.uniprot.org/uniprotkb/Q92620) · Ensembl [ENSG00000140829](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140829)

## Data

Gene col 6451: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6451); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6451, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6451]; `tensor/DDL_lfc|DDL_z.npy` [6451]; `embed/gene_vectors.npy` [6451]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6451 or target_col == 6451). Every well: [[DHX38 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHX38.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
