---
symbol: "OSGEPL1"
type: "gene"
col: 4913
ensembl_id: "ENSG00000128694"
name: "O-sialoglycoprotein endopeptidase like 1"
location: "2q32.2"
module: 16
arm: "+"
pooled_cpm: 6.87
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 16
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# OSGEPL1

*O-sialoglycoprotein endopeptidase like 1* — 2q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.00× (z +8.8, q 5e-16, up in 5 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.69× (z +7.0, q 8e-10, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.375× (z -12.9, q 3e-35, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SF3B3]] (+0.64, fdr 1e-05), [[MMACHC]] (+0.62, fdr 1e-05), [[DUSP19]] (+0.62, fdr 1e-05); moves opposite to [[ZBTB46]] (-0.55, fdr 2e-05), [[SLC25A29]] (-0.55, fdr 1e-05), [[SAMD4B]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[WNT9A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4913.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +8.8 | 5e-16 | 5/12 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.69×** | +7.0 | 8e-10 | 27/47 (PANC-1, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +6.9 | 1e-09 | 18/47 (A-427, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.50×** | +5.2 | 3e-05 | 14/34 (Panc 03.27, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.46×** | +5.0 | 5e-05 | 17/47 (A549, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.43×** | +4.8 | 2e-04 | 10/46 (PANC-1, A-427, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.40×** | +4.3 | 0.001 | 12/42 (SNU-423, LOX-IMVI, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.35×** | +4.0 | 0.005 | 16/47 (LoVo, A549, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.34×** | +3.8 | 0.008 | 7/46 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.016 | 7/47 (PANC-1, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.30×** | +3.6 | 0.019 | 10/30 (LS 180, J82, …) | rises with dose | composition shift |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.30×** | +3.4 | 0.033 | 3/47 (LOX-IMVI, HepG2/C3A, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.040 | 2/47 (HEC-1-A, RPMI-7951) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.049 | 5/48 (Panc 03.27, LoVo, …) | rises with dose |  |
| [[Busulfan (drug)]] 5 µM |  | 1.17× | +3.0 | 0.094 | 4/48 (MIA PaCa-2, SNU-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.098 | 10/45 (SW480, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4913.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.375×** | -12.9 | 3e-35 | 32/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.392×** | -12.3 | 3e-32 | 35/47 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.406×** | -11.8 | 4e-30 | 35/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.448×** | -10.5 | 9e-24 | 32/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.469×** | -9.9 | 4e-21 | 33/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.513×** | -8.7 | 2e-16 | 30/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.546×** | -7.5 | 6e-12 | 25/44 (SW480, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.867× | -6.1 | 6e-08 | 14/48 (SW 900, LS 180, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.766×** | -4.9 | 6e-05 | 20/44 (SHP-77, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.717×** | -4.2 | 0.001 | 17/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.693×** | -3.4 | 0.031 | 5/47 (LOX-IMVI, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.761×** | -3.4 | 0.031 | 12/38 (NCI-H23, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.771×** | -3.4 | 0.032 | 8/47 (SW1417, NCI-H2030, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.777×** | -3.3 | 0.044 | 11/47 (NCI-H23, SW1417, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.774×** | -3.2 | 0.045 | 13/46 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.839× | -3.2 | 0.048 | 10/47 (J82, Panc 03.27, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.848× | -3.0 | 0.081 | 4/48 (MIA PaCa-2, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4913. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.47 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0437× (z -22.0) |
| [[SW480 (line)]] | alt | 8.55 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.192× (z -11.0) |
| [[BT-474 (line)]] | alt | 3.99 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0291× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 5.59 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0947× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 4.58 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0612× (z -10.7) |
| [[LS 180 (line)]] | wt | 6.76 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0788× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 7.60 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.124× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.164× (z -9.6) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 8.09 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0846× (z -14.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0943× (z -9.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -10.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SNU-423 (line)]] | alt | 6.06 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0897× (z -9.1) |
| [[A-172 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4913), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SF3B3]] | +0.64 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[MMACHC]] | +0.62 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[DUSP19]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[MANEA]] | +0.61 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[MBLAC2]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[POMK]] | +0.56 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[ALG10]] | +0.56 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[TRUB1]] | +0.55 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[NUDT6]] | +0.55 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[FANCF]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[THNSL1]] | +0.55 | +0.55 / +0.56 | both halves | 1e-05 | STRING 443 |
| [[BBS10]] | +0.55 | +0.62 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB46]] | -0.55 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[SLC25A29]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[SAMD4B]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[CDC34]] | -0.52 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[GDI1]] | -0.52 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[WNT9A]] | -0.51 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[MIR22HG]] | -0.51 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[MROH1]] | -0.50 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[FRMD8]] | -0.50 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[STX12]] | -0.49 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[WNT2B]] | -0.49 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[MAP2K2]] | -0.49 | -0.50 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNT9A]] | B | WNT9A activity raises OSGEPL1's level | lines that do not express WNT9A (11) vs lines expressing it (39) | 1.48× lower at baseline in the lines without WNT9A | 0.012 | ⚠ within organs, on part of the lines; also absent: RAB6B, DZIP1L, MRAS |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.377). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.2, 20.2); signed map (9.7, -40.1). **Vector** length 56.5, 7.82% of its response variance represented; |z| ≥ 3 in 953 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.5 | +6.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | -2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | +1.7 | +5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.2 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.1 | -0.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.0 | -10.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.5 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -8.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.4 | -9.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.3 | -11.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.7 | -3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.4 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | O-sialoglycoprotein endopeptidase like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.2 — chr2:189,746,660-189,763,227 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Qri7, OSGEPL |
| Gene groups (HGNC) | OSGEP family |
| Reactome | 3 pathways, smallest: tRNA modification in the mitochondrion; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4B0](https://www.uniprot.org/uniprotkb/Q9H4B0) (tRNA N6-adenosine threonylcarbamoyltransferase, mitochondrial):

> Required for the formation of a threonylcarbamoyl group on adenosine at position 37 (t(6)A37) in mitochondrial tRNAs that read codons beginning with adenine. Probably involved in the transfer of the threonylcarbamoyl moiety of threonylcarbamoyl-AMP (TC-AMP) to the N6 group of A37. Involved in mitochondrial genome maintenance.

**Summary**, from NCBI Gene [64172](https://www.ncbi.nlm.nih.gov/gene/64172):

> Enables tRNA N(6)-L-threonylcarbamoyladenine synthase activity. Involved in tRNA threonylcarbamoyladenosine modification. Is active in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23075](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23075) · Entrez [64172](https://www.ncbi.nlm.nih.gov/gene/64172) · UniProt [Q9H4B0](https://www.uniprot.org/uniprotkb/Q9H4B0) · Ensembl [ENSG00000128694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128694)

## Data

Gene col 4913: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4913); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4913, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4913]; `tensor/DDL_lfc|DDL_z.npy` [4913]; `embed/gene_vectors.npy` [4913]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4913 or target_col == 4913). Every well: [[OSGEPL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSGEPL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
