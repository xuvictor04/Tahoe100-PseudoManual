---
symbol: "ASNSD1"
type: "gene"
col: 6164
ensembl_id: "ENSG00000138381"
name: "asparagine synthetase domain containing 1"
location: "2q32.2"
module: 12
arm: "+"
pooled_cpm: 29.65
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# ASNSD1

*asparagine synthetase domain containing 1* — 2q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.43× (z +13.3, q 1e-37, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.558× (z -9.1, q 7e-17, down in 35 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.616× (z -7.5, q 2e-11, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EBAG9]] (+0.78, fdr 7e-06), [[PHAX]] (+0.76, fdr 7e-06), [[C1orf131]] (+0.75, fdr 7e-06); moves opposite to [[AP2A1]] (-0.64, fdr 1e-05), [[MBOAT7]] (-0.59, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PNPLA4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6164.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **2.43×** | +13.3 | 1e-37 | 45/48 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.61×** | +10.6 | 1e-23 | 36/47 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +9.4 | 8e-19 | 41/47 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.82×** | +9.4 | 8e-19 | 47/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +9.4 | 8e-19 | 39/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +7.4 | 1e-11 | 29/48 (NCI-H2347, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.60×** | +7.3 | 2e-11 | 34/46 (NCI-H1792, SNU-423, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.52×** | +6.6 | 4e-09 | 38/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.45×** | +5.8 | 3e-07 | 33/48 (A498, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.45×** | +5.6 | 1e-06 | 21/37 (NCI-H2030, NCI-H1792, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.42×** | +5.1 | 2e-05 | 22/42 (A498, NCI-H2030, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.36×** | +4.8 | 6e-05 | 25/46 (A-172, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.33×** | +4.5 | 3e-04 | 24/48 (AsPC-1, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.29×** | +4.0 | 0.002 | 17/48 (AsPC-1, J82, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.002 | 21/48 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.59×** | +3.8 | 0.005 | 18/48 (NCI-H23, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.007 | 15/48 (RPMI-7951, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.59×** | +3.4 | 0.020 | 7/47 (HS-578T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.028 | 18/48 (NCI-H1792, C32, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.44×** | +3.0 | 0.075 | 4/48 (PANC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6164.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.558×** | -9.1 | 7e-17 | 35/47 (NCI-H23, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.616×** | -7.5 | 2e-11 | 36/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.676×** | -6.1 | 2e-07 | 34/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.679×** | -6.0 | 3e-07 | 30/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pentagastrin (drug)]] 5 µM |  | 0.864× | -3.2 | 0.17 | 9/48 (NCI-H460, NCI-H2347, …) | top dose only |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.820× | -3.1 | 0.20 | 9/48 (SNU-423, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6164. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 23.4 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +8.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.83× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A549 (line)]] | wt | 28.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +13.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.21× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 27.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.86× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 29.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +17.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.30× (z +13.9) | — |
| [[SW480 (line)]] | alt | 34.8 | 2 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 2.56× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.402× (z -9.0) |
| [[A498 (line)]] | wt | 34.6 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.81× (z +10.5) | — |
| [[BT-474 (line)]] | alt | 21.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +8.8) ⚠ cell-cycle shift, explains ~32% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.143× (z -11.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 25.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +10.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.25× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 41.5 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.47× (z +10.8) | — |
| [[A-172 (line)]] | wt | 36.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +12.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 38.5 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.111× (z -9.2) |
| [[C-33 A (line)]] | alt | 38.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[HepG2_C3A (line)]] | wt | 38.1 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.233× (z -9.3) |
| [[HS-578T (line)]] | alt | 26.6 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.73× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.270× (z -8.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 29.5 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.82× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.264× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 34.8 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.86× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 32.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SW 1271 (line)]] | alt | 45.2 | 0 | 1 | — | [[Menadione (drug)]] 0.5 µM 0.0703× (z -8.6) |
| [[A-427 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6164), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EBAG9]] | +0.78 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[PHAX]] | +0.76 | +0.83 / +0.69 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.75 | +0.88 / +0.61 | both halves | 7e-06 |  |
| [[AGGF1]] | +0.74 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.73 | +0.79 / +0.76 | both halves | 7e-06 | STRING 407 |
| [[FUNDC1]] | +0.72 | +0.82 / +0.59 | both halves | 7e-06 |  |
| [[ERAL1]] | +0.72 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[PEX12]] | +0.72 | +0.78 / +0.57 | both halves | 9e-06 |  |
| [[AASDHPPT]] | +0.71 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[NSMCE3]] | +0.71 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[SNHG11]] | +0.70 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[MRPL58]] | +0.70 | +0.75 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP2A1]] | -0.64 | -0.74 / -0.56 | both halves | 1e-05 |  |
| [[MBOAT7]] | -0.59 | -0.62 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PNPLA4]] | B | PNPLA4 activity lowers ASNSD1's level | lines that do not express PNPLA4 (11) vs lines expressing it (39) | 1.12× higher at baseline in the lines without PNPLA4 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000285679, PRKCZ, GPR160 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.739). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-32.2, 4.0); signed map (2.2, -21.3). **Vector** length 91.5, 21.4% of its response variance represented; |z| ≥ 3 in 838 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.4 | +13.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.0 | +9.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.4 | +9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +6.4 | +10.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.3 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +6.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +1.6 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.8 | -9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.5 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.7 | -6.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.4 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.2 | -7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | +1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.4 | -0.4 |
|  | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | asparagine synthetase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.2 — chr2:189,661,385-189,670,831 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NS3TP1, FLJ20752, NBLA00058 |
| Gene groups (HGNC) | Asparagine synthase family |
| Matched by | ensembl_id |

UniProt [Q9NWL6](https://www.uniprot.org/uniprotkb/Q9NWL6) carries no function annotation.

**Summary**, from NCBI Gene [54529](https://www.ncbi.nlm.nih.gov/gene/54529):

> Predicted to be involved in L-asparagine biosynthetic process. Predicted to act upstream of or within adipose tissue development; skeletal muscle tissue development; and transdifferentiation. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24910](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24910) · Entrez [54529](https://www.ncbi.nlm.nih.gov/gene/54529) · UniProt [Q9NWL6](https://www.uniprot.org/uniprotkb/Q9NWL6) · Ensembl [ENSG00000138381](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138381)

## Data

Gene col 6164: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6164); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6164, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6164]; `tensor/DDL_lfc|DDL_z.npy` [6164]; `embed/gene_vectors.npy` [6164]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6164 or target_col == 6164). Every well: [[ASNSD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASNSD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
