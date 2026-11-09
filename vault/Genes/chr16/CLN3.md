---
symbol: "CLN3"
type: "gene"
col: 12029
ensembl_id: "ENSG00000188603"
name: "CLN3 lysosomal/endosomal transmembrane protein, battenin"
location: "16p12.1"
module: 122
arm: "+"
pooled_cpm: 11.37
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 9
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# CLN3

*CLN3 lysosomal/endosomal transmembrane protein, battenin* — 16p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.49× (z +7.5, q 3e-11, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.662× (z -7.8, q 4e-12, down in 29 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEXA]] (+0.70, fdr 7e-06), [[WASHC2C]] (+0.65, fdr 7e-06), [[ATP6V0E1]] (+0.65, fdr 7e-06); moves opposite to [[PLGRKT]] (-0.57, fdr 2e-05), [[BZW1]] (-0.55, fdr 1e-05), [[CFL1]] (-0.52, fdr 1e-04).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CD59]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12029.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +7.5 | 3e-11 | 32/48 (RKO, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +7.5 | 3e-11 | 23/37 (Panc 03.27, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +5.9 | 6e-07 | 20/47 (PANC-1, A-427, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +5.8 | 8e-07 | 23/47 (KATO III, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +5.1 | 4e-05 | 13/29 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[NG25 (drug)]] 5 µM |  | **2.16×** | +5.0 | 5e-05 | 21/43 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +4.9 | 7e-05 | 13/22 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +4.4 | 8e-04 | 20/45 (COLO 205, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +4.3 | 0.001 | 13/45 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.002 | 16/47 (BT-474, A498, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.004 | 13/47 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.006 | 7/47 (SW480, BT-474, …) | top dose only | plate-row cell shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.006 | 8/48 (AsPC-1, LS 180, …) | two highest doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.7 | 0.007 | 15/40 (SW480, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +3.6 | 0.010 | 13/47 (KATO III, A-172, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.011 | 14/48 (SW 900, CHP-212, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.014 | 12/48 (SK-MEL-2, SW480, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.027 | 14/47 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.028 | 12/47 (RKO, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12029.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -7.8 | 4e-12 | 29/46 (MIA PaCa-2, C32, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.568×** | -7.6 | 1e-11 | 27/47 (SW480, A549, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.632×** | -6.1 | 2e-07 | 22/45 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.712×** | -4.4 | 0.002 | 19/46 (NCI-H23, NCI-H460, …) | top dose only | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **0.538×** | -4.1 | 0.006 | 16/43 (J82, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.782×** | -3.3 | 0.073 | 12/47 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.783×** | -3.3 | 0.073 | 18/47 (SNU-1, A-427, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.784×** | -3.3 | 0.073 | 18/47 (SW1417, A-172, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.777×** | -3.2 | 0.073 | 15/45 (C-33 A, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12029. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 16.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.216× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 12.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +13.7) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[C32 (line)]] | wt | 7.89 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 8.36 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -8.8) |
| [[HOP62 (line)]] | alt | 4.94 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -9.6) ⚠ cell-cycle shift, explains ~55% of this change |
| [[J82 (line)]] | alt | 7.89 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +9.0) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[LoVo (line)]] | wt | 8.81 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.186× (z -9.2) ⚠ cell-cycle shift, explains ~20% of this change |
| [[MIA PaCa-2 (line)]] | alt | 19.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -10.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -10.4) |
| [[A-172 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12029), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEXA]] | +0.70 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[WASHC2C]] | +0.65 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[ATP6V0E1]] | +0.65 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[VPS41]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[RRAGB]] | +0.65 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[SPNS1]] | +0.64 | +0.66 / +0.65 | both halves | 7e-06 | STRING 413 |
| [[SLC26A11]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[WASHC2A]] | +0.62 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[AP5Z1]] | +0.62 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[TSC1]] | +0.61 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SLC38A7]] | +0.60 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ATP6V1C1]] | +0.60 | +0.63 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLGRKT]] | -0.57 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[BZW1]] | -0.55 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[CFL1]] | -0.52 | -0.34 / -0.66 | both halves | 1e-04 |  |
| [[HAS3]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[CPSF3]] | -0.50 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[NT5E]] | -0.50 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[SPRY4-AS1]] | -0.49 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[CCNYL1]] | -0.49 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[FOXL1]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[SLC4A7]] | -0.49 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[C11orf24]] | -0.49 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[ADARB1]] | -0.49 | -0.49 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD59]] | B | CD59 activity lowers CLN3's level | lines that do not express CD59 (7) vs lines expressing it (43) | 1.37× higher at baseline in the lines without CD59 | 0.083 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers CLN3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-19.1, 14.0); signed map (-10.3, -19.7). **Vector** length 86.9, 17.7% of its response variance represented; |z| ≥ 3 in 840 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.4 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.3 | +3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.0 | +4.3 |
|  | [[NG25 (drug)]] 5 µM |  | +4.0 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.8 | +4.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.6 | -7.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.9 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -7.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | CLN3 lysosomal/endosomal transmembrane protein, battenin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.1 — chr16:28,474,111-28,495,575 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BTN1, JNCL, SLC29B1; previously BTS |
| Gene groups (HGNC) | Solute carrier family 29 |
| Reactome | 2 pathways, smallest: Glycosphingolipid transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13286](https://www.uniprot.org/uniprotkb/Q13286) (Battenin):

> Mediates microtubule-dependent, anterograde transport connecting the Golgi network, endosomes, autophagosomes, lysosomes and plasma membrane, and participates in several cellular processes such as regulation of lysosomal pH, lysosome protein degradation, receptor-mediated endocytosis, autophagy, transport of proteins and lipids from the TGN, apoptosis and synaptic transmission. Facilitates the proteins transport from trans-Golgi network (TGN)-to other membrane compartments such as transport of …

**Summary**, from NCBI Gene [1201](https://www.ncbi.nlm.nih.gov/gene/1201):

> This gene encodes a protein that is involved in lysosomal function. Mutations in this, as well as other neuronal ceroid-lipofuscinosis (CLN) genes, cause neurodegenerative diseases commonly known as Batten disease or collectively known as neuronal ceroid lipofuscinoses (NCLs). Many alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2074](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2074) · Entrez [1201](https://www.ncbi.nlm.nih.gov/gene/1201) · UniProt [Q13286](https://www.uniprot.org/uniprotkb/Q13286) · Ensembl [ENSG00000188603](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188603)

## Data

Gene col 12029: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12029); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12029, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12029]; `tensor/DDL_lfc|DDL_z.npy` [12029]; `embed/gene_vectors.npy` [12029]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12029 or target_col == 12029). Every well: [[CLN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
