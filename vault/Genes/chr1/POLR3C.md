---
symbol: "POLR3C"
type: "gene"
col: 11782
ensembl_id: "ENSG00000186141"
name: "RNA polymerase III subunit C"
location: "1q21.1"
module: 11
arm: "+"
pooled_cpm: 27.7
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# POLR3C

*RNA polymerase III subunit C* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.93× (z +19.6, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.545× (z -12.8, q 6e-35, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF115]] (+0.84, fdr 7e-06, ⚠ same locus), [[ZC3HC1]] (+0.79, fdr 7e-06), [[LATS1]] (+0.76, fdr 7e-06), [[ZNF253]] (+0.75, fdr 1e-05); moves opposite to [[UBA6]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11782.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +19.6 | 0e+00 | 44/47 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.26×** | +17.2 | 0e+00 | 44/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.98×** | +13.9 | 2e-41 | 42/48 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.72×** | +11.4 | 5e-28 | 39/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +10.3 | 6e-23 | 32/45 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +8.5 | 2e-15 | 33/48 (LOX-IMVI, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.13×** | +7.6 | 3e-12 | 30/46 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +7.5 | 4e-12 | 23/48 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +7.2 | 4e-11 | 31/49 (LoVo, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +6.4 | 8e-09 | 23/46 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +6.2 | 3e-08 | 22/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.29×** | +5.4 | 4e-06 | 18/48 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +4.8 | 6e-05 | 20/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +4.5 | 3e-04 | 11/48 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.51×** | +4.1 | 0.001 | 5/48 (MIA PaCa-2, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +4.1 | 0.001 | 14/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.012 | 12/47 (H4, NCI-H460, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.3 | 0.028 | 3/48 (BT-474, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11782.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.545×** | -12.8 | 6e-35 | 39/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.580×** | -11.6 | 2e-28 | 37/48 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.661×** | -8.8 | 4e-16 | 33/47 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.738×** | -6.4 | 2e-08 | 26/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.805×** | -4.6 | 4e-04 | 20/45 (NCI-H1573, SHP-77, …) | two highest doses | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.858× | -4.6 | 4e-04 | 18/48 (SW480, RKO, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.807×** | -4.4 | 9e-04 | 18/46 (NCI-H23, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.825×** | -3.9 | 0.006 | 16/36 (SHP-77, KATO III, …) | two highest doses | composition shift |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | 0.893× | -3.4 | 0.043 | 4/48 (CHP-212, SW 1271, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11782. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 32.5 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.348× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 38.8 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.240× (z -14.1) |
| [[J82 (line)]] | alt | 22.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +13.1) | — |
| [[KATO III (line)]] | alt | 24.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.255× (z -10.6) |
| [[PANC-1 (line)]] | alt | 24.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +11.4) | — |
| [[A498 (line)]] | wt | 19.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +12.5) | — |
| [[HOP62 (line)]] | alt | 21.8 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.81× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 19.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 31.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.26× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.159× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[A-172 (line)]] | wt | 35.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.3) | — |
| [[A549 (line)]] | wt | 31.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.2) | — |
| [[AN3 CA (line)]] | alt | 38.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.129× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 23.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +11.9) | — |
| [[COLO 205 (line)]] | alt | 31.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -12.4) |
| [[Hs 766T (line)]] | wt | 25.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +8.9) | — |
| [[LoVo (line)]] | wt | 25.2 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.96× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 18.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 19.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.417× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 25.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[NCI-H2030 (line)]] | alt | 28.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 78.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -23.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[A-427 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11782), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF115]] | +0.84 | +0.82 / +0.73 | both halves | 7e-06 | STRING 594; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ZC3HC1]] | +0.79 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[LATS1]] | +0.76 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[ZNF253]] | +0.75 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[RPP38]] | +0.75 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[TMEM192]] | +0.73 | +0.76 / +0.54 | both halves | 1e-05 |  |
| [[ARL14EP]] | +0.72 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[ZFX]] | +0.71 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[INTS14]] | +0.71 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[NAIF1]] | +0.71 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[NKAPD1]] | +0.71 | +0.78 / +0.53 | both halves | 1e-05 |  |
| [[ZFY]] | +0.70 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[YJU2]] | +0.70 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBA6]] | -0.68 | -0.67 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises POLR3C's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[IL1RAP]] | B | IL1RAP activity lowers POLR3C's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 1.35× higher at baseline in the lines without IL1RAP | 0.088 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.721). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.5, 8.0); signed map (3.7, -21.8). **Vector** length 108, 26.0% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.4 | +17.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.2 | +19.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.6 | +13.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.0 | +10.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.1 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +7.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.2 | +3.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.1 | +3.0 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.2 | -12.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.6 | -11.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.5 | -8.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.3 | -6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -2.4 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase III subunit C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.1 — chr1:145,824,053-145,844,402 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPC62, RPC3, C82 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 10 pathways, smallest: RNA Polymerase III Chain Elongation; RNA Polymerase III Transcription Termination; RNA Polymerase III Transcription Initiation From Type 2 Promoter |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUI4](https://www.uniprot.org/uniprotkb/Q9BUI4) (DNA-directed RNA polymerase III subunit RPC3):

> DNA-dependent RNA polymerase catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. Specific peripheric component of RNA polymerase III (Pol III) which synthesizes small non-coding RNAs including 5S rRNA, snRNAs, tRNAs and miRNAs from at least 500 distinct genomic loci. Part of POLR3C/RPC3-POLR3F/RPC6-POLR3G/RPC7 heterotrimer, coordinates the dynamics of Pol III stalk and clamp modules during the transition from apo to elongation state. Pol III …

**Summary**, from NCBI Gene [10623](https://www.ncbi.nlm.nih.gov/gene/10623):

> Enables single-stranded DNA binding activity. Involved in positive regulation of innate immune response; positive regulation of interferon-beta production; and transcription by RNA polymerase III. Located in nucleoplasm. Part of RNA polymerase III complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30076](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30076) · Entrez [10623](https://www.ncbi.nlm.nih.gov/gene/10623) · UniProt [Q9BUI4](https://www.uniprot.org/uniprotkb/Q9BUI4) · Ensembl [ENSG00000186141](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186141)

## Data

Gene col 11782: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11782); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11782, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11782]; `tensor/DDL_lfc|DDL_z.npy` [11782]; `embed/gene_vectors.npy` [11782]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11782 or target_col == 11782). Every well: [[POLR3C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR3C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
