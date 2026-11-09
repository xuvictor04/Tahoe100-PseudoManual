---
symbol: "ATG4A"
type: "gene"
col: 2177
ensembl_id: "ENSG00000101844"
name: "autophagy related 4A cysteine peptidase"
location: "Xq22.3"
module: 72
arm: "+"
pooled_cpm: 9.9
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# ATG4A

*autophagy related 4A cysteine peptidase* — Xq22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.68× (z +17.2, q 0e+00, up in 44 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SHP-77 0.103×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (Panc 03.27 0.144×); [[Proglumide (drug)]] 0.05 µM in 1 line (COLO 205 0.0602×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC167]] (+0.59, fdr 2e-05), [[P4HA2]] (+0.58, fdr 4e-05), [[MACO1]] (+0.58, fdr 2e-05); moves opposite to [[ADNP]] (-0.51, fdr 6e-05), [[STAG1]] (-0.49, fdr 4e-05), [[TFAM]] (-0.49, fdr 2e-04).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2177.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.68×** | +17.2 | 0e+00 | 44/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.56×** | +16.7 | 0e+00 | 44/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.38×** | +16.2 | 0e+00 | 37/45 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.28×** | +15.7 | 0e+00 | 47/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +15.5 | 0e+00 | 36/43 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.58×** | +12.5 | 8e-34 | 41/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.58×** | +12.5 | 8e-34 | 39/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.52×** | +12.2 | 2e-32 | 41/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.62×** | +12.0 | 2e-31 | 43/44 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.60×** | +8.8 | 5e-17 | 35/46 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +8.7 | 1e-16 | 28/43 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.93×** | +8.7 | 2e-16 | 31/42 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +8.4 | 2e-15 | 31/44 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.84×** | +7.7 | 6e-13 | 29/46 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +7.2 | 2e-11 | 30/47 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2177.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SHP-77 0.103×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (Panc 03.27 0.144×); [[Proglumide (drug)]] 0.05 µM in 1 line (COLO 205 0.0602×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.760× | -3.7 | 0.13 | 12/47 (A-172, SW48, …) | rises with dose |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.797× | -3.1 | 0.48 | 4/47 (NCI-H2347, SW480, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 5 µM |  | 0.799× | -3.0 | 0.48 | 2/47 (HEC-1-A, A549) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2177. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.5 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +12.3) | — |
| [[SW480 (line)]] | alt | 13.2 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +13.1) | — |
| [[HOP62 (line)]] | alt | 5.20 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.50× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 11.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +10.0) | — |
| [[A549 (line)]] | wt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 7.30 | 0 | 1 | — | [[Proglumide (drug)]] 0.05 µM 0.0602× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 7.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.144× (z -9.4) |
| [[RKO (line)]] | wt | 8.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.33× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 9.42 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.121× (z -8.5) |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.103× (z -10.9) |
| [[SNU-423 (line)]] | alt | 9.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +9.5) | — |
| [[A-172 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2177), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC167]] | +0.59 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[P4HA2]] | +0.58 | +0.47 / +0.41 | both halves | 4e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[MACO1]] | +0.58 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[PSMD13]] | +0.58 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[MAPRE3]] | +0.57 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[FAM219A]] | +0.55 | +0.52 / +0.37 | both halves | 8e-05 |  |
| [[AAK1]] | +0.54 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[GCKR]] | +0.54 | +0.48 / +0.36 | both halves | 9e-05 |  |
| [[ACTR1A]] | +0.53 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[RDH11]] | +0.53 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[LNPK]] | +0.53 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[TESK1]] | +0.53 | +0.40 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADNP]] | -0.51 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[STAG1]] | -0.49 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[TFAM]] | -0.49 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[SERBP1]] | -0.49 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[POLR1G]] | -0.48 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[NOP56]] | -0.47 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[GNL3L]] | -0.46 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[SLC25A13]] | -0.45 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[ZNF121]] | -0.45 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[PCF11]] | -0.45 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[PABPC4]] | -0.45 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[TTC27]] | -0.44 | -0.22 / -0.49 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ATG4A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.9, -15.8); signed map (-40.9, 30.4). **Vector** length 59.1, 9.83% of its response variance represented; |z| ≥ 3 in 1,229 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +12.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.3 | +12.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.1 | +12.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.2 | +6.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.8 | +8.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +6.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +6.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +4.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.5 | +3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.0 | +3.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +0.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.8 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.1 | -0.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | autophagy related 4A cysteine peptidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.3 — chrX:108,091,668-108,154,671 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously AUTL2, APG4A |
| Gene groups (HGNC) | Autophagy related; Autophagy related 4 family cysteine peptidases |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 2 pathways, smallest: Macroautophagy; Autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WYN0](https://www.uniprot.org/uniprotkb/Q8WYN0) (Cysteine protease ATG4A):

> Cysteine protease that plays a key role in autophagy by mediating both proteolytic activation and delipidation of ATG8 family proteins. The protease activity is required for proteolytic activation of ATG8 family proteins: cleaves the C-terminal amino acid of ATG8 proteins to reveal a C-terminal glycine. Exposure of the glycine at the C-terminus is essential for ATG8 proteins conjugation to phosphatidylethanolamine (PE) and insertion to membranes, which is necessary for autophagy. Preferred …

**Summary**, from NCBI Gene [115201](https://www.ncbi.nlm.nih.gov/gene/115201):

> Autophagy is the process by which endogenous proteins and damaged organelles are destroyed intracellularly. Autophagy is postulated to be essential for cell homeostasis and cell remodeling during differentiation, metamorphosis, non-apoptotic cell death, and aging. Reduced levels of autophagy have been described in some malignant tumors, and a role for autophagy in controlling the unregulated cell growth linked to cancer has been proposed. This gene encodes a member of the autophagin protein …

**Accessions** — [HGNC:16489](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16489) · Entrez [115201](https://www.ncbi.nlm.nih.gov/gene/115201) · UniProt [Q8WYN0](https://www.uniprot.org/uniprotkb/Q8WYN0) · Ensembl [ENSG00000101844](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101844)

## Data

Gene col 2177: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2177); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2177, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2177]; `tensor/DDL_lfc|DDL_z.npy` [2177]; `embed/gene_vectors.npy` [2177]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2177 or target_col == 2177). Every well: [[ATG4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATG4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
