---
symbol: "MFSD13A"
type: "gene"
col: 6128
ensembl_id: "ENSG00000138111"
name: "solute carrier family 68 member 1"
location: "10q24.32"
module: 17
arm: "+"
pooled_cpm: 4.15
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# MFSD13A

*solute carrier family 68 member 1* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.06× (z +13.2, q 3e-37, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.714× (z -4.1, q 0.028, down in 11 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SNU-423 0.0615×).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRPF39]] (+0.70, fdr 2e-05), [[MAP4K2]] (+0.66, fdr 3e-05), [[HACE1]] (+0.63, fdr 3e-04); moves opposite to [[HCG18]] (-0.60, fdr 3e-05), [[LINC00571]] (-0.57, fdr 4e-04), [[ATXN1L]] (-0.56, fdr 0.001, ⚠ one half only (not replicated)), [[SON]] (-0.55, fdr 1e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LRRC8B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6128.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.06×** | +13.2 | 3e-37 | 37/46 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.80×** | +12.2 | 6e-32 | 29/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.71×** | +11.8 | 7e-30 | 33/45 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.58×** | +10.8 | 4e-25 | 3/6 (A498, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +9.1 | 8e-18 | 19/38 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +8.3 | 1e-14 | 20/44 (A498, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.95×** | +7.9 | 2e-13 | 10/20 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +7.3 | 2e-11 | 15/22 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +6.8 | 6e-10 | 18/46 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +6.6 | 3e-09 | 14/41 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.69×** | +5.7 | 5e-07 | 2/8 (CFPAC-1, SW480) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +4.9 | 4e-05 | 10/46 (RKO, LoVo, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.8 | 7e-05 | 9/27 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.002 | 3/45 (NCI-H1573, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.005 | 6/35 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +3.3 | 0.030 | 4/40 (SW480, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.34×** | +3.2 | 0.047 | 1/29 (A-427) | all doses, stronger at high dose |  |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.047 | 4/36 (SW1417, LoVo, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.053 | 2/46 (HepG2/C3A, NCI-H2030) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6128.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SNU-423 0.0615×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.714×** | -4.1 | 0.028 | 11/45 (SNU-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.725×** | -3.9 | 0.031 | 10/43 (SNU-1, A-427, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.822× | -3.4 | 0.15 | 12/46 (NCI-H460, RKO, …) | rises with dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.752× | -3.2 | 0.21 | 8/39 (LS 180, SW1417, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.764× | -3.1 | 0.21 | 5/46 (hTERT-HPNE, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6128. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 2.97 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0615× (z -8.5) |
| [[A-172 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6128), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 9 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF39]] | +0.70 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[MAP4K2]] | +0.66 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[HACE1]] | +0.63 | +0.28 / +0.59 | both halves | 3e-04 |  |
| [[TMEM14A]] | +0.62 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[KCTD6]] | +0.61 | +0.31 / +0.61 | both halves | 2e-04 |  |
| [[RSAD1]] | +0.58 | +0.25 / +0.60 | both halves | 4e-04 |  |
| [[CYB5A]] | +0.58 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[ARRB2]] | +0.58 | +0.21 / +0.63 | both halves | 7e-04 |  |
| [[C6orf136]] | +0.58 | +0.35 / +0.61 | both halves | 1e-04 |  |
| [[SLC25A12]] | +0.58 | +0.38 / +0.72 | both halves | 7e-05 |  |
| [[METTL17]] | +0.58 | +0.28 / +0.58 | both halves | 3e-04 |  |
| [[ANAPC4]] | +0.57 | +0.39 / +0.58 | both halves | 6e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCG18]] | -0.60 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[LINC00571]] | -0.57 | -0.26 / -0.55 | both halves | 4e-04 |  |
| [[ATXN1L]] | -0.56 | -0.18 / -0.62 | ⚠ one half (not replicated) | 0.001 |  |
| [[SON]] | -0.55 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[ASXL2]] | -0.52 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[SMCR8]] | -0.51 | -0.23 / -0.47 | both halves | 5e-04 |  |
| [[MMADHC-DT]] | -0.51 | -0.11 / -0.53 | ⚠ one half (not replicated) | 0.002 |  |
| [[OSTM1]] | -0.49 | -0.30 / -0.30 | both halves | 2e-04 |  |
| [[CDK12]] | -0.49 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[TUG1]] | -0.49 | -0.15 / -0.50 | ⚠ not reproduced | 0.001 |  |
| [[PDK1-AS1]] | -0.49 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[ATP6V1D]] | -0.49 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[PDCD6IP-DT]] | -0.48 | -0.27 / -0.44 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC8B]] | B | LRRC8B activity raises MFSD13A's level | lines that do not express LRRC8B (6) vs lines expressing it (44) | 1.68× lower at baseline in the lines without LRRC8B | 0.096 | ⚠ within organs, on part of the lines; also absent: GCLC, RHOF, RHPN1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.610). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (3.5, -6.9); signed map (-33.2, -6.5). **Vector** length 49.5, 6.13% of its response variance represented; |z| ≥ 3 in 905 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +2.4 | +10.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.3 | +4.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.3 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.7 | -2.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | +0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 68 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:102,461,395-102,477,045 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22529, bA18I14.8; previously C10orf77, TMEM180, MFSD13A |
| Gene groups (HGNC) | Solute carrier family 68 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14CX5](https://www.uniprot.org/uniprotkb/Q14CX5) (Solute carrier family 68 member 1):

> May act as a cation symporter.

**Summary**, from NCBI Gene [79847](https://www.ncbi.nlm.nih.gov/gene/79847):

> Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26196](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26196) · Entrez [79847](https://www.ncbi.nlm.nih.gov/gene/79847) · UniProt [Q14CX5](https://www.uniprot.org/uniprotkb/Q14CX5) · Ensembl [ENSG00000138111](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138111)

## Data

Gene col 6128: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6128); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6128, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6128]; `tensor/DDL_lfc|DDL_z.npy` [6128]; `embed/gene_vectors.npy` [6128]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6128 or target_col == 6128). Every well: [[MFSD13A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFSD13A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
