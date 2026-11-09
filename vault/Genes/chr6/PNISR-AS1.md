---
symbol: "PNISR-AS1"
type: "gene"
col: 13652
ensembl_id: "ENSG00000228506"
name: "PNISR antisense RNA 1"
location: "6q16.2"
module: 46
arm: "+"
pooled_cpm: 5.59
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# PNISR-AS1

*PNISR antisense RNA 1* — 6q16.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.23× (z +17.7, q 0e+00, up in 42 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.398× (z -9.8, q 6e-20, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFF-DT]] (+0.79, fdr 1e-05), [[PBLD]] (+0.78, fdr 1e-04), [[AHI1-DT]] (+0.77, fdr 2e-05); moves opposite to [[STUB1]] (-0.69, fdr 4e-04), [[WRAP73]] (-0.68, fdr 1e-04), [[TECPR1]] (-0.68, fdr 1e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13652.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.23×** | +17.7 | 0e+00 | 42/43 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.80×** | +8.9 | 2e-16 | 28/48 (PANC-1, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +8.1 | 9e-14 | 29/42 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +7.2 | 8e-11 | 25/41 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.56×** | +6.8 | 1e-09 | 25/47 (A-427, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +4.6 | 3e-04 | 13/46 (A-172, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +4.4 | 7e-04 | 17/41 (NCI-H2030, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.49×** | +4.3 | 0.001 | 15/45 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +4.2 | 0.002 | 10/46 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.005 | 12/46 (KATO III, LS 180, …) | rises with dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.44×** | +3.9 | 0.005 | 6/47 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.048 | 6/43 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.051 | 5/46 (HT-29, RKO, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.34×** | +3.2 | 0.058 | 4/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.063 | 12/47 (NCI-H23, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13652.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.398×** | -9.8 | 6e-20 | 35/47 (NCI-H1792, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.459×** | -8.3 | 4e-14 | 33/47 (HEC-1-A, C32, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.493×** | -7.5 | 1e-11 | 33/47 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.499×** | -7.1 | 2e-10 | 23/37 (HCT15, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.691×** | -3.9 | 0.009 | 13/46 (LS 180, COLO 205, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **0.692×** | -3.9 | 0.009 | 11/26 (NCI-H1573, SW480, …) | inconsistent across doses | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.703×** | -3.7 | 0.013 | 11/47 (NCI-H661, BT-474, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.779×** | -3.7 | 0.013 | 14/48 (HT-29, C32, …) | rises with dose |  |
| [[Auranofin (drug)]] 0.5 µM |  | **0.724×** | -3.4 | 0.040 | 13/45 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.801×** | -3.3 | 0.052 | 15/47 (HCT15, SNU-1, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.735×** | -3.3 | 0.058 | 19/43 (NCI-H23, C32, …) | rises with dose | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **0.664×** | -3.1 | 0.092 | 10/43 (HCT15, RPMI-7951, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.752× | -3.0 | 0.11 | 10/47 (SW480, hTERT-HPNE, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13652. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 1.75 | 0 | 1 | — | [[5-Fluorouracil (drug)]] 0.5 µM 0.0489× (z -9.6) |
| [[KATO III (line)]] | alt | 6.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +9.0) | — |
| [[LoVo (line)]] | wt | 3.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.64× (z +11.0) | — |
| [[NCI-H1792 (line)]] | alt | 6.81 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 3.89 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 9.58 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0672× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 4.12 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0860× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 3.79 | 0 | 1 | — | [[Ataluren (drug)]] 0.5 µM 0.0658× (z -8.6) |
| [[PANC-1 (line)]] | alt | 8.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +10.7) | — |
| [[A-172 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13652), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 19 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFF-DT]] | +0.79 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[PBLD]] | +0.78 | +0.62 / +0.34 | both halves | 1e-04 |  |
| [[AHI1-DT]] | +0.77 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[TSTD3]] | +0.77 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[LINC00938]] | +0.75 | +0.66 / +0.43 | both halves | 4e-05 |  |
| [[SENP8]] | +0.74 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[VPS52]] | +0.72 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[RBM48]] | +0.71 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[C12orf60]] | +0.71 | +0.73 / +0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[THBS4]] | +0.71 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[PKN2-AS1]] | +0.71 | +0.62 / +0.25 | both halves | 4e-04 | same gene group |
| [[UBE3B]] | +0.71 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[CCDC90B-AS1]] | +0.71 | +0.62 / +0.22 | both halves | 6e-04 | same gene group |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STUB1]] | -0.69 | -0.41 / -0.24 | both halves | 4e-04 |  |
| [[WRAP73]] | -0.68 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[TECPR1]] | -0.68 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[TNK2]] | -0.67 | -0.62 / -0.38 | both halves | 7e-05 |  |
| [[PUSL1]] | -0.66 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[GPRIN1]] | -0.65 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[FCHO1]] | -0.65 | -0.46 / -0.29 | both halves | 3e-04 |  |
| [[CCDC112]] | -0.65 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[CAMK2G]] | -0.64 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[ANKRD27]] | -0.64 | -0.57 / -0.08 | ⚠ one half (not replicated) | 0.003 |  |
| [[PBX4]] | -0.64 | -0.57 / -0.24 | both halves | 5e-04 |  |
| [[ANTKMT]] | -0.64 | -0.35 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PNISR-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[OTUD7A]] | B | OTUD7A activity raises PNISR-AS1's level | lines that do not express OTUD7A (6) vs lines expressing it (44) | 1.41× lower at baseline in the lines without OTUD7A | 0.0998 | ⚠ within organs, on part of the lines; also absent: ENSG00000256673, WWOX, RUNDC3A-AS1; maybe low, not absent |
| [[CHTF8]] | C | CHTF8's natural level strengthens PNISR-AS1's drug response | CHTF8's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.05; direction not clear | 0.068 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[CATSPER2P1]] | C | CATSPER2P1 activity raises PNISR-AS1's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 1.63× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.776). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (1.1, 17.7); signed map (25.2, -14.0). **Vector** length 79.7, 14.2% of its response variance represented; |z| ≥ 3 in 1,083 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.4 | +17.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +8.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +5.3 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +8.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +3.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.5 | +2.5 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.3 | -9.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.0 | -7.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.8 | -8.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.3 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | PNISR antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6q16.2 — chr6:99,424,911-99,432,326 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40958](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40958) · Entrez [101927365](https://www.ncbi.nlm.nih.gov/gene/101927365) · Ensembl [ENSG00000228506](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228506)

## Data

Gene col 13652: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13652); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13652, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13652]; `tensor/DDL_lfc|DDL_z.npy` [13652]; `embed/gene_vectors.npy` [13652]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13652 or target_col == 13652). Every well: [[PNISR-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNISR-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
