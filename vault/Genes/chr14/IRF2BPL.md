---
symbol: "IRF2BPL"
type: "gene"
col: 4093
ensembl_id: "ENSG00000119669"
name: "interferon regulatory factor 2 binding protein like"
location: "14q24.3"
module: 14
arm: "+"
pooled_cpm: 32.59
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# IRF2BPL

*interferon regulatory factor 2 binding protein like* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.83× (z +7.0, q 2e-09, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.460× (z -8.9, q 2e-16, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFKBIE]] (+0.60, fdr 2e-05), [[BCOR]] (+0.59, fdr 1e-05), [[PIM3]] (+0.57, fdr 7e-05); moves opposite to [[SPTLC1]] (-0.55, fdr 3e-05), [[NDUFA10]] (-0.52, fdr 5e-05), [[AP2B1]] (-0.52, fdr 6e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF625]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4093.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.83×** | +7.0 | 2e-09 | 29/47 (A549, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.62×** | +5.6 | 7e-06 | 33/45 (HS-578T, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.48×** | +4.4 | 0.002 | 25/47 (CFPAC-1, A549, …) | all doses, flat | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.1 | 0.007 | 22/45 (SW1417, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +3.9 | 0.012 | 24/47 (MIA PaCa-2, A549, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.40×** | +3.6 | 0.032 | 22/46 (C32, A549, …) | all doses, flat | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4093.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.460×** | -8.9 | 2e-16 | 41/47 (SW 900, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.546×** | -7.0 | 1e-09 | 31/47 (SW 900, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.548×** | -6.5 | 1e-08 | 33/47 (C32, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.557×** | -6.5 | 1e-08 | 23/36 (SHP-77, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.654×** | -4.9 | 1e-04 | 24/47 (NCI-H2030, SW 900, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.654×** | -4.9 | 1e-04 | 28/47 (A498, SW 900, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.658×** | -4.8 | 1e-04 | 27/47 (SW 900, C32, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.884× | -4.7 | 2e-04 | 7/47 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.752×** | -4.6 | 2e-04 | 24/47 (NCI-H2347, SHP-77, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.490×** | -4.3 | 1e-03 | 29/46 (MIA PaCa-2, H4, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.506×** | -4.1 | 0.002 | 22/42 (NCI-H1573, C32, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.699×** | -4.0 | 0.004 | 24/46 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Pentagastrin (drug)]] 5 µM |  | **0.816×** | -3.3 | 0.041 | 15/47 (SW 1088, MIA PaCa-2, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.585×** | -3.2 | 0.052 | 23/47 (A498, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.752×** | -3.1 | 0.062 | 19/46 (RKO, NCI-H23, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.741×** | -3.1 | 0.068 | 19/47 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4093. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 71.9 | 0 | 8 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.206× (z -10.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.219× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 45.1 | 0 | 5 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.465× (z -20.4) ⚠ position not correctable · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 87.3 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0952× (z -23.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.274× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 71.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 25.3 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.271× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.305× (z -8.5) |
| [[C32 (line)]] | wt | 71.0 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -11.7) |
| [[A549 (line)]] | wt | 36.7 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 6.49× (z +12.1) | — |
| [[CFPAC-1 (line)]] | alt | 16.0 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 7.26× (z +11.2) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H1573 (line)]] | alt | 43.2 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0273× (z -12.5) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 53.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -13.9) ⚠ cell-cycle shift, explains ~19% of this change |
| [[SHP-77 (line)]] | alt | 72.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -14.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 25.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -12.6) |
| [[A498 (line)]] | wt | 32.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -9.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 29.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.615× (z -8.9) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 52.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -13.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 31.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -10.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 44.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -11.6) ⚠ cell-cycle shift, explains ~24% of this change |
| [[A-427 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4093), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKBIE]] | +0.60 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[BCOR]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[PIM3]] | +0.57 | +0.37 / +0.65 | both halves | 7e-05 |  |
| [[IRF2BP2]] | +0.56 | +0.39 / +0.63 | both halves | 6e-05 | same gene group; STRING 790 |
| [[FOXA2]] | +0.56 | +0.38 / +0.60 | both halves | 7e-05 |  |
| [[NR1D1]] | +0.55 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[SEMA4C]] | +0.55 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[MAGEF1]] | +0.55 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[ST3GAL2]] | +0.55 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[ORAI1]] | +0.54 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[RHOV]] | +0.54 | +0.36 / +0.53 | both halves | 9e-05 |  |
| [[ZIC2]] | +0.53 | +0.44 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTLC1]] | -0.55 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[NDUFA10]] | -0.52 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[AP2B1]] | -0.52 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[LRPPRC]] | -0.52 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[VAMP3]] | -0.51 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[PPIP5K2]] | -0.49 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[OPA1]] | -0.49 | -0.36 / -0.59 | both halves | 1e-04 |  |
| [[VDAC2]] | -0.48 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[IL18BP]] | -0.47 | -0.32 / -0.51 | both halves | 1e-04 |  |
| [[CSDE1]] | -0.47 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[NUTF2]] | -0.47 | -0.28 / -0.58 | both halves | 3e-04 |  |
| [[LARP4B]] | -0.47 | -0.42 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF625]] | B | ZNF625 activity raises IRF2BPL's level | lines that do not express ZNF625 (19) vs lines expressing it (31) | 1.88× lower at baseline in the lines without ZNF625 | 0.021 | ⚠ within organs, on part of the lines; also absent: ZNF415, ZNF829, ZNF347 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.464). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.2, -3.9); signed map (-2.9, 12.6). **Vector** length 117, 32.0% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +5.8 | +4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.8 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +0.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +3.6 |
|  | [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +2.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +1.8 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.5 | -6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -9.3 | -3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.9 | -0.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.3 | -6.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -4.2 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -2.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | interferon regulatory factor 2 binding protein like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:77,024,543-77,028,708 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EAP1, KIAA1865; previously C14orf4 |
| Gene groups (HGNC) | RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1B7](https://www.uniprot.org/uniprotkb/Q9H1B7) (Probable E3 ubiquitin-protein ligase IRF2BPL):

> Probable E3 ubiquitin protein ligase involved in the proteasome-mediated ubiquitin-dependent degradation of target proteins. Through the degradation of CTNNB1, functions downstream of FOXF2 to negatively regulate the Wnt signaling pathway. Probably plays a role in the development of the central nervous system and in neuronal maintenance (Probable). Also acts as a transcriptional regulator of genes controlling female reproductive function. May play a role in gene transcription by transactivating …

**Summary**, from NCBI Gene [64207](https://www.ncbi.nlm.nih.gov/gene/64207):

> This gene encodes a transcription factor that may play a role in regulating female reproductive function. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:14282](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14282) · Entrez [64207](https://www.ncbi.nlm.nih.gov/gene/64207) · UniProt [Q9H1B7](https://www.uniprot.org/uniprotkb/Q9H1B7) · Ensembl [ENSG00000119669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119669)

## Data

Gene col 4093: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4093); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4093, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4093]; `tensor/DDL_lfc|DDL_z.npy` [4093]; `embed/gene_vectors.npy` [4093]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4093 or target_col == 4093). Every well: [[IRF2BPL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRF2BPL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
