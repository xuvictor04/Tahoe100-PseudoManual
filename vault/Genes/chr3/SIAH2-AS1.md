---
symbol: "SIAH2-AS1"
type: "gene"
col: 14398
ensembl_id: "ENSG00000244265"
name: "SIAH2 and CLRN1 antisense RNA 1"
location: "3q25.1"
module: 26
arm: "+"
pooled_cpm: 2.58
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# SIAH2-AS1

*SIAH2 and CLRN1 antisense RNA 1* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 42.3× (z +47.0, q 0e+00, up in 31 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (NCI-H23 0.0634×; ⚠ cell-cycle shift, explains ~18% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H1573 0.0526×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Talc (drug)]] 0.5 µM in 1 line (KATO III 0.0671×); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (KATO III 0.0765×); [[Flutamide (drug)]] 0.5 µM in 1 line (BT-474 0.0549×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIBAR1-DT]] (+0.84, fdr 7e-06), [[CPEB2-DT]] (+0.83, fdr 7e-06), [[PSMD7-DT]] (+0.83, fdr 7e-06); moves opposite to [[COMMD2]] (-0.71, fdr 4e-05), [[ALAD]] (-0.70, fdr 1e-04), [[PAFAH1B3]] (-0.68, fdr 9e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14398.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **42.3×** | +47.0 | 0e+00 | 31/31 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **18.6×** | +24.9 | 0e+00 | 26/26 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **14.5×** | +22.8 | 0e+00 | 32/33 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **4.16×** | +17.9 | 0e+00 | 27/44 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **4.18×** | +12.7 | 8e-35 | 32/37 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.26×** | +10.2 | 2e-22 | 18/30 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.22×** | +10.0 | 2e-21 | 1/2 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.53×** | +7.6 | 2e-12 | 1/2 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.26×** | +7.2 | 3e-11 | 19/38 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.97×** | +6.0 | 1e-07 | 3/10 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +5.7 | 6e-07 | 5/12 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.57×** | +5.6 | 9e-07 | 12/43 (A498, SW480, …) | top dose only | low cells (technical?) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.55×** | +5.5 | 2e-06 | 18/42 (A-172, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +4.5 | 2e-04 | 8/28 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Demeclocycline (drug)]] 5 µM |  | **1.42×** | +4.4 | 5e-04 | 6/42 (RPMI-7951, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.046 | 3/44 (SW480, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14398.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (NCI-H23 0.0634×; ⚠ cell-cycle shift, explains ~18% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H1573 0.0526×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Talc (drug)]] 0.5 µM in 1 line (KATO III 0.0671×); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (KATO III 0.0765×); [[Flutamide (drug)]] 0.5 µM in 1 line (BT-474 0.0549×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.686× | -3.4 | 0.44 | 11/41 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.711× | -3.0 | 0.56 | 7/42 (RKO, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14398. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 4.06 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 46.9× (z +19.0) | — |
| [[KATO III (line)]] | alt | 4.61 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.4× (z +14.0) | [[Talc (drug)]] 0.5 µM 0.0671× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 1.63 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 52.0× (z +15.7) | — |
| [[NCI-H1573 (line)]] | alt | 6.39 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 43.5× (z +19.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0526× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 8.92 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.8× (z +19.1) | [[Belinostat (drug)]] 0.5 µM 0.0634× (z -11.9) ⚠ cell-cycle shift, explains ~18% of this change |
| [[PANC-1 (line)]] | alt | 1.46 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 46.4× (z +17.2) | — |
| [[SW480 (line)]] | alt | 2.01 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 30.6× (z +16.4) | — |
| [[A498 (line)]] | wt | 4.73 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.9× (z +15.7) | — |
| [[BT-474 (line)]] | alt | 11.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.7× (z +12.0) | [[Flutamide (drug)]] 0.5 µM 0.0549× (z -8.8) |
| [[COLO 205 (line)]] | alt | 4.69 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 30.9× (z +13.6) | — |
| [[HOP62 (line)]] | alt | 1.74 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 71.5× (z +16.9) | — |
| [[HT-29 (line)]] | alt | 3.05 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 31.1× (z +13.8) | — |
| [[LoVo (line)]] | wt | 2.77 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 40.3× (z +16.1) | — |
| [[LS 180 (line)]] | wt | 1.59 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 52.1× (z +12.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.63 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 44.2× (z +15.0) | — |
| [[Panc 03.27 (line)]] | alt | 2.49 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 40.5× (z +13.5) | — |
| [[A-172 (line)]] | wt | 2.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 91.2× (z +15.9) | — |
| [[A549 (line)]] | wt | 1.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 38.1× (z +12.6) | — |
| [[AsPC-1 (line)]] | alt | 1.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 88.1× (z +10.1) | — |
| [[C-33 A (line)]] | alt | 3.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 38.6× (z +11.6) | — |
| [[C32 (line)]] | wt | 1.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 79.9× (z +11.7) | — |
| [[CFPAC-1 (line)]] | alt | 2.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 53.8× (z +15.5) | — |
| [[HS-578T (line)]] | alt | 1.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 181× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 1.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 94.8× (z +9.1) | — |
| [[J82 (line)]] | alt | 2.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 33.6× (z +12.9) | — |
| [[NCI-H2030 (line)]] | alt | 1.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 48.4× (z +12.5) | — |
| [[NCI-H2347 (line)]] | alt | 1.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 35.7× (z +14.1) | — |
| [[SNU-423 (line)]] | alt | 1.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 47.4× (z +11.6) | — |
| [[SW1417 (line)]] | alt | 2.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 37.5× (z +13.9) | — |
| [[A-427 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.935 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14398), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIBAR1-DT]] | +0.84 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.83 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.83 | +0.81 / +0.62 | both halves | 7e-06 |  |
| [[MYLK4]] | +0.83 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[SAXO1]] | +0.82 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[LINC00880]] | +0.80 | +0.76 / +0.58 | both halves | 7e-06 |  |
| [[ZFHX2-AS1]] | +0.80 | +0.69 / +0.55 | both halves | 1e-05 | same gene group |
| [[TMEM202-AS1]] | +0.80 | +0.75 / +0.58 | both halves | 7e-06 | same gene group |
| [[INTS6-AS1]] | +0.80 | +0.74 / +0.59 | both halves | 7e-06 | same gene group |
| [[PKN2-AS1]] | +0.80 | +0.74 / +0.54 | both halves | 1e-05 | same gene group |
| [[MALINC1]] | +0.79 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[DENND6A-AS1]] | +0.79 | +0.71 / +0.61 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD2]] | -0.71 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[ALAD]] | -0.70 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[PAFAH1B3]] | -0.68 | -0.51 / -0.37 | both halves | 9e-05 |  |
| [[WRAP73]] | -0.67 | -0.49 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SIAH2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CRPPA]] | B | CRPPA activity lowers SIAH2-AS1's level | lines that do not express CRPPA (5) vs lines expressing it (45) | 1.66× higher at baseline in the lines without CRPPA | 0.060 | ⚠ within organs, on part of the lines; also absent: TBL1X, NLGN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.826). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.3, 19.0); signed map (25.4, -2.4). **Vector** length 70.6, 11.4% of its response variance represented; |z| ≥ 3 in 1,185 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.2 | +47.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +24.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.5 | +12.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.3 | +17.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +22.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +2.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.9 | -3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | SIAH2 and CLRN1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q25.1 — chr3:150,761,937-150,873,554 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously CLRN1-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40526](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40526) · Entrez [105374155](https://www.ncbi.nlm.nih.gov/gene/105374155) · Ensembl [ENSG00000244265](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244265)

## Data

Gene col 14398: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14398); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14398, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14398]; `tensor/DDL_lfc|DDL_z.npy` [14398]; `embed/gene_vectors.npy` [14398]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14398 or target_col == 14398). Every well: [[SIAH2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIAH2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
