---
symbol: "OOEP"
type: "gene"
col: 12801
ensembl_id: "ENSG00000203907"
name: "oocyte expressed protein"
location: "6q13"
module: 21
arm: "+"
pooled_cpm: 6.58
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# OOEP

*oocyte expressed protein* — 6q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.76× (z +19.3, q 0e+00, up in 37 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (Panc 03.27 0.0842×); [[Roxadustat (drug)]] 0.5 µM in 1 line (HT-29 0.0531×); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H2030 0.116×; ⚠ cell-cycle shift, explains ~0% of this change); [[Estrone sulfate (potassium) (drug)]] 0.5 µM in 1 line (A549 0.0603×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM184B]] (+0.80, fdr 7e-06), [[SPATA1]] (+0.80, fdr 7e-06), [[EIF3J-DT]] (+0.80, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KLRD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12801.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.76×** | +19.3 | 0e+00 | 37/40 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.40×** | +12.1 | 2e-31 | 11/11 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +8.4 | 6e-15 | 21/34 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +8.4 | 6e-15 | 21/38 (LoVo, SW 900, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.23×** | +8.2 | 2e-14 | 15/24 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.33×** | +8.0 | 8e-14 | 11/16 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.17×** | +8.0 | 1e-13 | 29/44 (NCI-H23, LoVo, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +6.3 | 3e-08 | 20/46 (NCI-H2347, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +5.8 | 3e-07 | 19/28 (SW1417, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.4 | 5e-06 | 17/37 (RKO, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +5.2 | 9e-06 | 14/36 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +5.0 | 2e-05 | 14/27 (Panc 03.27, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.002 | 15/48 (HOP62, HS-578T, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +4.0 | 0.002 | 10/43 (J82, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +3.9 | 0.004 | 7/43 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.012 | 13/46 (SW1417, NCI-H460, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.030 | 13/38 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.051 | 9/42 (Panc 03.27, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.081 | 5/44 (NCI-H23, NCI-H1792, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +2.9 | 0.082 | 6/45 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12801.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (Panc 03.27 0.0842×); [[Roxadustat (drug)]] 0.5 µM in 1 line (HT-29 0.0531×); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H2030 0.116×; ⚠ cell-cycle shift, explains ~0% of this change); [[Estrone sulfate (potassium) (drug)]] 0.5 µM in 1 line (A549 0.0603×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Roxadustat (drug)]] 5 µM |  | 0.718× | -3.3 | 0.36 | 13/44 (RKO, HOP62, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -3.2 | 0.36 | 11/48 (HEC-1-A, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12801. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 4.52 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.98× (z +10.4) | — |
| [[LoVo (line)]] | wt | 13.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +13.2) | — |
| [[NCI-H23 (line)]] | alt | 6.45 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.86× (z +10.5) | — |
| [[NCI-H2347 (line)]] | alt | 7.57 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 6.38 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.15× (z +10.7) | [[Bosentan (hydrate) (drug)]] 5 µM 0.0842× (z -9.8) |
| [[A498 (line)]] | wt | 3.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.29× (z +12.3) | — |
| [[A549 (line)]] | wt | 3.49 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0603× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 3.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 3.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.63× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 3.44 | 0 | 1 | — | [[Roxadustat (drug)]] 0.5 µM 0.0531× (z -9.0) |
| [[J82 (line)]] | alt | 4.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +9.2) | — |
| [[KATO III (line)]] | alt | 23.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 4.95 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.116× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 6.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.74× (z +11.1) | — |
| [[A-172 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12801), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM184B]] | +0.80 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[SPATA1]] | +0.80 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[EIF3J-DT]] | +0.80 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[ZNF451-AS1]] | +0.78 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.76 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[PSMD14-DT]] | +0.76 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[DENND6A-AS1]] | +0.76 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[HSPA2-AS1]] | +0.76 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[IL12RB2]] | +0.75 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[TBCE-1]] | +0.75 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[SPEN-AS1]] | +0.74 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[LRRC8C-DT]] | +0.73 | +0.60 / +0.57 | both halves | 8e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLRD1]] | B | KLRD1 activity lowers OOEP's level | lines that do not express KLRD1 (8) vs lines expressing it (42) | 1.80× higher at baseline in the lines without KLRD1 | 0.020 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers OOEP's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KLRK1-AS1]] | B | KLRK1-AS1 activity lowers OOEP's level | lines that do not express KLRK1-AS1 (11) vs lines expressing it (39) | 1.46× higher at baseline in the lines without KLRK1-AS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |
| [[SPACA6]] | C | SPACA6 activity lowers OOEP's level | lines that do not express SPACA6 (3) vs lines expressing it (47) | 2.16× higher at baseline in the lines without SPACA6 | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLE6, ZNF14, ZNF547 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.751). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.9, 23.6); signed map (30.3, -0.0). **Vector** length 56.1, 8.07% of its response variance represented; |z| ≥ 3 in 841 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +19.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +8.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.9 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +8.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +4.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +1.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -0.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -0.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.1 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | oocyte expressed protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q13 — chr6:73,368,555-73,395,133 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Em:AC019205.2, KHDC2; previously C6orf156 |
| Gene groups (HGNC) | Subcortical maternal complex |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NGQ2](https://www.uniprot.org/uniprotkb/A6NGQ2) (Oocyte-expressed protein homolog):

> Component of the subcortical maternal complex (SCMC), a multiprotein complex that plays a key role in early embryonic development (By similarity). The SCMC complex is a structural constituent of cytoplasmic lattices, which consist in fibrous structures found in the cytoplasm of oocytes and preimplantation embryos. They are required to store maternal proteins critical for embryonic development, such as ribosomal proteins, cytoskeletal tubulins and proteins controlling epigenetic reprogramming of …

**Summary**, from NCBI Gene [441161](https://www.ncbi.nlm.nih.gov/gene/441161):

> Predicted to enable RNA binding activity. Predicted to be a structural constituent of cytoplasmic lattice. Predicted to be involved in several processes, including cytoskeleton organization; positive regulation of double-strand break repair via homologous recombination; and protein storage. Predicted to act upstream of or within several processes, including embryo implantation; in utero embryonic development; and protein phosphorylation. Located in cytoplasm and nucleus. Part of subcortical …

**Accessions** — [HGNC:21382](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21382) · Entrez [441161](https://www.ncbi.nlm.nih.gov/gene/441161) · UniProt [A6NGQ2](https://www.uniprot.org/uniprotkb/A6NGQ2) · Ensembl [ENSG00000203907](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203907)

## Data

Gene col 12801: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12801); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12801, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12801]; `tensor/DDL_lfc|DDL_z.npy` [12801]; `embed/gene_vectors.npy` [12801]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12801 or target_col == 12801). Every well: [[OOEP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OOEP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
