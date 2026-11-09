---
symbol: "UFSP2"
type: "gene"
col: 3080
ensembl_id: "ENSG00000109775"
name: "UFM1 specific peptidase 2"
location: "4q35.1"
module: 41
arm: "+"
pooled_cpm: 23.8
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 10
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# UFSP2

*UFM1 specific peptidase 2* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.34× (z +5.7, q 7e-06, up in 14 of 34 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1573 2.98×; ⚠ cell-cycle shift, explains ~82% of this change).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.588× (z -15.2, q 0e+00, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM167B]] (+0.68, fdr 7e-06), [[LTN1]] (+0.65, fdr 7e-06), [[UFL1]] (+0.65, fdr 1e-05); moves opposite to [[E2F3]] (-0.60, fdr 1e-05), [[GATAD2A]] (-0.60, fdr 1e-05), [[TCF20]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3080.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1573 2.98×; ⚠ cell-cycle shift, explains ~82% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +5.7 | 7e-06 | 14/34 (A549, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.44×** | +3.9 | 0.033 | 14/46 (HOP62, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.13× | +3.6 | 0.057 | 7/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.11 | 14/44 (A-427, NCI-H2030, …) | rises with dose | composition shift |
| [[Verteporfin (drug)]] 5 µM |  | 1.18× | +3.3 | 0.11 | 10/48 (NCI-H2030, BT-474, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.11 | 6/48 (SW480, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.11 | 12/48 (LoVo, SW480, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | 1.17× | +3.1 | 0.13 | 9/46 (A-172, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Terfenadine (drug)]] 5 µM |  | 1.11× | +3.0 | 0.15 | 8/48 (LS 180, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3080.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.588×** | -15.2 | 0e+00 | 37/48 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.579×** | -10.6 | 7e-24 | 33/47 (H4, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.637×** | -8.7 | 4e-16 | 31/47 (C-33 A, HS-578T, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.741×** | -8.5 | 2e-15 | 28/48 (J82, RPMI-7951, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.743×** | -6.0 | 2e-07 | 24/46 (RPMI-7951, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.811×** | -6.0 | 2e-07 | 26/48 (BT-474, SNU-423, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.781×** | -4.8 | 1e-04 | 20/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.804×** | -4.4 | 8e-04 | 19/48 (SNU-423, HT-29, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.797×** | -4.3 | 1e-03 | 19/47 (Hs 766T, SW48, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.839× | -3.5 | 0.023 | 16/48 (LoVo, A498, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.844× | -3.4 | 0.031 | 10/48 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.846× | -3.4 | 0.035 | 16/48 (NCI-H2347, LS 180, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.850× | -3.3 | 0.047 | 9/48 (COLO 205, SHP-77, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.738×** | -3.2 | 0.056 | 6/44 (HS-578T, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | 0.854× | -3.2 | 0.056 | 17/48 (NCI-H460, BT-474, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3080. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 42.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -13.0) |
| [[RPMI-7951 (line)]] | alt | 45.9 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 31.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -9.8) |
| [[A-172 (line)]] | wt | 24.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -9.4) |
| [[A549 (line)]] | wt | 19.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -9.6) |
| [[C-33 A (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.150× (z -10.0) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 32.7 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0818× (z -9.5) |
| [[H4 (line)]] | wt | 27.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0492× (z -16.4) |
| [[HOP62 (line)]] | alt | 23.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -10.0) |
| [[HS-578T (line)]] | alt | 31.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -9.2) |
| [[J82 (line)]] | alt | 21.1 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.401× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 26.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +11.4) ⚠ cell-cycle shift, explains ~82% of this change | — |
| [[NCI-H460 (line)]] | wt | 21.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -9.5) |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -9.2) |
| [[SNU-1 (line)]] | wt | 23.4 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0796× (z -12.4) ⚠ transcription drop |
| [[SW480 (line)]] | alt | 22.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -9.8) |
| [[A-427 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3080), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM167B]] | +0.68 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[LTN1]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[UFL1]] | +0.65 | +0.68 / +0.57 | both halves | 1e-05 | STRING 879 |
| [[LYSMD3]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ABITRAM]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[SKIC3]] | +0.61 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[IFT52]] | +0.61 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[TBC1D23]] | +0.61 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[TMF1]] | +0.60 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[MAP3K13]] | +0.60 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[SAR1B]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[THAP8]] | +0.59 | +0.58 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[E2F3]] | -0.60 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.60 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[TCF20]] | -0.59 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[SNRPB]] | -0.57 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[ZNF710]] | -0.56 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[DOCK9]] | -0.56 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[EPM2A]] | -0.55 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[TLNRD1]] | -0.55 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ITGA2-AS1]] | -0.55 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[ZNF718]] | -0.53 | -0.52 / -0.37 | both halves | 9e-05 |  |
| [[HNRNPAB]] | -0.53 | -0.63 / -0.40 | both halves | 5e-05 |  |
| [[RASSF3]] | -0.53 | -0.46 / -0.58 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises UFSP2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.3, -39.3); signed map (-52.1, 16.7). **Vector** length 91.8, 18.7% of its response variance represented; |z| ≥ 3 in 827 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +3.8 | +2.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.8 | +3.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.5 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.5 | -0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.1 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +1.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +2.2 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -15.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -6.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.4 | -8.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.9 | -4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | UFM1 specific peptidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:185,399,537-185,425,979 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11200; previously C4orf20 |
| Gene groups (HGNC) | UFM1 specific peptidase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUQ7](https://www.uniprot.org/uniprotkb/Q9NUQ7) (Ufm1-specific protease 2):

> Thiol-dependent isopeptidase that specifically cleaves UFM1, a ubiquitin-like modifier protein, from conjugated proteins, such as CD274/PD-L1, CYB5R3, DDRGK1, MRE11, RPL26/uL24, TRIP4 and RPL26/uL24. While it is also able to mediate the processing of UFM1 precursors, a prerequisite for conjugation reactions, UFSP2 mainly acts as a protein deUFMylase that mediates deconjugation of UFM1 from target proteins. Mediates deUFMylation of RPL26/uL24, a critical step to release the UFM1 ribosome E3 …

**Summary**, from NCBI Gene [55325](https://www.ncbi.nlm.nih.gov/gene/55325):

> This gene encodes a highly conserved cysteine protease. The protein cleaves two C-terminal residues from ubiquitin-fold modifier 1, a ubiquitin-like post-translational modifier protein. Activation of ubiquitin-fold modifier 1 by the encoded protein exposes a C-terminal glycine residue that allows interaction with other proteins and transfer to its target protein. An allelic variant of this gene has been associated with Beukes hip dysplasia. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:25640](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25640) · Entrez [55325](https://www.ncbi.nlm.nih.gov/gene/55325) · UniProt [Q9NUQ7](https://www.uniprot.org/uniprotkb/Q9NUQ7) · Ensembl [ENSG00000109775](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109775)

## Data

Gene col 3080: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3080); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3080, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3080]; `tensor/DDL_lfc|DDL_z.npy` [3080]; `embed/gene_vectors.npy` [3080]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3080 or target_col == 3080). Every well: [[UFSP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UFSP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
