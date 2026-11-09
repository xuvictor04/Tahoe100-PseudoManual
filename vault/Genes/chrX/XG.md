---
symbol: "XG"
type: "gene"
col: 4520
ensembl_id: "ENSG00000124343"
name: "Xg glycoprotein (Xg blood group)"
location: "Xp22.33"
module: 39
arm: "+"
pooled_cpm: 2.48
n_lines_expressing: 45
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 10
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# XG

*Xg glycoprotein (Xg blood group)* — Xp22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.60× (z +11.7, q 7e-29, up in 2 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.09× (z +10.3, q 2e-22, up in 20 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 0.0479×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0499×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPYS]] (+0.83, fdr 7e-06), [[FNDC7]] (+0.82, fdr 7e-06), [[IMPA1P1]] (+0.81, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 10 go from it, the strongest it → [[CCDC181]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4520.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.60×** | +11.7 | 7e-29 | 2/3 (NCI-H2030, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.09×** | +10.3 | 2e-22 | 20/25 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.73×** | +9.1 | 1e-17 | 2/4 (NCI-H2030, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.88×** | +8.7 | 3e-16 | 5/14 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.67×** | +6.3 | 3e-08 | 9/29 (A-172, SW480, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +6.0 | 2e-07 | 9/17 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.73×** | +5.0 | 5e-05 | 6/38 (A-172, NCI-H460, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **2.05×** | +4.6 | 3e-04 | 11/40 (HS-578T, Hs 766T, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +4.6 | 3e-04 | 5/26 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +3.8 | 0.009 | 2/10 (NCI-H460, HS-578T) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 1.69× | +3.1 | 0.10 | 1/17 (SW480) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.64× | +3.1 | 0.10 | 3/14 (NCI-H460, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.65× | +3.0 | 0.10 | 3/30 (A549, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4520.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 0.0479×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0499×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.560× | -3.5 | 0.12 | 7/23 (NCI-H1573, HS-578T, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | 0.581× | -3.5 | 0.12 | 9/30 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.598× | -3.3 | 0.14 | 11/39 (NCI-H1573, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); composition shift |
| [[Eplerenone (drug)]] 0.05 µM |  | 0.575× | -3.3 | 0.14 | 6/31 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Anethole trithione (drug)]] 5 µM |  | 0.702× | -3.2 | 0.14 | 3/40 (COLO 205, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 0.05 µM |  | 0.600× | -3.0 | 0.23 | 4/32 (A549, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4520. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 3.28 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 0.0499× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0479× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.793 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.726 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.877 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.872 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.862 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.912 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.749 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.884 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4520), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPYS]] | +0.83 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.82 | +0.75 / +0.79 | both halves | 7e-06 |  |
| [[IMPA1P1]] | +0.81 | +0.73 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[HPX]] | +0.81 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[TRIM72]] | +0.80 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[OIT3]] | +0.80 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[GARIN1B]] | +0.79 | +0.68 / +0.79 | both halves | 7e-06 |  |
| [[USP50]] | +0.78 | +0.68 / +0.79 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.77 | +0.70 / +0.80 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.77 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[LINC00393]] | +0.76 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[AXDND1]] | +0.76 | +0.64 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers XG's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ADGRG7]] | B | ADGRG7 activity raises XG's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 2.20× lower at baseline in the lines without ADGRG7 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172 |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC181]] | B | XG activity lowers CCDC181's level | lines that do not express XG (5) vs lines expressing it (45) | 1.68× higher at baseline in the lines without XG | 0.016 | ⚠ within organs, on part of the lines; also absent: TXNRD3, FSCN1, ELK3; maybe low, not absent |
| [[MSANTD1]] | B | XG activity raises MSANTD1's level | lines that do not express XG (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without XG | 0.019 | ⚠ within organs, on part of the lines; also absent: TXNRD3, FSCN1, ELK3; maybe low, not absent |
| [[C21orf91-OT1]] | B | XG activity raises C21orf91-OT1's level | lines that do not express XG (5) vs lines expressing it (45) | 2.02× lower at baseline in the lines without XG | 0.020 | ⚠ within organs, on part of the lines; also absent: TXNRD3, FSCN1, ELK3; maybe low, not absent |
| [[PILRA]] | B | XG activity raises PILRA's level | lines that do not express XG (5) vs lines expressing it (45) | 2.16× lower at baseline in the lines without XG | 0.022 | ⚠ within organs, on part of the lines; also absent: TXNRD3, FSCN1, ELK3; maybe low, not absent |
| [[SLC6A13]] | B | XG activity raises SLC6A13's level | lines that do not express XG (5) vs lines expressing it (45) | 2.08× lower at baseline in the lines without XG | 0.024 | ⚠ within organs, on part of the lines; also absent: TXNRD3, FSCN1, ELK3; maybe low, not absent |
| [[NLGN3]] | B | XG activity raises NLGN3's level | lines that do not express XG (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without XG | 0.069 | ⚠ within organs, on part of the lines; also absent: TXNRD3, FSCN1, ELK3; maybe low, not absent |
| [[ADORA1]] | B | XG activity raises ADORA1's level | lines that do not express XG (5) vs lines expressing it (45) | 2.21× lower at baseline in the lines without XG | 0.070 | ⚠ within organs, on part of the lines; also absent: TXNRD3, FSCN1, ELK3; maybe low, not absent |
| [[LINC02936]] | B | XG activity raises LINC02936's level | lines that do not express XG (5) vs lines expressing it (45) | 1.81× lower at baseline in the lines without XG | 0.078 | ⚠ within organs, on part of the lines; also absent: TXNRD3, FSCN1, ELK3; maybe low, not absent |
| [[VWCE]] | B | XG activity raises VWCE's level | lines that do not express XG (5) vs lines expressing it (45) | 1.74× lower at baseline in the lines without XG | 0.079 | ⚠ within organs, on part of the lines; also absent: TXNRD3, FSCN1, ELK3; maybe low, not absent |
| [[CPNE9]] | B | XG activity raises CPNE9's level | lines that do not express XG (5) vs lines expressing it (45) | 1.48× lower at baseline in the lines without XG | 0.097 | ⚠ within organs, on part of the lines; also absent: TXNRD3, FSCN1, ELK3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.799). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.7, -15.1); signed map (17.5, 10.5). **Vector** length 51.1, 7.73% of its response variance represented; |z| ≥ 3 in 814 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +5.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +4.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -2.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.7 | -3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | Xg glycoprotein (Xg blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.33 — chrX:2,752,040-2,816,500 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PBDX |
| Gene groups (HGNC) | Blood group antigens; Pseudoautosomal region 1 |
| Matched by | ensembl_id |

UniProt [P55808](https://www.uniprot.org/uniprotkb/P55808) carries no function annotation.

**Summary**, from NCBI Gene [7499](https://www.ncbi.nlm.nih.gov/gene/7499):

> This gene encodes the XG blood group antigen, and is located at the pseudoautosomal boundary on the short (p) arm of chromosome X. The three 5' exons reside in the pseudoautosomal region and the remaining exons within the X-specific end. A truncated copy of this gene is found on the Y chromosome at the pseudoautosomal boundary. It is transcribed, but not expected to make a Y-chromosome specific gene product. Alternatively spliced transcript variants encoding different isoforms have been found …

**Accessions** — [HGNC:12806](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12806) · Entrez [7499](https://www.ncbi.nlm.nih.gov/gene/7499) · UniProt [P55808](https://www.uniprot.org/uniprotkb/P55808) · Ensembl [ENSG00000124343](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124343)

## Data

Gene col 4520: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4520); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4520, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4520]; `tensor/DDL_lfc|DDL_z.npy` [4520]; `embed/gene_vectors.npy` [4520]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4520 or target_col == 4520). Every well: [[XG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
