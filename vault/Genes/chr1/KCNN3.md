---
symbol: "KCNN3"
type: "gene"
col: 6777
ensembl_id: "ENSG00000143603"
name: "potassium calcium-activated channel subfamily N member 3"
location: "1q21.3"
module: 61
arm: "+"
pooled_cpm: 4.78
n_lines_expressing: 42
n_dd_up: 32
n_dd_down: 1
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# KCNN3

*potassium calcium-activated channel subfamily N member 3* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 12.9× (z +27.8, q 0e+00, up in 35 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.695× (z -4.0, q 0.039, down in 9 of 37 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (Hs 766T 0.207×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 0.249×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Triamcinolone (drug)]] 0.5 µM in 1 line (Hs 766T 0.221×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKNOX2]] (+0.67, fdr 7e-06), [[COL5A3]] (+0.66, fdr 7e-06), [[SGCZ]] (+0.66, fdr 7e-06).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NBEAP1]] → it (grade B ⚠); 3 go from it, the strongest it → [[DNAI1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6777.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **12.9×** | +27.8 | 0e+00 | 35/38 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.43×** | +26.0 | 0e+00 | 25/28 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **10.4×** | +25.5 | 0e+00 | 34/36 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.65×** | +23.6 | 0e+00 | 23/28 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **7.60×** | +22.0 | 0e+00 | 31/35 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.90×** | +20.9 | 0e+00 | 30/37 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **4.61×** | +16.6 | 0e+00 | 17/31 (A-172, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.56×** | +16.5 | 0e+00 | 31/37 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.40×** | +12.8 | 2e-35 | 1/6 (LOX-IMVI) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.19×** | +12.6 | 2e-34 | 26/31 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.11×** | +11.8 | 1e-30 | 22/32 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.81×** | +11.2 | 2e-27 | 18/28 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.78×** | +10.3 | 5e-23 | 2/8 (CFPAC-1, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **4.92×** | +9.0 | 7e-18 | 23/32 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.28×** | +8.9 | 2e-17 | 4/16 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.93×** | +7.1 | 4e-11 | 17/34 (A-172, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.9 | 2e-10 | 13/37 (A-172, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.72×** | +5.9 | 1e-07 | 10/26 (SHP-77, C32, …) | rises with dose | cell-cycle shift (explains ~16% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6777.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (Hs 766T 0.207×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 0.249×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Triamcinolone (drug)]] 0.5 µM in 1 line (Hs 766T 0.221×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.695×** | -4.0 | 0.039 | 9/37 (NCI-H23, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6777. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.27 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 30.5× (z +13.6) | — |
| [[A498 (line)]] | wt | 2.08 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 7.26 | 5 | 0 | [[Harringtonine (drug)]] 5 µM 18.6× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 63.5 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.40× (z +10.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 35.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[A-172 (line)]] | wt | 5.66 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.51× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 1.87 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 45.6× (z +12.6) | — |
| [[SHP-77 (line)]] | alt | 6.91 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 26.5× (z +11.0) | — |
| [[SW480 (line)]] | alt | 2.31 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 21.7× (z +11.1) | — |
| [[A549 (line)]] | wt | 1.99 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 65.6× (z +9.8) | — |
| [[C32 (line)]] | wt | 7.99 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 6.82 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.23× (z +12.1) | — |
| [[SNU-423 (line)]] | alt | 6.92 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 14.5× (z +10.5) | — |
| [[BT-474 (line)]] | alt | 3.61 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 85.7× (z +14.0) | — |
| [[CFPAC-1 (line)]] | alt | 3.39 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 24.1× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 2.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.41× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 1.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +9.1) | — |
| [[A-427 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.904 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.822 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.848 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6777), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKNOX2]] | +0.67 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[COL5A3]] | +0.66 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[COL26A1]] | +0.65 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[NHSL2]] | +0.65 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[SYN1]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 | pathway: Neuronal System |
| [[DLGAP2]] | +0.64 | +0.65 / +0.66 | both halves | 7e-06 | pathway: Neuronal System |
| [[CSMD2]] | +0.63 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[VAT1L]] | +0.63 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[IL11]] | +0.62 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ATP8A2]] | +0.62 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[PLCL1]] | +0.62 | +0.58 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NBEAP1]] | B | NBEAP1 activity raises KCNN3's level | lines that do not express NBEAP1 (27) vs lines expressing it (23) | 1.80× lower at baseline in the lines without NBEAP1 | 0.041 | ⚠ within organs, on part of the lines; also absent: EYA2, VAV3, GRAMD1B |
| [[TOP2A]] | B | TOP2A activity lowers KCNN3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CSMD2]] | B | CSMD2 activity raises KCNN3's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 1.99× lower at baseline in the lines without CSMD2 | 0.073 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent |
| [[LINC02220]] | B | LINC02220 activity strengthens KCNN3's drug response | lines that do not express LINC02220 (18) vs lines expressing it (21) | the lines without LINC02220 respond 0.68× as strongly (z diff +1.08); strongest at Panobinostat 5 µM: 8.31x vs 18x (z diff +2.7) | 0.089 | ⚠ within organs, on part of the lines; also absent: COL16A1, SEMA5A, ANKRD30B; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ERG]] | B | ERG activity raises KCNN3's level | lines that do not express ERG (30) vs lines expressing it (20) | 1.72× lower at baseline in the lines without ERG | 0.092 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAI1]] | B | KCNN3 activity raises DNAI1's level | lines that do not express KCNN3 (8) vs lines expressing it (42) | 2.22× lower at baseline in the lines without KCNN3 | 0.056 | ⚠ within organs, on part of the lines; also absent: VLDLR-AS1, ADGRG2, SLC17A7; maybe low, not absent |
| [[IL3RA]] | B | KCNN3 activity raises IL3RA's level | lines that do not express KCNN3 (8) vs lines expressing it (42) | 1.30× lower at baseline in the lines without KCNN3 | 0.073 | ⚠ within organs, on part of the lines; also absent: VLDLR-AS1, ADGRG2, SLC17A7; maybe low, not absent |
| [[SEMA7A]] | B | KCNN3 activity lowers SEMA7A's level | lines that do not express KCNN3 (8) vs lines expressing it (42) | 1.95× higher at baseline in the lines without KCNN3 | 0.098 | ⚠ within organs, on part of the lines; also absent: VLDLR-AS1, ADGRG2, SLC17A7; maybe low, not absent |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.725). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.1, 33.0); signed map (32.1, 25.3). **Vector** length 69.1, 12.8% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +20.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.6 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +6.4 | +12.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +26.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +5.9 | +8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +16.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +3.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.9 | -1.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | potassium calcium-activated channel subfamily N member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:154,697,455-154,870,281 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KCa2.3, hSK3, SKCA3 |
| Gene groups (HGNC) | Potassium calcium-activated channels |
| Reactome | 3 pathways, smallest: Ca2+ activated K+ channels; Potassium Channels; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGI6](https://www.uniprot.org/uniprotkb/Q9UGI6) (Small conductance calcium-activated potassium channel protein 3):

> Small conductance calcium-activated potassium channel that mediates the voltage-independent transmembrane transfer of potassium across the cell membrane through a constitutive interaction with calmodulin which binds the intracellular calcium allowing its opening. The current is characterized by a voltage-independent activation, an intracellular calcium concentration increase-dependent activation and a single-channel conductance of 10 picosiemens. Also presents an inwardly rectifying current, …

**Summary**, from NCBI Gene [3782](https://www.ncbi.nlm.nih.gov/gene/3782):

> Action potentials in vertebrate neurons are followed by an afterhyperpolarization (AHP) that may persist for several seconds and may have profound consequences for the firing pattern of the neuron. Each component of the AHP is kinetically distinct and is mediated by different calcium-activated potassium channels. This gene belongs to the KCNN family of potassium channels. It encodes an integral membrane protein that forms a voltage-independent calcium-activated channel, which is thought to …

**Accessions** — [HGNC:6292](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6292) · Entrez [3782](https://www.ncbi.nlm.nih.gov/gene/3782) · UniProt [Q9UGI6](https://www.uniprot.org/uniprotkb/Q9UGI6) · Ensembl [ENSG00000143603](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143603)

## Data

Gene col 6777: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6777); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6777, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6777]; `tensor/DDL_lfc|DDL_z.npy` [6777]; `embed/gene_vectors.npy` [6777]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6777 or target_col == 6777). Every well: [[KCNN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
