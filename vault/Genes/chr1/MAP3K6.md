---
symbol: "MAP3K6"
type: "gene"
col: 6652
ensembl_id: "ENSG00000142733"
name: "mitogen-activated protein kinase kinase kinase 6"
location: "1p36.11"
module: 2
arm: "+"
pooled_cpm: 7.46
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 29
n_dd_up_clean: 8
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# MAP3K6

*mitogen-activated protein kinase kinase kinase 6* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Budesonide (drug)]] 0.5 µM: 1.53× (z +4.8, q 0.001, up in 17 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.308× (z -18.5, q 0e+00, down in 41 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGGHG]] (+0.58, fdr 2e-05), [[TMEM164]] (+0.55, fdr 3e-05), [[PLCG1]] (+0.54, fdr 3e-05); moves opposite to [[SEMA3A]] (-0.49, fdr 4e-05), [[MFSD4B]] (-0.48, fdr 3e-05), [[GEM]] (-0.47, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADCY3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6652.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 0.5 µM |  | **1.53×** | +4.8 | 0.001 | 17/44 (NCI-H2347, NCI-H1573, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.017 | 14/46 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.40×** | +3.8 | 0.028 | 10/45 (NCI-H1573, LOX-IMVI, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.028 | 15/44 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.56×** | +3.6 | 0.039 | 7/35 (J82, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.37×** | +3.5 | 0.039 | 11/45 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.37×** | +3.3 | 0.077 | 10/42 (NCI-H1573, NCI-H2030, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.083 | 15/43 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.33× | +3.1 | 0.10 | 6/44 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | 1.32× | +3.1 | 0.10 | 7/45 (SHP-77, LS 180, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.35× | +3.1 | 0.10 | 5/22 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.31× | +3.0 | 0.11 | 11/47 (SW1417, HT-29, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.45× | +3.0 | 0.12 | 8/45 (PANC-1, SNU-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 3 with an alert ⚠; shown: the 15 strongest. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6652.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.308×** | -18.5 | 0e+00 | 41/42 (LoVo, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.251×** | -15.3 | 0e+00 | 33/41 (HS-578T, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.291×** | -13.7 | 3e-40 | 42/45 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.316×** | -12.8 | 4e-35 | 40/46 (HS-578T, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.352×** | -11.6 | 7e-29 | 42/46 (HS-578T, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.430×** | -9.0 | 2e-17 | 32/43 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.535×** | -6.9 | 4e-10 | 28/45 (RKO, HCT15, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.542×** | -6.8 | 9e-10 | 29/46 (HS-578T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.330×** | -6.4 | 9e-09 | 27/45 (LOX-IMVI, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.665×** | -6.4 | 1e-08 | 25/46 (HS-578T, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.357×** | -6.0 | 1e-07 | 24/45 (A498, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.592×** | -5.8 | 3e-07 | 24/45 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.602×** | -5.6 | 9e-07 | 22/46 (SNU-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.628×** | -5.1 | 1e-05 | 20/45 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.638×** | -5.0 | 3e-05 | 21/46 (LoVo, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6652. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 21.1 | 0 | 6 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0615× (z -17.2) |
| [[LoVo (line)]] | wt | 10.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -18.5) |
| [[A-172 (line)]] | wt | 5.55 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0420× (z -12.3) |
| [[BT-474 (line)]] | alt | 11.6 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0374× (z -14.4) |
| [[C-33 A (line)]] | alt | 12.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0959× (z -13.7) |
| [[Hs 766T (line)]] | wt | 18.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0764× (z -18.0) |
| [[NCI-H1573 (line)]] | alt | 7.38 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0956× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 9.87 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.129× (z -9.7) |
| [[C32 (line)]] | wt | 14.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -12.8) |
| [[HCT15 (line)]] | alt | 8.85 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0762× (z -8.6) |
| [[HOP62 (line)]] | alt | 6.46 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -9.6) |
| [[LS 180 (line)]] | wt | 6.06 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0314× (z -14.3) |
| [[NCI-H2030 (line)]] | alt | 9.17 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -16.1) |
| [[PANC-1 (line)]] | alt | 8.06 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -13.0) |
| [[RKO (line)]] | wt | 6.00 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0565× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 14.4 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.102× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.239× (z -10.2) |
| [[A498 (line)]] | wt | 5.23 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -8.6) |
| [[H4 (line)]] | wt | 6.81 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0483× (z -8.6) |
| [[J82 (line)]] | alt | 8.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 8.07 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.107× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 3.90 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0657× (z -11.0) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 4.84 | 0 | 1 | — | [[Lactate (calcium) (drug)]] 0.5 µM 0.0468× (z -10.6) |
| [[SNU-1 (line)]] | wt | 8.18 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0470× (z -9.8) |
| [[SNU-423 (line)]] | alt | 4.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -9.9) |
| [[SW 900 (line)]] | alt | 4.95 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0730× (z -8.5) |
| [[A-427 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6652), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGGHG]] | +0.58 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[TMEM164]] | +0.55 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[PLCG1]] | +0.54 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[NRBP2]] | +0.54 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[TFCP2L1]] | +0.53 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[MARVELD1]] | +0.53 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[ARRDC1]] | +0.53 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[TRABD2B]] | +0.53 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[MAPK12]] | +0.53 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[ATP1A1]] | +0.51 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[SHC1]] | +0.50 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[ADCK5]] | +0.50 | +0.58 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA3A]] | -0.49 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[MFSD4B]] | -0.48 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[GEM]] | -0.47 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[KCNIP4]] | -0.46 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[KIAA1217]] | -0.43 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[PKD1L2]] | -0.43 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[PRKAA2]] | -0.42 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[BTG1]] | -0.42 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[CHURC1]] | -0.41 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[CCDC148]] | -0.41 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[CRLF2]] | -0.41 | -0.29 / -0.37 | both halves | 2e-04 |  |
| [[HIF1A-AS3]] | -0.41 | -0.34 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | B | ADCY3 activity raises MAP3K6's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.65× lower at baseline in the lines without ADCY3 | 0.083 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[NR3C1]] | B | NR3C1 activity raises MAP3K6's level | compounds that target NR3C1: 2 of 3 raise it (Betamethasone dipropionate, Budesonide) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.429). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (32.2, 13.9); signed map (21.0, 33.2). **Vector** length 75.4, 14.4% of its response variance represented; |z| ≥ 3 in 1,092 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Budesonide (drug)]] 5 µM |  | +3.2 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +0.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.4 | +3.2 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.4 | +4.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.4 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -15.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -6.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.9 | -5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.7 | -18.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.7 | -3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -1.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -6.9 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:27,355,184-27,366,961 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MAPKKK6, ASK2, MEKK6 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; STE11 kinase family |
| Hallmark sets | MYC_TARGETS_V2 |
| Matched by | ensembl_id |

**Function**, from UniProt [O95382](https://www.uniprot.org/uniprotkb/O95382) (Mitogen-activated protein kinase kinase kinase 6):

> Component of a protein kinase signal transduction cascade. Activates the JNK, but not ERK or p38 kinase pathways.

**Summary**, from NCBI Gene [9064](https://www.ncbi.nlm.nih.gov/gene/9064):

> This gene encodes a serine/threonine protein kinase that forms a component of protein kinase-mediated signal transduction cascades. The encoded kinase participates in the regulation of vascular endothelial growth factor (VEGF) expression. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:6858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6858) · Entrez [9064](https://www.ncbi.nlm.nih.gov/gene/9064) · UniProt [O95382](https://www.uniprot.org/uniprotkb/O95382) · Ensembl [ENSG00000142733](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142733)

## Data

Gene col 6652: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6652); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6652, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6652]; `tensor/DDL_lfc|DDL_z.npy` [6652]; `embed/gene_vectors.npy` [6652]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6652 or target_col == 6652). Every well: [[MAP3K6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
