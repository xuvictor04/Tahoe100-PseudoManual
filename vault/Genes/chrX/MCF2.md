---
symbol: "MCF2"
type: "gene"
col: 2198
ensembl_id: "ENSG00000101977"
name: "MCF.2 cell line derived transforming sequence"
location: "Xq27.1"
module: 37
arm: "+"
pooled_cpm: 3.24
n_lines_expressing: 47
n_dd_up: 25
n_dd_down: 13
n_dd_up_clean: 18
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# MCF2

*MCF.2 cell line derived transforming sequence* — Xq27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.31× (z +24.5, q 0e+00, up in 29 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.567× (z -5.4, q 5e-05, down in 17 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRZB]] (+0.85, fdr 7e-06), [[LINC02955]] (+0.80, fdr 7e-06), [[PXDNL]] (+0.80, fdr 7e-06); moves opposite to [[MRPS31P4]] (-0.67, fdr 1e-05), [[SDHAF3]] (-0.66, fdr 1e-05), [[ALAD]] (-0.66, fdr 4e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[ATP11C]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2198.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.31×** | +24.5 | 0e+00 | 29/30 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **7.79×** | +18.6 | 0e+00 | 24/28 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.95×** | +14.5 | 4e-45 | 26/33 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.36×** | +11.4 | 5e-28 | 20/34 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.11×** | +9.9 | 3e-21 | 21/42 (PANC-1, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.06×** | +9.6 | 8e-20 | 20/43 (HOP62, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +8.6 | 4e-16 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.44×** | +7.8 | 6e-13 | 4/9 (HOP62, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +6.3 | 2e-08 | 4/15 (SW480, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.91×** | +6.1 | 6e-08 | 16/41 (HOP62, NCI-H460, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.81×** | +5.1 | 2e-05 | 6/38 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.58×** | +4.3 | 8e-04 | 8/35 (A-427, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.59×** | +4.1 | 0.002 | 8/41 (A498, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +4.0 | 0.002 | 5/23 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +4.0 | 0.002 | 7/43 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.008 | 12/32 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.018 | 7/43 (NCI-H460, H4, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.018 | 7/39 (SHP-77, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.037 | 8/36 (SW480, A498, …) | rises with dose |  |
| [[Gefitinib (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.059 | 3/43 (A498, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2198.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.567×** | -5.4 | 5e-05 | 17/42 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.628×** | -4.4 | 0.002 | 12/42 (HS-578T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.725×** | -4.3 | 0.002 | 12/40 (PANC-1, LOX-IMVI, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.418×** | -4.3 | 0.002 | 8/23 (HOP62, A549, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.646×** | -4.0 | 0.008 | 11/15 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Posaconazole (drug)]] 5 µM |  | **0.664×** | -3.7 | 0.019 | 5/43 (hTERT-HPNE, AN3 CA, …) | top dose only | plate-row cell shift; position effect removed |
| [[Bexarotene (drug)]] 5 µM |  | **0.683×** | -3.6 | 0.026 | 7/43 (SW48, Panc 03.27, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.488×** | -3.5 | 0.028 | 7/37 (RKO, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.504×** | -3.4 | 0.045 | 12/37 (LOX-IMVI, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Flutamide (drug)]] 5 µM |  | **0.704×** | -3.3 | 0.052 | 8/42 (CFPAC-1, LS 180, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.716×** | -3.2 | 0.082 | 4/43 (AN3 CA, BT-474, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.630×** | -3.1 | 0.088 | 2/43 (NCI-H1573, NCI-H2030) | inconsistent across doses | noisy plate (z scaled) |
| [[Lopinavir (drug)]] 5 µM |  | **0.724×** | -3.0 | 0.100 | 6/43 (SW 900, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2198. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 3.32 | 3 | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +9.7) | [[Roxadustat (drug)]] 0.05 µM 0.0776× (z -10.1) |
| [[HOP62 (line)]] | alt | 3.23 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.15× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 4.72 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.37× (z +12.9) | — |
| [[A498 (line)]] | wt | 4.68 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +12.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0941× (z -8.6) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 16.0 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 8.99× (z +9.7) | — |
| [[C32 (line)]] | wt | 1.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.7× (z +8.7) | — |
| [[LoVo (line)]] | wt | 6.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 1.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.8× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 3.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.30× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 2.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.9× (z +9.8) | — |
| [[A-172 (line)]] | wt | 0.789 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.825 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.911 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.948 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2198), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRZB]] | +0.85 | +0.81 / +0.77 | both halves | 7e-06 |  |
| [[LINC02955]] | +0.80 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[PXDNL]] | +0.80 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.79 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.79 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.79 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[MFSD2B]] | +0.78 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[DPYS]] | +0.77 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[YIPF7]] | +0.77 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[LINC00393]] | +0.77 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.77 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[SLC26A7]] | +0.76 | +0.77 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS31P4]] | -0.67 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[SDHAF3]] | -0.66 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[ALAD]] | -0.66 | -0.40 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MCF2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP11C]] | C | MCF2 activity raises ATP11C's level | lines that do not express MCF2 (3) vs lines expressing it (47) | 2.59× lower at baseline in the lines without MCF2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SATB2; maybe low, not absent; its own permutation p |
| [[C21orf91-OT1]] | C | MCF2 activity raises C21orf91-OT1's level | lines that do not express MCF2 (3) vs lines expressing it (47) | 1.80× lower at baseline in the lines without MCF2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SATB2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.679). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.1, -14.1); signed map (19.2, 2.8). **Vector** length 77.1, 13.2% of its response variance represented; |z| ≥ 3 in 1,230 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +24.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +18.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +14.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +11.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +6.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +2.6 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.9 | -5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -4.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -3.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.8 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | MCF.2 cell line derived transforming sequence |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq27.1 — chrX:139,581,770-139,708,216 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DBL, ARHGEF21 |
| Gene groups (HGNC) | Dbl family Rho GEFs; CRAL-TRIO lipid binding domain containing |
| Reactome | 20 pathways, smallest: Axonal growth inhibition (RHOA activation); p75NTR regulates axonogenesis; NRAGE signals death through JNK |
| Matched by | ensembl_id |

**Function**, from UniProt [P10911](https://www.uniprot.org/uniprotkb/P10911) (Proto-oncogene DBL):

> Guanine nucleotide exchange factor (GEF) that modulates the Rho family of GTPases. Promotes the conversion of some member of the Rho family GTPase from the GDP-bound to the GTP-bound form. Isoform 1 exhibits no activity toward RHOA, RAC1 or CDC42. Isoform 2 exhibits decreased GEF activity toward CDC42. Isoform 3 exhibits a weak but significant activity toward RAC1 and CDC42. Isoform 4 exhibits significant activity toward RHOA and CDC42. The truncated DBL oncogene is active toward RHOA, RAC1 and …

**Summary**, from NCBI Gene [4168](https://www.ncbi.nlm.nih.gov/gene/4168):

> The oncogenic protein encoded by this gene is a guanine nucleotide exchange factor (GEF) that exerts control over some members of the Rho family of small GTPases. Several transcript variants encoding different isoforms have been found for this gene. These isoforms exhibit different expression patterns and varying levels of GEF activity.[provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:6940](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6940) · Entrez [4168](https://www.ncbi.nlm.nih.gov/gene/4168) · UniProt [P10911](https://www.uniprot.org/uniprotkb/P10911) · Ensembl [ENSG00000101977](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101977)

## Data

Gene col 2198: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2198); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2198, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2198]; `tensor/DDL_lfc|DDL_z.npy` [2198]; `embed/gene_vectors.npy` [2198]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2198 or target_col == 2198). Every well: [[MCF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
