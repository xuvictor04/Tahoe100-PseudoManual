---
symbol: "CIBAR1-DT"
type: "gene"
col: 14469
ensembl_id: "ENSG00000246662"
name: "CIBAR1 divergent transcript"
location: "8q22.1"
module: 26
arm: "+"
pooled_cpm: 4.57
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# CIBAR1-DT

*CIBAR1 divergent transcript* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 10.1× (z +32.1, q 0e+00, up in 33 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.188×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.227×; ⚠ cell-cycle shift, explains ~62% of this change); [[Belinostat (drug)]] 5 µM in 1 line (SHP-77 0.242×; ⚠ cell-cycle shift, explains ~44% of this change).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIAH2-AS1]] (+0.84, fdr 7e-06), [[NEB]] (+0.83, fdr 7e-06), [[INTS6-AS1]] (+0.83, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[CLVS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14469.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **10.1×** | +32.1 | 0e+00 | 33/33 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **3.47×** | +17.3 | 0e+00 | 32/43 (A-172, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **4.70×** | +15.2 | 0e+00 | 32/38 (C32, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.87×** | +15.0 | 0e+00 | 24/30 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.74×** | +12.4 | 2e-33 | 28/34 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.31×** | +11.6 | 3e-29 | 22/36 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.29×** | +11.2 | 2e-27 | 2/4 (HOP62, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.94×** | +10.6 | 2e-24 | 8/14 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.80×** | +9.3 | 6e-19 | 2/4 (PANC-1, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.40×** | +8.6 | 5e-16 | 25/41 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +6.5 | 4e-09 | 12/32 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.47×** | +5.3 | 4e-06 | 12/43 (HS-578T, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.0 | 0.002 | 4/16 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +3.7 | 0.007 | 6/41 (C-33 A, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.47×** | +3.6 | 0.012 | 3/42 (SHP-77, A-172, …) | top dose only | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.043 | 4/44 (A498, HS-578T, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.065 | 3/43 (SHP-77, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14469.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.188×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.227×; ⚠ cell-cycle shift, explains ~62% of this change); [[Belinostat (drug)]] 5 µM in 1 line (SHP-77 0.242×; ⚠ cell-cycle shift, explains ~44% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.706× | -3.3 | 0.40 | 6/40 (RPMI-7951, A-427, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.800× | -3.1 | 0.40 | 4/44 (A-172, A498, …) | top dose only |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.737× | -3.0 | 0.40 | 8/36 (SW1417, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14469. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 117 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.188× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 2.84 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 40.4× (z +15.2) | — |
| [[HEC-1-A (line)]] | alt | 2.70 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.91× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 2.85 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.9× (z +13.0) | — |
| [[A-172 (line)]] | wt | 2.31 | 2 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 22.5× (z +11.9) | — |
| [[A498 (line)]] | wt | 2.01 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 29.7× (z +15.3) | — |
| [[LoVo (line)]] | wt | 1.91 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.4× (z +12.2) | — |
| [[LOX-IMVI (line)]] | wt | 2.44 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.4× (z +11.6) | — |
| [[NCI-H2030 (line)]] | alt | 2.85 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +11.6) | — |
| [[PANC-1 (line)]] | alt | 2.79 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.70× (z +12.5) | — |
| [[A549 (line)]] | wt | 2.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 1.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 37.8× (z +8.7) | — |
| [[C32 (line)]] | wt | 4.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 1.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 3.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.1× (z +10.3) | — |
| [[J82 (line)]] | alt | 1.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.6× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 4.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.72× (z +9.7) | — |
| [[NCI-H460 (line)]] | wt | 1.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +11.2) | — |
| [[Panc 03.27 (line)]] | alt | 2.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.6× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 2.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 3.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.9× (z +12.1) | — |
| [[SW1417 (line)]] | alt | 2.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.20× (z +9.0) | — |
| [[SW480 (line)]] | alt | 2.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.63× (z +10.7) | — |
| [[A-427 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14469), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIAH2-AS1]] | +0.84 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[NEB]] | +0.83 | +0.81 / +0.66 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.83 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[ZFHX2-AS1]] | +0.83 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.82 | +0.68 / +0.64 | both halves | 7e-06 | same gene group |
| [[CCDC90B-AS1]] | +0.81 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[DENND6A-AS1]] | +0.81 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[MMADHC-DT]] | +0.81 | +0.72 / +0.51 | both halves | 1e-05 | same gene group |
| [[LINC01090]] | +0.81 | +0.73 / +0.57 | both halves | 9e-06 |  |
| [[PBLD]] | +0.80 | +0.77 / +0.32 | both halves | 2e-04 |  |
| [[PPP1R12A-AS2]] | +0.80 | +0.78 / +0.38 | both halves | 6e-05 |  |
| [[PKN2-AS1]] | +0.80 | +0.76 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CIBAR1-DT's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[DYSF]] | B | DYSF activity lowers CIBAR1-DT's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.29× higher at baseline in the lines without DYSF | 0.089 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent; its own permutation p |
| [[C17orf67]] | C | C17orf67 activity lowers CIBAR1-DT's level | lines that do not express C17orf67 (3) vs lines expressing it (47) | 3.80× higher at baseline in the lines without C17orf67 | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ARHGAP10, IQSEC2, MBOAT2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLVS1]] | C | CIBAR1-DT's natural level weakens CLVS1's drug response | CIBAR1-DT's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.82, reverse -0.46; direction clear | 2e-04 | ⚠ tissue can mimic it; precision caveat |
| [[CHRM5]] | C | CIBAR1-DT's natural level weakens CHRM5's drug response | CIBAR1-DT's natural level across 43 lines (lineage-adjusted; a glimpse) | r -0.79, reverse -0.42; direction clear | 0.002 | ⚠ tissue can mimic it; precision caveat |
| [[LINC02307]] | C | CIBAR1-DT's natural level weakens LINC02307's drug response | CIBAR1-DT's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.55; direction not clear | 0.077 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[MYT1L]] | C | CIBAR1-DT's natural level weakens MYT1L's drug response | CIBAR1-DT's natural level across 36 lines (lineage-adjusted; a glimpse) | r -0.73, reverse -0.56; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.854). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (10.5, 18.7); signed map (26.2, -3.8). **Vector** length 70.8, 11.4% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.5 | +32.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.5 | +15.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.1 | +17.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +15.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +12.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +2.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.3 | -2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -4.0 | -1.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -3.5 | -1.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -1.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | CIBAR1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q22.1 — chr8:93,213,302-93,700,433 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously LINC00535 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43644](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43644) · Entrez [642924](https://www.ncbi.nlm.nih.gov/gene/642924) · Ensembl [ENSG00000246662](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000246662)

## Data

Gene col 14469: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14469); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14469, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14469]; `tensor/DDL_lfc|DDL_z.npy` [14469]; `embed/gene_vectors.npy` [14469]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14469 or target_col == 14469). Every well: [[CIBAR1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CIBAR1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
