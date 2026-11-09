---
symbol: "LIG4"
type: "gene"
col: 10489
ensembl_id: "ENSG00000174405"
name: "DNA ligase 4"
location: "13q33.3"
module: 16
arm: "+"
pooled_cpm: 9.28
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 29
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# LIG4

*DNA ligase 4* — 13q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.32× (z +25.5, q 0e+00, up in 42 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HT-29 0.155×); [[Ipatasertib (drug)]] 0.5 µM in 1 line (RKO 0.0579×); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 0.120×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (BT-474 0.0657×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF260]] (+0.79, fdr 7e-06), [[BCDIN3D]] (+0.77, fdr 7e-06), [[VEZF1]] (+0.77, fdr 7e-06); moves opposite to [[UQCRH]] (-0.75, fdr 7e-06), [[MED26]] (-0.73, fdr 7e-06), [[SDHAP2]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RGS10]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10489.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.32×** | +25.5 | 0e+00 | 42/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.43×** | +20.0 | 0e+00 | 43/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.52×** | +18.5 | 0e+00 | 40/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.03×** | +13.6 | 4e-40 | 41/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.40×** | +10.4 | 5e-23 | 29/35 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +7.6 | 3e-12 | 28/47 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.83×** | +7.4 | 9e-12 | 32/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.81×** | +7.3 | 2e-11 | 24/47 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +7.2 | 3e-11 | 31/45 (COLO 205, NCI-H23, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.72×** | +6.7 | 1e-09 | 24/45 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.3 | 2e-08 | 20/42 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +6.0 | 1e-07 | 9/16 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +5.9 | 1e-07 | 23/47 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.8 | 3e-07 | 16/48 (A498, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +5.2 | 7e-06 | 20/46 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +5.2 | 7e-06 | 16/47 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +4.7 | 7e-05 | 20/47 (SW480, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10489.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HT-29 0.155×); [[Ipatasertib (drug)]] 0.5 µM in 1 line (RKO 0.0579×); [[Digitoxin (drug)]] 5 µM in 1 line (KATO III 0.120×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (BT-474 0.0657×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Naproxen (drug)]] 5 µM |  | 0.760× | -3.2 | 0.71 | 9/44 (AsPC-1, HT-29, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10489. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +15.9) | — |
| [[A-172 (line)]] | wt | 13.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +14.0) | — |
| [[A498 (line)]] | wt | 7.40 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.04× (z +14.5) | — |
| [[PANC-1 (line)]] | alt | 7.42 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +15.5) | — |
| [[RKO (line)]] | wt | 16.8 | 3 | 1 | [[Harringtonine (drug)]] 5 µM 7.45× (z +10.6) | [[Ipatasertib (drug)]] 0.5 µM 0.0579× (z -11.2) |
| [[COLO 205 (line)]] | alt | 15.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 4.94 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.58× (z +12.3) | — |
| [[SW480 (line)]] | alt | 14.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +14.2) | — |
| [[A549 (line)]] | wt | 5.79 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.49× (z +11.9) | — |
| [[AsPC-1 (line)]] | alt | 3.90 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +12.3) | — |
| [[HT-29 (line)]] | alt | 14.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +12.7) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.155× (z -11.6) |
| [[KATO III (line)]] | alt | 10.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.120× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LOX-IMVI (line)]] | wt | 10.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.81× (z +13.4) | — |
| [[NCI-H1573 (line)]] | alt | 19.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 4.56 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.10× (z +13.4) | — |
| [[BT-474 (line)]] | alt | 6.63 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0657× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +10.6) | — |
| [[J82 (line)]] | alt | 14.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +13.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.41 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 7.45× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 3.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.95× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 7.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 9.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +10.0) | — |
| [[A-427 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10489), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF260]] | +0.79 | +0.74 / +0.79 | both halves | 7e-06 |  |
| [[BCDIN3D]] | +0.77 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[VEZF1]] | +0.77 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[ZNF518B]] | +0.75 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[UBQLN2]] | +0.74 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[ZNF776]] | +0.73 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[ZNF620]] | +0.73 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[C7orf25]] | +0.73 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[ZNF606]] | +0.72 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[ZNF655]] | +0.72 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[ZBTB33]] | +0.72 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[LZIC]] | +0.71 | +0.73 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRH]] | -0.75 | -0.68 / -0.70 | both halves | 7e-06 |  |
| [[MED26]] | -0.73 | -0.69 / -0.71 | both halves | 7e-06 |  |
| [[SDHAP2]] | -0.70 | -0.71 / -0.61 | both halves | 7e-06 |  |
| [[GMCL1]] | -0.70 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[SDHAP1]] | -0.70 | -0.73 / -0.55 | both halves | 1e-05 |  |
| [[SHQ1]] | -0.69 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[IGSF8]] | -0.68 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[QPCTL]] | -0.67 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[RARS2]] | -0.67 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[RGS10]] | -0.66 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[THOC3]] | -0.66 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[L2HGDH]] | -0.66 | -0.58 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS10]] | C | RGS10 activity lowers LIG4's level | lines that do not express RGS10 (4) vs lines expressing it (46) | 1.61× higher at baseline in the lines without RGS10 | 0.099 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, ARHGEF17, CHST3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.767). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-31.6, 12.6); signed map (3.2, -29.5). **Vector** length 81.4, 15.8% of its response variance represented; |z| ≥ 3 in 1,181 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.3 | +13.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.5 | +20.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.4 | +18.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.1 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +25.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +7.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.2 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +5.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +4.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.7 | +5.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.6 | +7.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.3 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.4 | -2.7 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | DNA ligase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q33.3 — chr13:108,207,439-108,218,368 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | DNA ligases |
| Reactome | 9 pathways, smallest: 2-LTR circle formation; Integration of provirus; Early Phase of HIV Life Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P49917](https://www.uniprot.org/uniprotkb/P49917) (DNA ligase 4):

> DNA ligase involved in DNA non-homologous end joining (NHEJ); required for double-strand break (DSB) repair and V(D)J recombination. Catalyzes the NHEJ ligation step of the broken DNA during DSB repair by resealing the DNA breaks after the gap filling is completed. Joins single-strand breaks in a double-stranded polydeoxynucleotide in an ATP-dependent reaction. LIG4 is mechanistically flexible: it can ligate nicks as well as compatible DNA overhangs alone, while in the presence of XRCC4, it can …

**Summary**, from NCBI Gene [3981](https://www.ncbi.nlm.nih.gov/gene/3981):

> The protein encoded by this gene is a DNA ligase that joins single-strand breaks in a double-stranded polydeoxynucleotide in an ATP-dependent reaction. This protein is essential for V(D)J recombination and DNA double-strand break (DSB) repair through nonhomologous end joining (NHEJ). This protein forms a complex with the X-ray repair cross complementing protein 4 (XRCC4), and further interacts with the DNA-dependent protein kinase (DNA-PK). Both XRCC4 and DNA-PK are known to be required for …

**Accessions** — [HGNC:6601](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6601) · Entrez [3981](https://www.ncbi.nlm.nih.gov/gene/3981) · UniProt [P49917](https://www.uniprot.org/uniprotkb/P49917) · Ensembl [ENSG00000174405](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174405)

## Data

Gene col 10489: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10489); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10489, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10489]; `tensor/DDL_lfc|DDL_z.npy` [10489]; `embed/gene_vectors.npy` [10489]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10489 or target_col == 10489). Every well: [[LIG4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIG4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
