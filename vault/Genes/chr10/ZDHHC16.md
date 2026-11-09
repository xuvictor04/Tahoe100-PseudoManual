---
symbol: "ZDHHC16"
type: "gene"
col: 10088
ensembl_id: "ENSG00000171307"
name: "zDHHC palmitoyltransferase 16"
location: "10q24.1"
module: 2
arm: "+"
pooled_cpm: 9.48
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ZDHHC16

*zDHHC palmitoyltransferase 16* — 10q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.62× (z +8.4, q 2e-14, up in 24 of 41 measured lines) ⚠ transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.52× (z +7.3, q 5e-11, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.445× (z -19.9, q 0e+00, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAGA]] (+0.68, fdr 1e-05), [[CRAT]] (+0.65, fdr 7e-06), [[TMED2]] (+0.65, fdr 1e-05); moves opposite to [[PRPF38B]] (-0.66, fdr 7e-06), [[HELQ]] (-0.60, fdr 1e-05), [[HMGXB4]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZSWIM5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10088.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.62×** | +8.4 | 2e-14 | 24/41 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +8.1 | 2e-13 | 10/20 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.34×** | +7.3 | 5e-11 | 16/48 (NCI-H1573, LoVo, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +7.3 | 5e-11 | 24/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +6.7 | 2e-09 | 21/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +6.4 | 1e-08 | 22/47 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.3 | 2e-08 | 14/32 (A498, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.3 | 8e-06 | 14/48 (A549, H4, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +5.3 | 9e-06 | 9/27 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.5 µM |  | **1.31×** | +4.7 | 1e-04 | 11/47 (PANC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trifluridine (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.034 | 6/47 (Hs 766T, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Larotrectinib (drug)]] 5 µM |  | 1.14× | +3.3 | 0.042 | 8/48 (PANC-1, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Levobupivacaine (hydrochloride) (drug)]] 0.05 µM |  | 1.21× | +3.0 | 0.10 | 3/46 (KATO III, A498, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10088.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.445×** | -19.9 | 0e+00 | 40/46 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.596×** | -8.7 | 1e-15 | 28/46 (SK-MEL-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.640×** | -7.8 | 2e-12 | 25/43 (HS-578T, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.491×** | -6.5 | 1e-08 | 22/43 (HOP62, A-427, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.569×** | -5.1 | 3e-05 | 20/47 (A-427, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.758×** | -4.8 | 1e-04 | 13/46 (H4, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -4.8 | 2e-04 | 1/48 (AN3 CA) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **0.765×** | -4.6 | 2e-04 | 20/45 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.782×** | -4.3 | 0.001 | 15/46 (KATO III, NCI-H1573, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.820×** | -3.4 | 0.034 | 14/47 (NCI-H460, NCI-H661, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.823×** | -3.2 | 0.070 | 9/46 (A-172, HEC-1-A, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.832×** | -3.2 | 0.070 | 10/45 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.883× | -3.0 | 0.10 | 7/48 (NCI-H2030, NCI-H661, …) | top dose only | position effect removed |
| [[Levobupivacaine (hydrochloride) (drug)]] 5 µM |  | 0.834× | -3.0 | 0.10 | 7/46 (AN3 CA, NCI-H2030, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10088. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.38 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 9.40 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -14.0) |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0642× (z -13.2) |
| [[A-172 (line)]] | wt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -10.3) |
| [[A498 (line)]] | wt | 11.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -11.5) |
| [[BT-474 (line)]] | alt | 6.34 | 0 | 1 | — | [[Neratinib (drug)]] 0.05 µM 0.0835× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 9.87 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -9.8) |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0895× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 9.80 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -11.7) |
| [[HepG2_C3A (line)]] | wt | 8.65 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0665× (z -9.8) |
| [[HOP62 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -9.8) |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 8.49 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0618× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 6.07 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0923× (z -15.1) |
| [[NCI-H2347 (line)]] | alt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -9.9) |
| [[SW 900 (line)]] | alt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -9.0) |
| [[A-427 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10088), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAGA]] | +0.68 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[CRAT]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[TMED2]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[HECTD3]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[VAMP3]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[SDHA]] | +0.62 | +0.67 / +0.46 | both halves | 2e-05 |  |
| [[PABIR2]] | +0.62 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[LMF2]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[TMEM30A]] | +0.61 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[EDEM2]] | +0.61 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[AP2M1]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ABHD17A]] | +0.61 | +0.64 / +0.43 | both halves | 3e-05 | STRING 522 |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF38B]] | -0.66 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[HELQ]] | -0.60 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[HMGXB4]] | -0.60 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[BPTF]] | -0.59 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[TGIF2-RAB5IF]] | -0.58 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[ATF1]] | -0.57 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[PPIG]] | -0.56 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[ZNF75A]] | -0.56 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[NBPF10]] | -0.56 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[YAF2]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[ARMC5]] | -0.55 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[TGIF2]] | -0.55 | -0.54 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZSWIM5]] | B | ZSWIM5 activity lowers ZDHHC16's level | lines that do not express ZSWIM5 (5) vs lines expressing it (45) | 1.26× higher at baseline in the lines without ZSWIM5 | 0.089 | ⚠ within organs, on part of the lines; also absent: DLGAP1, ABHD12B, TTN; maybe low, not absent; its own permutation p |
| [[HDAC6]] | B | HDAC6 activity lowers ZDHHC16's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.495). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.0, -20.8); signed map (-47.9, -11.7). **Vector** length 64.3, 9.32% of its response variance represented; |z| ≥ 3 in 921 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.2 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +8.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.7 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +6.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.4 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | +0.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.2 | +2.9 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.2 | +1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.1 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.7 | -19.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.4 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -3.2 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.1 — chr10:97,446,170-97,457,370 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APH2 |
| Gene groups (HGNC) | Zinc fingers DHHC-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969W1](https://www.uniprot.org/uniprotkb/Q969W1) (Palmitoyltransferase ZDHHC16):

> Palmitoyl acyltransferase that mediates palmitoylation of proteins such as PLN and ZDHHC6. Required during embryonic heart development and cardiac function, possibly by mediating palmitoylation of PLN, thereby affecting PLN phosphorylation and homooligomerization (By similarity). Also required for eye development (By similarity). Palmitoylates ZDHHC6, affecting the quaternary assembly of ZDHHC6, its localization, stability and function. May play a role in DNA damage response (By similarity). …

**Summary**, from NCBI Gene [84287](https://www.ncbi.nlm.nih.gov/gene/84287):

> Enables palmitoyltransferase activity. Predicted to be involved in several processes, including eye development; protein palmitoylation; and telencephalon development. Predicted to be located in endoplasmic reticulum membrane. Predicted to be active in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20714](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20714) · Entrez [84287](https://www.ncbi.nlm.nih.gov/gene/84287) · UniProt [Q969W1](https://www.uniprot.org/uniprotkb/Q969W1) · Ensembl [ENSG00000171307](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171307)

## Data

Gene col 10088: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10088); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10088, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10088]; `tensor/DDL_lfc|DDL_z.npy` [10088]; `embed/gene_vectors.npy` [10088]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10088 or target_col == 10088). Every well: [[ZDHHC16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
