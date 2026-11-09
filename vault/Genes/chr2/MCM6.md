---
symbol: "MCM6"
type: "gene"
col: 1140
ensembl_id: "ENSG00000076003"
name: "minichromosome maintenance complex component 6"
location: "2q21.3"
module: 6
arm: "+"
pooled_cpm: 31.69
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MCM6

*minichromosome maintenance complex component 6* — 2q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.25× (z +11.8, q 2e-29, up in 36 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.66× (z +7.4, q 1e-11, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.701× (z -7.3, q 1e-10, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM4]] (+0.84, fdr 7e-06), [[MCM3]] (+0.83, fdr 7e-06), [[MCM5]] (+0.80, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1140.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **2.25×** | +11.8 | 2e-29 | 36/41 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.55×** | +9.1 | 2e-17 | 32/45 (NCI-H2347, A549, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.85×** | +8.6 | 1e-15 | 32/46 (SW480, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **1.83×** | +8.5 | 3e-15 | 26/38 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +7.4 | 1e-11 | 32/46 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.68×** | +7.0 | 2e-10 | 25/40 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.64×** | +7.0 | 2e-10 | 28/45 (SW480, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.57×** | +6.5 | 4e-09 | 28/46 (PANC-1, A549, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.47×** | +5.6 | 2e-06 | 23/46 (A549, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.45×** | +5.4 | 4e-06 | 22/46 (A549, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~62% of this change | **1.44×** | +5.2 | 1e-05 | 27/45 (NCI-H2347, A549, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.40×** | +4.7 | 1e-04 | 21/46 (A549, SHP-77, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.24×** | +4.5 | 3e-04 | 20/46 (SW480, A-427, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.4 | 4e-04 | 20/46 (RKO, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.34×** | +4.3 | 7e-04 | 17/46 (SW48, SW480, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.6 | 0.010 | 17/46 (J82, NCI-H2347, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.075 | 7/46 (LoVo, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.087 | 17/45 (NCI-H1792, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1140.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.701×** | -7.3 | 1e-10 | 25/46 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.788×** | -4.9 | 2e-04 | 22/46 (LS 180, COLO 205, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.548×** | -4.6 | 8e-04 | 22/46 (SW 900, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.733×** | -4.5 | 8e-04 | 21/46 (CHP-212, SW 1088, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.749×** | -3.9 | 0.010 | 18/46 (A-427, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.832×** | -3.8 | 0.013 | 15/46 (LOX-IMVI, HCT15, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.834× | -3.8 | 0.014 | 20/46 (Panc 03.27, HOP62, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.787×** | -3.6 | 0.023 | 13/46 (A-427, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.630×** | -3.5 | 0.026 | 14/45 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.652×** | -3.3 | 0.061 | 18/46 (Panc 03.27, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.654×** | -3.2 | 0.061 | 10/45 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.800×** | -3.1 | 0.081 | 18/45 (AN3 CA, J82, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.810×** | -3.1 | 0.089 | 17/46 (A-172, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.84 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1140. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 72.0 | 2 (2 ⚠) | 5 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.72× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -17.0) |
| [[MIA PaCa-2 (line)]] | alt | 43.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -18.4) |
| [[SNU-423 (line)]] | alt | 15.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[A-427 (line)]] | wt | 84.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -17.0) |
| [[A549 (line)]] | wt | 15.2 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +9.4) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[RKO (line)]] | wt | 46.6 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.133× (z -14.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 66.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[HEC-1-A (line)]] | alt | 87.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -9.5) |
| [[J82 (line)]] | alt | 59.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +9.1) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[LOX-IMVI (line)]] | wt | 16.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.99× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | — |
| [[NCI-H23 (line)]] | alt | 53.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 18.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +9.5) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H460 (line)]] | wt | 22.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.52× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | — |
| [[SHP-77 (line)]] | alt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[SW480 (line)]] | alt | 51.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | — |
| [[A-172 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.40 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.31 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1140), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM4]] | +0.84 | +0.85 / +0.82 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[MCM3]] | +0.83 | +0.86 / +0.82 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[MCM5]] | +0.80 | +0.82 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[CDCA7]] | +0.77 | +0.81 / +0.74 | both halves | 7e-06 | STRING 583 |
| [[VRK1]] | +0.77 | +0.78 / +0.73 | both halves | 7e-06 |  |
| [[POLA1]] | +0.76 | +0.79 / +0.77 | both halves | 7e-06 | pathway: Activation of the pre-replicative complex; STRING 956 |
| [[MCM2]] | +0.76 | +0.74 / +0.78 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[CLSPN]] | +0.76 | +0.78 / +0.72 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 953 |
| [[E2F1]] | +0.75 | +0.77 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 483 |
| [[MCM10]] | +0.75 | +0.78 / +0.73 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 999 |
| [[CDC45]] | +0.75 | +0.78 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 999 |
| [[KNTC1]] | +0.75 | +0.74 / +0.73 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 750 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises MCM6's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.14× lower at baseline in the lines without E2F2 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises MCM6's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.37× lower at baseline in the lines without CDC25A | 0.023 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises MCM6's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.49× lower at baseline in the lines without TCF19 | 0.030 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CDCA7]] | B | CDCA7 activity raises MCM6's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.13× lower at baseline in the lines without CDCA7 | 0.088 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[ZNF367]] | C | ZNF367 activity raises MCM6's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.55× lower at baseline in the lines without ZNF367 | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |
| [[PKMYT1]] | C | PKMYT1 activity raises MCM6's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 3.27× lower at baseline in the lines without PKMYT1 | 0.061 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; co-absent with the target |
| [[MCM10]] | C | MCM10 activity raises MCM6's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.21× lower at baseline in the lines without MCM10 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises MCM6's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.29× lower at baseline in the lines without DSCC1 | 0.089 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.798). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.8, -43.1); signed map (-36.5, -46.7). **Vector** length 118, 32.5% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Homology Directed Repair* (reactome, mean cos +0.62 to 32); *Chromosome Maintenance* (reactome, mean cos +0.60 to 29); *HDR through Homologous Recombination (HRR) or Single Strand Annealing (SSA)* (reactome, mean cos +0.62 to 29).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.3 | +8.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~62% of this change | +4.2 | +5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.0 | +9.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +3.9 | +7.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +2.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +0.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +4.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.0 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -3.7 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | minichromosome maintenance complex component 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.3 — chr2:135,839,626-135,876,443 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Mis5 |
| Gene groups (HGNC) | MCM family; minichromosome maintenance 2-7 complex |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 17 pathways, smallest: Unwinding of DNA; Activation of the pre-replicative complex; DNA strand elongation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14566](https://www.uniprot.org/uniprotkb/Q14566) (DNA replication licensing factor MCM6):

> Acts as a component of the MCM2-7 complex (MCM complex) which is the replicative helicase essential for 'once per cell cycle' DNA replication initiation and elongation in eukaryotic cells. Core component of CDC45-MCM-GINS (CMG) helicase, the molecular machine that unwinds template DNA during replication, and around which the replisome is built. The active ATPase sites in the MCM2-7 ring are formed through the interaction surfaces of two neighboring subunits such that a critical structure of a …

**Summary**, from NCBI Gene [4175](https://www.ncbi.nlm.nih.gov/gene/4175):

> The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication related proteins. The MCM complex consisting of this protein and MCM2, 4 and 7 proteins possesses …

**Accessions** — [HGNC:6949](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6949) · Entrez [4175](https://www.ncbi.nlm.nih.gov/gene/4175) · UniProt [Q14566](https://www.uniprot.org/uniprotkb/Q14566) · Ensembl [ENSG00000076003](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076003)

## Data

Gene col 1140: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1140); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1140, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1140]; `tensor/DDL_lfc|DDL_z.npy` [1140]; `embed/gene_vectors.npy` [1140]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1140 or target_col == 1140). Every well: [[MCM6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCM6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
