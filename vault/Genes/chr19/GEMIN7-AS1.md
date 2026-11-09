---
symbol: "GEMIN7-AS1"
type: "gene"
col: 15547
ensembl_id: "ENSG00000267348"
name: "GEMIN7 antisense RNA 1"
location: "19q13.32"
module: 21
arm: "+"
pooled_cpm: 3.06
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# GEMIN7-AS1

*GEMIN7 antisense RNA 1* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 9.73× (z +34.9, q 0e+00, up in 34 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (A-427 0.0641×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C2CD5-AS1]] (+0.82, fdr 7e-06), [[ADNP-AS1]] (+0.80, fdr 7e-06), [[CTDSPL2-DT]] (+0.79, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15547.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **9.73×** | +34.9 | 0e+00 | 34/34 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.60×** | +23.6 | 0e+00 | 5/5 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **8.12×** | +22.7 | 0e+00 | 18/18 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.78×** | +17.6 | 0e+00 | 7/8 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.85×** | +11.4 | 8e-28 | 35/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.71×** | +10.4 | 2e-23 | 22/32 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +9.9 | 3e-21 | 21/37 (SW 900, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.30×** | +9.0 | 1e-17 | 26/45 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.25×** | +8.5 | 2e-15 | 10/19 (NCI-H2030, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.66×** | +7.8 | 4e-13 | 15/44 (PANC-1, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +7.4 | 1e-11 | 16/26 (NCI-H460, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +6.8 | 4e-10 | 20/35 (HT-29, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +6.8 | 6e-10 | 19/46 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +6.2 | 2e-08 | 20/45 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.97×** | +3.8 | 0.005 | 1/4 (A498) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +3.7 | 0.006 | 6/42 (BT-474, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.008 | 7/42 (NCI-H2030, NCI-H2347, …) | two highest doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.011 | 5/44 (C32, BT-474, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.012 | 4/39 (PANC-1, NCI-H2347, …) | top dose only | position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.015 | 5/37 (C-33 A, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.025 | 5/36 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15547.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (A-427 0.0641×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.875× | -5.3 | 7e-05 | 21/47 (LS 180, A498, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.727× | -3.3 | 0.25 | 5/46 (RPMI-7951, AN3 CA, …) | top dose only |  |
| [[Rifaximin (drug)]] 5 µM |  | 0.749× | -3.0 | 0.47 | 7/42 (A-427, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15547. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 5.45 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +15.4) | — |
| [[PANC-1 (line)]] | alt | 2.47 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 26.7× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.92× (z +12.6) | — |
| [[HEC-1-A (line)]] | alt | 6.40 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +14.4) | — |
| [[NCI-H2030 (line)]] | alt | 4.19 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 30.8× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +8.8) | — |
| [[SW480 (line)]] | alt | 3.14 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +14.4) | — |
| [[A-172 (line)]] | wt | 2.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.09× (z +8.7) | — |
| [[A-427 (line)]] | wt | 3.28 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0641× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 2.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +10.7) | — |
| [[A549 (line)]] | wt | 3.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.6× (z +11.9) | — |
| [[BT-474 (line)]] | alt | 6.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 8.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.20× (z +8.9) | — |
| [[C32 (line)]] | wt | 3.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 2.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.54× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 3.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.68× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 4.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.0× (z +14.5) | — |
| [[KATO III (line)]] | alt | 3.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +10.5) | — |
| [[LoVo (line)]] | wt | 2.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.5× (z +12.0) | — |
| [[LOX-IMVI (line)]] | wt | 2.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 2.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.7× (z +11.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.82× (z +9.7) | — |
| [[NCI-H460 (line)]] | wt | 2.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.01× (z +10.9) | — |
| [[RPMI-7951 (line)]] | alt | 4.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 2.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +9.7) | — |
| [[SW 900 (line)]] | alt | 2.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 3.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.96× (z +9.8) | — |
| [[AN3 CA (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15547), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2CD5-AS1]] | +0.82 | +0.68 / +0.82 | both halves | 7e-06 | same gene group |
| [[ADNP-AS1]] | +0.80 | +0.72 / +0.73 | both halves | 7e-06 | same gene group |
| [[CTDSPL2-DT]] | +0.79 | +0.68 / +0.79 | both halves | 7e-06 |  |
| [[CNGB3]] | +0.78 | +0.65 / +0.80 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.78 | +0.66 / +0.79 | both halves | 7e-06 | same gene group |
| [[PAXBP1-AS1]] | +0.77 | +0.67 / +0.79 | both halves | 7e-06 | same gene group |
| [[SPATA21]] | +0.75 | +0.61 / +0.80 | both halves | 7e-06 |  |
| [[HRG-AS1]] | +0.75 | +0.64 / +0.75 | both halves | 7e-06 | same gene group |
| [[MROH8]] | +0.74 | +0.59 / +0.81 | both halves | 7e-06 |  |
| [[HNRNPK-AS1]] | +0.74 | +0.68 / +0.60 | both halves | 7e-06 | same gene group |
| [[FLJ40194]] | +0.74 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[HSPA2-AS1]] | +0.73 | +0.64 / +0.75 | both halves | 7e-06 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GEMIN7-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.800). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.1, 26.7); signed map (33.7, 3.5). **Vector** length 51.3, 6.39% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +34.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +22.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +23.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +17.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +6.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +3.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +1.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -5.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.9 | -0.4 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -0.8 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | GEMIN7 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.32 — chr19:45,076,510-45,092,635 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53773](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53773) · Entrez [105372419](https://www.ncbi.nlm.nih.gov/gene/105372419) · Ensembl [ENSG00000267348](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267348)

## Data

Gene col 15547: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15547); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15547, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15547]; `tensor/DDL_lfc|DDL_z.npy` [15547]; `embed/gene_vectors.npy` [15547]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15547 or target_col == 15547). Every well: [[GEMIN7-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GEMIN7-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
