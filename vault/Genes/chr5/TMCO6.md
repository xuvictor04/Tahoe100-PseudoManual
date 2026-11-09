---
symbol: "TMCO6"
type: "gene"
col: 3432
ensembl_id: "ENSG00000113119"
name: "transmembrane and coiled-coil domains 6"
location: "5q31.3"
module: 33
arm: "+"
pooled_cpm: 3.07
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# TMCO6

*transmembrane and coiled-coil domains 6* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.85× (z +6.0, q 8e-07, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.80× (z +5.9, q 8e-07, up in 16 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.393× (z -13.3, q 7e-38, down in 28 of 37 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM177]] (+0.67, fdr 5e-05), [[RCL1]] (+0.66, fdr 1e-05), [[ASB13]] (+0.63, fdr 1e-05); moves opposite to [[THAP2]] (-0.57, fdr 1e-04), [[COPZ1]] (-0.57, fdr 3e-05), [[ACBD5]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MCOLN2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3432.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +6.0 | 8e-07 | 0/1 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +5.9 | 8e-07 | 16/46 (A-427, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.66×** | +5.1 | 6e-05 | 7/42 (A-427, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.37×** | +4.5 | 9e-04 | 2/45 (SW480, HEC-1-A) | top dose only | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.003 | 9/44 (A498, SW 900, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.005 | 11/43 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.024 | 3/36 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +3.4 | 0.043 | 5/45 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.050 | 1/44 (Hs 766T) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.052 | 3/35 (PANC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.41×** | +3.2 | 0.061 | 1/29 (A498) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3432.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.393×** | -13.3 | 7e-38 | 28/37 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.511×** | -9.6 | 3e-19 | 24/35 (MIA PaCa-2, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.417×** | -8.8 | 2e-16 | 30/47 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.441×** | -8.3 | 2e-14 | 20/32 (SHP-77, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.435×** | -8.1 | 7e-14 | 27/42 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.566×** | -5.7 | 9e-07 | 20/29 (Panc 03.27, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.589×** | -5.4 | 7e-06 | 19/42 (BT-474, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.601×** | -5.1 | 2e-05 | 17/42 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.681×** | -3.9 | 0.007 | 16/39 (SK-MEL-2, RKO, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.692×** | -3.7 | 0.012 | 11/43 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.685×** | -3.7 | 0.012 | 11/29 (Panc 03.27, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -3.3 | 0.041 | 10/38 (A549, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3432. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 3.53 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 2.32 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0814× (z -9.6) |
| [[C-33 A (line)]] | alt | 6.47 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 2.36 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0578× (z -11.6) |
| [[LoVo (line)]] | wt | 5.09 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 6.74 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0744× (z -15.8) |
| [[NCI-H2030 (line)]] | alt | 4.48 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.103× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 5.18 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0684× (z -9.8) |
| [[PANC-1 (line)]] | alt | 3.72 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -12.6) |
| [[A-172 (line)]] | wt | 0.871 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.986 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3432), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM177]] | +0.67 | +0.39 / +0.72 | both halves | 5e-05 |  |
| [[RCL1]] | +0.66 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[ASB13]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[NLE1]] | +0.62 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[LRFN3]] | +0.62 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[TRABD]] | +0.62 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[PODXL2]] | +0.62 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[RGS19]] | +0.61 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[CLYBL]] | +0.61 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[SLC46A1]] | +0.61 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ADAMTSL5]] | +0.60 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[METAP1]] | +0.60 | +0.50 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP2]] | -0.57 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[COPZ1]] | -0.57 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[ACBD5]] | -0.56 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[C12orf57]] | -0.56 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[THAP9]] | -0.56 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[LINC01004]] | -0.55 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[LINC01135]] | -0.55 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[KRBOX5]] | -0.55 | -0.46 / -0.29 | both halves | 3e-04 |  |
| [[SGO1-AS1]] | -0.55 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[USP11]] | -0.54 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[ATF5]] | -0.53 | -0.47 / -0.25 | both halves | 4e-04 |  |
| [[LINC02307]] | -0.53 | -0.46 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCOLN2]] | B | MCOLN2 activity raises TMCO6's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.12× lower at baseline in the lines without MCOLN2 | 0.067 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[GNAZ]] | B | GNAZ activity raises TMCO6's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.21× lower at baseline in the lines without GNAZ | 0.072 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[ABCA3]] | B | ABCA3 activity raises TMCO6's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.30× lower at baseline in the lines without ABCA3 | 0.081 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.655). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.2, -41.6); signed map (-8.1, -52.7). **Vector** length 49.1, 6.18% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.52 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.4 | +2.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.3 | +5.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.1 | +5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.0 | +4.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.0 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | -1.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.2 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.1 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.1 | +2.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.4 | -8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.4 | -13.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.7 | -8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -0.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.1 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.1 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane and coiled-coil domains 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:140,639,435-140,645,408 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39769, PRO1580 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

UniProt [Q96DC7](https://www.uniprot.org/uniprotkb/Q96DC7) carries no function annotation.

**Summary**, from NCBI Gene [55374](https://www.ncbi.nlm.nih.gov/gene/55374):

> Predicted to enable nuclear import signal receptor activity. Predicted to be involved in protein import into nucleus. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28814](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28814) · Entrez [55374](https://www.ncbi.nlm.nih.gov/gene/55374) · UniProt [Q96DC7](https://www.uniprot.org/uniprotkb/Q96DC7) · Ensembl [ENSG00000113119](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113119)

## Data

Gene col 3432: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3432); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3432, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3432]; `tensor/DDL_lfc|DDL_z.npy` [3432]; `embed/gene_vectors.npy` [3432]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3432 or target_col == 3432). Every well: [[TMCO6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMCO6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
