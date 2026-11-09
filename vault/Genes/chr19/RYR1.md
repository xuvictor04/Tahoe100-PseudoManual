---
symbol: "RYR1"
type: "gene"
col: 12157
ensembl_id: "ENSG00000196218"
name: "ryanodine receptor 1"
location: "19q13.2"
module: 21
arm: "+"
pooled_cpm: 4.39
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# RYR1

*ryanodine receptor 1* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 9.10× (z +33.6, q 0e+00, up in 31 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belumosudil (drug)]] 5 µM: 0.591× (z -5.5, q 2e-05, down in 13 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Trifluridine (drug)]] 0.5 µM in 1 line (HCT15 0.0579×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (SK-MEL-2 0.0618×; ⚠ cell-cycle shift, explains ~0% of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0664×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAH10]] (+0.76, fdr 7e-06), [[DLGAP2]] (+0.75, fdr 7e-06), [[KCNAB1]] (+0.75, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12157.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **9.10×** | +33.6 | 0e+00 | 31/32 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.39×** | +18.6 | 0e+00 | 29/36 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.69×** | +16.6 | 0e+00 | 37/43 (SW480, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.91×** | +16.5 | 0e+00 | 4/4 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.88×** | +14.6 | 0e+00 | 34/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.60×** | +13.8 | 3e-41 | 10/11 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.29×** | +11.9 | 2e-30 | 2/6 (SW480, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.86×** | +11.3 | 1e-27 | 28/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.94×** | +10.1 | 5e-22 | 29/45 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.31×** | +8.6 | 3e-16 | 11/30 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +8.3 | 5e-15 | 15/35 (HEC-1-A, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.10×** | +8.0 | 7e-14 | 17/32 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.68×** | +7.9 | 2e-13 | 15/45 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +7.6 | 9e-13 | 4/15 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.94×** | +7.1 | 5e-11 | 22/46 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +4.4 | 3e-04 | 10/41 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +4.1 | 0.002 | 8/44 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.42×** | +3.8 | 0.005 | 2/42 (KATO III, LOX-IMVI) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +3.0 | 0.066 | 1/25 (NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12157.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Trifluridine (drug)]] 0.5 µM in 1 line (HCT15 0.0579×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (SK-MEL-2 0.0618×; ⚠ cell-cycle shift, explains ~0% of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0664×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.591×** | -5.5 | 2e-05 | 13/39 (A-172, H4, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.754× | -3.1 | 0.46 | 17/42 (NCI-H1573, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.740× | -3.0 | 0.46 | 5/44 (HT-29, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12157. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.56 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 2.16 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +15.2) | — |
| [[C32 (line)]] | wt | 1.91 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.8× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 3.31 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.81× (z +11.6) | — |
| [[A549 (line)]] | wt | 3.27 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 30.5× (z +14.4) | — |
| [[HCT15 (line)]] | alt | 12.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +8.8) | [[Trifluridine (drug)]] 0.5 µM 0.0579× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 8.24 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +17.9) | — |
| [[LoVo (line)]] | wt | 1.80 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.4× (z +13.0) | — |
| [[NCI-H2030 (line)]] | alt | 1.97 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.9× (z +11.6) | — |
| [[PANC-1 (line)]] | alt | 19.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.87× (z +9.9) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.270× (z -8.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SK-MEL-2 (line)]] | alt | 8.14 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0618× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Temsirolimus (drug)]] 0.5 µM 0.0664× (z -9.0) |
| [[A-172 (line)]] | wt | 1.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 39.6× (z +13.1) | — |
| [[A498 (line)]] | wt | 3.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.9× (z +16.3) | — |
| [[BT-474 (line)]] | alt | 2.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.5× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 2.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.23× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 2.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 1.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.8× (z +11.9) | — |
| [[NCI-H23 (line)]] | alt | 13.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.89× (z +13.6) | — |
| [[RPMI-7951 (line)]] | alt | 3.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 2.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.0× (z +9.0) | — |
| [[A-427 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12157), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAH10]] | +0.76 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.75 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[KCNAB1]] | +0.75 | +0.65 / +0.81 | both halves | 7e-06 |  |
| [[TMPRSS9]] | +0.74 | +0.68 / +0.79 | both halves | 7e-06 |  |
| [[IL12RB2]] | +0.74 | +0.66 / +0.79 | both halves | 7e-06 |  |
| [[LINC01579]] | +0.73 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[SPATA21]] | +0.72 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[ELAVL3]] | +0.72 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[CELF5]] | +0.71 | +0.65 / +0.78 | both halves | 7e-06 |  |
| [[SYNM-AS1]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[HPSE2]] | +0.71 | +0.53 / +0.80 | both halves | 1e-05 |  |
| [[SEC1P]] | +0.70 | +0.65 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RYR1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP3K9-DT]] | B | MAP3K9-DT activity raises RYR1's level | lines that do not express MAP3K9-DT (17) vs lines expressing it (33) | 1.65× lower at baseline in the lines without MAP3K9-DT | 0.026 | ⚠ within organs, on part of the lines; also absent: KIAA0319, STXBP2, SMPDL3B; maybe low, not absent |
| [[CACNA1B]] | B | CACNA1B activity raises RYR1's level | lines that do not express CACNA1B (15) vs lines expressing it (35) | 1.61× lower at baseline in the lines without CACNA1B | 0.032 | ⚠ within organs, on part of the lines; also absent: DGCR5, PPP1R14C; maybe low, not absent |
| [[STAG3]] | B | STAG3 activity raises RYR1's level | lines that do not express STAG3 (14) vs lines expressing it (36) | 1.53× lower at baseline in the lines without STAG3 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000290931, ENSG00000283674; maybe low, not absent |
| [[MRC2]] | B | MRC2 activity raises RYR1's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 1.59× lower at baseline in the lines without MRC2 | 0.077 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |
| [[GBX1]] | B | GBX1 activity raises RYR1's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 1.64× lower at baseline in the lines without GBX1 | 0.089 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.701). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.2, 31.1); signed map (25.7, 15.2). **Vector** length 61.2, 8.71% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.1 | +16.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +33.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +7.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.0 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.5 | +1.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -0.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -5.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ryanodine receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,433,691-38,595,273 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RYR, PPP1R137; previously MHS, MHS1, CCO |
| Gene groups (HGNC) | Ryanodine receptors; Protein phosphatase 1 regulatory subunits |
| Hallmark sets | KRAS_SIGNALING_DN, MYOGENESIS |
| Reactome | 6 pathways, smallest: Ion homeostasis; Stimuli-sensing channels; Cardiac conduction |
| Matched by | ensembl_id |

**Function**, from UniProt [P21817](https://www.uniprot.org/uniprotkb/P21817) (Ryanodine receptor 1):

> Cytosolic calcium-activated calcium channel that mediates the release of Ca(2+) from the sarcoplasmic reticulum into the cytosol and thereby plays a key role in triggering muscle contraction following depolarization of T-tubules. Repeated very high-level exercise increases the open probability of the channel and leads to Ca(2+) leaking into the cytoplasm. Can also mediate the release of Ca(2+) from intracellular stores in neurons, and may thereby promote prolonged Ca(2+) signaling in the brain. …

**Summary**, from NCBI Gene [6261](https://www.ncbi.nlm.nih.gov/gene/6261):

> This gene encodes a ryanodine receptor found in skeletal muscle. The encoded protein functions as a calcium release channel in the sarcoplasmic reticulum but also serves to connect the sarcoplasmic reticulum and transverse tubule. Mutations in this gene are associated with malignant hyperthermia susceptibility, central core disease, and minicore myopathy with external ophthalmoplegia. Alternatively spliced transcripts encoding different isoforms have been described. [provided by RefSeq, Jul …

**Accessions** — [HGNC:10483](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10483) · Entrez [6261](https://www.ncbi.nlm.nih.gov/gene/6261) · UniProt [P21817](https://www.uniprot.org/uniprotkb/P21817) · Ensembl [ENSG00000196218](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196218)

## Data

Gene col 12157: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12157); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12157, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12157]; `tensor/DDL_lfc|DDL_z.npy` [12157]; `embed/gene_vectors.npy` [12157]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12157 or target_col == 12157). Every well: [[RYR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RYR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
