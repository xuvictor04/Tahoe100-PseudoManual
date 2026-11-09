---
symbol: "OGFOD3"
type: "gene"
col: 11184
ensembl_id: "ENSG00000181396"
name: "2-oxoglutarate and iron dependent oxygenase domain containing 3"
location: "17q25.3"
module: 18
arm: "+"
pooled_cpm: 13.01
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# OGFOD3

*2-oxoglutarate and iron dependent oxygenase domain containing 3* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.05× (z +12.6, q 1e-33, up in 30 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.27× (z +6.1, q 2e-07, up in 20 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 3.31×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.387× (z -23.5, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX54]] (+0.67, fdr 7e-06), [[SARS2]] (+0.63, fdr 1e-05), [[CHID1]] (+0.63, fdr 9e-06); moves opposite to [[NOTCH2NLB]] (-0.58, fdr 1e-05), [[TRMT1L]] (-0.55, fdr 1e-05), [[GATAD1]] (-0.55, fdr 9e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11184.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 3.31×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +12.6 | 1e-33 | 30/37 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +11.6 | 2e-28 | 17/22 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +8.7 | 1e-15 | 21/33 (LS 180, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +6.1 | 2e-07 | 20/46 (CFPAC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.17 | 8/45 (NCI-H460, SW48, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11184.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.387×** | -23.5 | 0e+00 | 42/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.479×** | -12.8 | 3e-35 | 39/47 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.536×** | -10.5 | 3e-23 | 33/46 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.688×** | -6.3 | 5e-08 | 21/46 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.711×** | -5.7 | 1e-06 | 19/46 (RKO, SK-MEL-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.724×** | -5.6 | 2e-06 | 21/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.743×** | -5.1 | 2e-05 | 18/48 (SW1417, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.743×** | -5.1 | 2e-05 | 17/48 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.747×** | -5.1 | 2e-05 | 19/47 (Panc 03.27, SW1417, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.753×** | -4.9 | 5e-05 | 21/44 (A-172, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.771×** | -4.5 | 3e-04 | 12/47 (SW480, NCI-H1792, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.785×** | -4.2 | 0.001 | 16/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.790×** | -4.1 | 0.002 | 18/47 (J82, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.804×** | -3.8 | 0.006 | 7/47 (RPMI-7951, SNU-423, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.819×** | -3.4 | 0.022 | 7/47 (J82, Hs 766T, …) | two highest doses |  |
| [[Tadalafil (drug)]] 5 µM |  | **0.823×** | -3.2 | 0.039 | 11/47 (C-33 A, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.842× | -3.0 | 0.087 | 14/47 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11184. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 18.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -17.5) |
| [[HEC-1-A (line)]] | alt | 17.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.31× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 15.4 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 12.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.0) |
| [[A-427 (line)]] | wt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -12.1) |
| [[BT-474 (line)]] | alt | 19.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.132× (z -9.1) ⚠ toxic |
| [[HOP62 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -11.9) |
| [[HT-29 (line)]] | alt | 9.06 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -10.0) |
| [[J82 (line)]] | alt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -12.3) |
| [[KATO III (line)]] | alt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -12.9) |
| [[LoVo (line)]] | wt | 11.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -11.6) |
| [[LS 180 (line)]] | wt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 7.50 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 9.46 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.140× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~7% of this change |
| [[SNU-423 (line)]] | alt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -10.7) |
| [[SW1417 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -12.2) |
| [[SW48 (line)]] | wt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0682× (z -10.0) |
| [[SW480 (line)]] | alt | 20.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -16.8) |
| [[A-172 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11184), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX54]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[SARS2]] | +0.63 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[CHID1]] | +0.63 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[EIF3B]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[RPUSD4]] | +0.62 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[LAPTM4B]] | +0.61 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[PEMT]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[USP5]] | +0.57 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[ADPGK]] | +0.57 | +0.72 / +0.35 | both halves | 1e-04 |  |
| [[TRRAP]] | +0.57 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[SNRPD3]] | +0.56 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[SENP3]] | +0.56 | +0.47 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH2NLB]] | -0.58 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[TRMT1L]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[GATAD1]] | -0.55 | -0.66 / -0.37 | both halves | 9e-05 |  |
| [[BTG1]] | -0.54 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[LYSMD3]] | -0.54 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[APLF]] | -0.52 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[NBPF10]] | -0.52 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[SLC41A2]] | -0.52 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[COMMD3]] | -0.52 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[TIPRL]] | -0.52 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[H3-3B]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[MARCKS]] | -0.50 | -0.53 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises OGFOD3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.496). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.5, -32.4); signed map (-23.8, -47.1). **Vector** length 59.0, 8.15% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +0.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +2.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.7 | -10.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -12.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.4 | -23.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.9 | -2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -3.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | 2-oxoglutarate and iron dependent oxygenase domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,389,210-82,418,637 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22222; previously C17orf101 |
| Gene groups (HGNC) | Iron (II) and 2-oxoglutarate dependent oxygenases |
| Matched by | ensembl_id |

UniProt [Q6PK18](https://www.uniprot.org/uniprotkb/Q6PK18) carries no function annotation.

**Summary**, from NCBI Gene [79701](https://www.ncbi.nlm.nih.gov/gene/79701):

> Predicted to enable several functions, including L-ascorbic acid binding activity; dioxygenase activity; and iron ion binding activity. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26174](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26174) · Entrez [79701](https://www.ncbi.nlm.nih.gov/gene/79701) · UniProt [Q6PK18](https://www.uniprot.org/uniprotkb/Q6PK18) · Ensembl [ENSG00000181396](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181396)

## Data

Gene col 11184: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11184); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11184, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11184]; `tensor/DDL_lfc|DDL_z.npy` [11184]; `embed/gene_vectors.npy` [11184]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11184 or target_col == 11184). Every well: [[OGFOD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OGFOD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
