---
symbol: "NUP210L"
type: "gene"
col: 6769
ensembl_id: "ENSG00000143552"
name: "nucleoporin 210 like"
location: "1q21.3"
module: 53
arm: "+"
pooled_cpm: 6.48
n_lines_expressing: 50
n_dd_up: 43
n_dd_down: 2
n_dd_up_clean: 31
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# NUP210L

*nucleoporin 210 like* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 9.50× (z +40.6, q 0e+00, up in 41 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.473× (z -5.0, q 3e-04, down in 12 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.0779×); [[Pimozide (drug)]] 0.05 µM in 1 line (A-172 0.131×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R36]] (+0.83, fdr 7e-06), [[LINC00393]] (+0.82, fdr 7e-06), [[DNAH10]] (+0.81, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6769.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **9.50×** | +40.6 | 0e+00 | 41/41 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.15×** | +29.5 | 0e+00 | 34/38 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **7.18×** | +25.1 | 0e+00 | 43/44 (NCI-H460, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.09×** | +14.4 | 1e-44 | 30/38 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.94×** | +13.7 | 8e-41 | 42/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.11×** | +13.5 | 2e-39 | 30/48 (HOP62, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.85×** | +12.8 | 8e-36 | 28/38 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +12.1 | 5e-32 | 7/11 (HEC-1-A, HOP62, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.78×** | +12.0 | 2e-31 | 12/18 (SW480, J82, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.66×** | +12.0 | 3e-31 | 28/38 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +10.4 | 2e-23 | 19/31 (SW480, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +8.6 | 3e-16 | 19/32 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.93×** | +8.3 | 3e-15 | 24/47 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +8.1 | 3e-14 | 26/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +7.3 | 8e-12 | 21/48 (SW480, A498, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.68×** | +6.6 | 1e-09 | 18/47 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +6.6 | 1e-09 | 15/47 (J82, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.07×** | +6.4 | 5e-09 | 18/44 (A-172, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +6.2 | 2e-08 | 19/44 (MIA PaCa-2, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6769.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (drug)]] 0.05 µM in 1 line (LOX-IMVI 0.0779×); [[Pimozide (drug)]] 0.05 µM in 1 line (A-172 0.131×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.473×** | -5.0 | 3e-04 | 12/39 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.748×** | -3.6 | 0.094 | 8/43 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | 0.781× | -3.1 | 0.41 | 6/44 (HT-29, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6769. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 7.37 | 5 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +15.9) | [[Pimozide (drug)]] 0.05 µM 0.131× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 4.46 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.8× (z +23.1) | — |
| [[SW480 (line)]] | alt | 5.83 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.12× (z +14.9) | — |
| [[C32 (line)]] | wt | 6.85 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.1× (z +15.1) | — |
| [[HOP62 (line)]] | alt | 4.77 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.9× (z +14.8) | — |
| [[LoVo (line)]] | wt | 5.82 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +17.1) | — |
| [[HS-578T (line)]] | alt | 5.63 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +12.2) | — |
| [[LOX-IMVI (line)]] | wt | 5.59 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.7× (z +15.0) | [[Canagliflozin (drug)]] 0.05 µM 0.0779× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 13.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +14.7) | — |
| [[NCI-H2347 (line)]] | alt | 6.88 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.00× (z +13.5) | — |
| [[PANC-1 (line)]] | alt | 3.37 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +14.8) | — |
| [[A498 (line)]] | wt | 5.51 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.7× (z +18.0) | — |
| [[HEC-1-A (line)]] | alt | 18.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.55× (z +12.4) | — |
| [[HT-29 (line)]] | alt | 5.75 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.24× (z +11.5) | — |
| [[J82 (line)]] | alt | 5.92 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.90× (z +11.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.39 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.1× (z +12.8) | — |
| [[NCI-H2030 (line)]] | alt | 21.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.36× (z +13.3) | — |
| [[SNU-423 (line)]] | alt | 2.94 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +10.4) | — |
| [[SW 900 (line)]] | alt | 9.69 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +12.0) | — |
| [[A549 (line)]] | wt | 4.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.2× (z +12.0) | — |
| [[AsPC-1 (line)]] | alt | 4.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.4× (z +12.7) | — |
| [[BT-474 (line)]] | alt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.6× (z +14.3) | — |
| [[CFPAC-1 (line)]] | alt | 4.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.6× (z +12.6) | — |
| [[H4 (line)]] | wt | 7.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.77× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +11.4) | — |
| [[HepG2_C3A (line)]] | wt | 3.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.0× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 5.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.28× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 7.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +11.0) | — |
| [[KATO III (line)]] | alt | 5.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 4.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.44× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 6.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.28× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 3.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.7× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 2.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.3× (z +10.6) | — |
| [[RKO (line)]] | wt | 3.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.4× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 8.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 7.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.56× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 4.34 | 1 | 0 | [[Auranofin (drug)]] 5 µM 65.6× (z +12.4) | — |
| [[SW1417 (line)]] | alt | 3.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +10.9) | — |
| [[SW48 (line)]] | wt | 5.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +9.1) | — |
| [[A-427 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6769), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R36]] | +0.83 | +0.77 / +0.79 | both halves | 7e-06 |  |
| [[LINC00393]] | +0.82 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[DNAH10]] | +0.81 | +0.80 / +0.73 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.81 | +0.85 / +0.73 | both halves | 7e-06 |  |
| [[LINC02955]] | +0.81 | +0.83 / +0.75 | both halves | 7e-06 |  |
| [[LRP2BP]] | +0.80 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.80 | +0.82 / +0.73 | both halves | 7e-06 |  |
| [[LINC01588]] | +0.80 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[LINC00880]] | +0.80 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[FAM184B]] | +0.79 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[USP50]] | +0.79 | +0.85 / +0.68 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.79 | +0.82 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F2]] | B | F2 activity raises NUP210L's level | lines that do not express F2 (11) vs lines expressing it (39) | 1.38× lower at baseline in the lines without F2 | 0.051 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers NUP210L's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MLIP]] | B | MLIP activity raises NUP210L's level | lines that do not express MLIP (7) vs lines expressing it (43) | 1.36× lower at baseline in the lines without MLIP | 0.093 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.861). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.5, -11.0); signed map (21.5, 9.5). **Vector** length 82.6, 16.5% of its response variance represented; |z| ≥ 3 in 1,152 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.2 | +25.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.9 | +40.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.5 | +12.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +29.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +12.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +13.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.0 | +6.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.5 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +7.3 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +0.5 |
|  | [[NG25 (drug)]] 5 µM |  | -2.8 | -5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | +1.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.7 | +8.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | nucleoporin 210 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:153,992,690-154,155,116 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q5VU65](https://www.uniprot.org/uniprotkb/Q5VU65) carries no function annotation.

**Summary**, from NCBI Gene [91181](https://www.ncbi.nlm.nih.gov/gene/91181):

> Predicted to act upstream of or within Sertoli cell development and spermatid development. Predicted to be located in nuclear membrane. Predicted to be part of nuclear pore. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29915](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29915) · Entrez [91181](https://www.ncbi.nlm.nih.gov/gene/91181) · UniProt [Q5VU65](https://www.uniprot.org/uniprotkb/Q5VU65) · Ensembl [ENSG00000143552](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143552)

## Data

Gene col 6769: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6769); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6769, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6769]; `tensor/DDL_lfc|DDL_z.npy` [6769]; `embed/gene_vectors.npy` [6769]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6769 or target_col == 6769). Every well: [[NUP210L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUP210L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
