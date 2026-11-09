---
symbol: "DLGAP2"
type: "gene"
col: 12511
ensembl_id: "ENSG00000198010"
name: "DLG associated protein 2"
location: "8p23.3"
module: 165
arm: "+"
pooled_cpm: 2.63
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# DLGAP2

*DLG associated protein 2* — 8p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 10.8× (z +29.7, q 0e+00, up in 23 of 26 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.106×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.213×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.132×; ⚠ toxic); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.180×); [[BAY1125976 (drug)]] 0.05 µM in 1 line (LoVo 0.0470×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBFOX3]] (+0.82, fdr 7e-06), [[MIR4300HG]] (+0.82, fdr 7e-06), [[USH2A]] (+0.82, fdr 7e-06).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12511.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **10.8×** | +29.7 | 0e+00 | 23/26 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **9.14×** | +27.6 | 0e+00 | 29/29 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.19×** | +12.7 | 2e-34 | 22/25 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.62×** | +12.0 | 3e-31 | 29/43 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **3.88×** | +12.0 | 5e-31 | 24/34 (SW480, SHP-77, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.07×** | +11.9 | 1e-30 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.45×** | +10.9 | 7e-26 | 4/8 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.02×** | +9.0 | 2e-17 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.46×** | +8.0 | 1e-13 | 22/44 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.31×** | +7.4 | 8e-12 | 19/41 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.75×** | +7.0 | 1e-10 | 6/43 (HEC-1-A, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.08×** | +6.5 | 5e-09 | 12/31 (A-427, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.09×** | +6.3 | 2e-08 | 14/35 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +5.6 | 1e-06 | 6/29 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.86×** | +5.5 | 2e-06 | 14/39 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +5.1 | 2e-05 | 4/19 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +4.6 | 1e-04 | 14/43 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.008 | 2/25 (HEC-1-A, PANC-1) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12511.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.106×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.213×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.132×; ⚠ toxic); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.180×); [[BAY1125976 (drug)]] 0.05 µM in 1 line (LoVo 0.0470×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.909× | -3.1 | 0.97 | 15/47 (C32, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12511. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 48.5 | 2 | 7 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 4.60× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.213× (z -13.3) |
| [[SW480 (line)]] | alt | 1.34 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.0× (z +12.6) | — |
| [[LoVo (line)]] | wt | 1.89 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.0× (z +13.0) | [[BAY1125976 (drug)]] 0.05 µM 0.0470× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 1.96 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 76.1× (z +14.2) | — |
| [[A-172 (line)]] | wt | 1.27 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.4× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 1.81 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.27× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 2.51 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 11.9× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 1.74 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.0× (z +12.7) | — |
| [[A498 (line)]] | wt | 1.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.2× (z +10.8) | — |
| [[A549 (line)]] | wt | 2.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.0× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 1.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 40.4× (z +12.2) | — |
| [[Hs 766T (line)]] | wt | 1.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.0× (z +12.0) | — |
| [[KATO III (line)]] | alt | 1.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 40.1× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 1.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 28.2× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 2.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 48.4× (z +12.1) | — |
| [[NCI-H2347 (line)]] | alt | 1.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 0.952 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.66× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 2.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.1× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 6.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.992 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.942 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12511), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBFOX3]] | +0.82 | +0.75 / +0.84 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.82 | +0.81 / +0.84 | both halves | 7e-06 |  |
| [[USH2A]] | +0.82 | +0.81 / +0.81 | both halves | 7e-06 |  |
| [[MTUS2]] | +0.81 | +0.71 / +0.84 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.81 | +0.74 / +0.87 | both halves | 7e-06 |  |
| [[XKR4]] | +0.81 | +0.83 / +0.77 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.80 | +0.74 / +0.82 | both halves | 7e-06 |  |
| [[KCNAB1]] | +0.80 | +0.83 / +0.78 | both halves | 7e-06 | pathway: Neuronal System |
| [[LINC01579]] | +0.80 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.79 | +0.75 / +0.80 | both halves | 7e-06 |  |
| [[DPP6]] | +0.78 | +0.78 / +0.80 | both halves | 7e-06 | STRING 477 |
| [[RYR3]] | +0.78 | +0.65 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DLGAP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM | C | DLGAP2's natural level lowers the cells' numbers under Fedratinib (hydrochloride hydrate) 5 µM (makes them more sensitive) | DLGAP2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.72 | 0.206 over the table, 0.011 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.903). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.0, 30.4); signed map (30.6, 16.3). **Vector** length 51.6, 7.03% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +27.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +29.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +12.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +11.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +7.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +3.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | -0.3 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | DLG associated protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.3 — chr8:737,628-1,708,476 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DAP-2; previously ERICH1-AS1, C8orf68 |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P1A6](https://www.uniprot.org/uniprotkb/Q9P1A6) (DLG-associated protein 2):

> May play a role in the molecular organization of synapses and neuronal cell signaling. Could be an adapter protein linking ion channel to the subsynaptic cytoskeleton. May induce enrichment of PSD-95/SAP90 at the plasma membrane.

**Summary**, from NCBI Gene [9228](https://www.ncbi.nlm.nih.gov/gene/9228):

> The product of this gene is a membrane-associated protein that may play a role in synapse organization and signalling in neuronal cells. This gene is biallelically expressed in the brain, however, only the paternal allele is expressed in the testis (PMID:18055845). Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:2906](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2906) · Entrez [9228](https://www.ncbi.nlm.nih.gov/gene/9228) · UniProt [Q9P1A6](https://www.uniprot.org/uniprotkb/Q9P1A6) · Ensembl [ENSG00000198010](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198010)

## Data

Gene col 12511: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12511); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12511, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12511]; `tensor/DDL_lfc|DDL_z.npy` [12511]; `embed/gene_vectors.npy` [12511]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12511 or target_col == 12511). Every well: [[DLGAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLGAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
