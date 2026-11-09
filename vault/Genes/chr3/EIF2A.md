---
symbol: "EIF2A"
type: "gene"
col: 6944
ensembl_id: "ENSG00000144895"
name: "eukaryotic translation initiation factor 2A"
location: "3q25.1"
module: 56
arm: "+"
pooled_cpm: 120.28
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# EIF2A

*eukaryotic translation initiation factor 2A* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.74× (z +10.2, q 1e-21, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.668× (z -5.9, q 2e-06, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPB1]] (+0.65, fdr 7e-06), [[SRP72]] (+0.65, fdr 7e-06), [[SUPV3L1]] (+0.63, fdr 1e-05); moves opposite to [[ERF]] (-0.54, fdr 1e-05), [[TAOK2]] (-0.53, fdr 2e-05), [[ORAI1]] (-0.49, fdr 2e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6944.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.74×** | +10.2 | 1e-21 | 48/49 (LoVo, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.45×** | +9.6 | 3e-19 | 48/48 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.61×** | +7.0 | 4e-10 | 46/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +6.0 | 3e-07 | 41/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +5.9 | 3e-07 | 40/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.09×** | +5.7 | 1e-06 | 33/38 (AsPC-1, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +5.3 | 1e-05 | 33/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +5.1 | 2e-05 | 42/48 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.3 | 9e-04 | 30/47 (LoVo, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +3.5 | 0.023 | 29/48 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.035 | 23/48 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[EX229 (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.081 | 28/48 (LOX-IMVI, KATO III, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.081 | 15/49 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.49×** | +3.1 | 0.081 | 27/48 (Panc 03.27, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.23×** | +3.1 | 0.081 | 22/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.48×** | +3.0 | 0.081 | 25/48 (Hs 766T, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6944.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.668×** | -5.9 | 2e-06 | 36/48 (A498, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.682×** | -5.6 | 5e-06 | 38/48 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.696×** | -5.3 | 2e-05 | 38/48 (A498, H4, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.703×** | -5.2 | 3e-05 | 39/48 (A498, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.732×** | -4.6 | 5e-04 | 37/48 (A498, SW1417, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.848× | -3.4 | 0.059 | 20/49 (LoVo, RPMI-7951, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.793×** | -3.3 | 0.088 | 24/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.803×** | -3.2 | 0.090 | 24/48 (RKO, SW480, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.808× | -3.1 | 0.11 | 24/48 (BT-474, LOX-IMVI, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | 0.674× | -3.0 | 0.14 | 22/49 (A498, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6944. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 112 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.97× (z +14.6) | — |
| [[LoVo (line)]] | wt | 138 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.85× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.642× (z -8.6) ⚠ cell-cycle shift, explains ~16% of this change |
| [[NCI-H460 (line)]] | wt | 86.3 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +11.4) | — |
| [[BT-474 (line)]] | alt | 103 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 130 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.58× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 115 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.67× (z +10.4) | — |
| [[A498 (line)]] | wt | 88.8 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.451× (z -8.7) |
| [[KATO III (line)]] | alt | 158 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.54× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 137 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 181 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.63× (z +9.2) | — |
| [[RKO (line)]] | wt | 124 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.85× (z +9.5) | — |
| [[SW480 (line)]] | alt | 134 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.37× (z +9.7) | — |
| [[A-427 (line)]] | wt | 149 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 5.47× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 116 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +9.4) | — |
| [[H4 (line)]] | wt | 161 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.298× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.345× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[HT-29 (line)]] | alt | 132 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.96× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 76.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.342× (z -9.3) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 95.4 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.43× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 95.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.51× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[SW48 (line)]] | wt | 108 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.21× (z +10.8) | — |
| [[A-172 (line)]] | wt | 69.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 101 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 84.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 118 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 158 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 160 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6944), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPB1]] | +0.65 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[SRP72]] | +0.65 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[SUPV3L1]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[TVP23B]] | +0.63 | +0.69 / +0.46 | both halves | 2e-05 |  |
| [[MIGA1]] | +0.63 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[USPL1]] | +0.62 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[TFG]] | +0.61 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[TMEM39A]] | +0.61 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[NUS1]] | +0.61 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[COPB2]] | +0.60 | +0.63 / +0.53 | both halves | 1e-05 | same gene group |
| [[RSL24D1]] | +0.60 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[LONP2]] | +0.60 | +0.74 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERF]] | -0.54 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[TAOK2]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ORAI1]] | -0.49 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[LRRC57]] | -0.49 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[SMURF1]] | -0.48 | -0.23 / -0.42 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises EIF2A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.529). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.0, -19.2); signed map (-59.1, 11.1). **Vector** length 88.5, 27.9% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *COPII-mediated vesicle transport* (reactome, mean cos +0.52 to 8); *Antigen Presentation: Folding, assembly and peptide loading of class I MHC* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change | +5.5 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.0 | -1.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +0.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +4.7 | -3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.6 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.0 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -6.4 | +3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.1 | +2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.2 | +5.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | +0.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.6 | +5.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | -1.5 | -2.6 |
|  | [[Pentamidine (isethionate) (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.5 | -1.4 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -1.4 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.1 — chr3:150,546,678-150,586,016 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EIF-2A |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BY44](https://www.uniprot.org/uniprotkb/Q9BY44) (Eukaryotic translation initiation factor 2A):

> Functions in the early steps of protein synthesis of a small number of specific mRNAs. Acts by directing the binding of methionyl-tRNAi to 40S ribosomal subunits. In contrast to the eIF-2 complex, it binds methionyl-tRNAi to 40S subunits in a codon-dependent manner, whereas the eIF-2 complex binds methionyl-tRNAi to 40S subunits in a GTP-dependent manner.

**Summary**, from NCBI Gene [83939](https://www.ncbi.nlm.nih.gov/gene/83939):

> This gene encodes a eukaryotic translation initiation factor that catalyzes the formation of puromycin-sensitive 80 S preinitiation complexes and the poly(U)-directed synthesis of polyphenylalanine at low concentrations of Mg2+. This gene should not be confused with eIF2-alpha (EIF2S1, Gene ID: 1965), the alpha subunit of the eIF2 translation initiation complex. Although both of these proteins function in binding initiator tRNA to the 40 S ribosomal subunit, the encoded protein does so in a …

**Accessions** — [HGNC:3254](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3254) · Entrez [83939](https://www.ncbi.nlm.nih.gov/gene/83939) · UniProt [Q9BY44](https://www.uniprot.org/uniprotkb/Q9BY44) · Ensembl [ENSG00000144895](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144895)

## Data

Gene col 6944: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6944); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6944, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6944]; `tensor/DDL_lfc|DDL_z.npy` [6944]; `embed/gene_vectors.npy` [6944]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6944 or target_col == 6944). Every well: [[EIF2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
