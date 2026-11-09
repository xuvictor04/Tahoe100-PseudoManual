---
symbol: "MTFR2"
type: "gene"
col: 7090
ensembl_id: "ENSG00000146410"
name: "mitochondrial fission regulator 2"
location: "6q23.3"
module: 71
arm: "+"
pooled_cpm: 10.68
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# MTFR2

*mitochondrial fission regulator 2* — 6q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (17 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.96× (z +12.5, q 3e-33, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.624× (z -6.0, q 1e-06, down in 13 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Rapamycin (drug)]] 5 µM: 0.801× (z -4.1, q 0.011, down in 15 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYLK2]] (+0.67, fdr 7e-06), [[CHAF1B]] (+0.65, fdr 7e-06), [[PYGM]] (+0.62, fdr 1e-05); moves opposite to [[P2RX4]] (-0.50, fdr 5e-05), [[RNFT1]] (-0.49, fdr 4e-05), [[XPA]] (-0.49, fdr 4e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7090.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +12.5 | 3e-33 | 37/46 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +9.4 | 2e-18 | 29/45 (LOX-IMVI, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.58×** | +8.8 | 4e-16 | 36/47 (PANC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.49×** | +8.6 | 1e-15 | 30/43 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.99×** | +8.4 | 7e-15 | 14/27 (NCI-H460, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.68×** | +6.8 | 8e-10 | 26/47 (SW480, A549, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +6.7 | 2e-09 | 21/48 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.50×** | +6.3 | 2e-08 | 12/20 (PANC-1, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.63×** | +6.2 | 4e-08 | 21/40 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.60×** | +6.2 | 4e-08 | 21/47 (SW480, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.59×** | +6.1 | 7e-08 | 20/47 (NCI-H23, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.5 | 2e-06 | 18/48 (HOP62, J82, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.45×** | +4.9 | 4e-05 | 15/48 (LoVo, NCI-H460, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.55×** | +4.8 | 7e-05 | 18/47 (SW480, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.46×** | +4.7 | 8e-05 | 15/45 (MIA PaCa-2, RKO, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 1e-04 | 18/47 (J82, SK-MEL-2, …) | rises with dose |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.80×** | +4.0 | 0.001 | 9/48 (PANC-1, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.65×** | +3.4 | 0.015 | 5/46 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.045 | 3/48 (SW480, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.057 | 10/46 (BT-474, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Pyridoxine (drug)]] 0.05 µM |  | **1.25×** | +2.9 | 0.069 | 2/48 (hTERT-HPNE, HCT15) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.24×** | +2.8 | 0.092 | 14/44 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7090.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.624×** | -6.0 | 1e-06 | 13/21 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 5 µM |  | **0.801×** | -4.1 | 0.011 | 15/48 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.752×** | -3.8 | 0.033 | 21/35 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **0.759×** | -3.6 | 0.040 | 14/47 (SW 1271, NCI-H661, …) | rises with dose |  |
| [[Erlotinib (drug)]] 5 µM |  | **0.755×** | -3.6 | 0.041 | 12/47 (J82, LOX-IMVI, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -3.5 | 0.048 | 13/48 (A-172, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **0.782×** | -3.2 | 0.099 | 11/43 (NCI-H2347, A-427, …) | inconsistent across doses | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 0.848× | -3.1 | 0.15 | 5/48 (LOX-IMVI, SW 1271, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.851× | -3.0 | 0.16 | 10/48 (SHP-77, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.64 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7090. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 13.7 | 0 | 1 | — | [[Ponatinib (drug)]] 0.5 µM 0.190× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 4.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +11.4) | — |
| [[COLO 205 (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -8.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 6.36 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.115× (z -8.5) |
| [[LoVo (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -11.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.63× (z +10.3) | — |
| [[PANC-1 (line)]] | alt | 12.1 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.25× (z +8.8) | — |
| [[RKO (line)]] | wt | 15.5 | 0 | 1 | — | [[MK-3903 (drug)]] 5 µM 0.0415× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -8.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 17.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.126× (z -10.8) |
| [[SW480 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -16.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7090), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYLK2]] | +0.67 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[CHAF1B]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[PYGM]] | +0.62 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[LINC02236]] | +0.61 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[TOPBP1]] | +0.60 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[CDCA5]] | +0.57 | +0.55 / +0.60 | both halves | 1e-05 | STRING 518 |
| [[CHEK1]] | +0.57 | +0.59 / +0.61 | both halves | 7e-06 | STRING 430 |
| [[TRIP13]] | +0.57 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[ORC1]] | +0.56 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[PITRM1-AS1]] | +0.56 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[ZNF695]] | +0.56 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[CDC6]] | +0.56 | +0.62 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P2RX4]] | -0.50 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[RNFT1]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[XPA]] | -0.49 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[SYP]] | -0.49 | -0.45 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises MTFR2's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.68× lower at baseline in the lines without E2F2 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MTFR2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.569). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-30.7, -48.1); signed map (-37.7, -51.3). **Vector** length 75.9, 13.5% of its response variance represented; |z| ≥ 3 in 987 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +12.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | +4.0 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +3.8 | +8.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.5 | +6.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.3 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +5.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.8 | +4.0 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.8 | -3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial fission regulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.3 — chr6:136,231,024-136,250,335 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DUFD1, FAM54A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P444](https://www.uniprot.org/uniprotkb/Q6P444) (Mitochondrial fission regulator 2):

> May play a role in mitochondrial aerobic respiration essentially in the testis. Can also promote mitochondrial fission (By similarity).

**Summary**, from NCBI Gene [113115](https://www.ncbi.nlm.nih.gov/gene/113115):

> Predicted to be involved in aerobic respiration and mitochondrial fission. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21115](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21115) · Entrez [113115](https://www.ncbi.nlm.nih.gov/gene/113115) · UniProt [Q6P444](https://www.uniprot.org/uniprotkb/Q6P444) · Ensembl [ENSG00000146410](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146410)

## Data

Gene col 7090: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7090); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7090, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7090]; `tensor/DDL_lfc|DDL_z.npy` [7090]; `embed/gene_vectors.npy` [7090]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7090 or target_col == 7090). Every well: [[MTFR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTFR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
