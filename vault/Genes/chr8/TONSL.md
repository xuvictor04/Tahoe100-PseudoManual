---
symbol: "TONSL"
type: "gene"
col: 8397
ensembl_id: "ENSG00000160949"
name: "tonsoku like, DNA repair protein"
location: "8q24.3"
module: 6
arm: "+"
pooled_cpm: 6.19
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# TONSL

*tonsoku like, DNA repair protein* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.09× (z +8.7, q 2e-15, up in 30 of 47 measured lines) ⚠ cell-cycle shift, explains ~76% of this change. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.05 µM: 1.37× (z +3.4, q 0.026, up in 8 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.750× (z -4.8, q 8e-04, down in 21 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RECQL4]] (+0.89, fdr 7e-06), [[XRCC3]] (+0.87, fdr 7e-06), [[CDC45]] (+0.86, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 17 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8397.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **2.09×** | +8.7 | 2e-15 | 30/47 (A549, RKO, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **1.91×** | +7.6 | 8e-12 | 13/26 (A498, HOP62, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.84×** | +6.6 | 7e-09 | 6/15 (NCI-H2347, HEC-1-A, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | **1.74×** | +6.2 | 6e-08 | 4/10 (BT-474, NCI-H2347, …) | all doses, flat | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.69×** | +6.2 | 7e-08 | 21/45 (LOX-IMVI, H4, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.62×** | +5.6 | 2e-06 | 20/45 (A549, COLO 205, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +5.1 | 3e-05 | 16/46 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.52×** | +4.9 | 8e-05 | 13/46 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~68% of this change | **1.52×** | +4.7 | 1e-04 | 13/33 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +4.6 | 3e-04 | 8/32 (NCI-H2030, AsPC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.41×** | +4.0 | 0.003 | 11/44 (HS-578T, PANC-1, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.27×** | +4.0 | 0.004 | 6/44 (LS 180, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.27×** | +3.9 | 0.004 | 11/41 (A549, NCI-H2030, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.40×** | +3.8 | 0.006 | 9/38 (NCI-H2347, PANC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.37×** | +3.4 | 0.026 | 8/39 (A-427, J82, …) | all doses, stronger at high dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.049 | 8/42 (SW480, J82, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.051 | 4/46 (A-427, NCI-H2030, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8397.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.750×** | -4.8 | 8e-04 | 21/44 (LS 180, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.769×** | -4.4 | 0.003 | 15/46 (A-172, LS 180, …) | rises with dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -4.2 | 0.005 | 12/48 (MIA PaCa-2, H4, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.720×** | -3.9 | 0.014 | 19/43 (HOP62, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.730×** | -3.7 | 0.022 | 15/38 (RKO, Hs 766T, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.734×** | -3.7 | 0.022 | 16/43 (A-172, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.806×** | -3.6 | 0.022 | 18/40 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.742×** | -3.4 | 0.052 | 11/44 (LS 180, A-172, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.758×** | -3.3 | 0.052 | 7/45 (AN3 CA, RKO, …) | rises with dose | position effect removed |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.678×** | -3.3 | 0.052 | 6/47 (SW480, SW 1271, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.758×** | -3.3 | 0.052 | 7/46 (A-427, AN3 CA, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.828×** | -3.2 | 0.070 | 7/46 (H4, RKO, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.87 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8397. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.13 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.174× (z -9.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.05 µM 0.0864× (z -9.0) |
| [[LS 180 (line)]] | wt | 7.60 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.224× (z -9.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A498 (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.191× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 5.02 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.113× (z -8.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[Hs 766T (line)]] | wt | 4.68 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0689× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 6.42 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0921× (z -8.8) |
| [[A-427 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8397), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RECQL4]] | +0.89 | +0.85 / +0.90 | both halves | 7e-06 | STRING 402 |
| [[XRCC3]] | +0.87 | +0.85 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[CDC45]] | +0.86 | +0.85 / +0.85 | both halves | 7e-06 | STRING 424 |
| [[POLE]] | +0.86 | +0.84 / +0.85 | both halves | 7e-06 | STRING 464 |
| [[MCM5]] | +0.86 | +0.88 / +0.84 | both halves | 7e-06 | STRING 655 |
| [[FANCA]] | +0.85 | +0.84 / +0.84 | both halves | 7e-06 |  |
| [[CHAF1A]] | +0.85 | +0.82 / +0.86 | both halves | 7e-06 |  |
| [[CDC25A]] | +0.83 | +0.79 / +0.84 | both halves | 7e-06 |  |
| [[MYBL2]] | +0.83 | +0.82 / +0.81 | both halves | 7e-06 |  |
| [[PKMYT1]] | +0.82 | +0.79 / +0.84 | both halves | 7e-06 |  |
| [[E2F1]] | +0.82 | +0.80 / +0.82 | both halves | 7e-06 |  |
| [[RAD51]] | +0.82 | +0.78 / +0.83 | both halves | 7e-06 | STRING 518 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises TONSL's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.66× lower at baseline in the lines without E2F2 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[ZNF367]] | C | ZNF367 activity raises TONSL's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.07× lower at baseline in the lines without ZNF367 | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.848). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.1, -43.6); signed map (-36.8, -45.7). **Vector** length 77.4, 14.1% of its response variance represented; |z| ≥ 3 in 942 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.64 to 65); *DNA strand elongation* (reactome, mean cos +0.70 to 28); *DNA Replication* (reactome, mean cos +0.69 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | +4.0 | +6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +3.4 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | +3.2 | +7.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +5.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +3.1 | +8.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.4 | +0.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.4 | +2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.3 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.5 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -3.5 | -3.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -3.4 | -3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.0 | -4.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -3.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | tonsoku like, DNA repair protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,428,775-144,444,440 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IKBR; previously NFKBIL2 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96HA7](https://www.uniprot.org/uniprotkb/Q96HA7) (Tonsoku-like protein):

> Component of the MMS22L-TONSL complex, a complex that promotes homologous recombination-mediated repair of double-strand breaks (DSBs) at stalled or collapsed replication forks. The MMS22L-TONSL complex is required to maintain genome integrity during DNA replication. It mediates the assembly of RAD51 filaments on single-stranded DNA (ssDNA): the MMS22L-TONSL complex is recruited to DSBs following histone replacement by histone chaperones and eviction of the replication protein A complex …

**Summary**, from NCBI Gene [4796](https://www.ncbi.nlm.nih.gov/gene/4796):

> The protein encoded by this gene is thought to be a negative regulator of NF-kappa-B mediated transcription. The encoded protein may bind NF-kappa-B complexes and trap them in the cytoplasm, preventing them from entering the nucleus and interacting with the DNA. Phosphorylation of this protein targets it for degradation by the ubiquitination pathway, which frees the NF-kappa-B complexes to enter the nucleus. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7801) · Entrez [4796](https://www.ncbi.nlm.nih.gov/gene/4796) · UniProt [Q96HA7](https://www.uniprot.org/uniprotkb/Q96HA7) · Ensembl [ENSG00000160949](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160949)

## Data

Gene col 8397: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8397); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8397, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8397]; `tensor/DDL_lfc|DDL_z.npy` [8397]; `embed/gene_vectors.npy` [8397]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8397 or target_col == 8397). Every well: [[TONSL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TONSL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
