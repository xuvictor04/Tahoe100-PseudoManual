---
symbol: "TADA2B"
type: "gene"
col: 10329
ensembl_id: "ENSG00000173011"
name: "transcriptional adaptor 2B"
location: "4p16.1"
module: 107
arm: "+"
pooled_cpm: 10.28
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# TADA2B

*transcriptional adaptor 2B* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.10× (z +5.4, q 2e-05, up in 2 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.22× (z +4.5, q 0.001, up in 14 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.765× (z -6.1, q 5e-07, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF746]] (+0.68, fdr 7e-06), [[GCC1]] (+0.68, fdr 1e-05), [[GFER]] (+0.63, fdr 1e-05); moves opposite to [[RTKN2]] (-0.57, fdr 1e-05), [[FAM81A]] (-0.56, fdr 2e-05).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10329.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.4 | 2e-05 | 2/48 (MIA PaCa-2, NCI-H23) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +5.4 | 2e-05 | 20/41 (HS-578T, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +4.5 | 0.001 | 14/43 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.19× | +4.1 | 0.006 | 14/47 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.011 | 13/46 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.012 | 16/42 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.8 | 0.014 | 11/44 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.036 | 6/46 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +3.4 | 0.046 | 16/39 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.046 | 5/47 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.061 | 3/48 (MIA PaCa-2, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.061 | 6/47 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.093 | 4/46 (PANC-1, AsPC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10329.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.765×** | -6.1 | 5e-07 | 21/48 (NCI-H1573, NCI-H661, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.701×** | -5.8 | 2e-06 | 20/46 (RPMI-7951, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.701×** | -5.5 | 6e-06 | 12/19 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.737×** | -4.7 | 3e-04 | 20/46 (BT-474, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.774×** | -4.1 | 0.004 | 10/47 (NCI-H1573, LoVo, …) | all doses, flat | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.778×** | -4.1 | 0.004 | 19/34 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.814×** | -3.3 | 0.064 | 15/47 (NCI-H1573, HT-29, …) | all doses, flat | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.815×** | -3.3 | 0.064 | 8/47 (NCI-H2030, SNU-1, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.810×** | -3.3 | 0.067 | 16/44 (A-427, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10329. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 13.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0990× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[A-427 (line)]] | wt | 7.86 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -9.0) ⚠ cell-cycle shift, explains ~61% of this change |
| [[A498 (line)]] | wt | 17.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -12.5) |
| [[A549 (line)]] | wt | 9.33 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0863× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HCT15 (line)]] | alt | 13.6 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0948× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.268× (z -8.7) ⚠ toxic |
| [[J82 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[KATO III (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[Panc 03.27 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SW480 (line)]] | alt | 8.34 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0989× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10329), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF746]] | +0.68 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[GCC1]] | +0.68 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[GFER]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[TSSC4]] | +0.63 | +0.60 / +0.57 | both halves | 8e-06 |  |
| [[GORASP1]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[NME6]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[ZNF768]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ZNF282]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[LRRC47]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ZNF419]] | +0.59 | +0.49 / +0.52 | both halves | 2e-05 |  |
| [[ZNF777]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[KTI12]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTKN2]] | -0.57 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[FAM81A]] | -0.56 | -0.48 / -0.66 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TADA2B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[RNF135]] | B | RNF135 activity raises TADA2B's level | lines that do not express RNF135 (6) vs lines expressing it (44) | 1.36× lower at baseline in the lines without RNF135 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000291063, TMEM54, ENSG00000266865; its own permutation p |
| [[SDK1]] | B | SDK1 activity lowers TADA2B's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 1.20× higher at baseline in the lines without SDK1 | 0.098 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.701). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.7, -1.4); signed map (-6.0, -23.3). **Vector** length 65.6, 9.83% of its response variance represented; |z| ≥ 3 in 821 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +3.4 | +4.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.3 | +3.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.2 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.2 | +3.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | -5.3 | -4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -4.4 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.3 | -5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -4.2 | -2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | transcriptional adaptor 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:7,041,899-7,057,952 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC21874 |
| Gene groups (HGNC) | Zinc fingers ZZ-type; Myb/SANT domain containing; SAGA complex |
| Reactome | 5 pathways, smallest: HATs acetylate histones; Ub-specific processing proteases; Chromatin modifying enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86TJ2](https://www.uniprot.org/uniprotkb/Q86TJ2) (Transcriptional adapter 2-beta):

> Coactivates PAX5-dependent transcription together with either SMARCA4 or GCN5L2.

**Summary**, from NCBI Gene [93624](https://www.ncbi.nlm.nih.gov/gene/93624):

> TADA2B functions as a transcriptional adaptor protein that potentiates transcription through coordination of histone acetyltransferase (HAT) activity and by linking activation factors to basal transcriptional machinery (Barlev et al., 2003 [PubMed 12972612]).[supplied by OMIM, Apr 2010]

**Accessions** — [HGNC:30781](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30781) · Entrez [93624](https://www.ncbi.nlm.nih.gov/gene/93624) · UniProt [Q86TJ2](https://www.uniprot.org/uniprotkb/Q86TJ2) · Ensembl [ENSG00000173011](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173011)

## Data

Gene col 10329: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10329); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10329, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10329]; `tensor/DDL_lfc|DDL_z.npy` [10329]; `embed/gene_vectors.npy` [10329]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10329 or target_col == 10329). Every well: [[TADA2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TADA2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
