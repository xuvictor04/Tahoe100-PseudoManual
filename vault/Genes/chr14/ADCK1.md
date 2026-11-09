---
symbol: "ADCK1"
type: "gene"
col: 732
ensembl_id: "ENSG00000063761"
name: "aarF domain containing kinase 1"
location: "14q24.3"
module: 124
arm: "+"
pooled_cpm: 5.54
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# ADCK1

*aarF domain containing kinase 1* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.82× (z +14.3, q 1e-43, up in 38 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.607× (z -4.9, q 6e-04, down in 18 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.0870×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (SHP-77 0.112×).
> Its strongest partners by |cos| (74 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 26 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPM2A]] (+0.77, fdr 2e-05), [[CRPPA]] (+0.74, fdr 2e-04), [[GABPB1-AS1]] (+0.74, fdr 4e-05); moves opposite to [[SLC27A1]] (-0.65, fdr 6e-04), [[GNAI2]] (-0.65, fdr 8e-04, ⚠ one half only (not replicated)), [[EFHC1]] (-0.64, fdr 4e-05), [[ACTR6]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 732.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.82×** | +14.3 | 1e-43 | 38/42 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +8.1 | 1e-13 | 30/39 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +7.6 | 4e-12 | 24/40 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.66×** | +7.0 | 5e-10 | 19/46 (HEC-1-A, BT-474, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.85×** | +5.8 | 9e-07 | 20/43 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +5.5 | 3e-06 | 20/45 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +5.3 | 8e-06 | 16/40 (NCI-H2347, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.67×** | +5.0 | 4e-05 | 18/47 (LoVo, NCI-H1573, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +4.4 | 6e-04 | 14/37 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +4.4 | 7e-04 | 1/7 (BT-474) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +4.4 | 7e-04 | 4/12 (SW1417, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.49×** | +3.9 | 0.004 | 15/47 (hTERT-HPNE, H4, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.024 | 16/47 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.42×** | +3.4 | 0.028 | 11/44 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.028 | 11/46 (RPMI-7951, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Afatinib (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.036 | 4/46 (NCI-H2030, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.052 | 8/45 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.057 | 5/43 (A-427, LoVo, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.057 | 7/42 (SW480, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 732.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.0870×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (SHP-77 0.112×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.607×** | -4.9 | 6e-04 | 18/37 (SHP-77, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.695× | -3.6 | 0.10 | 18/47 (PANC-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 0.729× | -3.1 | 0.35 | 13/47 (A-427, SW480, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.734× | -3.0 | 0.35 | 16/45 (A-427, SHP-77, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.62 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 732. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 8.79 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0870× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Saquinavir (drug)]] 0.5 µM 0.112× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 1.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.5× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 4.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.90× (z +10.2) | — |
| [[A-172 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 732), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 25 of them with an alert (⚠; 25 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPM2A]] | +0.77 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[CRPPA]] | +0.74 | +0.66 / +0.31 | both halves | 2e-04 |  |
| [[GABPB1-AS1]] | +0.74 | +0.71 / +0.42 | both halves | 4e-05 |  |
| [[TMEM147-AS1]] | +0.73 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[DPH5-DT]] | +0.72 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[MAD2L1-DT]] | +0.69 | +0.69 / +0.40 | both halves | 5e-05 |  |
| [[MYLK-AS1]] | +0.69 | +0.73 / +0.38 | both halves | 7e-05 |  |
| [[ZNF337-AS1]] | +0.67 | +0.70 / +0.31 | both halves | 2e-04 |  |
| [[PIGW]] | +0.67 | +0.60 / +0.31 | both halves | 2e-04 |  |
| [[KICS2]] | +0.67 | +0.73 / +0.38 | both halves | 6e-05 |  |
| [[ENOX2]] | +0.66 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[AVEN]] | +0.66 | +0.56 / +0.32 | both halves | 1e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A1]] | -0.65 | -0.64 / -0.22 | both halves | 6e-04 |  |
| [[GNAI2]] | -0.65 | -0.61 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[EFHC1]] | -0.64 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ACTR6]] | -0.63 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[CARHSP1]] | -0.62 | -0.61 / -0.24 | both halves | 5e-04 |  |
| [[ARL3]] | -0.62 | -0.55 / -0.26 | both halves | 4e-04 |  |
| [[DPY30]] | -0.62 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[RRAS]] | -0.62 | -0.60 / -0.29 | both halves | 2e-04 |  |
| [[MGST3]] | -0.62 | -0.57 / -0.25 | both halves | 4e-04 |  |
| [[FBXO33]] | -0.61 | -0.53 / -0.40 | both halves | 4e-05 |  |
| [[RAB11FIP1]] | -0.60 | -0.54 / -0.26 | both halves | 4e-04 |  |
| [[HAUS3]] | -0.59 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[WASF2]] | -0.59 | -0.64 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ADCK1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MYO1E]] | B | MYO1E activity lowers ADCK1's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 1.93× higher at baseline in the lines without MYO1E | 0.059 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[PRKAR1B]] | B | PRKAR1B activity raises ADCK1's level | lines that do not express PRKAR1B (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without PRKAR1B | 0.094 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.800). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-3.3, 9.0); signed map (24.6, -28.6). **Vector** length 64.2, 9.57% of its response variance represented; |z| ≥ 3 in 1,060 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +14.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +7.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +2.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +0.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | +0.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | +3.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.4 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | +0.8 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.3 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -1.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.3 | -0.4 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | aarF domain containing kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:77,800,109-77,935,014 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39600 |
| Gene groups (HGNC) | ADCK family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86TW2](https://www.uniprot.org/uniprotkb/Q86TW2) (AarF domain-containing protein kinase 1):

> Appears to be essential for maintaining mitochondrial cristae formation and mitochondrial function by acting via YME1L1 in a kinase-independent manner to regulate essential mitochondrial structural proteins OPA1 and IMMT. The action of this enzyme is not yet clear (Probable). It is not known if it has protein kinase activity and what type of substrate it would phosphorylate (Ser, Thr or Tyr) (Probable).

**Summary**, from NCBI Gene [57143](https://www.ncbi.nlm.nih.gov/gene/57143):

> Predicted to enable ATP binding activity and protein serine/threonine kinase activity. Involved in negative regulation of mitochondrial fusion and positive regulation of cristae formation. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19038](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19038) · Entrez [57143](https://www.ncbi.nlm.nih.gov/gene/57143) · UniProt [Q86TW2](https://www.uniprot.org/uniprotkb/Q86TW2) · Ensembl [ENSG00000063761](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000063761)

## Data

Gene col 732: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 732); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 732, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 732]; `tensor/DDL_lfc|DDL_z.npy` [732]; `embed/gene_vectors.npy` [732]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 732 or target_col == 732). Every well: [[ADCK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADCK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
