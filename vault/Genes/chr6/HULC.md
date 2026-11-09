---
symbol: "HULC"
type: "gene"
col: 16097
ensembl_id: "ENSG00000285219"
name: "hepatocellular carcinoma up-regulated long non-coding RNA"
location: "6p24.3"
module: 191
arm: "+"
pooled_cpm: 2.35
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/191"]
generated_by: "tahoemap"
---

# HULC

*hepatocellular carcinoma up-regulated long non-coding RNA* — 6p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.44× (z +27.2, q 0e+00, up in 32 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ciclopirox (drug)]] 0.05 µM in 1 line (A498 0.0499×); [[Bimatoprost (drug)]] 0.05 µM in 1 line (SHP-77 0.0600×); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0662×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNAB1]] (+0.84, fdr 7e-06), [[DNAH3]] (+0.81, fdr 7e-06), [[LINC01933]] (+0.77, fdr 7e-06); moves opposite to [[IQCB1]] (-0.58, fdr 1e-05).
> It is in [[Module 191]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16097.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.44×** | +27.2 | 0e+00 | 32/34 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.57×** | +21.9 | 0e+00 | 29/31 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **9.24×** | +20.1 | 0e+00 | 38/46 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **5.96×** | +16.1 | 0e+00 | 33/39 (C32, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.45×** | +15.3 | 0e+00 | 34/42 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.42×** | +12.9 | 5e-36 | 34/39 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.73×** | +12.8 | 1e-35 | 34/45 (SW480, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.99×** | +12.5 | 7e-34 | 25/30 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.15×** | +10.4 | 3e-23 | 11/15 (LS 180, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.25×** | +10.2 | 8e-23 | 0/1 | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.56×** | +9.6 | 3e-20 | 1/3 (PANC-1) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.65×** | +8.8 | 8e-17 | 24/44 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.50×** | +8.3 | 6e-15 | 24/41 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.98×** | +6.1 | 4e-08 | 17/43 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +5.6 | 1e-06 | 7/45 (hTERT-HPNE, J82, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +4.9 | 3e-05 | 9/45 (J82, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +4.8 | 5e-05 | 9/23 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.41×** | +4.4 | 4e-04 | 7/45 (SHP-77, HEC-1-A, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16097.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ciclopirox (drug)]] 0.05 µM in 1 line (A498 0.0499×); [[Bimatoprost (drug)]] 0.05 µM in 1 line (SHP-77 0.0600×); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0662×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vilanterol (drug)]] 5 µM |  | 0.759× | -3.6 | 0.15 | 9/42 (Panc 03.27, HS-578T, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 5 µM |  | 0.763× | -3.5 | 0.15 | 6/45 (KATO III, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16097. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 1.83 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 19.4× (z +12.9) | — |
| [[KATO III (line)]] | alt | 3.08 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 23.2× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 2.78 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.9× (z +12.2) | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0662× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 1.85 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.5× (z +15.7) | — |
| [[SHP-77 (line)]] | alt | 5.20 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 44.4× (z +12.4) | [[Bimatoprost (drug)]] 0.05 µM 0.0600× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 3.52 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.3× (z +13.9) | — |
| [[hTERT-HPNE (line)]] | wt | 3.19 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 276× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 2.17 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 47.4× (z +13.2) | — |
| [[SW1417 (line)]] | alt | 2.34 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 29.0× (z +10.9) | — |
| [[C32 (line)]] | wt | 6.42 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.74× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 2.71 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.5× (z +13.0) | — |
| [[A-427 (line)]] | wt | 2.59 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 21.3× (z +8.5) | — |
| [[A498 (line)]] | wt | 1.91 | 0 | 1 | — | [[Ciclopirox (drug)]] 0.05 µM 0.0499× (z -9.2) |
| [[A549 (line)]] | wt | 1.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.1× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 2.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.2× (z +13.1) | — |
| [[J82 (line)]] | alt | 3.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.36× (z +11.6) | — |
| [[LoVo (line)]] | wt | 1.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 4.07 | 1 | 0 | [[Auranofin (drug)]] 5 µM 26.0× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 1.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.5× (z +9.8) | — |
| [[A-172 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.929 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.43 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16097), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNAB1]] | +0.84 | +0.87 / +0.82 | both halves | 7e-06 |  |
| [[DNAH3]] | +0.81 | +0.82 / +0.80 | both halves | 7e-06 |  |
| [[LINC01933]] | +0.77 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[COL26A1]] | +0.77 | +0.78 / +0.80 | both halves | 7e-06 |  |
| [[ESR1]] | +0.74 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[MAP3K20-AS1]] | +0.74 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[LINC00871]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[DYNLRB2-AS1]] | +0.72 | +0.66 / +0.75 | both halves | 7e-06 |  |
| [[DPP6]] | +0.71 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.71 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.71 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[LINC02208]] | +0.71 | +0.77 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCB1]] | -0.58 | -0.57 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HULC's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00871]] | B | LINC00871 activity raises HULC's level | lines that do not express LINC00871 (12) vs lines expressing it (38) | 1.35× lower at baseline in the lines without LINC00871 | 0.053 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CXCL13]] | B | CXCL13 activity raises HULC's level | lines that do not express CXCL13 (8) vs lines expressing it (42) | 1.34× lower at baseline in the lines without CXCL13 | 0.069 | ⚠ within organs, on part of the lines; also absent: DNAH2; maybe low, not absent |
| [[LINC02456]] | B | LINC02456 activity raises HULC's level | lines that do not express LINC02456 (9) vs lines expressing it (41) | 1.32× lower at baseline in the lines without LINC02456 | 0.089 | ⚠ within organs, on part of the lines; also absent: GUCY1A2, OLFM2, ZNF610; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 191]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.877). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.6, 27.1); signed map (30.2, 14.0). **Vector** length 59.8, 8.79% of its response variance represented; |z| ≥ 3 in 1,187 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.8 | +16.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +27.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +12.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +3.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | +0.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.0 | +0.9 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.5 | +0.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.0 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | hepatocellular carcinoma up-regulated long non-coding RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p24.3 — chr6:8,435,568-9,294,133 (+) |
| Ensembl biotype | lncRNA |
| Also known as | NCRNA00078, LINC00078, HCCAT1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [728655](https://www.ncbi.nlm.nih.gov/gene/728655):

> This gene produces a long RNA that was discovered as upregulated in hepatocellular carcinoma and is associated with cancer progression. Expression of this transcript is regulated by microRNAs and at the transcriptional level by Sp1 family factors. The transcript may regulate gene expression by functioning as a competing RNA for microRNAs. [provided by RefSeq, Dec 2017]

**Accessions** — [HGNC:34232](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34232) · Entrez [728655](https://www.ncbi.nlm.nih.gov/gene/728655) · Ensembl [ENSG00000285219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000285219)

## Data

Gene col 16097: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16097); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16097, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16097]; `tensor/DDL_lfc|DDL_z.npy` [16097]; `embed/gene_vectors.npy` [16097]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16097 or target_col == 16097). Every well: [[HULC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HULC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
