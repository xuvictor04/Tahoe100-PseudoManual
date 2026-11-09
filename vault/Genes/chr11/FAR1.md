---
symbol: "FAR1"
type: "gene"
col: 12429
ensembl_id: "ENSG00000197601"
name: "fatty acyl-CoA reductase 1"
location: "11p15.3"
module: 188
arm: "+"
pooled_cpm: 139.69
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 6
n_dd_up_clean: 19
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/188"]
generated_by: "tahoemap"
---

# FAR1

*fatty acyl-CoA reductase 1* — 11p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.93× (z +10.9, q 5e-25, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.732× (z -5.2, q 1e-04, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METAP1]] (+0.75, fdr 7e-06), [[GPD1L]] (+0.74, fdr 7e-06), [[CCNY]] (+0.72, fdr 7e-06); moves opposite to [[ZNF24]] (-0.68, fdr 7e-06), [[ZNF335]] (-0.67, fdr 7e-06), [[SON]] (-0.67, fdr 1e-05).
> It is in [[Module 188]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GFOD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12429.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.93×** | +10.9 | 5e-25 | 46/47 (LOX-IMVI, HT-29, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.86×** | +10.3 | 2e-22 | 46/47 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.81×** | +9.4 | 1e-18 | 42/47 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.47×** | +7.8 | 7e-13 | 40/47 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.58×** | +7.6 | 4e-12 | 40/47 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +7.1 | 1e-10 | 40/46 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +6.3 | 3e-08 | 36/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +6.2 | 4e-08 | 37/47 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.98×** | +5.9 | 2e-07 | 27/37 (SW480, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +5.0 | 3e-05 | 31/47 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +5.0 | 3e-05 | 30/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +4.9 | 4e-05 | 34/47 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +4.6 | 2e-04 | 26/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +4.5 | 3e-04 | 36/48 (HT-29, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.4 | 4e-04 | 32/44 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.60×** | +4.1 | 0.002 | 26/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.007 | 25/47 (NCI-H1792, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.007 | 24/47 (PANC-1, A-427, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.026 | 25/47 (SW 900, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12429.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.732×** | -5.2 | 1e-04 | 32/47 (LoVo, SW48, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.802×** | -3.7 | 0.068 | 23/48 (RKO, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.813×** | -3.4 | 0.082 | 23/47 (HS-578T, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.815×** | -3.4 | 0.082 | 22/47 (BT-474, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.816×** | -3.4 | 0.082 | 23/48 (Hs 766T, NCI-H2347, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.818×** | -3.3 | 0.082 | 24/47 (SW48, NCI-H460, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.831× | -3.1 | 0.17 | 19/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12429. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 191 | 6 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.05× (z +9.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 1.99× (z +9.5) | — |
| [[A-172 (line)]] | wt | 162 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 112 | 4 | 0 | [[Belinostat (drug)]] 5 µM 2.85× (z +11.1) | — |
| [[PANC-1 (line)]] | alt | 134 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.23× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.14× (z +10.3) | — |
| [[COLO 205 (line)]] | alt | 51.0 | 3 | 0 | [[Belinostat (drug)]] 5 µM 4.08× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 112 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.78× (z +11.0) | — |
| [[LoVo (line)]] | wt | 170 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.11× (z +10.3) ⚠ toxic | [[Auranofin (drug)]] 5 µM 0.467× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 55.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.12× (z +11.4) | — |
| [[NCI-H2347 (line)]] | alt | 156 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.26× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 101 | 3 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.62× (z +10.7) ⚠ unreliable plate only · without an alert: [[Belinostat (drug)]] 5 µM 2.15× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 228 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.36× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 139 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.22× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 58.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.79× (z +9.3) | — |
| [[hTERT-HPNE (line)]] | wt | 70.4 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.98× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 120 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.87× (z +9.1) ⚠ toxic | — |
| [[RKO (line)]] | wt | 174 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -11.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.365× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 181 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.478× (z -9.3) |
| [[SW 1088 (line)]] | alt | 101 | 0 | 1 | — | [[Decitabine (drug)]] 5 µM 0.0903× (z -8.6) |
| [[SW 1271 (line)]] | alt | 131 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.173× (z -8.7) |
| [[SW48 (line)]] | wt | 279 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.340× (z -10.2) |
| [[A-427 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 231 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 183 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 147 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 218 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 170 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 288 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 67.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12429), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METAP1]] | +0.75 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[GPD1L]] | +0.74 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[CCNY]] | +0.72 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[MFSD14B]] | +0.72 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[NUP93]] | +0.72 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[SKP2]] | +0.68 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[WDR5]] | +0.68 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[NTAQ1]] | +0.68 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[OTUD6B]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[GCSH]] | +0.67 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[OLA1]] | +0.67 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[COLGALT1]] | +0.66 | +0.62 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF24]] | -0.68 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[ZNF335]] | -0.67 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[SON]] | -0.67 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[RBBP6]] | -0.67 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[OFD1]] | -0.67 | -0.69 / -0.62 | both halves | 7e-06 |  |
| [[ZNF764]] | -0.67 | -0.68 / -0.46 | both halves | 2e-05 |  |
| [[EP300]] | -0.65 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[BOLA1]] | -0.65 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[RBM23]] | -0.65 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[LINC02307]] | -0.65 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[FAM200A]] | -0.65 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[ANGPT2]] | -0.64 | -0.58 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GFOD1]] | B | GFOD1 activity raises FAR1's level | lines that do not express GFOD1 (5) vs lines expressing it (45) | 1.48× lower at baseline in the lines without GFOD1 | 0.037 | ⚠ within organs, on part of the lines; also absent: SLC2A6, CNKSR3; maybe low, not absent |
| [[GRB14]] | B | GRB14 activity lowers FAR1's level | lines that do not express GRB14 (14) vs lines expressing it (36) | 1.32× higher at baseline in the lines without GRB14 | 0.084 | ⚠ within organs, on part of the lines; also absent: GPR37; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 188]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.865). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.3, -12.0); signed map (-41.0, -14.6). **Vector** length 123, 43.3% of its response variance represented; |z| ≥ 3 in 1,139 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.2 | +7.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.9 | +10.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.8 | +7.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.4 | +4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.9 | +6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.4 | +3.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.2 | +2.5 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.2 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -10.0 | -0.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -8.7 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.8 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.0 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -1.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.4 | -2.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | fatty acyl-CoA reductase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.3 — chr11:13,668,659-13,732,346 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22728, SDR10E1; previously MLSTD2 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Reactome | 2 pathways, smallest: Wax and plasmalogen biosynthesis; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVX9](https://www.uniprot.org/uniprotkb/Q8WVX9) (Fatty acyl-CoA reductase 1):

> Catalyzes the reduction of saturated and unsaturated C16 or C18 fatty acyl-CoA to fatty alcohols. It plays an essential role in the production of ether lipids/plasmalogens which synthesis requires fatty alcohols. In parallel, it is also required for wax monoesters production since fatty alcohols also constitute a substrate for their synthesis (By similarity).

**Summary**, from NCBI Gene [84188](https://www.ncbi.nlm.nih.gov/gene/84188):

> The protein encoded by this gene is required for the reduction of fatty acids to fatty alcohols, a process that is required for the synthesis of monoesters and ether lipids. NADPH is required as a cofactor in this reaction, and 16-18 carbon saturated and unsaturated fatty acids are the preferred substrate. This is a peroxisomal membrane protein, and studies suggest that the N-terminus contains a large catalytic domain located on the outside of the peroxisome, while the C-terminus is exposed to …

**Accessions** — [HGNC:26222](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26222) · Entrez [84188](https://www.ncbi.nlm.nih.gov/gene/84188) · UniProt [Q8WVX9](https://www.uniprot.org/uniprotkb/Q8WVX9) · Ensembl [ENSG00000197601](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197601)

## Data

Gene col 12429: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12429); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12429, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12429]; `tensor/DDL_lfc|DDL_z.npy` [12429]; `embed/gene_vectors.npy` [12429]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12429 or target_col == 12429). Every well: [[FAR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
